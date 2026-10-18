# Portfolio guide

[Live portfolio](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/) · [Resume PDF](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/assets/Abhijith-Viswanathan-Resume.pdf) · [Complete project directory](projects/)

Updated October 18, 2026. The resume selects five projects for entry-level software, backend and full-stack roles. Start with Health Passport for the broader workflow, NoteMesh for collaboration and concurrency, DocSearch Atlas for retrieval, RescueRoute for constrained route optimization, or PropertyPulse for indexed database search. Shipyard remains documented as an additional delivery lab.

These are my personal projects, covering full-stack applications, search, cloud systems and optimization. Development notes document AI-assisted tooling; recorded checks and benchmarks describe reproducible local behavior. The October 18 update adds reproducible synthetic local benchmarks. NoteMesh, DocSearch and Shipyard tests were rerun; Health Passport's application-suite totals remain historical evidence.

## Global Health Passport

[Repository and setup](https://github.com/abhijith-abhii/global-health-passport) · [Contribution and review](https://github.com/abhijith-abhii/global-health-passport/blob/main/docs/PORTFOLIO_REVIEW.md) · [Case study](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/projects/health-passport/)

Java, Spring Boot, React, TypeScript and PostgreSQL support a shared web/mobile API for consent-controlled records, care-team tasks and organization-scoped workflows. The synthetic prototype includes record provenance, encrypted document handling and Flyway migrations.

Recorded verification passed 94 backend and 18 mobile tests plus web build checks. Review the repository for exact scope and environment. No live patient deployment, compliance certification or native-device validation is claimed.

## RescueRoute

[Repository and setup](https://github.com/abhijith-abhii/rescue-route) · [Case study](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/projects/rescue-route/) · [Benchmark evidence](https://github.com/abhijith-abhii/rescue-route/blob/main/benchmarks/README.md)

My personal project for community food-delivery planning. Capacity, unloading windows and depot-return constraints are checked during route optimization. A visual dashboard compares plans; SQLite persists idempotent requests. 36 tests passed. Across 20 synthetic delivery days, modelled distance fell 18.71% with the same 480 deliveries. A separate eight-stop experiment reduced median runtime 99.69% versus exhaustive search, matching the optimum on all ten fixtures; no general optimality guarantee is claimed.

## PropertyPulse

[Repository and setup](https://github.com/abhijith-abhii/propertypulse-api) · [Case study](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/projects/propertypulse-api/) · [Benchmark evidence](https://github.com/abhijith-abhii/propertypulse-api/blob/main/benchmarks/README.md)

My rental-search API project with city/bedroom/budget filters, cursor pagination and version-checked updates. 23 tests passed. A composite partial index reduced median database search time 97.37% over 100,000 synthetic listings. The separate HTTP comparison did not improve; the claim is limited to the measured database operation.

## NoteMesh

[Repository and setup](https://github.com/abhijith-abhii/notemesh) · [Case study](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/projects/notemesh/) · [Recorded CI](https://github.com/abhijith-abhii/notemesh/actions/runs/36416543900)

Flask, SQLite and Server-Sent Events synchronize saved note revisions across browsers. Transactional revision checks reject stale edits and preserve the user's draft; revision history and Markdown export make changes inspectable. This uses whole-note optimistic concurrency, not character-level collaborative merging.

The September 28 verification records 13 passing checks and a two-browser sync/conflict-and-recovery demonstration.

## DocSearch Atlas

[Repository and setup](https://github.com/abhijith-abhii/docsearch) · [Case study](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/projects/docsearch/) · [Recorded CI](https://github.com/abhijith-abhii/docsearch/actions/runs/36417056669)

Python, Flask and SQLite FTS5 provide incremental runbook indexing, ranked passages and source-linked extractive answers. Optional local FLAN-T5-small generation is a separate answer mode, with explicit no-evidence handling. Current functionality extends the earlier search-only version.

The September 28 verification records 19 passing checks. Synthetic local examples do not establish answer quality on an organization's real documents.

## Shipyard

[Repository and setup](https://github.com/abhijith-abhii/shipyard) · [Case study](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/projects/shipyard/) · [Recorded CI](https://github.com/abhijith-abhii/shipyard/actions/runs/36416088236)

Docker and GitHub Actions package a Flask service using a non-root user. Tests precede the build, and a temporary CI container verifies readiness and a known response digest. The project documents read-only runtime constraints and rollback steps.

The September 28 verification records nine passing checks and temporary container execution. This is a delivery lab, with no production deployment claim.

## More backend work

- [Durable Queue](https://github.com/abhijith-abhii/durable-queue): SQLite jobs, transactional claims, expiring leases, fenced completion, retry and idempotent enqueue. Single-host and at-least-once delivery.
- [Contract Pipeline](https://github.com/abhijith-abhii/contract-pipeline): contract-driven CSV validation, quarantine, atomic batches and safe replay.

The [complete project directory](projects/) groups the wider collection by software, data, AI/ML, cloud and security topics, with repository-specific evidence and limitations.

## Portfolio maintenance

Feature work after its examples, documentation and appropriate checks are ready. Keep contribution statements, README setup steps, configuration examples and screenshots current. Exclude credentials, private data and local runtime files. Update the resume and live portfolio links when a featured project changes materially.

## Measured local performance — October 18, 2026

These are laboratory workloads, not production user counts. Each HTTP run used 8 clients and 2,400 measured requests; source revisions and full reproduction steps are linked below.

| Project | Measured result | Evidence |
|---|---|---|
| notemesh | 22.276 ms p95; 1,060.34 requests/s median across 3 rounds | [Workload and results](https://github.com/abhijith-abhii/notemesh/blob/main/benchmarks/README.md) |
| docsearch | 42.940 ms p95; 496.75 requests/s median across 3 rounds; unchanged indexing used 94.76% less time than full rebuilding on 1,000 synthetic documents | [Workload and results](https://github.com/abhijith-abhii/docsearch/blob/main/benchmarks/README.md) |
| shipyard | 9.924 ms p95; 1,160.77 requests/s median across 3 rounds | [Workload and results](https://github.com/abhijith-abhii/shipyard/blob/main/benchmarks/README.md) |
| health-passport | 3.295 ms p95; 4,863.43 requests/s median across 3 rounds | [Workload and results](https://github.com/abhijith-abhii/global-health-passport/blob/main/benchmarks/README.md) |
