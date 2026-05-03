# Release Gate Template — Pilot Kit

**When to use this.** At the L2 -> L3 boundary, before deploying an
agent-built artefact to production.

**Who fills this in.** The release manager with input from the engineering
lead, security lead, and (where applicable at adoption phase 4 or for
high-stakes regulated systems) an organisationally-separate validator.

**Deliverable.** One filled file per release. Archive with the linked
evidence bundle.

**Canonical sources.** Condition list:
`governance/gate-registry.yaml`. Prose authority:
`release-governance.md`.

---

## Release metadata

- **Release ID:** `{{release_id}}`
- **Specification ID (link to SR Gate template):** `{{spec_id}}`
- **Artefact identifier (image digest / package hash):** `{{artefact_digest}}`
- **Adoption phase:** `<phase_1 / phase_2 / phase_3 / phase_4>`
- **High-stakes regulated:** `<yes / no>`
- **Blast radius tier:** `<1 / 2 / 3>`
- **External-facing:** `<yes / no>`
- **Date prepared:** `{{YYYY-MM-DD}}`

---

## RG-1 — Evidence Bundle Complete

Link the evidence bundle (filled from `evidence-bundle-template.md`):

- Bundle path / URL: `<TODO>`
- Bundle content hash: `<TODO>`

## RG-2 — Independent Validation Passed

Applicability: blocking at adoption phase 4+; blocking at any phase for
high-stakes regulated systems. Otherwise recommended.

**Organisationally-separate validator declaration:**

- Validator role: `<TODO>`
- Validator organisational unit: `<TODO>`
- Reporting line distinct from delivery team: `<yes / no — explain>`
- Validation report link: `<TODO>`
- Validation verdict: `<pass / fail / waived>`

## RG-3 — Rollback Procedure Tested

- Rollback procedure document: `<TODO>` (also see
  `runbook-template.md`)
- Rollback drill date: `<TODO>`
- Rollback drill outcome: `<TODO>`
- Time-to-rollback measured: `<TODO>`

## RG-4 — Accountable Human Sign-Off

- Accountable Human (must match SR-5 unless reassigned in writing):
  `<TODO>`
- Sign-off statement: `<TODO>`
- Sign-off date: `<TODO>`

## RG-5 — Compliance Documentation Complete

Scope is tier-dependent. Cite authorities by `id` from
`freshness-register.yaml`.

- Authorities in scope: `<TODO: list of IDs>`
- Mapping document: `<TODO>`
- Domain profile applied (if any from `domains/`): `<TODO>`

## RG-6 — Dynamic Security Testing Passed

Applicability: blocking for external-facing changes and blast-radius tier
2/3. Recommended at tier 1.

- DAST tool / suite used: `<TODO>`
- Date of run: `<TODO>`
- Findings summary: `<TODO>`
- Open critical/high findings: `<TODO>`
- Sign-off by Security Engineering Lead: `<TODO>`

## RG-7 — Control State Record Complete and Current

The Control State Record format is the canonical artefact described in
`release-governance.md`. Fill the following fields:

- Control State Record ID: `<TODO>`
- Records all currently-applicable controls: `<yes / no>`
- Records control verdict per item: `<yes / no>`
- Records exceptions/waivers: `<yes / no>`
- Records reproducibility surface: `<yes / no>`
- Records foundation-model dependencies (model id, version, hash, drift
  status): `<yes / no>`
- Foundation-model drift status: `<no_drift / drift_detected_within_tolerance / drift_exceeds_tolerance>`
  - If drift_exceeds_tolerance, link the re-evaluation record: `<TODO>`
- Reproducibility surface declared:
  - Build provenance attestation (SLSA / in-toto): `<TODO link>`
  - Training data snapshot or version: `<TODO>`
  - Prompt set hash (where applicable): `<TODO>`
  - Random seeds / nondeterminism declarations: `<TODO>`

## RG-8 — Waiver Governance

- Waivers attached to this release: `<count>`
- Waiver IDs (each filled per `waiver-template.md`): `<TODO>`
- Each waiver has a non-permanent expiry: `<yes / no>`
- Each waiver has a compensating control operational at issue time:
  `<yes / no>`

---

## Gate Decision

| Condition | Verdict |
| --- | --- |
| RG-1 | `<pass / fail / missing / waived / requires-human-decision>` |
| RG-2 | `<...>` |
| RG-3 | `<...>` |
| RG-4 | `<...>` |
| RG-5 | `<...>` |
| RG-6 | `<...>` |
| RG-7 | `<...>` |
| RG-8 | `<...>` |

**Overall verdict:** `<pass / fail / requires-human-decision>`

**Deciding human (must NOT also be the waiver grantor for any attached
waiver):**

- Name: `<TODO>`
- Role: `<TODO>`
- Date: `<TODO>`
- Signature / commit hash: `<TODO>`
