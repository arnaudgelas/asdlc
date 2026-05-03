# Annex — Adoption Economics and Capacity Model

_An annex documenting the resourcing implications of adopting and operating
the Agentic Software Delivery Lifecycle. The figures in this annex are
indicative, anchored to industry benchmarks where benchmarks exist. They
are not authoritative cost projections for any specific organisation;
calibration against local conditions is required before they are used as
budget inputs._

See [asdlc-guide.md](asdlc-guide.md) for the AdoptionPhase model that
structures the figures below. See [conformance-profiles.md](conformance-profiles.md)
for the profile definitions that determine which cost band an organisation
sits in. See [governance/gate-registry.md](governance/gate-registry.md) for
the gate condition counts that drive reviewer-hour estimates.

---

## Disclaimer

The figures presented here are indicative and pending field calibration.
They are derived from a combination of practitioner experience, public
benchmarks for adjacent governance regimes (DevOps platform engineering
ratios, model risk management staffing in regulated banking, ITIL service
management overheads), and published cloud-cost references for inference
workloads. They are not the result of a controlled study across multiple
organisations operating ASDLC at scale, because that population does not
yet exist at the scale required for statistical calibration. An organisation
using these figures as budget inputs must treat them as starting estimates
and refine them against its own operational telemetry within the first two
quarters of operation. The figures are presented as ranges, not point
estimates, to discourage false precision.

Where industry benchmarks are cited, the benchmark is named at the relevant
table. Where no benchmark exists, the table notes "practitioner estimate".

---

## Reviewer-hours per gate by tier

The reviewer-hours below state the human time required per gate decision,
not the total gate cycle time. Cycle time is governed by gate-readiness
predictability (see release-governance.md "Predictive Gate Clearing"); the
reviewer-hours are the floor of the human time the gate consumes regardless
of cycle time.

The figures are stated by BlastRadiusTier (BR) and AutonomyTier (A). Higher
BR and lower A both increase reviewer-hours: higher blast radius requires
more substantive review per condition, and lower autonomy means more
condition assessments are not eligible for agent-proposed-with-human-review
acceleration.

### Specification Readiness Gate (9 conditions)

| BlastRadiusTier | A1 (advisory only) | A2 (monitored) | A3 (human-gated) | A4 (human-in-loop on tasks) |
|------------------|--------------------|------------------|--------------------|------------------------------|
| BR1 | 1.0 – 2.0 hours | 1.5 – 3.0 hours | 2.0 – 4.0 hours | 3.0 – 5.0 hours |
| BR2 | 2.0 – 4.0 hours | 3.0 – 5.0 hours | 4.0 – 7.0 hours | 5.0 – 9.0 hours |
| BR3 | 4.0 – 8.0 hours | 5.0 – 10.0 hours | 7.0 – 14.0 hours | 9.0 – 18.0 hours |

### Release Gate (8 conditions)

| BlastRadiusTier | A1 | A2 | A3 | A4 |
|------------------|------|------|------|------|
| BR1 | 1.5 – 3.0 hours | 2.0 – 4.0 hours | 3.0 – 5.0 hours | 4.0 – 7.0 hours |
| BR2 | 3.0 – 6.0 hours | 4.0 – 8.0 hours | 6.0 – 10.0 hours | 8.0 – 14.0 hours |
| BR3 | 6.0 – 12.0 hours | 8.0 – 16.0 hours | 12.0 – 22.0 hours | 16.0 – 30.0 hours |

### Operational Readiness Gate (8 conditions)

| BlastRadiusTier | A1 | A2 | A3 | A4 |
|------------------|------|------|------|------|
| BR1 | 1.0 – 2.0 hours | 1.5 – 3.0 hours | 2.0 – 4.0 hours | 3.0 – 5.0 hours |
| BR2 | 2.0 – 4.0 hours | 3.0 – 5.0 hours | 4.0 – 7.0 hours | 5.0 – 9.0 hours |
| BR3 | 4.0 – 8.0 hours (BR3 includes DR/failover review under DoD-8) | 5.0 – 10.0 hours | 7.0 – 14.0 hours | 9.0 – 18.0 hours |

The ranges widen with BR because high-blast-radius systems involve more
artefacts per condition (more eval results, larger SBOMs, more compliance
filings); they also widen with A4 because human-in-loop operation produces
more decisions per gate that require human attestation. Practitioner
estimate; no public benchmark.

---

## Steward portfolio bounds

A System Steward holds ongoing accountability for the operational governance
of the systems in their portfolio. The maximum portfolio size is bounded
because the steward's reviews must remain substantive, not nominal. A
steward whose portfolio exceeds the bounds below is operating a system
count that cannot be substantively governed at the cadence the Operational
DoD requires.

| Steward portfolio dimension | A1–A2 systems | A3 systems | A4 systems | Tier 4 envelopes |
|------------------------------|----------------|--------------|--------------|--------------------|
| Active systems per steward (max) | 12 – 20 | 6 – 10 | 3 – 5 | n/a |
| Active envelopes per steward (max) | n/a | n/a | n/a | 1 – 3 |
| Active waivers per steward (max, across portfolio) | 8 – 15 | 5 – 10 | 3 – 6 | 2 – 5 per envelope |

The waiver bound exists because each waiver carries an expiry-tracking
obligation and, typically, a compensating-control monitoring obligation. A
steward holding more active waivers than the bound is operating a portfolio
in which waiver accountability has degraded into list-keeping. Practitioner
estimate, anchored to model risk management practices in regulated banking
where MRM "model owners" typically hold portfolios of 8 to 20 models with
analogous review obligations.

---

## Inference budget bounds per gate

The inference budgets below apply where governance agents are used at the
gate (evidence bundle assembly, control state record validation, gate
readiness assessment, predictive clearing). They state the rough USD spend
per gate decision. They do not include the inference cost of the underlying
delivery loop, which is governed separately under FinOps governance.

| BlastRadiusTier | SR Gate | Release Gate | Operational Gate |
|------------------|------------|----------------|--------------------|
| BR1 | $0.50 – $3 | $1 – $6 | $0.50 – $3 |
| BR2 | $2 – $12 | $4 – $25 | $2 – $12 |
| BR3 | $5 – $40 | $10 – $80 | $5 – $40 |

Footnote: Inference token pricing is volatile. The figures above assume
mid-2025 published prices for frontier-class models used as the analysis
backbone, with smaller models invoked for sub-tasks where structured
extraction is sufficient. The ranges should be re-derived against current
provider pricing every two quarters; an organisation that does not refresh
the budgets against provider price changes is operating against stale
budgets.

---

## Minimum tooling per AdoptionPhase

The minimum tooling required at each AdoptionPhase is stated below.
Operating at a higher AdoptionPhase without the corresponding tooling is
self-contradictory: the AdoptionPhase claim is a description of operational
maturity, and the tooling is the operational substrate that makes that
maturity possible.

### AdoptionPhase 1 (foundation)

- Manual gate logs: structured records of SR, Release, and Operational gate
  decisions captured in a versioned text or markdown system.
- Manual evidence bundle assembly: evidence artefacts collected by hand
  into a release-folder convention, with a manual completeness checklist.
- Manual waiver tracking: a single spreadsheet or text register of active
  waivers, their grantors, and their expiry dates.
- No automation requirement at this phase; the obligation is record-
  keeping discipline.

### AdoptionPhase 3 (instrumented)

- Governance graph store: a queryable store implementing the node and edge
  types defined in [governance/graph.md](governance/graph.md), populated
  from delivery-pipeline events.
- Evidence registry: a content-addressable store for evidence artefacts,
  with hash-based integrity and retrieval-by-bundle-ID.
- Basic evaluation harness: an evaluation runner that can produce machine-
  readable evaluation reports with timestamps, IDs, and pass/fail verdicts
  consumable by the evidence bundle assembly.
- Control state record generation: a tool that produces the structured
  control state record from evaluation outputs and the bundle's contents,
  suitable for ingestion at the Release Gate.

### AdoptionPhase 5 (continuous)

- All AdoptionPhase 3 tooling, plus:
- Push notifications and active monitoring: governance agents producing
  scheduled and event-driven readiness reports per release-governance.md
  predictive gate clearing.
- Automated drift detection: continuous monitoring of operational DoD
  conformance per system, with steward notifications on detected drift
  before the next quarterly review.
- Champion / challenger evaluation: evaluation harness extended to support
  comparative model and prompt evaluation under controlled traffic
  splitting, with results integrated into the evidence bundle.
- FinOps attribution: cost attribution per system, per gate, per agent
  invocation; integrated into operational dashboards and Layer 1 demand
  decisions.

---

## Headcount uplift per AdoptionPhase

The headcount uplift below states the additional FTE that ASDLC adoption
imposes on top of an existing engineering organisation, per 100 engineers
(or per 10 ARTs, where the SAFe scaling integration in [annex-safe.md](annex-safe.md)
applies). The uplift is incremental, not gross; it is the net new staffing
that ASDLC adoption requires above what a non-ASDLC organisation of the
same size would already employ.

### Per 100 engineers / per 10 ARTs

| Role | AdoptionPhase 1 | AdoptionPhase 3 | AdoptionPhase 5 |
|------|------------------|------------------|------------------|
| System Stewards (named accountable governance owners) | 0.5 – 1.5 FTE | 2 – 4 FTE | 4 – 7 FTE |
| Governance Portfolio Owner (cross-system steward oversight) | 0 – 0.5 FTE | 1 – 2 FTE | 2 – 3 FTE |
| Release Manager uplift (above pre-ASDLC baseline) | 0.5 – 1 FTE | 1 – 2 FTE | 2 – 3 FTE |
| Compliance Liaison (the bridge between ASDLC artefacts and regulatory filings) | 0 – 1 FTE | 1 – 2 FTE | 2 – 4 FTE |
| Governance Tooling SRE (operates the governance infrastructure as a governed system per `asdlc.md` "Governance of Governance") | 0 – 0.5 FTE | 1 – 2 FTE | 3 – 5 FTE |

Total range per 100 engineers: AdoptionPhase 1 → 1 – 4.5 FTE;
AdoptionPhase 3 → 6 – 12 FTE; AdoptionPhase 5 → 13 – 22 FTE.

The per-engineer uplift narrows at scale: an organisation of 1,000
engineers does not need ten times the AdoptionPhase 5 staffing of an
organisation of 100, because some functions (Governance Portfolio Owner,
governance-tooling SRE) scale sub-linearly. Practitioner estimate,
anchored to public DevOps platform-engineering ratios (Puppet State of
DevOps and DORA reports historically place platform engineering at
roughly 5–10% of engineering headcount in mature organisations) and to
regulated-bank model risk management ratios (where MRM staff are
typically 1–3% of model-development staff).

---

## Worked example: a 500-engineer organisation at AdoptionPhase 3, five ARTs, ASDLC-Regulated

The worked example below illustrates the application of the figures above
to a specific organisation. The figures are illustrative; an actual
adoption planning exercise must use the organisation's own systems
inventory, cadence, and cost basis.

### Organisation profile

- 500 engineers across five ARTs (100 engineers per ART on average).
- AdoptionPhase 3.
- ASDLC-Regulated profile (per [conformance-profiles.md](conformance-profiles.md)).
- 35 active production systems, distributed: 15 BR1, 15 BR2, 5 BR3.
- Autonomy mix: 10 A1, 18 A2, 7 A3, 0 A4 (no Tier 4 envelopes yet).
- Release cadence: ARTs release fortnightly; total ~140 release-gate
  decisions per quarter across the organisation.

### FTE uplift (incremental)

Applying the per-100-engineers ranges to a 500-engineer organisation, with
the sub-linear scaling adjustment for shared functions:

- System Stewards: 10 – 20 FTE (across 35 systems; mean steward portfolio
  ~3 systems).
- Governance Portfolio Owner: 3 – 5 FTE (one portfolio owner per ART plus
  a cross-organisational owner).
- Release Manager uplift: 4 – 8 FTE (above pre-ASDLC release-management
  baseline).
- Compliance Liaison: 4 – 8 FTE.
- Governance Tooling SRE: 4 – 8 FTE.

Total incremental FTE: 25 – 49 FTE. Mid-range: ~35 FTE — approximately
7% of the engineering headcount.

### Gate-hours per quarter

- SR Gate decisions per quarter: ~140 (one per Feature accepted into PI;
  five ARTs × ~28 Features per ART per quarter). Mean SR Gate hours per
  decision (BR-mix-weighted, A-mix-weighted): ~3.5 hours. Total: ~490
  reviewer-hours per quarter.
- Release Gate decisions per quarter: ~140. Mean Release Gate hours per
  decision (BR-mix-weighted): ~6.5 hours. Total: ~910 reviewer-hours per
  quarter.
- Operational Gate decisions per quarter: ~12 (new system introductions
  per quarter at AdoptionPhase 3). Plus quarterly DoD reviews of all 35
  systems: 35 × 2 hours = 70 hours.

Total gate reviewer-hours per quarter: ~1,470 hours, or roughly 11 FTE
quarter-equivalents distributed across the named roles above.

### Infrastructure cost (illustrative)

- Governance graph store: ~$30k – $60k annual run-rate (managed graph DB +
  ingestion pipeline).
- Evidence registry: ~$15k – $30k annual run-rate (content-addressable
  storage + indexing).
- Evaluation harness compute: variable; budget ~$100k – $250k annual at
  this scale, dominated by inference cost for evaluation runs.
- Governance agent inference: applying the per-gate inference ranges and
  the gate volumes above, ~$15k – $80k per quarter, or ~$60k – $320k
  annual.

Total infrastructure annual cost: ~$200k – $660k — under 1% of the
fully-loaded engineering cost at this scale, but a non-trivial line item
that must be funded as runway, not absorbed by individual teams.

---

## Anti-patterns

### Under-resourced steward portfolios

The steward bound exists because steward review must be substantive, not
nominal. A steward holding twice the portfolio bound is producing reviews
that have neither the time nor the depth required by the Operational DoD;
their sign-offs are present but their substance is not. The detection
signal is the steward's review-time distribution: a portfolio whose
quarterly DoD reviews consume an average of less than 30 minutes per
system is being reviewed nominally. The corrective action is to reduce
the portfolio, not to streamline the review.

### Ceremony theatre

ASDLC obligations can be operationalised as ceremonies — gate meetings,
release readiness reviews, quarterly DoD reviews — that satisfy the form
of the obligation while losing the substance. The detection signal is the
defect rate observed downstream of the ceremony: a release readiness
review that produces no findings across 20 consecutive releases is either
operating against an unusually low defect rate or is detecting nothing.
Against base rates of release defects across the industry, the second
explanation is more likely. The corrective action is to raise the
evidence-presentation requirements at the ceremony, not to add another
ceremony.

### Single throat to choke compliance reviewer

A compliance liaison who reviews every artefact across every system is a
single point of failure for the organisation's gate throughput. The
detection signal is compliance-review queue length: a queue that
exceeds three business days at the median is a structural bottleneck. The
corrective action is to stratify compliance review by system risk profile,
delegate first-pass review to embedded reviewers within the ARTs, and
reserve the central liaison's time for portfolio-level escalations and
externally-facing filings — not to hire a second equally-loaded liaison
into the same single-point structure.

---

## Relationship to other ASDLC documents

The cost figures here are downstream of the conformance profile an
organisation claims; an organisation moving between profiles
(ASDLC-Minimum → ASDLC-Regulated → ASDLC-Tier4) will see the cost band
shift. See [conformance-profiles.md](conformance-profiles.md) for the
profile definitions that drive the cost tier.

The reviewer-hour estimates depend on the canonical condition counts in
[governance/gate-registry.md](governance/gate-registry.md). If the
registry's condition counts change, the reviewer-hour figures must be
re-derived; the figures here are anchored to the current registry
enumeration.

The headcount and tooling figures relate directly to the AdoptionPhase
model in [asdlc-guide.md](asdlc-guide.md). An organisation's AdoptionPhase
self-assessment is the single most important driver of the uplift figure;
an organisation that self-assesses at AdoptionPhase 3 but operates the
manual processes of AdoptionPhase 1 will under-budget by a significant
margin.

The FinOps governance obligations that govern the inference-budget
projections are defined in [finops-governance.md](finops-governance.md);
this annex projects the cost — that document governs the attribution and
control of the cost.
