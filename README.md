# TrinityMetrics

Site: <https://iamstein.github.io/TrinityMetrics/>

A repository and publishing site focused on integrating human expertise, generative AI, and regulated clinical data workflows for statistical and pharmacometric analysis.

## Purpose

TrinityMetrics explores how AI can be used in clinical, statistical, and pharmacometric work without weakening accountability, reproducibility, or data integrity.

The repository is designed to support two connected goals:

- a **Quarto website/blog** for public-facing writing
- a **code repository** for reusable materials, examples, and workflow assets

## Site structure

The Quarto site is organized around a small set of stable pages:

- **Home** for project framing and current direction
- **Blog** for essays, working positions, and implementation notes
- **Projects** for open-source tools and longer-running working documents
- **Guides** for working practices, such as how to read a paper
- **Resources** for reference documents, checklists, and practical guides
- **Code** for repository layout, examples, and reusable materials
- **About** for the bio, audience, and project status, with the CV linked beside it

## Repository layout

~~~~text
.
├─ _quarto.yml
├─ index.qmd
├─ about.qmd
├─ resources.qmd
├─ code.qmd
├─ blog/
│  ├─ index.qmd
│  ├─ drafts/
│  └─ posts/
├─ projects/
│  ├─ index.qmd
│  ├─ projects.yml
│  └─ <project>/
├─ guides/
│  ├─ index.qmd
│  └─ guides.yml
├─ code/
├─ data/
├─ examples/
├─ skills/
├─ references/
├─ .github/workflows/
├─ styles.css
└─ docs/
~~~~

### Key directories

- `blog/drafts/` contains working Markdown drafts that are not yet published
- `blog/posts/` contains published Quarto posts
- `projects/` contains one directory per project, listed by `projects/projects.yml`
- `guides/` contains working-practice guides, listed by `guides/guides.yml`
- `data/` contains datasets used by posts and examples
- `code/` contains reusable scripts, templates, and utilities
- `examples/` contains worked examples and case studies
- `skills/` contains specialized AI guidance/context files
- `references/` contains PDFs and other static support materials
- `docs/` contains the rendered site output for GitHub Pages

## Local development

To preview the site locally:

```bash
quarto preview
```

To render the site into `docs/`:

```bash
quarto render
```

## GitHub Pages publishing

The site is configured to render to `docs/`.

`.github/workflows/publish.yml` renders the site and deploys it on every push
to `main`. That workflow also fetches the CV from Google Docs into
`docs/files/stein-cv.pdf` at build time, so the published PDF matches the
document as of the last build. The document must stay shared as *anyone with
the link, Viewer* for the fetch to work.

## Notes

- The Quarto configuration lives in `_quarto.yml`.
- Site styling adjustments live in `styles.css`.
- The repository is intentionally early-stage and will evolve as posts, examples, and reusable materials are added.
