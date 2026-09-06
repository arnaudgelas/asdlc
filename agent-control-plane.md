# Agent Control Plane — ASDLC Cross-Cutting

_The catalog of named governance agents, their schemas, and their human decision
points._

See [Governance Agents](governance/agents.md) for the governance agent framework
and epistemic tiers. See [Governance Graph](governance/graph.md) for the
semantic model these agents operate on. See
[Governance Queries](governance/queries.md) for the questions these agents
answer.

---

## What the Agent Control Plane Governs

The governance/agents.md framework establishes the principles by which agents
may participate in governance work: the four epistemic tiers that label every
governance artefact, the three autonomy classifications — advisory, monitored
execution, and human-gated — that define how much autonomous authority an agent
may exercise, the structural requirement that governance agents are themselves
agentic systems governed by the ASDLC and not exempt from it, and the
layer-by-layer model that maps governance task types to appropriate autonomy
levels. What the framework does not do is name the specific agents that
organisations implementing the ASDLC should instantiate. That is the function of
the Agent Control Plane. The Control Plane is an operational catalog: it names
each governance agent, defines its governing schema, and specifies the human
decision point that caps each agent's autonomy, connecting the principles of the
framework to the concrete systems an organisation must build and govern.

A governance agent schema is not a software architecture specification — it is a
governance specification. It defines what the agent is permitted to consume,
produce, and act on; what it may never touch regardless of context or
instruction; who is accountable for its behaviour; and under what conditions a
human must be in the loop before an output may serve as governance evidence or
an action may be taken. Organisations implement these agents in whatever agentic
framework fits their infrastructure. The ASDLC defines the governance contract,
not the implementation. The governance contract is what makes the agent's
behaviour auditable: when a gate decision record references an agent output, the
schema in this catalog establishes what that agent was and was not permitted to
do, what level of human review is required before the output carries governance
weight, and who owns the accountability for the agent's actions.

Each agent named in this catalog is a governed system in its own right. It
requires its own ASDLC specification — with the agent's governance task as the
business need, its blast radius assessed against the worst case of acting on an
incorrect output, and its permission scope as a documented constraint. It
requires its own evaluation suite, including false positive, false negative,
adversarial governance input, and drift detection cases as defined in
governance/agents.md. It requires a named accountable human and a named steward
assigned before deployment, not after. And it requires a kill switch that has
been tested before the agent operates in a production governance context. Adding
a governance agent to the Control Plane is itself a governed loop iteration. It
is not an informal deployment, and an organisation that treats it as such has
introduced an ungoverned agent into the systems that protect all its other
agentic work.

---

## Agent Schema Structure

Every agent named in this catalog carries a fixed set of schema fields. The
fields are not optional; an agent whose schema omits any of them has not been
fully specified for governance purposes, and the omission must be resolved
before the agent is deployed. The fields are defined here once and applied
consistently across all named agents.

The **agent_id** is a stable identifier for the agent across versions. It is
used in governance graph edges — specifically the generated_by edge — to record
which agent produced a given artefact. The agent_id persists across version
increments; a new version of the same agent carries the same identifier with an
updated version suffix. When an organisation replaces one agent with a
substantively different agent performing the same governance task, a new
agent_id is assigned, because the governance provenance of artefacts produced by
the old agent must remain traceable to the old agent's specification.

The **purpose** is a single sentence stating the governance task the agent
performs. It is not a description of the agent's capabilities or its technical
implementation — it is a statement of what governance work the agent exists to
do. The purpose statement is what an organisation consults when deciding whether
to invoke this agent for a given situation, and it is what a reviewer reads when
interpreting the agent's output in a gate decision record. Purpose statements
that are too broad — covering multiple distinct governance tasks — indicate that
an agent is under-specified and may be operating beyond a clearly bounded scope.

The **allowed_inputs** field enumerates the governance artefact types and data
sources the agent may consume, referenced by governance graph node types where
applicable. The allowed_inputs field is a permission boundary: the agent may not
consume artefact types or data sources that are not on this list, regardless of
whether they are available in the operating environment. This boundary is
material to blast radius assessment — an agent whose inputs include production
system configurations has a different blast radius profile from one whose inputs
are limited to read-only specification documents — and it is what the agent's
accountable human uses to verify that the agent has operated within its defined
scope.

The **allowed_tools** field enumerates the capability categories the agent may
invoke, described by capability function rather than tool name or vendor.
Acceptable categories include structured data query (read-only), web content
retrieval, text synthesis, document analysis, cryptographic hash verification,
schema validation, timeline assembly, trend calculation, and anomaly detection.
Describing capabilities rather than tools ensures the governance contract
remains stable as the underlying tooling changes, and prevents the schema from
encoding implicit vendor dependencies. An agent that invokes a capability not on
its allowed_tools list has acted outside its specification, and the output of
that invocation may not be accepted as governance evidence.

The **forbidden_tools** field enumerates capability categories that are
explicitly prohibited. These are not default-off capabilities that the agent
simply has not been granted — they are actively blocked, and the prohibition is
documented so that any circumvention is visible as a specification violation.
The distinction matters for audit purposes: if a capability is absent from the
allowed_tools list but not present in the forbidden_tools list, its status is
ambiguous; if it is present in the forbidden_tools list, any invocation is
unambiguously out of scope. Prohibited categories for governance agents
typically include direct writes to production systems, modification of
accountability records, deletion of governance artefacts, and issuance of
binding governance determinations that the schema assigns to a human.

The **data_access_classification** field records the maximum data sensitivity
level the agent may access, as defined by the organisation's data classification
policy. Governance agents that must access operational telemetry, incident logs,
or deployment configurations may require access to internal-sensitive data;
agents that access user research repositories may require access to data subject
to the organisation's privacy classification controls. The
data_access_classification establishes the upper bound: an agent specified at
internal-sensitive may not access data classified as confidential or restricted,
regardless of whether those data sources would improve the agent's output
quality.

The **autonomy_tier** records the agent's assigned autonomy level — advisory,
monitored execution, or human-gated — as defined in governance/agents.md. This
field applies to the agent's primary function; where an agent operates at
different autonomy levels for distinct subtasks, each subtask's autonomy tier is
documented in the approval_required_for field. Upgrading an autonomy tier
requires a specification change, a new evaluation suite run, and explicit
approval from the accountable human. The autonomy_tier in the schema is the
agent's authorised level, not its demonstrated capability level; the two may
differ, and where they do, the schema governs.

The **approval_required_for** field specifies the particular outputs or actions
for which the agent must pause and obtain explicit human approval before either
filing the output as governance evidence or proceeding with the next action.
This field operationalises the human decision point for each agent and is what
the accountable human and steward monitor to confirm that the agent is not
bypassing required review steps. The field must be specific enough to implement
as a runtime checkpoint: a statement that "approval is required for significant
outputs" is not a specification; a statement that "approval is required before
any evidence summary is filed to the governance graph as a DemandItem input" is.

The **output_artifacts** field records the governance graph node types the agent
produces, connected via generated_by edges. This field makes the agent's
contribution to the governance graph traceable: when a reviewer inspects a
governance graph node, the agent that produced it and the schema under which it
operated can be retrieved from this record. Output artefacts that have not yet
received human endorsement carry the agent-proposed epistemic label; artefacts
endorsed by a qualified human reviewer carry the agent-proposed, human-reviewed
label and reference the reviewer's identity and the date of endorsement.

The **logging_required** field is set to yes for all governance agents without
exception. Every input consumed, every output produced, every tool call invoked,
and every approval requested or granted must be logged with a timestamp and the
agent version that was active at the time of the event. This log is not an
operational convenience — it is the audit record that makes the agent's
behaviour reviewable. Without it, the agent's accountability chain has a
structural gap: the governance artefacts it produces cannot be traced to the
specific inputs that generated them, and the human decision points it is
supposed to enforce cannot be verified as having been enforced.

The **kill_switch** field documents the mechanism by which the agent can be
halted immediately — stopping all active invocations and preventing new
invocations until the switch is explicitly reset. The kill switch mechanism must
be documented in the agent's specification, tested before the agent enters
production, and accessible to the accountable human and the steward without
requiring access to the agent's internal implementation. The existence and
tested status of the kill switch is a required field in the agent's governance
record; an agent deployed without a tested kill switch has not satisfied the
deployment requirements for governance agents regardless of how well it performs
its primary governance task.

The **owner** field names the HumanOwner role accountable for the agent's
behaviour. This is the individual who accepts accountability for what the agent
does, who reviews anomalous outputs, who authorises autonomy tier upgrades, and
who is named in the governance log as the responsible party when the agent's
output is used in a gate decision record. The owner role is defined by
functional responsibility — product owner, security function lead, release
manager — not by organisational hierarchy, because governance accountability
must be attached to the role that has the expertise to assess the agent's
outputs, not simply the role with the highest seniority.

---

## Named Governance Agents

### Demand Evidence Agent

**agent_id:** demand-evidence-agent

**purpose:** Collects and structures evidence for demand item validation — user
research signals, operational metric anomalies, regulatory publications, and
business outcome gaps — and presents it to the product owner and business demand
sponsor for sufficiency assessment.

**allowed_inputs:** Operational observability data (SLO records, output quality
records, cost anomaly records — read-only); published regulatory and standards
updates (web-accessible); user feedback repositories (read-only); existing
demand backlog (read-only); governance graph DemandItem nodes.

**allowed_tools:** Structured data query (read-only); web content retrieval;
text synthesis for evidence summaries.

**forbidden_tools:** Direct modification of the demand backlog; creation of
DemandItem nodes; web publishing; write access to any governance artefact
without human approval.

**data_access_classification:** Up to internal-sensitive. No personal data
access without explicit DPIA clearance.

**autonomy_tier:** Advisory.

**approval_required_for:** Every evidence summary submitted as input to a demand
validation decision. The product owner and business demand sponsor assess
sufficiency; the agent does not.

**output_artifacts:** EvidenceArtifact nodes (demand signal summaries, labeled
agent-proposed, pending product owner and business demand sponsor review).

**logging_required:** Yes.

**kill_switch:** Documented and tested before production deployment. Accessible
to the product owner and system steward.

**owner:** Product owner.

The Demand Evidence Agent addresses a practical constraint in organisations
operating multiple agentic systems simultaneously: the volume of operational
signals, regulatory publications, and user feedback that must be monitored to
identify genuine demand items exceeds what any product owner can track manually
without priority filtering. The agent's function is to perform that filtering —
collecting signals across the permitted sources, structuring them into summaries
that identify what changed and why it might represent a demand item, and
presenting those summaries with supporting evidence to the product owner for
assessment. The agent does not determine that a demand item exists; it assembles
the evidence a product owner needs to make that determination with confidence
rather than intuition.

The boundary between the agent's function and the human's function is precisely
located at the sufficiency determination. The product owner and business demand
sponsor must assess whether the evidence the agent has assembled is sufficient
to warrant creating a DemandItem node and initiating the specification readiness
process. This assessment requires judgment that the agent cannot perform:
whether the evidence represents a genuine gap versus a transient anomaly,
whether the business context makes this gap a priority given competing demands,
and whether the regulatory signal is directly applicable to the organisation's
obligations or is a general publication without immediate binding effect. The
agent's evidence summary is the input to that judgment; the human's assessment
is the governance event that produces a governance artefact.

The human decision point is placed at evidence sufficiency rather than at a
later stage because demand validation is the point at which the organisation
commits to investing a full loop iteration in a direction. An incorrectly
assessed demand item — one built on insufficient evidence — can propagate
through the specification readiness gate and into loop execution before the
inadequacy of the original evidence becomes apparent. By placing the decision
point at sufficiency assessment and requiring the product owner and business
demand sponsor to accept the evidence before it enters the governance record,
the governance structure ensures that the downstream commitment is grounded in
evidence that at least two governance-accountable humans have found credible.

---

### Spec Critic Agent

**agent_id:** spec-critic-agent

**purpose:** Pre-lints draft specifications against gate conditions, flagging
structural gaps — missing threat model, unmeasurable success criterion, absent
out-of-scope declarations, token budget absent for Tier 2 and above — before
formal gate assessment begins.

**allowed_inputs:** Draft specifications (read-only); gate condition
definitions; constraint checklist; governance graph Specification nodes (prior
versions, for lineage comparison, read-only).

**allowed_tools:** Structured document analysis; constraint checklist execution.

**forbidden_tools:** Modification of the specification; creation of gate
decision records; write access to the gate decision log.

**data_access_classification:** Up to internal-sensitive.

**autonomy_tier:** Advisory.

**approval_required_for:** All lint reports before they are filed as
agent-proposed pre-assessment inputs. The specification analyst reviews and may
override any flag before the report enters the governance record.

**output_artifacts:** EvidenceArtifact nodes (pre-lint reports, labeled
agent-proposed, pending specification analyst review).

**logging_required:** Yes.

**kill_switch:** Documented and tested before production deployment. Accessible
to the specification analyst and system steward.

**owner:** Specification analyst.

The Spec Critic Agent exists because human reviewers performing gate assessments
under time pressure will find the mechanical defects in a specification — the
absent section heading, the success criterion without a baseline, the threat
model referenced but not attached — but they will find them during the gate
session, consuming time that could be spent on the substantive assessments that
require human judgment. The agent performs the mechanical check before the
session: it compares the draft specification against the gate condition
definitions, identifies the structural elements that are absent or structurally
incomplete, and produces a report that the specification analyst can review and
use to direct remediation before the formal gate. A gate session that begins
with the specification's mechanical completeness already verified can focus the
available human attention on Condition 1 (is the business need genuinely
validated?), Condition 2 (is the success criterion genuinely measurable?), and
Condition 4 (is the threat model substantively adequate?) — the conditions where
human judgment is irreplaceable.

The agent's scope is explicitly limited to structural and mechanical checks. It
can determine that no threat model section is present, or that the present
section does not include all required threat categories in its table of
contents. It cannot determine whether the threat model's proposed mitigations
for the threats it does identify are adequate — that determination requires the
security function's domain expertise. The distinction is between the presence of
a required element and the quality of that element. The agent checks presence;
humans assess quality. This boundary is not a limitation of the agent's
capability — it is a governance design choice. An agent that assessed the
quality of a threat model would be performing the security function's role, with
advisory epistemic status that could nonetheless shape the security function's
review if presented without appropriate labeling.

The specification analyst's role in reviewing the lint report is not clerical
endorsement. The analyst examines each flag the agent has raised and makes an
independent determination: does this flag identify a genuine gap, or does the
specification address the condition in a way the agent's pattern matching did
not recognize? The analyst may override flags where the specification satisfies
the condition through a non-standard but valid approach. The analyst may also
add flags for gaps the agent did not detect — the agent's mechanical check
supplements the analyst's review; it does not replace it. When the lint report
is filed into the governance record, it reflects the analyst's endorsed view of
the pre-assessment state of the specification, not the agent's raw output.

---

### Threat Model Agent

**agent_id:** threat-model-agent

**purpose:** Produces first-draft STRIDE-based and OWASP LLM Top 10-scoped
threat models from specification content, for security function review and
validation.

**allowed_inputs:** Approved specification (read-only); governance graph Risk
nodes (prior threat models for this system type, read-only); constraint
inventory (read-only).

**allowed_tools:** Structured document analysis; threat model template
instantiation.

**forbidden_tools:** Modification of the threat model after security function
review commences; write access to Risk nodes in the governance graph without
human approval.

**data_access_classification:** Up to internal-sensitive.

**autonomy_tier:** Advisory.

**approval_required_for:** The complete threat model before it is accepted as
meeting the Technical Readiness Sub-Gate's threat modeling requirement. The
security function validates: scope completeness (all required categories
addressed per specification-readiness.md Condition 4), residual risk level for
each category, and whether any category warrants a blocking decision before gate
entry.

**output_artifacts:** EvidenceArtifact nodes (threat model draft, labeled
agent-proposed, pending security function review).

**logging_required:** Yes.

**kill_switch:** Documented and tested before production deployment. Accessible
to the security function lead and system steward.

**owner:** Security function lead.

The Threat Model Agent addresses the most time-intensive mechanical component of
the Technical Readiness Sub-Gate: the initial structuring of the threat model.
The ASDLC's Condition 4 requirements define a specific minimum scope for agentic
threat models — thirteen threat categories, each requiring either a concrete
mitigation or a justified out-of-scope declaration. Producing an initial draft
that applies this structure to the specific specification content, maps the
agent's interfaces and data flows to the relevant threat categories, and
instantiates the threat model template with the specification's constraint
context is work that the agent performs faster and more consistently than a
human starting from a blank document. The security function's review then begins
from a structured, populated draft rather than from nothing, which is a
different — and more productive — kind of review.

The agent's output is explicitly a draft for review, and this labeling is not a
formality. The threat model draft produced by the agent is agent-proposed in the
epistemic tier hierarchy defined in governance/agents.md. It may not be filed as
satisfying the gate condition without security function review, regardless of
how comprehensive the draft appears. The reason is architectural: a threat model
that appears comprehensive but omits a critical attack vector through
plausible-sounding language is indistinguishable from a genuinely comprehensive
threat model when evaluated only by the structural checks the agent can perform.
The security function's review is what makes the distinction — it is the domain
expertise that can assess whether the proposed mitigation for prompt injection
is adequate for this specific agent's retrieval surface, not merely whether the
prompt injection category is present with a mitigation statement. The presence
of a mitigation statement is what the Spec Critic Agent checks; the adequacy of
the mitigation is what the security function assesses.

The human decision point is placed at the security function's validation of the
complete threat model because the blast radius of an inadequate threat model is
the blast radius of all the vulnerabilities the threat model failed to surface
before the loop ran. In agentic systems at Tier 2 and above, where the threat
model is a required gate condition component, a superficially adequate threat
model that the security function has not independently validated could allow a
system with an unaddressed attack surface to proceed through the gate and into
production. The security function's validation is not a post-hoc review of what
the agent produced; it is the accountability event that converts a structured
draft into a governance artefact — and the security function lead, as the
agent's owner, is accountable for ensuring that review is substantive rather
than expedient.

---

### Compliance Mapper Agent

**agent_id:** compliance-mapper-agent

**purpose:** Maps specification constraints to applicable regulatory
requirements and standards, identifying which constraints satisfy which
obligations and which obligations may remain unaddressed.

**allowed_inputs:** Specification constraints (read-only); organisational
regulatory obligation register (read-only); standards reference library
(read-only); governance graph Constraint nodes (read-only).

**allowed_tools:** Structured document analysis; regulatory text retrieval
(read-only).

**forbidden_tools:** Modification of the regulatory obligation register;
issuance of compliance determinations; write access to Constraint nodes without
human approval.

**data_access_classification:** Up to internal-sensitive.

**autonomy_tier:** Advisory.

**approval_required_for:** All compliance mappings before they are filed as
governance evidence. The compliance function validates the mapping and
determines whether any gaps require specification revision before gate entry.

**output_artifacts:** EvidenceArtifact nodes (compliance mapping, labeled
agent-proposed, pending compliance function review).

**logging_required:** Yes.

**kill_switch:** Documented and tested before production deployment. Accessible
to the compliance function lead and system steward.

**owner:** Compliance function lead.

The Compliance Mapper Agent performs the cross-reference work between the
specification's constraint inventory and the organisation's regulatory
obligation register — a task that is both essential to the Technical Readiness
Sub-Gate and structurally repetitive across specifications in the same
regulatory domain. For an organisation operating in a regulated sector where
each specification that touches customer data or decisioning logic must
demonstrate coverage of applicable data protection, financial services, or
sector-specific AI regulation obligations, the agent provides a consistent
first-pass mapping: each obligation in the register is checked against the
constraint inventory, and obligations for which no constraint is present or for
which the constraint coverage is ambiguous are flagged for compliance function
review. The agent does not determine whether the coverage is adequate; it
identifies where coverage is present, where it is absent, and where the
relationship between constraint and obligation requires human interpretation.

The distinction between mapping and determination is the operative governance
boundary. A compliance mapping that says "Constraint C-4 references data
minimisation obligations and appears to address GDPR Article 5(1)(c) for the
data flows described in the specification" is a proposed mapping — it is the
agent's interpretation of the relationship between a constraint statement and a
regulatory text. Whether that interpretation is correct, whether the constraint
as written actually satisfies the obligation as applied to the specific
processing activities described in the specification, and whether the mapping
covers all the obligations that apply given the full regulatory context of the
organisation's jurisdiction and sector — these are determinations that require
the compliance function's legal and regulatory expertise. The agent surfaces the
proposed relationship; the compliance function validates or revises it.

The human decision point is placed at the compliance function's validation
because compliance determinations carry legal and regulatory consequences. An
agent-proposed compliance mapping that is filed as a gate condition artefact
without compliance function review is, in a governance sense, a compliance
determination made without a qualified human. The regulatory frameworks that
govern AI systems in financial services, healthcare, and public administration
do not recognise AI-generated compliance assessments as substitutes for human
professional judgment; and an organisation that relies on an unreviewed agent
mapping to satisfy a compliance gate condition has created an accountability gap
that could not be resolved in the event of regulatory scrutiny. The compliance
function lead's endorsement of the mapping converts it from an advisory input
into an accountable governance artefact.

---

### Evidence Bundle Agent

**agent_id:** evidence-bundle-agent

**purpose:** Assembles the release evidence bundle from loop outputs, governance
graph query results, and machine-verifiable checks; validates completeness
against the required schema; and presents the assembled bundle to the release
manager for review.

**allowed_inputs:** Loop outputs and artefacts (read-only); governance graph
nodes relevant to the release (all node types, read-only); SLSA provenance
attestations; SBOM; model version records; deployment configuration (read-only).

**allowed_tools:** Structured data query; cryptographic hash verification; SLSA
attestation verification; schema validation; document assembly.

**forbidden_tools:** Modification of any artefact in the evidence bundle;
creation of gate decision records; issuance of release approval; write access to
the approved_by edge in the governance graph.

**data_access_classification:** Up to internal-sensitive.

**autonomy_tier:** Monitored execution (for machine-verifiable checks); advisory
(for bundle assembly and completeness assessment).

**approval_required_for:** The assembled evidence bundle before the release gate
assessment begins. The release manager reviews the bundle, verifies the
agent-proposed completeness assessment, and makes all gate condition
determinations.

**output_artifacts:** EvidenceArtifact nodes (assembled bundle with completeness
report, labeled agent-assembled with human review required; individual
machine-verifiable check results labeled monitored-execution).

**logging_required:** Yes.

**kill_switch:** Documented and tested before production deployment. Accessible
to the release manager and system steward.

**owner:** Release manager.

The Evidence Bundle Agent performs the collection and assembly work that would
otherwise require the release manager to retrieve artefacts from multiple
sources, verify their consistency, and confirm their completeness against the
release gate schema before the assessment can begin. This assembly work is
well-suited to monitored execution for its machine-verifiable components — the
agent can confirm that an SLSA attestation is cryptographically valid, that the
model version recorded in the evidence bundle matches the model version in the
deployment configuration, that the SBOM was generated within the defined
freshness window, and that the dynamic security scan is present and shows no
unresolved findings at the gate's blocking severity level. These checks have
clear correctness criteria, produce binary outcomes, and are reproducible: the
agent either finds the attestation valid or it does not, and the log records
what it found and when.

The bundle assembly function operates at the advisory tier because the
completeness assessment — the determination that the assembled bundle contains
everything required for the gate — requires more than mechanical checking. It
requires reading each artefact against the gate conditions and assessing whether
the content of the artefact is substantively sufficient, not only whether the
artefact is present. A threat model that is present in the bundle but was
produced without security function review, a success criterion that is stated in
the specification but was not verified against the deployed system, a blast
radius assessment that was assessed at gate entry but has not been updated after
a scope change during the loop — these gaps are not detectable by a mechanical
presence check. The release manager's review of the assembled bundle is what
distinguishes a genuinely complete bundle from a structurally complete one.

The human decision point is placed at the release manager's review of the
assembled bundle, and this placement is precise: the release manager reviews the
bundle and makes all gate condition assessments before any gate condition is
recorded as passed. The agent's assembly and completeness report are a
preparation function — they ensure the release manager begins the gate session
with the evidence organised, the machine-verifiable checks already executed, and
the structural completeness assessed. The release manager's gate session is then
spent on the substantive assessments: are the acceptance criteria actually met
by the evidence? Is the threat model adequate for the blast radius of this
release? Is the evidence of business value sufficient for a go decision? The
release manager's sign-off is the accountability event; the agent's assembly is
the preparation that makes that accountability event tractable.

---

### FinOps Agent

**agent_id:** finops-agent

**purpose:** Monitors inference costs and production economics against forecast,
surfaces unit-cost trends and cost anomalies, and proposes optimisation
candidates for budget owner review.

**allowed_inputs:** CostRecord nodes (read-only); token consumption logs
(read-only); model pricing records (read-only); specification cost forecasts
(read-only); optimisation pattern catalog (read-only).

**allowed_tools:** Structured data aggregation; trend calculation; anomaly
detection.

**forbidden_tools:** Modification of cost records; unilateral changes to model
routing policy; write access to Specification nodes; direct communication with
model providers.

**data_access_classification:** Up to internal-sensitive.

**autonomy_tier:** Monitored execution (for anomaly detection and alert
generation); advisory (for optimisation proposals).

**approval_required_for:** All optimisation proposals before they are acted on.
Proposals that require specification changes must enter the specification
readiness process through the Spec Critic Agent before action. Cost anomaly
alerts fire at monitored execution autonomy; the budget owner determines the
response.

**output_artifacts:** EvidenceArtifact nodes (cost reports, anomaly alerts
labeled monitored-execution; optimisation proposals labeled agent-proposed);
CostRecord nodes (updated with actual-versus-forecast comparison).

**logging_required:** Yes.

**kill_switch:** Documented and tested before production deployment. Accessible
to the economics owner and system steward.

**owner:** Economics owner, as defined in finops-governance.md.

The FinOps Agent addresses the operational economics monitoring function
described in finops-governance.md, providing continuous comparison of actual
inference costs against the forecasts established in approved specifications.
The agent aggregates cost records across the governed systems in its scope,
calculates unit-cost trends at the granularity defined in the organisation's
cost governance policy, and applies anomaly detection logic to identify cost
events that deviate from forecast beyond the defined tolerance threshold. When
an anomaly is detected, the agent generates an alert at monitored execution
autonomy — the alert itself requires no human approval before it is filed as a
CostRecord update and surfaced to the budget owner — because cost anomaly alerts
exist to direct human attention to a condition, not to authorise a response. The
budget owner receives the alert and decides how to respond.

The distinction between alert generation and optimisation proposal reflects the
difference in blast radius between the two functions. A cost anomaly alert that
incorrectly identifies a non-anomalous cost pattern as anomalous directs the
budget owner's attention to a non-problem; this is a false positive with low
blast radius — the budget owner reviews, finds nothing actionable, and the alert
is noted in the governance log as a false positive for evaluation suite
calibration. An optimisation proposal that incorrectly identifies a model
routing change as cost-effective — proposing to route a class of requests to a
less capable model that costs less per token but produces outputs requiring
significantly more human review — has a blast radius that extends through the
organisation's operations until the error is detected and the routing change is
reversed. The advisory tier for optimisation proposals ensures that a qualified
human reviews the proposal before it is acted on, with access to context about
the operational implications that the agent's cost-focused model does not
capture.

Optimisation proposals that require changes to a system's specification —
because the optimisation involves altering the token budget, the model tier, the
tool permission scope, or any other constraint that was established through the
specification readiness process — must re-enter the specification readiness
process rather than being implemented directly. The FinOps Agent may surface the
proposal, but the budget owner's approval to investigate it is not approval to
implement it. Implementation requires a specification change, a Spec Critic
pre-lint, and a specification readiness gate assessment. This requirement
prevents the economics governance loop from becoming a bypass route for
specification changes that would otherwise require gate scrutiny.

---

### Runbook Drift Agent

**agent_id:** runbook-drift-agent

**purpose:** Continuously compares deployed system configuration against the
runbook's documented state, detecting drift across model version, tool manifest,
component versions, environment configuration, and escalation chain currency.

**allowed_inputs:** Deployed configuration (read-only); Runbook nodes
(read-only); Deployment nodes (read-only); HumanOwner nodes (for escalation
chain currency checking, read-only).

**allowed_tools:** Structured document comparison; configuration state query
(read-only).

**forbidden_tools:** Modification of the runbook; direct notification to
external parties; write access to Deployment nodes.

**data_access_classification:** Up to internal-sensitive.

**autonomy_tier:** Monitored execution (for drift detection and staleness
flagging); advisory (for proposed runbook update drafts).

**approval_required_for:** All proposed runbook updates. The steward reviews the
drift report and proposed updates, makes corrections, and accepts the update as
satisfying the operational Definition of Done runbook currency condition.

**output_artifacts:** EvidenceArtifact nodes (drift reports labeled
monitored-execution; runbook update proposals labeled agent-proposed, pending
steward review).

**logging_required:** Yes.

**kill_switch:** Documented and tested before production deployment. Accessible
to the system steward and stewardship coordinator.

**owner:** System steward.

The Runbook Drift Agent performs the continuous comparison that the operational
Definition of Done requires — verifying that the runbook accurately describes
the system as deployed — at a frequency and across a scope that manual steward
review cannot match without consuming the steward's time in routine monitoring
rather than judgment-intensive stewardship work. The agent compares the deployed
configuration's model version against the runbook's stated model version,
verifies that the tool manifest matches the tool grants documented in the
runbook, checks component versions against the runbook's component inventory,
and validates that the escalation chain references human owners who are
currently active and whose contact records are current in the HumanOwner nodes.
When a discrepancy is detected, the agent generates a drift report at monitored
execution autonomy — the report documents what was found and where, and is filed
as a governance artefact immediately, without waiting for human approval,
because the steward needs accurate information about the current drift state to
determine the appropriate response.

The proposed runbook update drafts that the agent generates alongside the drift
report operate at the advisory tier because updating a runbook is not a
mechanical transcription exercise. A drift item that shows the deployed model
version has changed may indicate that the specification's model version
constraint has been violated and requires immediate investigation, or it may
indicate that the runbook has not been updated following an approved model
version change that was recorded in the deployment governance record. The agent
detects the discrepancy; the steward determines its significance. Similarly, a
drift item that shows an escalation chain contact is no longer current may
require a runbook update with a replacement contact, or it may indicate that the
named human owner has left the organisation and that the system requires
accountable human reassignment — a governance decision that extends beyond
runbook maintenance. The agent's proposed update addresses the surface
discrepancy; the steward's review determines whether the discrepancy requires a
deeper response.

The human decision point is placed at the steward's review of the full drift
report, not at individual drift items. This reflects the operational reality
that drift items are often related — a model version change, a tool manifest
update, and an environment configuration change that appear as separate drift
items may all stem from the same deployment event — and that the steward needs
to assess the drift picture as a whole to determine whether each item is a
genuine runbook gap, an acceptable operational variance documented elsewhere in
the governance record, or a signal of a deeper governance failure. The steward's
review of the drift report must be recorded in the governance log, because the
record of that review is what demonstrates that the operational DoD runbook
currency condition is being actively maintained rather than passively assumed.

---

### Incident Analysis Agent

**agent_id:** incident-analysis-agent

**purpose:** During incident response, reconstructs event timelines from traces,
logs, metric change events, deployment records, and cost anomalies; correlates
the incident with recent deployments, configuration changes, and known risks;
and proposes initial containment approaches for incident commander review.

**allowed_inputs:** System traces (read-only); application logs (read-only);
metric records (read-only); Deployment nodes (read-only); Incident nodes
(read-only); Risk nodes (read-only); governance graph nodes (broad read-only
access during active incident).

**allowed_tools:** Log aggregation and structured query (read-only); timeline
assembly; anomaly correlation.

**forbidden_tools:** Execution of containment or remediation actions;
modification of any production system; write access to Incident nodes without
incident commander approval; external communication.

**data_access_classification:** Up to internal-sensitive. Broader access scope
is permitted during declared incidents, subject to incident commander
authorisation, and access scope reverts to standard on incident closure.

**autonomy_tier:** Advisory. All outputs require incident commander review
before action.

**approval_required_for:** Every proposed containment action before execution.
Every timeline and correlation analysis before it is treated as authoritative in
post-incident review.

**output_artifacts:** EvidenceArtifact nodes (incident timeline labeled
agent-generated; containment proposals labeled agent-proposed; post-incident
review timeline and contributing factors draft labeled agent-proposed, pending
incident commander review).

**logging_required:** Yes.

**kill_switch:** Documented and tested before production deployment. Accessible
to the on-call engineer, incident commander, and system steward.

**owner:** On-call engineer during active incident; system steward for
post-incident governance.

The Incident Analysis Agent addresses the information assembly problem that is
most acute in the first minutes of a declared incident: the incident commander
must understand what happened, what changed recently, and where the most
credible causal paths lie, but the evidence is distributed across multiple log
systems, metric stores, deployment records, and governance graph nodes that
require different query interfaces to retrieve. The agent performs that
retrieval and assembles a timeline — ordering events by timestamp, correlating
metric change events with deployment records, and flagging governance graph
nodes (Risk nodes, Deployment nodes) that are temporally proximate to the
incident's onset — in a compressed timeframe that human manual retrieval across
the same sources cannot match. The timeline is labeled agent-generated and is
presented to the incident commander as a starting point for their own analysis,
not as an authoritative account.

The containment proposals the agent generates operate at the advisory tier
without exception. There is no autonomy level under which the Incident Analysis
Agent may execute a containment action without incident commander approval. The
time pressure of an active incident is real and acknowledged; it does not
override the human-gated requirement for containment actions, for the same
reason that the time pressure of a failing canary deployment does not override
the human-gated requirement for rollback in deployment governance. The agent's
role during an incident is to compress the time the incident commander needs to
make an informed decision, not to make the decision. The agent proposes; the
incident commander commands. An agent that executes containment actions without
authorisation has taken an action with blast radius that may exceed the blast
radius of the incident itself, and has done so without the accountability that
the incident commander's authorisation provides.

The post-incident governance function of the agent is distinct from the active
incident response function, and the ownership shifts accordingly. After the
incident is closed and the post-incident review is initiated, the agent produces
a timeline and contributing factors draft for the post-incident review author's
consideration. This draft draws on the same timeline assembly that was produced
during the incident, extended with the incident's resolution events and any
governance record updates that occurred during the response. The post-incident
review author reviews the draft, applies their own judgment about contributing
factors, corrects timeline inaccuracies where the agent's correlation logic
produced false associations, and produces the human-authored post-incident
review that serves as the definitive governance record. The agent's draft is an
acceleration tool; the author's review is the accountability event that converts
the draft into a governance artefact.

---

## Tool Authorization Matrix

Every governance agent operates within a defined tool authorization envelope.
The allowed_tools and forbidden_tools fields in an agent's schema describe that
envelope in functional terms. This section formalises the envelope as a matrix:
for each combination of ASDLC layer and governance autonomy level, the matrix
specifies which tool classes an agent may invoke. The matrix is not a
suggestion; it is the RBAC equivalent for agentic governance. An agent that
invokes a tool class outside its authorized envelope has acted outside its
specification, and the output of that invocation may not be accepted as
governance evidence.

Tool classes are defined by function, not by vendor or implementation:

- **Read-governance-graph** — read-only access to governance graph nodes and
  edges.
- **Write-governance-graph** — create or update governance graph nodes and
  edges.
- **Evidence-assembly** — read artefacts from the evidence store and compose
  them into bundles.
- **Evidence-generation** — run tools that produce new EvidenceArtifacts
  (scanners, SBOMs, hash generators, compliance checkers).
- **Specification-read** — read demand items, specifications, acceptance
  criteria, and constraints.
- **Specification-write** — create or modify specifications and related nodes.
- **Notification-send** — send push notifications to named humans.
- **Gate-assessment** — mark gate conditions as pass or fail. This is a
  human-only tool class. No agent autonomy level may invoke it under any
  circumstances.
- **Rollback-trigger** — initiate production rollback.
- **External-regulatory-query** — query external regulatory databases and
  compliance APIs.
- **Model-invocation** — invoke a foundation model for inference (reasoning,
  generation, classification).
- **Code-execution** — execute code in a sandboxed environment.
- **Production-read** — read operational telemetry and production system state.
- **Production-write** — modify production system configuration or state.

The authorization matrix below defines permitted tool classes by layer and
autonomy level. "+" indicates tool classes added relative to the Advisory
baseline for that layer. Unlisted tool classes are not authorized at any level
for that layer unless explicitly justified and approved through the process
described in Tool Authorization Lifecycle below.

| Layer                                 | Advisory                                                                                                                             | Monitored Execution                                                                                        | Human-Gated                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Layer 1** (Specification Readiness) | Read-governance-graph, Specification-read, External-regulatory-query, Model-invocation, Notification-send                            | + Evidence-generation (validation evidence only), Specification-write (draft only, flagged agent-proposed) | No additional tools                                                                            |
| **Layer 2** (Loop Execution)          | Read-governance-graph, Specification-read, Evidence-assembly, Evidence-generation, Model-invocation, Code-execution, Production-read | + Write-governance-graph (loop output filing only)                                                         | No additional tools                                                                            |
| **Layer 3** (Release Gate)            | Read-governance-graph, Evidence-assembly, Evidence-generation, Specification-read, Model-invocation                                  | + Write-governance-graph (evidence bundle assembly filing only), Notification-send, Production-read        | + Rollback-trigger (proposed; requires human authorization before execution)                   |
| **Layer 4** (Operational Stewardship) | Read-governance-graph, Production-read, Model-invocation, Evidence-generation, Notification-send                                     | + Write-governance-graph (operational evidence filing only), Evidence-assembly                             | + Production-write (proposed; requires human authorization before execution), Rollback-trigger |

**Gate-assessment is explicitly prohibited for all layers and all autonomy
levels.** It is not absent from the matrix because it was overlooked; it is
absent because no agent may hold it. Any agent schema that includes
Gate-assessment in its allowed_tools field has not been correctly specified, and
the specification must be corrected before the agent is deployed.

The Write-governance-graph entries for Monitored Execution are scoped
constraints, not blanket write access. "Loop output filing only" means the agent
may create EvidenceArtifact nodes generated by its own loop work and attach them
via generated_by edges. It does not mean the agent may create or modify
Specification nodes, gate decision records, or accountability records. Each
scoped constraint must be documented in the agent's schema with the same
precision as the approval_required_for field.

---

## Preventing Tool Permission Escalation via Agent Composition

When Agent A orchestrates Agent B, the effective tool permission set for the
composed system is the union of both agents' individually authorized tool sets,
scoped to their respective layer-phase contexts. If that union includes any tool
class that Agent A is not individually authorized for, the composition has
created an unauthorized tool access path. The effect is that Agent A can
accomplish through delegation what it is not permitted to do directly — this is
the agentic equivalent of privilege escalation, and it is a governance violation
regardless of whether the access path was intentional.

This failure mode requires explicit structural controls, not only monitoring:

**Composition records must declare the composed permission set.** The
composition record defined in governance/agents.md for multi-agent pipelines
must enumerate the composed tool permission set — the union of all participating
agents' authorized tool classes. This is a required field, not an optional
annotation. A composition record that does not include the composed permission
set has not been fully specified for governance purposes.

**Unauthorized tool classes in the composed set require explicit justification
and approval.** Any tool class that appears in the composed permission set but
is not in Agent A's individual authorization must be explicitly justified — why
does the composition require access that the orchestrating agent itself does not
hold? — and must be approved by Agent A's accountable human before the
composition is deployed. This approval is recorded in the governance graph
alongside the composition record and is subject to the same review cadence as
all tool authorization records.

**Composed systems are governed entities with their own ToolAuthorizationRecord
nodes.** A multi-agent pipeline is not the sum of its constituent agents'
governance records. It is a distinct governed entity. The governance graph must
contain a ToolAuthorizationRecord node for the composed system, covering the
full composed permission set. Individual agent records are insufficient for
governing the composed system's authorization envelope.

**Orchestration context must be carried in every sub-agent invocation record.**
When a sub-agent invokes a tool in the context of being orchestrated by a
higher-level agent, the invocation log record must carry the orchestrating
agent's identifier. Governance tooling must flag any invocation where the
orchestrating agent's individual tool authorization does not include the tool
class the sub-agent invoked. The flag is a governance staleness event if the
composition record has already been approved with that tool class in scope; it
is a governance violation if no approved composition record covers the
invocation path.

The purpose of these controls is not to make multi-agent composition impractical
— it is to ensure that the governance visibility that applies to individual
agents is not lost when agents are composed. A governance infrastructure that
governs individual agents precisely but allows composed systems to acquire
unconstrained access through orchestration has governed the pieces and left the
whole ungoverned.

---

## Tool Authorization Lifecycle

Tool authorizations are not permanent grants. They are time-limited governance
decisions that require periodic review and must be explicitly maintained. An
agent operating on stale authorization is an ungoverned agent in a material
sense: its current tool access has not been validated against its current
specification and operational context.

**Review triggers.** A tool authorization record must be reviewed whenever any
of the following conditions occurs:

- The agent's GASH (Governance Agent State Hash — see
  [governance/agents.md](governance/agents.md)) changes — any update to the
  model version, system prompt, or tool manifest used by the agent constitutes
  a GASH change and requires
  re-evaluation of the authorization record, because a changed agent may
  exercise its authorized tools differently than the agent that was originally
  authorized.
- The system's blast radius tier changes — a blast radius increase requires
  immediate review, because tool classes that were appropriate for a lower blast
  radius may require additional controls or removal at a higher tier.
- A production incident traces to unauthorized or inappropriately authorized
  tool use — the incident post-review must include a tool authorization review
  as a mandatory action item.

**Authorization expansions.** Adding a new tool class to an agent's authorized
set requires: a specification change documenting the new tool class and the
governance rationale for adding it; an evaluation suite update that includes
test cases covering the new tool's use, including at minimum one false negative
case and one adversarial case; explicit approval from the agent's accountable
human recorded in the governance log; and a new or updated
ToolAuthorizationRecord node in the governance graph reflecting the expanded set
with the approval date and approver identity. An agent that begins using a new
tool class before all four of these conditions are satisfied is operating
outside its specification.

**Authorization contractions.** Removing a tool class from an agent's authorized
set does not require an evaluation suite update, because the change reduces the
agent's capability rather than extending it. However, contractions must still be
recorded: the ToolAuthorizationRecord node must be updated, the specification
must reflect the change, and the contraction event must be logged with the date
and the identity of the accountable human who authorised the removal. Unrecorded
contractions create governance ambiguity — if the record still shows the tool
class as authorized, an audit cannot distinguish between a governed contraction
and an unauthorized invocation that happened to stop.

**Staleness threshold.** An agent operating with a tool authorization record
that has not been reviewed within twelve months — a policy-set staleness
period, chosen by the authors rather than derived from any measured rate of
authorization drift — is operating on stale authorization. This is a governance staleness event. The steward responsible for
the agent must initiate a review and produce an updated ToolAuthorizationRecord
node — confirming that the current authorization remains appropriate, or
modifying it as required — within the staleness resolution window defined in the
organisation's governance policy. Until the review is complete and the record is
updated, the agent's outputs must be labeled with the staleness flag in addition
to their normal epistemic tier label. Gate assessments that rely on outputs
carrying a staleness flag must note the flag in the gate decision record and the
accountable human must explicitly acknowledge it.

---

## Adding Agents to the Control Plane

The process for adding a named governance agent to the Control Plane follows the
same governance structure as adding any agentic system under the ASDLC. An
organisation that wants to add a new governance agent must satisfy four
requirements before the agent may be deployed in a production governance
context, and the absence of any one of them means the agent has not been
governed.

First, the agent requires a specification filed through the specification
readiness gate. The specification must identify the agent's governance task as
the business need, with evidence that the task represents a genuine governance
gap and not a duplication of a task already assigned to an existing named agent.
The specification must assess blast radius against the worst case of acting on
an incorrect output — not the typical case, and not the best case — and assign
the appropriate autonomy tier accordingly. The specification must define the
token budget as a hard constraint for any agent at Tier 2 blast radius or above,
and must define the permission scope — allowed inputs, allowed tools, and
forbidden tools — with the specificity required by the schema structure defined
in this document. A specification that passes the gate with vague permission
boundaries has not satisfied Condition 4 (constraints identified) for a
governance agent.

Second, the agent requires an evaluation suite that addresses all four case
categories defined in governance/agents.md: standard functional correctness
cases; false positive cases, where well-formed governance artefacts are
presented and the agent should produce no flags; false negative cases, where
governance-deficient artefacts are presented with plausible-sounding language
that might obscure the deficiency; and adversarial governance input cases, where
inputs are constructed with the intent of manipulating the agent into producing
an incorrect assessment. For agents at the monitored execution autonomy tier,
the evaluation suite must additionally include drift detection cases that verify
the agent detects changing conditions over time rather than only in response to
event triggers. The evaluation suite must be run against the agent before
deployment and must demonstrate correct output across all four case categories.
An evaluation suite that achieves high scores on functional correctness cases
but has not been constructed to include false negative and adversarial cases is
not an evaluation suite for a governance agent — it is a functional test suite
applied to a governance context.

Third, a named accountable human and a named steward must be assigned before the
agent enters production governance use. The accountable human must be the holder
of the functional role that corresponds to the agent's governance task — as
defined in the owner field of the agent's schema — and must have explicitly
accepted accountability for the agent's behaviour. The steward must have the
operational access and authority required to monitor the agent's governance log,
respond to anomalous outputs, and invoke the kill switch if required. Neither
role may be assigned as a formality; the assignment must be recorded in the
agent's governance record and the named individuals must be reachable during the
agent's operating hours.

Fourth, the kill switch must be tested before production deployment. The test
must verify that invoking the kill switch halts all active agent invocations and
prevents new invocations without requiring access to the agent's internal
implementation, and that the system's operational state after the kill switch is
invoked is documented and predictable. The kill switch test result is recorded
in the deployment governance record. An agent whose kill switch has not been
tested is not ready for production deployment regardless of the quality of its
specification, evaluation suite, or ownership assignment. The kill switch is not
a last resort; it is a required operational control, and its untested state
represents an unknown in the governance infrastructure that the agent is
supposed to protect.

An organisation that deploys a governance agent without satisfying all four
requirements has not governed its governance agents. That is not a minor
procedural gap — it is a structural failure in the governance of governance
itself. The integrity of the ASDLC's gate structures depends on the reliability
of the agents that assist those gates. An ungoverned governance agent is an
uncontrolled input into every gate decision it touches.

---

## Normative References

The trust-boundary, tool-authorization, and adversarial-evaluation
requirements in this document are calibrated against the agentic and
prompt-injection literature. The following are the load-bearing references:

- OWASP GenAI Security Project, *Agentic AI — Threats and Mitigations* (2025):
  https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ —
  primary practitioner reference for tool misuse, goal hijacking, identity and
  privilege abuse, memory poisoning, and excessive autonomy. The
  forbidden_tools, approval_required_for, and Tool Authorization Matrix design
  in this document map directly to these threat classes.
- Greshake et al., *Not what you've signed up for: Compromising Real-World
  LLM-Integrated Applications with Indirect Prompt Injection* (2023):
  https://arxiv.org/abs/2302.12173 — the foundational evidence that retrieval
  inputs, tool outputs, and other content crossing into the agent's context
  must be treated as hostile data. This is the source behind the
  trust-boundary enforcement requirement and the input-validation expectations
  on every governance agent's allowed_inputs.
- Debenedetti et al., *AgentDojo: A Dynamic Environment to Evaluate Prompt
  Injection Attacks and Defenses for LLM Agents* (2024):
  https://arxiv.org/abs/2406.13352 — task-and-tool benchmark structure that
  the evaluation requirements in *Adding Agents to the Control Plane* (false
  positive, false negative, adversarial governance input, drift detection)
  inherit. Cite as evaluation evidence, not as a settled standard; the
  benchmark is a calibration point, not a sufficiency proof.
- OWASP LLM Top 10 (2025): https://genai.owasp.org/llm-top-10/ — broad
  application security baseline; complements the agentic-specific guidance
  above.

These references underwrite the threat surface this document governs. They
do not relax the requirement that every governance agent must satisfy the
specification, evaluation, ownership, and kill-switch conditions in *Adding
Agents to the Control Plane* before it is deployed.

---

_The Agent Control Plane does not make governance easier by reducing the
standard. It makes governance tractable at scale by ensuring that every agent
contributing to a governance decision is itself a governed system — named,
specified, evaluated, and owned — so that the accountability chain from gate
condition to gate decision to named human is unbroken at every point where agent
assistance is used._
