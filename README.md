# TrinityMetrics

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
- **Resources** for reference documents, checklists, and practical guides
- **Code** for repository layout, examples, and reusable materials
- **About** for scope, audience, and project status

## Repository layout

~~~~text
.
├─ _quarto.yml
├─ index.qmd
├─ about.qmd
├─ blog/
│  ├─ index.qmd
│  └─ posts/
├─ resources.qmd
├─ code.qmd
├─ drafts/
├─ code/
├─ examples/
├─ skills/
├─ references/
├─ styles.css
└─ docs/
~~~~

### Key directories

- `drafts/` contains working Markdown drafts that are not yet published
- `blog/posts/` contains published Quarto posts
- `code/` contains reusable scripts, templates, and utilities
- `examples/` contains worked examples and case studies
- `skills/` contains specialized AI guidance/context files
- `references/` contains PDFs and other static support materials
- `docs/` contains the rendered site output for GitHub Pages

## Current publishing plan

The initial public launch is planned around two posts published together:

- a short philosophy post on AI assistance and human decision ownership
- a practical post on synthetic data workflows

That should make the purpose of the repository clear from the start.

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

There are two workable publishing patterns:

- **render locally and commit `docs/`**
- **use GitHub Actions to render and deploy automatically**

This repository includes a GitHub Actions workflow for automated publishing.

## Notes

- The Quarto configuration lives in `_quarto.yml`.
- Site styling adjustments live in `styles.css`.
- The repository is intentionally early-stage and will evolve as posts, examples, and reusable materials are added.
