# Data Analytics projects

SQL, business dashboards, marketing attribution and experiments that turn data into explained decisions.

**5 projects** · SQL · Dashboards · A/B testing · Public-data research

[All project categories](../README.md) · [My GitHub profile](https://github.com/abhijith-abhii)

**Start with [Retail Control Tower](https://github.com/abhijith-abhii/retail-supply-chain-control-tower)** — Explore retail revenue, profit and delivery performance.

| Project | What it does | Open |
|---|---|---|
| **[Margin Ledger](https://github.com/abhijith-abhii/margin-ledger)** | Find product and return patterns with SQL | [Code and setup](https://github.com/abhijith-abhii/margin-ledger#readme) |
| **[JourneyMark](https://github.com/abhijith-abhii/journeymark)** | Compare marketing attribution assumptions | [Code and setup](https://github.com/abhijith-abhii/journeymark#readme) |
| **[Retail Control Tower](https://github.com/abhijith-abhii/retail-supply-chain-control-tower)** | Explore retail revenue, profit and delivery performance | [Code and setup](https://github.com/abhijith-abhii/retail-supply-chain-control-tower#readme) |
| **[Experiment Lens](https://github.com/abhijith-abhii/experiment-lens)** | Audit and interpret an A/B experiment | [Code and setup](https://github.com/abhijith-abhii/experiment-lens#readme) |
| **[Energy Brief](https://github.com/abhijith-abhii/energy-brief)** | Research electricity generation trends reproducibly | [Code and setup](https://github.com/abhijith-abhii/energy-brief#readme) |

## Margin Ledger

Find product and return patterns with SQL.

- Eight SQL reports at order-line grain
- Return reversals and exact money calculations
- Consistent totals and a business-results report

**Stack:** SQLite · Python · Flask

**Data:** Synthetic retail orders

**Recorded checks:** 8 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** The business data is synthetic. Shipping, tax and processing fees are excluded. Descriptive patterns do not establish why real customers behave a certain way.

[Code and startup instructions](https://github.com/abhijith-abhii/margin-ledger#readme) · [Demonstration guide](https://github.com/abhijith-abhii/margin-ledger/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/margin-ledger/blob/main/VERIFICATION.md)

## JourneyMark

Compare marketing attribution assumptions.

- First-touch, last-touch, linear and time-decay models
- Lookback windows and repeated-conversion boundaries
- Unattributed credit and conservation checks

**Stack:** pandas · Flask

**Data:** Synthetic touchpoint journeys

**Recorded checks:** 10 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** Attribution describes a chosen credit rule. It does not prove a channel caused a purchase or measure incremental advertising return.

[Code and startup instructions](https://github.com/abhijith-abhii/journeymark#readme) · [Demonstration guide](https://github.com/abhijith-abhii/journeymark/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/journeymark/blob/main/VERIFICATION.md)

## Retail Control Tower

Explore retail revenue, profit and delivery performance.

- Interactive revenue, profit and delivery dashboard
- Market, segment and month filters
- Distinct-order delivery metrics and safe-field selection

**Stack:** Python · SQLite · browser

**Data:** Existing synthetic fixture; provenance preserved

**Recorded checks:** 8 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** The finished scope is the synthetic-data browser dashboard. The preserved optional forecasting pipeline, native Power BI work and real-source Kaggle analysis were not revalidated as completed deliverables.

[Code and startup instructions](https://github.com/abhijith-abhii/retail-supply-chain-control-tower#readme) · [Demonstration guide](https://github.com/abhijith-abhii/retail-supply-chain-control-tower/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/retail-supply-chain-control-tower/blob/main/VERIFICATION.md)

## Experiment Lens

Audit and interpret an A/B experiment.

- Unique-user validation and sample-ratio checks
- Conversion intervals, lift and significance testing
- Separate sample-size planning calculation

**Stack:** scipy · Flask

**Data:** Seeded randomized synthetic experiment

**Recorded checks:** 9 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** This is a fixed-horizon normal-approximation analysis. Sparse outcomes, repeated peeking, multiple comparisons and causal validity beyond the experiment design need additional work.

[Code and startup instructions](https://github.com/abhijith-abhii/experiment-lens#readme) · [Demonstration guide](https://github.com/abhijith-abhii/experiment-lens/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/experiment-lens/blob/main/VERIFICATION.md)

## Energy Brief

Research electricity generation trends reproducibly.

- Pinned public OWID electricity dataset
- Country/year comparisons with missing-value handling
- Source checksums and a reproducible research report

**Stack:** Python · pandas · Flask

**Data:** Our World in Data energy data / cited upstream

**Recorded checks:** 10 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** The six countries are an illustrative selection. These historical comparisons do not isolate policy effects or provide forecasts.

[Code and startup instructions](https://github.com/abhijith-abhii/energy-brief#readme) · [Demonstration guide](https://github.com/abhijith-abhii/energy-brief/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/energy-brief/blob/main/VERIFICATION.md)

## How to explore

Open a project's README, follow its startup instructions and demonstration, then review its design decisions and evidence. Datasets, dependencies and execution limits are explained in the linked repository. These are AI-assisted personal projects; code and tests are evidence of implementation, not employment deliverables or production adoption.
