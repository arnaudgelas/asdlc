# Waiver Template — Pilot Kit

**When to use this.** When a gate condition cannot be met at gate time
and the team requests temporary acceptance of the gap.

**Who fills this in.** The requester drafts; the grantor signs. The
grantor MUST be a different role from the human authorising the gate
pass for the same release (separation of duties).

**Deliverable.** One waiver record per granted exception. Permanent
waivers are NOT permitted; every waiver has an expiry date.

**Canonical source.** `waiver-governance.md`.

---

## Waiver record

- **Waiver ID:** `{{waiver_id}}`
- **Date filed:** `{{YYYY-MM-DD}}`
- **Linked specification ID:** `{{spec_id}}`
- **Linked release ID (if any):** `{{release_id}}`
- **Gate and condition waived:** `<e.g. RG-6, DoD-8, SR-7>`

## Requester

- Role: `<TODO>`
- Name: `<TODO>`

## Grantor (must differ from gate-pass authoriser for this release)

- Role: `<TODO>`
- Name: `<TODO>`
- Authority basis: `<TODO: e.g. delegated under operations/governance.md
  by the ASDLC Steward on YYYY-MM-DD>`

## Risk description

What is the gap? What is the risk if the gap is not closed? Which
authorities (cite by `id` from `freshness-register.yaml`) speak to this
risk?

`<TODO>`

## Compensating control

The compensating control MUST be operational at the time of issue, not
planned. Describe:

- Control: `<TODO>`
- Where it runs: `<TODO>`
- How it is monitored: `<TODO>`
- Evidence the control is operational today: `<TODO link>`

## Remediation plan

How and when will the underlying gap be closed?

- Owner: `<TODO>`
- Milestones:
  - `<TODO: YYYY-MM-DD — milestone>`
  - `<TODO: YYYY-MM-DD — milestone>`
- Expected closure date: `<TODO>`

## Expiry

- Expiry date (no permanent waivers): `{{YYYY-MM-DD}}`
- On-expiry behaviour: `<auto-revoke / requires re-grant / triggers
  retirement-gate consideration>`

## Sign-off

- Requester signature / commit: `<TODO>`
- Grantor signature / commit: `<TODO>`
- Date: `<TODO>`
