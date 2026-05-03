# SR Gate Template — Pilot Kit

**When to use this.** At the L1 -> L2 boundary, before any agent loop
begins engineering execution on a demand item.

**Who fills this in.** The Accountable Human (SR-5) with the
specification author. The Gate Decision block at the bottom is signed by
the deciding human (may be the same person if no separation-of-duties
policy applies in the pilot).

**Deliverable.** One filled file per pilot specification. Archive
alongside the evidence bundle for end-to-end traceability.

**Canonical sources.** Condition list:
`governance/gate-registry.yaml`. Prose authority:
`specification-readiness.md`.

---

## Specification metadata

- **Specification ID:** `{{spec_id}}`
- **Title:** `{{spec_title}}`
- **Demand item link:** `{{demand_link}}`
- **Author:** `{{author_role}}`
- **Accountable Human:** `{{accountable_human_role}}`
- **Blast radius tier (preliminary):** `{{tier_1_2_or_3}}`
- **Date drafted:** `{{YYYY-MM-DD}}`

---

## SR-1 — Business Need Validated

Prompt: state the business need and the validation evidence (interview
notes, OKR link, customer-impact data). One paragraph.

`<TODO: business need + validation evidence>`

## SR-2 — Value Measurable

Prompt: define the success metric, its baseline, and its target. The
metric must be measurable from operational telemetry post-deployment.

- Metric: `<TODO>`
- Baseline: `<TODO>`
- Target: `<TODO>`
- Measurement source: `<TODO>`

## SR-3 — Acceptance Criteria Expressible

Prompt: enumerate acceptance criteria as testable assertions.

- AC1: `<TODO>`
- AC2: `<TODO>`
- ACn: `<TODO>`

## SR-4 — Constraints Identified

Prompt: list regulatory, contractual, technical, organisational
constraints. Reference authorities by `id` from
`freshness-register.yaml` where applicable.

`<TODO: constraints + authority IDs>`

## SR-5 — Accountable Human Named

- Role: `<TODO>`
- Name: `<TODO>`
- Authority basis: `<TODO>` (e.g. delegated by VP Engineering on
  YYYY-MM-DD)

## SR-6 — Blast Radius Assessed

Prompt: justify the tier (1/2/3) using
`specification-readiness.md` blast-radius criteria. State the worst
plausible failure and its scope.

- Tier: `<TODO>`
- Worst plausible failure: `<TODO>`
- Scope: `<TODO: users, systems, data, regulators>`

## SR-7 — Out-of-Scope Explicitly Stated

Prompt: enumerate what the agent loop MUST NOT do. Closed-form list.

`<TODO>`

## SR-8 — Loop Cost Justified

Prompt: state the loop's expected token / wallclock / human-review cost
and justify against expected value (from SR-2). Calibrate depth to
blast-radius tier.

- Estimated cost: `<TODO>`
- Estimated value: `<TODO>`
- Justification: `<TODO>`

## SR-9 — Context Thread Assembled and Reviewed

Prompt: list every input the agent loop will receive (specs, prior
runbooks, threat models, authority citations from
`freshness-register.yaml`). Confirm a human has read the assembled
thread.

- Context inventory: `<TODO>`
- Human reviewer: `<TODO: role>`
- Review date: `<TODO: YYYY-MM-DD>`

---

## Gate Decision

| Condition | Verdict |
| --- | --- |
| SR-1 | `<pass / fail / missing / waived / requires-human-decision>` |
| SR-2 | `<...>` |
| SR-3 | `<...>` |
| SR-4 | `<...>` |
| SR-5 | `<...>` |
| SR-6 | `<...>` |
| SR-7 | `<...>` |
| SR-8 | `<...>` |
| SR-9 | `<...>` |

Verdict enum mirrors `gate_state_enum` in
`governance/gate-registry.yaml`.

**Overall verdict:** `<pass / fail / requires-human-decision>`

If any condition is `waived`, link the waiver record produced from
`waiver-template.md`:

- Waiver ID(s): `<TODO>`

**Deciding human:**

- Name: `<TODO>`
- Role: `<TODO>`
- Date: `<TODO: YYYY-MM-DD>`
- Signature / commit hash: `<TODO>`
