# 30-Day Pilot Calendar — Pilot Kit

A 30-day ASDLC pilot is a single demand item taken end-to-end across the
four layers, producing one of every artefact in this kit. The calendar
below is a default; teams may compress or extend.

**Prerequisite.** A pilot demand item identified at L1, blast-radius tier
1 or 2, with an Accountable Human pre-named.

---

## Week 1 — SR Gate pilot (Days 1-7)

**Goal.** Validate one demand item end-to-end through the SR Gate.

**Activities.**

- Day 1-2: Author specification using `sr-gate-template.md`.
- Day 3-4: Assemble context thread (SR-9), cite authorities by `id` from
  `freshness-register.yaml`.
- Day 5: Internal review; resolve any `requires-human-decision` items.
- Day 6: SR Gate decision meeting; record verdicts per condition.
- Day 7: File `Specification` and `Human` nodes plus
  `signed_off_by` edge in `graph-lite-nodes.csv` and
  `graph-lite-edges.csv`.

**Exit criteria.** SR Gate template fully filled with overall verdict
`pass` (or `requires-human-decision` resolved before Week 2 begins).

**Artefacts produced.** One filled `sr-gate-template.md`; up to one
filled `waiver-template.md`; two CSV rows.

---

## Week 2 — Engineering execution + Release Gate pilot (Days 8-14)

**Goal.** Run one engineering loop iteration; pass it through the Release
Gate.

**Activities.**

- Day 8-10: Engineering execution (agent loop or human/agent
  collaboration) producing the candidate artefact.
- Day 11: Assemble evidence bundle using
  `evidence-bundle-template.md`.
- Day 12: Run security tests (RG-6, where applicable). Run independent
  validation if adoption phase 4+ or high-stakes regulated (RG-2).
- Day 13: Draft Control State Record (RG-7). Test and document rollback
  (RG-3).
- Day 14: Release Gate decision using `release-gate-template.md`. Add
  `Release`, `EvidenceBundle`, `Authority`, `Waiver` nodes
  and corresponding edges to the graph-lite CSVs.

**Exit criteria.** Release Gate template fully filled with overall
verdict `pass`. Evidence bundle archived with content hash. Any waiver
filed has a non-permanent expiry and an operational compensating control.

**Artefacts produced.** One filled `release-gate-template.md`; one
filled `evidence-bundle-template.md`; zero or more
`waiver-template.md` records; updated graph-lite CSVs.

---

## Week 3 — Operational handoff + Operational DoD pilot (Days 15-21)

**Goal.** Stand up the system in operations; pass the L3 -> L4
Operational Readiness Gate.

**Activities.**

- Day 15-16: Author runbook using `runbook-template.md`.
- Day 17: Configure observability and alerts; declare SLOs.
- Day 18: Assign on-call rotation and system steward (DoD-3, DoD-4).
- Day 19: Run security scan suite (DoD-5); confirm license inventory
  (DoD-6); set trace retention (DoD-7).
- Day 20: If blast-radius tier 3, run DR/failover drill (DoD-8).
- Day 21: Operational Readiness Gate decision using
  `operational-dod-template.md`. Add `Runbook` node and
  `governed_by` edges to graph-lite CSVs.

**Exit criteria.** DoD template fully filled with overall verdict
`pass`. Runbook archived. Persistent re-check schedule recorded.

**Artefacts produced.** One filled `operational-dod-template.md`; one
filled `runbook-template.md`; updated graph-lite CSVs.

---

## Week 4 — Retrospective + governance graph spot-check (Days 22-30)

**Goal.** Assess the pilot outcome; produce a 30-day report.

**Activities.**

- Day 22-23: Run governance graph spot-check using `graph-lite-csv.md`
  recipes. Verify:
  - Every release node reaches back to a specification node.
  - Every release node has an evidence-bundle node.
  - Every cited authority appears as an `Authority` node.
  - Every waiver has a non-lapsed expiry.
- Day 24: Run `python3 scripts/check_links.py --root .` on the pilot
  artefact directory; resolve any broken links.
- Day 25-26: Retrospective with the pilot team. Capture what worked,
  what didn't, what scaled, what didn't.
- Day 27-28: Author 30-day report (free-form). Cover:
  - Which gate conditions were easy / hard.
  - Which authorities were over- or under-applied.
  - Whether the team can sustain the cadence at scale.
  - Recommended next-step adoption phase.
- Day 29: Internal review of the 30-day report.
- Day 30: Decision: proceed to broader adoption, run a second pilot, or
  decline. Record the decision with the deciding human.

**Exit criteria.** 30-day report archived with the pilot artefacts.
Graph-lite CSVs handed to whoever owns migration to a real graph store
(if adoption proceeds).

**Artefacts produced.** One 30-day report; final graph-lite CSVs.

---

## Anti-patterns to avoid in a 30-day pilot

- **Choosing a tier-3 demand item.** Pilots are for learning; tier-3
  systems should adopt under a domain profile in `domains/` with full
  conformance scaffolding.
- **Skipping waivers.** If a condition cannot be met, file a waiver
  rather than silently proceeding. The pilot's value is partly in
  exposing waiver throughput.
- **Treating DoD as one-time.** DoD is a persistent obligation; record
  the next re-check date in Week 3 even though the pilot ends in Week 4.
- **Hand-coding gate condition lists.** All condition lists come from
  `governance/gate-registry.yaml`. Templates in this kit reference but
  do not restate them.
