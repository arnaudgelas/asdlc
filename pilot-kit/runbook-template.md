# Runbook Template — Pilot Kit

**When to use this.** Drafted late in L2; finalised at L3 -> L4 readiness
to satisfy DoD-1 (Runbook Complete).

**Who fills this in.** The system steward (DoD-4) with the on-call lead.

**Deliverable.** One runbook per system in operational service. Linked
from the DoD template and the evidence bundle.

**Canonical sources.** `operations/dod.md` (DoD-1 prose), and the SLO /
observability requirements in DoD-2.

---

## System metadata

- **System name:** `{{system_name}}`
- **Specification ID:** `{{spec_id}}`
- **Release ID:** `{{release_id}}`
- **Owners:** `<system steward role>; <on-call rotation>`
- **Last updated:** `{{YYYY-MM-DD}}`

## Architecture overview

One paragraph + one diagram link. Cover:

- What the system does (one sentence).
- Core components and dependencies.
- External services and identities.
- Data flow at a glance.

`<TODO>`

## SLOs

| SLO ID | Description | Target | Measurement window |
| --- | --- | --- | --- |
| SLO-1 | `<TODO>` | `<TODO>` | `<TODO>` |
| SLO-2 | `<TODO>` | `<TODO>` | `<TODO>` |

## Alerting thresholds

| Alert | Trigger | Routes to | Severity |
| --- | --- | --- | --- |
| `<TODO>` | `<TODO>` | `<TODO>` | `<P1/P2/P3>` |

## Known failure modes

For each failure mode: symptom, detection signal, immediate action,
escalation criterion.

- Failure mode 1: `<TODO>`
- Failure mode 2: `<TODO>`

## Escalation chain

1. On-call primary: `<TODO>`
2. On-call secondary: `<TODO>`
3. System steward: `<TODO>`
4. Accountable Human: `<TODO>`
5. Domain SME (where applicable): `<TODO>`

## Rollback procedure

Linked to RG-3 evidence.

- Trigger criteria: `<TODO>`
- Step-by-step procedure: `<TODO>`
- Last drill date and outcome: `<TODO>`
- Estimated time-to-rollback: `<TODO>`

## Routine operational tasks

- Trace retention enforcement (DoD-7): `<TODO>`
- Security re-scan cadence (DoD-5): `<TODO>`
- License re-check cadence (DoD-6): `<TODO>`
- Foundation-model drift monitoring: `<TODO>`

## Cross-references

- Specification (SR Gate template): `<TODO link>`
- Release evidence bundle: `<TODO link>`
- Operational DoD record: `<TODO link>`
- Authority citations (by `id` from `freshness-register.yaml`):
  `<TODO>`

## Change history

| Date | Change | Author |
| --- | --- | --- |
| `<TODO>` | Initial version | `<TODO>` |
