# Annex — SAFe Implementation Mapping

> **Mapped against SAFe 6.0** (current as of last_verified date below). When
> SAFe revisions introduce role or artefact changes, this annex must be
> updated and re-verified.
>
> Last verified: 2026-05-07
> Next review due: 2026-11-07
> Owner: ASDLC Steward + SAFe LACE liaison

_A normative annex for organisations operating the Scaled Agile Framework
(SAFe). This annex maps ASDLC artefacts, roles, ceremonies, and cadences
onto SAFe's planning hierarchy. For organisations that do not operate SAFe,
this annex is advisory: the underlying ASDLC obligations apply regardless of
the scaling framework in use; this annex describes one specific way to
operationalise them._

See [asdlc.md](asdlc.md) for the framework-agnostic four-layer model and the
gate definitions that this annex maps onto SAFe constructs. See
[governance/gate-registry.yaml](governance/gate-registry.yaml) (and its
companion [governance/gate-registry.md](governance/gate-registry.md)) for
the canonical gate condition enumerations referenced below; the YAML file
is the machine-readable source of truth, the Markdown file is the prose
companion.

A SAFe 6.0 version-tracking entry for this annex is recorded in
[freshness-register.md](freshness-register.md); revisions to SAFe that
affect role or artefact mappings are tracked there.

---

## Scope

This annex is normative for organisations operating SAFe. It defines how the
ASDLC's four layers, three (initially) gates, role responsibilities, and
ceremony cadence map onto SAFe's Portfolio, Large Solution, and Essential
configurations. Where a SAFe organisation's local SAFe implementation
diverges from the standard SAFe taxonomy, the local taxonomy governs; this
annex assumes the standard role and ceremony names as published by Scaled
Agile, Inc.

For organisations that do not operate SAFe, the ASDLC obligations are framed
in framework-agnostic terms in `asdlc.md`. This annex is then advisory — a
worked example of one scaling integration. Other scaling frameworks (LeSS,
Disciplined Agile, Spotify-style models, custom enterprise scaling models)
require their own implementation annexes; the underlying obligations do not
change.

---

## Artefact mapping

The mapping below relates ASDLC artefacts to SAFe artefacts. The "what
changes" column states the substantive adjustment a SAFe organisation must
make when adopting ASDLC obligations on top of an existing SAFe practice.

| ASDLC artefact | SAFe artefact | What changes |
|----------------|---------------|--------------|
| DemandItem (`demand/value.md`) | Epic backed by a Lean Business Case | The Lean Business Case must include the Layer 1 SR-conditions evidence (validated need, measurable value, identified constraints, named accountable human, blast radius assessment, loop cost justification) before the Epic exits Funnel state. |
| Specification | Feature with PI Objective | The Feature's acceptance criteria are the SR-3 expressible criteria; the PI Objective carries the SR-2 measurable value statement; the Feature's Definition of Ready inherits the SR conditions enumerated in `governance/gate-registry.md`. |
| Loop iteration output | Story-level deliverable from the team's iteration | Engineering Definition of Done (manifesto) governs the Story closure; the Story is not "done" until the inner-loop DoD conditions are satisfied. |
| Evidence Bundle | System Demo evidence and System Team release readiness review record | The System Demo evidence is augmented by the machine-readable evidence bundle and control state record specified in `release-governance.md` Conditions 1 and 7. |
| Release object (release-governance.md) | ART Continuous Delivery Pipeline release | The ART CDP release artefact is gated by the eight Release Gate conditions in `governance/gate-registry.md`; CDP automation that bypasses any condition is non-conformant. |
| Accountable Human (P12 anchor) | Business Owner where accountability for outcome is held by the business; Product Manager where the accountability is for product outcome | The named individual is recorded by name, not by role title alone; SR-5 requires a person, not a delegation. |
| System Steward | System Owner | The System Owner role is the natural carrier; this annex names the System Owner as the default steward for ASDLC-governed systems within an ART. |
| Runbook (DoD-1) | Operational Documentation maintained by the System Team in concert with the System Owner | The runbook obligations in `operations/dod.md` extend SAFe's operational documentation expectations with agentic-specific content (reasoning trace access, agent control plane references, foundation model version pinning). |
| Waiver record (`waiver-governance.md`) | Risk ROAM record (Resolved, Owned, Accepted, Mitigated) at PI Planning, escalated to LPM where appropriate | The ROAM record carries the waiver's grantor, expiry date, and compensating control; an "Accepted" risk that lacks an expiry is non-conformant under RG-8. |
| Governance graph (governance/graph.md) | Agile Release Train metrics dashboard, augmented | The standard ART metrics are insufficient to answer ASDLC governance queries; the governance graph supplements them with provenance, evidence, and gate-state structure. |

---

## Roles in scope

The role-mapping prose in this annex blends standard SAFe 6.0 roles with
ASDLC-introduced roles. The two are separated explicitly below so that a
SAFe organisation can distinguish a role that already exists in its
operating model from a role that ASDLC adoption requires it to add.

### Standard SAFe roles in scope

The following are SAFe 6.0 roles, defined by Scaled Agile, Inc. ASDLC
integrates with them rather than redefining them. Citations refer to the
SAFe 6.0 documentation set (the public articles indexed at
`scaledagileframework.com`); a SAFe organisation's local taxonomy governs
where it diverges from the standard.

| Role | SAFe 6.0 reference | ASDLC integration |
|------|--------------------|-------------------|
| Epic Owner | SAFe 6.0, "Epic Owners" article | Owns the Lean Business Case carrying SR-1, SR-5, SR-8 evidence; accountable for the Epic's value-realisation review under L4 → L1 feedback. |
| Product Manager | SAFe 6.0, "Product Management" article | Owns Feature-level scope and SR-2, SR-7, SR-8 contributions; pairs with Product Owner on L2 → L1 validation failures. |
| Product Owner | SAFe 6.0, "Product Owner" article | Owns Story-level acceptance and SR-3 first draft; verifies inner-loop DoD before Story closure. |
| Release Train Engineer (RTE) | SAFe 6.0, "Release Train Engineer" article | Coordinates Release Gate decision at the ART; records gate state in the release object; verifies waiver currency at gate time (RG-8). |
| System Architect | SAFe 6.0, "System Architect/Engineering" article | Owns blast-radius assessment (SR-6), architectural runway (including Tier-4 envelope specifications), and runway investment for governance tooling. |
| Business Owner | SAFe 6.0, "Business Owners" article | Signs SR-5 nominations and RG-4 sign-offs at the value-stream level; accepts residual risk for Tier-4 envelopes. |
| System Team | SAFe 6.0, "System Team" article | Assembles evidence bundles, runs release-readiness review, owns DR/failover testing in concert with Shared Services SRE. |
| Solution Train Engineer (STE) | SAFe 6.0, "Solution Train Engineer" article | Coordinates the cross-ART Release Gate at Solution-Train scope; aggregates per-ART certifications into the Solution-level gate decision. |
| Lean Portfolio Management (LPM) executives | SAFe 6.0, "Lean Portfolio Management" article | Approves portfolio-level investment, Tier-3 SR-5 nominations, Tier-4 envelope authorisation, and L4 → L1 portfolio reviews. |
| LACE (Lean-Agile Center of Excellence) | SAFe 6.0, "LACE" article | Co-stewards governance practice itself where the practice is the artefact; partners with the ASDLC Steward on conformance attestation (see [conformance-profiles.md](conformance-profiles.md)). |

### ASDLC-added roles

The following roles are introduced by ASDLC and are not natively defined in
SAFe 6.0. For each, the table states the closest SAFe analogue (if any) and
the gap that justifies the addition. Organisations adopting ASDLC on top of
SAFe MUST staff these roles or assign their responsibilities explicitly to
existing roles; tacit assumption that someone owns the responsibility is
non-conformant.

| ASDLC role | Closest SAFe analogue | Gap that justifies the addition |
|------------|-----------------------|----------------------------------|
| System Steward | System Owner (where the local SAFe taxonomy uses one) | SAFe does not standardise a per-system steward role across configurations; ASDLC requires a named, persistent steward per system (DoD-4) regardless of whether the local SAFe model defines a System Owner. |
| Governance Portfolio Owner | LPM (collectively) | LPM owns investment decisions; it does not natively own the governance graph, the waiver portfolio, or cross-system foundation-model-drift response. ASDLC requires a single accountable governance portfolio owner so that these responsibilities are not diffused across LPM. |
| Specification Analyst | Business Analyst / Product Owner support | SAFe 6.0 does not standardise a specification-analyst role on the team; ASDLC's SR-9 context-thread assembly is a substantive activity that needs a named owner. The role MAY be played part-time by a Product Owner or Business Analyst, but the responsibility is named. |
| Accountable Human (per system) | Business Owner or Product Manager (depending on outcome type) | SAFe assigns accountability by role title; ASDLC SR-5 requires accountability by named person, not by role. The Accountable Human is a name recorded in the system's governance specification, not a role title alone. |
| Governance Tooling SRE | System Team / Shared Services SRE | The evidence-bundle pipeline, control-evaluation harness, and governance-graph store are runway components requiring SRE-grade operation; SAFe's System Team and Shared Services SRE patterns cover the work but not its specific governance scope. The role SHOULD be filled within the System Team or Shared Services rather than as a separate function. |
| Compliance Liaison | Shared Services (Compliance) | Shared Services is the SAFe pattern; ASDLC names the per-ART or per-value-stream compliance liaison so that RG-5, regulated-system trace retention (DoD-7), and waiver-grant attestation have a named counterparty. |

## Role ownership matrix

The matrix below states which SAFe role (standard or ASDLC-added) owns or
approves each ASDLC artefact at each layer. "Owns" means the role is
accountable for producing or maintaining the artefact; "approves" means the
role signs off on it as the gating decision-maker. Where multiple roles are
listed, the first is the primary owner; subsequent entries are approvers or
co-owners.

### Layer 1 — Demand & Value

| ASDLC artefact / activity | SAFe role(s) |
|----------------------------|--------------|
| DemandItem identification and pre-validation | Epic Owner (owns); Product Manager (approves at the Program backlog) |
| Lean Business Case authorship | Epic Owner (owns); LPM / Portfolio Stakeholders (approve) |
| SR-1 business need validation evidence | Epic Owner (owns); Business Owner (approves) |
| SR-2 measurable value criterion and owner | Product Manager (owns); Business Owner (approves) |
| SR-3 acceptance criteria first draft | Product Owner (owns the draft; the relevant domain expert authors it) |
| SR-4 constraints identification | System Architect with Compliance / Shared Services contribution (owns); Product Manager (approves) |
| SR-5 accountable human nomination | Business Owner (owns the nomination); LPM (approves at Tier 3) |
| SR-6 blast radius assessment | System Architect (owns); RTE (validates that ART has the capacity to govern at the assessed tier) |
| SR-7 out-of-scope statement | Product Manager (owns); Product Owner (validates against story-level scope) |
| SR-8 loop cost justification | Product Manager (owns); LPM (approves where loop cost crosses portfolio thresholds) |
| SR-9 context thread assembly and review | Specification analyst on the team (owns assembly); Product Owner (reviews) |
| Specification Readiness Gate decision | Product Owner with System Architect concurrence (joint approvers); Business Owner (final approver for Tier 3) |

### Layer 2 — Engineering Execution

| ASDLC artefact / activity | SAFe role(s) |
|----------------------------|--------------|
| Story-level execution under the manifesto inner loop | Team (owns); Product Owner (accepts) |
| Evidence bundle assembly | Team with the Evidence Bundle Agent (owns); System Team (validates structural completeness) |
| Engineering Definition of Done attestation | Team (attests); Product Owner (verifies before Story closure) |

### Layer 3 — Release & Deployment

| ASDLC artefact / activity | SAFe role(s) |
|----------------------------|--------------|
| Release object construction | Release Train Engineer with the System Team (joint owners) |
| RG-1 Evidence Bundle Complete | System Team (owns the verification); Release Train Engineer (approves) |
| RG-2 Independent Validation Passed | Independent validator outside the ART (owns); RTE (approves the validator's findings into the release record) |
| RG-3 Rollback Procedure Tested | System Team (owns); RTE (approves) |
| RG-4 Accountable Human Sign-Off | Business Owner where the accountability is for business outcome; Product Manager where the accountability is for product outcome (signs) |
| RG-5 Compliance Documentation Complete | Compliance / Shared Services (owns); Business Owner (approves) |
| RG-6 Dynamic Security Testing Passed | System Team with Shared Services security engineering (joint owners); RTE (approves) |
| RG-7 Control State Record Complete and Current | Evidence Bundle Agent operator (owns); RTE (verifies) |
| RG-8 Waiver Governance | Waiver grantors named in each waiver (own); RTE (verifies that no expired waivers are present at gate time) |

### Layer 4 — Operations & Maintenance

| ASDLC artefact / activity | SAFe role(s) |
|----------------------------|--------------|
| Runbook maintenance (DoD-1) | System Owner (owns); System Team (supports) |
| Operational observability (DoD-2) | System Team (owns the platform); System Owner (verifies coverage) |
| On-call assignment (DoD-3) | RTE coordinates; team-level on-call ownership |
| System Steward assignment (DoD-4) | System Owner is the default; LACE may co-steward where governance practice itself is the artefact |
| Security scan currency (DoD-5) | Shared Services security (owns); System Owner (approves the scan record) |
| License compliance (DoD-6) | Shared Services legal/compliance (owns); System Owner (verifies) |
| Trace retention policy (DoD-7) | System Owner (owns); Compliance / Shared Services (approves the retention period for regulated systems) |
| DR/failover testing (DoD-8) | System Team with Shared Services SRE (joint owners); System Owner (approves the test record) |
| Quarterly Operational DoD review | System Owner (owns); RTE (verifies cadence) |

### Solution-train layer (where applicable)

| ASDLC artefact / activity | SAFe role(s) |
|----------------------------|--------------|
| Cross-ART Tier 3 system release | Solution Train Engineer (owns coordination); RTEs of participating ARTs (joint approvers); the named Accountable Human at the Solution level (signs RG-4) |
| Cross-ART evidence bundle assembly | Solution Train's System Team (owns); STE (approves) |

### Portfolio layer

| ASDLC artefact / activity | SAFe role(s) |
|----------------------------|--------------|
| Tier 4 policy envelope authorisation | LPM (owns the investment decision); Business Owner of the affected value stream (signs SR-5 / RG-4 at the envelope level) |
| ASDLC conformance profile claim (see `conformance-profiles.md`) | LPM with LACE (joint owners); Accountable Executive (signs the attestation) |
| Portfolio-level waiver oversight | LPM with the Governance Portfolio Owner role (joint owners) |

---

## RACI matrix

The matrix below assigns Responsibility (**R**), Accountability (**A**),
Consultation (**C**), and Informing (**I**) for ASDLC governance activities
to SAFe and ASDLC-added roles. Each activity has exactly one **A**.
Consulted means bidirectional dialogue is required before the activity is
considered complete; Informed means the role is kept up-to-date on the
outcome but does not gate it. Empty cells indicate the role is not
applicable for the activity.

Role abbreviations: **LPM** Lean Portfolio Management; **RTE** Release
Train Engineer; **PdM** Product Management; **SArch** System Architect;
**STm** System Team; **BO** Business Owner; **Ops** Operations (SRE /
on-call); **SS** System Steward; **GPO** Governance Portfolio Owner;
**AH** Accountable Human; **SA** Specification Analyst; **CL** Compliance
Liaison.

| Activity | LPM | RTE | PdM | SArch | STm | BO | Ops | SS | GPO | AH | SA | CL |
|----------|-----|-----|-----|-------|-----|----|-----|-----|-----|----|----|-----|
| Demand validation (Tier 1) → SR Gate pass | I | C | R | C | | A | | | I | I | R | C |
| Specification refinement (PI Planning DoR satisfaction) | I | A | R | C | | C | | | | I | R | C |
| Engineering execution (the inner loop) | | I | C | C | R | I | | | | I | C | |
| Release Gate pass | I | A | C | C | R | C | C | I | I | C | | C |
| Operational Readiness Gate pass | I | C | I | C | R | C | R | A | I | C | | C |
| Operational stewardship (continuous DoD compliance) | I | I | I | C | R | I | R | A | C | I | | C |
| Retirement Gate pass | C | C | C | C | R | C | C | A | I | C | | C |
| Governance graph stewardship | I | C | I | C | C | | C | C | A | I | | C |
| Waiver portfolio review | A | C | C | C | I | C | I | C | R | C | | C |
| Foundation-model behavioural drift response (release-governance.md Cond 1 sub-clause) | I | R | C | C | R | C | C | C | A | C | | C |
| Drift-incident response (operations/governance.md "Model and Data Drift Detection") | I | C | C | C | R | I | R | A | C | C | | C |
| L4 → L1 feedback closure | A | I | R | I | I | C | I | C | R | C | | I |
| L4 → L2 feedback closure | I | A | C | C | R | I | R | C | I | I | | I |
| L3 → L2 feedback closure | I | A | C | C | R | I | C | I | I | I | | I |
| L2 → L1 feedback closure | I | C | R | I | C | C | | I | I | A | C | |

Notes:

- Where the Accountable role is shown as the same role as Responsible
  (e.g. RTE on the Release Gate pass row), the convention is that the role
  performs the work and carries the accountability simultaneously; this is
  permitted when no other role is better placed to be the single
  accountable party.
- The Accountable Human (AH) named under SR-5 is, in practice, a specific
  Business Owner or Product Manager; the AH column tracks the named
  individual's accountability where it differs from the role-level
  responsibility.
- Where Compliance Liaison (CL) is marked Consulted, the consultation MUST
  be evidenced (a recorded review, not an implicit cc-on-email) for
  regulated systems claiming the ASDLC-Regulated profile in
  [conformance-profiles.md](conformance-profiles.md).
- The drift-response rows distinguish the two drift loci: provider-side
  foundation-model behavioural drift (per
  [release-governance.md](release-governance.md) Condition 1 sub-clause)
  is typically a cross-system event accountable to the GPO, whereas
  per-system model and data drift (per
  [operations/governance.md](operations/governance.md) "Model and Data
  Drift Detection") is accountable to the System Steward.

---

## Ceremony cadence integration

### Specification Readiness Gate at PI Planning

The Specification Readiness Gate's natural ceremonial fit is at the
Definition of Ready check that precedes a Feature being committed in PI
Planning. Each Feature considered for inclusion in the PI must satisfy SR-1
through SR-9 before it is accepted into a team's PI commitment. A Feature
that has not passed the SR Gate is not eligible for commitment; it remains
in the Program backlog until the gate conditions are satisfied.

The integration is operationalised as follows:

- The Definition of Ready for Features in the Program backlog is augmented
  to include the SR conditions enumerated in `governance/gate-registry.md`.
- Pre-PI Planning preparation (Backlog Refinement, Architecture Runway
  preparation, Compliance review) explicitly tracks SR condition status per
  Feature.
- The first day of PI Planning includes a "Features Ready for Commitment"
  review at which the Product Manager confirms — by Feature, by SR
  condition — that the gate has been passed. Features with unsatisfied
  conditions are deferred.
- Features added to the PI mid-cycle through the standard scope-change
  mechanism must pass the SR Gate before commitment, not after.

### Release Gate at System Demo and ART release readiness review

The Release Gate's ceremonial integration is twofold. The System Demo
provides the substantive evidence-presentation moment where stakeholders see
the working system; the ART release readiness review (the System Team's
release-readiness assessment in the Continuous Delivery Pipeline) provides
the formal gate decision moment where the eight Release Gate conditions are
assessed against the evidence.

- The System Demo's evidence presentation must include the machine-readable
  evidence bundle reference and the control state record summary, not only
  the feature demonstration. A System Demo that demonstrates working
  software without the evidence bundle is a feature review, not a release
  readiness signal.
- The ART release readiness review is the formal Release Gate assessment.
  RG-1 through RG-8 are evaluated; the RTE records the gate decision in the
  release object. A "release readiness review" that does not produce a
  per-condition pass/fail/waived record on the eight Release Gate conditions
  is a status meeting, not a gate.
- Where the ART's release cadence is more frequent than the PI cadence, the
  Release Gate is assessed per release, not per PI; the PI provides the
  scope, the Release Gate provides the per-deployment authorisation.

### Operational DoD review at Inspect & Adapt

The Operational DoD's continuous obligation aligns with the Inspect & Adapt
event. The I&A is the natural moment to surface DoD-condition lapses across
the systems the ART operates: stewardship gaps, runbook staleness, scan
expiry, observability drift. Findings from the I&A's problem-solving
workshop that trace to DoD lapses must produce a backlog item with an owner
and a due date, not a retrospective note.

Specifically:

- The PI Predictability and Quality measures presented at the I&A include a
  per-system DoD-conformance summary derived from the governance graph
  (governance/graph.md).
- The problem-solving workshop's identified problems include DoD lapses as
  a standing input; teams may not deprioritise DoD-traced problems below
  feature-traced problems without an explicit System Owner sign-off.
- Corrective actions from the I&A that involve DoD remediation become PI
  backlog items (typically Enabler Stories) with named owners and dates.

### Feedback paths and I&A problem-solving items

The four ASDLC feedback paths defined in `asdlc.md` (L4 → L1, L4 → L2, L3 →
L2, L2 → L1) produce signals that must be converted into ART action. The I&A
is the consolidating moment for ART-level signals; LPM portfolio review is
the consolidating moment for portfolio-level signals.

- An L2 → L1 validation failure produces a problem-solving item assigned to
  the Product Manager and Product Owner pair within the SLOs in
  `asdlc.md`.
- An L3 → L2 release failure pattern produces an Enabler Story for the
  team's Govern phase, owned by the Engineering lead, surfaced at the
  earliest of the next I&A or 10 business days from pattern identification.
- An L4 → L2 maintenance signal produces a Story or Enabler in the next PI
  with a named owner; the System Owner is accountable for surfacing the
  signal to the Product Manager so it is prioritised.
- An L4 → L1 value realisation shortfall produces a portfolio-level review
  initiated by LPM within 30 calendar days; the Epic Owner whose Lean
  Business Case forecast the value is accountable for the review's
  evidence.

---

## LPM guardrail mapping

ASDLC obligations interact with Lean Portfolio Management at two specific
points: loop cost justification (SR-8) and blast radius assessment (SR-6).

### Loop cost justification and participatory budgeting

SR-8 requires that loop cost be justified before a specification enters
Layer 2. In a SAFe organisation operating Lean Portfolio Management with
participatory budgeting, the loop-cost justification provided at the Lean
Business Case stage is the input to the Epic-level investment decision. The
participatory-budgeting forum considers loop cost as an explicit line in the
Lean Business Case — alongside the Epic's expected value — when allocating
investment to the value streams that will execute the Epic.

The substantive obligation is that loop cost must be visible at the
investment decision point, not assumed to be small. SAFe's participatory
budgeting is the venue; SR-8 is the obligation.

### Blast radius and investment horizons

SR-6 (Blast Radius Assessed) maps onto LPM's investment horizon framework as
follows:

- BR1 systems sit within the Run-the-business horizon and are funded
  through value-stream operating budgets without portfolio-level approval
  per change.
- BR2 systems require value-stream-level investment approval; the Business
  Owner of the value stream signs the SR-5 nomination.
- BR3 systems require portfolio-level investment approval; LPM signs the
  SR-5 nomination.
- Tier 4 envelopes are portfolio-level investments regardless of the
  systems' individual blast radii because the envelope is itself the
  investment object; the envelope steward is named at LPM.

Guardrail tolerances at LPM (the level of variance an Epic may exhibit
before LPM intervention is required) must be stated per blast-radius tier;
a single guardrail tolerance applied across all tiers under-controls high-
blast-radius work and over-controls low-blast-radius work.

---

## Architectural runway integration

The pre-loop investment that ASDLC obligations require — evidence-bundle
infrastructure, governance-graph stores, control-evaluation pipelines,
gate-tooling — is architectural runway, not feature work. Treating this
investment as feature work produces feature backlogs that compete with
governance infrastructure; treating it as runway makes the System Architect
accountable for ensuring it exists before the teams need it.

Specifically:

- The evidence-bundle assembly pipeline, the control-evaluation harness,
  and the governance-graph store are runway components owned by the
  System Architect with the System Team's implementation support.
- The gate tooling for SR, Release, and Operational gates is runway; it is
  not built per-team and is not feature work for any single team.
- Tier 4 policy envelopes are part of the architectural runway. The
  envelope itself is an architectural commitment about the safety
  properties of an autonomous capability; it is not a feature delivered by
  a team. The runway must contain the envelope specification, the
  evaluation portfolio that validated the envelope, and the monitoring
  configuration before any Tier 4 operation begins.

The investment in runway is governed by LPM and is a standing line item in
the value stream's budget; it is not a discretionary "tech debt" allocation.

### Architectural runway for Tier-4 envelopes

Tier-4 policy envelopes — defined in [annex-aentm.md](annex-aentm.md) and
[annex-igm.md](annex-igm.md) — are part of the ART's architectural runway
investment, not feature work. Operationally:

- The **System Architect** owns the envelope specification: the safety
  properties the autonomous capability must hold, the evaluation portfolio
  that demonstrates the properties hold, and the monitoring configuration
  that detects envelope drift.
- The **Business Owner** accepts the envelope's residual risk on behalf
  of the value stream. The BO signature on the envelope authorisation is
  an SR-5 acceptance of accountability for the envelope's tolerated
  failure modes; it is not a procedural check.
- **PI Planning capacity for runway investment MUST explicitly include
  envelope review and re-gate cycles.** A PI plan that allocates feature
  capacity to teams whose systems sit inside a Tier-4 envelope without
  also reserving capacity for envelope review (the periodic cadence at
  which the envelope's evaluation portfolio is re-run, the monitoring
  thresholds re-validated, and any residual risk re-accepted) is
  under-funding the runway. Envelope re-gate cycles are scheduled at the
  cadence stated in the envelope's governance specification; PI capacity
  reserves time for them.

The adoption-cost implications of staffing and operating Tier-4 envelopes
within an ART are documented in
[annex-adoption-cost.md](annex-adoption-cost.md).

---

## Solution Train integration (multi-ART)

A Tier 3 system that spans multiple ARTs is governed at the Solution Train
level. The Release Gate for such a system has two compatible operating
modes; the Solution Train Engineer chooses the mode at the start of the PI
and records the choice in the system's governance specification.

### Single-train mode

One ART is designated the Releasing ART for the system. Its RTE is the
Release Gate decision authority. Other participating ARTs contribute
artefacts to the evidence bundle but do not separately gate. The Releasing
ART's Accountable Human signs RG-4 for the entire system. This mode is
appropriate when the system has a clear primary owner ART and the other
ARTs contribute auxiliary capability.

### Solution-train mode

The Solution Train Engineer is the Release Gate decision authority. Each
participating ART's RTE certifies, on a per-ART basis, that the ART's
contribution to the evidence bundle is complete and that the ART's
contribution satisfies its applicable SR conditions in the Layer 1 sense
and its applicable Release Gate conditions in the Layer 3 sense. The STE
aggregates the per-ART certifications into a single Solution-level Release
Gate decision; the Accountable Human at the Solution level signs RG-4.

This mode is appropriate for systems where the ARTs contribute substantially
co-equal capability and no single ART is the primary owner. It is more
governance-intensive than single-train mode; the choice should reflect the
genuine architecture of the system, not merely a preference for whichever
mode is administratively easier.

A Tier 3 cross-ART system that has not chosen a mode at the start of the PI
is not governable: the gate decision authority is unclear at the moment a
gate decision is required.

### Cross-ART Release Gate coordination

Whichever mode is chosen, four operational obligations apply to a Tier-3
multi-ART release.

- **Solution Train Engineer's coordination role.** The STE owns the
  coordination of the Release Gate across participating ARTs. In
  single-train mode this means ensuring auxiliary ARTs deliver their
  evidence contributions on the Releasing ART's gate timeline; in
  solution-train mode this means convening the gate decision itself,
  collecting per-ART certifications, and recording the aggregate decision
  in the Solution-level release object. The STE MUST NOT delegate the
  aggregate decision to any one participating RTE.
- **Single accountable human for cross-ART releases.** Exactly one
  Accountable Human signs RG-4 for a cross-ART release: in single-train
  mode this is the Releasing ART's Business Owner (or its Product Manager
  where the accountability is for product outcome); in solution-train mode
  this is the Solution-level Accountable Human named in the system's
  governance specification (typically one Business Owner or, where the
  release is itself a programme-coordination event, the Solution Train
  Engineer). Multiple co-signatures are non-conformant under SR-5: ASDLC
  requires a single named accountable person per release.
- **Evidence bundle assembly across ARTs.** The Solution Train's System
  Team assembles the cross-ART evidence bundle from the per-ART evidence
  sources. Each participating ART delivers its evidence in the structural
  schema referenced in [release-governance.md](release-governance.md);
  the aggregate bundle MUST be a single, integrity-checked object whose
  provenance edges trace back to each contributing ART's source bundle.
  Two separate bundles handed to the gate decision-maker are not an
  aggregate bundle.
- **Rollback coordination across services.** The cross-ART rollback
  procedure MUST cover service-level rollback in dependency order, not
  only per-ART rollback. The STE coordinates the rollback rehearsal
  required for RG-3 across services; a rollback procedure that has been
  tested per-ART but never tested as an integrated cross-ART rehearsal is
  insufficient evidence for RG-3 on a cross-ART release.

---

## WSJF integration

SAFe prioritises work using Weighted Shortest Job First (WSJF), in which the
numerator is Cost of Delay (composed of User-Business Value, Time Criticality,
and Risk Reduction / Opportunity Enablement) and the denominator is Job Size.

ASDLC's value × urgency × risk × strategic-alignment composition maps onto
the WSJF Cost-of-Delay components as follows:

- **Value** maps onto User-Business Value.
- **Urgency** maps onto Time Criticality.
- **Risk** maps onto Risk Reduction / Opportunity Enablement, plus a
  blast-radius weighting term that WSJF does not contain in its standard
  form. The blast-radius term is multiplicative: a high-blast-radius item
  is not merely a higher-risk item; it is an item whose Cost of Delay is
  amplified by the consequences of failure.
- **Strategic alignment** is implicit in WSJF (high-strategic-alignment
  items typically score higher on User-Business Value and Risk Reduction);
  ASDLC asks for it explicitly.

A SAFe organisation adopting ASDLC obligations should extend its WSJF
formula with an explicit blast-radius weighting on the Cost-of-Delay
numerator. The form below is illustrative; the weights must be calibrated
to the organisation's risk appetite.

```
WSJF_ASDLC = (UBV + TC + RROE) * blast_radius_multiplier / Job_Size

where blast_radius_multiplier = {
    BR1: 1.0,
    BR2: 1.3,
    BR3: 1.7
}
```

### Worked example (illustrative)

Two Features compete for inclusion in the next PI. Each is a candidate
specification at the SR Gate.

Feature A — a customer-facing pricing rule update:

- UBV = 8, TC = 5, RROE = 5 — Cost of Delay raw = 18.
- BR3 (a pricing error directly affects external customers and creates
  regulatory exposure). Blast-radius multiplier = 1.7.
- Job Size = 5.
- WSJF_ASDLC = 18 * 1.7 / 5 = 6.12.

Feature B — an internal reporting enhancement:

- UBV = 6, TC = 6, RROE = 5 — Cost of Delay raw = 17.
- BR1 (an internal reporting error has limited blast radius). Blast-radius
  multiplier = 1.0.
- Job Size = 3.
- WSJF_ASDLC = 17 * 1.0 / 3 = 5.67.

Without the blast-radius weighting, Feature B would have outranked Feature A
(17 / 3 = 5.67 vs 18 / 5 = 3.6). With the weighting, Feature A is correctly
prioritised because its Cost of Delay reflects the consequence of being late
on a high-blast-radius change. The figures here are illustrative; an
organisation calibrating the multiplier should run a back-test against
historical Features whose actual blast-radius outcomes are known.

---

## Relationship to other ASDLC documents

This annex is a normative implementation mapping for SAFe organisations and
an advisory worked example for organisations operating other scaling
frameworks. It does not modify the underlying ASDLC obligations; it states
how those obligations are operationalised in a SAFe context.

The authoritative gate definitions live in [asdlc.md](asdlc.md),
[specification-readiness.md](specification-readiness.md),
[release-governance.md](release-governance.md), and
[operations/dod.md](operations/dod.md). The canonical, machine-readable
condition enumeration lives in
[governance/gate-registry.yaml](governance/gate-registry.yaml) (with
[governance/gate-registry.md](governance/gate-registry.md) as the prose
companion).

RTEs operating the Release Gate MUST be familiar with the strict
"organisationally separate" definition for RG-2 independent validation in
[release-governance.md](release-governance.md); a validator who reports
into the same delivery line as the team being validated does not satisfy
the condition. Drift detection — both per-system model/data drift and the
provider-side foundation-model behavioural drift sub-clause referenced in
the RACI matrix above — is specified in
[operations/governance.md](operations/governance.md).

The adoption-cost implications of operating ASDLC at SAFe scale (including
the staffing implications of the ASDLC-added roles enumerated above and
the runway investment for Tier-4 envelopes) are documented in
[annex-adoption-cost.md](annex-adoption-cost.md). The conformance profile
that SAFe organisations typically claim — usually ASDLC-Regulated,
sometimes ASDLC-Tier4 for portfolio-level autonomous systems — is defined
in [conformance-profiles.md](conformance-profiles.md).

Version-tracking for this annex against future SAFe releases is recorded
in [freshness-register.md](freshness-register.md).
