# ASDLC 30-Day Pilot Kit

This directory is the **minimum-viable adoption package** for an
organization piloting ASDLC for 30 days. It is deliberately small. It is
NOT a substitute for full ASDLC adoption — it produces just enough
evidence for a pilot team to assess whether ASDLC fits their environment
before committing to a full rollout.

## What is in the kit

Seven templates plus a 30-day calendar. Each template targets one
artefact a real ASDLC adoption produces; the templates are minimal,
fillable, and reference the canonical sources rather than restating them.

| File | Purpose |
| --- | --- |
| `sr-gate-template.md` | Single-specification template for the Specification Readiness Gate (9 conditions). |
| `release-gate-template.md` | Release Gate template (8 conditions). |
| `operational-dod-template.md` | Operational Definition of Done template — 8 total conditions (7 unconditional + 1 blast-radius-tier-3-only conditional). |
| `evidence-bundle-template.md` | Skeleton evidence bundle satisfying RG-1. |
| `waiver-template.md` | Waiver record per `waiver-governance.md`. |
| `runbook-template.md` | Minimal runbook for L4 operational handoff. |
| `graph-lite-csv.md` | Minimal CSV-format governance graph instance + migration notes. |
| `graph-lite-nodes.csv` | CSV node table for the graph-lite instance. |
| `graph-lite-edges.csv` | CSV edge table for the graph-lite instance. |
| `30-day-calendar.md` | Week-1-to-Week-4 detailed pilot schedule. |

## Canonical references

Templates do not restate the conditions; they reference the source of
truth:

- Gate condition lists: `governance/gate-registry.yaml` and
  `governance/gate-registry.md`.
- SR Gate prose authority: `specification-readiness.md`.
- Release Gate prose authority: `release-governance.md`.
- Operational DoD prose authority: `operations/dod.md`.
- Waiver governance: `waiver-governance.md`.
- Governance graph schema: `governance/graph.md`.
- External-authority freshness: `freshness-register.yaml`.

## Scope of a 30-day pilot

A pilot is one demand item taken end-to-end through:

1. SR Gate (Week 1).
2. Engineering loop + Release Gate (Week 2).
3. Operational handoff + DoD (Week 3).
4. Retrospective + governance graph spot-check + 30-day report (Week 4).

The pilot demand item should be **non-trivial but bounded** — blast
radius tier 1 or 2, not tier 3. A high-stakes regulated workload is
inappropriate for a pilot; for those, run the full ASDLC adoption track
under the relevant domain profile in `domains/`.

## What "successful pilot" means

At the end of 30 days, the pilot produces:

- One filled SR Gate template (with verdict per condition).
- One filled Release Gate template + evidence bundle.
- One filled DoD template + runbook.
- A populated `graph-lite-nodes.csv` and `graph-lite-edges.csv`.
- A 30-day report (template not required; free-form).
- Zero or more waivers, each with a tracked expiry.

If the team cannot complete this set in 30 days, the report explains
what blocked them — that is itself useful evidence about ASDLC fit.

## Migration after the pilot

If the pilot succeeds and the organization commits to broader ASDLC
adoption, the graph-lite CSVs migrate to a real graph store (Neo4j or
RDF triplestore); see `graph-lite-csv.md` for the migration recipe and
`governance/graph.md` for the canonical schema.

## What this kit deliberately omits

- Full conformance-profile selection (see `conformance-profiles.md`).
- Domain-specific profile depth (see `domains/`).
- Adoption-cost modeling (see `annex-adoption-cost.md`).
- Phase-4 independent validation gating (see RG-2 in
  `release-governance.md`).
- Maintenance-governance and retirement-gate templates (out of scope at
  30 days).

These are the right things to add in a 90-day or 180-day expansion.
