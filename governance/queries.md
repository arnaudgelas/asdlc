# Governance Queries — ASDLC Cross-Cutting

_The canonical questions every governed system must be able to answer, and when
to ask them._

See [Governance Graph](graph.md) for the semantic model these
questions traverse. See [Agent Control Plane](../agent-control-plane.md) for the
agents that answer these questions continuously. See
[Waiver Governance](../waiver-governance.md) for waiver-specific queries.

---

## Section 1: Why Canonical Governance Questions Matter

A governance system that cannot answer basic questions about its own state is
not governing — it is filing documents. The ASDLC gates produce decisions, and
those decisions produce records. But a record filed in a gate decision document
answers only the question "was this condition satisfied at this point in time?"
It does not answer "is the condition still satisfied now?" or "which conditions
across all active systems are currently failing?" or "which incidents from last
quarter produced required evaluation updates that have not been completed?"
These are not edge-case queries. They are the minimum situational awareness a
governed organization must maintain continuously. Without them, governance is a
checkpoint system that operates at gate events and is blind between them.

These are the questions that a living governance system must answer without
convening a meeting. The Governance Graph makes the data linkages required to
answer them. This document defines the canonical set: the questions that every
ASDLC-governed organization must be able to answer, the data sources those
questions draw on, and the cadence at which each question should be asked. The
canonical set is not exhaustive — organizations will develop additional queries
as their governance maturity grows — but no ASDLC implementation is complete if
it cannot answer every question in this set on demand.

The questions are implementation-agnostic. An organization using a property
graph database expresses them as graph traversal queries. An organization using
a relational database expresses them as join queries. An organization using
structured markdown with a scripting layer expresses them as document
traversals. The question is the governance requirement; the expression is an
implementation choice. What cannot vary across implementations is the set of
questions that must be answerable, the data required to answer them, and the
cadence at which the answers must be current.

---

## Section 2: Gate Health Queries

Gate health queries assess the current state of gate conditions. They should be
answerable on demand, not only at scheduled gate events. A gate condition whose
current state is unknown between gate assessments is a governance visibility
gap: the organization has approved a condition as satisfied and has no way of
knowing whether it remains satisfied. The queries in this section close that
gap.

**Q-GH-1: What is the current GateState of every condition in the Specification
Readiness Gate for specification [X]?**

This question returns the full set of gate conditions for the named
specification, with the current GateState of each. Any condition whose state is
`fail`, `missing`, `stale`, `contradicted`, or `requires-human-decision` is
immediately visible, together with the evidence or the absence of evidence that
produced that state.

Data: GateDecision nodes for this specification, linked EvidenceArtifact nodes
with freshness status and content hashes, AcceptanceCriterion and Constraint
nodes that define the condition set. Cadence: on demand by any governance
participant. Triggers: any modification to the specification itself, to any
linked EvidenceArtifact, or to any AcceptanceCriterion or Constraint node within
the specification's scope.

**Q-GH-2: Which evidence artifacts supporting active gate conditions have
exceeded their freshness window?**

This question identifies every EvidenceArtifact whose freshness window has
elapsed, crossing the boundary from `pass` to `stale` since the last gate
assessment. The answer is the list of conditions whose GateState is currently
`stale` and that previously held a `pass` state — meaning the condition was once
satisfied and the question is now whether it still is.

Data: EvidenceArtifact nodes with freshness_window and last_modified timestamps,
linked to active GateDecision nodes. Cadence: continuous. The Runbook Drift
Agent or Evidence Bundle Agent monitors freshness windows and transitions
GateState values from `pass` to `stale` at the moment the window expires. An
agent that monitors this query continuously converts what would otherwise be an
invisible governance event into an immediate, actionable notification.

**Q-GH-3: Which release gate conditions are currently in `contradicted` state?**

Contradiction is not failure of a condition — it is inconsistency within the
governance record about a fact the condition depends on. The model version
recorded in the evaluation artefact differs from the model version in the
deployment configuration. The SBOM generated at build time names a library
version that does not match the version in the runtime manifest. These
discrepancies are invisible unless the governance record is structured to
surface them. This query makes contradiction visible.

Data: GateDecision nodes for active releases, specifically identifying cases
where two EvidenceArtifact nodes linked to the same condition carry conflicting
values. The model-version inconsistency between evaluation and deployment is the
canonical case; the same pattern applies to any versioned artefact that appears
in both the evidence record and the deployment configuration. Cadence:
continuous. Contradiction detection should be immediate: the moment a new
EvidenceArtifact introduces a value that conflicts with an existing one linked
to the same condition, the GateState transitions to `contradicted` and the
relevant governance participants are notified.

**Q-GH-4: Which waivers expire within the next 30 days (a policy-set lead time)?**

A waiver that expires without renewal or remediation causes the underlying
condition's GateState to revert immediately to its pre-waiver state. For a
system in production, that reversion is an operational DoD failure. The 30-day
window is the minimum lead time for waiver owners to either complete the
remediation plan or initiate a renewal. This query is the mechanism that makes
waiver expiry a planned event rather than an unnoticed administrative failure.

Data: GateDecision nodes in `waived` state, with linked waiver expiry dates.
Cadence: daily. Output includes the condition being waived, the waiver owner,
the expiry date, the current status of the remediation plan, and whether a
compensating control is still confirmed operational.

**Q-GH-5: Which conditions have been in `fail` state for more than [N] days
without a remediation record?**

A condition in `fail` state represents an active governance deficiency. A
condition in `fail` state for a policy-set 10 or more business days without a
remediation record linked in the governance graph represents a deficiency that
is not being actively addressed. This query surfaces dormant failures —
conditions that have entered `fail` state and have not prompted a documented
response.

Data: GateDecision nodes where GateState is `fail`, the timestamp of the last
state change, and the presence or absence of a linked remediation
EvidenceArtifact. Cadence: weekly. Any condition in `fail` state for more than
that policy-set 10 business days without a remediation record linked in the
governance graph warrants escalation to the accountable human. The escalation
is not discretionary — the governance graph records the escalation as required
when the threshold is crossed, and the accountable human's response (or absence
of response) is itself part of the governance record.

---

## Section 3: Release Readiness Queries

Release readiness queries determine whether a release candidate is ready for the
release gate assessment. They should be run by the Evidence Bundle Agent as part
of bundle assembly and reviewed by the release manager before the gate
assessment convenes. A release gate assessment that encounters unresolved
answers to these queries is not ready to close.

**Q-RR-1: What changed since the last approved release?**

This question establishes the material change set: every component of the
current release candidate that differs from the last approved release. Every
difference is a material change. Every material change must be covered by
corresponding evidence in the bundle. An evidence bundle that does not account
for every material change is an incomplete bundle, and the release gate cannot
close on an incomplete bundle.

Data: the last approved Deployment node, with linked Specification, Model,
Prompt, Tool, Dependency, and Build nodes — compared against the current release
candidate's corresponding linked nodes, using version identifiers and content
hashes. The answer is a diff across every governed artefact type, not a summary.
Each item in the diff is a material change that the bundle must address.

**Q-RR-2: Which evidence artifacts in the current bundle differ from those in
the last approved release?**

Where Q-RR-1 identifies what changed in the system, Q-RR-2 identifies what
changed in the evidence. New evidence artefacts, updated artefacts, and removed
artefacts each carry different governance implications. A new artefact covers a
new scope. An updated artefact supersedes a prior one and should be reviewed in
light of the prior artefact's findings. A removed artefact may indicate that a
previously covered condition is no longer in scope — which requires an explicit
gate decision rather than silent omission.

Data: EvidenceArtifact nodes linked to the current Release node compared against
EvidenceArtifact nodes linked to the last approved Release node, compared by
content hash. New, updated, and removed artefacts should be surfaced separately,
with the conditions they cover identified for each category.

**Q-RR-3: Which model, prompt, or tool versions differ between the verification
environment and the production deployment configuration?**

This is the contradiction check for the release gate. Evaluation evidence is
produced in a specific environment against specific artefact versions. If any of
those versions differ in the production deployment configuration, the evaluation
evidence does not describe the system that will be deployed. The condition whose
evidence depends on that evaluation is in `contradicted` state, and the release
gate cannot close in `contradicted` state without a governance decision.

Data: Model, Prompt, and Tool nodes linked to the EvidenceArtifact records
representing evaluation results, compared against the corresponding nodes linked
to the Deployment node representing the production configuration. Any version
identifier or content hash that differs between the two sides of the comparison
is a discrepancy. Any discrepancy puts the release into `contradicted` state for
the relevant condition.

**Q-RR-4: Which risks in the risk register have waivers expiring before the
planned deployment date?**

A waiver that expires before the deployment date means the waived condition will
be in `fail` state at the moment of deployment. Deploying a system with a
condition in `fail` state is a release gate failure regardless of when the
waiver was issued. This query identifies waivers whose timing makes them
inadequate to cover the release, not because they are invalid, but because their
validity window does not extend to the deployment date.

Data: Risk nodes with linked GateDecision nodes in `waived` state, with expiry
dates compared against the planned deployment date from the current release
record. Any waiver that expires before the deployment date requires renewal
before the release gate closes or completion of the remediation plan.

**Q-RR-5: Which dependencies in the current SBOM were flagged as agent-selected
with low OpenSSF Scorecard scores in any prior risk assessment?**

Agent-selected dependencies — dependencies introduced by an agent during
implementation without explicit human selection — represent a supply-chain
governance gap that does not disappear when the system passes a prior gate. A
dependency flagged in a prior risk assessment as agent-selected with a low
OpenSSF Scorecard score carries that provenance into the current release. The
release gate is the point at which that history is reviewed, not assumed
resolved.

Data: Dependency nodes with agent-selected provenance labels, linked Risk nodes
from prior risk assessments, and current OpenSSF Scorecard assessment results
where available. These dependencies require explicit human review and a
disposition decision in the release gate. A disposition decision is not the same
as approval — it is a formal acknowledgment of the dependency's provenance and
risk history, with a documented rationale for inclusion or exclusion.

**Q-RR-6: Which controls required by the DevSecOps control matrix for this
system's tier are absent from the evidence bundle?**

The DevSecOps control matrix defines mandatory controls by system tier. A
release for a Tier 2 system that does not include evidence of every mandatory
Tier 2 control is a release with a missing mandatory control — and a missing
mandatory control is a gate `fail`, not a minor omission. This query compares
the required control set against the evidence bundle before the gate assessment
convenes, so that gaps are identified during bundle assembly rather than
discovered during gate review.

Data: the mandatory controls defined in
[devsecops-controls.md](../devsecops-controls.md) for this system's tier, compared
against EvidenceArtifact nodes of type `control execution result` present in the
current evidence bundle. Each mandatory control that lacks a corresponding
EvidenceArtifact is a missing condition. Any missing mandatory control places
the release gate in `fail` state for that condition.

---

## Section 4: Operational Health Queries

Operational health queries assess the state of deployed systems after the
release gate closes. They should be answerable on demand and monitored
continuously for Tier 2 and above systems. A system that passes the release gate
and then operates without continuous governance visibility has crossed from
governed deployment into ungoverned operation. These queries maintain governance
visibility in production.

**Q-OH-1: Which operational DoD conditions are currently failing for system
[X]?**

The operational Definition of Done specifies the conditions a deployed system
must continuously satisfy. This query returns the current GateState of every
operational DoD condition for the named system, with any `fail`, `missing`, or
`stale` condition surfaced immediately to the steward. This is the primary
continuous governance query for systems in production: the steward's standing
view of whether the system is operating within its governed state.

Data: the Deployment node for the current production deployment, linked
operational DoD GateDecision nodes with their current GateState values from
continuous monitoring. Cadence: continuous. Any non-`pass` GateState is surfaced
immediately to the steward, who is accountable for initiating a remediation
response within the remediation SLO defined for that condition and tier.

**Q-OH-2: Which runbooks reference deployment IDs or model versions that are no
longer current?**

A runbook that describes how to respond to an incident is only as useful as its
accuracy. A runbook that references a model version that has since been
superseded, a deployment ID that no longer exists, or a rollback procedure that
targets an environment that has changed is not a runbook — it is a historical
document that will misguide an incident responder. This query identifies runbook
drift: the divergence between what the runbook describes and the current state
of the system it covers.

Data: Runbook nodes with linked Deployment and Model nodes, comparing the
versions documented in the runbook against the actual deployed versions in the
governance graph. Cadence: continuous, monitored by the Runbook Drift Agent. A
discrepancy sets the runbook's GateState to `stale` and notifies the steward,
who is accountable for updating the runbook or formally determining that the
discrepancy does not affect the runbook's operational validity.

**Q-OH-3: What is the current SLO error budget burn rate and projected time to
exhaustion for system [X]?**

The SLO error budget is the governance-recognized measure of a system's current
reliability headroom. A system burning its error budget faster than its SLO
window allows is trending toward an SLO breach. The projected time to exhaustion
— the point at which the error budget is fully consumed — is the governance
system's early warning of an operational condition that will force a governance
response. This query converts operational observability data into a
governance-visible signal.

Data: SLO configuration from the Deployment node, current error rate from
operational observability records linked to the Deployment. Cadence: continuous.
Output: current burn rate, projected time to error budget exhaustion, and the
GateState implication. A system burning its error budget at a rate that projects
exhaustion within the current SLO window triggers an immediate steward
notification. A system that has already exhausted its error budget is in `fail`
state for its reliability condition.

**Q-OH-4: Which systems have steward portfolio capacity violations?**

The steward accountability model requires that each steward maintain meaningful
oversight of the systems in their portfolio. Meaningful oversight is not
possible at unlimited scale. The tier-calibrated limits — five Tier 3 systems,
ten Tier 2 systems, or twenty Tier 1 systems per steward, all policy-set
defaults chosen by the authors rather than measured — represent the governance
framework's assessment of the maximum portfolio at which a steward can exercise
genuine accountability rather than nominal responsibility. A steward who
exceeds these limits has more systems than they can govern.

Data: HumanOwner nodes with steward role, linked Deployment nodes grouped by
tier. Steward portfolio counts are compared against the tier-calibrated limits.
Cadence: weekly. A violation is surfaced to the accountable human, who must
either reduce the steward's portfolio or formally approve a temporary exception
with a documented plan to return to compliance.

**Q-OH-5: Which incidents from the last 90 days (a policy-set window) required evaluation suite
updates that are still missing?**

Post-incident reviews produce required actions. When a review determines that an
incident revealed a gap in the evaluation suite — a failure mode the evaluation
did not detect, a model behavior the evaluation did not cover — a required
evaluation suite update is created. That update has a governance consequence:
until the evaluation suite is updated, the system's evaluation evidence does not
cover a known failure mode. This query tracks required evaluation suite updates
from post-incident reviews and identifies those that have not been completed.

Data: Incident nodes with linked post-incident review EvidenceArtifact nodes
that carry a required_evaluation_update flag, compared against current
Specification and evaluation suite EvidenceArtifact nodes to determine whether
the required update has been filed. Cadence: weekly. Missing required updates
are tracked as open remediation items, linked to the incident that produced
them, and remain open until a completed evaluation suite EvidenceArtifact is
filed that explicitly closes the gap identified in the post-incident review.

---

## Section 5: Cost and Value Queries

Cost and value queries assess the economic dimension of governed systems. The
ASDLC requires that systems deliver measurable value at a governable cost. A
system that cannot be assessed against this requirement is failing an
operational DoD condition, regardless of whether it is technically operational.
These queries make the economic governance state of every system continuously
visible.

**Q-CV-1: Which systems have costs exceeding their forecast by more than a policy-set 20%
over the last 30 days?**

The cost forecast filed in the specification is not an aspiration — it is a
governance commitment. A system whose actual costs exceed that forecast by more
than 20% over a rolling 30-day period has drifted from its governed economic
parameters. The 20% threshold is a policy-set FinOps governance warning level —
chosen, not measured, and it does not match the 25% and 50% variance figures
`finops-governance.md` states, which is a live inconsistency rather than a
scope distinction: above this threshold, the economics owner must be informed
and a review must be scheduled. The threshold is not a permission to run 19%
over forecast indefinitely; it is the boundary at which an informal management
response becomes a required governance response.

Data: CostRecord nodes for each Deployment, compared against the cost_forecast
linked to the Deployment's governing Specification. Cadence: continuous,
monitored by the FinOps Agent, which alerts at threshold breach. The economics
owner is the named governance participant who reviews the alert and determines
whether the overage reflects a legitimate forecast error, an optimization
opportunity, or a systemic economic governance failure.

**Q-CV-2: What is the cost per successful business outcome for system [X] over
the last measurement period?**

Cost per successful outcome is the primary economic governance metric for
agentic systems. Raw cost is not a governance signal in isolation: a system that
costs twice as much as forecast but delivers four times the business value is
economically well-governed. A system that costs exactly on forecast but delivers
no measurable value is economically failing. This query produces the ratio that
contextualizes cost within the value it purchases.

Data: CostRecord nodes for the Deployment over the measurement period, divided
by the count of successful outcome events from operational observability and
value realisation EvidenceArtifact nodes. Cadence: quarterly. If cost per
successful outcome is increasing faster than value per outcome — if the system
is becoming less economically efficient over time — the economics owner must
initiate a formal review. A system whose cost per outcome has increased for a
policy-set two consecutive quarters without a documented explanation and a
remediation plan is failing its economic governance condition.

**Q-CV-3: Which systems have not had a value realisation measurement in more
than 90 days?**

Value realisation measurement is an operational DoD requirement, not an
optional reporting exercise. A system operating for more than a policy-set 90
days without a value realisation measurement has no current evidence that it is
delivering the business value that justified its existence. The measurement
method and measurement owner are defined at the specification gate; the absence
of a recent measurement means the designated owner has not executed a required
governance obligation.

Data: DemandItem nodes with linked measurement_method and measurement_owner,
compared against the most recent EvidenceArtifact node of type `value
realisation measurement` linked to the current Deployment. Cadence: monthly.
Systems without a value realisation measurement within that policy-set past 90
days are in `missing` state for this operational DoD condition, and the
measurement owner is the named governance participant accountable for
remediation.

**Q-CV-4: Which optimization proposals from the FinOps Agent have been open for
more than 30 days without review by the budget owner?**

The FinOps Agent identifies cost optimization opportunities and files them as
EvidenceArtifacts awaiting budget owner review. An optimization proposal that
sits unreviewed for more than a policy-set 30 days is not a neutral
administrative delay — it has a calculable carrying cost: the ongoing cost of
the unoptimized configuration multiplied by the number of days since the
proposal was filed. This query surfaces unreviewed proposals and their
accumulated carrying cost, making the cost of non-action visible to governance
participants.

Data: EvidenceArtifact nodes of type `optimization proposal` from the FinOps
Agent, with creation timestamps and approval status from the budget owner.
Cadence: weekly. Unreviewed proposals exceeding the 30-day threshold are
surfaced to the budget owner and the accountable human. The proposal's
calculated carrying cost — the optimization value multiplied by elapsed days —
is included in the notification to make the economic consequence of non-action
explicit.

---

## Section 6: Security and Supply Chain Queries

Security and supply chain queries assess the integrity of the governed system's
components and the traceability of its construction. These are continuous
governance requirements, not periodic assessments. A vulnerability disclosed
today in a dependency the system uses today is a governance event today, not at
the next scheduled review.

**Q-SS-1: Which dependencies have known Critical or High vulnerabilities without
a filed VEX document or remediation record?**

A dependency with a known Critical or High vulnerability that has no VEX
document and no remediation record is an open security governance failure. The
VEX document is the mechanism by which the organization declares whether a known
vulnerability is exploitable in this system's specific configuration; without
it, the vulnerability's applicability is unknown. A remediation record is the
mechanism by which the organization confirms it is addressing the vulnerability;
without it, the vulnerability is known and unaddressed. Neither is acceptable
for Critical or High severity findings.

Data: Dependency nodes with CVE or vulnerability scan linkages, compared against
VEX EvidenceArtifact nodes and patch or remediation EvidenceArtifact nodes.
Cadence: continuous, triggered by new vulnerability disclosures. Any unaddressed
Critical vulnerability — no VEX document and no remediation record — triggers an
immediate steward notification. Any unaddressed High vulnerability without
disposition within the remediation SLO for this tier also triggers escalation.

**Q-SS-2: Which agents used during the last loop iteration were not in the
governance graph as governed agents?**

An agent that executes within the ASDLC loop and is not represented as a
governed Agent node in the governance graph is an ungoverned agent. It has no
specification, no evaluation suite, and no accountability record. Its outputs
cannot be attributed in the agentic provenance record with the same authority as
the outputs of governed agents. Any ungoverned agent that participated in a
governed loop is a governance gap — not an operational issue necessarily, but a
governance record failure that must be investigated and closed.

Data: the governed Agent nodes in the governance graph, compared against agent
identifiers recorded in the EvidenceArtifact (agentic provenance record) for the
most recent loop iteration. Any agent identifier in the provenance record that
does not correspond to a governed Agent node is an ungoverned agent. Cadence: at
the close of each loop iteration. The investigation must determine whether the
ungoverned agent's participation was an authorized exception that requires
retroactive governance documentation or an unauthorized use that requires a
governance incident record.

**Q-SS-3: Which model or prompt versions changed between the last two releases
without a corresponding evaluation suite run?**

Evaluation parity requires that every model or prompt version deployed has been
evaluated in a controlled environment before deployment. A change in model or
prompt version between releases that has no corresponding evaluation suite
EvidenceArtifact means the released version was not evaluated — or was evaluated
under a different version than what was released. Either case constitutes a
release governance failure for the model version consistency condition.

Data: EvidenceArtifact (agentic provenance record) nodes for the last two
Release nodes, comparing Model and Prompt version identifiers and content
hashes. Any Model or Prompt node whose version differs between the two releases
must have a corresponding evaluation EvidenceArtifact that confirms the new
version was evaluated. Any change without that corresponding artefact means
evaluation parity is unconfirmed — the model version consistency condition is in
`contradicted` state for that release.

**Q-SS-4: Which SLSA provenance attestations in the current release cannot be
verified against their declared source commits?**

A SLSA provenance attestation that cannot be verified is not an attestation — it
is an unverifiable claim. A release whose supply chain integrity relies on
unverifiable attestations has an unverified supply chain, regardless of how many
attestation documents are present in the evidence bundle. The existence of an
attestation document is not the governance condition; the verifiability of the
attestation against its declared source is.

Data: EvidenceArtifact (SLSA attestation) nodes linked to the current Release
node, with verification status from the Evidence Bundle Agent's attestation
check — specifically whether each attestation's declared source commit can be
confirmed as the actual build source. Any attestation whose verification fails
or cannot be completed puts the supply-chain integrity condition in `fail`
state. A `fail` state on supply-chain integrity is not a matter for a waiver; it
requires resolution before the release gate closes.

---

## Section 7: Query Ownership and Cadence

Each canonical governance query has a defined owner and a defined cadence.
Neither is optional. A query without an owner has no one accountable for
reviewing its output and acting on its findings. A query without a defined
cadence produces results that no one knows to expect. Both conditions convert
monitoring into theater: the data is collected, the question is answered, and
the answer produces no governance response.

Queries that run continuously — Q-GH-2, Q-GH-3, Q-OH-1, Q-OH-2, Q-OH-3, Q-CV-1,
Q-SS-1, Q-SS-2 — are owned by the governance agent whose continuous monitoring
scope covers the relevant data: the Runbook Drift Agent for runbook and
freshness queries, the Evidence Bundle Agent for artefact integrity and
attestation queries, the FinOps Agent for cost threshold queries. Continuous
queries produce alerts that are routed to the relevant governance participant —
the steward, the economics owner, or the accountable human — at the moment the
threshold is crossed. The routing is not discretionary: the governance graph
records the alert and the named recipient together.

Queries that run at gate events — Q-GH-1, Q-RR-1 through Q-RR-6, Q-SS-3, Q-SS-4
— are owned by the gate reviewer. The gate reviewer is responsible for
confirming that the query has been run, that its output has been reviewed, and
that any non-`pass` states are explicitly addressed in the gate decision record.
A gate that closes without running the applicable readiness queries has not
completed its review. The gate decision record must reference the query outputs,
not summarize them informally.

Queries that run weekly — Q-GH-5, Q-OH-4, Q-OH-5, Q-CV-4 — are owned by the
steward. Queries that run monthly or quarterly — Q-CV-2, Q-CV-3 — are owned by
the economics owner, with review by the product owner for the value realisation
dimension. The steward is accountable for weekly query review as a standing
responsibility of the role, not as an additional task. An organization that has
defined stewards as accountable for operational governance must provide stewards
with the tooling to run these queries without manual data assembly.

An organization that defines governance queries but assigns no owner to review
and act on the results has monitoring, not governance. The query is the
detection mechanism; human review and action is the governance mechanism.
Governance agents make detection continuous and efficient. They do not make it
sufficient. Sufficiency requires that every alert, every anomalous result, and
every threshold breach produces a documented human response from a named
governance participant — within the cadence that the governance framework
requires for that condition's tier and severity.
