# Demand & Value — ASDLC Layer 1

_The governed demand layer of the Agentic Software Delivery Lifecycle._

See the [Manifesto](../../manifesto.md) for the engineering execution layer (Layer
2). See [Specification Readiness](../specification-readiness.md) for the Layer 1→2
gate. See [Demand Metrics](metrics.md) for measurement. The epistemic-tier vocabulary
used here is imported from the Intelligence Governance Manifesto (IGM); refer
to IGM for the canonical tier definitions.

---

## What is the Demand & Value Layer?

Layer 1 is the governed demand layer of the ASDLC. It precedes the engineering
execution loop — the manifesto's Layer 2 — and exists for one reason: to ensure
that only validated, prioritised, loop-ready specifications enter that loop. The
demand layer does not execute. It governs what gets executed, determines the
order of execution, and is ultimately responsible for whether the execution
produced something worth building in the first place. A team with a well-run
agentic loop but a poorly-run demand layer will build the wrong things
correctly, consistently, at increasing speed. Layer 1 is where that failure is
caught before the loop is ever run.

---

## Business Need Identification and Validation

Every loop iteration begins with a claim: something is worth building. The
demand layer's first obligation is to determine whether that claim is true
before it consumes engineering capacity. A stakeholder request is not a
validated need. An assumption about user pain is not a validated need. A feature
that a competitor has shipped, with no evidence that your users share the
underlying problem, is not a validated need.

A need is validated when it is supported by evidence that can be examined
independently of the person who raised it. The following categories of evidence
are sufficient:

**User research.** Direct evidence from the people who will use the system —
interviews, usability studies, longitudinal surveys, or behavioural data from
existing systems — establishing that a specific pain point or unmet capability
exists and matters. The key word is direct: inferences from proxy populations,
internal assumptions about user behaviour, or anecdotes from sales calls are
supporting evidence, not primary validation.

**Quantitative data.** System metrics, business intelligence, or operational
data that makes the need observable in numbers. Escalation rates. Drop-off
rates. Error frequencies. Time spent on a task. Unit cost of a process step. The
data must be causally connected to the need, not merely correlated with a
vaguely related problem space.

**Regulatory mandate with citation.** A specific legal, regulatory, or
contractual requirement that creates an obligation, referenced by document,
article, and jurisdiction. The citation must be specific enough that a
compliance officer can verify it independently. "We need to comply with GDPR" is
not a validated need. "Article 22 GDPR restricts automated individual
decision-making and requires a remediation path; this need addresses that
requirement for our claims triage system" is.

**Market signal with evidence.** An observable shift in the external environment
— a new entrant, a changing standard, a documented shift in customer behaviour —
accompanied by evidence that the shift is real and affects your users
specifically. Market signals without user-specific evidence validate a category
of problem, not a specific need for your system.

**Executive decision with documented rationale.** A decision by an accountable
executive to pursue a direction for strategic reasons, with the rationale
documented. This is a legitimate validation path for strategic investments where
user research and data may be incomplete by design — early markets, genuinely
novel capabilities. The difference between an executive decision and a
stakeholder request is documentation, accountability, and the acceptance that
the strategic bet may be wrong. An executive who documents their rationale has
taken ownership of the need; a stakeholder who makes a request has not.

The evidence categories above define what constitutes valid validation evidence.
Generating that evidence requires deliberate discovery — the process of
understanding what users need and whether a proposed system would genuinely
serve them. Structured discovery techniques — including jobs-to-be-done analysis
(understanding the outcome users are hiring a solution to achieve), user journey
mapping (charting the end-to-end experience within which the need arises), and
continuous discovery cadences (regular, small-cycle user interviews that
generate ongoing evidence rather than one-time studies) — are proven methods for
generating the primary user research evidence that the validation bar requires.
No specific technique is mandated; the technique is a means to an end, and the
end is evidence that meets the validation bar for the appropriate blast radius
tier. Teams that generate validation evidence through structured discovery
produce more durable specifications: the evidence captures not just whether the
need exists but why it exists in context, which reduces specification drift
inside the loop.

The anti-patterns are worth naming explicitly. A stakeholder request without
supporting evidence is the most common. It conflates the act of articulation
with the act of validation. The second is assumed pain points: needs that
"everyone knows" exist, that have never been tested against users, and that may
reflect the organisation's internal frustration rather than the users'
experience. The third is competitive parity features — items added because a
competitor has them, without investigating whether the competitor's
implementation addresses a pain that your users actually have. Competitive
parity is a valid input into prioritisation; it is not validation of a need.

### The Validation Bar Scales with Blast Radius

Not every need requires the same depth of validation. A low-risk internal
tooling enhancement — scoped within a single team, affecting no customer-facing
behaviour, reversible within hours — warrants a lighter validation pass than a
customer-facing decisioning system operating under regulatory scrutiny. The
validation tier corresponds to the manifesto's autonomy tier model:

**Tier 1 (low blast radius):** At minimum, one category of primary evidence —
user research, quantitative data, or documented executive decision. The need can
be validated by the product owner and the team directly. Formal documentation is
lightweight: a ticket with the evidence referenced is sufficient.

**Tier 2 (medium blast radius):** At minimum, two independent categories of
evidence, with at least one data-backed or research-backed signal. The business
demand sponsor must explicitly sign off that the need is real. Evidence is
documented in a durable artefact — not a ticket field.

**Tier 3 (high blast radius — customer-facing, regulated, or high-volume
decisioning):** Multiple categories of evidence, including at minimum one
primary user research finding and one quantitative data signal, plus a formal
regulatory or risk assessment where applicable. Business demand sponsor sign-off
is required. The validation evidence is stored in a named document,
version-controlled, and referenced in the gate decision record (see
[Specification Readiness](../specification-readiness.md)).

The validation tier is determined at the demand backlog entry point, not
retrospectively. A team that assesses validation requirements after the
engineering investment has begun is not governing its demand layer — it is
auditing decisions already made.

### Evidence Freshness: Event-Triggered Staleness

Validation evidence does not expire on a calendar. It becomes stale when the
context that made it valid changes. A demand item whose validation evidence is
eight months old but whose context has not changed since that evidence was
gathered is still valid. A demand item whose validation evidence is three weeks
old but whose business context has shifted materially is not.

Evidence becomes stale — and revalidation is required — when any of the
following events occurs:

**Business context change.** The organisation's strategy, priorities, or
operating model shifts in a way that affects whether the validated need remains
a genuine priority. A reorganisation that changes ownership of the business
domain, a strategic pivot that deprioritises the underlying capability, or a
change in the unit economics of the relevant business process all constitute
business context changes.

**Regulatory or legal environment shift.** A new regulation, a regulatory
guidance update, an enforcement action against a comparable organisation, or a
change in jurisdictional applicability that affects the demand item's compliance
posture. Evidence gathered against the prior regulatory state does not validate
the need under the new regulatory environment.

**Key stakeholder change.** The departure or role change of the business demand
sponsor, the domain expert who provided primary user research, or an executive
who provided strategic rationale. New stakeholders have not validated the
evidence and may not endorse the conclusions it supports. Stakeholder change
does not automatically invalidate evidence — it triggers a revalidation
conversation with the new stakeholder to confirm they accept the prior evidence
base.

**Material competitive landscape change.** A significant entrant, a market
standard shift, or a major competitor capability release that changes the
urgency or framing of the demand item. This applies particularly to market
signal evidence: a market signal from nine months ago, gathered before a major
competitor launch, may no longer represent the current environment.

**Technical assumption change.** A change in the system architecture,
dependencies, platform constraints, or technical environment that the demand
item assumes. If the demand item was validated against an architecture that has
since changed, the assumptions underlying the decomposition and blast radius
assessment may no longer hold.

Product owners must evaluate evidence freshness at every demand backlog review
cycle. The question is not "when was this evidence gathered?" but "have any
staleness-triggering events occurred since this evidence was gathered?" A
backlog item that has survived multiple review cycles without triggering any
staleness event requires no revalidation — evidence age alone is not grounds for
revalidation. A backlog item that has aged without staleness-event review is an
unmonitored item, not a validated one; that monitoring obligation belongs to the
product owner.

### Regulatory Co-Evolution Intelligence

Regulatory requirements are not static inputs to demand governance. They
co-evolve continuously through enforcement actions, guidance letters,
consultation papers, court decisions, and legislative amendments. An
organisation that treats its regulatory context as "what was true when we last
did a regulatory review" is governing against a stale model of its obligations.

The demand layer manages regulatory co-evolution through a **regulatory context
map**: a set of governance graph Constraint nodes linked to the regulatory
sources that created them, with the regulatory source version (document version,
date, jurisdiction) recorded. This map is not a static reference document — it
is a live governance artefact updated as sources change.

Regulatory co-evolution agents — governed under the ASDLC as Layer 0 demand
intelligence outputs — monitor configured regulatory feeds and flag when a
regulatory source underpinning a constraint has been updated, superseded, or
reinterpreted by enforcement action. When a regulatory source changes, the
demand layer receives a push notification identifying: which deployed systems
have constraints derived from the changed source; which in-progress demand items
have regulatory constraints based on it; and whether the change creates a new
demand item (a new obligation) or modifies an existing constraint.

The product owner and domain compliance function review flagged items. If a
constraint in a deployed system is now outdated, it enters the L4→L2 maintenance
feedback path. If the change creates a new obligation, it enters the Layer 0
draft demand item queue.

Key governance principle: regulatory intelligence does not automatically change
constraints or create demand items. It surfaces the signal; humans make the
determination. An organisation that allows regulatory co-evolution agents to
modify constraints or generate validated demand items without explicit human
review has misconfigured the governance boundary between signal surfacing and
decision-making.

---

## Value Definition

Validating that a need is real is necessary but not sufficient. The demand layer
must also establish, before the loop runs, what "valuable" means precisely
enough to measure after deployment. This is the function of value definition,
and it fails more often than any other step in demand governance.

Three categories of value apply across the ASDLC:

**Business value** is quantifiable impact on a business outcome: cost reduction,
revenue impact, risk reduction, compliance exposure removed, or operational time
saved. Business value must be measurable. "Improve the customer experience" is
not business value — it is a direction. "Reduce mean time to resolution for
claims by 20% within 90 days of deployment, measured against the baseline
established in Q3" is business value. If the value cannot be stated in these
terms, the need is not yet defined precisely enough to govern.

**User value** is improvement to a specific user's ability to accomplish a goal.
It may be qualitative, but it must be observable: a user interview, a task
completion metric, a satisfaction signal, or a behavioural change. "Users will
find it easier" is not user value — it is intent. "Users in segment A will be
able to complete the renewal workflow without escalation to a support agent,
where the current escalation rate is 34%" is. User value and business value are
not interchangeable. A feature can deliver user value without delivering
business value, and an organisation that conflates the two will build things
users appreciate but the business cannot sustain.

**Technical value** is debt reduction, reliability improvement, or architectural
enablement. It is a legitimate category of work — accumulated technical debt has
real cost, and architectural enablement can unlock compounding future value. But
technical value is only valid without business or user value backing when the
case is made explicitly and accepted explicitly by an accountable business
sponsor. "We need to refactor the identity service to reduce mean time to change
from 14 days to 2 days, which currently blocks three pending business
initiatives" is a valid technical value statement. "We should rewrite this
because it's messy" is not. Technical work entered into the demand backlog
without explicit business or user value justification is a prioritisation
failure, not a technical decision.

### The Business-Level Definition of Done for Layer 1

A demand item is done at Layer 1 — ready to cross into the specification
readiness gate — when three conditions hold simultaneously:

1. **The need is validated with evidence.** A primary evidence category is
   present, documented, and proportionate to the blast radius tier.
2. **The value is defined and measurable.** A specific, time-bounded, measurable
   value statement exists at the business level, owned by the business demand
   sponsor.
3. **The success criterion is specified.** A single statement of what business
   success looks like post-deployment: measurable, time-bounded, and owned by a
   named person. This success criterion becomes the business-level test for
   Validate (P8 in the manifesto) and for the operations layer's ongoing
   measurement.

A demand item that satisfies one or two of these conditions is not done at
Layer 1. It is in progress. Entering the loop with a partial Layer 1 completion
is the primary driver of "built the wrong thing correctly" failure modes — the
class of failure where verification passes and validation fails, because the
business success criterion was never precisely defined before execution began.

### Loop Cost Economics Assessment

Value definition is incomplete without an explicit loop cost economics
assessment. Value is not what a demand item delivers in isolation — it is what
it delivers minus the cost of the loop required to deliver it. This distinction
matters because loop costs are non-trivial and variable, and a demand item that
delivers genuine value may still be a non-viable investment if the cost of the
loop to deliver it exceeds that value.

Loop cost has four components that must be estimated before gate passage at Tier
2 and above (a brief note is sufficient at Tier 1):

**Engineering time.** The estimated engineering hours required to specify,
execute, verify, and validate the item through the full loop, including the
governance overhead at each phase gate — not just implementation time. Items
that are small in implementation scope can be large in governance time if they
require extensive evidence assembly, compliance filing, or cross-team
coordination.

**Agent inference cost.** At scale, the token-level cost of running governance
and execution agents through a loop iteration is material. For high-volume or
complex specifications — those that generate large context windows, require
multi-agent coordination, or involve extended evaluation runs — inference cost
must be estimated, not assumed to be negligible. An organisation that treats
agent inference cost as a rounding error will discover it as a budget problem at
scale.

**Governance overhead.** Gate preparation, evidence assembly, review cycles,
compliance filing, and audit documentation all have a time cost that is borne by
named accountable humans. This cost scales with blast radius tier and with
organisational governance maturity. At Tier 3, governance overhead can equal or
exceed implementation time for small feature items — and that cost is real, even
when no line of code is written.

**Opportunity cost of loop capacity.** Every active loop iteration consumes
governance capacity that is not applied to other items. A demand item that would
deliver modest value but occupy loop capacity for an extended period may be
correctly deprioritised in favour of multiple smaller items with greater
aggregate value. Opportunity cost is not a reason to avoid large initiatives —
it is a factor in sequencing and decomposition decisions.

The loop cost economics assessment produces a single explicit judgment: is the
value delivered by this demand item, as currently scoped, greater than the total
loop cost to deliver it? If the answer is no, the demand item is not viable as
scoped. The response is not to abandon the need — the need may be real — but to
rescope the item (narrower implementation, lighter governance tier, lower blast
radius) until the value/cost ratio is positive, or to defer it until the cost
structure changes. A demand item that fails loop cost economics does not enter
the backlog. This assessment is a named, explicit step in the
demand-to-specification bridge, not a vague "is this worth building" question to
be answered informally.

---

## Portfolio Governance

Demand layer governance is not just about individual items. It is about the
portfolio of items competing for the organisation's engineering capacity and
governance attention. Without portfolio governance, the demand backlog becomes a
political queue ordered by who asked most recently or most loudly, loop capacity
is misallocated, and governance maturity is outrun by the volume of active
initiatives.

Portfolio governance has three components:

### Demand Backlog

The demand backlog is the managed queue of validated business needs awaiting
specification and loop entry. It is not the same as an engineering backlog or a
sprint backlog. Those are execution artefacts. The demand backlog is a
governance artefact: it represents the organisation's prioritised claims on
engineering capacity, each with validation evidence attached.

Ownership is explicit. The demand backlog is owned by a single named role — the
product owner in most organisations — who is accountable for its contents, the
evidence behind each item, and the prioritisation order. Backlogs without
explicit owners are not backlogs — they are request registries, and request
registries cannot be governed.

Items enter the backlog through a single path: the validation step described
above. An item that has not been validated cannot appear in the demand backlog.
Items that arrive as informal requests, Slack messages, or verbal commitments
must be converted into validated demand items before they enter. The conversion
step is the product owner's responsibility. The evidence is the business demand
sponsor's responsibility.

### Prioritisation Criteria

The order of the demand backlog must be determined by documented criteria,
applied consistently. Undocumented prioritisation criteria produce political
prioritisation, where the items at the top of the queue reflect relationships
and influence rather than value and risk. Political prioritisation is not a
cultural failure — it is a governance design failure. It happens when the
criteria are missing, not when the people are bad.

The criteria are: **value × urgency × risk × strategic alignment**. Applied in
practice:

- **Value** is the magnitude of the business value statement — larger, more
  certain impact ranks higher.
- **Urgency** is the time sensitivity of the need — regulatory deadlines, market
  windows, contractual obligations. Urgency is not the same as importance;
  confusing them is a common cause of backlog mismanagement.
- **Risk** includes two kinds: the risk of acting (blast radius, implementation
  complexity) and the risk of not acting (compliance exposure, compounding
  technical debt, customer attrition). High risk of not acting increases
  priority; high risk of acting does not necessarily reduce it but does increase
  the governance bar.
- **Strategic alignment** is the degree to which the item advances documented
  strategic priorities. This criterion prevents tactical fire-fighting from
  consuming capacity needed for strategic investment.

These criteria must be documented and visible to all stakeholders who interact
with the demand backlog. When a stakeholder disputes prioritisation, the
response is to apply the criteria together, not to negotiate. If the criteria
produce a result the organisation cannot accept, the criteria should be revised
— openly, with all stakeholders — rather than abandoned silently for one item.

### Capacity Model

The number of simultaneous loop iterations that can be governed well is bounded.
It is bounded by the organisation's governance maturity, the availability of
accountable humans to review evidence bundles and accept production
accountability, and the overhead of coordination across concurrent
specifications. Running more active initiatives than governance capacity can
support is a Layer 1 failure — it will not appear as a demand layer failure, but
as a pattern of loop quality degradation, specification drift, rubber-stamping,
and evidence bundle shortcuts.

The phase model from the manifesto provides calibration guidance. A Phase 3
organisation — where the loop is newly operational and governance is still being
established — can typically govern one to three active agentic initiatives
simultaneously. A Phase 5 organisation — with mature tooling, established
evaluation portfolios, and governance infrastructure in place — can govern more.
What neither can govern well is more active initiatives than their named
accountable humans can actually review.

The practical test is simple: count the evidence bundles that require human
review per sprint cycle, count the hours available from named accountable
reviewers, and compare. If the review load exceeds capacity, the demand backlog
is oversubscribed and loop quality will suffer. The demand layer's response is
to gate new loop entries, not to encourage faster review.

---

## Demand-to-Specification Bridge

A validated, prioritised business need in the demand backlog is not yet a
loop-ready specification. It must cross a bridge before it can enter the Specify
phase of the manifesto's agentic loop. The bridge converts business-language
need statements into machine-readable, governance-compliant specifications. It
has three steps, and all three must complete before the specification readiness
gate is assessed.

### Step 0: Build vs. Buy Assessment

Before a validated business need is decomposed into loop-ready specifications,
confirm that the need cannot be satisfied by an existing capability. This
assessment applies at Tier 2 and above. At Tier 1, a brief note in the
specification is sufficient; at Tier 2 and Tier 3, the assessment is a
documented artefact.

The assessment examines three alternatives: whether a commercial or open-source
software component already addresses the validated need; whether an existing
internal capability — a deployed system, a configured agent, a published service
— can be adapted to serve the need without a new loop iteration; and whether the
need can be addressed by a process or policy change rather than a software
system.

The outcome of the assessment is a documented decision: build, adapt an existing
capability, or adopt an external component. Each option carries different
maintenance cost, different blast radius characteristics, and different
governance obligations — the decision must weigh all three explicitly, not just
the initial build cost.

A team that skips this step and builds a capability that already exists
internally or externally has consumed loop capacity on work that delivered no
marginal value. The build vs. buy assessment is the demand layer's protection
against that failure mode.

### Step 1: Decomposition

A business need is typically larger than a single loop iteration. The first step
is to break the validated need into loop-sized specifications: each scoped to a
single loop iteration, with a blast radius within the organisation's current
autonomy tier.

Loop-sized means: the specification can be executed within a single iteration of
the agentic loop, the acceptance criteria are checkable at the end of that
iteration, and the blast radius of failure at the current autonomy tier is
acceptable. A specification that requires multiple loop iterations to verify is
not loop-sized — it is an epic in need of decomposition. A specification whose
failure blast radius exceeds the current governance tier is not ready to enter
the loop at that tier — it requires either blast radius reduction (tighter
scope, sandboxed execution, staged rollout) or tier escalation (more restrictive
autonomy controls, higher evidence bar).

Decomposition is not a mechanical split. It requires judgment about dependency
order, value sequencing, and feedback path design. The person doing
decomposition must understand both the business need deeply enough to preserve
intent across split specifications, and the agentic loop deeply enough to know
what loop-sized means in their context. This is the specification analyst's core
skill.

#### Multi-Specification Decomposition Governance

When a demand item is decomposed into more than one specification — which is the
common case for any non-trivial business need — the decomposition itself is a
governed act, not an informal implementation convenience. The following
requirements apply whenever a single demand item produces two or more child
specifications:

**Decomposition record.** A decomposition record must be created and stored as a
durable artefact. The record names the parent demand item (by its backlog
identifier and title), lists all child specifications produced by the
decomposition (by their specification identifiers), documents the decomposition
rationale — why the parent was split at these boundaries and not others — and is
version-controlled alongside the parent demand item.

**Scope coverage check.** The decomposition record must include an explicit
statement that all child specifications together cover the full scope of the
parent demand item. This is not a guarantee of implementation completeness — it
is a governance claim that the decomposition did not silently drop scope. The
specification analyst is accountable for this claim; the business demand sponsor
must confirm that the child specifications, read together, represent the
business need the sponsor validated.

**Named accountability for the decomposition.** A named human — typically the
specification analyst, confirmed by the product owner — must accept
accountability for the decomposition boundary decisions. This is distinct from
accountability for the child specifications themselves. The decomposition
accountable person is responsible for the structural integrity of the split:
that the boundaries are correct, that dependencies across child specifications
are identified, and that the sequencing of child specification execution
preserves value delivery intent.

**Sibling specification awareness at gate.** No child specification may pass the
Specification Readiness Gate in isolation from its sibling specifications.
Before gate assessment of any child specification, all sibling specifications
must be identified and recorded — even if they have not yet reached gate-ready
status themselves. A child specification that passes the gate without its
siblings being identified creates the risk of partial delivery appearing
complete: the loop executes one child spec, the delivered increment appears to
satisfy a portion of the business need, and the remaining child specifications
are deprioritised, deferred, or forgotten. The gate decision record for each
child specification must reference the decomposition record and confirm that all
siblings are identified.

### Step 2: Translation

Each decomposed need must be translated into the specification language the loop
can act on: machine-readable acceptance criteria, explicit constraints, success
criterion traceability, and out-of-scope declarations. This step converts intent
from business language into governed specification.

The technical reference for this step is the companion requirements engineering
framework (`companion-re-framework.md`). That document covers the mechanics:
acceptance criteria templates, constraint taxonomy, traceability linking, and
the format requirements for machine-readable specification. The demand layer
governs whether translation is complete; the RE framework governs how
translation is done. The constraint identification component of this step
includes security threat analysis: the specification analyst must confirm that
the constraints documented in the specification cover identified threats from
the threat model, not just compliance rules and performance envelopes. A
constraint inventory that is silent on threat mitigations is incomplete,
regardless of how thorough its regulatory and operational content is.

The translation step is complete when a domain expert — not the specification
analyst — can read the translated specification and confirm that it faithfully
represents the business intent. This is the translation verification step. It is
not optional. A specification that the domain expert cannot recognise as their
intent has failed translation, regardless of how well-formed it is technically.

### Step 3: Gate

Once decomposition and translation are complete, the candidate specification is
assessed against the specification readiness gate defined in
[Specification Readiness](../specification-readiness.md). The gate is a structured
self-assessment against specific conditions. Loop entry is blocked until all
conditions are satisfied.

Before a specification enters the Specification Readiness Gate, a context thread
is assembled by a governance agent from the governance graph. The context thread
is a structured document — filed as an agent-proposed EvidenceArtifact, reviewed
by the specification analyst — that provides the executing agent at Layer 2 with
the governance lineage of the specification: the key L1 decision points, the
blast radius evidence, the validation evidence type and source, the constraint
identification rationale, and the two or three most relevant comparable
specifications from organisational episodic memory with the loop learnings from
each. The context thread is not additional specification — it does not add
requirements. It is provenance: the story of why the specification says what it
says, enabling the executing agent to calibrate its behaviour to the demand
layer's priorities rather than operating on the specification as if it were
self-contained. An absent or unreviewed context thread means the executing agent
will operate on specification without provenance — a controllable risk that
costs little to prevent.

The gate is not a committee approval. It does not require consensus or buy-in
from all stakeholders. It requires the conditions to be demonstrably met,
assessed by the product owner and specification analyst together, with the
business demand sponsor available for questions on validation evidence and
success criterion. The output of a gate assessment is a gate decision record —
passed, or failed with specific conditions not met — not a meeting summary.

The gate is the last line of demand layer defence. A specification that passes
it has the right to enter the Specify phase. A specification that fails it has
identified exactly which conditions are not met, providing the demand layer with
a specific remediation task rather than a vague sense that something is missing.

---

## Agent Participation in the Demand Layer

Agents in Layer 1 are governed participants, not assistants. The distinction is
substantive: an assistant model implies the agent is augmenting a human who is
doing the core work; a governed participant model recognises that agents may
perform substantive demand layer tasks — demand analysis, pattern identification
across the backlog, value estimation modelling, constraint identification, and
draft specification generation — while remaining subject to explicit governance
controls on their outputs. The change in framing is not cosmetic. It determines
what governance obligations apply.

Under the governed participant model, agents may perform the following demand
layer tasks, subject to the controls stated for each:

- **Demand analysis:** Agents may analyse candidate demand items — assessing
  evidence categories, identifying gaps in validation, and comparing items
  against prior validated needs — and produce analysis outputs for product owner
  review.
- **Pattern identification across the demand backlog:** Agents may identify
  recurring themes, duplicate or near-duplicate demand items, systemic gaps in
  coverage, and prioritisation inconsistencies across the full backlog — tasks
  that are impractical for humans to perform consistently at backlog scale.
- **Value estimation modelling:** Agents may produce quantitative value
  estimates by applying the organisation's documented value models to demand
  item inputs and producing scored outputs for product owner review.
- **Constraint identification:** Agents may surface applicable regulatory,
  security, and architectural constraints based on the demand item's
  classification — providing a constraint candidate list for the specification
  analyst to evaluate, not a definitive constraint set.
- **Draft specification generation:** Agents may produce first-draft
  specifications from validated demand items using established specification
  templates.

All agent-produced outputs in the demand layer are agent-proposed, not
validated. They require human review and explicit human validation before they
contribute to any gate decision or backlog record.

**Epistemic tier labeling requirement.** Any demand layer output produced or
substantially contributed to by an agent must be labeled at the point of
creation and in any governance record that references it. The required label is
one of: _agent-generated_ (the output was produced by an agent with no human
modification) or _agent-proposed, human-reviewed_ (the output was produced by an
agent and reviewed and endorsed by a named human). Neither label may be omitted,
and _agent-proposed, human-reviewed_ requires the reviewing human's name and the
date of review in the record. Demand analysis, backlog scoring, constraint
candidate lists, and draft specifications that do not carry one of these labels
are non-compliant outputs and may not be used in gate decisions.

### Demand Signal Aggregation

Governance agents may monitor business metrics, operational system outputs, and
feedback channels to surface demand signals for human evaluation. A governance
agent that detects a persistent SLO degradation pattern across multiple
deployments, a spike in user feedback on a specific failure mode, or a
regulatory publication that may create new constraints can surface these as
candidate demand items — not as validated demand items. The signal is advisory:
a candidate for human consideration, not a confirmed business need.

The product owner and business demand sponsor evaluate whether a surfaced signal
constitutes a genuine business need. The criteria for that evaluation are the
same as for any other candidate need: is there evidence the signal reflects a
real and material problem, and does the signal meet the validation bar
appropriate to its blast radius tier? The agent does not make that
determination. It identifies signals the human process might otherwise miss due
to volume or monitoring gaps — the operational data stream of a large deployment
may surface dozens of candidate signals per week, more than any human review
process can triage without assistance. Surfacing is not validating.

The distinction matters because an incorrectly surfaced signal consumes
prioritisation attention. If a governance agent surfaces low-quality signals —
signals that are statistically real but commercially insignificant, or signals
that reflect instrumentation artefacts rather than genuine user experience — the
product owner's triage time is spent on noise. Demand layer governance of signal
aggregation agents therefore includes ongoing evaluation of signal quality: what
fraction of surfaced signals, when evaluated, result in validated demand items
entering the backlog. That rate is a measurable output quality indicator for the
aggregation agent, and it must be tracked.

### Specification Pre-Linting

Before a draft specification is submitted for formal gate assessment, a
governance agent may perform a pre-linting pass: checking whether each of the
nine gate conditions has identifiable content in the draft, flagging conditions
where content is absent or structurally incomplete, and reporting specific gaps
to the specification analyst. Pre-linting is structural, not substantive. It
determines whether the shape of a specification is consistent with gate
requirements — not whether the specification satisfies those requirements.

Pre-linting is not a gate assessment and does not determine whether any
condition is satisfied. It is analogous to a compiler's syntax check: it
identifies structural problems before the substantive review, allowing the
specification analyst to resolve obvious gaps before the gate assessment clock
starts. A gate assessment where the specification is missing an out-of-scope
declaration entirely, or where the blast radius tier field is blank, should not
be the point at which that gap is first discovered. Pre-linting catches that
class of omission early. What pre-linting cannot catch is whether the content
present in those fields is correct, complete, or well-reasoned — those are
substantive judgments that require human assessment.

Pre-linting results are advisory; the specification analyst may disagree with a
flag and proceed to gate assessment. The analyst may determine that a field the
agent flagged as absent is actually present under an unconventional heading, or
that a structural pattern the agent did not recognise satisfies the intent of
the condition. The flag is a prompt for review, not a gate condition in its own
right. Pre-linting reports must be clearly labeled as agent-generated, must be
delivered to the specification analyst before the formal gate assessment begins,
and must not be presented to the gate assessment as a substitute for the gate
decision record.

### Backlog Scoring Support

The demand backlog prioritisation criteria defined in this document — business
value, urgency, risk, and strategic alignment — are documented criteria.
Governance agents may apply these criteria to backlog items and produce scored
rankings for product owner review. Because the criteria are explicit and the
inputs (value statements, urgency classifications, blast radius tiers, strategic
priority mappings) are documented artefacts, the mechanical application of the
criteria to a backlog item is a tractable computational task. The agent can
produce a scored ranking across the backlog that the product owner would
otherwise produce manually, with greater consistency and lower time cost.

The product owner retains prioritisation authority; the agent's scoring is
advisory input, not a ranking decision. Where the scoring criteria require
judgment that the agent cannot exercise — assessing strategic alignment in the
context of an undocumented executive conversation, or evaluating the urgency of
a regulatory signal against the organisation's current compliance posture — the
agent must flag those dimensions as requiring human assessment rather than
producing a score. A backlog item that the agent ranks without flagging
unresolvable judgment requirements is more misleading than one that arrives with
explicit gaps marked. The flag is the honest output.

The product owner's review of agent-produced backlog scoring is not a rubber
stamp. It is the step at which the judgment dimensions the agent could not
exercise are applied, where strategic context that is not captured in formal
artefacts is incorporated, and where the ranking is adjusted to reflect the
totality of the organisation's prioritisation intent. An organisation that
accepts agent-produced backlog rankings without this review has not implemented
backlog scoring support — it has delegated prioritisation to an agent, which is
a governance failure under the demand layer's accountability model.

### Demand-to-Specification Translation Support

At Step 2 of the Demand-to-Specification Bridge — translation — governance
agents may assist the specification analyst by producing structured first drafts
of the translated specification. This assistance may include mapping business
need statements to acceptance criteria candidates using the organisation's
established specification patterns, identifying constraint categories likely
applicable to the system type based on prior specifications of comparable scope
and blast radius, and generating a candidate out-of-scope list derived from the
decomposition boundary decisions made in Step 1. The agent produces a draft; the
specification analyst produces the specification.

All translation drafts are reviewed and revised by the specification analyst and
endorsed by domain experts before they constitute a specification. The agent's
contribution compresses the blank-page problem — the time cost of producing a
first draft from scratch — and may improve structural consistency across
specifications by applying established templates mechanically. It does not
compress the specification analyst's judgment work: determining whether the
acceptance criteria candidates are correct, whether the constraint categories
cover the full threat model, whether the out-of-scope list properly bounds the
implementation without excluding needed behaviour. Those are specification
analyst responsibilities that do not transfer to the agent.

An agent-produced translation draft does not satisfy the domain expert
verification requirement in Step 2. That requirement exists because the
translation must be verified by someone who understands the domain, not by
someone who can pattern-match against prior specifications. A domain expert who
has reviewed an agent-produced draft is performing a more substantive review
task than one who has reviewed a specification analyst's draft — because the
domain expert cannot assume the agent has understood the business intent, only
that it has reproduced a plausible structure. Domain expert verification of
agent-produced drafts must therefore be treated as requiring the same rigour as
verification of any other draft, and must not be abbreviated on the assumption
that the agent's output is closer to correct than a human analyst's.

### Governance Requirements for Demand Layer Agents

Governance agents participating in the demand layer are themselves governed
under the ASDLC. Each demand layer agent requires a specification defining its
task scope and the boundaries of its advisory function, an evaluation suite
demonstrating that its output quality meets the standard required for its role
(signal quality rate for aggregation agents, structural coverage rate for
pre-linting agents, scoring consistency and flagging rate for backlog scoring
agents), and a named accountable human who owns the agent's outputs and is
responsible for the quality of the agent's contribution to the demand process.

The blast radius of a demand layer governance agent is determined by the blast
radius of acting on an incorrect agent output. A demand signal that is
incorrectly surfaced wastes prioritisation attention and may crowd out genuine
signals; across a high-volume backlog, that effect compounds. A specification
pre-lint that incorrectly clears a missing constraint — or incorrectly flags a
present one — may allow a flawed specification to reach gate assessment without
the gap being caught, or may delay a correct specification unnecessarily. A
backlog scoring error that misranks high-urgency regulatory work below
lower-priority enhancement work may cause the organisation to miss a compliance
window. These are real consequences; they are smaller than the consequences of
incorrect agent action at the loop or release layer, but they are not trivial.

Demand layer governance agents operate as governed participants under the
epistemic tier labeling requirement stated in this section. All agent outputs
are labeled _agent-generated_ or _agent-proposed, human-reviewed_ at the point
of creation. No demand layer governance decision — signal validation, gate
assessment, prioritisation ranking, or translation verification — may be
recorded as complete solely on the basis of agent output. The agent's
contribution is input to human judgment, not a replacement for it, and the
governance record must reflect which decisions were informed by agent-proposed
content, what human review that content received, and which human accepted
accountability for the decision based on that content. An unlabeled agent output
used in a gate decision is a governance non-conformance.

---

## Feedback from Inner and Outer Loops to Demand

The demand layer is not upstream-only. Evidence flows back from every downstream
layer, and the demand layer must act on that evidence. Treating feedback as
noise — or acknowledging it without changing demand processes — is how
organisations establish systematic patterns of building the wrong things.

**From Layer 2 (validation failures).** When the loop builds the wrong thing
correctly — when verification passes but validation fails — the proximate cause
is almost always in the demand layer. The specification was loop-ready by form:
it passed the gate, it was machine-readable, the acceptance criteria were
testable. But it did not represent the actual business need faithfully. This is
a specification quality failure, and its root cause is in translation (the
specification did not preserve intent) or in validation (the need was not as
well-understood as the validation evidence suggested). A pattern of validation
failures — more than one in three loop iterations, or any validation failure
that reaches a customer-facing system — requires a demand layer retrospective,
not just a loop-level post-incident review.

**From Layer 3 (release failures).** Release gate failures — loop outputs that
fail the release layer's governance checks — frequently indicate scoping or
constraint problems at the demand layer. If the release layer consistently
identifies missing compliance documentation, undiscovered security requirements,
or integration constraints that were not in the specification, the constraint
identification step of the gate is failing. A pattern of release failures that
trace to constraint discovery post-gate is a demand layer calibration signal:
the blast radius assessments and constraint identification pass at the gate are
not thorough enough for the organisation's current deployment environment.

**From Layer 4 (operational failures and value misses).** The most important
feedback signal is whether deployed systems achieve their business success
criterion. If they do not — consistently, across multiple loop iterations — the
demand validation process is producing false positives. Either the needs are
real but the success criteria are set wrong, or the needs are not as real as the
evidence suggested, or the value measurement infrastructure does not exist to
measure outcomes accurately. All three are demand layer failures. A value
realisation rate below 60% over any rolling four-release window is a demand
health emergency, not an engineering quality problem.

**Feedback handling protocol.** Each feedback signal from a downstream layer
must produce a specific demand layer action: an update to the validation
criteria, a change to the translation process, a tightening of the gate
conditions, or a correction to the decomposition heuristics. Acknowledging a
feedback signal without changing a process is not acting on it. The demand
metrics document (`metrics.md`) provides the measurement framework for
tracking whether feedback loops are working.

---

## Roles

Three roles are specific to the demand layer. They are defined here in the
agentic context, where their responsibilities differ meaningfully from their
equivalents in traditional software delivery.

### Product Owner (Agentic Context)

The product owner in the agentic SDLC is accountable for specification readiness
and the success criterion. The fundamental job shift from the traditional
product owner role is this: the agentic product owner produces loop-ready
specifications, not user story backlogs. A user story backlog is an execution
artefact for a team that writes code. A loop-ready specification is a governed
input for a system that verifies outcomes against evidence.

This means the agentic product owner must understand the manifesto's
specification requirements — what machine-readable acceptance criteria look
like, what a complete constraint set contains, what a blast radius assessment
requires — well enough to assess specification readiness without delegating that
judgment entirely to the specification analyst. A product owner who cannot
assess specification readiness cannot govern the demand-to-specification bridge.

The product owner owns the demand backlog, owns the prioritisation criteria and
their consistent application, owns the gate decision records, and owns the
escalation path when validation evidence is insufficient or success criteria are
contested. This is a governance role, not a coordination role.

### Business Demand Sponsor

The business demand sponsor is accountable for business need validation. This
role holds two non-delegatable responsibilities: owning the evidence that the
need is real, and signing off on the success criterion. These responsibilities
cannot be discharged by the product owner or the specification analyst on the
sponsor's behalf — they are the sponsor's claim on the engineering investment,
and the sponsor must be prepared to defend them.

The business demand sponsor is not always a senior executive. At Tier 1 blast
radius, the sponsor may be a team lead or domain manager. At Tier 3, the sponsor
is typically a senior executive or programme director who has accepted personal
accountability for the business outcome. What makes someone the sponsor is not
their seniority — it is their acceptance of accountability for the success
criterion.

The sponsor is the named person who owns the success criterion post-deployment.
If the system ships and does not achieve the criterion, the sponsor is
accountable for that outcome and owns the retrospective. This accountability
structure is what prevents the success criterion from drifting into
unmeasurability: a named accountable person has something at stake in keeping it
precise.

### Specification Analyst

The specification analyst is responsible for the technical translation from
validated need to loop-ready specification. This role bridges domain knowledge
and the manifesto's specification discipline. The specification analyst must
understand the business well enough to decompose a need faithfully and the loop
well enough to scope a specification correctly.

The specification analyst's work is primarily in the demand-to-specification
bridge: running the decomposition step, producing the translated specification,
and supporting the gate assessment. The specification analyst does not own the
validation evidence (that is the sponsor's responsibility) or the success
criterion (that is the product owner's accountability) — but the analyst must be
able to identify when either is insufficient to proceed.

In smaller organisations, one person may hold both the product owner and
specification analyst roles. The responsibilities remain separate: the
accountability for specification readiness (product owner) and the technical
translation work (specification analyst) are distinct functions even when they
are not distinct roles. Merging them into a single person without acknowledging
their different obligations produces a common failure mode: specification
analysts who approve their own translation work without independent domain
verification.

For the organizational evolution perspective — how these roles emerge through
the ASDLC maturity phases and what skills they require — see
[Adoption Roles](../../adoption/roles.md).

---

_The demand layer is the manifesto's prerequisite. The loop is rigorous — it
verifies, validates, learns, and governs. But the rigour of the loop is only as
valuable as the intent it is applied to. The demand layer governs that intent:
ensuring it is real, measurable, scoped, and ready before the first token of
execution is spent._

_The question the demand layer answers, for every item, before the loop runs: is
this the right thing to build, do we know what success looks like, and have we
said clearly what we will not build? Until all three answers are yes, the loop
does not start._
