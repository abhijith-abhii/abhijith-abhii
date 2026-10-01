# AI & ML Engineering projects

Document retrieval, constrained workflows, model evaluation and multimodal search with inspectable results.

**5 projects** · Retrieval · Local models · Evaluation · Guardrails

[All project categories](../README.md) · [My GitHub profile](https://github.com/abhijith-abhii)

**Start with [DocSearch Atlas](https://github.com/abhijith-abhii/docsearch)** — Answer engineering runbook questions with evidence.

| Project | What it does | Open |
|---|---|---|
| **[DocSearch Atlas](https://github.com/abhijith-abhii/docsearch)** | Answer engineering runbook questions with evidence | [Code and setup](https://github.com/abhijith-abhii/docsearch#readme) |
| **[QueryGuard](https://github.com/abhijith-abhii/queryguard)** | Ask bounded sales questions safely | [Code and setup](https://github.com/abhijith-abhii/queryguard#readme) |
| **[Release Pilot](https://github.com/abhijith-abhii/release-pilot)** | Assemble a release review from local changes | [Code and setup](https://github.com/abhijith-abhii/release-pilot#readme) |
| **[EvalBench](https://github.com/abhijith-abhii/evalbench)** | Compare model answers using repeatable evidence | [Code and setup](https://github.com/abhijith-abhii/evalbench#readme) |
| **[ShelfMatch](https://github.com/abhijith-abhii/shelfmatch)** | Find material swatches using text and image features | [Code and setup](https://github.com/abhijith-abhii/shelfmatch#readme) |

## DocSearch Atlas

Answer engineering runbook questions with evidence.

- Incremental SQLite FTS5 runbook retrieval
- Source-linked extractive answers
- Optional local FLAN inference and no-evidence responses

**Stack:** SQLite FTS5 · Flask

**Data:** Authored runbooks; existing DocSearch code

**Recorded checks:** 19 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** Retrieval is lexical, so paraphrases without shared words may be missed. Generated answers can be wrong even when citations are displayed.

[Code and startup instructions](https://github.com/abhijith-abhii/docsearch#readme) · [Demonstration guide](https://github.com/abhijith-abhii/docsearch/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/docsearch/blob/main/VERIFICATION.md)

## QueryGuard

Ask bounded sales questions safely.

- Five supported sales-question intents
- Parameterized SQL with read-only access
- SQLite authorizer and query budgets

**Stack:** SQLite · Flask

**Data:** Synthetic sales database

**Recorded checks:** 15 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** This is a bounded rules-based interface over synthetic data. It does not use a language model to generate arbitrary SQL.

[Code and startup instructions](https://github.com/abhijith-abhii/queryguard#readme) · [Demonstration guide](https://github.com/abhijith-abhii/queryguard/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/queryguard/blob/main/VERIFICATION.md)

## Release Pilot

Assemble a release review from local changes.

- Allowlisted local inspection and test workflow
- Passing-test gate, content cache and audit records
- Optional local-model summaries with guarded fallback

**Stack:** Python · Flask

**Data:** Local sample release workspace

**Recorded checks:** 10 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** The tool cannot send, tag, push or deploy a release. The summary guard is conservative but does not guarantee semantic truth; the result is for human review.

[Code and startup instructions](https://github.com/abhijith-abhii/release-pilot#readme) · [Demonstration guide](https://github.com/abhijith-abhii/release-pilot/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/release-pilot/blob/main/VERIFICATION.md)

## EvalBench

Compare model answers using repeatable evidence.

- Actual direct and context-assisted FLAN runs
- Exact-match and token-overlap scoring
- Paired bootstrap intervals and case-by-case inspection

**Stack:** Python · Flask

**Data:** Authored QA cases; explicit recorded responses

**Recorded checks:** 7 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** The small authored set cannot establish general superiority. Token overlap measures agreement with reference text, not guaranteed factual correctness.

[Code and startup instructions](https://github.com/abhijith-abhii/evalbench#readme) · [Demonstration guide](https://github.com/abhijith-abhii/evalbench/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/evalbench/blob/main/VERIFICATION.md)

## ShelfMatch

Find material swatches using text and image features.

- Sixteen original material swatches
- Text similarity and color/texture image features
- Adjustable modality weights and ranked gallery

**Stack:** Pillow · scikit-learn · Flask

**Data:** Authored product cards and images

**Recorded checks:** 12 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** This is an interpretable feature baseline, not a pretrained vision-language model. Images are procedural swatches; queries use catalog references rather than arbitrary uploads.

[Code and startup instructions](https://github.com/abhijith-abhii/shelfmatch#readme) · [Demonstration guide](https://github.com/abhijith-abhii/shelfmatch/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/shelfmatch/blob/main/VERIFICATION.md)

## How to explore

Open a project's README, follow its startup instructions and demonstration, then review its design decisions and evidence. Datasets, dependencies and execution limits are explained in the linked repository. These are AI-assisted personal projects; code and tests are evidence of implementation, not employment deliverables or production adoption.
