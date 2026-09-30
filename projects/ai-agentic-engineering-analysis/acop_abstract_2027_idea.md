# ACoP 2027 abstract idea: agentic engineering for pharmacometrics analysis

Draft idea, 2026-09-12. Not an abstract yet. This is the argument, the parts
that are missing, and the question of whether it is worth submitting.

This file is not rendered into the site. `_quarto.yml` renders `.qmd` only, so
it stays a working file in the repository.

## Working title

- Agentic Engineering for Pharmacometrics Analysis
- Alternate: A Scaffold for Human and AI Collaboration in Population Modeling
- Alternate: What a Modeling Plan Has to Say When an Agent Implements It

## The argument

Vibe coding accepts whatever the agent produces and judges it by whether it
runs. Agentic engineering writes the plan, the constraints and the checks
first, then commissions the agent to build inside them. Pharmacometrics already
works the second way. There is an analysis plan, an exploratory data analysis
step, model development, conclusions, and a report that somebody other than the
author reviews and approves.

So the proposal is not a new process. It is the existing process, written down
in a form an agent can follow, with the review points redesigned for the fact
that the work now arrives in minutes rather than weeks.

The division of labor stays where it already is. The agent does the hands-on
work. Every review and every approval is done by a human, who owns the result.

## The five stages

| # | Stage | Who does the work | What the human must see before moving on |
|---|---|---|---|
| 1 | Modeling plan | Human and agent together, with the agent also critiquing the plan | The plan itself, agreed. This becomes the instruction the agent follows |
| 2 | Initial data analysis | Agent | The data summary and the exploratory figures, signed off. Expect a back and forth |
| 3 | Model development | Agent, with the human at defined gates | The base model, before any covariate work begins. Later gates to be worked out |
| 4 | Conclusions | Human leads, agent suggests | Nothing to approve. The human owns this outright |
| 5 | Methods and report | Agent drafts | The full draft, reviewed and approved as any report is today |

Stage 3 is the one that needs thinking. The base model gate is obvious. What
comes after it is not, and a covariate search run unattended can cover a lot of
ground before anyone looks.

## What this actually adds

The honest doubt is that this is all in the SOPs already, and the only real
work is trying it with an agent and tightening what breaks. That doubt is
mostly right, and the abstract is stronger for saying so. Four things do change,
and they are the content a poster can carry.

**A plan written for a pharmacometrician is not a plan an agent can follow.**
A human modeler fills the gaps with shared convention: which diagnostics to
look at, how to handle values below the limit of quantification, what counts as
converged, when a covariate is worth keeping. An agent does not share that
convention and does not ask. It picks something plausible and moves on, and the
choice is invisible unless someone goes looking. Making the tacit part explicit
is real work and it is the deliverable most likely to be reused by others.

**The review points have to be designed, because the natural pacing is gone.**
Today a base model takes days, so it sits in front of you and gets inspected.
An agent produces one before you have finished reading the data summary. Review
stops happening for structural reasons rather than because anyone decided to
skip it. Gates have to be placed deliberately and the agent has to stop at them.

**The failure mode inverts.** Vibe coding fails loudly, with an error. An
agentic analysis fails quietly, with a model that converges, produces clean
diagnostics, and answers a question nobody asked. Verification has to move from
"did it run" to "is this the analysis the plan specified".

**Authorship no longer implies review.** When a person writes the code, their
name on the report means they looked at it. When an agent writes it, that link
is broken and the record of who checked what has to be made explicit.

## What the poster would show

The scaffold, as artifacts people can copy:

- A modeling plan template, in Markdown, with the sections an agent needs that
  a human plan usually leaves implicit.
- The gate list: where the agent stops, and what a human has to look at there.
- A repository layout, so data, scripts, model runs and the report sit where
  both a human and an agent expect them.
- Possibly the whole thing packaged as a skill file, so it loads into the agent
  rather than being a document somebody remembers to follow.

And one worked analysis run this way end to end, with what went wrong in it.

## The risk, and the prerequisite

An ACoP poster that is all framework and no analysis will not land. The
audience will want to see a real model, real diagnostics, and an honest account
of where the agent went wrong and how the gate caught it.

So the prerequisite is running one complete analysis this way before the
abstract is written. Without that, this is a position paper, and it should
either wait a year or be pitched as a workshop rather than a poster.

## Open questions

1. Which analysis is the worked example? It has to be one where the data can be
   shown, which points at a public dataset or a synthetic one.
2. Is the argument tool-agnostic by design? Naming a product dates the poster
   and narrows the audience.
3. Is the skill file the deliverable, or the plan template? Doing both well is
   more than one poster holds.
4. How does this sit with regulated work? Everything above assumes exploratory
   analysis. A submission-grade analysis has validation requirements this does
   not address, and saying so explicitly is safer than leaving it open.
5. What is the ACoP 2027 abstract deadline and word limit? Neither is known
   here and both shape how much of the above survives.

## Relation to the rest of this project

The [working specification](specification.qmd) already covers the general
version of this: what is in place in this repository, how a spec gets written,
and how work divides between a human and an agent. This abstract is the
pharmacometrics-specific case of it, aimed at an outside audience rather than
at this repository. If the abstract is written, the specification is where the
general claims should stay, and the abstract should carry the worked example
and the five stages.
