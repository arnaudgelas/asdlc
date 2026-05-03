# Operational DoD Template — Pilot Kit

**When to use this.** At the L3 -> L4 Operational Readiness Gate, and on
the steward's recurring cadence thereafter (practitioner default:
quarterly).

**Who fills this in.** The system steward (DoD-4) with the on-call lead
(DoD-3) and security engineering.

**Deliverable.** One filled file per system in operational service. The
DoD is a **persistent obligation** — re-check on cadence; do not treat as
one-time.

**Canonical sources.** Condition list:
`governance/gate-registry.yaml`. Prose authority:
`operations/dod.md`.

---

## System metadata

- **System ID:** `{{system_id}}`
- **Specification ID (SR Gate file):** `{{spec_id}}`
- **Release ID (RG Gate file):** `{{release_id}}`
- **Blast radius tier:** `<1 / 2 / 3>`
- **Date of L3 -> L4 readiness check:** `{{YYYY-MM-DD}}`
- **Next persistent re-check due:** `{{YYYY-MM-DD}}`

---

## DoD-1 — Runbook Complete

- Runbook path: `<TODO>` (filled from `runbook-template.md`)
- Architecture overview present: `<yes / no>`
- Failure modes documented: `<yes / no>`
- Escalation chain documented: `<yes / no>`

## DoD-2 — Operational Observability Configured

- Telemetry source: `<TODO>` (logs, metrics, traces)
- SLOs defined:
  - SLO-1: `<TODO: e.g. p95 latency < 500ms>`
  - SLO-2: `<TODO>`
- Alerting thresholds linked to SLOs:
  - Alert-1: `<TODO>`
  - Alert-2: `<TODO>`
- Dashboard URL: `<TODO>`

## DoD-3 — On-Call Assignment Made

- Primary on-call rotation: `<TODO>`
- Secondary / escalation: `<TODO>`
- Schedule tool: `<TODO>` (e.g. PagerDuty, Opsgenie)
- Acknowledged by on-call lead: `<TODO: role + date>`

## DoD-4 — System Steward Assigned

- Steward role: `<TODO>`
- Steward name: `<TODO>`
- Steward acceptance date: `<TODO>`
- Successor role identified: `<TODO>`

## DoD-5 — Security Scan Clean

- SAST tool + run date: `<TODO>`
- Dependency / SCA tool + run date: `<TODO>`
- Container / image scan + run date: `<TODO>`
- Secrets scan + run date: `<TODO>`
- Findings summary: `<TODO>`
- Open critical/high findings: `<TODO>`

## DoD-6 — License Compliance Confirmed

- License inventory (SPDX or equivalent): `<TODO>`
- Disallowed licenses present: `<yes / no — list>`
- Reviewer: `<TODO>`

## DoD-7 — Trace Retention Policy Set

- Trace retention period: `<TODO>`
- Retention policy reference (jurisdiction-specific where applicable):
  `<TODO>`
- Storage location: `<TODO>`
- Access control: `<TODO>`

## DoD-8 — DR/Failover Tested (conditional on blast radius 3)

Applicability: blocking for blast-radius tier 3. Recommended at tier 1
and 2 unless required by regulatory or contractual mandate.

- Applicable: `<yes — blocking / yes — recommended / no>`
- Last DR drill date: `<TODO>`
- RTO measured: `<TODO>`
- RPO measured: `<TODO>`
- Outcome: `<TODO>`

---

## Operational Readiness Verdict

| Condition | Verdict |
| --- | --- |
| DoD-1 | `<pass / fail / missing / waived / requires-human-decision>` |
| DoD-2 | `<...>` |
| DoD-3 | `<...>` |
| DoD-4 | `<...>` |
| DoD-5 | `<...>` |
| DoD-6 | `<...>` |
| DoD-7 | `<...>` |
| DoD-8 | `<pass / fail / not_applicable>` |

**Overall verdict:** `<pass / fail / requires-human-decision>`

**Steward sign-off:**

- Name: `<TODO>`
- Role: `<TODO>`
- Date: `<TODO>`

**Persistent re-check schedule:** quarterly (default) or as set by the
steward; record next due date above.
