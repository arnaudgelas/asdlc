# DevSecOps Control Matrix — ASDLC Cross-Cutting

_Which pipeline security controls are mandatory at each tier._

See [Security Governance](security-governance.md) for the security lifecycle and
SSDF mapping. See [Deployment Governance](deployment-governance.md) for
promotion gate mechanics. See [Release Governance](release-governance.md) for
the release gate conditions.

---

## What this document governs

[Deployment Governance](deployment-governance.md) defines the mechanics of
environment promotion gates: what conditions govern movement from development to
test, test to staging, staging to production, and what the promotion gate record
must contain. This document defines which security controls must be present in
the pipeline for each autonomy and blast-radius tier.

Controls are described by capability — not by tool. An organisation implements
each control with the tooling appropriate to their stack, their build system,
and their ecosystem. The ASDLC mandates the capability and the tier threshold;
it does not mandate the implementation choice. Two organisations, one using a
compiled statically-typed language and one using a dynamically-typed interpreted
language, will implement the static analysis control with entirely different
tooling; the control is the same.

A control listed as **mandatory** means its absence is a gate failure at that
tier. The promotion gate cannot pass without evidence that the control ran and
its results were reviewed.

A control listed as **recommended** means its absence must be explicitly
justified and documented in the governance record. A justification such as "we
don't have this tooling yet" is not a valid justification for Tier 2 and above;
it is a remediation backlog item with a defined timeline.

A control listed as **not applicable** is not required at that tier and need not
be justified.

---

## Control Matrix

### Control 1 — Secrets Detection

**Capability:** Automated scanning of source code, configuration files, and
container images for hardcoded credentials, API keys, tokens, private keys, and
high-entropy strings indicative of secrets material. The scan runs on every
commit that is proposed for merge to the main branch and as a gate condition at
every promotion boundary.

**Tier 1:** Mandatory

**Tier 2:** Mandatory

**Tier 3:** Mandatory

**Applicability conditions:** Universal. No exemption exists for system type,
language, or deployment model. The ASDLC Secure Implementation Standard
prohibits hardcoded credentials unconditionally; this control is the automated
enforcement mechanism for that standard.

**Gate treatment:** Any finding blocks promotion. A finding that is suppressed
without a filed justification and accountable human approval is a violation of
the prohibition, not a waived finding. Where a finding is a false positive, the
suppression must document why it is a false positive with enough specificity to
allow the suppression to be independently reviewed.

---

### Control 2 — Static Application Security Testing (SAST)

**Capability:** Automated analysis of source code for security vulnerabilities
without executing the code. The analysis must cover code that touches external
interfaces, processes untrusted input, or handles credentials. The scope of
analysis is not limited to agent-specific code; all code in the repository that
meets these criteria is in scope.

**Tier 1:** Recommended — mandatory for code that touches external interfaces,
processes untrusted input, or handles credentials.

**Tier 2:** Mandatory

**Tier 3:** Mandatory

**Applicability conditions:** The mandatory sub-condition for Tier 1 applies
regardless of whether the organisation has formally adopted SAST as a universal
practice. If the codebase contains code in any of the three categories (external
interfaces, untrusted input, credential handling), SAST is mandatory for that
code at all tiers.

**Gate treatment:** No unresolved Critical or High severity findings at any
promotion gate without a filed waiver. A waiver requires: a named accountable
human approval, a documented technical justification for why the finding does
not represent an exploitable risk in the specific deployment context, and a
remediation timeline. Waiver-filed findings are not closed; they are tracked
until remediation is complete. Scan results and finding dispositions are filed
in the evidence bundle.

---

### Control 3 — Software Composition Analysis (SCA) / Dependency Vulnerability Scanning

**Capability:** Automated scanning of all direct and transitive dependencies
against known vulnerability databases. The scan produces, as a byproduct, a
Software Bill of Materials (SBOM) that enumerates every dependency at the
version deployed. The SBOM is a required artefact; a scan that does not produce
a machine-readable SBOM is not a compliant SCA execution.

**Tier 1:** Mandatory

**Tier 2:** Mandatory

**Tier 3:** Mandatory

**Applicability conditions:** Universal. All systems have dependencies; all
dependency sets are scannable. The control applies regardless of whether the
organisation has adopted pinned dependencies (pinning is required by the
Dependency Integrity implementation standard, not by this control's
applicability condition — but a system without pinned dependencies will produce
inconsistent SCA results across builds, which is itself a finding).

**Gate treatment:** No unresolved Critical or High CVEs at any promotion gate
without a filed VEX (Vulnerability Exploitability eXchange) document. A VEX
document must state: the CVE identifier, the affected package and version, the
assessment of whether the vulnerability is exploitable in this system's specific
deployment context, and the basis for that assessment. VEX is the
machine-readable standard for communicating exploitability context alongside
vulnerability scan results.

**SBOM format:** The SBOM must be generated in a machine-readable format. SPDX
and CycloneDX are both acceptable; the organisation chooses based on ecosystem
fit, downstream tooling requirements, and regulatory context. The ASDLC does not
mandate a format — it mandates that a machine-readable SBOM is produced and
filed.

---

### Control 4 — Dynamic Application Security Testing (DAST) / API Security Testing

**Capability:** Automated testing of the running application or API for security
vulnerabilities by sending inputs to a deployed instance and observing
responses. This is the runtime counterpart to SAST: where SAST analyses what the
code says it does, DAST observes what the running system actually does when
presented with inputs designed to elicit security failures.

**Tier 1:** Recommended — where applicable

**Tier 2:** Mandatory — where applicable

**Tier 3:** Mandatory — where applicable

**Applicability conditions:** A system is subject to this control where it
exposes HTTP endpoints accessible from outside its own process, external APIs
consumed by other systems or users, or where it processes external user input in
a running state. A system with no external interface — no HTTP endpoints, no API
surface, no external input path — is exempt. The exemption must be documented. A
system that adds an external interface after its initial deployment is no longer
exempt from the point that interface is present.

**Gate treatment:** No unresolved High severity findings at any promotion gate
without a filed waiver. Waiver requirements are the same as for Control 2. DAST
is run against a representative deployed instance, not against source code; the
environment in which DAST is executed must be documented in the evidence bundle
entry.

---

### Control 5 — Infrastructure-as-Code (IaC) Scanning

**Capability:** Automated scanning of infrastructure definition files — cloud
resource templates, container orchestration manifests, network policy
definitions, configuration-as-code — for security misconfigurations.
Misconfigurations include: overly permissive network access rules, storage
resources with public access enabled, compute resources without required
encryption, identity and access management policies that violate
least-privilege.

**Tier 1:** Recommended — where applicable

**Tier 2:** Mandatory — where applicable

**Tier 3:** Mandatory — where applicable

**Applicability conditions:** A system is subject to this control where its
infrastructure is defined in code rather than manually provisioned. Manually
provisioned infrastructure is not exempt from security configuration
requirements — it is governed by a different mechanism (configuration audit)
that is not in scope for this pipeline control matrix. The ASDLC's strong
preference is for IaC-managed infrastructure at Tier 2 and above; manual
provisioning at these tiers requires documented justification in the deployment
governance record.

**Gate treatment:** Findings are assessed by severity. Critical
misconfigurations block promotion. High severity misconfigurations require a
filed waiver with the same waiver requirements as Control 2. The IaC repository
must be treated as a security-sensitive code path subject to the code owner
review requirement (Control 8).

---

### Control 6 — Container Image Scanning

**Capability:** Automated scanning of container images for OS-level
vulnerabilities and known CVEs in base images and installed packages. The scan
runs against the final image that will be deployed, not only against the base
image, because the image-building process may add packages that are themselves
vulnerable.

**Tier 1:** Recommended — where applicable

**Tier 2:** Mandatory — where applicable

**Tier 3:** Mandatory — where applicable

**Applicability conditions:** A system is subject to this control where it is
deployed as container images. Systems deployed as bare-metal processes, as
serverless functions without container packaging, or as managed services where
the organisation does not control the container image are exempt. Managed
services where the organisation does provide a container image are not exempt —
the image the organisation provides is in scope.

**Gate treatment:** No unresolved Critical or High CVEs without a filed VEX
document. Container image scan results are filed in the evidence bundle as a
distinct entry from the SCA dependency scan — they cover different surfaces and
both are required where applicable.

---

### Control 7 — Signed Commits and Tags

**Capability:** Cryptographic signing of all commits merged to the main branch
and all release tags, by the committing developer or the CI system performing
the merge. Branch protection is configured to prevent unsigned commits from
merging to the main branch. The signing key must be associated with a verified
identity in the version control system.

**Tier 1:** Recommended

**Tier 2:** Mandatory

**Tier 3:** Mandatory

**Applicability conditions:** Universal where applicable tier threshold is met.
The specific signing mechanism (developer GPG keys, SSH signing keys, or CI
system signing) is an implementation choice; the requirement is that the
signature is cryptographically verifiable and linked to an accountable identity.

**Gate treatment:** Unsigned commits on the main branch at Tier 2 or above are a
branch protection configuration failure, not an individual commit finding.
Branch protection must be configured to enforce signing before any Tier 2 or
Tier 3 system begins production operation. This is verified at the Operational
Readiness Gate.

---

### Control 8 — Branch Protection and Code Owner Review

**Capability:** The main branch is protected: direct pushes are blocked; all
changes require at minimum one pull request review by a reviewer who is not the
change author; and code owners are defined and their review is required for
changes to security-sensitive paths. Security-sensitive paths include:
authentication and authorisation logic, external integration code, credential
handling, agent prompts and system instructions, tool permission definitions,
and IaC configurations.

**Tier 1:** Recommended

**Tier 2:** Mandatory

**Tier 3:** Mandatory

**Applicability conditions:** Universal where applicable tier threshold is met.
Code owner definitions must be maintained — a code owner definition that names a
person who has left the organisation or the team is not a compliant code owner
definition.

**Gate treatment:** Branch protection configuration is verified at the
Operational Readiness Gate for all Tier 2 and above systems. The review of pull
requests by code owners is an operational control, not a gate-time control; its
effectiveness depends on code owner definitions being current and on reviewers
actually reviewing, not rubber-stamping.

---

### Control 9 — Supply-Chain Provenance (SLSA)

**Capability:** The build pipeline produces a cryptographically signed
provenance attestation that links the specific source commit to the specific
build output artefact. The attestation records: the source repository, the
source commit hash, the build platform, the build steps, and the resulting
artefact digest. The attestation is generated by a hosted,
non-developer-controlled build service — provenance generated on a developer's
local machine does not provide the tamper-resistance that supply-chain
provenance is designed to deliver.

**Tier 1:** Not required

**Tier 2:** Mandatory — SLSA Level 2 minimum

**Tier 3:** Mandatory — SLSA Level 2 minimum; SLSA Level 3 recommended

**Applicability conditions:** Universal at Tier 2 and above. SLSA Level 2
requires a hosted build service that generates provenance. SLSA Level 3
additionally requires that the build service itself is hardened against
tampering and that the provenance is generated in an isolated build environment.
The progression from Level 2 to Level 3 is a meaningful supply-chain security
improvement; Tier 3 systems that handle sensitive data or operate in regulated
environments should assess whether Level 3 is warranted given their threat
model.

**Reference:** SLSA v1.2 — https://slsa.dev/spec/

---

### Control 10 — Image Signing and Artifact Attestation

**Capability:** Container images and deployment artefacts are cryptographically
signed. The signature is verified before deployment proceeds. Signing and
verification must use an open attestation format, ensuring that the verification
process is not dependent on a specific vendor's tooling.

**Tier 1:** Not required

**Tier 2:** Recommended

**Tier 3:** Mandatory

**Applicability conditions:** Applies to container-deployed systems and to any
system that produces a discrete deployable artefact. Systems that are deployed
through a continuous delivery process without a discrete artefact (for example,
directly from source) are governed by the signed commits and SLSA provenance
controls instead.

**Gate treatment:** At Tier 3, a deployment promotion gate must verify the
artefact signature before permitting deployment. Verification failure is a hard
gate block; a deployment that proceeds without signature verification has not
satisfied this control.

---

### Control 11 — Policy-as-Code

**Capability:** Security and compliance policies are encoded as
machine-executable rules that run as part of the promotion pipeline and produce
deterministic pass or fail outcomes. Policy rules cover requirements such as:
required metadata labels being present, approved base images being used,
required resource limits being set, network policy compliance, required
annotations on deployable artefacts. The policy set is versioned alongside the
application code, ensuring that policy changes are subject to the same review
and audit process as code changes.

**Tier 1:** Recommended

**Tier 2:** Mandatory

**Tier 3:** Mandatory

**Applicability conditions:** Universal at Tier 2 and above. The specific policy
rules are determined by the organisation's compliance requirements, the system's
threat model, and the applicable regulatory context. The ASDLC mandates that the
mechanism exists and is active — the organisation determines what policies are
encoded based on their governance requirements.

**Gate treatment:** Policy evaluation results are filed in the evidence bundle.
A policy failure is a gate block. A policy rule that consistently fails is
either misconfigured or identifying a genuine compliance gap; it must not be
suppressed without a documented change control process that either updates the
policy or remediates the finding.

---

### Control 12 — Environment Drift Detection

**Capability:** The running production infrastructure is continuously compared
against the declared configuration. Differences between declared and actual
state — drift — trigger alerts that are routed to the on-call engineer and the
system steward. For agentic systems, drift detection must additionally cover:
agent permission scope drift (the running agent's tool permissions differ from
the specification), tool manifest drift (the tools available to the agent differ
from the deployed configuration), and model version drift (the foundation model
version in use differs from the evaluated version).

**Tier 1:** Not required

**Tier 2:** Recommended

**Tier 3:** Mandatory

**Applicability conditions:** Universal at Tier 3. At Tier 2, the justification
for not implementing drift detection must address the specific agentic drift
types (permission scope, tool manifest, model version) in addition to
infrastructure drift, as these are higher-risk for agentic systems than
infrastructure drift alone.

**Operational integration:** Drift alerts are operational events, not pipeline
events. They are routed to the on-call and steward escalation chain defined in
the runbook. A drift alert that is acknowledged but not resolved within the SLA
defined in the runbook is an escalation event.

---

### Control 13 — OpenSSF Scorecard

**Capability:** The project's security posture is assessed against the OpenSSF
Scorecard, an automated tool that evaluates a set of security hygiene practices
and produces a score across categories including: vulnerability disclosure
policy, branch protection, code review, CI testing, signed releases, token
permissions, dependency pinning, fuzzing, SAST, and absence of binary artefacts
checked into source control. The score is tracked over time as a metric.

**Tier 1:** Recommended

**Tier 2:** Recommended

**Tier 3:** Recommended

**Applicability conditions:** Universal as a recommended practice. The Scorecard
is not a gate condition at any tier — it is a directional metric that identifies
security hygiene gaps and tracks improvement. Many of the categories the
Scorecard assesses correspond to mandatory controls in this matrix; an
organisation that satisfies the mandatory controls for their tier will typically
achieve a strong Scorecard result without additional effort.

**Reference:** OpenSSF Scorecard — https://openssf.org/projects/scorecard/

---

## Controls Not Included in This Matrix

### Interactive Application Security Testing (IAST)

IAST instruments the application runtime to detect security vulnerabilities
during test execution. Unlike DAST, which sends inputs to a running application
from the outside, IAST observes application behaviour from within the runtime
during test execution.

IAST is not in this mandatory control matrix because it requires runtime
instrumentation support that is not universally available across the languages
and frameworks used to build agentic systems. IAST is most effective for
interpreted languages with available instrumentation agents; it is not
applicable to compiled languages or to systems where runtime instrumentation is
architecturally infeasible or prohibited by the execution environment.

Teams working in contexts where IAST is applicable — specifically, teams
building agentic systems in interpreted languages where IAST instrumentation
agents are available — may add IAST as an additional control beyond this matrix.
Its absence from the mandatory matrix does not preclude its use, and for
applicable contexts it provides complementary coverage to DAST that can reduce
the false negative rate in dynamic security testing.

### Fuzzing

Fuzzing — automated generation and delivery of unexpected, malformed, or random
inputs to a target in order to discover crashes, memory errors, or unexpected
behaviour — is a powerful technique for security-sensitive input boundaries,
parsers, binary protocol handlers, and any code that processes
attacker-controlled data with complex structure.

Fuzzing is not in the mandatory control matrix as a universal requirement
because it requires significant engineering investment to implement effectively,
produces high value primarily for specific code patterns (parsers, binary
protocols, complex input validation logic), and is not applicable in the same
form to all components of an agentic system.

Teams building Tier 3 systems that include complex input parsers, binary
protocol handling, or code that processes attacker-controlled data at security
boundaries should evaluate fuzzing independently and include it where the
cost-benefit assessment is favourable. For the subset of Tier 3 systems where
these code patterns exist, fuzzing is strongly recommended and its absence
should be documented with a technical justification.

---

## Control Execution and Evidence

Each mandatory control produces a result. That result is filed as part of the
evidence bundle for the relevant promotion gate. Filing a result means it is a
structured record associated with the gate — not a log entry in a build system
that may be rotated out. The evidence bundle is the authoritative record of what
controls ran, what they found, and what was done about the findings.

The evidence bundle entry for each control must include:

- The control type (from this matrix, by name)
- The scan scope (what was scanned: the specific branch, commit hash, image
  digest, or environment)
- The tool category used — for example, "dependency vulnerability scanner",
  "SAST analyser", "secrets detector" — not the specific tool name, which is an
  implementation detail
- The finding count by severity (Critical, High, Medium, Low, Informational)
- The disposition for each Critical and High finding: pass (no finding), pass
  with filed waiver (waiver document reference), or fail (gate blocked)

A control that ran but whose results are not filed in the evidence bundle is
treated as if the control did not run. The build system log is not the evidence
bundle. The evidence bundle is explicitly filed, explicitly referenced at the
gate, and explicitly part of the gate record that the accountable human reviews
before sign-off.

A control that is marked mandatory for a given tier but is absent from the
evidence bundle is a gate failure condition at that tier, independent of what
the control would have found had it run.

---

## Normative References

- OWASP DevSecOps Guideline: https://owasp.org/www-project-devsecops-guideline/
- SLSA v1.2: https://slsa.dev/spec/
- OpenSSF Scorecard: https://openssf.org/projects/scorecard/
- NIST SP 800-218 (SSDF) RV practice group:
  https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SP 800-218A, *Secure Software Development Practices for Generative AI
  and Dual-Use Foundation Models* (2024):
  https://doi.org/10.6028/NIST.SP.800-218A
- OWASP LLM Top 10 (2025): https://genai.owasp.org/llm-top-10/
- OWASP GenAI Security Project, *Agentic AI — Threats and Mitigations* (2025):
  https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
- CISA et al., *Shifting the Balance of Cybersecurity Risk: Principles and
  Approaches for Secure by Design Software* (2023):
  https://www.cisa.gov/resources-tools/resources/secure-by-design
