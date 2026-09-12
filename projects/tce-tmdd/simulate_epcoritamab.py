"""Regenerate the epcoritamab reference profile in data/epcoritamab_published_median.csv.

Unlike the other three settings in this project, no digitization is involved.
The epcoritamab population PK paper is paywalled, but the EMA public assessment
report for Tepkinly (EMA/CHMP/419797/2023, Table 7, run 154) prints the whole
final parameter set, so the published model can simply be run.

  https://www.ema.europa.eu/en/documents/assessment-report/tepkinly-epar-public-assessment-report_en.pdf

Published model: two compartments, non-specific linear clearance plus a
quasi-steady-state target-mediated clearance, first-order subcutaneous
absorption. The target pool BASE is held at steady state (their k_deg = k_int)
and is never depleted, so the target-mediated term reduces exactly to
Michaelis-Menten with Vmax = k_int * BASE * Vc and Km = Kss.

Values are for a typical patient of 75 kg and 65 years. Regimen is the
approved 0.16 mg / 0.8 mg / 48 mg weekly step-up.

This file records the parameters and the equations; the CSV it describes is
produced by the R chunk in class-model.qmd, which is where the solver lives.
"""

PARAMETERS = dict(                 # EMA/CHMP/419797/2023 Table 7, run 154
    CL_F=0.481,                    # L/day, apparent non-specific clearance, RSE 2.66%
    Q_F=0.488,                     # L/day, apparent inter-compartmental clearance
    Vc_F=9.33,                     # L, apparent central volume
    Vp_F=14.1,                     # L, apparent peripheral volume
    ka=0.584,                      # 1/day, absorption rate constant
    BASE=2.03,                     # ug/mL, total target concentration, RSE 5.84%
    Kss=0.214,                     # ug/mL, quasi-steady-state constant, RSE 7.27%
    kint=0.0278,                   # 1/day, drug-target complex elimination, RSE 9.31%
)
REGIMEN = dict(days=[0, 7] + list(range(14, 176, 7)),
               mg=[0.16, 0.8] + [48] * len(range(14, 176, 7)))

# Derived quantities quoted in class-model.qmd Section 8:
#   total target pool          = BASE * Vc_F                 = 18.94 mg
#   target-mediated CL at C->0 = kint * BASE * Vc_F / Kss    =  2.46 L/day
#   total CL at C->0           = CL_F + the above            =  2.94 L/day
#   ratio to the saturated CL  = 2.94 / 0.481                =  6.1
#   max target-mediated rate   = kint * BASE * Vc_F          =  0.527 mg/day
