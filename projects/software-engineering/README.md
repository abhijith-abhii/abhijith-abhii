# Software Engineering projects

Useful applications and developer tools, from shared notes and browser extensions to an open-source regression patch.

**7 projects** · APIs · SQLite · Collaboration · Browser extensions

[All project categories](../README.md) · [My GitHub profile](https://github.com/abhijith-abhii)

**Start with [LinkScope](https://github.com/abhijith-abhii/linkscope)** — URL shortener with campaign analytics.

| Project | What it does | Open |
|---|---|---|
| **[LinkScope](https://github.com/abhijith-abhii/linkscope)** | URL shortener with campaign analytics | [Code and setup](https://github.com/abhijith-abhii/linkscope#readme) |
| **[NoteMesh](https://github.com/abhijith-abhii/notemesh)** | Shared meeting notes without lost edits | [Code and setup](https://github.com/abhijith-abhii/notemesh#readme) |
| **[Repo Radar](https://github.com/abhijith-abhii/repo-radar)** | Understand public repository activity | [Code and setup](https://github.com/abhijith-abhii/repo-radar#readme) |
| **[TabHarbor](https://github.com/abhijith-abhii/tabharbor)** | Organize crowded browser sessions | [Code and setup](https://github.com/abhijith-abhii/tabharbor#readme) |
| **[Upstream Lab](https://github.com/abhijith-abhii/upstream-lab)** | Reproduce and improve an open-source behavior | [Code and setup](https://github.com/abhijith-abhii/upstream-lab#readme) |
| **[Global Health Passport](https://github.com/abhijith-abhii/global-health-passport)** | Synthetic health workflows across Java, React and Expo | [Code and setup](https://github.com/abhijith-abhii/global-health-passport#readme) |
| **[Durable Queue](https://github.com/abhijith-abhii/durable-queue)** | Persistent SQLite jobs with leases, retries and recovery | [Code and setup](https://github.com/abhijith-abhii/durable-queue#readme) |

## LinkScope

URL shortener with campaign analytics.

- Custom aliases, expiry and link disabling
- Daily and referrer click aggregates
- Campaign labels and CSV export

**Stack:** Flask · SQLite

**Data:** Synthetic links; local click events

**Recorded checks:** 15 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** Counts describe visits, not unique people. The local application has no authenticated management or public anti-abuse service.

[Code and startup instructions](https://github.com/abhijith-abhii/linkscope#readme) · [Demonstration guide](https://github.com/abhijith-abhii/linkscope/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/linkscope/blob/main/VERIFICATION.md)

## NoteMesh

Shared meeting notes without lost edits.

- Saved-note synchronization over SSE
- Revision checks and preserved conflict drafts
- Persistent history and Markdown export

**Stack:** Flask · SQLite · SSE

**Data:** Local shared notes

**Recorded checks:** 13 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** Synchronization happens when a whole note is saved. There is no character-by-character collaborative merge. Room names are not authentication.

[Code and startup instructions](https://github.com/abhijith-abhii/notemesh#readme) · [Demonstration guide](https://github.com/abhijith-abhii/notemesh/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/notemesh/blob/main/VERIFICATION.md)

## Repo Radar

Understand public repository activity.

- Live GitHub snapshots with bounded pagination
- Five-minute cache and dated activity charts
- Explicit synthetic sample mode

**Stack:** Python · Flask

**Data:** GitHub REST API; labeled fixture

**Recorded checks:** 10 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** API rate limits and network availability affect live mode. A commit count is not a measure of developer performance or complete repository history.

[Code and startup instructions](https://github.com/abhijith-abhii/repo-radar#readme) · [Demonstration guide](https://github.com/abhijith-abhii/repo-radar/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/repo-radar/blob/main/VERIFICATION.md)

## TabHarbor

Organize crowded browser sessions.

- Domain-based tab groups and duplicate preview
- Saved workspaces and restore in a new window
- Alarm-based focus timer

**Stack:** Chrome MV3 · JavaScript

**Data:** Local browser tabs only

**Recorded checks:** 15 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** Verified with bundled Chromium on Linux CI; Chrome Web Store publication is not included. The extension has not been published in the Chrome Web Store. Workspaces save URLs, not login sessions or browsing history. Saved URLs are not encrypted.

[Code and startup instructions](https://github.com/abhijith-abhii/tabharbor#readme) · [Demonstration guide](https://github.com/abhijith-abhii/tabharbor/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/tabharbor/blob/main/VERIFICATION.md)

## Upstream Lab

Reproduce and improve an open-source behavior.

- Pinned python-slugify failure reproducer
- CLI regex validation patch
- Before-and-after regression evidence

**Stack:** Python · pytest

**Data:** Attributed upstream source

**Recorded checks:** 10 local project checks passed in the September 2026 verification. This directory update did not rerun the application.

**Scope:** No upstream pull request has been submitted or accepted. The reproducer deliberately stops if its existing var/upstream checkout is already modified.

[Code and startup instructions](https://github.com/abhijith-abhii/upstream-lab#readme) · [Demonstration guide](https://github.com/abhijith-abhii/upstream-lab/blob/main/LEARNING_GUIDE.md) · [Recorded verification](https://github.com/abhijith-abhii/upstream-lab/blob/main/VERIFICATION.md)

## Global Health Passport

Synthetic health workflows across Java, React and Expo.

- Consent, provenance and care-team workflows
- Shared backend for web and mobile clients
- Synthetic records and documented architecture

**Stack:** Java · Spring Boot · React · Expo

**Data:** Synthetic health data

**Scope:** Synthetic prototype; no live patient deployment or compliance certification.

[Code and startup instructions](https://github.com/abhijith-abhii/global-health-passport#readme) · [Demonstration guide](https://github.com/abhijith-abhii/global-health-passport#readme)

## Durable Queue

Persistent SQLite jobs with leases, retries and recovery.

- Transactional claims and expiring leases
- Retries, dead letters and idempotent enqueue
- Stale-worker fencing

**Stack:** Python · SQLite

**Data:** Local demonstration jobs

**Scope:** Single-host queue with at-least-once delivery; external side effects still require idempotency.

[Code and startup instructions](https://github.com/abhijith-abhii/durable-queue#readme) · [Demonstration guide](https://github.com/abhijith-abhii/durable-queue#readme)

## How to explore

Open a project's README, follow its startup instructions and demonstration, then review its design decisions and evidence. Datasets, dependencies and execution limits are explained in the linked repository. These are AI-assisted personal projects; code and tests are evidence of implementation, not employment deliverables or production adoption.
