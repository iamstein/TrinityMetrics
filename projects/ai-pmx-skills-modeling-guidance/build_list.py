"""Build the PMx Skills Index pages from the latest monthly data file.

Reads list/YYYY-MM.yml (the newest one) and writes:
  list/tool.yml, list/task.yml          ranked skills, for curated-list.qmd
  list/unproven.yml                     skills with no evidence of use, not ranked
  list/evaluation.yml                   evaluation resources, not ranked
  curated-list-evidence.qmd                          the evidence behind every score

The monthly run calls this after writing the data file; nothing runs at render
time. Usage: python3 build_list.py
"""

from pathlib import Path

import yaml

HERE = Path(__file__).parent
FLAG_ICON = {
    "no licence": "⚠️ no licence",
    "archived": "⚠️ archived",
    "major error": "❌ major error",
    "authors not found": "⚠️ authors not found",
    "author match probable": "⚠️ author match probable",
    "no evidence of use": "no evidence of use",
}
ITEM_TEXT = {
    "R1": "States what the skill does not do",
    "R2": "Cites sources for its recommendations",
    "R3": "Says what to do when a check fails",
    "R4": "Qualifies numeric thresholds, or gives none",
    "R5": "Ties evaluation depth to intended use",
    "R6": "States the limitations of its own output",
    "R7": "Code examples complete enough to run",
    "R8": "Examples run in continuous integration",
    "R9": "Continuous integration passes on the pinned commit",
    "R10": "Stores outputs from a real run",
}
ANSWER = {"y": "✅ yes", "n": "no", "na": "not applicable"}


def latest():
    files = sorted((HERE / "list").glob("20??-??.yml"))
    return yaml.safe_load(files[-1].read_text()), files[-1].stem


def listing_rows(skills, by_id):
    rows = []
    for s in skills:
        if s["rank"] is None:
            continue
        rank = str(s["rank"])
        if s["rank_range"] != rank:
            rank += f" ({s['rank_range']})"
        also = ", ".join(by_id[i]["name"] for i in s["also_in_library"])
        rows.append({
            "title": title(s),
            "path": s["url"],
            "rank": rank,
            "library": s["library"],
            "tags": s["tags"],
            "S": s["S"], "Q": s["Q"], "E": s["E"], "M": s["M"], "U": s["U"],
            "flags": " · ".join(FLAG_ICON[f] for f in s["flags"]),
            "evidence": f"[evidence](curated-list-evidence.html#{s['id']})"
            + (f"; also in this library: {also}" if also else ""),
        })
    return rows


def unproven_rows(skills):
    rows = []
    for s in skills:
        if s["use"]["proven"]:
            continue
        flags = [FLAG_ICON[f] for f in s["flags"] if f != "no evidence of use"]
        rows.append({
            "title": title(s), "path": s["url"], "category": s["category"], "tags": s["tags"],
            "S": s["S"], "Q": s["Q"], "E": s["E"], "M": s["M"],
            "flags": " · ".join(flags),
            "evidence": f"[evidence](curated-list-evidence.html#{s['id']})",
        })
    return sorted(rows, key=lambda r: r["S"], reverse=True)


def title(s):
    """Skill names such as 'estimation' only make sense beside their library."""
    return f"{s['library'].split('/')[1]} · {s['name']}"


def esc(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def evidence_section(s):
    out = [f"## {title(s)} {{#{s['id']}}}", ""]
    if not s["use"]["proven"]:
        rank = "unproven: no evidence of use, so not ranked"
    elif s["rank"] is None:
        rank = "not ranked: beyond the per-library cap"
    elif s["rank_range"] == str(s["rank"]):
        rank = f"rank {s['rank']}"
    else:
        rank = f"rank {s['rank']} (range {s['rank_range']})"
    out += [
        f"[{s['library']} at `{s['commit'][:7]}`]({s['url']}) · {s['category']} skill · {rank} · tags: {s['tags']}",
        "",
        "| S | Q | E | M | U |", "|---:|---:|---:|---:|---:|",
        f"| {s['S']} | {s['Q']} | {s['E']} | {s['M']} | {s['U']} |", "",
    ]
    q = s["quality"]
    out += [
        f"**Quality.** {q['rubric_yes']} of {q['rubric_applicable']} applicable rubric items met"
        f" ({q['Q_rubric']}), less {q['major_errors']} major and {q['minor_errors']} minor errors.", "",
        "| Item | | Evidence |", "|:---|:---|:---|",
    ]
    for k, v in q["items"].items():
        if v["answer"] == "na":
            continue
        out.append(f"| {k} {ITEM_TEXT[k]} | {ANSWER[v['answer']]} | {esc(v['evidence'])} |")
    out.append("")
    for e in q["errors"]:
        mark = "❌ Major error" if e["severity"] == "major" else "Minor error"
        out += [f"- **{mark}.** {esc(e['quote'])} {esc(e['reason'])}"]
    if q["errors"]:
        out.append("")
    out += ["**Expertise.**", "", "| Author | Share | Field h-index | OpenAlex | Match |", "|:---|---:|---:|:---|:---|"]
    for a in s["expertise"]["authors"]:
        link = f"[record]({a['openalex']})" if a["openalex"] else "none"
        out.append(f"| {esc(a['name'])} | {a['share']} | {a['h_field']} | {link} | {esc(a['evidence'])} |")
    m = s["maintenance"]
    checks = ", ".join(f"{k} {'✅' if v else '✗'}" for k, v in m["checks"].items())
    out += [
        "",
        f"**Maintenance.** Last change to the skill's files {s['last_commit']}"
        f" ({m['days_since_change']} days; recency {m['recency']}). Usability {m['usability']}: {checks}."
        + (" Repository archived, so M is 0." if s["archived"] else ""),
        "",
    ]
    u = s["use"]
    if u["people"]:
        out += [f"**Use.** {u['points']} points from people outside the authors in the last 12 months.", "",
                "| Person | What they did | Expert | Evidence |", "|:---|:---|:---|:---|"]
        for p in u["people"]:
            links = ", ".join(f"[{n + 1}]({x})" for n, x in enumerate(p["urls"]))
            expert = f"yes: {esc(p['expert_evidence'])}" if p["expert"] else "no"
            out.append(f"| {esc(p['name'])} (`{p['login']}`) | {esc(p['kind'])} | {expert} | {links} |")
        out.append("")
    else:
        out += ["**Use.** No issue, pull request or comment from anyone outside the authors in the last 12"
                " months, and no deliberate installation found in another project.", ""]
    out += [f"Repository stars and forks, used only to break ties: {s['stars']} and {s['forks']}.", ""]
    if s["note"]:
        out += [f"*Note.* {s['note']}", ""]
    return out


def main():
    data, month = latest()
    skills = data["skills"]
    by_id = {s["id"]: s for s in skills}
    for cat in ("tool", "task"):
        rows = listing_rows([s for s in skills if s["category"] == cat], by_id)
        (HERE / "list" / f"{cat}.yml").write_text(yaml.safe_dump(rows, sort_keys=False, allow_unicode=True, width=1000))
    (HERE / "list" / "unproven.yml").write_text(
        yaml.safe_dump(unproven_rows(skills), sort_keys=False, allow_unicode=True, width=1000))
    ev = [{"title": r["name"], "path": r["url"], "contents": r["contents"], "licence": r["licence"],
           "last_commit": r["last_commit"], "authors": r["authors"]} for r in data["evaluation_resources"]]
    (HERE / "list" / "evaluation.yml").write_text(yaml.safe_dump(ev, sort_keys=False, allow_unicode=True, width=1000))

    page = [
        "---",
        f'title: "PMx Skills Index: evidence, {month}"',
        'subtitle: "What every score in the index rests on"',
        'description: "The rubric answers with quotes, error-audit findings, matched OpenAlex records with field h-indices, and repository measurements behind each skill in the PMx Skills Index."',
        "categories: [GenAI, Pharmacometrics methods]",
        "date: last-modified",
        "toc: true",
        "toc-depth: 2",
        "toc-location: left",
        "---",
        "",
        "::: {.callout-important appearance=\"simple\"}",
        "**Written by Claude, not by a person.** This page is generated by the monthly run from",
        f"`list/{month}.yml`. The [index](curated-list.qmd) explains how to read it, and",
        "[Specification 2](specification2-curated-list.qmd) defines every score.",
        ":::",
        "",
    ]
    for cat, label in (("tool", "Tool Skills"), ("task", "Task Skills")):
        page += [f"# {label}", ""]
        for s in [s for s in skills if s["category"] == cat]:
            page += evidence_section(s)
    (HERE / "curated-list-evidence.qmd").write_text("\n".join(page))


if __name__ == "__main__":
    main()
