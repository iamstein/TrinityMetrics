# Enabling AI-Assisted Pharmacometric Workflows Using Synthetic Data

**Authors:** Andrew Stein

## Objectives

To describe a practical workflow enabling AI-assisted, agentic coding for pharmacometric analyses when clinical datasets cannot leave secure environments.

## Methods

We defined a structure-preserving synthetic data workflow that separates dataset structure from sensitive patient-level values. Synthetic datasets were designed to retain analysis-relevant characteristics such as covariate distributions, dosing records, and observation schedules without containing real patient data. These datasets were then used in pilot pharmacometric workflows to develop, test, and refine analysis code and AI-assisted pipelines in unrestricted local or cloud environments. Final model fitting, validation, and decision-relevant interpretation were reserved for secure systems containing the real data.

## Results

This workflow enabled substantial parts of analysis development to occur outside restricted environments while preserving confidentiality requirements. Synthetic datasets were sufficient to support code development for data ingestion, exploratory analysis, NLME model specification, and Shiny-based trial simulation workflows in unrestricted environments. Code and workflow logic developed with synthetic data could then be transferred into secure systems for execution, validation, and interpretation on real clinical data. This established a practical separation between AI-assisted development and regulated use of sensitive datasets.

## Conclusions

Structure-preserving synthetic data offers a practical route for introducing AI-assisted pharmacometric workflows under clinical data access constraints. The approach enables development outside restricted environments while preserving secure execution, validation, and scientific accountability on real data.

**Keywords:** pharmacometrics, synthetic data, AI workflows
