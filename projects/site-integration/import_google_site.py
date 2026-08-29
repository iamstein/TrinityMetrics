#!/usr/bin/env python3
"""Turn a Google Takeout export of a Google Site into inventory rows and .qmd drafts.

Two subcommands, both reading an unzipped Takeout export directory:

    python3 import_google_site.py inventory EXPORT_DIR
    python3 import_google_site.py convert   EXPORT_DIR --out OUT_DIR

`inventory` prints the Markdown rows for Section 5 of specification.qmd: one row
per page and one per file, with the disposition columns left blank to fill in.

`convert` writes one .qmd draft per page. Site chrome that repeats across pages
(the navigation menu, the footer) is detected by frequency and dropped, so no
Google Sites class names are hard-coded and the script does not break when
Google changes them.

Standard library only, so it runs anywhere python3 does. The drafts it writes
are drafts: check every one against the live page before committing it.
"""

import argparse
import html
import os
import re
import sys
from collections import Counter
from html.parser import HTMLParser

DEFAULT_BASE_URL = "https://sites.google.com/site/andrewsteinphd"

PAGE_EXTS = {".html", ".htm"}
SKIP_CONTENT = {"script", "style", "noscript", "head", "title", "meta", "link"}
HEADINGS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5, "h6": 6}
BLOCK_TAGS = {
    "p", "div", "section", "article", "header", "footer", "nav", "main",
    "ul", "ol", "li", "table", "tr", "blockquote", "pre", "hr", "br",
} | set(HEADINGS)

# A block appearing on at least this fraction of pages is site chrome.
BOILERPLATE_FRACTION = 0.6


class Block:
    """One block-level piece of a page: a heading, paragraph, list item or row."""

    def __init__(self, kind, text, level=0):
        self.kind = kind
        self.text = text
        self.level = level

    def key(self):
        return (self.kind, self.level, self.text.strip())

    def render(self):
        text = self.text.strip()
        if self.kind == "heading":
            return "#" * self.level + " " + text
        if self.kind == "list":
            return "  " * max(0, self.level - 1) + "- " + text
        if self.kind == "quote":
            return "> " + text
        if self.kind == "pre":
            return "```\n" + self.text.rstrip() + "\n```"
        if self.kind == "rule":
            return "---"
        if self.kind in ("row", "sep"):
            return "| " + " | ".join(c.strip() for c in self.text.split("\x1f")) + " |"
        return text


class PageParser(HTMLParser):
    """Convert the subset of HTML a Google Site emits into Markdown blocks."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.buf = []
        self.skip_depth = 0
        self.list_depth = 0
        self.in_quote = False
        self.in_pre = False
        self.cells = None
        self.title = None
        self._in_title = False
        self._in_anchor = 0
        self._table_row = 0
        self.links = []

    # -- buffer handling ---------------------------------------------------

    def _flush(self, kind="para", level=0):
        text = "".join(self.buf)
        self.buf = []
        text = re.sub(r"[ \t]+", " ", text).strip()
        if text:
            self.blocks.append(Block(kind, text, level))

    def _flush_item(self):
        """Close whatever is buffered, as a list item if a list is open."""
        if self.list_depth:
            self._flush("list", self.list_depth)
        else:
            self._flush()

    def _emit(self, kind, text, level=0):
        self.blocks.append(Block(kind, text, level))

    # -- parser callbacks --------------------------------------------------

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in SKIP_CONTENT:
            if tag == "title":
                self._in_title = True
            else:
                self.skip_depth += 1
            return
        if self.skip_depth:
            return

        if tag in HEADINGS:
            self._flush()
        elif tag == "li":
            self._flush_item()
            self.list_depth = max(1, self.list_depth)
        elif tag in ("ul", "ol"):
            # A nested list opens while its parent item's text is still buffered.
            self._flush_item()
            self.list_depth += 1
        elif tag == "blockquote":
            self._flush()
            self.in_quote = True
        elif tag == "pre":
            self._flush()
            self.in_pre = True
        elif tag == "table":
            self._flush()
            self._table_row = 0
        elif tag == "tr":
            self.cells = []
        elif tag in ("td", "th"):
            self.buf = []
        elif tag == "hr":
            self._flush()
            self._emit("rule", "")
        elif tag == "br":
            self.buf.append("  \n")
        elif tag == "a":
            href = attrs.get("href", "")
            if href:
                self.links.append(href)
                self.buf.append("\x02" + href + "\x03")
            self._in_anchor = self._in_anchor + 1 if href else self._in_anchor
        elif tag == "img":
            src = attrs.get("src", "")
            alt = attrs.get("alt", "")
            if src:
                self.links.append(src)
                self._flush()
                self._emit("para", f"![{alt}]({src})")
        elif tag in ("strong", "b"):
            self.buf.append("**")
        elif tag in ("em", "i"):
            self.buf.append("*")
        elif tag == "code" and not self.in_pre:
            self.buf.append("`")
        elif tag in BLOCK_TAGS:
            self._flush()

    def handle_endtag(self, tag):
        if tag in SKIP_CONTENT:
            if tag == "title":
                self._in_title = False
            elif self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return

        if tag == "a":
            if self._in_anchor:
                self.buf.append("\x04")
                self._in_anchor -= 1
        elif tag in HEADINGS:
            self._flush("heading", HEADINGS[tag])
        elif tag == "li":
            self._flush("list", max(1, self.list_depth))
        elif tag in ("ul", "ol"):
            self._flush()
            self.list_depth = max(0, self.list_depth - 1)
        elif tag == "blockquote":
            self._flush("quote")
            self.in_quote = False
        elif tag == "pre":
            self._flush("pre")
            self.in_pre = False
        elif tag in ("td", "th"):
            if self.cells is not None:
                self.cells.append("".join(self.buf).strip())
                self.buf = []
        elif tag == "tr":
            if self.cells:
                self._emit("row", "\x1f".join(self.cells))
                self._table_row += 1
                if self._table_row == 1:
                    self._emit("sep", "\x1f".join("---" for _ in self.cells))
            self.cells = None
        elif tag in ("strong", "b"):
            self.buf.append("**")
        elif tag in ("em", "i"):
            self.buf.append("*")
        elif tag == "code" and not self.in_pre:
            self.buf.append("`")
        elif tag in BLOCK_TAGS:
            self._flush("quote" if self.in_quote else "para")

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data
            return
        if self.skip_depth:
            return
        self.buf.append(data if self.in_pre else data.replace("\n", " "))

    def close(self):
        super().close()
        self._flush()


def resolve_links(text):
    """Turn the \\x02href\\x03 markers left by the parser into Markdown links."""
    out = []
    pos = 0
    for match in re.finditer("\x02(.*?)\x03(.*?)(?:\x04|$)", text, re.S):
        out.append(text[pos:match.start()])
        href, label = match.group(1), match.group(2)
        label = label.strip()
        out.append(f"[{label}]({href})" if label else f"<{href}>")
        pos = match.end()
    out.append(text[pos:])
    return re.sub(r"[\x02\x03\x04]", "", "".join(out))


def parse_page(path):
    parser = PageParser()
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        parser.feed(handle.read())
    parser.close()
    for block in parser.blocks:
        block.text = resolve_links(block.text)
    title = html.unescape((parser.title or "").strip())
    if not title:
        for block in parser.blocks:
            if block.kind == "heading":
                title = block.text
                break
    return title, parser.blocks, parser.links


def walk(export_dir):
    """Return (pages, files) as lists of paths relative to export_dir, sorted."""
    pages, files = [], []
    for root, dirnames, filenames in os.walk(export_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in filenames:
            if name.startswith("."):
                continue
            rel = os.path.relpath(os.path.join(root, name), export_dir)
            ext = os.path.splitext(name)[1].lower()
            (pages if ext in PAGE_EXTS else files).append(rel)
    return sorted(pages), sorted(files)


def old_url(base_url, rel):
    """Guess the live URL for an exported path. Check these against the site."""
    path = rel.replace(os.sep, "/")
    for ext in PAGE_EXTS:
        if path.lower().endswith(ext):
            path = path[: -len(ext)]
            break
    if path.endswith("/index"):
        path = path[: -len("/index")]
    return base_url.rstrip("/") + "/" + path.lstrip("/")


def escape_cell(text):
    return text.replace("|", "\\|").replace("\n", " ").strip()


def cmd_inventory(args):
    pages, files = walk(args.export_dir)
    if not pages and not files:
        sys.exit(f"No files found under {args.export_dir}")

    file_set = {f.replace(os.sep, "/") for f in files}
    rows = []
    for rel in pages:
        title, _blocks, links = parse_page(os.path.join(args.export_dir, rel))
        attached = sorted(
            {
                os.path.basename(link.split("?")[0])
                for link in links
                if any(
                    os.path.basename(link.split("?")[0]) == os.path.basename(f)
                    for f in file_set
                )
            }
        )
        rows.append(
            (
                f"`{old_url(args.base_url, rel)}`",
                escape_cell(title) or "*(untitled)*",
                "page",
                ", ".join(f"`{name}`" for name in attached) or "---",
            )
        )
    for rel in files:
        rows.append(
            (
                f"`{old_url(args.base_url, rel)}`",
                f"`{os.path.basename(rel)}`",
                "file",
                "---",
            )
        )

    print("| # | Old URL | Title | Kind | Files on it | Disposition | Lands at | Reason / note |")
    print("|---|---|---|---|---|---|---|---|")
    for index, (url, title, kind, attached) in enumerate(rows, start=1):
        print(f"| {index} | {url} | {title} | {kind} | {attached} |  |  |  |")
    print()
    print(f"<!-- {len(rows)} rows: {len(pages)} pages, {len(files)} files. -->")
    print("<!-- Record this count in Section 5; acceptance check 2 reads it. -->")


def slugify(text, fallback):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or fallback


def yaml_quote(text):
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def cmd_convert(args):
    pages, _files = walk(args.export_dir)
    if not pages:
        sys.exit(f"No .html pages found under {args.export_dir}")

    parsed = {}
    for rel in pages:
        parsed[rel] = parse_page(os.path.join(args.export_dir, rel))

    # Site chrome is whatever repeats across most pages.
    counts = Counter()
    for _title, blocks, _links in parsed.values():
        counts.update({block.key() for block in blocks})
    threshold = max(2, int(len(pages) * BOILERPLATE_FRACTION))
    chrome = {key for key, count in counts.items() if count >= threshold} if len(pages) >= 3 else set()

    os.makedirs(args.out, exist_ok=True)
    written = []
    for rel, (title, blocks, _links) in parsed.items():
        body = [b for b in blocks if b.key() not in chrome]
        # Drop a leading H1 that only repeats the title.
        if body and body[0].kind == "heading" and body[0].text.strip() == title.strip():
            body = body[1:]

        name = slugify(os.path.splitext(os.path.basename(rel))[0], "page")
        if name == "index":
            name = slugify(os.path.basename(os.path.dirname(rel)) or "home", "home")
        out_path = os.path.join(args.out, name + ".qmd")

        lines = [
            "---",
            f"title: {yaml_quote(title or name)}",
            'description: ""',
            "toc: false",
            "---",
            "",
            "<!-- Imported draft. Source: " + rel.replace(os.sep, "/") + " -->",
            "<!-- Old URL: " + old_url(args.base_url, rel) + " -->",
            "<!-- Check against the live page, fix links and file paths, then delete these comments. -->",
            "",
        ]
        # List items and table rows must stay contiguous; everything else gets
        # a blank line around it.
        previous = None
        for block in body:
            grouped = previous in ("list", "row", "sep") and block.kind in ("list", "row", "sep")
            if previous is not None and not grouped:
                lines.append("")
            lines.append(block.render())
            previous = block.kind
        lines.append("")
        with open(out_path, "w", encoding="utf-8") as handle:
            handle.write("\n".join(lines).rstrip() + "\n")
        written.append((out_path, len(body)))

    for path, count in sorted(written):
        print(f"{path}  ({count} blocks)")
    print(f"\n{len(written)} drafts written to {args.out}/", file=sys.stderr)
    if chrome:
        print(f"{len(chrome)} repeated blocks dropped as site chrome.", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL,
                        help="Live site root, used to reconstruct old URLs.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_inv = sub.add_parser("inventory", help="Print the Section 5 table rows.")
    p_inv.add_argument("export_dir")
    p_inv.set_defaults(func=cmd_inventory)

    p_con = sub.add_parser("convert", help="Write one .qmd draft per page.")
    p_con.add_argument("export_dir")
    p_con.add_argument("--out", required=True, help="Directory for the drafts.")
    p_con.set_defaults(func=cmd_convert)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
