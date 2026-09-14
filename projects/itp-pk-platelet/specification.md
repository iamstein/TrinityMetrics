# PK–platelet modelling to support Phase 2 dose and regimen selection in ITP

*Working specification for a B-cell depleting agent with escalation and randomized expansion data. Revised 14 September 2026 following critical review.*

**Status.** No PK–platelet model has been fitted and no decision simulation has been run. Section 14 contains reproducible illustrative calculations, not evidence of model-based sample-size savings. This revision incorporates the [critical review](specification-review.md). The [reference notebook](references.qmd) preserves the earlier search and reading notes; its older interpretations and verification markers are not a substitute for the claims and source qualifications in this specification. The [project index](index.qmd) lists the documents.

## In brief

**The question.** In a small study of a B-cell depleting agent in immune thrombocytopenia (ITP), can longitudinal platelet counts, pharmacokinetics (PK) and immune measurements improve the selection of a Phase 2 dose or short-course regimen over simpler analyses of the same patients?

**The clinical objective.** Preserve durable platelet control while avoiding unnecessary treatment and immune impairment. If a lower dose achieves the same durable immune reset, longer B-cell depletion offers no additional efficacy benefit and may impose additional burden. Depletion duration is a candidate predictor and immune recovery measure, not an efficacy objective or a calibrated infection-risk measure.

**The biological alternatives.** Benefit may require continued suppression of pathogenic immunity, may persist after healthy B-cell repopulation, or may follow different patterns in different patients. A model that makes platelet benefit disappear whenever total B cells return cannot test a reset hypothesis. This specification compares reversible suppression, persistent benefit consistent with reset, and mixtures of transient responders, durable responders and nonresponders. Persistence over follow-up is not proof of permanent immune tolerance.

**The working conclusion.** PK–platelet modelling could be useful when doses or regimens differ in response onset, durability, rescue requirements, treatment-free control or immune recovery, and those differences are supported by the study design. It may also help choose the next informative regimen. Its incremental value must be demonstrated against arm-level response estimates, simple dose-response curves and longitudinal platelet models without PK. A saturated peripheral B-cell biomarker does not rule out useful platelet modelling; it may rule out forcing the efficacy model through that biomarker.

**What is not yet known.** Whether PK adds decision-relevant information beyond assigned dose; whether B cells add information beyond PK and platelets; whether a persistent-response component is identifiable; and whether any gain is large enough to reduce patients, follow-up or decision loss. No numerical saving is assumed.

**How the project answers the question.** Specify a clinical decision, compare increasingly complex models under that same decision, and simulate plausible biological and trial-management alternatives. Report efficacy loss, unnecessary immune burden, calibration and inconclusive decisions, including model failures. Use available real data for exploratory checks and prior calibration alongside simulation.

**Scope.** The deliverable is a decision-method evaluation, not a recommendation for any named drug. A detailed B-cell systems model and a patient-level reanalysis of published trials are not required. Rare infection risks may need external evidence and sensitivity analysis rather than a fitted infection model. When benefit–risk information is inadequate, the output is explicitly an efficacy-based shortlist requiring clinical review.

## 1. Objective and study setting

### 1.1 Objective

Determine under which data, design and biological conditions a model improves selection of a clinically acceptable dose or regimen for Phase 2 in primary ITP. Improvement means lower expected clinical decision loss, more reliable identification of acceptable options, fewer patients or shorter follow-up at comparable decision performance. Agreement with the winner of a later finite trial is a secondary reproducibility measure, not the definition of truth.

A regimen $r$ specifies amount per administration, route, number of administrations and spacing. For comparisons that change only dose, these other attributes remain fixed. Predictions for untested schedules are reported separately from decisions among studied regimens.

### 1.2 Reference design

The initial design scenarios use three to five escalation levels with three to six patients per level, followed by two concurrently randomized expansion arms with 20 or 40 patients each. Total sample size therefore ranges from 49 to 110; each simulation reports its exact allocation. Escalation observations are available to every method that can use them, subject to exchangeability checks. Expansion doses may be fixed in advance or selected adaptively from escalation; these are separate design scenarios.

The intended data include serum drug concentration, circulating B-cell counts, immunoglobulins and platelet counts, together with dosing, background treatment, rescue, bleeding, infections and follow-up status. Additional immune and platelet-production measurements are evaluated for incremental value. The population, prior treatments and background-treatment policy must be specified before fitting.

### 1.3 Decisions requiring clinical input

Before using the work for an actual dose recommendation, the clinical team must set the endpoint and follow-up horizon, minimum worthwhile efficacy, acceptable efficacy loss, safety exclusions, and the importance of immune recovery and treatment burden. Sections 3 and 13 define how those choices enter the analysis. Illustrative simulation settings are labelled as such; they do not establish clinical standards.

## 2. Main uncertainties

Rank these by their potential to change the decision rather than by the number of unobserved compartments.

1. **Persistence mechanism.** Does benefit disappear with reconstitution, persist after reconstitution, or vary by patient? Short follow-up during complete depletion may not distinguish these possibilities.
2. **Clinical tradeoff.** How much efficacy loss is acceptable for a reduction in exposure, treatment burden or immune impairment? Higher-than-needed dosing is not assumed to be the cheap error.
3. **Design and attribution.** Are expansion regimens randomized, background treatment controlled, and escalation cohorts exchangeable with expansion? A good fit cannot repair an unidentified causal contrast.
4. **Incremental information.** Do repeated platelets, PK or immune markers improve the decision beyond a simple dose-response analysis?
5. **Peripheral versus pathogenic immunity.** Blood B cells may not track the tissue cells or pathogenic activity that determine response. This challenges a specific biomarker link, not all dose–platelet models.
6. **Response heterogeneity.** Effects may be continuous, clustered, delayed or transient. A binary endpoint does not establish a binary biological response.
7. **Observation and management.** Rescue, TPO receptor agonist (TPO-RA) tapering, corticosteroids, biological platelet fluctuations, missed visits and dropout can dominate apparent durability.
8. **Prior transfer.** Parameters from another agent, disease or age group may not transfer. Published response-time ranges do not directly identify a transduction rate.
9. **Immune safety.** Total B-cell count and total IgG incompletely describe immune competence. Rare events cannot be estimated precisely from this reference design.

## 3. Clinical endpoints and estimands

### 3.1 Historical IWG criteria

The International Working Group (IWG) criteria provide terminology, not an automatic endpoint specification for this project. The original source is [Rodeghiero et al., Blood 2009](https://doi.org/10.1182/blood-2008-07-162503), read in the earlier project review.

| Term | IWG definition |
|:---|:---|
| Complete response, CR | Platelets $\ge100\times10^9$/L and absence of bleeding |
| Response, R | Platelets $\ge30\times10^9$/L, at least twice baseline, and absence of bleeding |
| No response | Platelets below 30, less than twice baseline, or bleeding |
| Loss of CR or R | Loss of the corresponding platelet criterion or bleeding |
| Confirmation | At least two measurements separated by at least 7 days for response; at least 1 day for no response or loss of response |
| Time to response | From starting treatment to achieving the response criteria |
| Duration of response | Time from achievement to loss; cumulative time in response can also be reported |

The IWG discontinued “partial” and “minimal” response terminology; older studies using those terms must be interpreted under their own definitions. CR is a response threshold, not a claim that platelet counts have normalized. Corticosteroid dependence affects IWG response classification and must not be ignored when reproducing that endpoint.

Newly diagnosed, persistent and chronic ITP refer to disease duration of less than 3 months, 3–12 months and more than 12 months, respectively. Define the population rather than pooling these categories without justification. Historical definitions of refractory disease should not be treated as current universal eligibility rules.

### 3.2 Primary estimand for this project

For each regimen $r$, define $p(r)$ as the probability of meeting the **protocol-specific durable platelet-control endpoint** in the target population under the specified background-treatment and rescue policy, at a common follow-up horizon $H$.

The protocol must resolve all of the following:

| Component | Required specification |
|:---|:---|
| Population | Disease phase, baseline platelet criteria, prior B-cell therapy, splenectomy and concomitant treatment |
| Treatment | Complete investigational regimen and the background-treatment policy |
| Platelet endpoint | Threshold, confirmation rules, assessment window and required fraction of qualifying visits |
| Rescue | Drugs or interventions counted as rescue, washout if applicable, and whether rescue constitutes failure |
| Treatment withdrawal | Whether successful taper and cessation of background therapy are required |
| Other events | Rules for bleeding, death, treatment discontinuation, new ITP treatment and dropout |
| Missing observations | Prespecified classification and sensitivity analyses; do not silently shrink the required denominator |
| Summary | Probability of durable control, with secondary time-to-event and burden summaries |

For a reset-oriented programme, sustained control after the investigational course and protocol-defined withdrawal of background therapy is particularly relevant. Control while a TPO-RA continues is a separate estimand. Do not condition the main randomized comparison on patients who successfully taper; taper success is an outcome of the assigned policy.

### 3.3 Secondary outcomes and immune recovery

Report time to initial response, relapse or treatment failure, time in platelet control, rescue use, background-treatment reduction, bleeding and treatment burden. Report infections and serious infections, immunoglobulin trajectories and B-cell recovery separately. Where available, B-cell subsets or functional immune measurements can qualify interpretation of total-count recovery.

A descriptive assessment of platelet control after B-cell recovery helps evaluate persistence. It must account for differing recovery times and follow-up and should not replace the common-horizon randomized comparison with a selected subgroup analysis. Patients who have not recovered by $H$ do not supply direct evidence about post-recovery remission.

### 3.4 Trial-specific definitions and response delays

Recent trials do not share a single durable-response definition. VAYHIT2 used time to treatment failure and a policy incorporating eltrombopag tapering; it is not interchangeable with a fixed-window platelet response rate. Other definitions in the reference notebook require checking against their primary reports before reproduction. [VAYHIT2 primary report](https://pubmed.ncbi.nlm.nih.gov/41363800/).

The IWG's reported rituximab ranges of 7–56 days to initial response and 14–180 days to peak response provide predictive context. They are not an estimated between-patient distribution or a direct prior on an effect-compartment half-life. Calibrate candidate priors by simulating the published regimen, baseline severity, visit schedule and endpoint.

For otherwise identical event definitions, adding a no-bleeding requirement can only reduce the true response probability. An estimated platelet-only probability is not guaranteed to upper-bound actual clinical response under model misspecification. Label platelet-only outputs accurately.

## 4. Biomarkers and what they can support

| Measurement | Potential contribution | Limitation to carry into the analysis |
|:---|:---|:---|
| Platelet count | Endpoint trajectory, onset, fluctuations and durability | Reflects production, destruction and treatment management together |
| Circulating CD19+ or CD20+ cells | Peripheral depletion and recovery | Does not establish tissue depletion or pathogenic activity; below-limit values are censored |
| Naive and memory B cells, plasmablasts | Composition of recovery and candidate activity markers | Requires validated gating, adequate counts and a justified link to response |
| Total IgG, IgM, IgA | Immune safety and exploratory response predictors | Bulk immunoglobulin does not identify the pathogenic antibody fraction |
| Glycoprotein-specific platelet autoantibodies | Candidate evidence about pathogenic antibodies | Direct platelet-bound and indirect serum assays measure different quantities; assay-negative does not mean disease-negative |
| Immature platelet fraction and absolute immature count | Supportive information about platelet production | The fraction changes with its platelet-count denominator; neither measure alone identifies production and destruction rates |
| BAFF, thrombopoietin, glycocalicin | Exploratory mechanistic covariates | Not assumed to be calibrated measures of tissue depletion or platelet destruction |

**Total IgG is not an estimator of the pathogenic plasma-cell floor.** A small pathogenic fraction may fall while total IgG is stable. Use total IgG for immune safety and test additional predictive value without asserting this mechanistic identification.

**Autoantibody data require a measurement model.** MAIPA or another glycoprotein-specific assay can inform a latent activity state, but its output is not automatically a quantitative observation of circulating pathogenic IgG. Specify assay type, units or ordinal scale, target, limits, sample requirements and interference from treatments. Evaluate baseline-positive selection and serial testing feasibility. Assay performance depends on method and population; use an assay-specific source rather than a universal sensitivity. [Al-Samkari et al., 2020](https://pubmed.ncbi.nlm.nih.gov/31891657/).

Nonspecific platelet-associated IgG should not be substituted for glycoprotein-specific testing. Anti-GPIb/IX specificity is an exploratory response covariate, not an established rule for predicting treatment failure; a primary IVIg study did not confirm a reliable response prediction. [Rogier et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32630482/).

Include a marker in the decision model only if its added information is worth its measurement and modelling burden. A measured intermediate need not improve prediction, even when biologically relevant. The simulation compares models with and without each added layer.

## 5. Use of other drugs as evidence

Rituximab and ianalumab inform B-cell depletion hypotheses; plasma-cell-directed agents inform a different intervention on antibody production; FcRn, SYK and BTK agents provide examples of other routes to platelet effects; TPO-RAs provide platelet-production and turnover modelling precedents. These mechanisms are not interchangeable sources of efficacy parameters.

The detailed drug catalogue and search history belong in the [reference notebook](references.qmd). No exhaustive or current approval-status catalogue is needed for the present decision-method study. Verify the particular source and claim before using a parameter, trial definition or dose-response shape. Ianalumab targets BAFF-R, not BAFF itself.

Long-lived plasma cells provide a plausible resistance mechanism for some B-cell-directed interventions. Evidence from selected splenic samples does not quantify a universal nonresponder fraction. [Mahévas et al., 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3533302/). Likewise, rituximab's long-term response proportion cannot be converted into the fraction of pathogenic antibody production attributable to those cells.

## 6. Four questions the project must answer

**6.1 Can the studied dose and regimen contrasts be estimated?** Examine randomization, dose coverage, exposure overlap, late PK sampling, route and adherence. Start with simple PK and endpoint models, but do not declare PK or dose-response parameters identifiable from sample size alone.

**6.2 Which additional data change the decision?** Compare binary outcomes, longitudinal platelets, PK and immune markers using the same patients, target population and decision rule. Separate gain from pooling doses under a shape assumption from gain due to additional measurements.

**6.3 Can the data distinguish transient suppression from persistent benefit?** Follow-up after the treatment course and after immune recovery is informative. If the data end during depletion, retain both mechanisms as plausible and report how the dose decision changes between them.

**6.4 What is the cost of being wrong?** Quantify unacceptable efficacy loss, unnecessary treatment and immune burden, and delayed or inconclusive decisions. Do not assume over-treatment is less consequential than under-treatment. Evaluate alternative clinically plausible tradeoffs.

## 7. Depletion depth, duration and persistent remission

At the evaluated therapeutic doses, peripheral counts may fall below the assay limit in every arm. In that situation, observed depth offers little discrimination; lower doses, earlier sampling or better assays may change that. Recovery timing can remain dose-dependent, but the effect size and precision are empirical questions. Under dose-proportional exponential terminal PK, doubling dose shifts crossing of a fixed concentration threshold by one terminal half-life. B-cell recovery need not follow that simplified threshold rule.

The efficacy link has at least three interpretations:

- **Suppression:** continued reduction of pathogenic activity is required; recovery may precede relapse.
- **Persistent change:** a course changes pathogenic activity so that control persists after total B cells return.
- **Heterogeneity:** some patients have durable benefit, some transient benefit and some little or none.

Longer depletion was associated with sustained rituximab response in follow-up data, but the association is not a randomized test of deliberately prolonging depletion. Relapse studies implicate both surviving memory cells and newly generated cells. These observations motivate competing models rather than establish a universal mechanism. [Patel et al., 2012](https://pubmed.ncbi.nlm.nih.gov/22566601/); [Crickx et al., 2021](https://pubmed.ncbi.nlm.nih.gov/33853929/).

Immune recovery is also relevant to burden: impaired vaccine responses were observed after rituximab in ITP. This does not calibrate infection risk per day of depletion, nor demonstrate the incremental harm of a particular higher dose. [Nazi et al., 2013](https://pubmed.ncbi.nlm.nih.gov/23851398/).

A platelet response model must allow benefit to persist independently of total B-cell depletion if it is to evaluate the persistent-change hypothesis. Duration of depletion may inform the analysis, but maximizing it is not a primary comparator or selection objective.

## 8. Candidate models

### 8.1 A hierarchy that measures incremental value

| Model | Data and structure | Incremental question |
|:---|:---|:---|
| M0: arm-level endpoint | Protocol-defined response by randomized regimen; regularization and parsimonious baseline adjustment | What does the randomized comparison already support? |
| M1: dose-response endpoint | M0 plus justified pooling across dose levels under alternative shapes | What is gained by a shape assumption? |
| M2: dose–longitudinal platelet | Assigned regimen, baseline and platelet trajectories; continuous-effect and response/relapse alternatives | Do repeated platelets improve the clinical decision? |
| M3: PK–platelet | M2 with PK-driven effects and regimen simulation | Does PK improve on assigned regimen? |
| M4: PK–B-cell–platelet | M3 with a candidate peripheral depletion/recovery link | Does that biomarker improve the decision? |
| M5: marker extensions | Selected subset, autoantibody or immunoglobulin measurements with observation models | Which further measurements earn their cost? |

M0 can use independent beta-binomial arm estimates as a starting analysis. M1 compares a logistic curve in log dose, an Emax-type response curve with a ceiling, and a weakly constrained alternative. The logistic benchmark is not assumed to have a finite plateau or be suitable for untested schedule changes. With few arms, avoid fitting multiple flexible shape parameters without external information. M2 should include a parsimonious longitudinal mixed-effects model as well as the turnover structures below; none is automatically the reference truth.

### 8.2 PK and peripheral B cells

For intravenous administration, a candidate linear two-compartment PK model is

$$
V_c\frac{dC}{dt}=-CL\,C-Q(C-C_p)+I_{\rm IV}(t)+F k_a A_{\rm SC},\qquad
V_p\frac{dC_p}{dt}=Q(C-C_p).
$$

For subcutaneous administration, doses enter an absorption depot with $dA_{\rm SC}/dt=-k_aA_{\rm SC}$; for IV-only data that depot and its parameters are omitted. Concentrations have units mg/L, volumes L, clearances L/day, depot amount mg and $k_a$ day$^{-1}$. SC-only data may identify apparent parameters rather than $F$ and absolute clearance separately. Assess dose proportionality, late PK and time-dependent clearance; evaluate nonlinear target effects as alternative generating mechanisms or fitted models when justified.

A peripheral B-cell turnover candidate is

$$
\frac{dB_i}{dt}=k_{B,i}\{B_{0,i}-[1+E_B(C_i)]B_i\},\qquad B_i(0)=B_{0,i}.
$$

Here $k_B$ is day$^{-1}$, $B$ is cells/µL, and the dimensionless loss stimulus can be saturable, $E_B(C)=E_{\max,B}C/(EC_{50,B}+C)$, or proportional, $s_B C$. The low-concentration limit of the saturable form is proportional to $C$ with slope $E_{\max,B}/EC_{50,B}$. A log form $s_{\log}\log(1+C/C_*)$ is a separate empirical alternative, not an equivalent reduction; $C_*$ is a fixed concentration scale independent of the assay limit.

Choose the fitted form based on information in the nadir, early dynamics, recovery and PK. Censored nadirs do not establish a universal identifiability result. Use likelihood contributions for below-limit measurements, not zero or half-limit substitution.

Let $\alpha$ be a prespecified fraction of baseline used to describe recovery; 0.2 is an illustrative sensitivity-analysis threshold, not immune competence. For a patient depleted below that threshold at the end of the course, define

$$
T_{{\rm rep},i}=\inf\{t>t_{\rm last}:B_i(t)\ge\alpha B_{0,i}\}-t_{\rm last}.
$$

Report patients never depleted, or already recovered by course completion, separately. For observed data, recovery is interval-censored between visits or right-censored at last observation. Specify confirmation and absolute-count sensitivity criteria. Do not treat the first observed qualifying visit as the exact recovery time.

### 8.3 A parsimonious platelet layer

Use platelet concentrations $P_i$ in $10^9$/L and production $q_i(t)$ in $(10^9$/L)/day:

$$
\frac{dP_i}{dt}=q_i(t)-k_{P,i}\{1+\theta_i[1-\eta_i H_i(t)]\}P_i,
\qquad 0\le H_i,\eta_i\le1.
$$

$k_P$ is a reference loss rate in day$^{-1}$, $\theta_i\ge0$ describes excess baseline loss conditional on the production assumptions, and $\eta_i$ is removable excess loss. They are phenomenological parameters unless external evidence supports mechanistic interpretation. Background treatments may affect production, destruction or both through explicitly specified time courses.

At a constant untreated baseline, $P_{0,i}=q_{0,i}/[k_{P,i}(1+\theta_i)]$. Baseline counts therefore identify a ratio, not production and destruction separately. Literature priors on turnover can regularize the model; assess transfer uncertainty. Do not estimate a full set of patient-specific production, loss, delay and sensitivity parameters from sparse data without demonstrating recovery.

A precursor transit chain is optional only when production is perturbed and its lag matters, for example under an explicit TPO-RA model. A chain initialized at equilibrium with constant production contributes constant inflow and can be removed. ITP may involve impaired production as well as increased destruction; include such alternatives in simulation rather than interpreting this reduced loss model as complete disease biology.

### 8.4 Reversible and persistent drug-effect structures

The following low-dimensional alternatives make the persistence assumption explicit.

For M4, let $u_i(t)=\max[0,1-B_i(t)/B_{0,i}]$ and

$$
\frac{dZ_i}{dt}=k_{e,i}(u_i-Z_i),\qquad Z_i(0)=0.
$$

For an M3 suppression alternative, replace $u$ with a bounded concentration stimulus $f_S(C)$; M2 uses a regimen-specific bounded post-treatment input without individual PK. These alternatives test whether blood B cells add information rather than forcing the same mediator into every model.

For persistent benefit, introduce a separate state $R_i(t)$:

$$
\frac{dR_i}{dt}=k_{I,i} f_I(C_i)(1-R_i)-k_{R,i}R_i,
\qquad R_i(0)=0,\qquad f_I(C)=\frac{C}{EC_I+C}.
$$

$R$ denotes reduction of pathogenic activity consistent with persistent benefit, not the fraction of total B cells depleted. With $k_R=0$, an induced change remains after concentration has vanished and B cells have returned. With $k_R>0$, it decays on its own timescale. If $k_I=0$, no persistent component is induced. $k_I$ and $k_R$ are day$^{-1}$; $EC_I$ is mg/L. For M2, use a prespecified regimen input instead of $f_I(C)$ and restrict predictions to regimens its data support.

Compare suppression-only ($H=Z$), persistence-only ($H=R$), and a combined alternative

$$
H=1-(1-Z)(1-R).
$$

The combined form keeps the effect bounded while allowing persistence when $Z$ returns to zero. It is a candidate structure, not established immune biology. Avoid estimating both components unless the data and simulation justify it. A population mixture can assign no response ($\eta=0$), suppression-only and persistent-effect classes using prespecified class probabilities, with within-class variability limited by sample size. A continuous distribution of effects is a competing model; a logit-normal distribution can itself become bimodal on the original scale.

Dose dependence is explicit through assigned input and concentration in these dynamic models. If instead using a dose-dependent latent-class probability, specify its equation and distinguish it from the dynamic effect model; do not leave the dose-to-response connection implicit. Do not identify $\eta$ or a class probability with a long-lived plasma-cell fraction.

The exact zero-relapse component is a structural sensitivity case. Finite follow-up rarely distinguishes it from sufficiently slow relapse, so report persistence through $H$, with longer-term extrapolation separately labelled. A long transduction delay must not be used as the sole mechanism for all durable responses.

### 8.5 Optional tissue and antibody generating model

Use a tissue alternative to challenge the fitted peripheral link, rather than calling an unspecified chain the “full true model.” One explicit candidate is

$$
\frac{dC_T}{dt}=k_T(\rho C-C_T),\qquad
\frac{db_T}{dt}=k_{BT}\{1-[1+E_T(C_T)]b_T\},
$$

$$
\frac{da}{dt}=k_A\{\phi+(1-\phi)b_T(1-R)-a\},\qquad
\frac{dP}{dt}=q(t)-k_P(1+\theta a)P.
$$

Here $C_T$ is mg/L, $\rho$ is a dimensionless partition factor, $b_T$ is tissue B cells relative to baseline, and $a$ is normalized pathogenic antibody activity. Initial values are $C_T=0$, $b_T=a=1$ and $R=0$. All $k$ values are day$^{-1}$; $E_T$ is a dimensionless saturable loss stimulus. $R$ follows Section 8.4 with an explicitly chosen serum or tissue concentration input. $\phi\in[0,1]$ is residual antibody production in this generating mechanism, not a clinical nonresponse probability.

When $R=0$, tissue recovery restores antibody production. A persistent $R>0$ permits lower pathogenic production despite recovery of total tissue B cells. Vary tissue exposure, potency and recovery independently of peripheral parameters to create meaningful blood–tissue discordance. Also generate data from models without this antibody chain. Robustness to one additional tissue lag is not sufficient evidence for robustness to structural error.

### 8.6 Observation, variability and treatment-management models

Specify a parameter manifest for each simulation scenario before generating data: fixed values and units, random-effect distributions and correlations, class probabilities where used, initial conditions, dosing, visit times, assay limits, treatment rules and random seed. Source-informed values carry source and uncertainty; deliberately hypothetical values are labelled. Priors used for fitting are recorded separately from generating values.

A baseline longitudinal observation candidate is

$$
\log P^{\rm obs}_{ij}=\log P_i(t_{ij})+w_i(t_{ij})+\epsilon_{ij},
$$

where $w_i$ is a mean-zero biological fluctuation process with covariance $\sigma_w^2\exp(-|t-s|/\tau_w)$ and $\epsilon_{ij}$ is independent assay error. This distinguishes temporally correlated fluctuations from measurement error. Specify how low or zero reported counts are censored. More realistic process-noise alternatives can replace this model in stress scenarios. The clinical endpoint is evaluated from simulated protocol observations, not just a smooth latent mean.

PK and B-cell likelihoods include their measurement errors and limits. Marker extensions require assay-specific observation equations; total IgG is not equated with $a$. Prebaseline observations inform initial state uncertainty rather than forcing equilibrium in every patient.

Background treatment, rescue and dropout are part of the generating process. Specify their rules and effect durations in each scenario. Model post-rescue observations through those effects, or use a prespecified primary endpoint analysis with rescue classified as failure and a separate sensitivity analysis for the latent platelet course. No fit may quietly treat informative post-rescue missingness as random.

## 9. Data and design requirements

| Requirement | Decision it supports | Consequence if limited |
|:---|:---|:---|
| Concurrent randomized expansion regimens | Causal comparison of studied options | Observational contrasts need stronger assumptions |
| Informative regimen coverage | Dose-response shape or schedule effects | Two doses may support only their direct comparison |
| Dosing, sampling and adherence records | PK and regimen simulation | Exposure uncertainty increases |
| Multiple pretreatment platelet counts and treatment history | Baseline state and fluctuation estimates | Severity and treatment effects are harder to separate |
| Platelet sampling aligned with endpoint | Onset and durable-control classification | Sparse visits can miss instability or delay confirmation |
| Background-treatment and rescue dates, doses and reasons | Attribution and protocol-policy simulation | Drug-specific effects may be unresolved |
| Follow-up after investigational treatment | Durability and treatment-free control | Early response does not establish persistence |
| Follow-up after B-cell recovery in enough patients | Distinguishing suppression from persistent benefit | The reset interpretation remains uncertain |
| Late PK and B-cell measurements | Peripheral recovery model | Tail and recovery parameters may be prior-dominated |
| Immunoglobulins, infections, bleeding and discontinuations | Clinical acceptability and immune burden | Output may be restricted to an efficacy shortlist |
| Optional subsets, autoantibodies, IPF and absolute immature counts | Mechanism discrimination | Value assessed by model ablation and design simulation |

There is no universal fatal requirement for three doses, a fourfold or eightfold dose range, or complete recovery in every patient. Choose sampling and dose range to resolve the intended decision. Weekly early platelet/B-cell visits and monthly later immune visits are candidate schedules to test, not blanket requirements. An early dose decision and longer immune follow-up can have different data cuts.

## 10. Identifiability, priors and validation

Check practical identifiability at the level of the intended predictions as well as individual parameters. Confounding among baseline production/loss, drug sensitivity, induction delay and relapse is expected. PK parameters, recovery rates and persistent-response fractions may remain uncertain even with many repeated measurements.

Use prior predictive simulations, parameter-recovery studies, posterior coverage, sensitivity to plausible prior widths and structures, and stability of regimen predictions. Fixing a parameter is an assumption to challenge, not evidence it is known. Record empirical Bayes shrinkage and covariance; EBE correlations alone cannot establish identifiability. Mixture fits also require checks for unstable classes, label switching and prior-driven allocations.

For Bayesian fits, prespecify computational diagnostics and remedial actions, including convergence, effective sample sizes and divergent transitions where relevant. For likelihood fits, use profiles and numerical conditioning where appropriate. Diagnose fits before scoring; include computational failures in the operating-characteristic denominator under the fallback policy.

Evaluate held-out patients and, where feasible, dose groups or cohorts. Do not validate generalization by randomly withholding individual counts while retaining the rest of the same patient's trajectory. Check response onset, count distributions, autocorrelation, rescue frequency, durable response and immune recovery, not just mean platelets. Good predictive fit within the observed window does not validate post-recovery extrapolation.

## 11. Exposure–response confounding and pooling

Fixed dosing is not randomization. Expansion arms should be concurrently randomized, and escalation borrowing requires compatible populations and management. Differences in calendar time, disease phase, prior treatment and background therapy can imitate a dose response. Compare pooled fits with expansion-only fits and robust or discounted borrowing. If escalation results determine expansion choices, simulate that adaptation.

Individual exposure can correlate with prognosis because of clearance, body size, target burden or disease state. Testing baseline circulating B cells as a clearance covariate does not establish that all relevant confounding is controlled. Anchor inference in assigned-regimen contrasts; examine within-arm exposure associations and sensitivity to shared PK–outcome determinants and time-varying clearance.

Forward simulation under a dose is necessary for regimen prediction but does not remove bias from a confounded fitted exposure effect. Integrate over a common target covariate distribution and propagate PK uncertainty. Do not condition alternative-dose predictions on the patient's actual postbaseline IgG or B-cell trajectory as if it would remain unchanged under the alternative treatment.

## 12. Fitting and deriving the endpoint

Fit M0 and M1 directly to the protocol endpoint. Fit M2–M5 to longitudinal and event data, then derive exactly the same endpoint by simulating visits, biological variability, assay error and treatment-management events. Compare decision performance rather than assume a continuous model wins because it uses more observations.

A binary endpoint discards some trajectory information, but the size of the loss depends on the data-generating mechanism. If a perfectly observed latent class contains all information about dose response and within-class trajectories contain none, the remaining information is Bernoulli. That is a special case, not a universal ceiling on every longitudinal model. Onset, within-class effect and relapse may carry additional information. True low-count episodes relevant to the endpoint must not be smoothed away as measurement mistakes.

When rescue defines failure, it is part of the endpoint. When estimating a hypothetical no-rescue trajectory, state the additional assumptions and report that estimand separately. Rescue decisions can depend on bleeding, prior counts, trends and clinical practice as well as current count. Treatment-policy simulations must represent the dependencies that materially change the endpoint.

Prespecify death, discontinuation and missing-visit handling. Test sensitivity to informative dropout and visit frequency. A clinical endpoint with bleeding or successful treatment withdrawal cannot be reconstructed from platelets alone without the additional event information or explicit assumptions.

## 13. Regimen selection rule

### 13.1 Efficacy acceptability

Let $\mathcal R$ be the prespecified set of studied regimens remaining after the clinical safety exclusions. Apply the prespecified exclusion policy before computing the efficacy reference maximum; an excluded regimen must not set an unattainable efficacy requirement for the permissible options. For posterior draw $m$, compute target-population endpoint probabilities $p^{(m)}(r)$ and the within-draw maximum $p_*^{(m)}=\max_{r'\in\mathcal R}p^{(m)}(r')$. If no regimen remains, stop without a recommendation. Otherwise estimate

$$
Q(r)=\Pr\{p(r)\ge p_{\min}\ \text{and}\ p(r)\ge p_* -\Delta\mid\mathcal D\}.
$$

A regimen is efficacy-eligible if $Q(r)\ge q$. The minimum efficacy $p_{\min}$ prevents selecting an ineffective regimen merely because all options are similar. $\Delta$ is the acceptable absolute loss, not a significance threshold. The maximum is computed within each posterior draw; uncertainty is not removed by substituting the maximum posterior mean.

For initial **method-development scenarios only**, vary $p_{\min}$ over 0.30 and 0.40, $\Delta$ over 0.05 and 0.10, and $q$ over 0.80 and 0.90. These values are illustrative inputs to explore tradeoffs, not clinical recommendations. Actual values require clinical agreement for the selected endpoint and population.

### 13.2 Safety, immune recovery and burden

Apply prespecified clinical safety exclusions before recommending a regimen. Among efficacy-eligible options, evaluate a burden vector containing administered amount, administrations, duration of depletion, immunoglobulin impairment and observed or externally informed adverse outcomes. Total depletion time is a surrogate burden measure, not a predicted infection count.

A weighted burden $B(r)=\sum_j\lambda_j b_j(r)$ may rank eligible regimens only when the component scales and weights are explicit and clinically agreed. Avoid double-counting correlated immune measures. Evaluate alternative weights and external risk assumptions; a small trial cannot precisely establish rare-event equivalence. When no defensible common weighting exists, return the nondominated eligible options with their efficacy and burden uncertainty. For otherwise comparable regimens, lower dose or fewer administrations can be a prespecified tie-breaker.

### 13.3 Inconclusive outcomes and comparators

If no regimen is eligible, distinguish evidence of inadequate efficacy from insufficient precision. Return “no eligible regimen” or an inconclusive shortlist and the next informative design; do not default silently to the highest dose. If all model fits fail, use the prespecified M0 fallback when valid, otherwise return inconclusive. Report the fallback frequency.

Apply this same selection framework to M0–M5. Use highest clinically acceptable dose and empirical highest response as descriptive benchmarks, not the only competitors. A biomarker-only benchmark, if included, tests the historical practice of relying on depletion; it does not define the clinical objective. No primary benchmark should maximize depletion duration.

## 14. Sample size: illustrations and the unanswered question

### 14.1 Selecting a higher response rate is not selecting a near-optimal regimen

With two equal arms and ties split fairly, the exact probability of selecting the arm with the higher true response rate is

$$
\sum_{k=0}^{n}\Pr(X_H=k)\{\Pr(X_L<k)+\tfrac12\Pr(X_L=k)\}.
$$

| Higher true rate | Lower true rate | Patients per arm | Exact probability of selecting higher rate |
|---:|---:|---:|---:|
| 55% | 45% | 20 | 73.57% |
| 55% | 45% | 40 | 81.43% |
| 55% | 50% | 141 | 79.97% |
| 55% | 50% | 142 | 80.05% |

These calculations show sampling uncertainty under a narrow objective. The 142-per-arm value is the exact minimum for 80% selection in the last comparison. By contrast, an approximate two-sided 5% superiority test at 80% power for 50% versus 55% requires 1,565 per arm. Neither calculation establishes what is needed for Section 13's joint minimum-efficacy and near-optimality rule. At a true effect exactly on an acceptability boundary, demanding high posterior certainty about its side is a distinct problem.

### 14.2 What a simple shape assumption can contribute

Consider five twofold-spaced dose levels, four escalation patients at each, and 20 additional expansion patients at each of the highest two. Under a correctly specified two-parameter logistic curve in log dose, with top response 55% and next response 45%, a Fisher-information calculation gives a local variance ratio of **5.23** for the contrast between those doses versus unpooled estimates at the top two doses. Both estimates use 24 patients at each top dose; only the pooled fit also uses the 12 patients at lower doses.

This is an illustrative binary dose-response calculation. It contains no PK, B cells or longitudinal platelets. The apparent gain comes from borrowing under a strong shape assumption. The logistic has no finite plateau boundary and approaches one at arbitrarily high dose; it is not a validated efficacy shape for this drug class. Different shapes, poor exchangeability and finite-sample fitting can change both variance and bias.

Do not convert this variance ratio into a claim that a PK–platelet model saves a factor of two to five patients or makes 20 per arm sufficient. Incremental savings must compare models under the same decision, total allocation and follow-up, with misspecification included.

### 14.3 Reproducibility and reporting

[`scripts/specification-calculations.R`](scripts/specification-calculations.R) reproduces the exact two-arm selection probabilities, approximate superiority sizes and illustrative logistic variance ratios using base R. Run `Rscript scripts/specification-calculations.R` from this project directory. These calculations are separate from the decision simulation in Section 15.

Estimate sample-size or follow-up savings only after defining acceptable decision performance, including efficacy loss, burden and inconclusive outcomes. Report scenario-specific results and uncertainty; do not promise a single saving across biological mechanisms.

## 15. Simulation study

### 15.1 Define complete scenarios before fitting

For each scenario, freeze the manifest described in Section 8.6 and the clinical decision inputs in Section 13. It must include background-treatment and rescue policies, missingness, observation error and parameter distributions, not just mean ODE trajectories. Define a large Monte Carlo target population to estimate true $p(r)$ and burden for each regimen, with numerical error small relative to the decision tolerance. No “true plateau bottom” is required.

Start with a deliberately small debugging set, then vary escalation levels (3 or 5), patients per level (3 or 6), expansion size (20 or 40 per arm), regimen placement and follow-up (6 or 12 months). Add longer immune follow-up scenarios when recovery is rarely observed by 12 months. Compare two tested doses separately from comparisons involving course length or spacing.

### 15.2 Required biological and design alternatives

| Scenario family | What must be challenged |
|:---|:---|
| Reversible suppression | Relapse follows loss of suppression; persistent-effect fits may overpredict durability |
| Persistent benefit | Control persists despite early B-cell recovery; suppression-only fits may favor unnecessary depletion |
| Mixed responses | Nonresponse, transient response and persistent response coexist |
| Continuous heterogeneity | No true discrete classes; mixture assumptions may mislead |
| All doses on efficacy plateau | Immune burden still differs; larger dose need not be better |
| Rising efficacy over studied range | No exact plateau exists; assess whether more information or another regimen is needed |
| No worthwhile regimen | Prevent near-equality from being mistaken for adequate efficacy |
| Blood–tissue discordance | Vary tissue potency, exposure and recovery, not only a delay |
| Production and management effects | TPO-RA tapering, steroids and rescue alter count trajectories and endpoint success |
| PK misspecification | Nonlinear or time-dependent clearance and PK–prognosis correlation |
| Informative observation | Rescue, bleeding-driven visits, dropout and correlated platelet fluctuations |
| Cohort nonexchangeability | Escalation differs from expansion; pooling may increase bias |
| Adaptive expansion choice | Dose selection based on escalation changes the observed contrast and uncertainty |

Include both source-calibrated and deliberately adverse but plausible cases. Do not generate every dataset from a close relative of the preferred fitted model. Use model ablation to isolate the contribution of PK and each immune marker; test serial autoantibody availability and assay-negative selection without presuming a fixed sensitivity or guaranteed benefit.

### 15.3 Fit and decide fairly

Fit M0–M4 to the same simulated patients using the measurements each model permits; add M5 only for selected informative scenarios. Give simple comparators the same eligible cohort information and baseline adjustments. Apply the same selection rule, target covariate distribution, and fallback policy. Predictions for untested regimens are a separate analysis because M0 cannot make those extrapolations.

Record computational diagnostics, calibration and sensitivity to priors. Use a prespecified limited retry policy; retain failed fits in the trial denominator. Evaluate the effect of choosing a model from the data, if model selection will be part of the actual workflow, rather than reporting only the best model in hindsight.

### 15.4 Score decision value

Report probability of selecting a truly efficacy-acceptable regimen, probability and magnitude of efficacy loss beyond $\Delta$, selection below $p_{\min}$, unnecessary burden, expected clinical loss, and the probability of an inconclusive or failed decision. An inconclusive result is not counted as successful selection. Report the quality and coverage of any returned shortlist as well as final selections.

Evaluate a scenario-specific loss such as

$$
L(r)=w_0[p_{\min}-p(r)]_+ + w_1[p_*-p(r)-\Delta]_+ + B(r),
$$

with $[x]_+=\max(x,0)$, explicit scales and weights, and a separately specified cost for deferral. This is a sensitivity-analysis template, not an established clinical utility function. Report its individual components so conclusions do not depend on an opaque weighted total. Also report calibration and interval coverage, response/relapse predictions and immune recovery error.

Use at least enough replicates for the required precision. For orientation, 2,000 independent simulated trials at an operating characteristic of 0.8 yield a Monte Carlo standard error of about 0.009. Report intervals and paired uncertainty for between-method differences, using common generated trials where possible. Pilot runs may be smaller but cannot support final decision claims.

### 15.5 Deliverables

Produce a main comparison of decision performance versus sample size and follow-up, separated by persistence mechanism. Include sensitivity tables for safety/burden weights, priors, dose coverage and misspecification; a failure/inconclusive-rate table; and a measurement-ablation summary. A favorable average must not hide substantial harm in a plausible subgroup of scenarios.

## 16. External plausibility checks

Published aggregate data can constrain plausible response and recovery patterns but cannot validate a generic compound's dose-response curve. Reproduce the relevant population, dosing, background therapy, observation window and endpoint before comparison. Retain uncertainty and separate sources used to set priors from independent checks.

**Ianalumab/VAYHIT2.** Reported 12-month freedom from treatment failure was 54% at 9 mg/kg and 51% at 3 mg/kg, with substantial uncertainty and eltrombopag management incorporated into the trial. These observations support considering a small efficacy difference, not declaring equivalence or requiring a plateau below 3 mg/kg. [Primary trial report](https://pubmed.ncbi.nlm.nih.gov/41363800/).

**Rituximab regimens and follow-up.** Compare low- and standard-dose reports only after checking populations, endpoints and concomitant treatment. Similar pooled response rates do not establish equivalence. Long-term response and recovery observations can challenge predictions of inevitable immediate relapse or guaranteed permanent reset; they do not identify the precise persistent-response mechanism. [Long-term follow-up](https://pubmed.ncbi.nlm.nih.gov/22566601/).

A failure of a design-matched check prompts investigation of assumptions and uncertainty. A mismatch to one aggregate point estimate is not by itself proof that a model is wrong. Do not require unobserved doses to have a particular efficacy merely to pass a check.

## 17. Findings that would limit or negate value

**The biomarker chain adds no value.** If peripheral B cells do not improve calibrated decisions beyond M3, omit that efficacy link. This does not rule out direct PK–platelet or dose–platelet models.

**PK adds no value.** If M2 performs as well as M3 for studied-regimen decisions, use M2 for that decision. PK may still be useful for a separate schedule or exposure question, subject to validation.

**The decision is assumption-driven.** If acceptable changes to priors, persistence structure or cohort borrowing change the recommendation materially, report the range of plausible decisions and the data needed to resolve it. Prior dominance does not imply equivalence to raw arm rates; it can create a very different and overconfident recommendation.

**The study does not identify attribution or persistence.** Dominant background effects, poorly recorded rescue, lack of randomized contrast or follow-up ending during depletion may prevent a credible drug-specific or post-recovery conclusion.

**A simpler method is adequate.** If a simpler model delivers comparable clinical loss, calibration and timeliness, a more complex chain is not justified for this use. Conversely, a curve still rising at the top dose does not automatically make every model useless: the value may lie in detecting an unresolved decision rather than naming a plateau.

**Benefit–risk remains unresolved.** When immune safety information is inadequate, return an efficacy shortlist and explicit remaining tradeoffs rather than claim a benefit–risk optimum. Negative and inconclusive evaluations are valid deliverables.

## 18. Milestones

1. **Finalize the decision framework.** Write the endpoint, population, regimen set, treatment-management policy, clinical tolerances and inconclusive policy. For generic simulations, label a finite grid of hypothetical settings.
2. **Audit decision-critical sources and data.** Verify endpoint definitions, parameter units, prior populations and relevant immune follow-up. Record access and verification limitations. Inspect available real-data trajectories and management events.
3. **Build simple baselines.** Implement M0 and M1, then a parsimonious M2. Reproduce Section 14's calculations and establish a common decision function.
4. **Specify complete generating cases.** Implement suppression, persistent benefit and major structural alternatives with parameter manifests and observation/management processes. Use prior predictive checks rather than fixing every literature value.
5. **Add PK and immune models incrementally.** Implement M3 and M4 only after lower-level checks, calibrating late PK, depletion and recovery. Confirm that persistent models retain benefit after total B-cell recovery.
6. **Run pilot recovery and decision checks.** Establish failure handling, numerical stability and plausible endpoint distributions before the larger simulation.
7. **Run the prespecified comparison and sensitivity analysis.** Report decision loss, acceptability, calibration, inconclusive decisions and measurement value.
8. **Perform external checks and clinical review.** Assess transfer limitations and determine whether the output supports a shortlist, a regimen choice or another study design.

No milestone guarantees a particular model will win. Exploratory fitting to available real data and simulation can proceed iteratively; real-data fitting need not wait for an assumed full mechanistic model to pass.

## 19. What previous modelling attempts establish

The reference search found relevant regulatory and published modelling examples. Its incompleteness does not establish that no other PK–platelet model exists. These examples show feasibility constraints and differing uses, not a general rule that destruction-blocking therapies have binary effects or cannot be modelled continuously.

| Example | Evidence and interpretation | Verification basis |
|:---|:---|:---|
| Fostamatinib | FDA records failure of attempted continuous platelet models; design and exposure-response interpretation require attention to titration and outcome timing | Earlier project reading of FDA/EMA reviews; FDA search extract corroborated in the critical review |
| Efgartigimod | PMDA describes insufficient explanation of between-patient platelet variation for Phase 2-based regimen simulations; IgG reduction informed the subsequent regimen | PMDA Section 6.R.1 checked during critical review |
| Rilzabrutinib | Earlier notes describe a longitudinal model in 305 pooled patients supporting an already chosen regimen; a continuous association did not establish a durable-endpoint dose contrast | Earlier project reading; full FDA PDF was not retrievable during critical review, so detailed extraction still needs audit before reuse |
| Eltrombopag | Published modelling includes a nonresponder mixture and simulation of response-guided dosing; some platelet parameters were fixed | PAGE poster read in earlier project; paper and transfer assumptions require checking |
| Romiplostim and other TPO-RAs | Candidate sources for production and turnover structures | Relevant source must be read before transferring parameter values |
| Animal IVIg models | Mechanistic precedents for antibody-related platelet effects | Biological context, not direct quantitative validation for a human B-cell depleter |

Primary regulatory sources: [FDA fostamatinib review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2018/209299Orig1s000MultidisciplineR.pdf), [EMA fostamatinib assessment](https://www.ema.europa.eu/en/documents/assessment-report/tavlesse-epar-public-assessment-report_en.pdf), [PMDA efgartigimod review](https://www.pmda.go.jp/files/000273743.pdf), and [FDA rilzabrutinib review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2025/219685Orig1s000IntegratedR.pdf). The eltrombopag precedent is [Hayes et al., 2011](https://doi.org/10.1177/0091270010383019).

The efgartigimod Phase 2 study had 38 patients, below the proposed total of 49–110; 305 patients is several times that total, not ten times. Neither comparison defines a universal minimum sample size. [Phase 2 primary report](https://pubmed.ncbi.nlm.nih.gov/31821591/).

A model can be useful for supporting a regimen, predicting durability, interpreting an interruption or designing the next study even when it did not originally select a dose. Differences between production and destruction mechanisms, titration, cohort design and endpoint choice should be investigated as explanations rather than asserted as proven causes of success or failure.

## 20. Intended use and decision on further work

This specification is for a pharmacometrician and clinical team evaluating whether escalation and expansion data can support a Phase 2 dose or regimen choice for a B-cell depleting agent in ITP.

The strongest opportunity is a study with credible regimen contrasts, informative longitudinal response or relapse, recorded background treatment and sufficient follow-up to assess the desired durability. A model may help retain benefit while reducing unnecessary depletion or shortening a course. Peripheral biomarker saturation does not remove that opportunity, but it limits what the biomarker can establish.

Proceed with the model hierarchy and competing persistence mechanisms. Advance to a joint PK–B-cell–platelet model only when it improves a clinically relevant decision robustly over simpler methods. The deliverable may be a regimen recommendation under agreed clinical tradeoffs, an efficacy shortlist, evidence that a simpler analysis is sufficient, or a design for obtaining the missing information. Sample-size savings and a recoverable plateau boundary are possible findings, not premises.
