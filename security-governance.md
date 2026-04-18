# Security Governance — ASDLC Cross-Cutting

_Security as a lifecycle capability, not a gate condition._

See [Specification Readiness](specification-readiness.md) for the threat
modeling gate condition. See [Release Governance](release-governance.md) for the
release security gate. See [Deployment Governance](deployment-governance.md) for
pipeline security controls. See
[Operations Governance](operations/governance.md) for runtime security and
incident response. See [Maintenance Governance](maintenance-governance.md) for
vulnerability disclosure and patching. See
[DevSecOps Controls](devsecops-controls.md) for the mandatory control matrix by
tier.

---

## What this document governs

The ASDLC embeds security conditions at every gate. The Specification Readiness
Gate requires threat modeling. The Release Gate requires a passed security scan.
The Operational Readiness Gate requires a dependency vulnerability scan and a
filed SBOM. These conditions are necessary. They are not sufficient.

A system can satisfy every gate condition and still have no secure development
practices, no security architecture review, no secure coding standards, and no
systematic vulnerability response. Gate conditions test for the presence of
specific artefacts at a specific boundary. They do not govern how the system was
designed, how the code was written, or whether the organisation has the
capability to respond to vulnerabilities found in production.

This document defines security as a lifecycle capability that runs through all
four ASDLC layers. It does not duplicate the gate conditions — those are
normative in their respective gate documents. It defines what the gate
conditions cannot define: the practices that must be active across the lifecycle
for the gate conditions to be meaningful, and the organisational capabilities
that must exist for the framework to produce secure systems, not just gated
artefacts.

---

## NIST SSDF Mapping

The NIST Secure Software Development Framework (SP 800-218 v1.1) defines four
practice groups. The following mapping identifies which ASDLC layers are the
primary operational locus for each practice group. The mapping is normative:
organisations operating the ASDLC under US federal contractor requirements or
regulatory contexts that cite SSDF can use this mapping to confirm coverage.

### PO — Prepare the Organisation

**ASDLC locus:** Layer 1 Demand & Value, and organisational ASDLC adoption
(phase calibration).

The PO practice group covers the policies, roles, competencies, and processes
that an organisation must establish before secure software development can be
practised at the team level. Within the ASDLC, PO practices are operationalised
at the demand and adoption layer:

- **Security roles and responsibilities** must be defined before any loop begins
  at Tier 2 or above. The Specification Readiness Gate's Condition 4
  (constraints identified) requires that security constraints — including named
  security review responsibilities — are identified before loop entry. PO
  practice is satisfied when the constraint identification process is documented
  and the security reviewer role is filled, not when it is aspirationally
  described.
- **Security requirements for external component suppliers** are directly
  applicable to the ASDLC in the context of foundation model providers. An
  organisation that relies on a foundation model provider as a component of its
  agentic system must have a defined process for assessing and accepting the
  security posture of that provider. The absence of such a process is a PO gap
  regardless of what the model provider's own security certifications say.
- **Criteria for managing security risks from external components** — model
  weights, agent frameworks, tool libraries, data connectors — must be
  established as part of the ASDLC adoption process, not discovered per-project.
  These criteria govern the Software Composition Analysis control defined in
  [DevSecOps Controls](devsecops-controls.md).
- **Security requirements defined before loop entry** is the Specification
  Readiness Gate's Condition 4 expressed as a SSDF PO practice. The gate
  condition requires that security constraints are identified; the PO practice
  requires that the process for identifying them is itself defined, not
  improvised each time.

### PS — Protect the Software

**ASDLC locus:** Layer 2 Engineering Execution (Specify and Design phases),
Specification Readiness Gate.

The PS practice group covers designing for security, protecting the code from
unauthorised modification, and securing the supply chain. Within the ASDLC:

- **Secure design and architecture** begins at specification, not at the
  security gate. The threat model required by the Specification Readiness Gate
  is the minimum expression of PS at the L1→L2 boundary. Secure design continues
  through the Design phase of the engineering loop, where trust boundaries are
  defined, permission scopes are assigned, and safe failure modes are specified.
  A threat model filed at the specification readiness gate without a
  corresponding secure design in the subsequent Design phase artefact is a PS
  gap.
- **Threat modeling** for agentic systems must address the full OWASP LLM Top 10
  scope. This is stated in the Specification Readiness Gate's technical sub-gate
  condition. The PS practice group's practice PS.1.2 — identifying and
  documenting security requirements before the design — is operationalised by
  this condition.
- **Trust boundary definition for agentic systems** is a PS practice that is
  specific to this system class and is addressed in the Secure Design Principles
  section below.
- **Least-privilege design for tool and plugin permission scopes** is a PS
  practice operationalised by the Least-Privilege Tool Access principle below.
  The permission scope documented in the specification is the normative
  reference against which the deployed agent's permissions are audited.

### RV — Produce Well-Secured Software (Produce + Verify)

**ASDLC locus:** Layer 2 Engineering Execution (Execute and Verify phases),
Layer 3 Release Gate, Layer 3 Deployment.

The RV practice group covers implementing secure practices during development,
verifying the software against security requirements, and protecting artefacts
and the supply chain through to deployment. Within the ASDLC:

- **Secure implementation practices** — no hardcoded credentials, input
  validation at system boundaries, output sanitisation before downstream
  consumption — are defined as capability-level requirements in the Secure
  Implementation Standards section below. They are not testable by any single
  gate condition; they require active practice throughout the Execute phase.
- **Security testing in the loop** — static analysis, dependency scanning,
  dynamic testing for external-facing systems — is governed by the
  [DevSecOps Controls](devsecops-controls.md) mandatory control matrix. The RV
  practice group's requirement for security testing to be integrated into the
  development process is operationalised by requiring these controls to run on
  every build, not only at gate time.
- **Artefact protection and supply-chain integrity** — signed commits, signed
  releases, SLSA provenance attestation — are governed by the DevSecOps Controls
  mandatory control matrix. The tier thresholds define where these controls
  become mandatory.
- **Evidence filing** — scan results, findings, dispositions, and waivers — is
  required by the release gate's evidence bundle condition. The RV practice
  group's requirement for evidence of security verification to be retained is
  operationalised by the evidence bundle requirements in
  [Release Governance](release-governance.md).

### RS — Respond to Vulnerabilities

**ASDLC locus:** Layer 4 Operations, Layer 4 Maintenance.

The RS practice group covers identifying vulnerabilities in deployed software
and responding to them in a structured way. Within the ASDLC:

- **Vulnerability disclosure intake** — the process by which external reporters
  can disclose vulnerabilities in a system — must be defined for all Tier 2+
  systems before the Operational Readiness Gate passes. A system that has no
  published vulnerability disclosure policy is not RS-compliant at the point of
  deployment.
- **Triage and remediation** — assessing the severity and blast radius of
  reported vulnerabilities, prioritising response, and executing fixes — is
  governed in detail in [Maintenance Governance](maintenance-governance.md). The
  RS practice group's requirement for a documented vulnerability response
  process is operationalised by the maintenance governance requirements.
- **Root cause analysis** — understanding why the vulnerability existed — feeds
  back into the engineering loop's Learn and Govern phases and into the
  evaluation portfolio. A vulnerability response that closes the finding without
  filing a root cause analysis has satisfied neither the RS practice group nor
  the ASDLC's maintenance feedback requirements.
- **Prevention feedback** — updating practices, training data evaluation, and
  specification constraints based on vulnerability root causes — is the RS
  practice group's primary contribution to continuous improvement. This feedback
  path is governed by the L4→L2 maintenance signal path defined in
  [asdlc.md](asdlc.md).

---

## Secure Design Principles for Agentic Systems

These principles are specific to agentic systems and supplement the standard
SSDF PS practice group. They apply at Tier 1 as guidance and at Tier 2 and above
as required design properties. Compliance with these principles must be
demonstrable in the specification, the design artefact, and the evaluation
portfolio — not only asserted.

### 1. Least-Privilege Tool Access

Agents must be granted only the tool permissions required for their defined
scope. Permission scope must be documented in the specification and is subject
to the threat model review. An agent that can invoke a tool not referenced in
its specification is not operating within its authorised scope, regardless of
whether it actually invokes that tool.

Permission scope is a constraint, not a configuration detail. It belongs in the
specification before the loop begins, not in a deployment configuration
discovered at release time. The threat model must explicitly evaluate whether
the defined permission scope satisfies least-privilege given the full range of
tasks the agent is specified to perform.

### 2. Trust Boundary Enforcement

Define and document trust boundaries between: human principals and agents,
agents and tools, agents and external services, and agents and other agents.
These four boundary types are not exhaustive — any interface where a trust
transition occurs is a trust boundary.

Inputs crossing a trust boundary must be validated before processing. Validation
is not optional for boundaries characterised as "trusted" — trust must be
established through explicit architectural decision, not assumed from context.
Outputs crossing a trust boundary must be sanitised to prevent injection into
the consuming context.

Trust boundaries must be identified in the threat model. An agent that receives
inputs from an external retrieval system without validation at the
retrieval→agent boundary has an unaddressed trust boundary regardless of how the
retrieval system itself is characterised.

### 3. Minimal Footprint

Agents must not retain state, access resources, or maintain connections beyond
what the current task requires. Persistent memory, file system access, network
connections, and spawned sub-processes are capabilities that must be explicitly
justified in the specification and bounded by the task scope.

An agent specification that authorises "general file system access" or
"unrestricted network access" does not satisfy the minimal footprint principle.
The specification must name the specific resources accessed, the specific
directories or endpoints involved, and the specific task context that requires
each access.

### 4. Auditability by Design

Every consequential agent action must produce an auditable record.
"Consequential" means: actions that modify state, invoke external services,
communicate with other agents, make decisions that affect the output delivered
to the human principal, or cause any resource consumption that crosses a cost or
rate threshold.

Systems where agent actions cannot be reconstructed from logs are not compliant
with this principle. Auditability is not a logging configuration — it is a
design property. If the system's architecture does not produce reconstructible
action records as a natural consequence of its operation, the architecture must
be changed before the system is Tier 2 eligible.

The [Operations Governance](operations/governance.md) document defines the
specific trace retention and observability requirements that operationalise this
principle in production.

### 5. Safe Failure Modes

Agents must be designed to fail safely — defaulting to inaction and escalation
rather than autonomous recovery when encountering unexpected states. An agent
that attempts autonomous recovery from an unexpected state may succeed or may
amplify the failure; the ASDLC requires that this is not left to chance.

Safe failure modes must be:

- Documented in the specification before the loop begins
- Implemented as explicit logic, not as the absence of error handling
- Tested in the evaluation suite with explicit test cases that exercise the
  failure condition and confirm the safe failure behaviour
- Verified at the release gate as part of the evidence bundle

An evaluation portfolio that does not include failure mode tests does not
satisfy this principle, regardless of how the specification describes failure
behaviour.

### 6. Human Override

Every agentic system must have a documented and tested kill switch or human
override mechanism. The override mechanism must:

- Allow a human principal to halt or reverse agent actions without requiring
  technical expertise in the system's implementation
- Be documented in the runbook with step-by-step invocation instructions
- Be tested at minimum annually as part of DR and resilience testing, with test
  results filed in the operational evidence record
- Be exercisable without requiring the agent to be in a specific operational
  state — an override that only works when the system is functioning normally is
  not an override

The override mechanism is not the same as the rollback procedure, though they
may share components. The rollback procedure restores a known good state after a
failed deployment. The human override halts or reverses agent actions during
operation. Both must exist and both must be tested.

---

## Security Architecture Review

For Tier 2 and above, a security architecture review is required before loop
entry — at or alongside the Specification Readiness Gate technical sub-gate. The
review is a structured assessment of the specification and design intent against
the security principles above. It is not a code review and cannot be conducted
on a working implementation; if the design has not been articulated in the
specification, the review cannot proceed.

The review assesses:

- Whether the threat model covers the full OWASP LLM Top 10 scope and
  specifically addresses the four trust boundary types defined in Principle 2
- Whether trust boundaries are correctly identified and that the validation and
  sanitisation strategy at each boundary is specified, not deferred
- Whether the permission model satisfies the Least-Privilege Tool Access
  principle — that is, whether every tool permission can be traced to a specific
  task in the specification
- Whether safe failure modes are specified for each class of unexpected state
  the agent may encounter
- Whether the human override mechanism is described in enough detail to assess
  its adequacy

The review is conducted by the security function: an internal security team, an
appointed security reviewer with relevant competency, or an external assessor
for regulated contexts where independence requirements apply. The security
function is responsible for the review outcome; the engineering team is
responsible for providing the specification artefacts the review requires.

The review outcome is one of three states:

- **Pass**: The specification satisfies the review criteria. The technical
  sub-gate may proceed.
- **Conditional pass**: The specification satisfies the review criteria subject
  to specific documented changes before loop entry. The changes are recorded as
  conditions on the gate pass. The review does not need to be repeated if the
  conditions are satisfied, but the satisfaction of each condition must be filed
  before the loop begins.
- **Fail**: The specification does not satisfy the review criteria. The
  specification must be revised and the review repeated. The loop does not begin
  until the review passes.

A specification with unresolved security architecture findings does not pass the
Technical Sub-Gate. The technical sub-gate reviewer is responsible for
confirming that the security architecture review outcome is Pass or Conditional
Pass (conditions satisfied) before issuing a technical sub-gate pass decision.

---

## Secure Implementation Standards

Rather than mandating specific coding standards — which are language, framework,
and ecosystem dependent — the ASDLC mandates the following capability-level
requirements. These apply to all code produced in the engineering execution
loop, whether written by human engineers, agent-generated, or some combination.
The implementation mechanism is the team's responsibility; these are the
outcomes that must be achieved.

### Input Validation at All System Boundaries

All inputs from external sources, tool calls, retrieval results, and inter-agent
messages are validated before processing. Validation must confirm that the input
conforms to the expected structure, type, and value ranges, and must reject
non-conforming inputs with a logged rejection event.

Validation is not optional for inputs characterised as coming from "trusted"
sources. Trust must be established through explicit architectural decision —
typically through the trust boundary definition in the specification and design
artefact. A retrieval system, an external API, or another agent is not a trusted
input source by default. The trust characterisation must be explicit and present
in the threat model.

The evaluation portfolio must include test cases that exercise boundary
validation logic with malformed, unexpected, and adversarially crafted inputs.

### Output Sanitisation Before Downstream Consumption

Agent outputs consumed by downstream systems — other agents, tools, databases,
or human-facing interfaces — must be sanitised to prevent injection into the
consuming context. "Injection into the consuming context" means that
agent-generated content causes the consuming system to interpret that content as
instructions rather than data.

The sanitisation requirement applies at the point where output leaves the
agent's control. An agent that produces output that is passed without
sanitisation to a database write, a tool invocation, another agent's system
prompt, or a human-facing interface has an unsanitised output boundary,
regardless of how the output itself was generated.

### No Hardcoded Credentials

No API keys, tokens, passwords, private keys, or other credentials appear in
source code, configuration files committed to source control, container images,
or agent prompts and system instructions. Credentials are managed through a
secrets management system and are injected into the running environment at
runtime through a documented and audited mechanism.

This requirement is testable by secrets detection scanning (see
[DevSecOps Controls](devsecops-controls.md), Control 1). A secrets detection
finding that is waived without a filed justification and accountable human
approval is a violation of this requirement, not a waiver of it.

### Dependency Integrity

All dependencies are pinned to specific versions. Version pinning must be
enforced in the build system, not only documented in a manifest. Hash
verification of dependency downloads is required where the build system supports
it — which for current major build ecosystems across all primary development
languages, it does. A build system that does not support hash verification of
dependency downloads is not an acceptable build system for Tier 2 or above.

The Software Composition Analysis control (see
[DevSecOps Controls](devsecops-controls.md), Control 3) scans pinned
dependencies against known vulnerability databases. Pinning is a prerequisite
for meaningful SCA results; an unpinned dependency may resolve to a different
version at different build times, producing inconsistent scan results.

---

## SAMM Note

Organisations that want to assess their security practice maturity in a
structured way can apply the OWASP Software Assurance Maturity Model (SAMM)
independently. SAMM covers five business functions: Governance, Design,
Implementation, Verification, and Operations. Each function has three security
practices, each assessed at three maturity levels.

The ASDLC does not embed a SAMM maturity assessment and does not require a
specific SAMM score. The ASDLC defines minimum practice requirements — the floor
below which agentic systems at a given tier must not fall. SAMM provides a
complementary lens for teams that want to understand their trajectory beyond
that floor: where they are, what the next maturity level looks like, and how
security practice improvement maps to measurable outcomes. Teams that are
building internal security practice capability will find SAMM useful for
structuring that work; the ASDLC's minimum requirements will typically
correspond to SAMM maturity level 1 in the relevant practice areas, with Tier 3
requirements beginning to approach level 2 in Design and Verification.

---

## Normative References

- NIST SP 800-218 v1.1 (Secure Software Development Framework):
  https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SP 800-218 Rev. 1 draft (December 2025 update):
  https://csrc.nist.gov/pubs/sp/800/218/r1/ipd
- NIST SP 800-218A, *Secure Software Development Practices for Generative AI
  and Dual-Use Foundation Models: An SSDF Community Profile* (2024):
  https://doi.org/10.6028/NIST.SP.800-218A
- NIST AI 100-2e2025, *Adversarial Machine Learning: A Taxonomy and Terminology
  of Attacks and Mitigations* (2025):
  https://doi.org/10.6028/NIST.AI.100-2e2025
- OWASP GenAI Security Project, *Agentic AI — Threats and Mitigations* (2025):
  https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
- OWASP SAMM (optional maturity assessment): https://owasp.org/www-project-samm/
- OWASP LLM Top 10 (2025):
  https://genai.owasp.org/llm-top-10/
- OWASP DevSecOps Guideline: https://owasp.org/www-project-devsecops-guideline/
- CISA et al., *Shifting the Balance of Cybersecurity Risk: Principles and
  Approaches for Secure by Design Software* (April 2023, updated October 2023):
  https://www.cisa.gov/resources-tools/resources/secure-by-design

### Empirical evidence base

The capability-level controls in this document — mandatory static analysis,
secrets scanning, dependency scanning, and human review of agent-generated
code — are calibrated against empirical findings on AI-assisted coding. Pearce
et al., *Asleep at the Keyboard? Assessing the Security of GitHub Copilot's
Code Contributions* (IEEE S&P 2022, https://arxiv.org/abs/2108.09293), found
that AI code assistants emit insecure code at meaningful rates across CWE-style
scenarios. Perry et al., *Do Users Write More Insecure Code with AI
Assistants?* (ACM CCS 2023, https://arxiv.org/abs/2211.03622), reported that
users with AI assistance produced less secure code while reporting higher
confidence in its security — supporting the anti-rubber-stamp posture that
human review of AI-generated code is required, not optional. Greshake et al.,
*Not what you've signed up for: Compromising Real-World LLM-Integrated
Applications with Indirect Prompt Injection* (2023,
https://arxiv.org/abs/2302.12173), is the foundational reference for treating
external retrieval and tool inputs as hostile data at trust boundaries. These
findings are calibration points, not universal laws — model and tool
performance evolve — but they are the load-bearing evidence behind the
controls in this document and the trust-boundary requirements in
[Agent Control Plane](agent-control-plane.md).

---

## Regulated Industries

Organizations operating in regulated industries must supplement the security
governance requirements in this document with the sector-specific regulatory
mappings maintained in the domain files. Each domain file maps ASDLC gate
conditions and security requirements to the applicable regulatory frameworks for
that sector. These domain files do not constitute legal or regulatory advice —
they map principles to frameworks; qualified regulatory counsel must be engaged
for compliance determinations.

- Financial services: SR 11-7 model risk management, DORA operational
  resilience, EU AI Act obligations, MiFID II — see
  [Financial Services Regulatory Alignment](../domains/financial-services.md)
- Medical devices: FDA software as a medical device requirements, IEC 62304, ISO
  14971 risk management — see
  [Medical Devices Regulatory Alignment](../domains/medical-devices.md)
- Aviation: DO-178C software considerations, ARP4754A system development — see
  [Aviation Regulatory Alignment](../domains/aviation.md)
- Automotive: ISO 26262 functional safety, SOTIF, UNECE WP.29 — see
  [Automotive Regulatory Alignment](../domains/automotive.md)
- Pharmaceuticals: GxP validation, 21 CFR Part 11 electronic records — see
  [Pharma Regulatory Alignment](../domains/pharma.md)
- Defense and government: CMMC, FISMA, NIST SP 800-53 — see
  [Defense and Government Regulatory Alignment](../domains/defense-government.md)
