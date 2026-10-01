# Cloud & DevOps projects

Container delivery, infrastructure configuration, cost analysis, recovery and measured Kubernetes autoscaling.

**5 projects** · Docker · Terraform · CI · Kubernetes · Reliability

[All project categories](../README.md) · [My GitHub profile](https://github.com/abhijith-abhii)

**Start with [Shipyard](https://github.com/abhijith-abhii/shipyard)** — Ship a health-checked service through CI.

| Project | What it does | Open |
|---|---|---|
| **[Shipyard](https://github.com/abhijith-abhii/shipyard)** | Ship a health-checked service through CI | [Code and setup](https://github.com/abhijith-abhii/shipyard#readme) |
| **[Network Foundry](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab)** | Reproduce a segmented AWS network safely | [Code and setup](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab#readme) |
| **[CostCompass](https://github.com/abhijith-abhii/costcompass)** | Explain AWS cost drivers and review opportunities | [Code and setup](https://github.com/abhijith-abhii/costcompass#readme) |
| **[Failover Forge](https://github.com/abhijith-abhii/failover-forge)** | Measure local recovery under service failure | [Code and setup](https://github.com/abhijith-abhii/failover-forge#readme) |
| **[Scale Lab](https://github.com/abhijith-abhii/scale-lab)** | Understand autoscaling under measured load | [Code and setup](https://github.com/abhijith-abhii/scale-lab#readme) |

## Shipyard

Ship a health-checked service through CI.

- Container build and delivery through GitHub Actions
- Non-root runtime and read-only filesystem
- Health and functional smoke checks

**Stack:** Docker · GitHub Actions · Flask

**Data:** Local service; temporary CI containers

**Recorded checks:** 9 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** Actual temporary CI container verified; no continuously hosted public service or production rollout. The deployment target is a temporary CI container or local Compose service. Continuous public hosting, registry delivery and zero-downtime production rollout are outside this scope.

[Code and startup instructions](https://github.com/abhijith-abhii/shipyard#readme) · [Demonstration guide](https://github.com/abhijith-abhii/shipyard/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/shipyard/blob/main/VERIFICATION.md)

## Network Foundry

Reproduce a segmented AWS network safely.

- Terraform private network and endpoint configuration
- Fault scenarios and Python diagnostics
- Credential-free validation and mock-provider tests

**Stack:** Terraform · Python

**Data:** AWS configuration; no paid apply

**Recorded checks:** 16 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** No AWS resources deployed; only configuration, Python and mock-provider checks executed. No AWS resources were deployed. These checks cannot prove live packet delivery or account-specific IAM behavior. Terraform apply would require a separate cost and account review.

[Code and startup instructions](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab#readme) · [Demonstration guide](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/aws-network-infrastructure-troubleshooting-lab/blob/main/VERIFICATION.md)

## CostCompass

Explain AWS cost drivers and review opportunities.

- Synthetic AWS-style billing reconciliation
- Service/tag summaries and anomaly flags
- Hypothetical compute-savings scenarios

**Stack:** pandas · Flask

**Data:** Synthetic AWS billing rows

**Recorded checks:** 8 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** No real AWS account is connected. The data is synthetic and the app makes no infrastructure changes or automatic spending decisions.

[Code and startup instructions](https://github.com/abhijith-abhii/costcompass#readme) · [Demonstration guide](https://github.com/abhijith-abhii/costcompass/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/costcompass/blob/main/VERIFICATION.md)

## Failover Forge

Measure local recovery under service failure.

- Two real local HTTP service processes
- Primary failure, client fallback and restart
- Measured recovery sequence and process cleanup

**Stack:** Python · HTTP subprocesses

**Data:** Local synthetic service traffic

**Recorded checks:** 5 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** This is a same-host, stateless process experiment. It is not a multi-region system, load balancer or data-replication test; no recovery-point objective was measured.

[Code and startup instructions](https://github.com/abhijith-abhii/failover-forge#readme) · [Demonstration guide](https://github.com/abhijith-abhii/failover-forge/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/failover-forge/blob/main/VERIFICATION.md)

## Scale Lab

Understand autoscaling under measured load.

- Replica calculator and containerized worker
- Kubernetes probes, resource requests and HPA
- Real disposable kind-cluster load experiment

**Stack:** Kubernetes · kind · Python

**Data:** Ephemeral local/CI cluster

**Recorded checks:** 12 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** Actual kind cluster scaled from two to six available replicas; multi-node production operation and scale-down benchmarks are outside scope. The calculator simplifies controller behavior. The real test uses a disposable single-node cluster; scale-down timing, node autoscaling and production capacity were not benchmarked.

[Code and startup instructions](https://github.com/abhijith-abhii/scale-lab#readme) · [Demonstration guide](https://github.com/abhijith-abhii/scale-lab/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/scale-lab/blob/main/VERIFICATION.md)

## How to explore

Open a project's README, follow its startup instructions and demonstration, then review its design decisions and evidence. Datasets, dependencies and execution limits are explained in the linked repository. These are AI-assisted personal projects; code and tests are evidence of implementation, not employment deliverables or production adoption.
