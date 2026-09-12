# Portfolio guide

For backend roles, start with Durable Queue or Contract Pipeline to inspect a focused implementation, then explore the larger Health Passport workflow. For full-stack roles, start with Health Passport's screenshots, shared API and web/mobile architecture.

All four repositories contain AI-assisted personal work. The three smaller projects were created in September 2026; they are new learning projects, not historical employment deliverables. Tests demonstrate behavior of the code, not the owner's independent proficiency.

## Global Health Passport

[Repository](https://github.com/abhijithviswanathan/global-health-passport) · [Review and contribution](https://github.com/abhijithviswanathan/global-health-passport/blob/main/docs/PORTFOLIO_REVIEW.md)

The flagship connects patient consent and records to care-team tasks, clinical execution and hospital operations across a shared Java API and React/Expo clients. Review server-enforced authorization, relational migrations, provenance and workflow state before the UI details. The README includes synthetic screenshots and local setup.

Current portfolio checks: 63 local backend tests passed, with 31 PostgreSQL cases skipped locally. The [hosted verification](https://github.com/abhijithviswanathan/global-health-passport/actions/runs/34668275365) then passed the backend with real PostgreSQL, web types/lint/build and mobile types/tests on fresh runners. Mobile has 18 behavior tests. Historical browser reports are explicitly distinguished from this review. No real patient deployment or native-device verification is claimed.

## Durable Queue

[Repository](https://github.com/abhijithviswanathan/durable-queue) · [Engineering notes](https://github.com/abhijithviswanathan/durable-queue/blob/main/ENGINEERING.md)

Python and SQLite job processing with transactional claims, expiring leases, fenced completion, backoff, dead letters and idempotent enqueue. It demonstrates recovery and concurrency boundaries. Delivery is at least once; external side effects still require idempotency. It is a single-host queue, not a distributed broker.

After cloning: `python3 demo.py`, then `python3 -m unittest discover -s tests -v`. Eight tests passed locally; GitHub CI passed on Python 3.11, 3.12 and 3.13.

## Contract Pipeline

[Repository](https://github.com/abhijithviswanathan/contract-pipeline) · [Engineering notes](https://github.com/abhijithviswanathan/contract-pipeline/blob/main/ENGINEERING.md)

Contract-driven CSV ingestion separates valid records from quarantine, commits batches atomically, rejects incompatible contract changes and prevents repeated input from duplicating work. Exact decimal values remain strings. It demonstrates deterministic validation and failure recovery without a cloud data platform.

After cloning: `python3 demo.py`, then `python3 -m unittest discover -s tests -v`. Ten tests passed locally; GitHub CI passed on Python 3.11, 3.12 and 3.13. The demo accepts three rows, rejects three and safely replays the input.

## DocSearch

[Repository](https://github.com/abhijithviswanathan/docsearch) · [Engineering notes](https://github.com/abhijithviswanathan/docsearch/blob/main/ENGINEERING.md)

Local Markdown search uses SQLite's built-in FTS5/BM25 ranking, incremental content hashes, heading-based chunks and source line references. It excludes symlinks and selected hidden/vendor paths, and can export escaped offline HTML. It is lexical search; it does not generate answers or implement a new ranking algorithm.

After cloning: `python3 demo.py`, then `python3 -m unittest discover -s tests -v`. Nine tests passed locally; GitHub CI passed on Python 3.11, 3.12 and 3.13. Open `var/demo.html` to inspect ranked passages.

## Portfolio maintenance

Feature projects here after their examples, checks and documentation are ready. Keep dates and contribution statements accurate. Add screenshots only when they illustrate the project, and exclude credentials, private data and local runtime files before publishing.
