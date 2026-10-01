# Portfolio guide

[Live portfolio](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/) · [Resume PDF](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/assets/Abhijith-Viswanathan-Resume.pdf) · [LinkedIn](https://www.linkedin.com/in/abhijith-viswanathan-0a7216436/) · [Complete project directory](projects/)

Updated October 1, 2026. The resume selects four projects for entry-level software, backend and full-stack roles. Start with Health Passport for the broader workflow, NoteMesh for collaboration and concurrency, DocSearch Atlas for retrieval, or Shipyard for container delivery.

These are AI-assisted personal projects. I directed Health Passport's development and am strengthening my ability to trace, explain and extend the implementations myself. Recorded checks demonstrate code behavior; they do not establish independent proficiency or production adoption. Test results below are historical repository evidence, not new runs performed for this resume update.

## Global Health Passport

[Repository and setup](https://github.com/abhijith-abhii/global-health-passport) · [Contribution and review](https://github.com/abhijith-abhii/global-health-passport/blob/main/docs/PORTFOLIO_REVIEW.md) · [Case study](https://abhijith-viswanathan-portfolio.abhijithabhi3331.chatgpt.site/projects/health-passport/)

Java, Spring Boot, React, TypeScript and PostgreSQL support a shared web/mobile API for consent-controlled records, care-team tasks and organization-scoped workflows. The synthetic prototype includes record provenance, encrypted document handling and Flyway migrations.

Recorded verification passed 94 backend and 18 mobile tests plus web build checks. Review the repository for exact scope and environment. No live patient deployment, compliance certification or native-device validation is claimed.

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
