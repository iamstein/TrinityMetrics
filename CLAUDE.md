# Claude Code instructions

## Writing guide

The writing guide is the skill at `.claude/skills/writing-for-andy/SKILL.md`,
also available as `/writing-for-andy`. Load it before drafting a new document,
or before substantially rewriting an existing one — a `.qmd` page, a blog post,
a project document, `README.md`. Load it once per session, on the first such
task, and again whenever Andy asks for it by name. Do not load it for code,
configuration, a typo fix, a link change, or as a session preamble. Do not edit
it during a session; say in the conversation what looks wrong and let Andy
decide.

The guide's Part 1 asks for a document contract. For this repository:

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

To archive a project, move the whole card from `projects/projects.yml` to
`projects/archive.yml`. That is the only step: the folder does not move, the
URL does not change, and `projects/archive.qmd` lists whatever is in the second
file. Quarto's listing `exclude:` does not filter yaml metadata, so a category
such as `Archived` will not keep a card off the Projects page; the second file
is the mechanism. Drop `Draft` on the way across, rewrite the `subtitle:` to
say how the project ended, such as `Finished` or `Overtaken by a button`, and
keep the topical category so the archived card still shows what kind of project
it was. Add a callout at the top of the project's own `index.qmd` saying it is
archived and pointing at `../archive.qmd`, because a reader arriving from a
search result never sees either listing page.

When the last card leaves a section, delete the section heading and its
listing from `projects/index.qmd` in the same commit. An emptied listing still
renders its heading, with nothing under it.

`projects/archive.qmd` carries the same sections, in the same order, so a
project keeps its heading when it moves. Archiving into a category the archive
page has no section for means adding one, listing and heading together. Do not
create sections there ahead of need, for the same reason an emptied one comes
out. Archive listings show `subtitle` and set `categories: false`, since the
heading already says the category and `Draft` is dropped on the way across.

## Other conventions in this repository

- `.github/copilot-instructions.md` — Markdown mechanics: blank lines around
  lists and headings, `-` bullets, ATX headings, preserve each file's existing
  wrapping.
- `.claude/skills/evaluate-blog-posts/SKILL.md` — the rubric for judging whether
  a blog draft is ready to publish.

## Privacy

The repository is public, so a committed line is public whether or not its
page renders. Andy's family members are referred to by relationship and never
by name, in pages, commit messages and code comments alike. Personal matters
stay off the site unless he has asked for that specific text. What counts as
personal is set by `sensitive-topics.txt` below, a list kept private because
the list itself would say too much. When a note or page touches family
or anything personal, show him the wording and ask before committing it.

`_scripts/privacy-check.sh` runs as the commit-msg hook and enforces part of
this. It reads two lists kept outside the repository, in
`~/.config/trinitymetrics/`: `private-names.txt` blocks a commit, and
`sensitive-topics.txt` holds one until it is committed again with
`PRIVACY_REVIEWED=1`. Do not read, print or copy either list, do not set
`PRIVACY_REVIEWED=1` without Andy's go-ahead for that commit, and never use
`--no-verify`. A new clone needs `git config core.hooksPath .githooks` once.

The check finds words and nothing else. A description that identifies a
person without naming them passes it, which is why the rule above comes
first.

## Site

The site is Quarto, published to GitHub Pages by `.github/workflows/publish.yml`
on every push to `main`. `blog/drafts/**` is excluded from the render, so
anything there is private until it moves. Preview a page with
`quarto preview <file>.qmd`.

## Frozen computation

The publish workflow installs Quarto and Python, and no R. A page that runs R
therefore has to replay from a cache committed under `_freeze`, which is what
the site-wide `execute: freeze: auto` in `_quarto.yml` produces. A page that
overrides it with `freeze: false` forces execution on the runner and fails the
build. `projects/pmx-model-based-tdp/worked-comparison.qmd` shipped that way
and broke publishing for every push until its cache was committed, including
the pushes that had nothing to do with it.

The error names R rather than the page that needs it:

```
ERROR: Error executing 'Rscript': Failed to spawn 'Rscript': entity not found
Unable to locate an installed version of R.
```

That reads as a missing dependency on the runner, so look at the last page in
the render list instead of at the workflow.

After adding or changing a page that runs R, render it locally and commit its
directory under `_freeze` in the same commit. When a render looks like it
skipped the work, delete the page's directory under both `_freeze` and
`.quarto/_freeze` and render again. The second is a local freezer cache, kept
out of git, and it will replay a page whose committed cache you just deleted.

Do not add R to the workflow. The pages here need `brms`, `rstanarm`, `rxode2`
and `nlmixr2` between them, which means Stan and a compiler toolchain.
Installing a subset is worse than installing none, because the build keeps
passing until someone edits a page whose packages are missing, and the failure
then arrives far from the change that caused it.

Quarto finds R outside `PATH`, so rendering locally says nothing about whether
a page will build on the runner. The run on `main` is the only check that
settles it.
