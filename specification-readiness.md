# Specification Readiness Gate — ASDLC Layer 1→2

_The gate that separates governed demand from engineering execution._

See [Demand & Value](demand/value.md) for how loop-ready specifications are
produced. See the [Manifesto](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto.md) for what the Agentic Loop
requires of a specification. See [Demand Metrics](demand/metrics.md) for how
gate health is measured.

---

## What the Specification Readiness Gate Is

The specification readiness gate is the ASDLC's primary quality control
checkpoint at the Layer 1→2 boundary. A specification that fails this gate is
not ready to enter the Specify phase of the Agentic Loop. The gate is not a
committee approval and it is not a management checkpoint. It is a structured
self-assessment, led by the product owner and specification analyst, that asks a
precise question about each of nine conditions: is this demonstrably true, or is
it not? A specification may be well-intentioned, carefully written, and
enthusiastically sponsored, and still fail the gate. The gate has no interest in
intent — only in evidence. Its purpose is to prevent what the manifesto
identifies as the costliest class of agentic failure: well-executed work on the
wrong problem.

---

## The Nine Gate Conditions

### Condition 1: Business Need Validated

**The condition.** There is documented evidence — not assertion — that the need
is real. The evidence was produced or collected by someone other than the person
who will benefit from the work. It can be examined independently.

**Minimum evidence by risk tier.**

At Tier 1 (low blast radius), and the counts in all three tiers below are
policy-set defaults chosen by the authors rather than calibrated against
outcomes: at least one primary evidence category present and referenced — user
research finding, quantitative data point, regulatory citation, or documented
executive decision. A one-paragraph summary in the specification document with
a link to the source is sufficient.

At Tier 2 (medium blast radius): at least two independent categories of
evidence, with at least one being data-backed or research-backed. The evidence
is documented in a durable artefact separate from the specification, and the
business demand sponsor has explicitly confirmed the need is real.

At Tier 3 (high blast radius — customer-facing, regulated, or decisioning
systems): multiple categories of evidence including at minimum one primary user
research finding and one quantitative data signal. Regulatory or risk assessment
documentation included where applicable. Business demand sponsor sign-off is on
record and references the specific evidence.

**Passing case** — every figure in the specimen below is illustrative, invented for the example. The specification includes: "User research (n=18 interviews,
Q1 2026) established that claims agents spend a mean of 47 minutes per case on
manual lookups that could be automated; supporting data from the operations
dashboard confirms 340 cases per week in scope. The compliance team has
confirmed no regulatory constraints on automation of this specific lookup.
Business sponsor sign-off: [name], [date]."

**Failing case.** The specification states: "The business needs this to improve
operational efficiency — this has been requested by multiple stakeholders."
Multiple stakeholder requests are not validation. The need may be real, but the
evidence is not present.

**Downstream failure mode if bypassed.** The loop produces a technically correct
implementation of an incorrectly understood need. Validate fails. The
organisation discovers it built the wrong thing after the full cost of an
agentic loop iteration, and the root cause is unfindable because no one wrote
down what they thought they were building or why.

---

### Condition 2: Value Measurable

**The condition.** A specific, time-bounded, measurable business success
criterion exists. It states what the business outcome looks like in numbers,
within a defined timeframe, compared to a defined baseline.

**Minimum evidence by risk tier.**

At Tier 1: a single quantifiable success criterion, stated in the
specification. "Reduces analyst lookup time by at least 15 minutes per case,
measured on the first 100 cases after deployment" is sufficient — the figures
are illustrative. The baseline value must be stated.

At Tier 2: a success criterion with a defined measurement method, a named owner,
and a time boundary. The measurement method must exist — it cannot be "we will
figure out how to measure this after deployment."

At Tier 3: a success criterion with documented measurement methodology, a named
accountable owner separate from the specification analyst, a time boundary, and
a mechanism for collecting the measurement data that is confirmed to exist
before loop entry. The business demand sponsor signs off on the success
criterion and its measurement methodology explicitly.

**Passing case**, illustrative in every figure. "Success criterion: mean time to resolution for claims in
category B reduces from 47 minutes (Q4 2025 baseline, n=1,847 cases) to 32
minutes or below, measured over the first 90 days post-deployment. Owner:
[name]. Measurement source: claims operations dashboard, filter: category B,
metric: handle time."

**Failing case.** "Success criterion: improve operational efficiency and reduce
agent frustration." Neither component is measurable, bounded, or owned.

**Downstream failure mode if bypassed.** The loop deploys a system and the
organisation cannot determine whether it worked. The validation step in the loop
has nothing to validate against. Business value assessment is impossible. Worse,
teams learn to assert success without evidence, and the accountability structure
of the outer loop degrades.

---

### Condition 3: Acceptance Criteria Expressible

**The condition.** The need can be expressed as machine-readable acceptance
criteria. A domain expert — not the specification analyst, not the engineer, but
the person who understands the business need — can produce a first draft of the
acceptance criteria before the loop starts. If they cannot, the need is not
well-understood enough to specify.

**Minimum evidence by risk tier.**

At Tier 1: a draft set of acceptance criteria exists in the specification
document. The criteria may be informal ("when a user submits a lookup, the
response appears within 2 seconds" — an illustrative figure) but must be
specific enough to test. The domain expert has reviewed and confirmed them.

At Tier 2: acceptance criteria are written in a format that can be directly
translated into executable evaluations, with explicit pass/fail conditions.
Domain expert sign-off is documented.

At Tier 3: acceptance criteria follow the structured format defined in the
companion requirements engineering framework
(`agentic-engineering-manifesto/companion/re-framework.md`),
covering both behavioural criteria and constraint criteria. They include
adversarial cases and edge conditions. Domain expert review is recorded with
specific sign-off on each criterion category.

**Passing case**, illustrative. "Given a claims agent submits a policy lookup
for a category B claim, the system returns the relevant policy sections within
2 seconds. Given
the policy database is unavailable, the system returns a clear error message and
falls back to the manual lookup workflow without data loss."

**Failing case.** "The system should be fast and helpful and should integrate
well with the existing workflow." None of these are acceptance criteria — they
are descriptions of desired properties with no testable conditions.

**Downstream failure mode if bypassed.** The Specify phase begins without
testable criteria. The agent has no objective function for correctness. The
evaluation portfolio (P8 in the manifesto) cannot be built. Verification becomes
assertion. The evidence bundle contains self-referential confidence rather than
independently verifiable evidence.

**Governance evaluation cases.** The evaluation portfolio that operationalises
Condition 3 must include governance evaluation cases, not only product
evaluation cases. A governance evaluation case tests whether the governance
system worked correctly for this specification's loop iteration — it is not a
test of the product's behaviour. Required governance evaluation cases are:
evidence bundle completeness (all required fields in the evidence bundle are
present and non-empty for this specification type); provenance consistency (the
provenance fields are consistent across artefacts in the same bundle — model
version in the agentic provenance record matches model version in the deployment
configuration, and the tool manifest in the provenance record matches the tool
manifest used during the loop); control state record accuracy (the stated status
for each control in the control state record matches the underlying artefact — a
control state record entry that says `pass` for a control whose supporting
artefact shows a finding is a governance evaluation failure); rollback procedure currency (the rollback procedure test timestamp falls within the policy-set 48-hour freshness window relative to the planned deployment); and SBOM completeness (the
SBOM covers the dependency set that will be deployed, not a prior snapshot).

Governance evaluation failures trigger the same remediation sub-cycle as product
evaluation failures. A failing governance evaluation case blocks the loop output
from proceeding to the release gate, exactly as a failing product evaluation
case does. A governance evaluation suite that has never been run is a governance
system that is trusted rather than verified. A team that has product evaluation
cases but no governance evaluation cases is testing whether they built the right
thing, but not whether they built it in a way that will survive a release gate
audit, an incident investigation, or a regulatory review.

The specification analyst is responsible for ensuring the evaluation portfolio
includes governance evaluation cases. The product owner validates coverage at
the gate assessment. A specification that describes acceptance criteria for the
product but has no governance evaluation cases in the portfolio is not complete.

**Intelligence governance evaluation cases.** For any specification whose
implementation will depend on intelligence governed under the Intelligence
Governance Manifesto (IGM) — claims in the domain graph, provenance-tracked
assertions, or other governed knowledge substrate — the evaluation portfolio
must additionally include a defined set of intelligence governance
evaluation cases. These are tests of the IGM-side governance, distinct from
both product evaluation and ASDLC governance evaluation. Required
intelligence governance evaluation cases are:

- *Confidence-threshold enforcement.* The agent does not act on a claim
  whose epistemic tier is below the threshold defined for the action class
  in the policy envelope. A test in which a claim is degraded to below
  threshold must produce an action refusal or escalation, not a degraded
  action.
- *Contradiction detection.* When the domain graph contains a contradiction
  on a claim the agent depends on, the agent surfaces the contradiction
  rather than silently selecting one side. The evaluation case must cover
  each contradiction type the system's domain is known to produce
  (jurisdictional divergence, logical contradiction, temporal supersession,
  scope variation, extraction error).
- *Decay-window compliance.* The agent does not act on a claim whose decay
  window has expired without a current re-validation event. A test in which
  a claim's decay window is advanced past expiry must produce a refusal or
  escalation; an action taken on a decayed claim is a governance failure
  even if the action would have been correct.
- *Feedback-loop closure.* For systems where the L4 → Intelligence
  Lifecycle feedback path applies (see `asdlc.md` Feedback Paths and IGM
  Principle 10), the evaluation portfolio includes a case in which a
  simulated production incident produces a structured intelligence-feedback
  artefact identifying the implicated claims and the appropriate IGM
  authorities. A system that handles incidents without producing this
  artefact has an open feedback loop and fails this case.

Intelligence governance evaluation cases are required for any system
depending on intelligence — they are not waived by autonomy tier. The
specification analyst, in consultation with the IGM authority responsible
for the relevant claim class, ensures coverage. A specification that
declares dependency on the domain graph but does not include intelligence
governance evaluation cases is incomplete for Condition 3.

---

### Condition 4: Constraints Identified

**The condition.** All known constraints on the implementation are documented
before loop entry: security requirements, compliance obligations, data
classification rules, domain ownership boundaries, performance envelopes,
integration constraints, and any known limitations on the solution space.
Constraints discovered after the Specify phase begins are scope failures, not
verification failures.

**Minimum evidence by risk tier.**

At Tier 1: a constraint section in the specification that addresses security and
data handling at minimum. Explicit statement of what the implementation is not
permitted to do. Known integration constraints listed.

At Tier 2: a complete constraint inventory reviewed by the security team (or
equivalent) and the relevant domain owners. Compliance team sign-off for any
specification that touches regulated data or regulated processes. Constraints
referenced by their source (policy document, regulation article, architectural
decision record).

At Tier 3: formal constraint review with documented sign-offs from security,
compliance, architecture, and affected domain owners. Constraints classified by
type (hard constraints that are not negotiable versus soft constraints that are
preferences). For regulated industries, constraints mapped to the relevant
regulatory framework with citations. An explicit statement that all known
constraints have been identified, signed by the business demand sponsor.

**Threat modeling.** For agentic specifications, threat modeling is a required
component of constraint identification. At Tier 2 (medium blast radius), a
threat model using a structured methodology — STRIDE or equivalent — must be
produced covering the specification's external interfaces, data flows, and trust
boundaries. The threat model output — identified threats, proposed mitigations,
and accepted residual risks — must be present in the constraint inventory before
the gate is assessed. At Tier 3 (high blast radius), the threat model is
formally reviewed by the security function. The minimum threat surface below is
consistent with the OWASP LLM Top 10 (https://genai.owasp.org/llm-top-10/),
the OWASP *Agentic AI — Threats and Mitigations* guidance
(https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/), and
the formal attack taxonomy in NIST AI 100-2e2025, *Adversarial Machine
Learning: A Taxonomy and Terminology of Attacks and Mitigations*
(https://doi.org/10.6028/NIST.AI.100-2e2025). For agentic specifications at
Tier 2 and above, the threat model must address all of the following
categories as a required minimum scope. Each category must be explicitly covered: the threat
model must document either a concrete mitigation or a justified out-of-scope
declaration for each. At Tier 3, the security function reviews the completeness
of that coverage.

The required minimum threat categories for agentic specifications are:

_Prompt injection — direct and indirect._ Adversarial inputs embedded in user
instructions, tool outputs, retrieved documents, or any other content processed
by the agent that redirect agent behaviour in ways not authorised by the
principal hierarchy. Indirect prompt injection — where the adversarial content
arrives through the environment rather than directly from the user — is the more
common attack surface in agentic pipelines and must be addressed explicitly.
Acceptance criteria must include evaluation against known prompt injection
patterns relevant to the agent's tool and retrieval surface.

_Insecure output handling._ Agent outputs consumed downstream without
sanitisation or validation — structured data passed to interpreters, databases,
code execution environments, or downstream agents without appropriate encoding,
schema validation, or trust boundary enforcement. In multi-agent pipelines,
outputs from one agent become inputs to the next; each handoff is a potential
injection point. Constraints must specify how agent outputs are validated before
being acted upon by any downstream component.

_Training data poisoning and RAG corpus poisoning._ Data used to train,
fine-tune, or supply retrieval context for the model is compromised, causing the
model to produce systematically biased, incorrect, or adversarially influenced
outputs. For agentic specifications using retrieval-augmented generation,
retrieval corpus poisoning — where adversarial content is introduced into the
indexed knowledge base — is the operationally relevant attack path and must be
addressed independently of training-time poisoning. Constraints must specify
data provenance controls and corpus integrity verification procedures for any
retrieval system the agent depends on.

_Model denial of service and cost exhaustion._ Adversarial inputs or
environmental conditions that cause excessive token consumption, recursive tool
calls, runaway agent loops, or unbounded memory growth, resulting in service
degradation or costs that exceed the value of the work being performed. The
token budget constraint (required separately under this condition) is the
primary mitigation, but the threat model must also address adversarial patterns
specifically designed to trigger resource exhaustion — for example, inputs
crafted to maximise context window usage or trigger repeated tool invocations.

_Supply-chain vulnerabilities._ Compromise of any component in the model
delivery and execution chain: the model itself, system prompts and instruction
sets, fine-tuning datasets, tool definitions, plugin or MCP server
implementations, embedding models, and third-party libraries used in the agent
runtime. A compromised component anywhere in the supply chain can subvert the
agent's behaviour regardless of the correctness of the specification.
Constraints must identify the components in scope, their provenance, and the
controls used to verify their integrity before deployment.

_Sensitive information disclosure._ The agent revealing training data, system
prompts, internal orchestration state, memory contents, or confidential data
from the retrieval corpus — either through direct extraction attacks or through
inference from model behaviour. In agentic systems, the attack surface includes
not only the model's parametric knowledge but also any data in the agent's
context window, working memory, or tool call history at the time of the
disclosure. Constraints must specify what information classifications are in
scope, how system prompts and internal state are protected, and what retrieval
corpus contents are sensitive.

_Insecure plugin and tool design; tool authorisation._ Tools or plugins
accessible to the agent that lack sufficient authorisation checks, carry overly
broad permission scopes, accept unvalidated inputs, or expose administrative or
destructive operations that the agent's role does not require. The principle of
least privilege applies to tool grants: the agent must be granted only the
specific tool permissions required to accomplish the specified scope, with no
ambient access to broader capabilities. Constraints must enumerate each tool the
agent is permitted to invoke, the permission scope of each, and the
authorisation check that prevents the agent from invoking tools outside its
defined role.

_Excessive agency._ The agent taking actions beyond the scope of its defined
role — reading, writing, or invoking capabilities that its specification does
not authorise, particularly in multi-agent or tool-using contexts where the
blast radius of an out-of-scope action may be large. Excessive agency is
distinct from tool abuse: tool abuse is an external actor manipulating the
agent; excessive agency is the agent itself expanding beyond its mandate due to
ambiguous instructions, insufficiently scoped tool grants, or inadequate
human-in-the-loop checkpoints. Acceptance criteria must include explicit
coverage of what actions the agent is not permitted to take, and the constraint
inventory must document how those prohibitions are enforced at runtime.

_Overreliance._ Downstream systems or human operators accepting agent outputs
without appropriate validation — particularly for high-consequence decisions
where the agent's output is used directly without independent verification. In
agentic pipelines, overreliance risk increases when agents are composed in
chains, because errors propagate and accumulate before any human reviews the
result. Constraints must specify the validation checkpoints required before
agent outputs are acted upon, and acceptance criteria must include evaluation of
agent behaviour on inputs where the correct output is rejection or escalation
rather than a confident answer.

_Model theft and system prompt extraction._ Extraction of model weights,
fine-tuning data, system prompt contents, or proprietary instruction sets
through adversarial querying — including membership inference attacks, prompt
extraction through repeated probing, and model inversion. For agentic
specifications, the system prompt frequently encodes proprietary orchestration
logic and role definitions whose disclosure would undermine trust boundaries
across the agent hierarchy. Constraints must specify what model components and
instruction content are considered confidential and what controls prevent their
extraction through adversarial interaction.

_Memory poisoning._ Adversarial content injected into persistent agent memory
stores — episodic memory, semantic memory, or shared state accessible across
agent invocations — causing the agent to retrieve and act on corrupted or
adversarially crafted context in future interactions. Memory poisoning is a form
of persistent prompt injection: the adversarial payload is written to memory in
one session and triggered in a later session, potentially by a different user or
in a different operational context. Constraints must specify memory provenance
controls, sanitisation procedures for content written to persistent memory, and
monitoring for anomalous memory content.

_Principal impersonation._ An agent or external actor falsely claiming a
higher-authority principal identity — impersonating a human operator, a senior
agent in the hierarchy, or an authorised orchestrator — in order to obtain
elevated permissions, override safety constraints, or redirect the agent's
behaviour. In multi-agent architectures, principal verification is a structural
requirement: agents must not accept elevated-authority instructions from any
source that cannot be cryptographically or structurally verified as holding that
authority. Constraints must specify how the agent verifies the identity and
authority of principals whose instructions it acts upon.

These categories are distinct from generic application security threats and
require explicit coverage in the threat model. The threat model is not satisfied
by a general statement that security has been considered — each category must be
addressed individually with a documented mitigation or a justified out-of-scope
declaration. At Tier 3, the security function confirms the completeness of this
coverage as part of the Technical Readiness Sub-Gate.

**Data protection impact assessment.** For specifications where the
implementation will process personal data at scale or involve automated
individual decision-making — automated credit decisions, insurance underwriting,
recruitment screening, claims triage, and equivalent high-risk processing
activities — a Data Protection Impact Assessment (DPIA) must be initiated before
the gate is assessed, per GDPR Article 35 and equivalent privacy legislation.
The DPIA does not need to be complete at gate time: it must be initiated, with
the preliminary risk assessment documented and attached to the constraint
inventory. Discoveries from the DPIA that affect the specification scope or
blast radius must update those sections before loop entry. This applies at Tier
2 and above.

**Regulatory constraint currency.** For specifications with regulatory-derived
constraints, the specification analyst must confirm at gate time that the
regulatory source versions underlying those constraints are current as of the
gate date. A constraint derived from a regulatory source that has been updated
since the constraint was written is a stale constraint — the constraint wording
may or may not still reflect the current regulatory requirement, but that
determination must be made explicitly, not assumed. The regulatory context map
(maintained by the demand intelligence function) provides the source version
check. A constraint inventory that references regulatory sources without
confirming their current version is incomplete for the purposes of Condition 4.

**Token budget.** For agentic specifications, a maximum token budget per loop
iteration is a required hard constraint at Tier 2 and above. The token budget
defines the ceiling on total tokens consumed by the agent — input, output, and
context — across the loop iteration. Agent executions that approach the budget
ceiling must either complete with degraded but safe output or abort and escalate
to a human; they must not continue indefinitely at unbounded cost. The token
budget is set based on the cost model applicable to the model tier being used
and the organisation's cost threshold for the specification's blast radius tier.
The token budget is a governance constraint, not a performance target: exceeding
it without escalation is a constraint violation.

**Accessibility.** For specifications whose output includes user-facing
interfaces accessible to the public or to a regulated population of users,
accessibility conformance is a required constraint. The specification must state
the required conformance level. WCAG 2.2 Level AA is the minimum required by EU
Directive 2016/2102, UK Accessibility Regulations 2018, and equivalent
legislation in most jurisdictions for public-sector and publicly-available
digital services; the applicable standard and level may differ by jurisdiction
and user population. Accessibility constraints discovered after specification
entry that require interface redesign are scope failures.

**Passing case.** "Constraints: (1) All policy data is classified as
confidential — no logging of policy content to application logs. Reference: data
classification policy v2.3, Section 4. (2) Response time must not exceed 3
seconds at P95 — hard constraint from the SLA for claims handling tools. (3) The
implementation must not modify the claims data store directly — read-only access
only. Reference: domain boundary agreement, claims domain, ADR-047. (4) Threat
model (STRIDE) produced covering the lookup API interface and the policy data
flow — identified threats: data exfiltration via malformed query; mitigation:
input validation and query parameterisation; residual risk: accepted. (5) DPIA
initiated — preliminary risk assessment attached; no discoveries requiring scope
revision at this stage. (6) Maximum token budget per loop iteration: 200,000
tokens (input + output + context); escalation trigger at 180,000."

**Failing cases.** "Constraints: TBD — will be confirmed with compliance and
architecture during development." This means constraint discovery has been
deferred into the loop. If a compliance constraint surfaces at the Verify phase,
the entire loop iteration may need to restart.

"Constraints: We will assess data protection requirements during development."
Data protection constraints discovered after loop entry are scope failures. GDPR
Article 35 imposes a mandatory pre-processing obligation for high-risk
processing activities; deferring the DPIA assessment converts a legal
requirement into a compliance incident.

"Constraints: No token limit specified — the agent will use as much context as
it needs." An unbounded token budget is not a constraint — it is the absence of
one. An agent executing against an unconstrained token budget can generate costs
that exceed the value of the work being done before anyone is notified.

**Downstream failure mode if bypassed.** Compliance and security constraints
surface mid-loop, requiring specification revision after engineering work has
begun. The loop restarts. In regulated environments, undiscovered constraints at
Verify or Validate can trigger compliance incidents. Bypassing threat modeling
means the agentic loop executes without a documented understanding of how the
system can be attacked. Adversarial inputs that the loop never considered can
exploit the agent in production before evaluation suites cover the attack
pattern. In all environments, constraint discovery inside the loop is more
expensive than constraint discovery before it.

---

### Condition 5: Accountable Human Named

**The condition.** A named person has accepted business-level accountability for
the outcome of this specification before the loop runs. This person owns the
success criterion, not the implementation. They are the P12 anchor, established
upstream of the loop.

**Minimum evidence by risk tier.**

At Tier 1: the product owner is named in the specification as the accountable
human. This is acceptable for low-blast-radius internal tooling where the
product owner has the authority to accept the outcome.

At Tier 2: the business demand sponsor is named as the accountable human,
separate from the product owner. The sponsor's explicit confirmation of
accountability is recorded in the specification or the gate decision record.

At Tier 3: a named senior accountable human with the organisational authority to
accept the business outcome is recorded, with a statement of what they are
accountable for (the success criterion, the downstream business impact, and the
response if the success criterion is not met). This person is not the engineer,
not the specification analyst, and not the product owner — they are the business
decision-maker.

**Passing case.** "Accountable human: [Name], Head of Claims Operations.
Accountable for: business success criterion (mean time to resolution target,
90-day measurement window). Responsibility if not met: initiates post-deployment
retrospective and owns the remediation decision."

**Failing case.** "Accountable human: the project team." A team is not a named
human. If the system ships and the success criterion is not met, the absence of
a named accountable human means no one owns the outcome.

**Downstream failure mode if bypassed.** The loop produces an output with no one
accountable for whether it worked at the business level. The manifesto's Govern
phase becomes a formality — there is no human to accept the evidence bundle and
no named person to surface the outcome signal. Post-deployment value measurement
is no one's job.

---

### Condition 6: Blast Radius Assessed

**The condition.** A preliminary assessment of the maximum credible impact if
the implementation fails has been conducted and documented. The assessment
covers both technical blast radius and governance failure blast radius. Both
inform the autonomy tier for the loop execution and the scope of the evidence
bundle required.

**Technical blast radius** is the operational harm if the implementation fails
in production: scope of affected users, systems, and processes; severity of
disruption, data loss, or financial impact; detectability; and reversibility.

**Governance failure blast radius** is a distinct and separately assessed
dimension. It is the governance harm that results if this specification enters
the loop and produces output that passes controls but should not have.
Governance failures of this type include: evidence laundering — where the gate
is passed on the basis of evidence that satisfies form but not substance, and
the loop produces an artefact that carries a misleading governance
certification; premature autonomy tier elevation — where a specification is
classified at a lower blast radius than its actual risk profile, causing the
loop to execute with insufficient oversight; and waiver accumulation — where a
specification with multiple waived conditions enters the loop and the combined
waivers erode the governance system's integrity beyond what any single waiver
would justify.

Governance failure blast radius is elevated when the specification involves
novel agent autonomy capabilities not previously governed by the ASDLC; first
use of a new model, framework, or tool type in the organisation's agentic
footprint; cross-system boundary changes that affect multiple domain ownership
boundaries simultaneously; or re-use of a specification structure from a prior
context in a new context where its assumptions may not hold. High governance
blast radius specifications require elevated validation rigor proportionate to
their governance risk, independently of their technical blast radius tier.

**Minimum evidence by risk tier.**

At Tier 1: a one-paragraph blast radius statement covering both dimensions: what
could go wrong technically, who would be affected, how quickly it could be
reversed; and whether any of the governance failure blast radius elevation
indicators apply to this specification. If neither technical nor governance
blast radius indicators are elevated, Tier 1 is confirmed.

At Tier 2: a structured blast radius assessment covering technical dimensions
(scope of impact, severity, detectability, reversibility) and an explicit
governance failure blast radius section addressing the four elevation
indicators. The assessment must confirm the appropriate autonomy tier across
both dimensions. Where technical blast radius is Tier 1 but governance blast
radius indicators are elevated, the combined assessment must reflect the higher
tier.

At Tier 3: a formal blast radius assessment reviewed by risk, security, and
architecture, covering both dimensions. Impact modelling for the worst-case
technical failure scenario. An explicit governance failure blast radius
assessment, reviewed by the governance function, addressing the full set of
elevation indicators and documenting the elevated validation rigor required. The
autonomy tier assignment is justified against both dimensions. The assessment is
a named document, version-controlled.

**Passing case.** "Technical blast radius: the lookup feature is read-only with
no write path to any production data store. Failure modes are limited to
incorrect lookup results (detected by agents within a single transaction) and
service unavailability (falls back to manual workflow). No regulatory reporting
impact. No customer data exposed. Governance failure blast radius: this
specification uses established frameworks with prior ASDLC coverage; no novel
autonomy, no new tool types, no cross-domain boundary changes; no elevation
indicators present. Combined blast radius: Tier 1."

**Failing case.** "Blast radius: low." Tier labels without assessment are not
assessments. The label may be correct, but it is unverifiable, and it addresses
only the technical dimension — the governance failure blast radius has not been
assessed at all.

**Downstream failure mode if bypassed.** If technical blast radius is
unassessed: the loop runs at the wrong autonomy tier, either with insufficient
governance (increasing the risk of undetected failures) or with excessive
governance that degrades into rubber-stamping. If governance failure blast
radius is unassessed: specifications with elevated governance risk enter the
loop at standard rigor, and the governance system produces outputs — evidence
bundles, control state records, autonomy tier assignments — that carry
misleading certification. The damage from governance failure blast radius is not
visible in production metrics; it is visible when a gate audit, an incident
investigation, or a regulatory review reveals that the governance record does
not reflect the actual governance that occurred.

---

### Condition 7: Out-of-Scope Explicitly Stated

**The condition.** The specification includes an explicit list of what it does
not include. Scope boundaries must be named, not assumed. Absent explicit
out-of-scope declarations, scope expands during execution.

**Minimum evidence by risk tier.**

At Tier 1: a policy-set minimum of two explicit out-of-scope statements. These
may be brief: "Out of scope: integration with the legacy claims UI (separate
initiative); bulk export functionality."

At Tier 2: a complete out-of-scope section that addresses: functionality
explicitly not included, user segments not served by this specification, systems
not in scope for integration, and edge cases not covered. Reviewed and confirmed
by the business demand sponsor.

At Tier 3: a formal scope boundary document, reviewed and signed off by all
affected domain owners. The out-of-scope statements are cross-referenced to the
blast radius assessment to confirm that excluded items are genuinely excluded
from the blast radius calculation.

**Passing case.** "Out of scope: (1) Modification of any claims data — this
specification is read-only. (2) Claims in categories C and D — the lookup logic
differs and will be addressed in a subsequent specification. (3) Mobile access —
desktop agent workflow only for this iteration. (4) Bulk or batch lookup —
single-case lookup only."

**Failing case.** No out-of-scope section. The loop begins with an implicit
assumption that scope is whatever is not explicitly in scope. Inside the loop,
agents interpret ambiguous scope boundaries generously, and the specification
drifts.

**Downstream failure mode if bypassed.** Specification drift inside the loop.
The agent or the engineer extends the implementation to cover cases that were
not specified, because the absence of out-of-scope boundaries makes the
extension seem reasonable. The evidence bundle grows. The blast radius expands.
The autonomy tier calibration becomes incorrect. The release layer receives a
loop output that is larger and less well-tested than the specification implied.

---

### Condition 8: Loop Cost Justified

**The condition.** The expected value of the work exceeds the expected cost of
running the loop to produce it. This is a named, explicit condition that must be
answered before the loop starts. "We have not estimated whether this is worth
building given the loop cost" is a gate failure.

The loop cost is not free. It includes engineering time (human effort in the
Specify, Build, Verify, Validate, and Govern phases); agent inference cost
(token consumption at the model tier being used across the full loop iteration,
including evaluation runs); governance overhead (gate preparation time, reviewer
participation, control filing, compliance documentation); and the cost of
validation (evaluation suite construction and execution, including governance
evaluation cases). Each of these costs is incurred whether or not the loop
produces a deployed output. A loop iteration that reaches Verify and then fails
is not a partial cost — it is the full loop cost without the value.

This condition does not require a precise financial model. It requires a named,
honest answer to the question: given what this loop will cost to run, does the
expected business outcome justify running it? A rough order-of-magnitude
estimate is sufficient evidence. What is not sufficient is silence — the absence
of any estimate.

**Minimum evidence by risk tier.**

At Tier 1: a brief written statement confirming that the expected value
(referencing the success criterion from Condition 2) exceeds the estimated loop
cost. The estimate does not need to be itemised — a one-paragraph judgement is
acceptable. The statement must be explicit: "we have considered loop cost and
the expected value justifies it" is evidence; no statement at all is a gate
failure.

At Tier 2: a loop cost estimate with at minimum four named components: estimated
engineering time (in person-days), estimated inference cost (in approximate
token volume and cost at the applicable model tier), estimated governance
overhead (gate sessions, reviews, compliance filing), and estimated validation
effort. The estimate is compared against the expected value defined in Condition
2's success criterion. The business demand sponsor confirms that the comparison
supports loop entry.

At Tier 3: a formal demand economics assessment covering all four loop cost
components with sourced estimates, compared against the quantified expected
value from Condition 2. The assessment must address the cost of a loop failure —
i.e., what the organisation pays if the loop runs to completion and the output
fails validation or does not achieve the success criterion. The business demand
sponsor and finance function (or equivalent) sign off on the assessment.

**Passing case**, illustrative throughout. "Expected value: reduction of 15 minutes per case across 340
cases per week yields approximately 85 person-hours per week of capacity
recovered. At fully-loaded cost, that is approximately £X per quarter. Loop cost
estimate: 8 person-days engineering, £Y inference at the model tier planned, 3
gate sessions estimated at 2 hours each, evaluation suite construction estimated
at 3 person-days. Loop cost is estimated at well under one quarter's value
delivery. Loop entry is justified."

**Failing case.** "We will assess ROI after deployment." Post-deployment ROI
assessment is not a pre-loop justification. The loop cost is committed at loop
entry, not after deployment. A team that cannot state the expected value before
the loop starts cannot verify the actual value after it — and has provided no
basis for the loop cost decision.

"This is a regulatory requirement, so cost justification does not apply."
Regulatory requirements reduce option value (the organisation may have no choice
about compliance) but they do not eliminate the need for loop cost estimation. A
regulatory obligation is best met by the most cost-effective loop execution that
satisfies the constraint — understanding loop cost is how the organisation makes
that choice.

**Downstream failure mode if bypassed.** The loop runs without a cost commitment
or a value commitment. When the loop completes, there is no basis for
determining whether running it was a good decision, because the expected cost
and expected value were never stated. Worse, the governance system loses a
mechanism for catching loops that should not be run at all — specifications that
are individually low-value and individually low-cost, but that, in aggregate,
consume governance capacity that should be reserved for higher-value work.

---

### Condition 9: Context Thread Assembled and Reviewed

**The condition.** Before the specification enters Layer 2, a context thread has
been assembled by a governance agent and reviewed by the specification analyst.
The context thread provides the executing agent with the governance lineage of
the specification — the story of why the specification says what it says —
enabling calibrated behaviour inside the loop rather than operation on the
specification as if it were self-contained. An absent or unreviewed context
thread means the executing agent lacks provenance context that costs little to
provide and materially reduces the risk of specification misinterpretation.

**Minimum content requirements.** The context thread must contain at minimum:

- The demand item's validation evidence summary: type, source, and recency.
- The blast radius rationale: why the specification was assigned its current
  blast radius tier and what the key risk factors were.
- The two most relevant comparable specifications from organisational memory,
  with the loop learnings from each — what worked, what failed, and what
  constraints were discovered only inside the loop.
- Any active waivers on related deployed systems that the executing loop should
  be aware of: a waiver on a constraint in a sibling system may be directly
  relevant to the executing agent's decision space.

**Assembly and review.** The context thread is assembled by a governance agent
from the governance graph and filed as an agent-proposed EvidenceArtifact. The
specification analyst reviews the context thread and confirms it accurately
represents the demand layer decisions before the gate is assessed. The
specification analyst's review is the gate condition — an agent-assembled but
unreviewed context thread does not satisfy Condition 9. The context thread does
not add requirements to the specification. It provides provenance.

**Minimum evidence by risk tier.**

At Tier 1: a brief context thread summarising the validation evidence and
identifying any directly comparable prior specification. The specification
analyst confirms it accurately represents the demand item. A one-paragraph
summary is sufficient.

At Tier 2: a structured context thread covering all four minimum content
elements above. The specification analyst sign-off is documented.

At Tier 3: a full context thread with explicit demand layer decision points
documented, blast radius rationale with supporting evidence, two or more
comparable specification references with loop learnings, and active waiver
inventory for related deployed systems. The specification analyst sign-off is on
record and names the governance graph version from which the thread was
assembled.

**Passing case.** "Context thread assembled [date] from governance graph v2.7.
Validation evidence: user research (n=18, Q1 2026), quantitative operations data
(340 cases/week baseline). Blast radius: Tier 1, read-only implementation, no
write path, no customer data exposure. Comparable specifications: Spec-0047
(claims lookup v1, 2025-Q2) — loop learning: constraint on response time at P95
was discovered post-gate; added to this specification's constraints
pre-emptively. Spec-0061 (policy retrieval, 2025-Q3) — loop learning: domain
expert verification missed an edge case in category B; this specification
includes explicit category B test coverage. Active waivers: none on related
systems. Specification analyst reviewed and confirmed: [name], [date]."

**Failing case.** No context thread present, or a context thread assembled but
not reviewed by the specification analyst. The executing agent receives the
specification without governance lineage, and the demand layer's L1 decisions —
why certain constraints were set, what trade-offs were accepted, what prior
loops revealed — are invisible to the execution layer.

**Downstream failure mode if bypassed.** The executing agent at Layer 2 operates
on the specification as if it were self-contained. It cannot calibrate to the
demand layer's priorities, cannot benefit from prior loop learnings on
comparable specifications, and may not know that active waivers on related
deployed systems affect the interpretation of its own constraints. Errors that
comparable specifications already made are repeated. Specification
misinterpretation that the governance lineage would have prevented goes
undetected until Verify or Validate. The cost of restarting the loop at that
point consistently exceeds the cost of assembling the context thread before
entry.

---

## Assessment Process

The gate assessment is a structured conversation, not a document review. The
product owner leads it. The specification analyst participates as the technical
resource on specification quality. The business demand sponsor should be
available for questions on Conditions 1, 2, 5, and 8 (validation evidence,
success criterion, accountability, and loop cost justification). For Tier 3
specifications, the security and compliance representatives who reviewed the
constraint inventory should be available for questions on Condition 4.

**Duration**, policy-set throughout — these are the authors' planning figures, not observed session lengths. At Tier 1 in a mature team: 30 minutes. The product owner and
specification analyst work through the nine conditions against the specification
document. Most conditions will be satisfied by prior work; the gate confirms it.
At Tier 2: 60–90 minutes. At Tier 3: a formal session, typically 2–3 hours, with
the full set of reviewers. In regulated contexts, the session may require
external validation against the relevant regulatory framework.

### Product and Technical Sub-Gates

The nine conditions naturally divide into two categories with different reviewer
profiles. Organising the assessment as two sequential sub-gates — with the
option to parallelise the second sub-gate against late-stage specification
refinement — reduces the coordination burden without reducing the rigour.

**Product Readiness Sub-Gate:** Conditions 1, 2, 3, 5, 7, 8, and 9. Assessed by
the product owner and specification analyst, with the business demand sponsor
available for questions. These conditions require product and domain knowledge,
not technical architecture expertise. At Tier 1 and Tier 2, this sub-gate can be run in a policy-set 30–60 minute structured session without external participants.
Condition 9 (context thread assembled and reviewed) is typically the last action
before the sub-gate session — the governance agent assembles the thread from the
governance graph and the specification analyst confirms it as part of the
sub-gate preparation rather than as a separate step.

**Technical Readiness Sub-Gate:** Conditions 4 and 6. Assessed with
participation from the security function (threat model review, data
classification confirmation), the architecture function (domain boundary
confirmation, blast radius assessment), and the compliance function (constraint
completeness against applicable regulatory obligations, DPIA status). At Tier 3,
this sub-gate is a formal session with sign-off from each function.

Both sub-gates must produce passing decisions before the combined gate decision
record records a pass. A specification where the Product Readiness Sub-Gate
passes but the Technical Readiness Sub-Gate fails is still a gate failure.
Parallelising them is permitted when the specification is sufficiently mature
that both assessments have meaningful material to assess — beginning the
Technical Sub-Gate against an incomplete constraint inventory is not
parallelisation, it is premature assessment.

**What the gate produces.** A single artefact: the gate decision record. It
contains:

- Date of assessment.
- Specification name and version.
- Names of all assessors.
- Decision: passed or failed.
- If passed: a statement that all nine conditions are satisfied, with a one-line
  confirmation for each.
- If failed: the specific conditions not met, the specific evidence missing or
  insufficient, and the specific remediation required before re-assessment.

The gate decision record is stored with the specification. For Tier 2 and Tier 3
specifications, it is version-controlled and retained as part of the audit
trail.

**What a gate failure means.** A gate failure is not a setback — it is the gate
working correctly. It means the specification has identified a specific gap
before the loop started. The product owner and specification analyst have a
precise remediation task rather than a vague sense that something is wrong. The
gap is filled, the condition is re-assessed, and the gate decision record is
updated. A specification that fails the gate twice on the same condition has a
systemic demand layer problem, not a specification quality problem.

### Live Gate State

The Specification Readiness Gate is not only assessed at a point in time — it
has a live state that can be inspected continuously. Each of the nine conditions
has a current GateState drawn from the governance graph. The GateState of a
condition is one of seven values: **pass** — the condition is satisfied by
current, non-stale evidence; **fail** — the condition is actively not met,
because a specific required element is absent or incorrect; **missing** — no
evidence or artefact for this condition has been submitted yet; **stale** —
evidence was previously accepted but a triggering event has occurred since it
was filed, making it no longer current; **contradicted** — two pieces of
evidence for this condition conflict with each other; **waived** — the condition
has been formally waived with accountable human approval, a documented
compensating control, and a recorded expiry date (see Waiver Governance); and
**requires-human-decision** — the condition cannot be assessed by an agent and
requires human judgment.

`missing` and `stale` are distinct from `fail`, and the distinction carries
operational meaning. A specification with no threat model has not failed
Condition 4 — no threat model has been attempted. A specification with a threat
model that was accepted but is now stale — because the architecture changed
after the model was filed — has a stale Condition 4. In both cases, the Threat
Model Agent can produce a draft that moves the condition toward `pass`, pending
human review. A specification where the threat model was submitted and actively
failed review has a `fail` state that requires understanding and correcting the
specific deficiency. These are three different situations that require three
different responses, and conflating them obscures the remediation path.

The GateState of each condition changes over time without a new gate assessment
being triggered. A condition that passed because a compliant threat model was
filed moves to `stale` when a triggering event occurs — a material architecture
change, a tool manifest change, a data source change, or a model version change
— not on a calendar schedule. The gate does not need to be re-opened for this to
happen — the state changes continuously as conditions change. This means the
governance graph reflects the current adequacy of each condition at any moment,
not only at the moment of the gate decision.

A gate is not passed once and forgotten. A specification that passed the
Specification Readiness Gate months ago may have conditions in `stale` or
`contradicted` state if the specification or its linked evidence has changed
since the gate decision. The gate decision record captures when the gate was
passed; the current GateState of each condition records whether it is still
satisfied now. Both are necessary: the gate decision record is the historical
audit trace, and the live GateState is the current governance signal.

### Evidence Freshness

Freshness is the property that makes evidence current: evidence satisfying a
gate condition is fresh if none of the triggering events for staleness have
occurred since it was filed. Staleness is event-triggered, not
calendar-triggered. A specification that was ready yesterday and has had none of
the triggering events — no stakeholder change, no business context change, no
technology assumption change, no scope change, no dependency landscape change —
is still ready today regardless of calendar age. The triggering events for each
condition are defined below.

**Condition 1 (Business Need Validated).** The validation evidence remains
current until the business context changes materially — a market shift, a
regulatory change, or a business priority reprioritisation. There is no fixed
calendar window; staleness is event-triggered. A user research study conducted
two years ago remains current if the business context it documented is
unchanged. The same study becomes stale the moment a regulatory change or a
material market shift alters the need it was validating.

**Condition 2 (Value Measurable).** The measurement method and measurement owner
remain current until the measurement infrastructure changes or the success
criterion is revised. Staleness is event-triggered by specification revision. A
success criterion that survives into a new loop iteration unchanged, with the
same measurement method and the same named owner, remains current. Revising the
criterion — or discovering that the measurement source has changed — triggers a
freshness review.

**Condition 3 (Acceptance Criteria Expressible).** The acceptance criteria
remain current for the duration of the loop iteration. Any material revision to
acceptance criteria after loop entry triggers a gate failure review. The gate is
not re-run for minor clarifications that do not change the pass/fail conditions
— it is re-run when the criteria change in ways that affect what the loop is
being asked to prove.

**Condition 4 (Constraints Identified).** The threat model must be refreshed on
any material architecture change, tool manifest change, data source change, or
model version change. There is no fixed calendar window — staleness is triggered
by changes to the system's attack surface. A threat model filed against a system
that has since added a new external API integration is stale for that
integration, even if it was filed last week. The constraint inventory must be
reviewed at each new loop iteration against the current system state; a
constraint inventory that was adequate for a prior iteration may be incomplete
for a current one.

**Condition 5 (Accountable Human Named).** The accountable human assignment
remains current as long as the named person is in the role. Personnel changes
that affect the accountable human trigger immediate staleness; a replacement
must be named before the next loop iteration or release gate. A named
accountable human who has left the organisation or changed roles is not a valid
P12 anchor, regardless of when they were named.

**Condition 6 (Blast Radius Assessed).** The blast radius assessment must be
revisited on any material scope change, capability expansion, or integration of
new external systems. Staleness is event-triggered. A blast radius assessment
that rated the specification as Tier 1 becomes stale if the specification
subsequently acquires a write path to a production data store that was not
present when the assessment was conducted.

**Condition 7 (Out-of-Scope Explicit).** Out-of-scope declarations remain
current as long as the system's scope is unchanged. Any scope expansion that
absorbs something previously declared out of scope triggers a gate review of the
relevant out-of-scope declaration. The out-of-scope section is not a historical
record of what was once excluded — it is a current statement of what remains
excluded, and it must be maintained accordingly.

**Condition 8 (Loop Cost Justified).** The demand economics assessment remains
current as long as the scope, the success criterion, the model tier, and the
organisational cost thresholds are unchanged. Staleness is triggered by: a
material scope change that alters the loop cost estimate; a revision to the
success criterion from Condition 2 that alters the expected value; a change in
the model tier or inference pricing that materially affects the inference cost
component; or a business context change that alters whether the expected value
still exceeds the loop cost. A loop cost justification that was valid for a
prior iteration must be re-assessed if any of these events have occurred since
it was filed. A justification produced for a specification that has since grown
in scope — acquiring additional acceptance criteria, additional threat model
categories, or additional governance overhead — is stale for the scope it did
not cover.

**Condition 9 (Context Thread Assembled and Reviewed).** The context thread
remains current as long as the governance graph it was assembled from has not
materially changed. Staleness is triggered by: the addition of new comparable
specifications to organisational memory that supersede the two referenced in the
thread; changes to the blast radius assessment that alter the rationale
documented; the creation or expiry of waivers on related deployed systems; or a
material change to the validation evidence that changes the demand item's
lineage. The specification analyst is responsible for confirming the context
thread is current at the point of gate assessment; a thread assembled weeks
before gate assessment in a period of active governance graph change should be
re-assembled before the assessment is run.

### Agent Participation in Gate Assessment

A governance agent — one that is itself governed under the ASDLC, with its own
specification and evaluation suite — may contribute to the pre-assessment
preparation work for this gate. The scope of that contribution is advisory and
preparatory: it does not substitute for any assessment that the gate assigns to
a human reviewer.

Before the formal gate assessment begins, a governance agent may generate a
first-draft threat model from the specification content, covering the required
OWASP LLM Top 10 scope as mapped to the agentic threat categories defined under
Condition 4. That draft is labeled agent-proposed and is filed as input to the
security function's review. It reduces the burden on the security reviewer by
providing a structured starting point — identified threats, candidate
mitigations, and proposed out-of-scope declarations — but it does not perform
the security review. The security function must independently validate the
threat model's completeness, the appropriateness of its proposed mitigations,
and the justification for any out-of-scope declarations. A clean agent-produced
draft does not mean Condition 4 is satisfied. The security function's
independent assessment satisfies Condition 4; the agent's draft assists it.

A governance agent may also scan the draft specification against a constraint
checklist before the formal gate assessment, reporting gaps against the
following: threat model present and covering the required scope; token budget
present and set as a hard constraint for Tier 2 and above; accessibility
conformance level stated for user-facing systems in scope of applicable
accessibility legislation; DPIA status documented for specifications involving
personal data processing at scale or automated individual decision-making. The
agent reports gaps; it does not assess the conditions. A specification that
clears the constraint checklist without gaps has met the agent's mechanical
formatting check — which is a useful signal — but the product owner,
specification analyst, security function, and compliance function assess whether
each condition is substantively satisfied. Clearing the checklist is not passing
the gate.

A governance agent may estimate the token budget range based on model tier
pricing and the scope described in the specification, providing a starting point
for the specification analyst's budget-setting work. Similarly, the agent may
check specification formatting and cross-reference completeness — confirming
that all referenced out-of-scope declarations are explicit, that every success
criterion has a stated measurement method, and that referenced artefacts are
linked and named consistently. These mechanical checks surface defects that
would otherwise be found by human reviewers at assessment time, which is a
useful efficiency. The specification analyst must confirm the token budget
estimate against the actual model deployment and set it as a hard constraint in
the specification. The agent's estimate does not constitute the constraint.

Any artefact contributed by a governance agent to the gate assessment record
must carry the label "agent-proposed, pending human review" until a qualified
human reviewer endorses it. When the gate decision record is produced, it must
identify which inputs to the assessment were agent-produced and which human
reviewer endorsed each one. An agent-produced threat model draft endorsed by the
security function becomes part of the gate record as a
security-function-reviewed artefact; it does not remain labeled as
agent-proposed after that endorsement. The purpose of the epistemic labeling
requirement is to preserve the integrity of the accountability chain through the
assessment: every piece of evidence in the gate record must be traceable to a
human who validated it, and artefacts that have not yet received that validation
must be distinguishable from those that have.

---

## Anti-Patterns

**Stakeholder pressure: "we need to start now."** The loop can start when the
specification is loop-ready. Starting before it is ready does not save time — it
produces wasted loop iterations, specification revision mid-execution, and
evidence bundles that do not prove what they claim to prove. If stakeholder
pressure is causing gates to be passed prematurely, the gate decision record
makes the decision visible and attributable. That visibility is the gate's
governance function.

**Assumed clarity: "everyone knows what we need."** If everyone knows it,
writing it down takes ten minutes. If it takes longer, the clarity was assumed,
not real. The specification readiness gate requires written evidence, not shared
understanding. Shared understanding is not a specification.

**Constraint discovery deferral: "we'll figure out compliance as we go."**
Constraint discovery inside the loop is a more expensive, higher-risk version of
the work that should have happened before loop entry. In regulated industries,
it is not just expensive — it can produce compliance incidents. The gate is
explicit: constraints are identified before the loop runs, not during it.

**Missing success criterion: "we'll know it when we see it."** A success
criterion that cannot be stated before the loop runs cannot be verified after.
The validate phase of the agentic loop has nothing to validate against. "We'll
know it when we see it" is an acceptance of ungoverned execution — the loop
runs, something ships, and the organisation has no basis for determining whether
it was the right thing.

**Premature decomposition.** Beginning to write specifications — decomposing the
need into loop-sized items, translating into acceptance criteria — before the
business need is validated and the value is defined. Premature decomposition
produces well-formed specifications for needs that may not survive the
validation step. The cost is not just the specification writing time; it is the
momentum that builds around a specification, making it psychologically harder to
discard even when the validation evidence does not support it.

---

## Phase-Calibrated Gate

The gate scales with the organisation's inner-loop maturity phase. The nine
conditions remain constant — they are non-negotiable. What changes is the
formality of the assessment, the depth of evidence required, and the tooling
available to support it.

**Phase 2.** The gate is run as an informal checklist. The product owner reviews
the specification against the nine conditions and documents the outcome in the
ticket or specification document. Single-reviewer assessment is acceptable. Most
gate failures at this phase will be on Conditions 2 (value measurable), 7
(out-of-scope stated), and 8 (loop cost justified) — these are the conditions
that teams learning the gate most commonly underestimate.

**Phase 3.** The gate is a structured review with the product owner and
specification analyst. A gate decision record is produced for all Tier 2 and
Tier 3 specifications. Tier 1 specifications may still use a lightweight
checklist. Teams at this phase are typically developing a library of worked
examples for each condition to speed up future assessments.

**Phase 4.** The gate is formal for all specifications above Tier 1. A gate
decision record with business sponsor sign-off is required. The gate is
integrated into the delivery workflow — a specification cannot be assigned to
loop entry without a passed gate record. Teams at this phase typically have
constraint libraries and acceptance criteria templates that make Conditions 3
and 4 faster to satisfy.

**Phase 5.** Where the conditions lend themselves to automation — acceptance
criteria format checking, constraint library matching, blast radius
classification, context thread assembly — the gate tooling handles the
mechanical checks. Human review focuses on the conditions that require judgment:
Condition 1 (is the evidence genuinely sufficient?), Condition 2 (is the success
criterion genuinely measurable with existing infrastructure?), Condition 5 (is
the named accountable human genuinely accountable, or is the name a formality?),
and Condition 9 (does the context thread accurately represent the demand layer
decisions, or did the governance graph produce a thread that is formally
complete but substantively thin?). Non-standard specifications — those with
unusual constraint combinations, novel blast radius profiles, or ambiguous scope
boundaries — receive full manual review regardless of tooling maturity.

At every phase, the gate decision record is the artefact that proves the gate
was run. A gate that was "run" but produced no record is, for governance
purposes, a gate that was not run.
