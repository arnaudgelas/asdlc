# Governance Graph — ASDLC Cross-Cutting

_The semantic model linking intent, evidence, risk, cost, and accountability
across the lifecycle._

See [Governance Agents](agents.md) for the governance agent
framework. See [Agent Control Plane](../agent-control-plane.md) for named
governance agents and their schemas. See
[Governance Queries](queries.md) for the canonical governance
questions this model answers. See [Waiver Governance](../waiver-governance.md) for
the waiver node lifecycle.

---

## From Documents to Inspectable Governance State

The ASDLC currently governs through documents that pass gates. Specifications
are reviewed at the specification readiness gate. Evidence bundles are assessed
at the release gate. Operational Definitions of Done are reviewed quarterly.
This structure works. It produces governance checkpoints where the state of a
system is formally examined against defined conditions. What it does not produce
is continuous governance visibility. Between gate events, governance state is
implicit — held in documents that may or may not be current, in people's
understanding of a system that evolves in production, and in tooling that is not
linked to the governance record. A question asked mid-loop — which acceptance
criteria are currently evidenced? which threats have no mitigating control?
which costs have exceeded their forecast? — cannot be answered from the
governance record without a new, informal investigation.

The governance graph makes governance state continuously inspectable. It is not
a replacement for documents. Documents remain the primary human-readable record
of what was decided and why. The governance graph is a semantic model — a
definition of how every governance artefact relates to every other, and what the
relationship between them means. An organisation that instantiates this model in
any appropriate technology gains the ability to answer governance questions at
any moment, not only at gate events. Which conditions are currently satisfied?
Which evidence has become stale since the last gate passed? Which risks have
controls that have not been tested within their required window? Which
accountable humans are named to which decisions? These questions are answerable
from the graph without convening a gate assessment, because the graph's
structure records the state continuously.

The governance graph is a conceptual model first. The ASDLC defines the node
types, the edge types, and the semantic relationships between them.
Organisations implement this model in whatever technology fits their context: a
property graph database, an RDF triple store, a relational database with
foreign-key relationships that enforce referential integrity across governance
artefacts, a JSON-LD document store, or a structured set of linked documents.
The ASDLC does not mandate an implementation. It mandates that every governance
artefact be addressable by a stable identifier, a cryptographic hash of its
content at the time of filing, a named owner, a timestamp, and the agent or tool
that produced it. How organisations achieve this traceability is an
implementation choice. That traceability must exist is a governance requirement.

---

## Active Governance Signals

The governance graph must not only answer queries — it must push signals when
governance state changes without human-initiated queries. A governance system
that only responds to questions produces governance that is only as current as
the last person who asked. The graph's continuous state model makes proactive
signalling possible: when state changes, the graph knows, and it must act on
that knowledge. Four categories of push events are mandatory.

**Staleness push.** When any EvidenceArtifact transitions from pass to stale due
to event-triggered freshness rules, the governed system's steward and the
relevant gate condition owner are notified within 1 hour. The notification must
include: which condition transitioned to stale, which artefact is stale, which
triggering event caused the transition (a deployment change, a model version
update, a dependency vulnerability, or a freshness window expiry), and the path
to resolution — either regenerate the artefact, or assess whether the triggering
event materially changes the substance of the prior evidence. A staleness
transition is not an automatic failure; it is a signal that the prior evidence's
currency is no longer verifiable without human assessment.

**Waiver expiry push.** At 14 days, 7 days, and 24 hours before any waiver
expires, the governance graph must push a notification to the waiver grantor and
the system steward. An expired waiver with no confirmed remediation is a
governance incident: the condition the waiver covered is now neither pass nor
waived, and the gate it protected is no longer valid. Waiver expiry push
notifications must include: which condition is waived, what the original
justification was, whether remediation has been initiated or confirmed, and the
consequence if the waiver lapses without resolution.

**Accountability gap push.** When a HumanOwner node's availability status
changes to unavailable, or when a HumanOwner's assignment to a governance node
expires without a named successor, the governance graph must push a notification
to the governance portfolio owner within 1 hour. An unowned system is an
immediate governance concern: the approved_by and owned_by edges that provide
accountability anchors are pointing to a human who cannot be reached or who no
longer holds the role. No gate can be passed on a system with an unresolved
accountability gap.

**Cross-system behavioural dependency push.** When a Deployment or Model node
changes in System A, the governance graph must query all systems that have a
depends_on or behavioral_dependency edge to System A and push a staleness review
notification to their stewards. This is the mechanism for propagating governance
impact across system boundaries: a model version change in a shared inference
service, a dependency update in a shared component, or a configuration change in
an upstream system may silently invalidate governance assumptions in downstream
systems. The cross-system dependency push makes that propagation visible before
a gate assessment discovers it.

Each push event is itself an EvidenceArtifact filed to the governance graph with
a generated_by edge to the governance graph infrastructure agent that produced
it. Push events that are not acknowledged within defined SLOs escalate to the
governance portfolio owner. The SLOs are: staleness push, 48 hours; waiver
expiry push, per the waiver's remaining lifecycle; accountability gap push, 24
hours; cross-system dependency push, 72 hours. Escalation is automatic and is
itself a push event filed to the graph.

---

## GateState

GateState is the most operationally significant concept in the governance graph.
A GateState node represents the live assessment status of a single gate
condition at a specific point in time. It is not a property of the gate — it is
a time-stamped record of the condition's status as the graph last computed or
received it, together with the evidence that produced that status. GateState
nodes are the mechanism by which the governance graph provides continuous
governance visibility: rather than recalculating every condition at gate time
from scratch, the graph maintains the current GateState for every condition and
updates it when evidence changes, when time thresholds are crossed, or when a
new assessment is filed.

A gate condition does not have a binary state. The binary model — pass or fail —
obscures meaningful distinctions that determine what action is required and who
must take it. The governance graph defines seven GateState values.

**pass** means the condition is satisfied by current, non-stale evidence. The
evidence artefact exists in the graph, its freshness window has not expired, and
no contradiction with other evidence has been detected. A pass state is not
permanent — it transitions to stale when the freshness window expires, and it
transitions to contradicted if a subsequent artefact introduces a conflict.

**fail** means the condition is actively not met. A required element is present
but incorrect. A threat model that was submitted and formally reviewed does not
satisfy the condition if it omits the required threat categories — it fails,
because the evidence is present and verified to be insufficient. The distinction
from missing is important: a failed condition requires understanding what the
specific deficiency is and correcting it; it cannot be resolved simply by
submitting evidence.

**missing** means no evidence or artefact for this condition has been submitted.
Nothing has been attempted. A missing condition is not the same as a failed
condition. A missing threat model can frequently be accelerated to a reviewable
draft by a governance agent; a failed threat model requires a human to
understand the specific gap and correct it.

**stale** means evidence was submitted and previously supported a pass state,
but the evidence has since exceeded its defined freshness window. The condition
was satisfied at a prior point; it is no longer verifiable as satisfied because
the evidence may not reflect the current state of the system. Stale is not fail.
A stale threat model was once reviewed and found correct; what has changed is
that time — or system changes — has made its current accuracy unverifiable. A
governance agent can determine when the evidence became stale and what system
changes occurred in the intervening period, which gives a human reviewer the
context to assess whether the substance of the prior evidence likely still holds
or requires full re-review.

**contradicted** means two pieces of evidence for this condition conflict. The
model version recorded in the evaluation artefact differs from the model version
recorded in the deployment configuration. The SBOM generated at build time names
a dependency version that does not match the version in the runtime manifest. A
contradicted condition cannot be assessed as pass without resolving the
conflict, because the governance record contains an internal inconsistency about
a fact that matters. Contradiction surfaces conflicts that would otherwise be
invisible: two documents disagree about a fact, and neither document is wrong in
isolation — they reflect different moments or different perspectives on the
system's state. The graph structure makes the conflict observable rather than
hidden in separately filed documents.

**waived** means the condition has been formally waived with accountable human
sign-off, a documented justification, and a recorded expiry date. A waiver
without an expiry date is not a valid waiver in the governance graph. Waivers
that do not expire are not waivers — they are permanent exclusions that have
bypassed the governance process. The expiry date is the mechanism by which a
waived condition returns to governance scrutiny at a defined future point. See
[Waiver Governance](../waiver-governance.md) for the waiver node lifecycle.

**requires-human-decision** means the condition cannot be assessed by an agent.
It requires human judgment that no automated check can substitute. The question
of whether a risk is acceptable at the level of residual exposure it carries
after control implementation is a human judgment. The question of whether the
business intent documented in the specification genuinely validates the demand
is a human judgment. The question of whether evidence assembled under novel
circumstances is sufficient is a human judgment. The governance graph records
these conditions as requiring-human-decision so that governance workers can
locate them without scanning every condition in the system.

These seven states exist because governance actions diverge sharply at the
boundary between them. Agents can frequently resolve missing and stale
conditions to the point of a human-reviewable draft: a missing threat model can
be accelerated to a draft that a security function can review; a stale SBOM can
be regenerated from the current source and submitted for re-verification. Agents
cannot resolve fail, contradicted, or requires-human-decision conditions without
human involvement. A failed condition requires a human to identify and correct a
specific substantive deficiency. A contradicted condition requires a human to
determine which of the conflicting records is authoritative and resolve the
inconsistency. A requires-human-decision condition requires a human to exercise
judgment. These are not gaps in the governance agent model — they are the
boundary that defines where agent assistance ends and human governance begins.

### Canonical Enum Authority

This document defines the canonical GateState enum. The seven values — pass,
fail, missing, stale, contradicted, waived, and requires-human-decision — are
the complete and exhaustive set. Every other ASDLC document must use exactly
these seven values when describing GateState; no document may introduce an
eighth value, rename one of the seven, or vary their semantics.

Compound conditions that combine GateState with other graph data (for example,
"waived with a waiver whose expiry is still in the future", or "stale and
deferred to a later gate") must be expressed as derived predicates over the
canonical state and the relevant graph attributes — for example,
`GateState = waived AND waiver.expiry > t`, or
`GateState = stale AND deferral.target_gate IS NOT NULL`. Such compound
conditions must not be introduced as new GateState values. A predicate over the
graph is the correct construct; an enum extension is not.

Pre-gate workflow statuses — for example, draft, in-review, ready-for-gate, or
returned-for-rework — are not GateStates. They describe the lifecycle of an
artefact before a gate condition has been formally assessed and live outside
this enum. A document that conflates a workflow status with a GateState
violates this authority.

A document that introduces a new GateState value, that omits a canonical value
without a documented migration path, or that varies the semantics of a
canonical value violates this authority. Such a document must either land a
major-version registry update first (see § 2.2) or replace the proposed
extension with a derived predicate over the canonical state.

**Note — Control State Record and GateState are distinct.** The control state
record is a concrete artefact — an EvidenceArtifact node in the governance graph
— produced by the engineering loop at completion. It contains the structured
verdict (pass, fail, waived, stale, or requires-human-decision) for every
required control evaluated during that loop iteration, the artefact identifier
supporting each verdict, and waiver metadata where applicable. It is generated
once per loop iteration, handed to the release gate as a required input
alongside the evidence bundle, and retained as part of the release artefact. It
is a snapshot: it captures the state of each condition at the moment the loop
concluded, under a specific evidence set, at a specific point in time.

GateState, by contrast, is a derived property — the current assessment of a gate
condition based on querying the governance graph at a point in time. GateState
is not stored as a fixed value on a node; it is computed from the graph's
current structure: the evidence artefacts present, their freshness windows, the
waiver records and their expiry dates, and the contradiction detection logic.
Because GateState is derived rather than stored, it changes continuously as
conditions change. An artefact can expire, a contradiction can be detected
between two independently filed records, a waiver can lapse when its expiry date
passes — and in each case the GateState of the affected condition transitions
without any human action on the condition itself. The control state record does
not change; the GateState computed from the graph does.

The relationship between the two is precise. The control state record from the
most recent completed loop iteration is the primary input used to initialise the
GateState of each condition at the start of the release gate assessment. The
release gate begins from the verdicts recorded in the control state record, then
immediately applies freshness checks and contradiction detection to the evidence
artefacts those verdicts reference. From that point, GateState continues to
evolve throughout the gate assessment window — an artefact filed as pass in the
control state record may transition to stale if its freshness window expires
before the gate assessment completes, without the control state record itself
being modified. This distinction matters operationally: when a release gate
assessment surfaces a stale condition, the appropriate investigation is whether
the underlying evidence is still current, not whether the control state record
is incorrect. The control state record was accurate when produced; the live
GateState reflects what has changed since.

---

## Node Types

### DemandItem

A DemandItem represents a validated business need that has entered the demand
backlog and is a candidate for a loop specification. It is the upstream anchor
of the governance graph — the point from which intent, specification, and
ultimately delivery can be traced. A DemandItem carries a stable identifier, a
reference to the business demand sponsor (HumanOwner), the date it entered the
backlog, and a current status drawn from: active, superseded, abandoned, or
completed. DemandItems connect to the Specification nodes that implement them
through the validates edge, to the HumanOwner who sponsors the demand, and to
the CostRecords that accumulate costs in service of that demand across loop
iterations.

### Specification

A Specification is the versioned, gate-approved statement of what a loop will
build and how success will be measured. It is the primary input to engineering
execution and the anchor from which the rest of the loop's governance artefacts
derive their purpose. A Specification carries a version identifier, a content
hash that fixes its state at gate approval, a reference to the specification
analyst (HumanOwner), a reference to the gate decision record that approved it,
and the phase and tier that determined the evidence and oversight requirements
for the loop. Specifications connect to the DemandItem that validates the
business need, to the AcceptanceCriterion and Constraint nodes that make the
specification executable, to the Risks the system must address, to the
GateDecision that approved it, and to EvidenceArtifacts that verify its
conditions are met.

### AcceptanceCriterion

An AcceptanceCriterion is a single, testable condition that the loop output must
satisfy. Each criterion is the smallest unit of verifiable intent: it can be
evaluated independently, it has a clear pass state, and evidence can be filed
against it. An AcceptanceCriterion carries a stable identifier, the expression
of the criterion itself, a measurability confirmation that the criterion can be
evaluated with existing infrastructure, and a reference to the evaluation method
used to verify it. AcceptanceCriteria are owned by their Specification and
verified by EvidenceArtifacts. A criterion without a corresponding
EvidenceArtifact in the evidence bundle is in a missing GateState.

### Constraint

A Constraint is a non-negotiable boundary on the solution space. Constraints
arise from security requirements, privacy obligations, compliance mandates,
accessibility standards, architecture decisions, or cost ceilings. The defining
characteristic of a constraint is that it is not negotiable within the scope of
the loop — violating a constraint is a governance failure, not a product
trade-off. A Constraint carries a stable identifier, a category classification
(security, privacy, compliance, accessibility, cost, or other), the source of
the constraint (a regulatory citation, an architecture decision record
reference, or a business policy reference), and a status (active, waived, or
expired). Constraints connect to the Specification they restrict, to the Risks
that a constraint violation would trigger, and to the Controls that mitigate the
risk of that violation.

### Risk

A Risk is a named threat or failure mode with a documented likelihood and impact
assessment. A Risk node is not a general concern — it is a specific, named
scenario with an assessed severity and a documented status. A Risk carries a
stable identifier, a category drawn from: security, privacy, safety, compliance,
financial, operational, model/agent, or supply-chain, a reference to the source
threat model that identified it, a residual risk level assessed after control
application, and an acceptance status drawn from: mitigated, accepted, or
blocking. Risks connect to the Constraints whose violation they represent, to
the Controls that mitigate them, to the Incidents that have confirmed them or
revealed new instances, and to the GateDecisions where residual risk acceptance
was recorded.

### Control

A Control is a specific measure that reduces the likelihood or impact of a named
Risk. A Control is not a general security posture — it is a specific,
implemented measure with verifiable evidence of effectiveness. A Control carries
a stable identifier, a control type classification (preventive, detective, or
corrective), a reference to the evidence that demonstrates its implementation, a
defined test frequency, and the date of its last test. Controls connect to the
Risks they mitigate through the mitigates edge and to the EvidenceArtifacts that
prove their implementation and continued effectiveness.

### EvidenceArtifact

An EvidenceArtifact is any artefact filed into the governance record as proof
that a condition is met or a fact is established. EvidenceArtifacts are the
primary content of evidence bundles and gate decision records. A well-formed
EvidenceArtifact carries a stable identifier, a cryptographic hash of its
content at the time of filing, a timestamp, the epistemic tier of the artefact
(human-authored, tool-generated, agent-proposed with human review, or
agent-generated), the identifier of the producing agent or tool, the identifier
of the human reviewer if the tier is agent-proposed with human review, and a
defined freshness window with the current freshness status derived from that
window. EvidenceArtifacts connect to the Specifications, Releases,
GateDecisions, Controls, and Incidents that they evidence, and their freshness
status drives the GateState of the conditions they verify.

EvidenceArtifacts that are produced by agents or tools must also carry tool
provenance fields that make the production process inspectable. These fields
are:

**tool_invocations:** a list of tool invocations made during the production of
this artefact. Each invocation record carries: the tool identifier, the tool
version, the invocation timestamp, a hash of the input parameters (not plaintext
if the parameters include sensitive data), and the data access classification of
the data accessed through the invocation. The list is ordered by invocation
timestamp, making the production sequence reconstructable.

**external_data_sources:** any external systems queried during artefact
production, including regulatory databases, vulnerability databases, and
dependency registries. Each source record carries: the source identifier, the
source version or access timestamp, and the data classification of the returned
data. An EvidenceArtifact that incorporates external data without a
corresponding external_data_sources record is incomplete.

**tool_authorization_basis:** a reference to the ToolAuthorizationRecord that
permitted these invocations — the entry in the phase-tier tool authorisation
matrix that authorised this agent to use these tools in this context. This
reference is the chain that connects tool usage back to an explicit
authorisation decision: it is not sufficient to record that a tool was invoked;
the governance record must show that the invocation was authorised.

Tool provenance is part of the epistemic tier determination. An artefact
produced entirely from deterministic tool outputs with fully documented tool
invocations is more reliably tool-generated than one where the tool invocations
are absent or partial. A human reviewer assessing an EvidenceArtifact can
traverse the tool_invocations list to verify that the artefact was produced
correctly and that the tools invoked were authorised for the agent's phase and
tier.

### Agent

An Agent node represents a governed AI agent with a defined specification, an
evaluation suite, and a named accountable human. In the governance graph, Agent
nodes are not engineering agents in the abstract — they are specific, versioned,
governed agent instances that have passed the ASDLC's own agent governance
requirements before being deployed. An Agent node carries the agent identifier,
the current version, the autonomy tier under which it operates, a reference to
its accountable human (HumanOwner), a reference to its evaluation suite
(EvidenceArtifact), and the current kill-switch status. Agents connect to the
EvidenceArtifacts they generate through the generated_by edge, to the Tools
available to them, and to the Models they use.

### Model

A Model node represents a foundation model or fine-tuned model used by an Agent.
The Model node records the provenance and deployment context of the model so
that governance questions about which model version was in use when a given
EvidenceArtifact was generated can be answered from the graph. A Model node
carries the model identifier, the version, a provider category (whether the
model is accessed via API, run on-premises, or a fine-tuned derivative), the
deployment mode, and a confirmation of evaluation parity with the version under
which the evaluation suite was run. Models connect to the Agents that use them,
to the Prompts paired with them, and to the EvidenceArtifacts that record their
provenance as part of the agentic traceability record.

### Prompt

A Prompt node represents a versioned system instruction or prompt template.
Prompts are governance artefacts because they determine agent behaviour — a
change to a system prompt changes what the agent does, and that change must be
traceable in the governance graph. A Prompt node carries the content hash of the
prompt (not the plaintext, to avoid exposing sensitive operational logic in the
governance record), the version, the timestamp of the last modification, and the
owner. Prompts connect to the Agents they configure and to the Models with which
they are paired.

### Tool

A Tool node represents a capability available to an agent: an external API, a
code execution environment, a file system interface, a database query interface,
or a retrieval system. Tool nodes define the permission surface of an agent —
the set of capabilities the agent can invoke — and are therefore central to
blast radius assessment. A Tool node carries the tool identifier, the permission
scope (what the tool is authorised to do), the version, and the data access
classification of the data the tool can read or write. Tools connect to the
Agents for which they are available and to the EvidenceArtifacts that constitute
the tool manifest record for a given release.

### ToolAuthorizationRecord

A ToolAuthorizationRecord node represents the authorisation for a specific agent
to use a specific set of tools in a specific phase and at a specific autonomy
tier. ToolAuthorizationRecord nodes are the governance records that make tool
provenance in EvidenceArtifacts traceable back to an explicit authorisation
decision. A ToolAuthorizationRecord carries: the agent identifier the
authorisation applies to, the authorised tool set (a list of Tool node
references), the phase or gate for which the authorisation is valid (Layer 1–4
or a named gate), the authorised autonomy tier, the HumanOwner who granted the
authorisation, and the validity period. ToolAuthorizationRecords connect to the
Agent node they authorise, to the Tool nodes in the authorised set, and to the
HumanOwner who granted the authorisation. An EvidenceArtifact's
tool_authorization_basis field must reference a ToolAuthorizationRecord that was
valid at the time the artefact was produced; an artefact referencing an expired
or absent ToolAuthorizationRecord has an unresolvable provenance gap.

### Dataset

A Dataset node represents a training dataset, fine-tuning corpus, retrieval
corpus, or embedding corpus used by a Model. Dataset nodes are required to
support supply-chain traceability for AI systems: when a model behaves
unexpectedly, the governance graph must be able to answer questions about what
data the model was trained or fine-tuned on and when that data was last
validated. A Dataset node carries a stable identifier, a version, a lineage
reference tracing the data to its source, the date of the last validation run,
and the access classification of the data. Datasets connect to the Models they
train or augment and to the EvidenceArtifacts that record their provenance.

### Dependency

A Dependency node represents an external software component, model, API, or data
source that the system depends on and that is not itself a first-party governed
system. Dependencies are the primary vector for supply-chain risk in deployed
systems. A Dependency node carries a stable identifier, the current version in
use, the pinned version required by the build, the date of the most recent
vulnerability scan, and a confirmation of inclusion in the SBOM. Dependencies
connect to the Build nodes that depend on them, to the Risk nodes that reflect
dependency-specific threat scenarios, and to the EvidenceArtifacts that
constitute the SBOM.

### Build

A Build node represents a specific, reproducible construction of the system from
source. Build nodes are the provenance anchor for release candidates — they
record what was built, from what source, in what environment, and with what
attestation of integrity. A Build node carries a build identifier, the source
commit hash, the artifact hash, a reference to the SLSA provenance attestation,
and the identifier of the build environment. Builds connect to the Dependencies
they incorporate, to the Releases they are promoted into, and to the
EvidenceArtifacts that contain the SLSA attestation.

### Release

A Release node represents an authorised candidate for production deployment. A
Release is not a Build — a Build is a verified construction of source; a Release
is an authorised promotion of a Build to the deployment track, supported by an
assembled evidence bundle and explicit gate sign-off. A Release node carries a
release identifier, a reference to the evidence bundle (EvidenceArtifact),
references to the gate decision records that assessed it, and a reference to the
accountable human sign-off. Releases connect to the Build they promote, to the
Deployments they become when landed in an environment, to the GateDecisions that
authorised them, and to the EvidenceArtifact bundle.

### Deployment

A Deployment node represents a specific instance of a Release running in a
defined environment at a defined point in time. A Deployment is not the same as
a Release — multiple Deployments can derive from the same Release across
environments, and a Deployment has a runtime configuration state that may differ
from the configuration at release time. A Deployment node carries a deployment
identifier, the environment, the deployed timestamp, a hash of the configuration
state at deployment time, and a reference to the rollback target if the
deployment must be reversed. Deployments connect to the Release they
instantiate, to the Runbook that documents their operation, to the Incidents
that occur during their lifecycle, and to the CostRecords that accumulate costs
in their environment.

### Runbook

A Runbook node represents the operational document that governs a deployed
system's day-to-day operation, incident response, and stewardship procedures. A
Runbook is a live governance artefact — it must remain current with the deployed
system or it is stale. A Runbook node carries the content hash of the current
version, the timestamp of the last modification, a reference to the deployed
version it documents, and a derived staleness status. Runbooks connect to the
Deployment they document, to the Incidents referenced during response, and to
the HumanOwner who stewards the document.

### Incident

An Incident node represents a production failure or anomaly that required a
formal response. Incidents are governance artefacts because they confirm or
reveal Risks, trigger specification updates, and generate post-incident review
EvidenceArtifacts that enter the governance record. An Incident node carries a
stable identifier, a classification (service degradation, quality failure,
security incident, or cost anomaly), a severity level, the detection timestamp,
the resolution timestamp, and a reference to the root cause analysis. Incidents
connect to the Deployment in which they occurred, to the Risks they confirm or
newly surface, to the EvidenceArtifacts that constitute the post-incident
review, and to the Specifications they may trigger evaluation updates for.

### CostRecord

A CostRecord node represents a discrete cost observation linked to a governance
artefact. CostRecords make cost governance queryable from the same model as all
other governance state: a question about whether costs are within forecast does
not require a separate finance system — it is answerable from the governance
graph by traversing from a Specification's forecast to the CostRecords
attributed to its Deployments. A CostRecord carries a stable identifier, the
period it covers, the amount, the attribution tags (system, team, environment,
phase, tier, and cost centre), and the unit of measurement (token count, API
call, inference unit, or currency amount). CostRecords connect to the Deployment
or Specification they are attributed to and to the EvidenceArtifacts that
constitute the cost forecast.

### HumanOwner

A HumanOwner node represents a named human with a defined governance role and a
documented scope of accountability. HumanOwner nodes are the accountability
anchors of the governance graph — they are the nodes to which the approved_by
and owned_by edges resolve, and those edges are what makes accountability in the
graph both specific and auditable. A HumanOwner node carries a stable
identifier, the governance role the human holds, and their current availability
status. HumanOwner nodes connect to DemandItems, Specifications, Releases,
Deployments, Runbooks, and GateDecisions through the owned_by or approved_by
edges.

### GateDecision

A GateDecision node represents a recorded gate assessment outcome for a specific
gate and artefact. GateDecisions are the formal record of governance judgments —
they record not only the outcome but the conditions assessed, the GateState of
each condition, the evidence reviewed, and the human who decided. A GateDecision
node carries a stable identifier, a gate type drawn from: specification
readiness, release, operational readiness, or retirement, the date of
assessment, the outcome drawn from: pass, conditional, or fail, the set of
conditions assessed with their GateState values at assessment time, a reference
to the deciding human (HumanOwner), and an expiry date if the outcome was
conditional. GateDecisions connect to the Specification, Release, Deployment,
or retiring system they assessed, to the HumanOwner who made the determination,
and to the EvidenceArtifacts that were reviewed as part of the assessment.

<!-- review/prompts/*.md may need re-checking after this change -->


---

## Edge Types

**validates** runs from DemandItem to Specification. A validated DemandItem
confirms that the Specification it connects to implements a business need that
has passed the demand layer's evidence requirements, establishing the business
intent anchor for the full downstream governance chain.

**implements** runs from Specification to AcceptanceCriterion and from
Specification to Constraint. The Specification defines these elements, and the
edge records that both the AcceptanceCriteria and the Constraints are properties
of the specific versioned Specification — they do not exist independently of it.

**verifies** runs from EvidenceArtifact to AcceptanceCriterion and from
EvidenceArtifact to Control. The EvidenceArtifact is the proof that the
AcceptanceCriterion is satisfied or that the Control is implemented; the absence
of a verifies edge pointing to a given AcceptanceCriterion is the structural
representation of the missing GateState.

**mitigates** runs from Control to Risk. The Control reduces the likelihood or
impact of the Risk it connects to, and this edge is what makes it possible to
ask, from the graph, which Risks currently have no Control with a current test
record pointing to them.

**violates** runs from Incident or finding to Constraint. A production event or
identified finding breached a defined boundary, and this edge records that the
constraint's boundary was crossed — a fact that is significant both for the Risk
model and for the governance record of the affected Deployment.

**depends_on** runs from Build to Dependency and from Deployment to Dependency.
This edge records structural dependency relationships that determine what is in
scope for vulnerability scanning, SBOM generation, and supply-chain risk
assessment.

**generated_by** runs from EvidenceArtifact to Agent or Tool. This edge records
the producing entity and, through the epistemic tier attribute on the
EvidenceArtifact node, the nature of the production — whether a human reviewed
the output before it was filed, whether it is the direct output of a
deterministic tool, or whether it is an agent-generated artefact that has not
yet received human review.

**approved_by** runs from Release or GateDecision to HumanOwner. This is the
accountability edge: it records that a specific named human, at a specific
moment in time, with reference to a specific evidence bundle, accepted
accountability for the decision. This edge cannot be created by an agent. Its
creation requires a human authentication event that is verifiably attributed to
the named HumanOwner.

**owned_by** runs from any governance node to HumanOwner. The stewardship and
accountability assignment — recording that a named human is responsible for the
continued governance of the node's artefact throughout its lifecycle.

**deployed_as** runs from Release to Deployment. A Release becomes one or more
Deployments when it is landed in environments; this edge records that
transition, making it possible to trace from a Deployment back through its
Release to the evidence bundle and gate decisions that authorised it.

**observed_by** runs from Deployment to EvidenceArtifact. Operational telemetry
records, SLO performance records, and cost observations are filed as
EvidenceArtifacts that attach to the Deployment they describe through this edge,
making operational governance state queryable from the same model as
pre-deployment governance state.

**costs** runs from Deployment or Specification to CostRecord. This edge links
cost observations to their governance source — a Specification's cost forecast
and the actual CostRecords accumulated by its Deployments can be compared by
traversing this edge from both ends.

**supersedes** runs from a later Specification, Release, or EvidenceArtifact to
an earlier one. This edge enables lineage traversal: when a question arises
about why the current state differs from a prior state, the supersedes chain
makes the sequence of versions navigable in the graph without requiring an
external version control system query.

**triggered_by** runs from Incident to Deployment event, recording what
operational condition produced the Incident, and from Risk to Incident,
recording that the Incident confirmed an existing Risk or that a newly
discovered Risk was surfaced by the Incident. This edge makes the relationship
between production failures and the Risk model visible in the governance record.

**invoked_via** runs from EvidenceArtifact to Tool. This edge records that the
producing agent invoked a specific Tool when creating this artefact. The edge
carries the invocation timestamp and the data classification of the data
accessed through the tool during that invocation. Multiple invoked_via edges on
a single EvidenceArtifact record multiple tool invocations, one edge per
invocation. The set of invoked_via edges on an EvidenceArtifact, taken together
with the tool_authorization_basis reference, is the structural representation of
tool provenance: it makes it possible to query, from the graph, which tools were
used to produce any given piece of evidence and whether those uses were
authorised.

**authorized_by** runs from ToolAuthorizationRecord to HumanOwner. This edge
records that a specific named human granted the tool authorisation captured in
the ToolAuthorizationRecord, making tool authorisation as accountable as gate
approval: not just which tools were authorised, but who authorised them and
when.

---

## Implementation Guidance

Organisations are free to implement this model in any technology appropriate to
their context. The ASDLC imposes requirements at the semantic level — what must
be true of the governance record — not at the implementation level. An
organisation that implements this model in a property graph database and an
organisation that implements it in a relational schema with carefully maintained
foreign keys and an organisation that implements it as a structured set of
linked documents with consistent identifier conventions are all compliant with
the governance graph requirements, provided the following five implementation
requirements are met.

Every node must be addressable by a stable identifier that survives system
upgrades, migrations, and tooling changes. An identifier that changes when the
underlying storage system is replaced is not stable. Stable identifiers may be
URIs, UUIDs generated at node creation, or structured codes drawn from a defined
namespace — the form is an implementation choice, the stability requirement is
not.

Every EvidenceArtifact node must record a cryptographic hash of its content at
the time of filing, a timestamp, and the identifier of the producing agent or
tool. The hash is the tamper-evidence mechanism: it makes it possible to verify
that the content of the artefact has not been altered since it was filed. The
producing agent or tool identifier is the traceability mechanism: it makes it
possible to query which agent or tool produced any given piece of evidence
without retrieving and inspecting the artefact itself.

Every approved_by edge must record the human identifier, the timestamp of the
approval event, and a reference to the evidence bundle that was in scope at the
time of approval. This three-element record is what makes accountability
auditable: not just who approved, but what they approved and what evidence they
reviewed when they approved it. An approved_by edge that records only the human
identifier is insufficient — without the timestamp and evidence bundle
reference, the edge records the fact of approval but not the conditions under
which it was given.

GateState must be derivable from the graph at any point in time without
performing a new gate assessment. This means the graph must contain sufficient
information — current evidence artefacts, freshness windows, contradiction
detection, waiver records with expiry dates, and requires-human-decision flags —
to compute the GateState of every condition from graph structure and timestamps
alone. An organisation that can only determine GateState by running a new gate
assessment has not implemented the governance graph requirement; it has
implemented a gate assessment tool.

The governance graph must be retained for the lifetime of the governed system
plus the applicable records retention period. Governance artefacts are not
operational logs to be rotated — they are the accountability record of decisions
made about a system that may remain in production for years after the initial
deployment. Retention requirements vary by jurisdiction and industry; the
governance graph's retention policy must be set at the longer of the
organisation's standard records retention requirement and any applicable
regulatory retention mandate.

---

## 2.1 Schema (formal)

The node and edge type definitions in the preceding sections are normative at
the semantic level. To make those definitions enforceable in an implementation,
organisations must publish a formal schema that fixes required fields, types,
identifier patterns, and cardinality constraints. The fragments below are
exemplars expressed in JSON Schema; an organisation may publish equivalent
schemas in JSON Schema, XSD, Protobuf, RDF/SHACL, or any comparable schema
language. Organisations must publish a schema for every node type and every
edge type defined in this document before claiming governance-graph
conformance.

The fragments are illustrative only. They demonstrate the level of precision
required and the patterns to follow; they are not the complete schema set.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://asdlc.example/schema/EvidenceArtifact.json",
  "title": "EvidenceArtifact",
  "type": "object",
  "required": [
    "id",
    "content_hash",
    "filed_at",
    "epistemic_tier",
    "producer_id",
    "freshness_window_seconds"
  ],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^evd:[A-Za-z0-9_-]{1,64}$"
    },
    "content_hash": {
      "type": "string",
      "pattern": "^sha256:[a-f0-9]{64}$"
    },
    "filed_at": {
      "type": "string",
      "format": "date-time"
    },
    "epistemic_tier": {
      "type": "string",
      "enum": [
        "human-authored",
        "tool-generated",
        "agent-proposed-with-human-review",
        "agent-generated"
      ]
    },
    "producer_id": {
      "type": "string",
      "pattern": "^(agent|tool|human):[A-Za-z0-9_.:-]{1,128}$"
    },
    "human_reviewer_id": {
      "type": "string",
      "pattern": "^human:[A-Za-z0-9_.:-]{1,128}$"
    },
    "freshness_window_seconds": {
      "type": "integer",
      "minimum": 0
    },
    "tool_invocations": {
      "type": "array",
      "items": { "$ref": "ToolInvocation.json" }
    },
    "external_data_sources": {
      "type": "array",
      "items": { "$ref": "ExternalDataSource.json" }
    },
    "tool_authorization_basis": {
      "type": "string",
      "pattern": "^tar:[A-Za-z0-9_-]{1,64}$"
    }
  },
  "allOf": [
    {
      "if": {
        "properties": {
          "epistemic_tier": { "const": "agent-proposed-with-human-review" }
        }
      },
      "then": { "required": ["human_reviewer_id"] }
    }
  ]
}
```

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://asdlc.example/schema/GateDecision.json",
  "title": "GateDecision",
  "type": "object",
  "required": [
    "id",
    "gate_type",
    "assessed_at",
    "outcome",
    "deciding_human_id",
    "conditions_assessed"
  ],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^gd:[A-Za-z0-9_-]{1,64}$"
    },
    "gate_type": {
      "type": "string",
      "enum": ["specification-readiness", "release", "operational-readiness"]
    },
    "assessed_at": {
      "type": "string",
      "format": "date-time"
    },
    "outcome": {
      "type": "string",
      "enum": ["pass", "conditional", "fail"]
    },
    "deciding_human_id": {
      "type": "string",
      "pattern": "^human:[A-Za-z0-9_.:-]{1,128}$"
    },
    "expiry": {
      "type": "string",
      "format": "date-time"
    },
    "conditions_assessed": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["condition_id", "gate_state"],
        "properties": {
          "condition_id": { "type": "string" },
          "gate_state": {
            "type": "string",
            "enum": [
              "pass",
              "fail",
              "missing",
              "stale",
              "contradicted",
              "waived",
              "requires-human-decision"
            ]
          },
          "evidence_ids": {
            "type": "array",
            "items": {
              "type": "string",
              "pattern": "^evd:[A-Za-z0-9_-]{1,64}$"
            }
          }
        }
      }
    }
  },
  "allOf": [
    {
      "if": { "properties": { "outcome": { "const": "conditional" } } },
      "then": { "required": ["expiry"] }
    }
  ]
}
```

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://asdlc.example/schema/HumanOwner.json",
  "title": "HumanOwner",
  "type": "object",
  "required": ["id", "role", "availability_status"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^human:[A-Za-z0-9_.:-]{1,128}$"
    },
    "role": {
      "type": "string",
      "enum": [
        "demand-sponsor",
        "specification-analyst",
        "steward",
        "economics-owner",
        "release-approver",
        "governance-portfolio-owner",
        "waiver-grantor",
        "tool-authorisation-grantor"
      ]
    },
    "availability_status": {
      "type": "string",
      "enum": ["available", "unavailable", "delegated"]
    },
    "delegate_id": {
      "type": "string",
      "pattern": "^human:[A-Za-z0-9_.:-]{1,128}$"
    }
  },
  "allOf": [
    {
      "if": {
        "properties": { "availability_status": { "const": "delegated" } }
      },
      "then": { "required": ["delegate_id"] }
    }
  ]
}
```

The full schema set must define equivalent fragments for every node type listed
in the Node Types section and every edge type listed in the Edge Types section,
including identifier patterns, required and optional fields, types (string,
integer, ISO 8601 timestamp, sha-256 hash hex), and any conditional
requirements implied by the prose (for example, that an EvidenceArtifact at the
agent-proposed-with-human-review tier requires a human_reviewer_id).

### Cardinality rules

The following cardinality rules are normative for the edges defined in this
document. An organisation's schema must enforce them.

- **validates** (DemandItem → Specification): one DemandItem may validate many
  Specifications; each Specification must be validated by exactly one
  DemandItem. The validates edge is required at Specification creation; a
  Specification with no validates edge must not pass the Specification
  Readiness Gate.
- **implements** (Specification → AcceptanceCriterion; Specification →
  Constraint): one Specification implements many AcceptanceCriteria and many
  Constraints (1:N in each case). Each Specification must have at least one
  AcceptanceCriterion and at least one Constraint linked by an implements edge
  for the Specification Readiness Gate to pass.
- **verifies** (EvidenceArtifact → AcceptanceCriterion; EvidenceArtifact →
  Control): many EvidenceArtifacts may verify many AcceptanceCriteria and many
  Controls (M:N). For each AcceptanceCriterion, at least one verifies edge
  from a non-stale EvidenceArtifact is required for the corresponding GateState
  to evaluate to pass; absence of any verifies edge produces a missing
  GateState.
- **mitigates** (Control → Risk): many Controls may mitigate many Risks (M:N).
  A Risk with no mitigates edge from any Control is in a structurally
  unmitigated state and must carry an explicit acceptance record on the
  associated GateDecision before any gate can pass.
- **violates** (Incident → Constraint; Finding → Constraint): many Incidents
  or Findings may violate many Constraints (M:N).
- **depends_on** (Build → Dependency; Deployment → Dependency): many Builds
  and Deployments may depend on many Dependencies (M:N). Every Dependency
  reachable through a depends_on edge from a Build must appear in the SBOM
  EvidenceArtifact for that Build.
- **generated_by** (EvidenceArtifact → Agent or Tool): each EvidenceArtifact
  must have exactly one generated_by edge; multiple producers must instead be
  represented by an aggregating EvidenceArtifact whose tool_invocations list
  records the individual producers.
- **approved_by** (Release → HumanOwner; GateDecision → HumanOwner): one
  Release is approved by exactly one HumanOwner (1:1); one GateDecision is
  approved by exactly one HumanOwner (1:1). The approved_by edge is required
  at Release Gate sign-off; a Release with no approved_by edge must not be
  promoted to Deployment.
- **owned_by** (any governance node → HumanOwner): every governance node must
  have exactly one current owned_by edge to a HumanOwner with availability
  status `available` or `delegated`. Multiple historical owned_by edges may
  exist through supersedes lineage.
- **deployed_as** (Release → Deployment): one Release may be deployed as many
  Deployments (1:N).
- **observed_by** (Deployment → EvidenceArtifact): one Deployment may be
  observed by many EvidenceArtifacts (1:N).
- **costs** (Deployment or Specification → CostRecord): one Deployment or
  Specification may have many CostRecords (1:N).
- **supersedes** (Specification, Release, or EvidenceArtifact → prior of same
  type): forms a directed acyclic graph; cycles are forbidden. Each node may
  supersede at most one prior node and may be superseded by at most one later
  node.
- **triggered_by** (Incident → Deployment event; Risk → Incident): many
  Incidents may be triggered by many Deployment events (M:N); many Risks may
  be triggered by many Incidents (M:N).
- **invoked_via** (EvidenceArtifact → Tool): many EvidenceArtifacts may be
  produced via many Tools (M:N); each invoked_via edge represents a single
  invocation, with multiple invocations expressed as multiple edges.
- **authorized_by** (ToolAuthorizationRecord → HumanOwner): one
  ToolAuthorizationRecord is authorised by exactly one HumanOwner (1:1).

### Referential integrity

Deletion of a node referenced by a non-superseded edge is forbidden. A node
that has been replaced by a newer version must be marked as superseded through
the supersedes edge; the prior node remains in the graph and remains
queryable, but is no longer the current node for queries that select the
current state. The supersedes chain provides the lineage path for any
replacement; it is the only mechanism by which a node may be effectively
removed from current queries while preserving the audit record. An attempt to
delete a node without a supersedes-style replacement, or to delete a
HumanOwner referenced by an active approved_by or owned_by edge, must fail at
the schema level.

## 2.2 Schema versioning

The governance graph schema is itself a versioned governance artefact. The
following versioning policy applies.

- The canonical GateState enum is normative. Adding a new value, removing a
  value, or altering the semantics of an existing value requires a
  major-version increment of the schema registry and a documented migration
  plan for all affected graph instances.
- New node types or edge types may be added in a minor-version registry
  update without invalidating existing graph instances, provided no existing
  node or edge type is altered.
- Adding a new optional field to an existing node or edge type is a
  minor-version change. Adding a new required field, removing a field, or
  changing the type or pattern of an existing field is a major-version
  change.
- Renaming an existing node or edge type is a major-version change and
  requires a documented migration path with a supersedes-style mapping from
  the old type name to the new one. The migration mapping itself is a
  governance artefact and must be retained for the same retention period as
  the underlying graph data.
- Existing EvidenceArtifact records remain valid against the schema version
  they were filed under, even after the registry advances to a later version.
  Queries against multi-version graphs must be schema-version-aware: the
  query engine must apply the field set, type rules, and identifier patterns
  appropriate to the schema version each artefact was filed under.

## 2.3 GateState computation algorithm

The following algorithm is normative for computing the GateState of a single
gate condition at a specific instant. It is expressed as language-agnostic
pseudocode. Two compliant implementations of the governance graph must
produce the same GateState for the same input data at the same instant;
divergence in computed GateState for identical inputs is non-conformance.

```
function compute_gate_state(condition, instant):
    # condition is a registry definition; instant is an ISO 8601 timestamp.

    # 1. Locate verifying evidence.
    verifying = select EvidenceArtifact e
                where exists verifies(e, condition)
                  and e.filed_at <= instant
                  and not superseded(e, instant)

    # 2. Locate active waivers.
    waivers = select Waiver w
              where w.condition_id = condition.id
                and w.granted_at <= instant
                and w.expiry > instant
                and not revoked(w, instant)

    # 3. Locate human-decision artefacts.
    human_decisions = select EvidenceArtifact e in verifying
                      where e.kind = "human-decision-record"

    # 4. Missing check.
    if verifying is empty and waivers is empty:
        return missing

    # 5. Active-waiver check (waiver overrides downstream states except
    #    contradicted, which signals an internal inconsistency that a waiver
    #    cannot validly suppress without explicit acknowledgement).
    if waivers is non-empty:
        if exists_contradiction(verifying):
            return contradicted
        return waived

    # 6. Contradiction check.
    if exists_contradiction(verifying):
        # Two artefacts disagree on a load-bearing fact identified by the
        # condition's registry definition (e.g., model_version,
        # dependency_version, sbom_hash).
        return contradicted

    # 7. Freshness check.
    fresh = filter verifying where
            (e.filed_at + e.freshness_window_seconds) > instant
            and not invalidated_by_event(e, instant)
    if fresh is empty:
        # An expired waiver, if any, has already been excluded above; the
        # condition has no current evidence supporting a pass state.
        return stale

    # 8. Human-decision flag.
    if condition.requires_human_decision and human_decisions is empty:
        return requires-human-decision

    # 9. Substantive failure check.
    if exists e in fresh where e.verdict = "fail":
        return fail

    # 10. Default.
    return pass
```

The functions `superseded`, `revoked`, `exists_contradiction`, and
`invalidated_by_event` are themselves derived from graph structure: a node is
superseded if a supersedes edge from a later node points to it with effective
date prior to the instant; a waiver is revoked if a Revocation node references
it with effective date prior to the instant; a contradiction exists if two
non-superseded EvidenceArtifacts verifying the same condition disagree on a
load-bearing fact identified by the condition's registry definition; an
artefact is invalidated by an event if a depends_on or behavioral_dependency
relationship targets a node whose state changed after the artefact was filed
and the registry definition marks that change as freshness-invalidating.

## 2.4 Query examples (concrete)

The following examples illustrate the canonical question "Which Risks
currently have no Control with a passing test record within the last 90
days?" expressed against three implementation substrates. Each example is
syntactically plausible against the schemas described above and includes
inline comments mapping clauses to node and edge types.

```cypher
// Cypher (property graph)
// Risks lacking a mitigates edge from a Control whose most recent test
// EvidenceArtifact is non-stale and within 90 days.
MATCH (r:Risk { acceptance_status: "blocking" })
WHERE NOT EXISTS {
  MATCH (c:Control)-[:mitigates]->(r)        // Control → Risk
  MATCH (e:EvidenceArtifact)-[:verifies]->(c) // Evidence → Control
  WHERE e.kind = "control-test-result"
    AND e.verdict = "pass"
    AND e.filed_at >= datetime() - duration({days: 90})
}
RETURN r.id AS risk_id, r.category AS category;
```

```sparql
# SPARQL (RDF)
# Same question, expressed against an RDF representation.
PREFIX g: <https://asdlc.example/graph/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?risk_id ?category
WHERE {
  ?risk a g:Risk ;
        g:id ?risk_id ;
        g:category ?category ;
        g:acceptance_status "blocking" .
  FILTER NOT EXISTS {
    ?control g:mitigates ?risk .                # Control mitigates Risk
    ?evidence g:verifies ?control ;             # Evidence verifies Control
              g:kind "control-test-result" ;
              g:verdict "pass" ;
              g:filed_at ?filed_at .
    FILTER (?filed_at >= (NOW() - "P90D"^^xsd:duration))
  }
}
```

```sql
-- SQL (relational)
-- Same question, expressed against a relational projection of the graph.
-- Tables: risks, controls, mitigates_edges, evidence_artifacts, verifies_edges.
SELECT r.id AS risk_id, r.category
FROM risks r
WHERE r.acceptance_status = 'blocking'
  AND NOT EXISTS (
    SELECT 1
    FROM mitigates_edges m                              -- Control → Risk
    JOIN controls c               ON c.id = m.control_id
    JOIN verifies_edges v         ON v.target_id = c.id -- Evidence → Control
                                 AND v.target_kind = 'Control'
    JOIN evidence_artifacts e     ON e.id = v.evidence_id
    WHERE m.risk_id = r.id
      AND e.kind = 'control-test-result'
      AND e.verdict = 'pass'
      AND e.filed_at >= NOW() - INTERVAL '90 days'
  );
```

The following two examples illustrate further canonical questions in Cypher
only.

```cypher
// "Which AcceptanceCriteria of the active Specification have GateState =
//  missing right now?"
// AcceptanceCriteria reachable from the active Specification with no
// non-superseded verifies edge from any EvidenceArtifact.
MATCH (s:Specification { status: "active" })-[:implements]->(ac:AcceptanceCriterion)
WHERE NOT EXISTS {
  MATCH (e:EvidenceArtifact)-[:verifies]->(ac)
  WHERE NOT EXISTS { MATCH (later:EvidenceArtifact)-[:supersedes]->(e) }
}
RETURN s.id AS specification_id, ac.id AS acceptance_criterion_id;
```

```cypher
// "Which active waivers expire in the next 14 days, and which conditions do
//  they cover?"
MATCH (w:Waiver)
WHERE w.granted_at <= datetime()
  AND w.expiry > datetime()
  AND w.expiry <= datetime() + duration({days: 14})
  AND NOT EXISTS { MATCH (rev:Revocation)-[:revokes]->(w) }
RETURN w.id AS waiver_id,
       w.condition_id AS condition_id,
       w.expiry AS expires_at,
       w.granted_by AS waiver_grantor;
```

## 2.5 Conformance test

An organisation claiming governance-graph conformance must demonstrate, on a
synthetic test corpus, that its implementation produces the canonical
GateState defined in § 2.3 for every condition under at least the following
scenarios.

- **Fresh-evidence pass.** A condition with a single non-stale verifying
  EvidenceArtifact at the appropriate epistemic tier, no contradictions, and
  no active waiver. Expected GateState: pass.
- **Stale-window expiry.** A condition with a verifying EvidenceArtifact
  whose freshness window has elapsed prior to the evaluation instant, no
  active waiver, no contradictions. Expected GateState: stale.
- **Contradicted artefact pair.** A condition with two non-superseded
  verifying EvidenceArtifacts that disagree on a load-bearing fact (for
  example, model_version), no active waiver. Expected GateState:
  contradicted.
- **Expired waiver fall-through.** A condition with a Waiver whose expiry is
  prior to the evaluation instant and verifying evidence that is otherwise
  stale. Expected GateState: stale (the expired waiver does not preserve the
  pass state).
- **Active waiver.** A condition with a Waiver whose expiry is after the
  evaluation instant, regardless of underlying evidence freshness. Expected
  GateState: waived.
- **Missing artefact.** A condition with no verifying EvidenceArtifact and no
  active waiver. Expected GateState: missing.
- **Requires-human-decision flag.** A condition whose registry definition
  carries the requires-human-decision flag, with verifying evidence present
  but no human-decision-record EvidenceArtifact. Expected GateState:
  requires-human-decision.
- **Multi-condition gate, mixed states.** A gate with at least three
  conditions where one is in pass state, one is waived (active waiver), and
  one is missing. Expected GateDecision outcome at the gate level: not pass,
  with each condition's GateState surfaced individually.

This is the conformance baseline. The schema registry repository should ship
a synthetic test corpus, expected GateState outputs, and a conformance test
harness once the Phase 2 schema work lands. An implementation that passes the
baseline corpus has demonstrated GateState computation parity with the
canonical algorithm; an implementation that fails any baseline scenario has
not.

---

## Governance State Projection

The governance graph must be able to project future governance state, not only
represent current state. Current state answers the question: "What is the
governance status right now?" Projection answers the question: "Given current
state and known future events, which gate conditions will transition from pass
to stale or missing before the next scheduled gate assessment?" The distinction
is operationally significant: a gate assessment that discovers stale conditions
at gate time is a reactive governance failure; a gate readiness forecast that
identifies those conditions seven days in advance is a proactive governance
practice.

The projection model is defined as follows.

For each EvidenceArtifact with a defined freshness window, the projected
staleness date is computable from the last validation timestamp and the window
duration. This computation is deterministic and requires no external input: the
governance graph has all the information it needs to identify every artefact
that will become stale before a specified future date.

For each upcoming scheduled change — Stage 6 maintenance notifications, planned
dependency updates, and scheduled model version changes — the governance graph
can project which gate conditions will be triggered stale by that change before
it occurs. A planned model version update that will invalidate the evaluation
parity assumption of a deployed agent, for example, produces a projected stale
GateState for every condition that depends on model version confirmation. This
projection is computable as soon as the planned change is recorded in the graph,
which may be days or weeks before the change is executed.

The projection horizon is configurable per system. The minimum projection
horizon is 7 days for standard systems and 14 days for high-blast-radius
systems. Systems with longer planned maintenance cycles or regulatory audit
windows should extend the projection horizon to match their operational cadence.

The output of the projection model is a gate readiness forecast. For each gate
condition, the forecast records its current GateState and its projected
GateState at the scheduled gate assessment date. A gate readiness forecast is
not a prediction — it is a deterministic computation based on known freshness
windows, known scheduled changes, and the current evidence state. It does not
predict whether new incidents will occur; it reports what will happen to
existing evidence given what is currently known.

Gate readiness forecasts must be computed and reviewed at the weekly steward
review. A gate readiness forecast showing more than two conditions at risk of
transitioning to stale before the scheduled gate assessment is an operational
signal requiring pre-emptive evidence regeneration. Discovering at gate time
that conditions are stale is not an acceptable outcome when the gate readiness
forecast identified that risk in advance. The forecast converts stale-condition
discovery from a gate-blocking reactive event into a routine pre-gate activity.

---

## Governance Quality Indicators

GateState is per-condition: a condition resolves to pass, fail, missing,
stale, contradicted, waived, or requires-human-decision. A gate that closes
with every condition at pass or waived is a governance outcome. Not all such
outcomes represent the same governance assurance. A gate closure where every
condition is backed by human-authored evidence, independently reviewed, with
no waivers, and where the deciding human documented specific challenges before
sign-off provides different governance assurance than a gate closure where
every condition is backed by agent-generated evidence, reviewed nominally,
with several active waivers covering critical conditions, and where sign-off
was instantaneous. The governance graph must make these differences observable.
GateState alone does not. Governance quality indicators do.

The four indicators below are computed at gate closure from data already
present in the governance graph. Each indicator is a descriptive measure
recorded as an attribute of the GateDecision node and projected into portfolio
dashboards and trend reports. The indicators are not synthesised into a single
score, and none of them is gating: a gate decision is determined by the
GateState of its conditions and the governance process around sign-off, not by
the indicators below.

**Epistemic composition ratio.** Recorded as a percentage. The proportion of
gate artefacts whose epistemic tier is human-authored or tool-generated, over
the total number of gate artefacts assessed. A complementary percentage
(agent-proposed-with-human-review plus agent-generated) makes the agent share
of the evidence chain visible. The indicator is not weighted, scored on a
fixed scale, or thresholded; it is a descriptive measure of the evidence
composition behind the gate decision.

**Active waiver burden.** Recorded as a count, broken down by criticality of
the condition each waiver covers. The breakdown distinguishes at least
high-criticality conditions from standard conditions and reports the number of
active waivers in each band, together with the median and maximum remaining
waiver duration in days. The indicator is not collapsed to a single score; the
count and breakdown are the indicator.

**Independence quality.** Recorded as a binary indicator (independent or
not-independent), with the precise definition adopted by
[Release Governance](../release-governance.md). A gate is independent only
when the independent validator is organisationally separate from the
engineering team responsible for the artefacts they validated, and when the
accountable human sign-off is provided by a different person from the
specification analyst. Intermediate arrangements are recorded as
not-independent; partial credit is not assigned.

**Approval engagement signal.** Recorded as a structured set of fields rather
than a single score. The fields are: review duration (the elapsed time from
evidence bundle delivery to sign-off, in minutes), the number of documented
challenges raised by the deciding human prior to sign-off, the number of
conditions returned for rework before approval, and the proportion of review
time spent on primary evidence artefacts versus agent-generated summaries
where that breakdown is observable. Each field is recorded as filed; no
field is converted into a 0-to-N score.

These indicators are descriptive, not gating. They populate portfolio
dashboards and trend reports for the governance portfolio owner, the steward
of the governed system, and the operational DoD review. They do not, by
themselves, block a gate decision, trigger a mandatory independent review, or
override the GateState computation defined in § 2.3.

A synthesised score (for example, a 0-to-100 composite indicator) requires
empirical calibration against external truth — incident outcomes, audit
findings, regulatory examination results, or comparable independent signals —
before adoption. The framework does not currently ship a calibrated synthesis.
Organisations that compute one for their internal use must document the
calibration evidence, the cohort against which the calibration was performed,
and the failure modes the synthesis is known to be susceptible to. Two failure
modes must be acknowledged explicitly: Goodhart's law applied to the epistemic
composition ratio (driving the ratio up by reclassification rather than by
substantive change to the evidence chain), and the performative-challenge
incentive applied to the approval engagement signal (raising challenges that
are recorded for the indicator but do not represent substantive review).

Portfolio review of governance quality indicators is mandatory at the same
cadence as the operational DoD review (quarterly by default; more frequently
where the governance portfolio owner determines that the indicators warrant
it). Portfolio review is not triggered by an indicator value crossing an
arbitrary threshold; it occurs on the defined cadence, and it considers the
indicators in their descriptive form alongside the GateState records, the
incident record, and the audit record.

[^1]: A prior specification of this section defined a 0-to-100 Governance
    Quality Score (GQS) with fixed component weights (40/20/20/20) and a
    threshold (GQS below 40 on any gate pass for a high-blast-radius system
    triggering a mandatory independent review). That specification was
    withdrawn pending the calibration evidence described above. The four
    components are retained as descriptive indicators; the synthesis and the
    threshold are not.

---

## Relationship to Other ASDLC Documents

The governance graph is a structural dependency of several other ASDLC
documents, and understanding those dependencies clarifies what each document
contributes to the overall governance model.

[Governance Agents](agents.md) provides the framework within which
Agent nodes in the governance graph are themselves governed. Every Agent node
that generates EvidenceArtifacts — whether it is a release evidence assembly
agent, a vulnerability triage agent, or a runbook staleness monitor — is subject
to the ASDLC's governance agent requirements: a specification, an evaluation
suite, an accountable human, and an autonomy tier assignment. The governance
graph's Agent node records the product of that governance process;
agents.md defines the process by which an agent becomes a well-formed
Agent node rather than an ungoverned system producing ungoverned outputs.

[Agent Control Plane](../agent-control-plane.md) names the specific governed agents
that operate on the governance graph and defines their schemas. Where
agents.md establishes the framework, the agent-control-plane defines
its instantiation: which specific agents are in scope, what tasks they are
authorised to perform, what data they are authorised to read and write, and how
their outputs enter the graph as EvidenceArtifacts at the appropriate epistemic
tier. The agent-control-plane is the governance record for the agents that
maintain the graph; the governance graph is the structure those agents operate
within.

[Governance Queries](queries.md) defines the canonical governance
questions that the model exists to answer. The node types, edge types, and
GateState values defined in this document are designed with specific query
patterns in mind — the ability to determine which conditions are currently
failing, which evidence is stale, which risks have no active control, and which
humans are accountable for which decisions. Governance queries defines those
questions precisely and specifies how they are answered from the graph's
structure, making the governance graph's operational utility concrete rather
than abstract.

[Waiver Governance](../waiver-governance.md) defines the lifecycle of the waived
GateState and the conditions under which it is valid. A waived GateState in the
governance graph is not a static property — it is a time-bounded state with a
structured expiry mechanism, a required accountability anchor, and a return path
to normal governance scrutiny when the waiver expires. Waiver governance defines
what must be true of the Waiver node, the approved_by edge, the expiry date, and
the transition back to an assessable condition. The governance graph records the
structural fact of a waiver; waiver governance defines the conditions under
which that structural fact is a legitimate governance outcome rather than a
governance bypass.
