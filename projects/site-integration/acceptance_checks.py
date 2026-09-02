import os, re, glob, sys, html, urllib.parse
root = "/Users/steinanf/git/TrinityMetrics"
spec = open(f"{root}/projects/site-integration/specification.qmd", encoding="utf-8").read()

print("=== Check 1 & 2: inventory dispositions ===")
rows = [l for l in spec.splitlines() if re.match(r"^\| \d+ \|", l) and len(l.split("|")) == 10]
disp = {}
bad = []
for l in rows:
    c = [x.strip() for x in l.split("|")]
    num, d, note = c[1], c[6], c[8] if len(c) > 8 else ""
    key = d.replace("✅", "").strip()
    disp[key] = disp.get(key, 0) + 1
    if not key: bad.append(num)
    if key == "DROP" and len(note) < 10: bad.append(f"{num} (DROP, no reason)")
print("rows:", len(rows), "dispositions:", disp)
print("rows missing a disposition or a DROP reason:", bad or "none")
print("sum of dispositions == row count:", sum(disp.values()) == len(rows) == 30)

print("\n=== Check 3: internal links in docs/ ===")
broken = []
n = 0
for f in glob.glob(f"{root}/docs/**/*.html", recursive=True):
    txt = open(f, encoding="utf-8", errors="ignore").read()
    for href in re.findall(r'(?:href|src)="([^"]+)"', txt):
        href = html.unescape(href)
        if re.match(r"^(https?:|mailto:|data:|#|//|javascript:)", href) or not href.strip():
            continue
        p = urllib.parse.unquote(href.split("#")[0].split("?")[0])
        if not p: continue
        n += 1
        t = os.path.normpath(os.path.join(os.path.dirname(f), p))
        if not os.path.exists(t):
            broken.append((os.path.relpath(f, root), href))
print("internal links checked:", n)
print("broken:", len(broken))
for b in sorted(set(broken))[:25]: print("   ", b[0], "->", b[1])

print("\n=== Check 5: resources coverage ===")
qy = open(f"{root}/_quarto.yml", encoding="utf-8").read()
res = re.search(r"resources:\n((?:\s+- .*\n)+)", qy).group(1)
print("resources: block ->", [l.strip("- \n") for l in res.strip().splitlines()])
missing = []
for f in glob.glob(f"{root}/docs/**/*.html", recursive=True):
    txt = open(f, encoding="utf-8", errors="ignore").read()
    for href in re.findall(r'href="([^"]+\.(?:pdf|docx|png|jpg|svg))"', txt):
        if href.startswith("http"): continue
        t = os.path.normpath(os.path.join(os.path.dirname(f), urllib.parse.unquote(href)))
        if not os.path.exists(t): missing.append((os.path.relpath(f, root), href))
print("referenced asset files missing from docs/:", missing or "none")
