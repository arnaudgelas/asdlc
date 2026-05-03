# Sub-prompt 07 — AI/Runtime Guardrails, Security, FinOps & DevSecOps (Parts 12 + 13)

**Purpose.** Produce the Part 12 (AI/Runtime Guardrails Assessment) and Part 13 (Security, FinOps & DevSecOps Assessment) file for `[[FRAMEWORK]]`.

**Wave:** Wave 1a. Runs in parallel with 01, 02-l1..l4, 02-g1..g3, 03, 04a, 04b, 05a, 08a. Cannot read other agents' outputs.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_07_guardrails_security.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`.

---

## 1. Inputs to read

### 1.1 `[[FRAMEWORK]]` artefacts
Read every source file at `[[FRAMEWORK_VERSION]]`. Quote exact rule text, guardrail definitions, security controls, FinOps tagging schema, DevSecOps pipeline configuration.

### 1.2 ASDLC core (mandatory — abort if missing)
- `asdlc.md` — § Governance Agents; § Tier 4 mechanics; § Relationship to Other Frameworks (NIST SSDF, OWASP LLM Top 10, NIST AI RMF, ISO 42001).
- `governance/agents.md` — governance failure modes, autonomy tier definitions, epistemic tier labelling.

### 1.3 ASDLC security + FinOps + DevSecOps corpus (mandatory)
- `security-governance.md` — security lifecycle, NIST SSDF mapping.
- `devsecops-controls.md` — DevSecOps pipeline control matrix by autonomy tier.
- `finops-governance.md` — FinOps and inference cost governance, FOCUS specification, FinOps maturity model.

### 1.4 Cross-cutting (read for context)
- `agent-control-plane.md` — named governance agents and decision points.
- `waiver-governance.md` — waiver lifecycle and accumulation patterns (a P10-equivalent failure mode in ASDLC).
- `governance/queries.md` — canonical governance questions (some of which directly query guardrail / security / FinOps state).

### 1.5 External reference material (mandatory; from `asdlc.md` § Evidence Base)

ASDLC's evidence base names specific external references that this agent uses for guardrail / security assessment. Map findings to the relevant external taxonomy where applicable:

- **NIST SP 800-218A** — Secure Software Development Practices for Generative AI and Dual-Use Foundation Models (2024). Used for Generative-AI-specific SSDF mapping.
- **NIST AI 100-2e2025** — Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (2025). Used as the formal attack taxonomy in §12.5 adversarial scenarios.
- **OWASP Agentic AI — Threats and Mitigations (2025)** — covers tool misuse, goal hijacking, identity and privilege abuse, memory poisoning specific to agentic systems.
- **OWASP Top 10 for LLM Applications (2025)** — broader application security baseline.
- **CISA et al., Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Secure by Design Software (2023)** — operational framing for security as lifecycle ownership.
- **NIST AI RMF 1.0 (NIST AI 100-1, 2023)** + **GenAI Profile (NIST AI 600-1, 2024)** — Govern / Map / Measure / Manage functions.
- **FinOps Foundation Framework + FOCUS specification** — for §13's FinOps assessment.

### 1.6 Domain file
- `[[DOMAIN_FILE]]` — read in full. Map every Critical / High finding in Part 12 / Part 13 to a specific regulatory provision.

   - **Scope guard.** If `[[DOMAIN_FILE]]` references out-of-scope corpora (`aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.md`, `agentic-governance-stack.md`, `manifesto-evolution-plan.md`, `phase-assessment-checklist.md`, `aplc-plan*`, or `igm-aent-coherence-review*`), ignore those sections — they are out of scope for this review and MUST NOT be forward-propagated into the output file.

### 1.7 Prior reviews
If `[[PRIOR_REVIEWS]]` is not `none`, read for peer comparison.

---

## 2. Methodology

### 2.1 Part 12 — AI/Runtime Guardrails Assessment

Part 12 has five required subsections:

#### §12.1 Input Guardrails

Markdown table with exact columns:

```
| Guardrail | Mechanism | Enforcement Level | Gap | ASDLC categories |
```

- **Mechanism** — `[[FRAMEWORK]]` artefact / command / rule (backticked path).
- **Enforcement Level** — `Enforced (blocks)` / `Enforced (advisory)` / `Convention (documented only)` / `Absent`.
- **Gap** — what is missing relative to OWASP LLM Top 10 / OWASP Agentic AI / NIST AI 100-2e2025 attack categories.
- **ASDLC categories** — comma-separated list (e.g., `L2, FS`).

Cover at minimum: prompt injection defences; input classification; rate limiting per-input-class; input-size bounds; provenance check on incoming content.

#### §12.2 Output Guardrails

Same column structure. Cover: output sanitisation; PII / sensitive-content redaction; output-classification gating; downstream-system validation contract; output-size bounds.

#### §12.3 Behavioural Guardrails

Same column structure. Cover: tool-use scope enforcement; action-class authorisation per autonomy tier; refusal behaviour on ambiguous instruction; goal-hijacking defences (per OWASP Agentic AI); memory-poisoning defences.

#### §12.4 Guardrail Architecture Assessment

One paragraph (120–200 words) on the framework's guardrail architecture — defence-in-depth vs. defence-in-line, per-layer enforcement vs. centralised, runtime vs. build-time, machine-enforced vs. convention.

Then a mandatory sub-block **Governance Failure Mode Coverage** assessing six modes that ASDLC inherits from manifesto P10 and operationalises across `governance/agents.md`, `waiver-governance.md`, and `governance/queries.md`. For each mode: Met / Partially met / Absent verdict + 1–2 sentence explanation citing `[[FRAMEWORK]]` evidence.

The six governance failure modes:
1. **Evidence laundering** — evidence bundles produced without independent verification, presented as proof.
2. **Approval laundering** — approval steps that have become rubber-stamps; approver does not engage with the artefact.
3. **Compliance theater** — controls that produce documentation but do not change behaviour.
4. **Stale-control reliance** — relying on a control whose currency / freshness has lapsed.
5. **Automated rubber-stamping** — agent-produced approvals presented as accountable sign-off.
6. **Waiver accumulation** — waivers granted without expiry, debt tracking, or portfolio review (per `waiver-governance.md`).

#### §12.4a Tool-authorization enforcement assessment

`agent-control-plane.md` defines three permitted tool-authorization enforcement modes. The framework MUST declare, per Agent node, an `enforcement_mode` schema field whose value is one of:

- **`in-band-token`** — control-plane-issued, signed capability token with default lifetime ≤ 1 hour, verified at tool runtime before any side effect.
- **`sandbox`** — sandboxed runtime mediation; every tool call is intercepted before any side effect.
- **`post-hoc-audit`** — unauthorised calls are logged and produce an immediate `Incident` node plus `EvidenceArtifact`. Detective-only.
- **`compound`** — two or more of the above simultaneously (e.g., in-band-token + sandbox).

The per-AutonomyTier requirement matrix (normative):

| AutonomyTier | Minimum required enforcement mode |
| --- | --- |
| **A1 — advisory** | `post-hoc-audit` is acceptable; `in-band-token` recommended. |
| **A2 — monitored execution** | `sandbox` OR `in-band-token` MUST be used. `post-hoc-audit` alone is non-conformant. |
| **A3 — limited autonomy** | `in-band-token` is REQUIRED. `sandbox` is additionally REQUIRED for any tool with side effects beyond reading. |
| **A4 — Tier 4 envelope operation** | `in-band-token` AND `sandbox` are both REQUIRED (compound). `post-hoc-audit` logs are an additional control, not a substitute. |

Render a markdown table with columns:

```
| AutonomyTier supported by [[FRAMEWORK]] | Declared enforcement_mode | Per-tier requirement | Verdict (Met / Partial / Non-conformant / Absent) | Evidence |
```

One row per AutonomyTier the framework supports. The Verdict column is `Met` if the declared mode meets or exceeds the per-tier minimum; `Partial` if some tools meet it but the schema does not enforce it framework-wide; `Non-conformant` if the declared mode falls below the minimum; `Absent` if the framework does not declare an `enforcement_mode` field at all. Cite `[[FRAMEWORK]]` source verbatim in the Evidence column.

#### §12.4b OWASP Agentic AI threat-to-mitigation matrix

The framework MUST provide explicit mitigations for the OWASP Agentic AI threat categories (per *OWASP Agentic AI — Threats and Mitigations, 2025*). Score each as one of `Present` / `Partially-present` / `Absent` with a one-sentence evidence anchor citing `[[FRAMEWORK]]` source verbatim.

```
| OWASP Agentic AI threat category | Required mitigation question | [[FRAMEWORK]] verdict | Evidence |
```

The six threat categories (rows are mandatory; row set is canonical and MUST NOT be modified):

1. **Tool misuse** — does the framework's enforcement mechanism (per §12.4a) prevent unauthorised tool invocation?
2. **Goal hijacking** — does the framework define a goal / objective specification with a verification mechanism?
3. **Identity & privilege abuse** — does the framework define an Agent identity model with versioning and authorization records?
4. **Memory poisoning** — does the framework define memory scope, sanitisation, and audit?
5. **Excessive agency** — does the framework cap autonomy via blast-radius and AutonomyTier limits?
6. **Unsafe tool composition** — does the framework require composition records and audit cross-tool authorization?

The authority is *OWASP Agentic AI — Threats and Mitigations (2025)*, cited per row where relevant.

#### §12.5 Adversarial Scenario

A red-team walk-through. Name a `[[ORGANIZATION]]` business workflow (sourced from `[[DOMAIN_FILE]]`) and walk through an adversarial scenario from NIST AI 100-2e2025 or OWASP Agentic AI. Show: (a) attacker objective; (b) attack vector against `[[FRAMEWORK]]`-managed system; (c) which `[[FRAMEWORK]]` guardrails fire (or fail to fire); (d) outcome at each ASDLC layer / gate; (e) concluding verdict naming the relevant ASDLC governance failure mode by name (per §12.4 sub-block).

The scenario MUST cite at least one named real-world incident that illustrates this attack class — drawn from the public record (e.g., Slack-AI exfiltration, Replit AI database deletion, agent-driven SDLC failures documented in Pearce et al. 2022 / Perry et al. 2023). The framework must be assessed against whether its guardrails would prevent or mitigate that incident class.

### 2.2 Part 13 — Security, FinOps & DevSecOps Assessment

Part 13 has six required subsections (one more than the AEM version, to absorb FinOps + DevSecOps):

#### §13.1 Determinism and Output Variance

One paragraph + concluding verdict line. Concludes with exactly one of these literal lines on a separate line:

- `**Determinism verdict: DETERMINISTIC-ADEQUATE**`
- `**Determinism verdict: PARTIALLY-DETERMINISTIC**`
- `**Determinism verdict: NON-DETERMINISTIC**`

The verdict reflects whether the framework's outputs are reproducible given identical inputs (DETERMINISTIC-ADEQUATE), partially reproducible (e.g., temperature=0 but tool ordering varies), or fundamentally non-reproducible without architectural change.

#### §13.2 Security Coverage Map

Markdown table with exactly 11 control-family rows (these are framework-agnostic; do NOT modify the row set):

```
| Control family | [[FRAMEWORK]] coverage | Mechanism | NIST SSDF / 800-218A mapping | Gap |
```

The 11 control families:
1. SAST (static application security testing)
2. DAST (dynamic application security testing)
3. SCA (software composition analysis)
4. Secrets scanning
5. SBOM generation
6. Dependency vulnerability scanning
7. Container / artefact image scanning
8. IaC (infrastructure-as-code) scanning
9. License compliance
10. Code provenance / SLSA attestation
11. Runtime application self-protection (RASP) / behavioural monitoring

Each row: `Met` / `Partial` / `Absent` in the coverage column; mechanism cite from `[[FRAMEWORK]]` source; SSDF mapping citing the relevant practice group from `security-governance.md`.

#### §13.3 Bias and Fairness Exposure

One paragraph + 2–4 bullets. Assess whether `[[FRAMEWORK]]` provides mechanisms to detect or mitigate bias in agent outputs (relevant to EU AI Act Article 10 obligations and `[[DOMAIN_FILE]]` fairness obligations).

#### §13.4 Regulatory Security Requirements

Markdown table with rows **exclusively** from `[[DOMAIN_FILE]]`'s security-relevant regulatory mappings (e.g., DORA Article 9, SR 11-7 §IV.A, GDPR Article 32). Do not import requirements from regulations not named in `[[DOMAIN_FILE]]`.

```
| Regulation / article | Requirement | [[FRAMEWORK]] coverage | Gap |
```

#### §13.5 FinOps Coverage

Markdown table assessing `[[FRAMEWORK]]`'s coverage of `finops-governance.md`'s requirements:

```
| FinOps capability | [[FRAMEWORK]] mechanism | FinOps Foundation maturity stage | Gap |
```

Cover at minimum: per-task token-cost attribution; cost SLO enforcement; model-tier selection by task class; FOCUS-compatible cost reporting; budget enforcement at the inference layer; cost-anomaly alerting.

#### §13.6 Critical Security Findings

3–6 critical findings, each with the exact labelled fields in this order:

```
**Finding {N} — {short title}**

- **Evidence:** <verbatim quote from [[FRAMEWORK]] source with file path>
- **Business impact:** <one sentence stating the operational consequence for [[ORGANIZATION]]>
- **Remediation:** <1–2 sentences naming the artefact / mechanism that closes the finding>
- **Severity:** <Critical / High / Medium / Low>
- **Effort:** <S / M / L / XL>
- **ASDLC categories violated:** <comma-separated list>
```

#### §13.7 Production drift detection assessment

`operations/governance.md` defines a *Model and Data Drift Detection* obligation. Score `[[FRAMEWORK]]` against the following five normative questions, each as `Met` / `Partial` / `Absent` with one-sentence evidence anchor citing `[[FRAMEWORK]]` source verbatim or recording explicit absence:

```
| Drift detection question | [[FRAMEWORK]] verdict | Evidence |
```

The five questions (canonical row set; MUST NOT be modified):

1. **Production benchmark portfolio + cadence by AutonomyTier** — does the framework define a production-side benchmark portfolio with cadence calibrated to AutonomyTier (continuous for A4, daily for A3, weekly for A2)?
2. **Drift SLO by AutonomyTier** — does the framework define a drift detection-to-response SLO (4 hours for A4, 24 hours for A3, 72 hours for A2)?
3. **Drift incident classification** — does the framework define a `Drift` incident class distinct from `Quality`, `Infrastructure`, and `Security` incident classes?
4. **Champion / challenger pattern** — does the framework specify the champion / challenger pattern for foundation-model-backed systems (production champion vs. shadow challenger with periodic comparison)?
5. **Foundation-model-drift gate trigger** — does drift confirmed traceable to provider-side foundation-model behavioural change trigger the foundation-model-drift gate condition (per `release-governance.md` Condition 1 sub-clause on foundation-model drift)?

Conclude with a one-sentence verdict line stating whether the framework's drift detection posture is `Met` / `Partial` / `Absent` overall, naming which of the five questions drove the verdict.

### 2.3 Banned soft language
Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`. Use declarative form.

### 2.4 Idempotence
Glob output. If exists AND ≥ 20 lines AND contains both Part 12 and Part 13 H2 headings AND all subsections (§12.1, §12.2, §12.3, §12.4, §12.4a, §12.4b, §12.5; §13.1–§13.7), exit. Otherwise rewrite.

---

## 3. Output structure

```
# [[FRAMEWORK]] Review 07 — Guardrails, Security, FinOps & DevSecOps (Parts 12 + 13)

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`
**Sources read:** <enumerate every file actually read>

---

## Part 12 — AI/Runtime Guardrails Assessment

### §12.1 Input Guardrails
<table per §2.1>

### §12.2 Output Guardrails
<table per §2.1>

### §12.3 Behavioural Guardrails
<table per §2.1>

### §12.4 Guardrail Architecture Assessment
<one paragraph + Governance Failure Mode Coverage sub-block with all 6 modes>

### §12.4a Tool-authorization enforcement assessment
<per-AutonomyTier table per §2.1, naming declared `enforcement_mode` (in-band-token / sandbox / post-hoc-audit / compound) and per-tier verdict against the A1 / A2 / A3 / A4 requirement matrix>

### §12.4b OWASP Agentic AI threat-to-mitigation matrix
<six-row canonical table covering tool misuse, goal hijacking, identity & privilege abuse, memory poisoning, excessive agency, unsafe tool composition; Present / Partially-present / Absent verdict per row>

### §12.5 Adversarial Scenario
<red-team walk-through with named real-world incident citation and ASDLC governance failure mode verdict>

---

## Part 13 — Security, FinOps & DevSecOps Assessment

### §13.1 Determinism and Output Variance
<one paragraph + Determinism verdict line>

### §13.2 Security Coverage Map
<11-row table per §2.2>

### §13.3 Bias and Fairness Exposure
<one paragraph + 2–4 bullets>

### §13.4 Regulatory Security Requirements
<table with rows exclusively from [[DOMAIN_FILE]]>

### §13.5 FinOps Coverage
<table per §2.2>

### §13.6 Critical Security Findings
<3–6 findings with exact labelled fields per §2.2>

### §13.7 Production drift detection assessment
<five-row canonical table covering production benchmark cadence by AutonomyTier, drift SLO by AutonomyTier, Drift incident class, champion / challenger pattern, foundation-model-drift gate trigger; Met / Partial / Absent verdict per row plus closing verdict line>

---
```

---

## 4. Hard rules

1. **Read `[[FRAMEWORK]]`'s source files before scoring.**
2. **Read all the ASDLC artefacts in §1.2–§1.4 before scoring.**
3. **Quote verbatim from `[[FRAMEWORK]]` source files** with backticked file paths. Paraphrase is not evidence.
4. **§12.4 Governance Failure Mode Coverage MUST cover all six modes** — none may be omitted.
5. **§12.5 Adversarial Scenario MUST cite at least one named real-world incident** that illustrates the attack class.
6. **§13.1 Determinism verdict line is mandatory** in the exact form `**Determinism verdict: DETERMINISTIC-ADEQUATE**` / `PARTIALLY-DETERMINISTIC` / `NON-DETERMINISTIC` on its own line.
7. **§13.2 Security Coverage Map has exactly 11 rows** in the canonical control-family order.
8. **§13.4 Regulatory Security Requirements rows are sourced exclusively from `[[DOMAIN_FILE]]`** — no imports from other regulations.
9. **§13.5 FinOps Coverage assesses `finops-governance.md` requirements.** Cite the FinOps Foundation maturity stage per row.
10. **§13.6 Critical Security Findings count is 3–6**, each with the exact labelled fields.
11. **Date format YYYY-MM-DD.** British English.
12. **Cross-references** use canonical part numbers.
13. **Out-of-scope corpus / tracked-files-only.** Every source file cited MUST be tracked by git on the current branch. Do not read or reference `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.md`, `agentic-enterprise.html`, `agentic-governance-stack.md`, `agentic-governance-stack.html`, `manifesto-evolution-plan.md`, `manifesto-evolution-plan.html`, `phase-assessment-checklist.md`, `phase-assessment-checklist.html`, `aplc-plan*`, or `igm-aent-coherence-review*` anywhere in the output. The output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`. If `[[DOMAIN_FILE]]`, a regulatory crosswalk, a governance file, or an operational template references these paths, ignore those sections and do not forward-propagate them.
14. **Banned soft language.** Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`.
15. **Cross-stack references.** ASDLC's external evidence base (NIST SP 800-218A, NIST AI 100-2e2025, OWASP Agentic AI, OWASP Top 10 for LLM, CISA Secure by Design, NIST AI RMF 1.0, FinOps FOCUS) is in scope and must be referenced. APLC / IGM / AEnt-M material is out of scope and must NOT be referenced.
16. **§12.4a, §12.4b, §13.7 are additive.** The existing §12 Guardrails Architecture and §13 Security + FinOps + DevSecOps content remains in full. The enforcement-mode assessment, OWASP Agentic AI threat-to-mitigation matrix, and production drift detection assessment are new subsections, not replacements for existing scope.

---

## 5. Self-Check Before Writing — gate

**Do not save the output file until every item below is confirmed.** Each item is a hard gate; a single failure blocks the write.

- [ ] All `[[VARIABLE]]` placeholders have been substituted.
- [ ] `[[FRAMEWORK]]` artefacts have been read — specific files are named in the sources-read header.
- [ ] All ASDLC artefacts in §1.2–§1.4 have been read.
- [ ] `[[DOMAIN_FILE]]` has been read; at least three specific regulatory articles are cited in Part 13.
- [ ] §12.1, §12.2, §12.3 each contain a markdown table with the canonical column headers (Guardrail | Mechanism | Enforcement Level | Gap | ASDLC categories).
- [ ] §12.4 contains the Governance Failure Mode Coverage sub-block scoring all six modes (evidence laundering, approval laundering, compliance theater, stale-control reliance, automated rubber-stamping, waiver accumulation).
- [ ] §12.4a Tool-authorization enforcement assessment table is present with one row per AutonomyTier the framework supports; declared `enforcement_mode` is named (in-band-token / sandbox / post-hoc-audit / compound) and scored against the A1 / A2 / A3 / A4 per-tier requirement matrix.
- [ ] §12.4b OWASP Agentic AI threat-to-mitigation matrix is present with all six canonical rows (tool misuse, goal hijacking, identity & privilege abuse, memory poisoning, excessive agency, unsafe tool composition); each row carries a Present / Partially-present / Absent verdict; OWASP Agentic AI (2025) is cited as the authority.
- [ ] §12.5 adversarial scenario cites at least one named real-world incident; the verdict explicitly names one of the six governance failure modes.
- [ ] §13.1 contains exactly one Determinism verdict line on its own line in the canonical form.
- [ ] §13.2 Security Coverage Map has exactly 11 rows in canonical control-family order with NIST SSDF / 800-218A mapping per row.
- [ ] §13.3 covers bias and fairness exposure with at least one regulation citation from `[[DOMAIN_FILE]]`.
- [ ] §13.4 Regulatory Security Requirements rows are sourced exclusively from `[[DOMAIN_FILE]]`.
- [ ] §13.5 FinOps Coverage table assesses at least 6 capabilities with FinOps Foundation maturity stage per row.
- [ ] §13.6 contains 3–6 Critical Security Findings, each with the exact labelled fields (Evidence / Business impact / Remediation / Severity / Effort / ASDLC categories violated).
- [ ] §13.7 Production drift detection assessment is present with all five canonical rows (production benchmark cadence by AutonomyTier — continuous A4 / daily A3 / weekly A2; drift SLO — 4h A4 / 24h A3 / 72h A2; Drift incident class distinct from Quality / Infrastructure / Security; champion / challenger pattern for foundation-model-backed systems; foundation-model-drift gate trigger linking to `release-governance.md` Condition 1 sub-clause); each row carries a Met / Partial / Absent verdict; the closing verdict line is present.
- [ ] Zero matches for any out-of-scope-corpus token (`APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, `igm-aent-coherence-review`) anywhere in the output, even where `[[DOMAIN_FILE]]` or any cross-stack file mentions them. Every cited source file is tracked by git on the current branch.
- [ ] No banned soft language appears.
- [ ] All dates use YYYY-MM-DD format.
- [ ] All cross-references use canonical part numbers.
