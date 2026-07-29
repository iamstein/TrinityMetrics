# Autonomous Overnight Model Search: A Vision for AI-Assisted Pharmacometrics

## Motivation

Pharmacometric model development is fundamentally an iterative search process. While the scientific decisions require expertise and judgment, much of the day-to-day work is repetitive:

- Generate candidate models.
- Submit jobs to a compute cluster.
- Wait for completion.
- Check convergence.
- Review diagnostics.
- Eliminate poor candidates.
- Decide what to try next.

The goal is **not** to automate the scientist out of the process.

The goal is to automate the repetitive exploration so that the scientist spends more time thinking and less time waiting.

---

## Vision

Imagine ending the workday by defining a search space rather than fitting a single model.

Examples might include:

- Structural model alternatives
- Covariate hypotheses
- Random-effects structures
- Residual error models
- Parameter constraints
- Search limits

An overnight workflow then explores this space automatically.

The next morning, instead of dozens of output files, the scientist receives a concise summary.

```
42 candidate models evaluated

25 failed hard technical criteria

9 were dominated by simpler models

5 remain scientifically plausible

3 recommended for human review
```

Along with:

- Reasons models failed
- Comparison of surviving models
- Key diagnostics
- Suggested next experiments

The scientist reviews only the handful of candidates that deserve careful attention.

---

## Guiding Principle

The objective is **not**:

> Find the best model.

Instead it is:

> Efficiently explore the model space, eliminate poor candidates, and present the scientist with the most informative remaining possibilities.

The AI explores.

The scientist judges.

---

## Proposed Architecture

### Development Environment

Most workflow development occurs locally using synthetic data.

Synthetic datasets allow development of:

- model-building logic
- AI prompts
- workflow orchestration
- testing
- debugging
- reproducibility

without requiring access to protected clinical data.

### Protected Compute Environment

The exact same workflow is then executed inside the secure computing environment.

Patient-level data never leave the cluster.

Only approved outputs are exported.

Possible exported artifacts include:

- model specifications
- convergence summaries
- objective function values
- aggregate diagnostics
- sanitized comparison reports
- provenance information

Raw patient data and subject-level outputs remain inside the secure environment.

---

## Overnight Workflow

An autonomous controller could perform something like:

1. Generate candidate models.
2. Submit jobs.
3. Wait for completion.
4. Parse outputs.
5. Reject technically invalid models.
6. Remove models dominated by simpler alternatives.
7. Rank remaining candidates.
8. Produce a concise report.
9. Suggest the next experiments.

Every step is logged.

Every decision is reproducible.

---

## Human in the Loop

The scientist begins each morning with a small set of promising candidates.

Questions become:

- Does this model make biological sense?
- Are the diagnostics meaningfully better?
- Is the additional complexity justified?
- What hypothesis should be tested next?

Rather than replacing scientific judgment, the workflow amplifies it.

---

## Long-Term Evolution

Initially the system may use deterministic rules.

Examples include:

- test an additional compartment
- add an IIV term
- remove unsupported covariates
- modify residual error structure
- retry failed estimation using predefined strategies

Eventually an AI agent could propose increasingly sophisticated modifications while remaining constrained by:

- predefined search limits
- scientific rules
- audit trails
- governance policies
- human approval

The AI becomes a tireless junior modeler rather than an autonomous decision maker.

---

## Why Synthetic Data Matters

Synthetic datasets enable development of nearly the entire automation pipeline outside protected environments.

This includes:

- workflow development
- prompt engineering
- automated testing
- benchmarking
- regression testing
- failure simulation

The production environment simply replaces the synthetic dataset with the protected clinical dataset while preserving the rest of the workflow.

This may become one of the strongest use cases for synthetic pharmacometric data.

---

## A Broader Shift

Historically, pharmacometricians built models.

Increasingly, pharmacometricians may build systems that build models.

The highest leverage may come from creating infrastructure that helps both humans and AI perform better science.

Examples include:

- synthetic data generators
- automated model search
- literature databases
- reusable model libraries
- standardized workflows
- AI-ready scientific knowledge bases

These are enabling technologies.

They make many future analyses better rather than solving only today's problem.

---

## An Architect-Gardener View

This idea also reflects a broader philosophy of scientific work.

The role of the scientist shifts from manually constructing every model to designing an environment in which good models can emerge.

The architect creates structure.

The gardener cultivates conditions.

The overnight workflow explores possibilities.

The scientist returns each morning to examine what has grown.

That is not replacing scientific creativity.

It is giving scientific creativity far more leverage.