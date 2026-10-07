# Quality rubric for the PMx Skills Index

The wording of each rubric item in Specification 2, Section 4.1. Andy edits
this file; the monthly agent reads it and never changes it. An item keeps its
number when its wording changes.

A *yes* needs a quoted line from the skill, or from a file the skill tells the
assistant to read, as evidence. An item answered without a quote scores *no*.
An item that does not apply is left out of the denominator.

| # | Item | Applies to |
|---|---|---|
| R1 | States what the skill does not do | All |
| R2 | Cites sources: at least 5 of 10 randomly sampled recommendations name a published source or official documentation | All |
| R3 | Says what to do when a check fails, beyond listing which checks to run | Task |
| R4 | Qualifies numeric thresholds such as shrinkage, RSE or condition number with context, or gives none | Task |
| R5 | Ties the depth of evaluation to the model's intended use | Task: model building and evaluation, including exposure-response |
| R6 | States the limitations of its own output | All |
| R7 | Gives code examples complete enough to run | Skills with code |
| R8 | Runs those examples in continuous integration | Skills with code |
| R9 | Continuous integration passes on the pinned commit | Skills with code |
| R10 | Stores outputs from a real run | Skills with code |

## Conventions Applied in Scoring

- **Skills with code** are skills whose instructions run analysis code or call
  analysis scripts. A persona or checklist with no code, or a skill whose only
  script is housekeeping, has R7 to R10 as not applicable.
- **R9 follows R8.** Continuous integration that does not run the skill's
  examples says nothing about them, so R9 is *no* whenever R8 is *no*.
- **R5** applies to model building, model evaluation and exposure-response
  modelling. It does not apply to NCA, simulation, dose projection or code
  review.
