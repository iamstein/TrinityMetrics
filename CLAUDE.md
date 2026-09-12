# Claude Code instructions

## Writing guide

Read `.github/skills/writing-for-andy/SKILL.md` before drafting a new document, or before
substantially rewriting an existing one — a `.qmd` page, a blog post, a project
document, `README.md`. Read it once per session, on the first such task, and
again whenever Andy asks for it by name. Do not read it for code, configuration,
a typo fix, a link change, or as a session preamble.

The guide originates in `iamstein/synpmx` at `design/WRITING_FOR_ANDY.md`. The
copy here is adapted for this repository and has diverged from that one. It sits
in `.github/skills/` rather than `.claude/skills/` so that it loads when this
instruction says to read it, and not on every session. Do not edit it during a
session; say in the conversation what looks wrong and let Andy decide.

Its Part 1 document contract lists synpmx files. The equivalent for this
repository:

| Document | Reader | Kind | Length |
|---|---|---|---|
| `README.md` | Deciding whether to clone | how-to | thin |
| `index.qmd` | Deciding whether to read further | how-to | thin |
| `blog/posts/*/index.qmd` | Following one argument | explanation | thin |
| `projects/*/index.qmd` | Finding the right document in the folder | how-to | thin |
| `projects/*/*.qmd` | Working on the project | reference | as long as the work needs |
| `guides/*.qmd` | Looking up how to do something | how-to | thin |
| `projects/*/presentation.qmd` | Sitting in the room | explanation | one idea per slide |
| `about.qmd`, `code.qmd` | Looking one thing up | reference | thin |
| `blog/drafts/*` | Andy, later | draft | unconstrained |

The machine-prose tics in the guide's Part 1 apply to everything, including
conversation and commit messages, whether or not the guide has been read this
session.

## Project folders

Each folder under `projects/` carries an `index.qmd` listing the documents in
it, the working specification first, as a plain list rather than a Quarto
listing. When a document there is added, renamed or removed, update that list
in the same commit.

After adding, renaming or removing a folder under `projects/`, run
`_scripts/check-project-cards.sh`. It reports any folder with no card, any
folder carrying a card in both yml files, and any card pointing at a file that
does not exist. `site-integration` sat with no card for weeks and nobody
noticed, which is the case it catches.

A project that reads sources also carries a `references.qmd` in the same
folder: the reading queue, the source list, and a status marker on every entry
recording whether the claim the project draws from it has been checked against
the source. `projects/tce-ipde/references.qmd` is the shape to copy, markers
and section order included.

A project's card on the Projects page carries `Draft` in its `categories:`
list in `projects/projects.yml` for as long as it is one, alongside the
category that puts it in the right section (`Dose-response methods`,
`Immunology and T-cell engagers`, `GenAI`, `Site Maintenance`). Remove `Draft`
in the same commit that the project stops being one — there is no `Public`
category, since every published page is public by default and a second label
for that would say nothing. A listing that mixes draft and finished cards
needs `categories: true` and `categories` added to its `fields:` list in
`projects/index.qmd`, or the pill never renders; a listing with nothing to
distinguish (`R packages`, `Matlab tools`) skips both.

Archive on relevance, not on completion. A finished project stays on the
Projects page for as long as someone would still go to it: `xgx` and `xgxr` are
done and stay, because people still use them. A project moves to the archive
when it stops being something to refer to, either because its question got
answered somewhere else or because the work it records is over. `site-integration`
and `positron-assistant-config` are the two cases so far. Finishing is not on
its own a reason to archive.

To archive, move the whole card from `projects/projects.yml` to
`projects/archive.yml`. That is the only step: the folder does not move, the
URL does not change, and `projects/archive.qmd` lists whatever is in the second
file. Quarto's listing `exclude:` does not filter yaml metadata, so a category
such as `Archived` will not keep a card off the Projects page; the second file
is the mechanism. Drop `Draft` on the way across, rewrite the `subtitle:` to
say how the project ended, such as `Finished` or `Overtaken by a button`, and
keep the topical category so the archived card still shows what kind of project
it was. Add a callout at the top of the project's own `index.qmd` saying it is
archived and pointing at `../archive.qmd`, because a reader arriving from a
search result never sees either listing page. A card whose `path:` leaves
`projects/`, as the MATLAB one points at `../software.qmd`, gets no callout;
that page is not a project folder and says for itself that it is kept for the
record.

When the last card leaves a section, delete the section heading and its
listing from `projects/index.qmd` in the same commit. An emptied listing still
renders its heading, with nothing under it.

## Other conventions in this repository

- `.github/copilot-instructions.md` — Markdown mechanics: blank lines around
  lists and headings, `-` bullets, ATX headings, preserve each file's existing
  wrapping.
- `.github/skills/evaluate-blog-posts/SKILL.md` — the rubric for judging whether
  a blog draft is ready to publish.

## Site

The site is Quarto, published to GitHub Pages by `.github/workflows/publish.yml`
on every push to `main`. `blog/drafts/**` is excluded from the render, so
anything there is private until it moves. Preview a page with
`quarto preview <file>.qmd`.
