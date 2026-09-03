# dose-response

Two synthetic oncology Phase 1/2 datasets, used by the
[sizing-studies](../../../projects/sizing-studies/) project to work the sample
size calculations against real-shaped data rather than only formulas.

## dose_tumor_resp.rds

96 patients, one row each: dose, baseline covariates, and RECIST-derived
response outcomes.

Column | Description
---|---
`ID` | Patient ID
`DOSE` | Assigned dose (mg)
`LD0` | Baseline sum of longest diameters (target lesions)
`ECOG0` | Baseline ECOG performance status (0 or 1)
`BOR` | Best overall response (RECIST category: CR, PR, SD, PD)
`OR` | Objective response, 1 if `BOR` is CR or PR, else 0
`BESTPCT` | Best percent change in tumor size from baseline
`WK8PCT` | Percent change in tumor size from baseline at week 8

## emax_tumor_size.rds

61 patients, one row each: average dose before the first tumor assessment and
the percent change in tumor size at that assessment.

Column | Description
---|---
`Average_Dose` | Average daily dose before the first assessment (mg)
`Tumor_Pct_Change` | Percent change in tumor size at the first assessment
