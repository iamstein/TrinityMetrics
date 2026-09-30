---
name: TrinityMetrics AI and tooling post evaluation
description: Use this skill when reviewing TrinityMetrics blog drafts about AI, workflows, tooling, reproducibility, or regulated scientific analysis for publication readiness.
---

# TrinityMetrics AI and Tooling Post Evaluation Skill

## Purpose
Evaluate whether a draft post meets TrinityMetrics standards for publication, with emphasis on practical usefulness, scientific integrity, and fit for regulated analytical workflows.

## When to use
Use this skill when:
- reviewing draft posts about AI-assisted analysis, statistical tooling, pharmacometrics, reproducibility, or workflow design
- deciding whether a post is ready to publish, needs revision, or should not be published yet
- comparing multiple drafts against a consistent editorial standard

Do not use this skill for:
- grammar-only copyediting
- formatting-only review
- SEO-only review without assessing substance

## TrinityMetrics framing
A strong TrinityMetrics post should usually do at least one of the following:
- reduce friction in a real scientific or analytical workflow
- make reasoning or decision boundaries more explicit
- improve reproducibility or auditability
- clarify how AI can assist without obscuring human responsibility
- provide a concrete, transferable pattern for regulated or high-consequence work

## Evaluation dimensions
Score each dimension from 0 to 5.

### 1. Friction Reduction (0-5)
Does the post provide a tool, method, template, or pattern that meaningfully reduces real workflow friction?

Consider:
- Is there a real bottleneck being addressed?
- Would this save time, reduce confusion, or lower process overhead?
- Is the gain practical rather than merely conceptual?

### 2. Usability (0-5)
Can a reader apply the idea within about 10 minutes?

Consider:
- Is the setup clear?
- Is any code readable and well-scoped?
- Are inputs and outputs clear?
- Could a technically competent reader try this without guesswork?

### 3. Concreteness (0-5)
Is the problem and solution specific and grounded in a real use case?

Consider:
- Is the post about an actual workflow, artifact, or decision point?
- Are claims tied to examples?
- Does it avoid vague AI-generalities?

### 4. Scientific Integrity (0-5)
Does the post preserve sound scientific reasoning?

Consider:
- Are limitations stated clearly?
- Are risks, failure modes, or misuse scenarios identified?
- Is analysis separated from decision-making?
- Does the post avoid overstating what AI or tooling can justify?

### 5. Reproducibility (0-5)
Could a reader reproduce the example or pattern?

Consider:
- Are the steps clear?
- Are assumptions explicit?
- Are examples sufficiently specified?
- Would another analyst be able to repeat the workflow?

### 6. Signal-to-Noise (0-5)
Is the post concise and focused on the tool, pattern, or argument?

Consider:
- Does each section earn its place?
- Is there excessive framing, repetition, or abstraction?
- Is the main takeaway obvious by the end?

## Optional fit checks
In addition to scoring, note whether the post:
- fits the TrinityMetrics audience of pharmacometricians, biostatisticians, statistical programmers, or clinical data scientists
- explains why the topic matters in regulated or high-accountability environments
- distinguishes useful AI assistance from automated judgment

## Scoring interpretation
- 25-30: Publish
- 18-24: Revise
- Below 18: Do not publish

A high score should reflect not just polish, but usefulness and integrity.

## Output format
Return the review in this structure:

- **Total Score:** X / 30
- **Decision:** Publish | Revise | Do not publish
- **One-sentence verdict:** Brief summary of whether the post is worth publishing and why
- **Dimension Scores:**
  - Friction Reduction: X / 5
  - Usability: X / 5
  - Concreteness: X / 5
  - Scientific Integrity: X / 5
  - Reproducibility: X / 5
  - Signal-to-Noise: X / 5
- **What the post does well:**
  - Bullet list
- **Key Issues:**
  - Bullet list
- **Suggested Fixes:**
  - Bullet list ordered from highest to lowest impact
- **Best excerpt or idea to preserve:**
  - Quote or short paraphrase

## Review guidance
Prioritize concrete, high-impact feedback.

When possible:
- point to specific passages
- separate structural problems from minor wording edits
- identify unsupported claims or missing caveats
- recommend the smallest set of changes needed to make the post publishable

Default to substance over style.

## Categorization requirement

- Classify posts as principle and/or tool.
- Classify as ai if about ai.
- Classify as biostats or pmx when either are referenced.
- Keep a tally of how many "tools" and "principles" there are.  Aim for 3-4x more tools than principle posts and point this out if there are too many "principle" posts.
