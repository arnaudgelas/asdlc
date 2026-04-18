# Governance Agents — ASDLC Cross-Cutting

_How AI agents participate in governance work across all four layers._

See [ASDLC Overview](../asdlc.md) for the four-layer architecture. See
[Specification Readiness](../specification-readiness.md) for the gate agents may
assist. See [Release Governance](../release-governance.md) for agent-assisted
evidence assembly. See [Operations Governance](../operations/governance.md) for
agent-assisted operational monitoring. See
[Maintenance Governance](../maintenance-governance.md) for agent-assisted
stewardship.

---

## The Governance Agent Model

The ASDLC governs agentic systems — systems that reason, plan, and act
autonomously in pursuit of specified goals. This document governs a different
and more specific subject: agents that participate in the governance work of the
ASDLC itself. These two roles are distinct and must not be conflated. An
engineering agent builds, executes, and produces loop outputs. A governance
agent generates evidence, validates conditions, monitors state, and surfaces
findings so that governance decisions can be made by humans who are equipped
with reliable information. A governance agent does not make governance decisions
— accountability for those decisions remains with named humans — but it performs
the repeatable evidence work that makes human governance decisions tractable at
scale and at the pace that agentic delivery demands.

Why this matters is a function of scale. As organisations deploy more agentic
systems under ASDLC governance, the governance workload does not stay constant —
it scales with the number of systems, the number of active loop iterations, the
number of release gates being assessed simultaneously, and the number of
operational systems under stewardship. Without agent participation in
governance, every gate assessment, every evidence bundle assembly, every
operational Definition of Done review, and every maintenance staleness check is
performed by humans at the same cost as the first. The human governance
workforce does not scale at the same rate as the agentic delivery workforce.
With agent participation in governance, the human governance load is
redistributed toward the work that requires judgment — assessing whether
evidence is genuinely sufficient, accepting accountability for outcomes,
identifying novel failure modes — and away from the work that can be
substantially assisted: evidence collection, condition checklist execution,
artefact consistency verification, and continuous state monitoring.

The limits of this model must be stated plainly before the model is applied.
Governance agents do not replace accountable humans. The foundational principle
that an agent cannot be the accountable party — established across the ASDLC's
treatment of engineering execution — applies with equal force to governance
agents. A governance agent that assembles an evidence bundle does not sign off
on it: the release manager does. A governance agent that produces a first-draft
threat model does not validate it: the security function does. A governance
agent that detects a runbook as stale does not update it without human review:
the steward does. The governance agent's role is to make the human's work more
tractable, not to substitute for the human's judgment or to absorb the human's
accountability. The boundary between what agents may do and what humans must
decide is not capability — it is consequence. Agents may prepare evidence,
summarize risk, flag missing controls, draft threat models, assemble bundles,
and recommend decisions. Agents may not accept residual risk, approve production
exposure, waive controls, or absorb accountability for business outcomes. When a
decision has consequences the organization must answer for, a named human must
make it.

---

## The Circular Dependency — Governance Agents Are Governed by ASDLC

The most important structural point in this document is this: a governance agent
is itself an agentic system. A governance agent that monitors operational state,
assembles evidence, drafts threat models, or proposes specification changes is
an agentic system operating in production. It therefore requires governance
under the ASDLC in the same way as any other agentic system. The governance
agent is not exempt from the framework it assists. It is subject to every
requirement the framework imposes: a specification defining its governance task
scope, constraints, and blast radius; an evaluation suite demonstrating that it
produces correct outputs under known conditions including adversarial cases; a
named accountable human who owns the system's actions; and a steward who governs
the system's lifecycle from deployment through retirement.

The blast radius of a governance agent is not defined by what the agent does in
isolation. It is defined by the blast radius of acting on an incorrect
governance agent output. A governance agent that monitors runbook staleness and
sends a notification when a staleness threshold is exceeded has low blast
radius: the worst outcome of an incorrect output is that a stale runbook remains
stale slightly longer than it should. A governance agent that assembles evidence
bundles for release gate assessment has medium blast radius: an incorrectly
assembled bundle — one that includes stale attestations, misidentifies the model
version under test, or omits a failed security scan — could allow a flawed
release to pass the gate unchallenged. A governance agent that recommends
specification changes based on operational patterns has higher blast radius: an
incorrect recommendation could distort a system's scope in ways that propagate
through multiple loop iterations before the distortion is detected. The blast
radius tier of the governance agent's outputs determines the oversight required
before those outputs can be used as governance evidence.

Governance agents must therefore be phased in under the same phase-calibration
approach that applies to other agentic systems. An organisation at Phase 2 —
where the engineering governance infrastructure is still being built — is not
yet ready to use governance agents for anything beyond advisory output reviewed
by humans before use. An organisation at Phase 4, with established evaluation
suites, proven rollback capabilities, and mature stewardship processes, can
operate governance agents at monitored execution autonomy for well-defined,
bounded tasks with clear correctness criteria. The autonomy level of any
governance task must match the maturity of the governance agent's own governance
infrastructure, not merely the maturity of the engineering loop it assists.
Deploying a governance agent at an autonomy level unsupported by its own
evaluation and oversight infrastructure is a governance failure — one that
compounds the risk of the systems it is supposed to govern.

---

## Governance Agent Behavioral Identity

A governance agent's behavior is determined not only by its application code but
by the simultaneous composition of four components: (a) the application code at
a specific commit, (b) the system prompt at a specific version, (c) the
foundation model — provider, model name, and snapshot version where the provider
makes snapshot versioning available — and (d) the tool manifest, meaning the set
of tools available to the agent and their versions or configurations. A change
in any one of these four components changes the agent's behavior. The
**Governance Agent State Hash (GASH)** is defined as a hash over the four
component identifiers taken together. When all four are fixed, the GASH is
stable and the agent's behavioral identity is known. When any component changes
— including a provider-initiated model update that occurs without the governance
organisation's action — the GASH changes and the agent's behavioral identity
changes.

The governance consequence of a GASH change is clear: the governance agent at
the new GASH is a different agent from the one whose evaluation evidence is on
record. Before the agent continues producing governance evidence at its current
autonomy level, a new evaluation run must be completed at the new GASH and the
results must be filed in the governance agent's specification record. The
evaluation run does not need to repeat tests that are demonstrably insensitive
to the specific component that changed — but this determination must be made
explicitly by the governance agent's accountable human, not assumed.

The governance agent's node in the governance graph must record two GASH values:
the current GASH and the GASH at which the last evaluation suite was run. The
divergence between these two — the **evaluation lag** — is an operational
metric. A zero evaluation lag means the agent is currently operating under a
GASH for which evaluation evidence exists. A non-zero evaluation lag means the
agent has changed since its last evaluation and is operating on unverified
behavioral identity. Evaluation lag must be surfaced to the governance agent's
accountable human as a standing operational dashboard item. An evaluation lag
that persists beyond the defined maximum — to be established in the governance
agent's specification — is a governance staleness event for the governance agent
itself, distinct from any staleness events it may detect in the systems it
governs.

An undetected GASH change discovered retrospectively is a governance staleness
event with specific consequence: all governance artefacts produced by the agent
since the GASH changed without detection must be reviewed for potential
re-assessment. The scope of that review is determined by the blast radius tier
of the affected artefacts and the nature of the component that changed. A system
prompt change that subtly altered how the agent interprets
constraint-completeness criteria is more likely to require broad re-assessment
than a tool manifest change affecting a single peripheral tool. The accountable
human determines the scope of the re-assessment; the determination and its
rationale must be filed as a governance artefact.

---

## Epistemic Tiers for Governance Artefacts

All governance artefacts — specifications, gate decision records, threat models,
evidence bundles, runbooks, post-incident reviews, vulnerability assessments,
and SBOM records — carry an epistemic status that determines how they may be
used in governance decisions. This status is not implicit; it must be labelled.
An evidence bundle that does not label the epistemic tier of each included
artefact is incomplete, because the epistemic status of each component is
material to assessing whether the gate conditions it is supposed to satisfy are
genuinely satisfied. The four tiers that apply across all governance artefacts
are as follows.

**Human-authored** is the default epistemic assumption when no label is present.
The artefact was produced by a human, without AI assistance in the substance of
the content. Human-authored artefacts may use AI assistance in ancillary ways —
grammar checking, formatting, translation — but the substantive determinations
and judgments in the artefact were made by the human and reflect the human's own
assessment. In governance contexts, human-authored artefacts carry the full
weight of the named author's accountability: when the document is reviewed, the
reviewer is reviewing the named human's conclusions.

**Tool-generated** artefacts were produced by deterministic tools: a static
analysis scanner, a dependency vulnerability database query, a software bill of
materials generator, a cryptographic hash function, an SLSA attestation
generator, a certificate expiry checker. The tool's output is deterministic for
given inputs; there is no inference or generation involved. Tool-generated
artefacts do not require the same qualitative review as agent-generated
artefacts, because the correctness of the tool can be validated independently of
any specific output — the tool is governed, not the individual output instance.
What requires governance is that the correct tool was run, on the correct
inputs, with the correct configuration, and that the output has not been altered
between generation and use.

**Agent-proposed, human-reviewed** artefacts were drafted by an AI agent and
then reviewed and validated by a qualified human before being accepted as
governance evidence. The human reviewer's identity and the date of review must
be recorded alongside the artefact. The acceptance of the artefact is the
human's, not the agent's: the human has read the draft, applied their own
judgment, confirmed its accuracy and completeness, and accepted responsibility
for its contents. The agent's contribution was to accelerate the production of a
reviewable draft; the human's contribution was to make it an accountable
governance artefact. An agent-proposed, human-reviewed artefact may serve as
primary evidence for gate conditions, because it carries a named human's
validation.

**Agent-generated** artefacts were produced by an AI agent and have not been
reviewed by a qualified human. Agent-generated artefacts without human review
may be used as advisory inputs to governance decisions — they can flag issues,
surface patterns, and direct human attention — but they may not serve as the
primary evidence for gate conditions. A gate condition whose sole evidence is an
agent-generated artefact that has not been reviewed by a qualified human is not
satisfied in the governance sense, regardless of the apparent quality of the
agent's output. The reason is not that agent-generated artefacts are necessarily
incorrect; it is that governance is an accountable human's assertion that
conditions are met, not an agent's assertion. No mechanism exists for an agent
to accept accountability for a governance determination.

Every governance artefact in every evidence bundle must carry a visible
epistemic label. The label is part of the artefact's metadata, not a separate
document. When a release manager reviews an evidence bundle, the epistemic
status of each component must be immediately visible without cross-referencing
another document.

---

## Governance Task Classification by Autonomy

Governance tasks are classified by the level of autonomous authority the
governance agent may exercise when executing them. Three governance autonomy
levels apply, distinct from the engineering execution autonomy tiers (P9) that
govern agents in the inner loop. The assignment of a governance task to an
autonomy level must be documented in the governance agent's specification.
Upgrading a task from a lower to a higher autonomy level requires a
specification change, a new evaluation suite run against the upgraded autonomy
scope, and explicit approval from the governance agent's accountable human.
Autonomy level assignment is not a one-time decision; it must be reviewed
whenever the governance agent's operational context, blast radius assessment, or
evaluation suite changes materially.

The classification of a governance task into one of these three levels is
determined by the consequence of acting on an incorrect agent output — not by
the agent's capability to perform the task. A sufficiently capable agent can
produce plausible outputs for any governance task; the autonomy classification
governs whether those outputs may be acted on without human review.

**Advisory** is the baseline level. The governance agent produces an output — a
flag, a draft, an assessment, a recommendation — that is presented to a human
governance worker as input. The human reviews the agent's output and makes their
own determination independently. The agent's output is not accepted as
governance evidence unless the human endorses it, at which point it becomes an
agent-proposed, human-reviewed artefact carrying the human's accountability.
Advisory tasks are appropriate where the consequence of an incorrect output is
that a human must correct it before it enters governance evidence — not where an
incorrect output could pass through into a gate decision without human scrutiny.
Examples include: threat model first drafts produced for security function
review; constraint gap flags in draft specifications that a specification
analyst must evaluate; vulnerability exploitability assessments that a security
engineer must confirm before a VEX status is assigned; and runbook drift
indicators that a steward must investigate before deciding whether to update the
runbook.

**Monitored execution** allows the governance agent to execute a defined
governance task and produce an output that is accepted as governance evidence if
it falls within expected parameters, with human review triggered only when the
output is anomalous or exceeds a defined threshold. The "expected parameters"
and the thresholds that trigger human review must be defined in the governance
agent's specification before the agent is deployed at this autonomy level. The
specification must also define what constitutes an anomalous output and what the
escalation path is when anomaly thresholds are breached. Monitored execution is
appropriate for tasks where correctness criteria are well-defined, outputs are
machine-verifiable, and the blast radius of an incorrect output is low to
medium. Examples include: SBOM freshness checks that compare generation date
against the defined freshness threshold; SLO burn rate calculations from
telemetry data; SLSA attestation verification against the defined provenance
requirements; certificate expiry monitoring; and on-call assignment presence
checks against the roster.

**Human-gated execution** covers governance tasks where the governance agent
proposes an action that requires explicit human approval before execution. The
agent may not execute the action autonomously under any circumstances,
regardless of how clear the triggering conditions appear. The agent presents the
proposed action, the triggering evidence, and the reasoning to a named human
authority, and execution proceeds only upon that human's explicit authorisation.
Human-gated execution is appropriate for actions whose consequences are
difficult to reverse, whose blast radius is high, or whose legitimacy depends on
human judgment that cannot be encoded in the agent's specification without
residual ambiguity. Examples include: emergency rollback triggers that the agent
may detect as warranted but may not initiate; specification change proposals
that could alter system scope; release gate condition overrides requested by the
agent on the basis of novel circumstances; and escalation to regulatory
notification where the agent has detected a condition that may require
regulatory disclosure.

---

## Governance Failure Modes Specific to Agent-Assisted Governance

The introduction of agents into governance work creates failure modes that do
not exist in purely human governance processes. These are not theoretical risks
— they are predictable failure patterns that emerge when agent-assisted
governance is implemented without explicit mitigations. Treating them as
compliance concerns to be managed through policy is insufficient; they must be
engineered against.

**Evidence laundering.** An agent assembles an evidence bundle from artefacts it
produced, then validates that bundle using a check it also runs, creating a
closed loop of self-attestation with no independent verification. The result is
a bundle that appears complete and consistent because the agent that produced it
is also the agent that checked it — not because the evidence independently
supports the governance conclusion. Mitigation: at least one verification step
in every evidence bundle must be executed by a process that did not produce the
artefact under review. The Spec Critic Agent should not validate the threat
model that the Threat Model Agent produced without an independent human security
review. The Evidence Bundle Agent should not both assemble the bundle and serve
as the sole validator of its completeness. Independence is not a preference — it
is a structural requirement.

**Approval laundering.** A human signs off on a change by reviewing an
agent-generated summary of the evidence bundle rather than the primary artefacts
themselves. The agent's summary may be accurate. It may also be selectively
framed, incomplete in ways the agent did not detect, or optimistic about
conditions that are borderline. The human sees a coherent, well-organized
summary and signs off — but has not reviewed the evidence that the summary
claims to represent. Mitigation: gate presentation interfaces must surface
primary artefacts — evaluation reports, static analysis outputs, the control
state record, the agentic provenance record — as the default review interface.
Agent-generated summaries are permitted as navigation aids but must not
substitute for primary artefact access. A sign-off that cannot be traced to the
reviewer having accessed the primary artefacts is a suspected laundering event,
not a valid Condition 4 approval.

**Compliance theater.** Governance evaluations and controls are configured to
satisfy an audit checklist rather than to detect failures in this specific
system. The controls run, produce results, and are filed. A reviewer inspecting
the evidence bundle sees green checkmarks. But the controls were never
calibrated to catch the failure modes specific to this system's design — they
were added because the gate requires them. Mitigation: back-test controls. For
any control in the evidence bundle, ask: would this control have detected a
known past failure in this system or a comparable system at a similar autonomy
tier? If not, the control requires recalibration. The independent validator is
responsible for this back-testing, not the team that produced the evidence
bundle.

**Automated rubber-stamping.** As the volume of governance agent outputs
increases, human reviewers begin approving without meaningful inspection. Review
time compresses. The human decision point becomes nominal. Detectable via
review-time distribution metrics: a pattern of very short review times on
complex evidence bundles, or approval without accessing primary artefacts. The
correct response when rubber-stamping is detected is not to add more governance
process — it is to reduce the system's autonomy tier until the oversight signal
quality is restored. A governance system in which humans have nominally retained
accountability but have stopped exercising judgment is not governed; it is
supervised.

These failure modes share a structural property — they produce governance
artefacts that appear correct under casual inspection but fail under adversarial
or incident-driven scrutiny. A governance audit or a production incident that
requires evidence reconstruction will expose them. Building governance agents
without explicitly mitigating these failure modes is not simpler governance; it
is governance theater at a higher level of automation.

---

## Agent Participation by Layer and Gate

### Layer 1 — Demand and Value

Governance agents operate at the advisory level in the demand and value layer.
Their appropriate contributions are: monitoring business metrics and flagging
threshold breaches that suggest a demand item should be raised; synthesising
structured feedback from operational systems into demand signal summaries that
product owners can evaluate; scoring backlog items against documented
prioritisation criteria to surface priority ordering for human review; and
performing pre-linting of draft specifications against gate conditions to
identify likely failures before the gate assessment begins. None of these
contributions constitute a governance determination. The product owner and
business demand sponsor make all prioritisation and validation decisions. Agents
surface evidence; humans validate demand.

### Specification Readiness Gate

Governance agents operate at the advisory level for all Specification Readiness
Gate activities. A governance agent may generate a first-draft threat model from
the specification content — but this draft carries the epistemic label of
agent-proposed and must be reviewed and validated by the security function
before the Technical Readiness Sub-Gate passes. The agent's threat model draft
is an acceleration tool for the security function's review, not a substitute for
that review. Governance agents may also scan draft specifications for missing
constraints against a defined constraint checklist, producing a gap report that
the specification analyst evaluates; and estimate token budgets from model tier
pricing and specification scope for the specification analyst's consideration.
Governance agents may not assess any gate condition as passed. All gate
conditions are assessed by the product owner, specification analyst, or
designated security and architecture reviewer as defined in the sub-gate
structure. An agent output that says a gate condition is satisfied does not make
the condition satisfied.

### Layer 2 — Engineering Execution

Engineering agents are first-class participants in the Layer 2 inner loop as
execution agents, and their role within the loop is governed by the manifesto's
engineering execution principles. Within the loop, governance agents may
additionally perform governance-adjacent tasks that prepare the handoff to Layer
3: flagging specification drift when the current implementation diverges
significantly from the specification as written; generating evidence bundle
components as loop outputs are produced, so that the bundle is substantially
assembled before the loop completes rather than assembled retrospectively; and
proposing Learn-phase knowledge updates from loop outcomes, drafted for the
engineering lead's review. All proposed knowledge updates are reviewed by the
engineering lead before being filed into institutional memory. Governance agents
do not assess inner-loop correctness; they support the evidence infrastructure
that the release gate will verify.

### Layer 3 — Release Gate

At the release gate, governance agents may operate at monitored execution for
evidence verification tasks and at advisory for evidence assembly tasks. The
practical distinction is this: a governance agent may autonomously verify that
an SLSA attestation is cryptographically valid, that the model version recorded
in the evidence bundle matches the model version in the deployment
configuration, that the SBOM was generated within the defined freshness window,
and that the dynamic security scan is present and contains no unresolved High or
Critical findings. These are machine-verifiable conditions with clear
correctness criteria. A governance agent may also assemble the evidence bundle
from loop outputs — collecting the artefacts, verifying their presence and
internal consistency, and producing a structured bundle — but this assembled
bundle carries the label agent-assembled and must be reviewed by the release
manager before any gate condition assessment is made. The release manager
reviews the assembled bundle and makes all gate condition assessments.
Governance agents may not assess any release gate condition as passed. The
release manager's review is not a rubber stamp on the agent's assembly; it is an
independent assessment of whether the assembled evidence is genuinely
sufficient.

### Layer 3 — Deployment

During deployment, governance agents may operate at monitored execution for
canary monitoring activities and must operate at human-gated execution for any
rollback-related actions. A governance agent may monitor canary deployment
metrics against the documented promotion criteria; calculate whether the
observation window conditions are satisfied given current metric values; detect
environment drift against the declared configuration baseline; and alert on
promotion gate condition failures. These monitoring outputs enter the deployment
record as tool-generated or agent-generated artefacts at the appropriate
epistemic tier, visible to the deployment engineer. A governance agent may not
initiate rollback autonomously under any circumstances. When canary metrics
breach the defined rollback trigger criteria, the agent's role is to propose
rollback and present the triggering evidence to the deployment engineer or
release manager, who authorises or declines. The time pressure of a failing
canary deployment does not override the human-gated requirement for rollback. An
agent that initiates rollback without authorisation has exceeded its autonomy
scope regardless of whether the rollback was the correct action.

### Layer 4 — Operations

In the operational layer, governance agents support two distinct workstreams.
The first is incident response: governance agents may reconstruct incident
timelines from distributed traces and logs; correlate incidents with recent
deployments or configuration changes identified in the change record; propose
initial containment actions for incident commander review, labelled as
agent-proposed and requiring explicit human approval before execution; and draft
the incident timeline and contributing factors sections of post-incident reviews
as a starting point for the incident commander's own account. All incident
response decisions — containment, escalation, recovery, and communication — are
made by the incident commander. The agent's proposed containment actions are
advisory inputs, not instructions. Post-incident review action items and
governance artefact updates are human-authored: the agent may draft a starting
structure, but the final record reflects the human team's analysis, not the
agent's reconstruction. The second workstream is continuous governance
monitoring: governance agents may operate at monitored execution for conditions
that are machine-verifiable, including scan recency against defined schedules,
SLO burn rate trajectory calculation, on-call assignment presence against the
roster, runbook modification date against the staleness threshold, and
certificate expiry trajectory against the renewal window.

### Layer 4 — Maintenance

In the maintenance layer, governance agents support vulnerability triage and
steward portfolio management at different autonomy levels. For vulnerability
triage, governance agents operate at the advisory level: they may perform
initial exploitability assessments against the deployment context for newly
disclosed vulnerabilities, model the blast radius of proposed dependency updates
against the system's integration surface, and flag candidate vulnerabilities for
steward review with supporting evidence. All VEX status determinations — whether
a disclosed vulnerability is applicable, not applicable, in triage, or
remediated — are human decisions made by the steward or the designated security
function. An agent-generated exploitability assessment that has not been
reviewed by a qualified human may inform the steward's analysis but may not
serve as the VEX record. For steward portfolio management, governance agents may
operate at monitored execution: they may monitor steward portfolio limits and
flag exceedances to the stewardship coordinator; track SBOM freshness across the
portfolio and flag staleness against the defined threshold; and monitor
re-verification triggers against the criteria defined in each system's
maintenance governance record. All steward assignment decisions, remediation
decisions, and deprecation decisions are human decisions.

---

## Governance Agent Evaluation Requirements

Because governance agents produce evidence that informs governance decisions —
and because incorrect governance evidence can propagate errors through the gate
structures that protect production quality — their evaluation suites must
address failure modes that general engineering agent evaluation does not face.
The evaluation suite for a governance agent must include standard functional
correctness cases and four additional case categories that are specific to
governance contexts.

False positive cases cover inputs that should not trigger a flag or alert but
that a naive governance agent might flag. An evidence bundle that correctly
omits a constraint because the constraint was explicitly declared out of scope
in the specification is not a gap: an agent that flags it as a gap has produced
an incorrect advisory output that directs human attention to a non-problem. In
aggregate, false positive flags erode trust in governance agent outputs and
cause human reviewers to discount genuine flags. Evaluation suites must include
well-formed artefacts that exercise the boundary conditions of what constitutes
a genuine gap versus a documented scope exclusion.

False negative cases cover inputs that should trigger a flag but that a
carefully constructed input might obscure. A specification with a plausibly
worded but unmeasurable success criterion — one that uses quantitative
vocabulary without grounding in a measurement methodology — should trigger a
Condition 2 flag at the specification readiness gate. A governance agent whose
evaluation suite does not include such cases may pass well-constructed but
governance-deficient artefacts without raising a flag. False negative cases are
the higher-risk failure mode in governance contexts: false positives create
noise, but false negatives create undetected governance gaps.

Adversarial governance input cases cover inputs constructed with the intent of
manipulating the governance agent into producing an incorrect assessment. A
threat model that appears comprehensive — uses structured methodology language,
covers the required threat categories, produces plausible mitigation statements
— but omits a critical attack vector through plausible-sounding language at the
relevant section should not satisfy the threat model completeness check. A
governance agent evaluation suite that does not include adversarially
constructed artefacts is not testing the agent against the conditions it will
encounter when the governance workload is high and the cost of a missed flag is
greatest.

Drift detection cases cover scenarios where the governance agent's assessment
should change over time as the governed system's state changes, even without a
new event trigger. A runbook that was current at deployment becomes stale as the
system evolves. A certificate that was valid at last scan becomes a renewal
urgency as its expiry date approaches. A steward portfolio that was within
limits grows beyond them as new systems are assigned. The governance agent must
detect these drift conditions not only in response to events but through
continuous state monitoring against time-varying thresholds. Evaluation suites
must include scenarios that verify drift detection across time-parameterised
conditions.

Governance agent evaluation suites must be updated after every incident in which
a governance agent's output was materially incorrect and contributed to a
governance failure. An evaluation suite that does not incorporate discovered
failure modes from production is not learning from production, and the
governance agent it governs is increasingly untested against its actual
operating environment.

---

## Adversarial Governance Testing

Governance agent evaluation suites test whether the agent produces correct
outputs under known inputs, including adversarially constructed inputs. That is
necessary but not sufficient. The governance system as a whole — the combination
of agents, interfaces, human review steps, and gate structures — must also be
tested for resistance to motivated adversaries: not attackers exploiting
software vulnerabilities, but participants who want to pass gates with lower
evidence quality than the framework requires. These participants may be acting
in good faith under time pressure, may be optimising for delivery velocity at
the expense of governance rigour, or may be deliberately circumventing controls.
The governance system must be tested against all three motivations.

Adversarial governance testing is a scheduled, structured exercise — not an
ongoing monitoring activity and not the same as the adversarial input cases in
governance agent evaluation suites. It must be conducted quarterly. The team
conducting it must include a member with no stake in the systems being governed
and a governance framework author. The output is an adversarial governance test
report, which is filed as a governance artefact and reviewed by the governance
portfolio owner. Any path that the test confirms exists — meaning the test team
was able to execute it end-to-end, or was able to establish that nothing in the
current framework would prevent its execution — must be closed through framework
changes. Documentation of the path without closing it is not an acceptable
response to a confirmed finding.

**Required attack scenarios tested quarterly:**

**Blast radius fragmentation.** A single demand item with Tier 3 aggregate
impact is structured as multiple Tier 2 items to avoid the higher validation
bar. The test confirms whether the governance framework detects this
fragmentation pattern — through specification review, through blast radius
assessment logic, or through gate condition checks — or whether it is possible
to pass the higher-impact work through lower-tier governance by distributing it
across multiple nominally independent items.

**Accountability concentration.** The same named human serves as both the
specification accountable human and the release sign-off authority, combined
with an unusually short approval time. The test confirms whether the governance
framework requires independence between specification accountability and release
approval, and whether approval time metrics are monitored as a signal of
non-genuine review.

**Waiver accumulation path.** Multiple individually valid waivers are identified
and combined. The test confirms whether there is a mechanism that detects when
the aggregate of valid individual waivers produces a system operating in an
effectively ungoverned state — where each waiver was legitimately granted but
their combination removes controls that no single waiver would have removed.

**Evidence laundering path.** A governance agent produces an artefact and the
same agent, or a closely coupled agent in the same pipeline, serves as the
validator of that artefact. The test confirms whether the independence
requirement for evidence validation is enforced structurally — by the governance
infrastructure — or relies on human reviewers noticing the dependency.

**Approval laundering path.** An evidence bundle is constructed where a human
technically has access to primary artefacts but the governance agent's summary
is the default presented view. The test confirms whether the approval interface
requires the reviewer to access and interact with primary artefacts before
sign-off is possible, or whether it is structurally possible to approve by
reviewing only the agent's summary.

---

## Organizational Memory — Multi-Tier Memory Architecture

Governance agents operate with access to a structured, four-tier memory
architecture. Each tier serves a distinct cognitive function, is a governed
artefact in its own right, and is subject to the same accountability
requirements that apply to all governance artefacts: versioned, with a named
steward, and auditable. The foundational governance rule for all tiers is that
memory is advisory input, not binding precedent. No gate condition can be
satisfied by memory alone. Memory directs human attention and informs agent
assembly; humans make determinations.

Every entry in every memory tier must record three provenance fields: the
evidence that produced the entry (what artefacts, events, or analyses the entry
was derived from); the date the entry was recorded; and a staleness trigger — a
defined class of events that would render the entry incorrect or outdated. An
entry without a staleness trigger cannot be reliably maintained, because there
is no basis on which to decide whether it remains valid. Stewards are
responsible for reviewing entries when their staleness triggers fire.

**Episodic memory** records specific past events with their full context:
individual gate failures, incident root causes, waiver grants with their stated
rationale and subsequent outcomes, and blast radius assessment precedents for
specific system types and architecture classes. Episodic memory is queryable by
similarity and by system or specification type — not only by identifier — so
that agents can surface patterns such as: "this class of specification has been
attempted three times; here is what each loop learned." Each episodic entry
records: the event itself; the system context at the time (phase, autonomy tier,
architecture class); the governance decision made; and the observed outcome.
Episodic memory is the factual substrate from which the other long-term memory
tiers are derived.

**Semantic memory** encodes accumulated domain knowledge: regulatory
interpretations that have been internally litigated and settled, threat model
patterns that recur across the organisation's system types, architectural
constraints and the rationale behind them, and technology-specific constraint
patterns that inform specification quality. Semantic memory is broader than a
catalogue of governance patterns — it is the organisation's encoded
understanding of its technical and regulatory domains. Entries in semantic
memory are derived from episodic memory through explicit curation, from
regulatory and standards documents, and from subject-matter expert review.
Semantic memory entries must identify the episodic or external sources from
which they were derived; an entry that cannot be traced to a source is
conjecture, not knowledge.

**Procedural memory** records learned patterns for executing governance work
effectively: which specification patterns lead to clean gate passes for which
system types; which evaluation approaches produce the best coverage for which
risk profiles; which constraint identification sequences catch the most defects
at specification stage rather than at release. Procedural memory is derived from
episodic memory through systematic pattern analysis — it is the mechanism by
which past experience improves future governance execution quality. Procedural
memory entries must be reviewed whenever the episodic base from which they were
derived changes materially enough that the derived pattern may no longer hold.

**Working memory** is the context assembled for a specific loop iteration or
gate assessment from the three long-term memory tiers. It is ephemeral: working
memory is assembled at the start of a task, used during it, and then decomposed.
Durable outputs — any new episodic entries generated during the task, any
procedural pattern updates suggested by the task's outcome — are written back to
long-term memory at completion, subject to steward review. A working memory
assembly record must be retained: what was retrieved from each long-term tier,
for which task, and what was written back.

Access to any memory tier by governance agents must be disclosed in gate
decision records where memory was used as input. The disclosure must be
specific: which entries were surfaced, from which tier, for which conditions,
and by which agent. This disclosure enables reviewers to evaluate whether the
memory that informed a decision was appropriate, current, and accurately
characterised, and enables the organisation to identify when memory is being
over-relied upon as a substitute for current evidence.

---

## Multi-Agent Governance Coordination

When multiple governance agents operate simultaneously on the same system — a
vulnerability triage agent and a dependency update impact agent active
simultaneously, or a release evidence assembly agent and an SLSA attestation
verification agent running in parallel for the same release — their outputs must
be coordinated before presentation to the governance worker who will use them.
Coordination is necessary because governance workers must be able to form a
coherent view of the system's governance state; fragmented outputs from multiple
agents that have not been reconciled require the governance worker to perform
coordination work that the agent infrastructure should have performed.

When governance agents produce conflicting assessments of the same condition —
one agent assesses a specification constraint as satisfied, another flags it as
deficient — the conflict must be surfaced to the governance worker with the
reasoning on both sides visible. The agents must not resolve the conflict
between themselves, and a coordinating agent must not resolve it silently by
selecting one assessment over the other. Conflicting governance assessments are
information: they indicate a condition where the correctness criteria are
ambiguous, the inputs to the agents differed, or one agent has a deficiency in
its evaluation logic. That information is most valuable to the governance worker
and the team responsible for the governance agent's evaluation suite when it is
visible, not when it has been silently arbitrated by the infrastructure.

A governance agent orchestrator may aggregate outputs from multiple governance
agents into a unified view for the governance worker. It may identify when
assessments are consistent across agents, when they are independent and
non-overlapping, and when they conflict. It may present the aggregated view with
appropriate epistemic labelling for each component. It may not resolve
substantive disagreements between governance agents by choosing one assessment
over another. Orchestration is a presentation function; it is not a decision
function. Any orchestration logic that selects between conflicting governance
agent outputs without surfacing the conflict to a human has introduced a hidden
decision into the governance process — one that has no accountability anchor and
no audit trail.

### Multi-Agent Composition Governance

When Agent A — at autonomy tier T_A with blast radius ceiling B_A — orchestrates
Agent B — at autonomy tier T_B with blast radius ceiling B_B — the **composed
autonomy tier** and **composed blast radius** of the pipeline must be assessed
before the composition is authorised for deployment.

The composition rules are as follows. The composed autonomy tier equals the
maximum of T_A and T_B: the pipeline as a whole operates at the highest tier of
any component agent, because the highest-autonomy agent's actions are a
reachable consequence of deploying the pipeline. The composed blast radius is
the cumulative impact of both agents' maximum credible actions taken together —
not the maximum of the two individually, because the agents can act in sequence
and their effects can compound. The composed tool permission set is the union of
both agents' individual tool permission sets, which may exceed either agent's
individually authorised scope.

If the composed autonomy tier or blast radius exceeds the authorization
reflected in the orchestrating agent's specification, the composition requires a
specification change and a new evaluation run before deployment. The
orchestrating agent's specification was written for the orchestrating agent
alone; it does not automatically extend to cover the behaviors that become
reachable through the sub-agent.

Tool permission escalation via composition is a governance violation regardless
of the individual agents' authorizations. An orchestrating agent that calls a
sub-agent to access tools the orchestrating agent is not authorized to use
directly is operating outside its specification, whether or not the sub-agent is
individually authorized to use those tools. The governance graph's tool manifest
record must reflect the composed tool permission scope for every multi-agent
pipeline — not the individual permissions of each component agent in isolation.

Before any multi-agent pipeline is deployed at monitored execution autonomy or
above, a **composition record** must be filed as a governance artefact. The
composition record names: all component agents, each with its individual
autonomy tier, blast radius, and tool set; the composed tier, blast radius, and
tool set derived from the composition rules above; the accountable human for the
composed system; and the evaluation evidence demonstrating that the composition
behaves correctly at its composed tier. The composition record is distinct from
each component agent's own specification: it is the governance record for the
pipeline as a system, not for the agents as individuals.

---

## Normative References

- NIST AI Risk Management Framework 1.0 (NIST AI 100-1, 2023):
  https://doi.org/10.6028/NIST.AI.100-1 — the GOVERN, MAP, MEASURE, MANAGE
  vocabulary used throughout this document.
- NIST AI RMF Generative AI Profile (NIST AI 600-1, 2024):
  https://doi.org/10.6028/NIST.AI.600-1 — generative-system risk profile.
- NIST AI RMF Playbook: https://www.nist.gov/airmf-resources/playbook/ —
  living set of suggested actions aligned to the four functions.
- ISO/IEC 5338:2023, *Information technology — Artificial intelligence — AI
  system life cycle processes*: https://www.iso.org/standard/81118.html.
- ISO/IEC 42001:2023, *AI management systems*:
  https://www.iso.org/standard/42001 — Section 6 covers organizational roles
  and responsibilities for AI management.
- ISO/IEC 23894:2023, *Artificial intelligence — Guidance on risk management*:
  https://www.iso.org/standard/77304.html.
- EU AI Act Article 9 — risk management system for high-risk AI.
- NIST SP 800-218 v1.1 (SSDF) — RS practice group for vulnerability response
  governance: https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SP 800-218A, *Secure Software Development Practices for Generative AI
  and Dual-Use Foundation Models* (2024):
  https://doi.org/10.6028/NIST.SP.800-218A — AI-specific SSDF community
  profile.
- IEEE P3394 — Ethical Governance of Autonomous and Intelligent Systems (in
  development; monitor for maturity).

### Empirical evidence base

- Perry et al., *Do Users Write More Insecure Code with AI Assistants?* (ACM
  CCS 2023, https://arxiv.org/abs/2211.03622) — primary empirical support for
  the rubber-stamping failure mode in *Governance Failure Modes Specific to
  Agent-Assisted Governance*. Users with AI assistance produced less secure
  code while reporting higher confidence; the analogous risk in governance
  is that human reviewers endorse agent-proposed governance artefacts more
  readily than they would have endorsed an unaided draft.
- Debenedetti et al., *AgentDojo* (2024, https://arxiv.org/abs/2406.13352) —
  task-and-tool environment underwriting the adversarial governance input
  requirement in *Governance Agent Evaluation Requirements*.

---

_Governance agents do not remove the need for governance judgment — they make
governance judgment possible at scale. The human governance workload in an
organisation operating dozens of agentic systems simultaneously cannot be
carried by human effort alone without degrading into rubber-stamping. The answer
to that pressure is not to lower the governance standard. It is to equip human
governance workers with agents that produce reliable evidence, monitor
conditions continuously, and surface findings precisely — so that the human's
attention is directed to the decisions that require it, not consumed by the
collection of evidence that agents can produce more quickly, more consistently,
and at lower cost._
