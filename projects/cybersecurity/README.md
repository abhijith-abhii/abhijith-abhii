# Cybersecurity & Secure Systems projects

A focused view of security controls in existing projects: SQL access restrictions, container hardening and private network design.

**3 security-related projects** · Access restrictions · Container hardening · Network isolation

[All project categories](../README.md) · [My GitHub profile](https://github.com/abhijith-abhii)

> These three projects are also listed under AI & ML Engineering or Cloud & DevOps. This section highlights their implemented security controls; it does not count them as additional projects or claim a standalone penetration-testing portfolio.

**Start with [QueryGuard](https://github.com/abhijith-abhii/queryguard)** — Ask bounded sales questions safely.

| Project | What it does | Open |
|---|---|---|
| **[QueryGuard](https://github.com/abhijith-abhii/queryguard)** | Ask bounded sales questions safely | [Code and setup](https://github.com/abhijith-abhii/queryguard#readme) |
| **[Shipyard](https://github.com/abhijith-abhii/shipyard)** | Ship a health-checked service through CI | [Code and setup](https://github.com/abhijith-abhii/shipyard#readme) |
| **[Network Foundry](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab)** | Reproduce a segmented AWS network safely | [Code and setup](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab#readme) |

## QueryGuard

Ask bounded sales questions safely.

**Database access restrictions.** Parameterized SQL, a read-only connection, a SQLite authorizer and query budgets. The recorded browser demonstration rejected a DROP TABLE request.

Primary area: **AI / ML Engineering**.

**Recorded checks:** 15 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** This is a bounded rules-based interface over synthetic data. It does not use a language model to generate arbitrary SQL.

[Code and startup instructions](https://github.com/abhijith-abhii/queryguard#readme) · [Demonstration guide](https://github.com/abhijith-abhii/queryguard/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/queryguard/blob/main/VERIFICATION.md)

## Shipyard

Ship a health-checked service through CI.

**Container hardening.** Non-root container execution and a read-only filesystem. The recorded CI run checked runtime identity and endpoints.

Primary area: **Cloud / DevOps**.

**Recorded checks:** 9 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** Actual temporary CI container verified; no continuously hosted public service or production rollout. The deployment target is a temporary CI container or local Compose service. Continuous public hosting, registry delivery and zero-downtime production rollout are outside this scope.

[Code and startup instructions](https://github.com/abhijith-abhii/shipyard#readme) · [Demonstration guide](https://github.com/abhijith-abhii/shipyard/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/shipyard/blob/main/VERIFICATION.md)

## Network Foundry

Reproduce a segmented AWS network safely.

**Private network design.** Terraform network segmentation, security-group rules, management endpoints and logs. Verification covers configuration, Python diagnostics and mock tests; no AWS resources were deployed.

Primary area: **Cloud / DevOps**.

**Recorded checks:** 16 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** No AWS resources deployed; only configuration, Python and mock-provider checks executed. No AWS resources were deployed. These checks cannot prove live packet delivery or account-specific IAM behavior. Terraform apply would require a separate cost and account review.

[Code and startup instructions](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab#readme) · [Demonstration guide](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab/blob/main/VERIFICATION.md)

## How to explore

Open a project's README, follow its startup instructions and demonstration, then review its design decisions and evidence. Datasets, dependencies and execution limits are explained in the linked repository. These are AI-assisted personal projects; code and tests are evidence of implementation, not employment deliverables or production adoption.
