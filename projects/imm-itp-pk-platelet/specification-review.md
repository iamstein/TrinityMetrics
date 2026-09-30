# Critical review of specification.md

Review date: 14 September 2026. Scope: all 20 sections, the opening summary, the calculation script, and relevant entries in references.qmd. This review describes the specification before revision; the specification was subsequently updated in response, and the findings below are preserved as the revision rationale. This is a scientific and methodological review, not a fitted analysis or a compound-specific dose recommendation. Selected primary sources were checked; this is not a complete verification of the reference collection. The conclusions below rest on the equations, calculations and evidence, not on which model wrote the original document.

**Overall assessment.** A PK–platelet model could be valuable, but the specification is not ready to serve as an analysis plan. Its strongest elements are the decision focus, recognition of peripheral biomarker saturation, attention to rescue and concomitant therapy, and proposal to evaluate operating characteristics before relying on a model. Its central conclusions are substantially more confident than its evidence supports. Most importantly, its equations encode reversible suppression, its proposed dose decision concerns near-maximal efficacy, and its sample-size calculations concern selecting the largest response rate. These are three different problems.

The project should ask whether longitudinal platelet data, PK, and immune measurements improve a clinically relevant dose-and-regimen decision over simpler analyses of the same patients. It should not begin by assuming that depletion duration is the necessary efficacy mediator, that a responder mixture is the correct biology, or that the model will save half the patients.

**1. The reset objection changes the model, not just its introduction — critical.**

Your objection is correct conditional on the premise: if a lower dose produces the same durable reset, prolonging depletion has no added efficacy value and may impose additional immune impairment. The goal is durable disease control with acceptable immune recovery. Duration of circulating B-cell depletion can still be informative, but it is neither the therapeutic objective nor an established surrogate for it.

The distinction between a hypothesis and a demonstrated fact matters. In a rituximab follow-up study, prolonged depletion was associated with sustained response; that observational association does not establish that increasing dose to extend depletion causes better remission. Tissue studies also identify surviving memory B cells and newly generated B cells in relapse. These findings support competing mechanisms rather than a universal reset or universal suppression story. [Patel et al., 2012](https://pubmed.ncbi.nlm.nih.gov/22566601/); [Crickx et al., 2021](https://pubmed.ncbi.nlm.nih.gov/33853929/).

The reduced model in Section 8.4 cannot produce lasting remission after immune reconstitution:

\[
B/B_0\to1\quad\Rightarrow\quad u\to0\quad\Rightarrow\quad Z\to0
\quad\Rightarrow\quad k_{\rm dest}\to k_{\rm dest,0}(1+\theta_i).
\]

With unchanged platelet production, platelets ultimately return to their pretreatment equilibrium. A very slow decay of Z can mimic persistence during limited follow-up, but that is delayed relapse, not a reset. The full model has the same problem if tissue B cells return to baseline: autoantibody production returns to its baseline rate. Neither model distinguishes healthy repopulation from restoration of pathogenic immunity.

Consequently, selecting on predicted platelets rather than B-cell counts does **not** remove the bias toward longer depletion. The bias is already inside the model translating B cells into predicted platelets.

At minimum, compare three generative hypotheses: reversible suppression; a durable change in pathogenic activity that persists after total B-cell recovery; and a mixture of durable responders, transient responders and nonresponders. A reset component need not be a detailed immune systems model. A persistent latent response state with a separate relapse process is enough to test whether the decision depends on allowing this possibility. Describe it as durable remission consistent with reset; the available measurements cannot prove immune tolerance has been restored.

**2. Excluding safety undermines the intended dose decision — critical.**

Sections 6.4 and 15 call a higher-than-needed dose the cheap error. That is an assumed value judgment, not a consequence of the model. A tolerable dose range established during escalation does not imply equal long-term infection risk or immune recovery across doses.

The user's phrase “infection time” should be expressed as duration of immune impairment or susceptibility, not duration of actual infection. B-cell count is not a calibrated infection-risk measure. An ITP rituximab study found impaired vaccine responses after treatment, providing a direct reason to consider immune function, although it does not quantify the incremental infection harm of a particular higher dose. [Nazi et al., 2013](https://pubmed.ncbi.nlm.nih.gov/23851398/).

A small study need not fit a complex infection model. It should nevertheless carry observed infections, serious infections, immunoglobulin trajectories, relevant immune recovery measures and treatment burden into the decision, with external assumptions or sensitivity analyses where necessary. If none of this enters, call the output an **efficacy-based dose shortlist**, not an optimal dose or a benefit–risk optimum.

The dose unit should also be reconsidered. For a short-course depleter, amount per administration, number of administrations and spacing may have different consequences. A model can be valuable for choosing a shorter course even if the two tested per-administration doses have similar response rates.

**3. The clinical decision and estimand need to be fixed before the model — critical.**

The document alternates between highest response probability, an exact plateau boundary, the lowest dose within five percentage points of the best, and a choice a later trial would confirm. These objectives are not interchangeable. A later finite trial is also noisy; agreement with its winner is not a definition of biological truth.

Define the target population, regimen set, follow-up horizon, background-treatment policy, response window, rescue rules and clinically acceptable efficacy loss. For a reset-oriented programme, a particularly relevant outcome is sustained platelet control after the investigational course and protocol-defined withdrawal of background treatment. Durable control while a TPO-RA is maintained answers a different question.

A workable efficacy criterion would assess, jointly over posterior draws,

\[
\Pr\{p(r)\ge p_{\min},\quad p(r)\ge \max_{r'\in\mathcal R}p(r')-\Delta\mid\mathcal D\}\ge q,
\]

then choose among eligible regimens using safety, immune recovery and burden. Here p refers to the fully specified endpoint in the same target population. The minimum efficacy requirement matters: when every regimen is ineffective, merely being within five points of the maximum can still select one. The maximum should be evaluated within each posterior draw, not treated as a known maximum of posterior means.

The present five-point tolerance and 80% posterior threshold are reasonable simulation inputs, not established clinical standards. Calibrate them. Specify what happens when no regimen meets the criteria: retain two candidates, gather more information, or stop. Permit an inconclusive result rather than forcing every dataset to name a dose.

**4. Section 14 does not establish sample-size savings for PK–platelet modelling — critical.**

I reran scripts/specification-calculations.R and independently evaluated the two-arm binomial selection probability. With equal allocation, true response rates 55% and 45%, and fair random resolution of ties, it is 73.57% at 20 per arm and 81.43% at 40 per arm. These are valid illustrative probabilities of choosing the arm with higher efficacy. They are not power calculations, evidence of near-equivalence, or probabilities of selecting the lowest acceptable dose.

The section correctly distinguishes selection from hypothesis testing, then abandons that distinction for its plateau claim. The 1,565-per-arm number is a conventional superiority-test calculation for 50% versus 55%. Under the section's own 80% correct-selection criterion, the corresponding exact minimum is 142 per arm. Neither number answers the five-point near-optimality decision. At a true difference exactly equal to a chosen margin, requiring confident classification relative to that boundary is intrinsically different from selecting the better arm.

The reported pooling factors are reproducible: with 20 expansion patients plus four escalation patients at each of the top two doses, the local Fisher-information ratio is approximately 5.23 for a ten-point difference. However, that calculation contains **no PK, B cells, platelet trajectories, rescue or immune reset**. It is a two-parameter logistic regression on binary response across five doses. Its gain demonstrates the potential value of imposing a dose-response shape, not the incremental value of PK–platelet modelling.

The baseline variance in that calculation also includes the four escalation patients at each expansion dose, despite prose that describes the comparator as the expansion arms alone. The selection table and information-ratio calculation therefore do not even use exactly the same arm sizes. The simple binary model must be an explicit comparator using the same patients and decision rule.

Further limitations:

- A local asymptotic variance ratio cannot be directly converted into finite-sample savings for a nonlinear posterior decision involving a maximum and a tolerance.
- A logistic curve linear in log dose has no finite plateau boundary and approaches response probability one, unless an additional ceiling is introduced. It is not the platelet model proposed in Section 8.
- The table reports the first passing sample size on a coarse grid, not exact required sample sizes; its Monte Carlo estimates also have uncertainty.
- “Nothing to gain” at larger dose differences is too strong: a model might reduce follow-up, change the course length, improve calibration or support a lower-dose choice.
- A wrong shape can be harmful, harmless or modestly inefficient. “Worse than without” is a scenario outcome to measure, not a universal property.

Delete the headline claims that 20 patients per arm become sufficient and that the model saves a factor of two to five. Retain the arithmetic as a deliberately simplified demonstration, clearly separated from the operating characteristics still to be evaluated.

**5. The efficacy biology is overcommitted to an unproven responder mixture — major.**

The document repeatedly treats response as essentially binary because a responder's platelets return to normal. A binary trial endpoint does not prove a two-class biological mechanism. Dose can influence response probability, onset, depth, variability, rescue needs and relapse timing in different combinations. Complete response under a trial threshold is also not synonymous with normalization.

A mixture is a useful candidate. It should compete against a continuous distribution of effect, a longitudinal response model and a response/relapse model. The cited eltrombopag mixture itself weakens the claimed distinction between production drugs with graded effects and destruction drugs with binary effects.

The “Bernoulli ceiling” is valid only under a particular factorization: once a perfectly observed latent response class is known, the remaining data carry no additional information about dose-response parameters. If trajectories carry information about relapse, severity, exposure sensitivity or dose-dependent dynamics within a class, that assumption fails. Conversely, if the target is the actual protocol-defined endpoint, true low-count episodes cannot simply be smoothed away as classification mistakes. Simulate the observation process used to determine response.

The identification of the long-lived plasma-cell fraction with the nonresponder proportion is also unsupported. A within-person fraction of pathogenic antibody production is not a population probability of response. At equilibrium, the response threshold also depends on platelet production, baseline disease severity and the treatment effect. Long-term relapse proportions cannot identify the fraction of antibody production from long-lived plasma cells. Splenic plasma-cell evidence supports a possible resistance mechanism, not that numerical mapping. [Mahévas et al., 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3533302/).

**6. Several biomarker claims are stronger than their biological or measurement basis — major.**

Total IgG cannot identify the pathogenic plasma-cell floor. Stable bulk IgG is compatible with a substantial reduction in a small pathogenic antibody fraction. A fall in total IgG likewise need not imply loss of the pathogenic fraction. Use total IgG principally for immune safety and as an exploratory predictor; a mechanistic link to pathogenic antibody production requires independent evidence. A postbaseline IgG trajectory also cannot simply be held fixed when simulating a different dose.

Peripheral B cells are a measured pharmacodynamic marker, not an established obligatory mediator of the platelet effect. Counts below quantification are censored and provide bounds; they are not “near-noiseless.” When all counts are below the limit, potentially relevant differences are precisely what cannot be observed. Blood–tissue discordance would weaken this biomarker link, but it would not invalidate a direct model relating randomized dose to platelet outcomes.

Autoantibody measurements could help, but MAIPA positivity does not make the latent A(t) state directly observed without a measurement model. Platelet-bound and free serum antibodies are different measurements; assay signal, binding, specificity, censoring and sampling feasibility matter. Baseline positivity can define a selected subgroup, and assay negativity is not absence of pathogenic immunity. A modern primary study illustrates that performance depends on test and population; a fixed universal sensitivity is inappropriate. [Al-Samkari et al., 2020](https://pubmed.ncbi.nlm.nih.gov/31891657/).

IPF is valuable supportive information, but IPF percentage equals immature platelets divided by total platelets. It can decline because the denominator rises. It does not by itself identify production and destruction rates; add absolute immature platelet counts and an observation model if pursuing that separation. BAFF and glycocalicin should likewise be described as candidate markers rather than validated measures of tissue depletion or destruction rate. Also correct the BAFF row: the specification elsewhere correctly names BAFF-R as ianalumab's target.

The claim that anti-GPIb/IX specificity predicts poor IVIg response needs qualification: a primary retrospective study did not confirm this as a reliable predictor. [Rogier et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32630482/). No intermediate layer should be declared to “clearly win” before testing its incremental decision value.

**7. The equations need repair and simplification before implementation — major.**

The supposed full generative model is incomplete. There is no equation for tissue B cells, no explicit dose dependence of the eta distribution, no complete random-effect specification, and no observation or treatment-management process. Section 15 asks for varying plateau locations on eta that Sections 8.1–8.3 do not define. Thus the proposed simulation cannot yet be implemented unambiguously.

There are also specific mathematical issues:

- At low concentration, Emax C/(EC50+C) is approximately (Emax/EC50) C. This is linear in concentration, not log-linear. S log(1+C/Cref) only reduces to a linear form when C is also small relative to Cref. The proposed log form is an alternative model, not an algebraically equivalent one-parameter reduction over the relevant range.
- Setting Cref to an assay's quantification limit ties the response curve's curvature to an analytical property. Changing that limit changes the shape in a way a single slope generally cannot undo. Use a fixed concentration scale and test alternatives.
- An unquantifiable nadir does not universally imply that only a ratio is identifiable; early dynamics, recovery and sufficiently informative PK can change the result. Conversely, a quantifiable nadir alone is not sufficient to separate Emax and EC50.
- Trep as written is a calendar time. Subtract the last-dose time to express elapsed time. Require recovery after depletion, or a patient never falling below the threshold can count as repopulated immediately. Recovery between visits is interval-censored; incomplete recovery is right-censored.
- If precursor compartments start at equilibrium and production never changes, they remain constant. Then ktr P3 = kprod throughout and the three transit states add no platelet dynamics. Use the simpler turnover model unless the model actually perturbs production.
- The precursor and production units in the table do not align with the circulating platelet concentration units. Specify consistent concentration/time units and the transit index range.
- Baseline platelets identify production divided by destruction, not destruction separately. Theta becomes identifiable only conditional on the assumed production rate and baseline equilibrium; that assumption is particularly questionable on background treatment.
- A reported time-to-response range is not a distribution for an effect-compartment rate. The onset also depends on severity, effect size, dosing, platelet turnover and the threshold. A six-week ke0 half-life is not a six-week time to response.
- Linear two-compartment PK may be a useful starting approximation, but identifiability cannot be declared from the intended sample size alone. Assess sampling, dose proportionality and late concentrations. For subcutaneous dosing, specify absorption and bioavailability; apparent parameters may be all that is identifiable. Ignoring time-dependent target effects can distort the very late exposure used to predict recovery.
- A logit-normal distribution can be bimodal on the original probability scale at sufficiently large variance. The claim that it cannot reproduce bimodality is mathematically incorrect, although it does not create exact point masses at zero and one.

As an illustrative check on the delay issue, take the model's equilibrium platelet ceiling to be 150, baseline 15, theta = 9 and eta = 1. At Z = 0.5 the equilibrium platelet count is only 27.3. Reaching 50 requires Z = 7/9, which takes about 91 days for an instantaneous sustained depletion input and a 42-day Z half-life, before allowing for platelet equilibration. These are illustrative model values, not estimates for ITP. They show why the prior needs predictive calibration.

**8. Trial design and causal attribution matter more than the current requirements table suggests — major.**

Fixed dose does not imply randomized dose. Explicitly randomize concurrent expansion arms, standardize background-treatment and rescue policies, and assess whether escalation cohorts are exchangeable with expansion cohorts. Chronological changes in eligibility, disease duration, prior therapy or clinical management can make pooling misleading. Expansion-dose selection is adaptive if it depends on escalation results; simulate that selection too.

Choosing dose as the final decision variable does not cure confounding in the fitted exposure–response relationship. A biased exposure coefficient remains biased when used in forward dose simulation. Baseline circulating B cells may not account for tissue burden, immune state or time-varying clearance. Anchor dose effects in randomized contrasts and evaluate sensitivity to PK–outcome associations within dose groups. Propagate uncertainty if fitting PK and response sequentially.

The “fatal” rules of three dose levels, fourfold or eightfold range and full repopulation follow-up are not universal. Two randomized doses can answer a comparison between those regimens. Additional levels become necessary for learning shape or extrapolating lower. Full recovery follow-up is crucial for assessing sustained benefit after reconstitution, but is not required for every earlier efficacy decision. More timepoints cannot replace missing clinically informative dose contrasts.

Distinguish the data needed for the immediate dose decision from the data needed to establish the reset hypothesis. If all patients remain depleted at the decision date, the correct conclusion may be that the mechanism of persistence is unresolved. Analyze disease phase, prior B-cell therapy, splenectomy and background treatment through prespecified parsimonious stratification or adjustment, rather than a large exploratory covariate search in 50–100 patients.

**9. Rescue, bleeding and longitudinal error require a real analysis policy — major.**

Model rescue according to its role in the estimand. If rescue constitutes endpoint failure, it is an observed component of the outcome, not merely censoring. If the objective is a hypothetical platelet trajectory without rescue, additional untestable assumptions are required. Simply excluding post-rescue counts is not an acceptable primary solution described as “accept the bias.”

A rescue model driven solely by current platelets may be inadequate when decisions also depend on bleeding, prior trends, background therapy and clinician practice. Record and simulate these processes at the level needed for the endpoint. TPO-RA tapering is especially important when its success is part of durable response.

Specify residual variation, within-patient temporal correlation, true biological fluctuations, missed visits, informative visits and dropout. Durable response depends on sequences of observations; a model that fits marginal means can still badly mispredict the durable endpoint. Use patient-level validation, not randomly withheld individual timepoints that let each patient's remaining trajectory leak into prediction.

The platelet-only probability is an upper bound on an otherwise identical endpoint with an added no-bleeding condition at the level of true event sets. A misspecified estimated response rate is not guaranteed to upper-bound actual clinical response. Recent trials also use different endpoints. Preserve the IWG discussion as historical context and implement the exact chosen protocol definition rather than applying every IWG clause to every contemporary trial.

**10. The literature argument should be narrowed and the external checks redesigned — major.**

The regulatory examples are useful feasibility warnings. They do not establish that continuous platelet modelling generally fails because destruction-blocking therapies act through a binary mechanism. They cover different targets, schedules, designs and intended uses. Absence from the searched literature is not evidence that no model exists; a model used to support or confirm a regimen can still be valuable.

The PMDA review directly supports the limited statement that the Phase 2 efgartigimod IgG–platelet model did not adequately explain interindividual platelet variation for the intended dose simulations, and that IgG reduction informed the subsequent regimen. It does not establish a universal sample-size or identifiability boundary. [PMDA review, Section 6.R.1](https://www.pmda.go.jp/files/000273743.pdf). Section 19 also overstates comparative sample sizes: the Phase 2 efgartigimod study enrolled 38 patients, below the proposed 50–100 total, while 305 is not ten times 50–100. [Primary Phase 2 report](https://pubmed.ncbi.nlm.nih.gov/31821591/); [sponsor trial description](https://www.sec.gov/Archives/edgar/data/1697862/000155837020003438/argx-20191231x20f.htm).

The FDA fostamatinib search extract corroborates failure of the attempted continuous models. The full FDA rilzabrutinib PDF was not retrievable in this review, so its detailed claims remain dependent on the existing reference notes. Separate confirmed primary-source observations from the specification's explanations for them.

VAYHIT2 reported 12-month freedom from treatment failure of 54% at 9 mg/kg and 51% at 3 mg/kg, with broad intervals, in a trial incorporating eltrombopag and tapering. That supports considering a small difference; it does not prove equivalence or locate a plateau below 3 mg/kg. Section 14's description of this comparison as ten points also contradicts the cited figures. [Cuker et al., primary trial report](https://pubmed.ncbi.nlm.nih.gov/41363800/).

Likewise, similar aggregate rituximab response rates across dose regimens do not establish equivalence without attention to populations, background therapy, endpoint and follow-up. Use these data to challenge ranges of plausible predictions after matching the design, not as a pass/fail requirement that every model predict a particular plateau. If the same data help choose priors or structures, they are not independent validation data. Cross-drug checks should concern plausibility, not dose translation for a generic compound.

**11. A fair model comparison and simulation programme — recommended replacement.**

Start with a hierarchy in which each added layer has to earn its complexity:

| Candidate | What it adds | Main question |
|---|---|---|
| Arm-level endpoint model | Regularized response estimates, protocol-defined rescue, baseline adjustment | What can the randomized comparison already support? |
| Simple dose-response model | Pooling across eligible cohorts with logistic, Emax or weakly constrained alternatives | How much comes from assuming a shape? |
| Dose–longitudinal platelet model | Onset, count variability, persistence and relapse | Do repeated platelets improve the decision? |
| PK–platelet model | Exposure and regimen dependence | Does PK help beyond assigned dose? |
| PK–B-cell–platelet model | Candidate depletion/recovery link | Do B cells improve prediction or just add assumptions? |
| Immune-marker extensions | Subsets, antibody assays, IgG where justified | Which measurements add enough value to justify collection? |

Fit simpler models to existing data if available; simulation and exploratory data review can proceed iteratively. There is no reason to prohibit all real-data fitting until a speculative mechanistic simulator passes.

For simulation, first define the complete data-generating and observation processes. Include at least: reset with early healthy repopulation; reversible suppression; mixed persistence and relapse; all tested doses on an efficacy plateau but differing immune burden; tissue efficacy poorly tracked by peripheral depletion; continuous response heterogeneity without a true two-class mixture; production effects and background-treatment tapering; nonlinearity or time dependence in PK; informative rescue and dropout; and nonexchangeable escalation cohorts. Evaluate a case with no worthwhile efficacy at any tested dose. Do not restrict misspecification to an added tissue lag, which the fitted effect compartment may already absorb.

Apply identical clinical decision rules to the candidates whenever possible. Compare using equal total patients and follow-up. Include a simple lowest-acceptable-dose rule; highest safe dose and maximized depletion duration are weak primary comparators for the user's question.

Report probability of selecting a regimen within the clinical tolerance, clinically important under-treatment, unnecessary exposure or immune burden, expected decision loss, interval coverage, calibration, frequency of inconclusive decisions, and fit failures. Do not silently discard nonconvergent fits. Report Monte Carlo uncertainty. Around a true success probability of 0.8, 2,000 simulated trials give a Monte Carlo standard error of about 0.009; choose precision deliberately and use an initial scenario subset for debugging.

An exact plateau bottom need not exist. Even when it does, missing it by one dose level may be clinically trivial or important depending on the curves. Decision loss is more transferable than exact-dose accuracy. A single summary figure is insufficient if it hides major harm under a subset of plausible mechanisms.

**12. Section-by-section disposition.**

| Section | Recommended action |
|---|---|
| Opening summary | Rewrite around durable control and immune recovery; remove promised sample savings and the assumption that duration is the unique dose signal. |
| 1. Objective | Define the decision and distinguish hypotheses from conclusions. Replace the assertion that classical PK–platelet modelling cannot help. |
| 2. Uncertainties | Put reset versus suppression, clinical utility, exchangeability and model incremental value first. Remove the numeric plasma-cell-floor inference. |
| 3. Endpoints | Retain the useful definitions; separate historical IWG criteria from the selected protocol. Calibrate delay priors predictively. |
| 4. Biomarkers | Retain the inventory; downgrade causal and identifiability claims and distinguish assays and measurement error. |
| 5. Drug catalogue | Move to a reference appendix and verify only claims that affect assumptions. Do not pool unlike mechanisms as interchangeable parameter sources. |
| 6. Four questions | Replace unconditional identifiability answers with data-dependent assessments; revise asymmetric error costs. |
| 7. Depletion depth | Change universal statements to observations about the studied range. Make duration one candidate predictor. |
| 8. Model | Add reset-capable alternatives, explicit dose dependence and complete observation processes; simplify inactive transit states. |
| 9. Data requirements | Replace universal fatal thresholds with decision-specific requirements. Prioritize randomization, treatment history and post-course follow-up. |
| 10. Identifiability | Add prior sensitivity, parameter recovery, posterior calibration, shrinkage and decision stability. EBE correlations and Fisher conditioning alone are insufficient. |
| 11. Confounding | Keep the concern; remove the claim that forward dose simulation resolves it. |
| 12. Fitting endpoint | Compare longitudinal and endpoint models; specify rescue, error correlation and dropout. Correct the logit-normal claim. |
| 13. Selection rule | Add minimum efficacy, immune burden, posterior-draw implementation and an inconclusive option. |
| 14. Sample size | Retain the verified illustrative calculations; remove unsupported conversion to PK–platelet sample savings. |
| 15. Simulation | Use competing mechanisms and fair baselines; score clinical loss, calibration and robustness. |
| 16. External checks | Replace required plateau predictions with uncertainty-aware, design-matched plausibility checks. |
| 17. Negative findings | Distinguish failure of the B-cell-mediated structure from failure of all platelet modelling. Prior dominance need not reduce a model to empirical rates. |
| 18. Milestones | Begin with estimand, empirical baselines and complete candidate structures. Use uncertainty distributions rather than reflexively fixing literature parameters. |
| 19. Literature explanation | Retain the regulatory evidence table after audit; replace universal mechanistic conclusions and erroneous sample-size comparisons. |
| 20. Intended use | Promise an evaluation of incremental decision value, including an inconclusive or negative finding, rather than a plateau discovery. |

Editorial cleanup should follow the substantive revision: the opening has a broken reset sentence; the count of verified sources changes across sections; Section 15 references reduced model “4.4”; fourfold and eightfold requirements conflict; n approximately 40 alternates with a 50–100-patient study; and several sections contradict one another about whether the plateau is identifiable. These are symptoms of an evolving argument rather than the main scientific problem.

**13. When the model would actually be worth building.**

| Situation | Assessment |
|---|---|
| Randomized doses or regimens span a meaningful change in onset, durability, rescue or treatment-free control | Strongest opportunity for a dose–platelet model; PK may add value for schedule changes. |
| Peripheral depletion is saturated but clinical response varies by randomized dose | Platelet modelling can remain useful; forcing mediation through blood B cells may be harmful. |
| Clinical benefit persists after recovery, with adequate follow-up and controlled background treatment | Strong opportunity to compare suppression and persistent-response models and shorten unnecessary treatment. |
| All studied doses have similar efficacy but different immune recovery | Valuable benefit–risk question, although efficacy alone may not establish how far below the lowest studied dose one can go. |
| Only within-arm exposure variation exists, all B cells are unquantifiable, follow-up is short, and rescue is poorly recorded | Low credibility for causal dose optimization, however good the fitted curves look. |
| A simple endpoint or dose-response model makes the same well-calibrated decision | The added mechanistic chain is not justified for this decision. |
| Predictions change substantially with reasonable priors or reset assumptions | Use the model to identify the next informative dose, regimen or follow-up period; do not treat its point recommendation as established. |

The proposed project is worth pursuing as a staged comparison of decision methods. The first investment should be in a precise clinical objective, credible simple baselines and competing persistence mechanisms. Proceed to a full PK–B-cell–platelet chain only if it improves those decisions robustly. The key human review questions are the acceptable loss of efficacy, the value placed on immune recovery, the evidence needed to call remission consistent with reset, and the feasible background-treatment and follow-up policies.
