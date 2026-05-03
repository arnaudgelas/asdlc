# Sub-prompt 08a — Enterprise Guardrail Domains (Part 14, intermediate §14.1–§14.15)

**Purpose.** Produce the intermediate Part 14 file for `[[FRAMEWORK]]` covering 15 enterprise agentic guardrail domains. Output is intermediate; agent 08b lifts §14.1–§14.15 verbatim and adds the cross-cutting matrix (§14.16), twelve non-negotiables (§14.17), schema verification (§14.18), and maturity verdict (§14.19) as the canonical Part 14 file.

**Wave:** Wave 1a. Runs in parallel with 01, 02-l1..l4, 02-g1..g3, 03, 04a, 04b, 05a, 07. Cannot read other agents' outputs.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_08a_domains.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`.

---

## 1. Inputs to read

### 1.1 `[[FRAMEWORK]]` artefacts
Read every source file at `[[FRAMEWORK_VERSION]]`. Quote exact rule text, schema fields, control definitions, and operational mechanisms.

### 1.2 ASDLC core (mandatory)
- `asdlc.md` — for the four-layer model, three gates, ASDLC values, governance posture.
- `governance/agents.md` — autonomy tier definitions (Tier 1 / 2 / 3 / 4); epistemic tier labelling.
- `agent-control-plane.md` — named governance agents and their schemas (the canonical Agent Card / Task Card schema sources for §14.18).
- `governance/graph.md` — GateState model (relevant to §14.5 provenance and §14.8 observability).
- `governance/queries.md` — canonical governance questions (relevant to §14.8 monitoring).

### 1.3 Layer + gate authoritative artefacts
Read `governance/gate-registry.yaml` first — it is the machine-readable single source of truth for gate condition counts, titles, and profile names. The companion prose `governance/gate-registry.md` paraphrases the YAML for human readers. Then read the prose sources `specification-readiness.md`, `release-governance.md`, `operations/dod.md` for the per-condition narrative. Gate pass conditions inform several domain assessments (e.g., §14.9 verification/validation/evidence aligns to G2 and the AEM evidence bundle); when a domain's required-controls table cites a specific gate condition, cite the registry's condition title verbatim.

### 1.4 Cross-cutting (read where directly relevant)
- `security-governance.md`, `devsecops-controls.md` — for §14.10 security guardrails.
- `finops-governance.md` — for §14.7 cost & resource limits.
- `waiver-governance.md` — for §14.6 specification & change control.
- `maintenance-governance.md` — for §14.11 data lifecycle and §14.15 learning / memory governance.

### 1.5 AEM cross-reference (mandatory for §14.9 evidence bundle anchor)
- `../manifesto-done.md` — the seven-condition Engineering DoD that produces the evidence bundle.

### 1.6 Domain file
- `[[DOMAIN_FILE]]` — read in full. Map every domain's regulatory exposure to specific articles.

The recognised domain catalogue is:

- `domains/insurance.md` — European insurance (Solvency II, IDD, DORA overlay).
- `domains/financial-services.md` — banking and capital markets (Basel III/IV, MiFID II, DORA).
- `domains/pharma.md` — pharmaceutical R&D and manufacturing (GxP, FDA 21 CFR Part 11, EMA Annex 11).
- `domains/aviation.md` — civil aviation and aerospace (DO-178C, ARP4754A, EASA AMC 20-115D).
- `domains/automotive.md` — automotive and ADAS (ISO 26262, ISO 21434, UNECE WP.29).
- `domains/defense-government.md` — defence and government (DoDI 5000.97, NIST SP 800-53, FedRAMP).
- `domains/sox.md` — US Sarbanes-Oxley financial reporting controls; ICFR, Section 302 management certification, Section 404 management/auditor attestation, COSO 2013 and PCAOB AS 2201.
- `domains/hipaa.md` — US healthcare protected health information; Privacy Rule (45 CFR §164.500–.534), Security Rule (45 CFR §164.302–.318), Breach Notification Rule (45 CFR §164.400–.414).
- `domains/ccpa.md` — California consumer privacy; CCPA and CPRA amendments; CPPA regulations and ADMT rules.
- `eu-ai-act-mapping.md` — cross-cutting EU AI Act risk-tier mapping (Article 6 high-risk; Article 9 risk management; Articles 12–15 logging, transparency, oversight, accuracy/robustness; Article 17 quality management; Article 26 deployer obligations; Article 72 post-market monitoring).

When `[[DOMAIN_FILE]]` resolves to one of `domains/sox.md`, `domains/hipaa.md`, `domains/ccpa.md`, or `eu-ai-act-mapping.md`, per-domain dispatch MUST produce regulatory exposure citations grounded in those articles in addition to the original six. When `[[INDUSTRY]]` overlay implies a US healthcare, US public-company, California consumer, or EU AI Act exposure, the agent MUST cross-reference `eu-ai-act-mapping.md` (where applicable) and the relevant US regime even when `[[DOMAIN_FILE]]` is one of the original six. Mappings MUST use "supports compliance with", "produces evidence aligned with", or "operationalises" framing — never "satisfies regulation X" or "is the X requirement". ASDLC artefacts are engineering controls; statutory satisfaction is determined by the framework operator's legal review, not by this review.

### 1.7 Lint suite as a credibility check

Agents MUST verify their enumeration of gate conditions, profile names, and enum values against the checkers invoked by `scripts/lint.py`. Specifically: `scripts/check_gate_counts.py` validates against the canonical counts and profile names declared in `governance/gate-registry.yaml`; `scripts/check_enums.py` validates the canonical seven-state GateState enum; `scripts/check_term_imports.py` validates that AEnt-M / IGM tokens carry appropriate attribution. A finding raised by any of these checkers against material the agent has produced or quoted is itself an integrity finding the agent MUST surface in the output, not silently correct.

---

## 2. Methodology

### 2.1 Per-domain output structure (mandatory for all 15 domains)

Each domain section MUST have:

```
### §14.{N} {Domain name}

**Domain question:** <one-sentence question that this domain answers>

**Required controls (per ASDLC):**

| Control | ASDLC source | Rationale |
|---|---|---|
<rows with control names, ASDLC source files, and one-clause rationale>

**[[FRAMEWORK]] coverage:**

| Control | [[FRAMEWORK]] mechanism | Coverage |
|---|---|---|
<rows; coverage values: Met / Partial / Absent / *[Scope gap]*>

**ASDLC anchor.** <One sentence stating which ASDLC layers / gates / categories most apply (e.g., "L2 + G2 + FS"; "L4 + Tier 4 envelope; CG").>

**Domain Coverage Score:** <0–100 integer>

**Top remediation for [[ORGANIZATION]]:** <one sentence naming the highest-leverage single change for this domain in [[ORGANIZATION]]'s context, citing at least one regulation from [[DOMAIN_FILE]] by article>
```

### 2.2 Domain catalogue (15 domains in canonical order)

| § | Domain | Domain question | Primary ASDLC anchor |
| --- | --- | --- | --- |
| 14.1 | Identity & Permissions | Who or what is the actor at each step, and what are they authorised to do? | CG; L2; `governance/agents.md` |
| 14.2 | Data classification & access boundaries | What data classes does the system see, and who/what may access each? | L2; L4; FS |
| 14.3 | Tooling & action surfaces | What tools / actions are available to agents, and what is excluded? | L2; CG; `agent-control-plane.md` |
| 14.4 | Autonomy & escalation | What autonomy tier governs each action class, and how does escalation work? | L2; CG; `governance/agents.md` autonomy tiers |
| 14.5 | Provenance & traceability | Can every action be traced to its specification, agent, model, and inputs? | L4 (G3 trace retention); CG (`governance/graph.md`); EM Engineering DoD |
| 14.6 | Specification & change control | How are specifications versioned, changed, and waived? | L1 (G1); CG (`waiver-governance.md`) |
| 14.7 | Cost & resource limits | What budgets / SLOs constrain inference cost and resource use? | FS (`finops-governance.md`); L4 |
| 14.8 | Monitoring & observability | What signals are produced; what is alertable; how is governance state queryable? | L4 (G3 SLOs); CG (`governance/queries.md`) |
| 14.9 | Verification, validation & evidence | How is correctness asserted, tested, and recorded? | L2 (Engineering DoD); G2 (Release Gate); G3 |
| 14.10 | Security guardrails | What attack classes are defended against; what controls run at build / release / runtime? | FS (`security-governance.md`, `devsecops-controls.md`); G2; G3 |
| 14.11 | Data lifecycle | How are data inputs / outputs retained, retired, and audited? | L4 (`maintenance-governance.md`); G3 |
| 14.12 | Incident response & rollback | What happens when something fails — detection, containment, rollback, lessons-captured? | L4; G2 (rollback tested); FB |
| 14.13 | Human guardrails (oversight, escalation, accountability) | What human decisions are mandatory; who is accountable; how is rubber-stamping detected? | CG; L1, L2, L3, L4 (per-layer accountable human) |
| 14.14 | Vendor / model governance | How are external models / dependencies tracked, versioned, and replaced? | L4 (`maintenance-governance.md`); FS |
| 14.15 | Learning / memory governance | How is what the system has learned stored, audited, and improved between runs? | FB (L4→L2 feedback); L4; CG |

### 2.3 Required controls — examples per domain

Each domain's "Required controls" table MUST list 4–8 controls. The agent derives the controls from the cited ASDLC sources (§1.2–§1.5). Examples (illustrative; adapt to `[[FRAMEWORK]]`'s artefact set):

- §14.1 controls might include: agent identity registration, named accountable human per agent, role-based action authorisation, tool-scope per role, audit trail of actor identity per action.
- §14.4 controls might include: per-action-class autonomy tier definition; tier-to-action-class machine enforcement; escalation chain on autonomy violation; envelope-level governance for Tier 4; rubber-stamping detection per `governance/agents.md`.
- §14.9 controls might include: evidence bundle conforming to `../manifesto-done.md` schema; independent validation for Phase 4+; provenance record per agent; rollback procedure tested with measured time-to-rollback.

### 2.4 Operating principle for §14.15

The §14.15 (Learning / memory governance) section MUST include the following operating principle as one of its required controls or as a `**Failure-class operating principle:**` sub-block:

> A failed agent run must improve the harness before it is retried.

This principle traces to ASDLC's feedback-paths-closure requirement (§ Feedback Paths in `asdlc.md`): a maintenance signal that produces only a hotfix, without an evaluation suite update or harness improvement, has not closed.

### 2.5 Regulatory framing

All regulatory mappings produced by this prompt MUST use "supports compliance with", "produces evidence aligned with", or "operationalises" — never "satisfies regulation X", "is the X requirement", "meets regulation X", "complies with regulation X", or equivalents asserting statutory satisfaction. ASDLC produces engineering controls and evidence; statutory satisfaction is a legal determination made by the operator. This rule applies to per-domain "Required controls" rationale, "[[FRAMEWORK]] coverage" rows, "Top remediation" sentences, and any prose tying a control or artefact to a specific article.

### 2.6 Banned soft language
Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`. Use declarative form.

### 2.7 Idempotence
Glob output. If exists AND ≥ 20 lines AND contains all 15 §14.{N} subsections AND each contains the canonical 5 mandatory blocks (Domain question; Required controls table; [[FRAMEWORK]] coverage table; ASDLC anchor; Domain Coverage Score; Top remediation), exit. Otherwise rewrite.

---

## 3. Output structure

```
# [[FRAMEWORK]] Review 08a — Enterprise Guardrail Domains (intermediate §14.1–§14.15)

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`
**Sources read:** <enumerate every file actually read>

---

## Part 14 (intermediate) — Enterprise Guardrail Domains

<§14.1 through §14.15 in canonical order, each with the 5 mandatory blocks per §2.1>

---
```

---

## 4. Hard rules

1. **Read all sources in §1.2–§1.5 before scoring.**
2. **All 15 domains MUST be present in canonical order** (§14.1 through §14.15).
3. **Each domain section MUST contain all 5 mandatory blocks** (Domain question; Required controls table; [[FRAMEWORK]] coverage table; ASDLC anchor; Domain Coverage Score; Top remediation).
4. **Every coverage statement names a specific [[FRAMEWORK]] artefact** AND quotes verbatim with file path.
5. **Domain Coverage Score is an integer 0–100.**
6. **§14.15 contains the operating principle** "A failed agent run must improve the harness before it is retried." as a required control or sub-block.
7. **ASDLC anchor names categories** by their `prompt.md` short form (L1 / G1 / L2 / G2 / L3 / G3 / L4 / T4 / CG / FS / FB).
8. **Date format YYYY-MM-DD.** British English.
9. **Out-of-scope corpus / tracked-files-only.** Every source file cited MUST be tracked by git on the current branch. Do not read or reference `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.{md,html}`, `agentic-governance-stack.{md,html}`, `manifesto-evolution-plan.{md,html}`, `phase-assessment-checklist.{md,html}`, `aplc-plan*`, or `igm-aent-coherence-review*`. Output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`.
10. **Banned soft language.** Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`.
11. **Regulatory framing.** All regulatory mappings MUST use "supports compliance with" / "produces evidence aligned with" / "operationalises". Output MUST NOT use "satisfies regulation", "is the X requirement", "meets regulation", or "complies with regulation" framing.
12. **Lint cross-check.** Gate condition counts, profile names, and GateState enum values cited in the output MUST be verifiable against `governance/gate-registry.yaml` (`scripts/check_gate_counts.py`) and the seven-state GateState enum (`scripts/check_enums.py`). AEnt-M / IGM tokens, where unavoidable, MUST be attributed per `scripts/check_term_imports.py`. A finding raised by any checker against the agent's output is an integrity finding the agent MUST surface.
13. **Do not include cross-cutting matrix (§14.16), twelve non-negotiables (§14.17), schema verification (§14.18), or maturity verdict (§14.19).** Those are produced by agent 08b in the canonical Part 14 file.
14. **Do not produce a composite [[FRAMEWORK]] score.** Part 1 is owned by agent 01.

---

## 5. Self-check before saving

- [ ] All 15 §14.{N} subsections are present in canonical order.
- [ ] Every subsection contains the 5 mandatory blocks (Domain question; Required controls table; [[FRAMEWORK]] coverage table; ASDLC anchor; Domain Coverage Score; Top remediation).
- [ ] Every coverage row names a specific [[FRAMEWORK]] artefact AND quotes verbatim.
- [ ] Each Domain Coverage Score is an integer 0–100.
- [ ] §14.15 contains the operating principle "A failed agent run must improve the harness before it is retried."
- [ ] Every ASDLC anchor uses canonical category short forms (L1 / G1 / L2 / G2 / L3 / G3 / L4 / T4 / CG / FS / FB).
- [ ] At least 5 distinct regulations from `[[DOMAIN_FILE]]` are referenced across the 15 domains.
- [ ] No §14.16, §14.17, §14.18, or §14.19 sections (those belong to agent 08b).
- [ ] Zero matches for any out-of-scope-corpus token (`APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, `igm-aent-coherence-review`) anywhere in the output.
- [ ] No banned soft language appears.
- [ ] All regulatory mappings use "supports compliance with" / "produces evidence aligned with" / "operationalises" framing; no "satisfies regulation" / "is the X requirement" / "meets regulation" / "complies with regulation" phrasing appears.
- [ ] When `[[DOMAIN_FILE]]` is `domains/sox.md`, `domains/hipaa.md`, `domains/ccpa.md`, or `eu-ai-act-mapping.md`, regulatory exposure citations are grounded in those domains' specific articles.
- [ ] Gate condition counts, profile names, and GateState enum values cited are reconcilable with `governance/gate-registry.yaml` and the canonical seven-state GateState enum; any checker finding raised by `scripts/lint.py` against the output is surfaced as an integrity finding.
- [ ] All dates use YYYY-MM-DD format.
- [ ] All `[[VARIABLE]]` placeholders are substituted.
