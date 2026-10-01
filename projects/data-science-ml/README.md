# Data Science & Machine Learning projects

Prediction, clustering and fine-tuning, with baselines, held-out evaluation and uncertainty made explicit.

**5 projects** · Regression · Classification · Clustering · Fine-tuning

[All project categories](../README.md) · [My GitHub profile](https://github.com/abhijith-abhii)

**Start with [Retention Studio](https://github.com/abhijith-abhii/retention-studio)** — Prioritize reviewable churn retention work.

| Project | What it does | Open |
|---|---|---|
| **[PayLens](https://github.com/abhijith-abhii/paylens)** | Explore salary estimates and uncertainty | [Code and setup](https://github.com/abhijith-abhii/paylens#readme) |
| **[Retention Studio](https://github.com/abhijith-abhii/retention-studio)** | Prioritize reviewable churn retention work | [Code and setup](https://github.com/abhijith-abhii/retention-studio#readme) |
| **[CourtCraft](https://github.com/abhijith-abhii/courtcraft)** | Compare basketball performance fairly | [Code and setup](https://github.com/abhijith-abhii/courtcraft#readme) |
| **[Ticket Tuner](https://github.com/abhijith-abhii/ticket-tuner)** | Adapt a small model for support routing | [Code and setup](https://github.com/abhijith-abhii/ticket-tuner#readme) |
| **[SpendMap](https://github.com/abhijith-abhii/spendmap)** | Understand spending with editable categories | [Code and setup](https://github.com/abhijith-abhii/spendmap#readme) |

## PayLens

Explore salary estimates and uncertainty.

- Synthetic salary regression with a median baseline
- Separate training, calibration and test splits
- Prediction intervals and held-out evaluation

**Stack:** scikit-learn · Flask

**Data:** Transparent synthetic compensation sample

**Recorded checks:** 10 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** These results describe authored synthetic data. They are not reliable market salary estimates or a guarantee about any individual’s compensation.

[Code and startup instructions](https://github.com/abhijith-abhii/paylens#readme) · [Demonstration guide](https://github.com/abhijith-abhii/paylens/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/paylens/blob/main/VERIFICATION.md)

## Retention Studio

Prioritize reviewable churn retention work.

- Calibrated churn scores and eligibility rules
- Capacity-limited review queue with cooldowns
- Stored decisions and audit history

**Stack:** pandas · scikit-learn · Flask

**Data:** IBM fictional telecom sample

**Recorded checks:** 27 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** The data is fictional and the labels are historical. A high churn score does not prove that outreach will prevent churn. Numerical runtime warnings occurred in the recorded macOS test environment.

[Code and startup instructions](https://github.com/abhijith-abhii/retention-studio#readme) · [Demonstration guide](https://github.com/abhijith-abhii/retention-studio/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/retention-studio/blob/main/VERIFICATION.md)

## CourtCraft

Compare basketball performance fairly.

- Per-36-minute rates and scoring efficiency
- Gamma-Poisson shrinkage and uncertainty intervals
- Minimum-minutes filter and comparisons

**Stack:** pandas · scipy · Flask

**Data:** Authored synthetic box scores

**Recorded checks:** 8 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** The dataset does not describe a real league. Rates and model intervals do not account for every factor, such as opponent strength, pace or team role.

[Code and startup instructions](https://github.com/abhijith-abhii/courtcraft#readme) · [Demonstration guide](https://github.com/abhijith-abhii/courtcraft/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/courtcraft/blob/main/VERIFICATION.md)

## Ticket Tuner

Adapt a small model for support routing.

- Actual FLAN-T5-small support-ticket fine-tuning
- Template-family splits and checkpoint selection
- TF-IDF baseline and local inference

**Stack:** PyTorch · Transformers

**Data:** Authored synthetic support corpus

**Recorded checks:** 7 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** Large trained weights are excluded from Git. A fresh clone needs the pinned base-model download and training. A perfect score on limited synthetic examples does not establish real-world support accuracy.

[Code and startup instructions](https://github.com/abhijith-abhii/ticket-tuner#readme) · [Demonstration guide](https://github.com/abhijith-abhii/ticket-tuner/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/ticket-tuner/blob/main/VERIFICATION.md)

## SpendMap

Understand spending with editable categories.

- Editable merchant rules and exact spending totals
- Monthly summaries and normalized customer features
- KMeans clustering with silhouette diagnostics

**Stack:** pandas · scikit-learn · Flask

**Data:** Synthetic transactions

**Recorded checks:** 10 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** The transactions are synthetic. Clusters are descriptive and depend on the rules and selected features; they are not financial advice.

[Code and startup instructions](https://github.com/abhijith-abhii/spendmap#readme) · [Demonstration guide](https://github.com/abhijith-abhii/spendmap/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/spendmap/blob/main/VERIFICATION.md)

## How to explore

Open a project's README, follow its startup instructions and demonstration, then review its design decisions and evidence. Datasets, dependencies and execution limits are explained in the linked repository. These are AI-assisted personal projects; code and tests are evidence of implementation, not employment deliverables or production adoption.
