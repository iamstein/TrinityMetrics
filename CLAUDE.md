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
| `about.qmd`, `code.qmd`, `resources.qmd` | Looking one thing up | reference | thin |
| `blog/drafts/*` | Andy, later | draft | unconstrained |

The machine-prose tics in the guide's Part 1 apply to everything, including
conversation and commit messages, whether or not the guide has been read this
session.

## Project folders

Each folder under `projects/` carries an `index.qmd` listing the documents in
it, the working specification first, as a plain list rather than a Quarto
listing. When a document there is added, renamed or removed, update that list
in the same commit.

A project that reads sources also carries a `references.qmd` in the same
folder: the reading queue, the source list, and a status marker on every entry
recording whether the claim the project draws from it has been checked against
the source. `projects/tce-ipde/references.qmd` is the shape to copy, markers
and section order included.

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
