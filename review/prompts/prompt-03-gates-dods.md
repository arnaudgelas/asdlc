# Sub-prompt 03 — Cross-Gate Synthesis & Definitions of Done

**Purpose.** Produce the Part 5 file for `[[FRAMEWORK]]` — the cross-gate synthesis, the AEM Engineering DoD assessment, and the ASDLC Operational DoD assessment. This file is the authoritative source for cross-gate failure-mode analysis and DoD assessments; agent 01 reads this file to populate the corresponding rows of Part 1.

**Wave:** Wave 1a. This prompt runs in parallel with prompts 01, 02-l1..l4, 02-g1..g4, 04a, 04b, 05a, 07, and 08a. It cannot read their outputs. Cross-references for analyses produced by other agents use canonical Part numbers — agent 09 (merge) resolves them.

**Note to orchestrator:** All `[[VARIABLE]]` placeholders in this file must be substituted before this prompt is passed to the agent. If any `[[...]]` pattern remains in your working copy, stop and resolve it before spawning.

**Output file.** Write exactly one file: `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_03_gates_dods.md`

**Canonical thresholds.** Severity labels, score ranges, effort labels, and category weightings are defined in `prompt.md`. Reference them; do not redefine.

---

## 1. Inputs to read

Before scoring, read the following in full. Do not score from memory.

### 1.1 `[[FRAMEWORK]]` artefacts
Read every source file that constitutes `[[FRAMEWORK]]` at version `[[FRAMEWORK_VERSION]]`. Quote exact gate names, condition identifiers, schema fields, and DoD-equivalent definitions when making claims.

### 1.2 ASDLC core (mandatory)
- `asdlc.md` — gate definitions, gate failure modes, feedback paths, ASDLC values.
- `asdlc-guide.md` — recommended adoption sequence, common failure modes, integration guidance.
- `README.md` — top-level gate descriptions and entry points.

### 1.3 Gate authoritative artefacts (mandatory — abort if any missing)
- `governance/gate-registry.yaml` — **the machine-readable canonical source of truth for every ASDLC gate's condition count and condition titles.** Read first. All gate condition counts cited in this output MUST match the YAML registry verbatim. Any divergence between the YAML registry and the prose sources below MUST be surfaced as an integrity finding.
- `governance/gate-registry.md` — derived human-readable view of `governance/gate-registry.yaml`; use for orientation, but the YAML is canonical when the two diverge.
- `specification-readiness.md` — authoritative prose source for SR Gate conditions.
- `release-governance.md` — authoritative prose source for Release Gate conditions and the release-approval chain.
- `deployment-governance.md` — environment promotion gates, feature-flag governance, rollback operationalisation.
- `operations/dod.md` — authoritative prose source for Operational Readiness Gate conditions.
- `retirement-gate.md` — authoritative prose source for Retirement Gate (G4) conditions.

### 1.4 AEM Engineering DoD (mandatory for Engineering DoD assessment)
- `../manifesto-done.md` — the seven engineering DoD conditions (Shipped, Observable, Verified, Provable, Learned from, Governed, Economical), the Hardening DoD, the agentic provenance record, the bundle integrity attestation, and the evidence freshness rules.
- `../manifesto.md` — defines what enters the Engineering DoD (the loop output).

If `../manifesto-done.md` is unreachable and `AGENTIC_MANIFESTO_PATH` is unset, abort. Engineering DoD cannot be assessed without AEM source.

### 1.5 Operational governance (for Operational DoD)
- `operations/governance.md` — operational lifecycle, SLO/SLA governance, incident management.
- `maintenance-governance.md` — stewardship transfer, security patching, technical debt lifecycle, decommissioning.

### 1.6 Cross-cutting (read where directly relevant)
- `governance/agents.md` — governance agent framework, autonomy tier definitions, epistemic tier labelling.
- `agent-control-plane.md` — named governance agents and schemas.
- `waiver-governance.md` — waiver lifecycle relevant to all gates.
- `security-governance.md`, `devsecops-controls.md` — security and DevSecOps controls aligned to gates.
- `finops-governance.md` — FinOps governance aligned to L1 cost justification and L4 operational cost.

### 1.7 Domain file
- `[[DOMAIN_FILE]]` — read end-to-end. Map every gate-related and DoD-related finding to a specific regulation or risk type that applies to `[[ORGANIZATION]]`.

### 1.8 Prior reviews
If `[[PRIOR_REVIEWS]]` is not `none`, read those files for peer comparison.

---

## 2. Methodology

### 2.1 Gate scoring (Part 4 in canonical part numbering)

Score each of the four gates 0–100 (integer) and provide a single-sentence assessment (≤ 50 words; semicolon-joined two-clause sentences count as a single sentence):

- G1 — Specification Readiness Gate
- G2 — Release Gate
- G3 — Operational Readiness Gate
- G4 — Retirement Gate

For each gate, the one-sentence assessment must contain BOTH an evidence-for clause (a specific `[[FRAMEWORK]]` artefact that supports the score) AND an evidence-against clause (the specific condition or set of conditions that `[[FRAMEWORK]]` does not enforce). Scope-gaps (the gate is documented as out of scope for the framework) are noted in the assessment with `*[Scope gap]*`; the score reflects what the framework provides relative to ASDLC's bar. G4 MAY legitimately be marked Not Applicable for frameworks predating retirement formalisation (per `prompt-02-gate.md`'s G4 handling); when N/A, state so explicitly and exclude G4 from the gate-pass-pattern analysis below.

**Score-consistency invariant.** The Part 4 per-gate scores in this file MUST equal the corresponding rows in agent 01's Part 1 Gates Table (and agent 02-g1..g4's individual scores). If the per-gate agents (02-g1..g4) produce numerically different scores, agent 09 (merge) detects the mismatch and surfaces it. Treat this file's scores as authoritative for Part 4.

### 2.2 Engineering DoD scoring (part of Part 5)

Score each of the seven AEM Engineering DoD conditions 0–100 (integer) and provide a single-sentence assessment (≤ 50 words):

- Shipped
- Observable
- Verified
- Provable
- Learned from
- Governed
- Economical

For each condition, the one-sentence assessment must contain BOTH an evidence-for clause (a specific `[[FRAMEWORK]]` artefact) AND an evidence-against clause (the specific gap against the AEM DoD definition in `../manifesto-done.md`).

The Engineering DoD is the **input** to the Release Gate (G2 condition 1). A weakness in the Engineering DoD propagates directly to G2 risk.

### 2.3 Operational DoD scoring (part of Part 5)

The Operational DoD is the Operational Readiness Gate (G3) viewed as a steady-state operational obligation rather than a release-time gate evaluation. It carries 8 entries per `governance/gate-registry.yaml`: DoD-1 through DoD-7 are unconditional; DoD-8 (DR/Failover Tested) is blocking for blast-radius tier 3. Score the framework's coverage of each Operational DoD condition 0–100 (integer):

1. Runbook complete and current
2. SLOs defined and monitoring configured
3. On-call assigned, briefed, and current
4. System steward assigned, current, and accepting accountability
5. Security scan clean — current dependency tree, current vulnerability data
6. License compliance confirmed — current dependency tree
7. Trace retention policy set, configured, and exercised
8. DR/Failover Tested — *conditional; blocking only for blast-radius tier 3, recommended otherwise*

For each condition: one-sentence assessment with evidence-for and evidence-against. The Operational DoD differs from G3 in that G3 is a release-time pass/fail check whereas the Operational DoD is the ongoing obligation — it can degrade over time as the runbook goes stale, as dependency updates introduce new vulnerabilities, as the steward leaves without transfer.

### 2.4 Cross-Gate Failure Modes section

Cross-gate analysis MUST consider all four gates (G1, G2, G3, G4). When G4 is marked Not Applicable per §2.1, the cross-gate failure-mode analysis still tests G3→G4 propagation hypothetically (i.e., the absence of a Retirement Gate is itself a failure mode worth surfacing) but excludes G4 from the gate-pass-pattern statistical synthesis.

Identify at least 5 distinct cross-gate failure modes — patterns where a weakness or partial pass at gate X creates a foreseeable failure at gate Y (or in the layer between them). For each:

- Format: `- **G{X}→G{Y}:** {failure mode description}`
- Each must cite at least two `[[FRAMEWORK]]` artefacts in backticks AND at least one regulation by article from `[[DOMAIN_FILE]]`.
- Examples (illustrative; the agent must derive these from `[[FRAMEWORK]]`'s artefacts, not copy them):
  - `**G1→G2:** Specifications enter the loop without explicit constraints (G1 partial pass) → Release Gate compliance documentation is filed against an unverifiable specification (G2 condition 5 silently fails) → SR 11-7 §IV.A model documentation requirement is unmet.`
  - `**G2→G3:** Rollback procedure documented but not tested (G2 condition 3 partial pass) → operational readiness assumes time-to-rollback meets SLO without measurement (G3 condition 1 unverifiable) → DORA Art. 12 ICT incident-response timeliness obligation is at risk.`
  - `**G3→G4:** Operational telemetry retained per G3 condition 7 but no retirement-time data-disposition obligation defined (G4 absent) → decommissioning leaves residual personal data in trace stores → GDPR Art. 17 right-to-erasure obligation is unmet.`

### 2.5 Cross-Layer Feedback Closure section

Assess `[[FRAMEWORK]]`'s coverage of the four ASDLC feedback paths (`asdlc.md` § Feedback Paths — the post-sprint version with the unified-schema sentence after the four path descriptions):

1. L4 → L1: value data to demand prioritisation
2. L4 → L2: maintenance signals to engineering Learn / Govern phases
3. L3 → L2: release failures to engineering Govern phase
4. L2 → L1: validation failures to demand layer retrospectives

**Unified closure schema.** All four feedback paths share the same closure schema: a process-change record + a corresponding evaluation/validation/criterion update + a re-run that demonstrates the change is effective. A path that produces only a process-change record without the evaluation update has not closed. Cite `asdlc.md` § Feedback Paths.

For each of the four paths, test the following and emit a verdict (`Closed` / `Partial` / `Open`) with a one-sentence explanation citing `[[FRAMEWORK]]` evidence:

1. Does `[[FRAMEWORK]]` define the path — specifically the signal source, the destination governance authority, and the latency SLO (the time window within which the feedback must produce an upstream change)?
2. Does `[[FRAMEWORK]]` apply the unified closure schema — process change + evaluation/validation/criterion update + re-run demonstrating effectiveness?
3. If the closure schema is missing for any path, name the missing path-component combination explicitly (e.g., "L4→L2: process-change record present, evaluation update absent, re-run absent").

Note that ASDLC defines five feedback paths total; the fifth (L4 → IGM) is intentionally omitted from this assessment because IGM is out of scope for ASDLC reviews. State the omission explicitly.

### 2.6 Human Escalation Architecture section

Assess `[[FRAMEWORK]]`'s human-escalation architecture across the four gates (G1, G2, G3, G4; treat G4 as in-scope unless the gate is marked Not Applicable per §2.1) with four labelled sub-paragraphs:

1. **Escalation triggers** — what classes of gate failure or operational anomaly trigger escalation? Name the triggers and their thresholds.
2. **Escalation path** — to whom does each trigger class escalate? Name the roles, not individuals.
3. **Response time** — what response-time SLO governs each escalation class?
4. **Fitness for `[[ORGANIZATION]]` context** — how does the escalation architecture fit `[[ORGANIZATION]]`'s regulatory environment? Cite at least four named regulatory obligations from `[[DOMAIN_FILE]]` that the escalation architecture must satisfy.

### 2.7 Industry-Specific DoD Requirements section

When `[[DOMAIN_FILE]]` specifies a regulated industry (i.e., references named regulatory frameworks like SR 11-7, DORA, IEC 62304, GAMP 5, DO-178C, GDPR, EU AI Act, Solvency II, etc.), this section is mandatory. For each named regulation in `[[DOMAIN_FILE]]`:

- State the regulation's specific obligations that map to the Engineering DoD or Operational DoD (e.g., model governance, ICT risk management, configuration management records, retention period).
- Assess whether `[[FRAMEWORK]]`'s DoD coverage satisfies the obligation (Met / Partial / Absent) and cite specific evidence from `[[FRAMEWORK]]`'s artefacts.

When `[[DOMAIN_FILE]]` does not name regulations, state explicitly: "No specific industry regulations identified in `[[DOMAIN_FILE]]`; the section is omitted."

### 2.8 DoD Hardening Test

After the Engineering DoD and Operational DoD scoring, apply the Hardening DoD test from `../manifesto-done.md`:

1. **Bundle integrity attestation** — does the framework produce or require a cryptographic hash or digital signature of the assembled evidence bundle? Verdict: Pass / Partial / Fail.
2. **Agentic provenance record** — does the framework record the foundation model identifier and version, provider category, evaluation/production model parity, system-instruction hash, tool manifest, memory state version, retrieval corpus version, embedding model version, dataset lineage, policy constraints active? Verdict per item: Pass / Partial / Fail.
3. **Security static analysis results** — OWASP ASVS-calibrated, no unresolved Critical/High. Verdict: Pass / Partial / Fail.
4. **Evidence freshness rules** — does the framework define and enforce evidence freshness windows (e.g., evaluation results valid for N days)? Verdict: Pass / Partial / Fail.

Conclude this section with **exactly one** of the literal sentences:
- `Hardening is complete.` — if all four items are Pass.
- `Hardening is not complete.` — if any item is Partial or Fail.

No other concluding sentence is permitted.

### 2.9 Banned soft language

Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`, `use judgment`. Use declarative form.

### 2.10 Idempotence (preflight)

Before writing, Glob `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_03_gates_dods.md`. If the file exists AND has ≥ 20 lines AND contains the canonical Part 4 and Part 5 headings AND every gate / DoD condition score is filled in (no `<score>` placeholders), exit without writing. Otherwise rewrite from scratch.

---

## 3. Output structure

### 3.1 File path

```
[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_03_gates_dods.md
```

### 3.2 H1 heading — exact format

```
# [[FRAMEWORK]] Review 03 — ASDLC Gate Analysis & Definitions of Done
```

### 3.3 Required sections (in order)

```
# [[FRAMEWORK]] Review 03 — ASDLC Gate Analysis & Definitions of Done

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`
**Source artefacts read:** <enumerated list of every [[FRAMEWORK]] source file actually read>

---

## Part 4 — ASDLC Gate Analysis

### Gate Scores

| # | Gate | Score | One-sentence assessment |
|---|---|---|---|
| G1 | Specification Readiness Gate | <score> | <one sentence with evidence-for and evidence-against, grounded in [[FRAMEWORK]] artefacts> |
| G2 | Release Gate | <score> | <one sentence with evidence-for and evidence-against> |
| G3 | Operational Readiness Gate | <score> | <one sentence with evidence-for and evidence-against> |
| G4 | Retirement Gate | <score or `N/A`> | <one sentence with evidence-for and evidence-against, or an N/A justification per §2.1> |

### Per-Gate Detail

#### G1 — Specification Readiness Gate (<score>/100)

**What [[FRAMEWORK]] does.** <One paragraph naming the gate-equivalent mechanism in [[FRAMEWORK]], with verbatim quotes from the framework's source files (path in backticks).>

**What ASDLC requires.** <One paragraph quoting the canonical conditions verbatim from `specification-readiness.md`.>

**The gap.** <One paragraph stating which of the 9 SR Gate conditions are unmet or partially met, naming each by number, with `[[ORGANIZATION]]`-specific regulatory exposure cited by article number.>

#### G2 — Release Gate (<score>/100)

<Same three labelled paragraphs as G1, citing `release-governance.md` for ASDLC requirements.>

#### G3 — Operational Readiness Gate (<score>/100)

<Same three labelled paragraphs as G1, citing `operations/dod.md` for ASDLC requirements.>

#### G4 — Retirement Gate (<score>/100 or `N/A`)

<Same three labelled paragraphs as G1, citing `retirement-gate.md` and `governance/gate-registry.yaml` for ASDLC requirements. The Retirement Gate is the lifecycle's fourth gate (8 conditions per `retirement-gate.md` and `governance/gate-registry.yaml`); enumerating those conditions is `prompt-02-gate.md` GATE_NUMBER=4's job — this section MUST cross-reference G4 so the cross-gate synthesis reflects the four-gate architecture. When G4 is N/A per §2.1, state the N/A justification in the "What [[FRAMEWORK]] does." paragraph and use the remaining paragraphs to record the absence as a finding rather than a score.>

### Cross-Gate Failure Modes

<Section heading exactly as shown. Below it, at least 5 bullets in the format `- **G{X}→G{Y}:** ...`, each citing at least two [[FRAMEWORK]] artefacts in backticks and at least one regulation by article. See §2.4.>

### Cross-Layer Feedback Closure

<Section heading exactly as shown. Below it, four bullets — one per ASDLC feedback path (L4→L1, L4→L2, L3→L2, L2→L1) — each in the format `- **L{X}→L{Y}:** Verdict: {Closed | Partial | Open}. {explanation citing [[FRAMEWORK]] evidence, including a verdict on the unified closure schema (process change + evaluation/validation/criterion update + re-run) and, if Partial or Open, the explicit missing path-component combination}`. Conclude with one sentence stating that the L4→IGM feedback path is out of ASDLC review scope. See §2.5.>

### Human Escalation Architecture

<Section heading exactly as shown. Below it, four labelled sub-paragraphs in the order Escalation triggers / Escalation path / Response time / Fitness for [[ORGANIZATION]] context. See §2.6.>

---

## Part 5 — ASDLC Definitions of Done

### Engineering DoD (Layer 2 — inherited from AEM)

| Condition | Score | Evidence For | Evidence Against |
|---|---|---|---|
| Shipped | <score> | <[[FRAMEWORK]] artefact + verbatim quote with path> | <verbatim quote from `../manifesto-done.md` + named gap> |
| Observable | <score> | … | … |
| Verified | <score> | … | … |
| Provable | <score> | … | … |
| Learned from | <score> | … | … |
| Governed | <score> | … | … |
| Economical | <score> | … | … |

### Operational DoD (Layer 4 — ASDLC-specific)

| Condition | Score | Evidence For | Evidence Against |
|---|---|---|---|
| Runbook complete and current | <score> | <[[FRAMEWORK]] artefact + verbatim quote with path> | <verbatim quote from `operations/dod.md` + named gap> |
| SLOs defined and monitoring configured | <score> | … | … |
| On-call assigned and briefed | <score> | … | … |
| System steward assigned | <score> | … | … |
| Security scan clean | <score> | … | … |
| License compliance confirmed | <score> | … | … |
| Trace retention policy set and configured | <score> | … | … |
| DR/Failover Tested *(conditional; blocking only at blast-radius tier 3)* | <score or `N/A`> | … | … |

### DoD Hardening Test

<Section heading exactly as shown. Below it, four bullets covering Bundle integrity attestation / Agentic provenance record / Security static analysis results / Evidence freshness rules — each with a Pass / Partial / Fail verdict. Section concludes with exactly one of: `Hardening is complete.` or `Hardening is not complete.` See §2.8.>

### Industry-Specific DoD Requirements

<Section heading exactly as shown. Required when `[[DOMAIN_FILE]]` specifies a regulated industry; otherwise the section explicitly states the omission. See §2.7.>

---
```

---

## 4. Hard rules

These rules apply without exception. They mirror the hard rules in `prompt.md`.

- **Score consistency invariant.** Part 4 per-gate scores and Part 5 per-condition scores MUST equal the corresponding rows in agent 01's Part 1 tables. Agent 03 is the authoritative source for Gate and DoD scores. Agent 01 reads these files to populate Part 1. Agent 09 (merge) detects mismatches.
- **Dates in YYYY-MM-DD format** everywhere a date appears.
- **Cross-references use canonical part numbers** (e.g., "see Part 3", "see Part 12"). Do not use file names or agent numbers in cross-references within the output content.
- **No references to out-of-scope corpora or untracked files.** Every source file cited MUST be tracked by git on the current branch. Do not read or cite `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.{md,html}`, `agentic-governance-stack.{md,html}`, `manifesto-evolution-plan.{md,html}`, `phase-assessment-checklist.{md,html}`, `aplc-plan*`, or `igm-aent-coherence-review*` anywhere in the output. The output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`.
- **No forward-propagation from `[[DOMAIN_FILE]]` into framework claims.** Use `[[DOMAIN_FILE]]` only to establish regulatory obligations. Never assert that `[[FRAMEWORK]]` implements behaviour by extrapolating from `[[DOMAIN_FILE]]`.
- **Banned soft language.** The output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, or `use judgement`. Make claims with evidence or do not make them.
- **Severity labels must use the canonical thresholds** defined in `prompt.md`.
- **Engineering DoD requires AEM source.** If `../manifesto-done.md` is unreachable, abort. Do not fabricate AEM DoD definitions.

---

## 5. Self-Check Before Writing

**Do not save the output file until every item below is confirmed.**

- [ ] All 4 ASDLC gates (G1, G2, G3, G4) are named explicitly and scored with an explicit whole-integer numeric score, or G4 is marked `N/A` with a stated justification per §2.1.
- [ ] All 7 AEM Engineering DoD conditions are scored with an explicit whole-integer numeric score.
- [ ] All 8 ASDLC Operational DoD conditions (7 unconditional + 1 conditional DR/Failover Tested) are scored with an explicit whole-integer numeric score, or DR/Failover Tested is marked `N/A` with the blast-radius-tier justification per `governance/gate-registry.yaml`.
- [ ] Each gate subsection contains exactly the three labelled paragraphs `**What [[FRAMEWORK]] does.**`, `**What ASDLC requires.**`, `**The gap.**`, in this order, with no bullets.
- [ ] Each gate subsection contains at least one verbatim quote from a `[[FRAMEWORK]]` source file with its path.
- [ ] Each gate subsection contains at least one verbatim quote from the gate's authoritative source (`specification-readiness.md`, `release-governance.md`, `operations/dod.md`, or `retirement-gate.md`) with its path; condition counts cited match `governance/gate-registry.yaml` verbatim.
- [ ] Each gate subsection cites a regulation by article or section number from `[[DOMAIN_FILE]]`.
- [ ] Cross-Gate Failure Modes section contains at least 5 items, each in the mandated format `- **G{X}→G{Y}:** ...`, each citing at least two `[[FRAMEWORK]]` artefacts and at least one regulation by article; the four-gate architecture is reflected (G4 included as origin or destination of at least one failure mode unless G4 is N/A and the absence is itself surfaced as a failure mode).
- [ ] Cross-Layer Feedback Closure section contains exactly four feedback-path bullets (L4→L1, L4→L2, L3→L2, L2→L1) each with a Closed / Partial / Open verdict AND a verdict on the unified closure schema (process change + evaluation/validation/criterion update + re-run); for any Partial or Open verdict the missing path-component combination is named explicitly. Section concludes with one sentence stating that L4→IGM is out of ASDLC review scope.
- [ ] Human Escalation Architecture section contains all four labelled sub-paragraphs (Escalation triggers, Escalation path, Response time, Fitness for `[[ORGANIZATION]]` context) with at least four named regulatory obligations in the Fitness paragraph, and covers all four gates (or notes G4 N/A).
- [ ] Engineering DoD Table has exactly 4 columns (Condition | Score | Evidence For | Evidence Against) and 7 rows in canonical order.
- [ ] Operational DoD Table has exactly 4 columns (Condition | Score | Evidence For | Evidence Against) and 8 rows in canonical order (7 unconditional + 1 conditional DR/Failover Tested).
- [ ] Each condition narrative contains at least one verbatim quote from a `[[FRAMEWORK]]` source file with its path AND at least one verbatim quote from the appropriate authoritative source (`../manifesto-done.md` for Engineering DoD; `operations/dod.md` for Operational DoD) with its path.
- [ ] DoD Hardening Test names all four hardening items (bundle integrity attestation; agentic provenance record; security static analysis; evidence freshness) and assigns Pass / Partial / Fail to each, ending with exactly one of the literal phrases `Hardening is complete.` or `Hardening is not complete.` and no other concluding sentence.
- [ ] Industry-Specific DoD Requirements section is present and references named articles/sections from `[[DOMAIN_FILE]]` (or explicitly states omission).
- [ ] Part 4 per-gate scores and Part 5 per-condition scores match (or this file is treated as authoritative and agent 01 will reconcile).
- [ ] All dates are in YYYY-MM-DD format.
- [ ] No remaining `[[...]]` placeholders appear in the output.
- [ ] No out-of-scope-corpus references appear anywhere in the output (zero matches for `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, or `igm-aent-coherence-review`). Every cited source file is tracked by git on the current branch.
- [ ] No banned soft language (`consider`, `may`, `could potentially`, `perhaps`, `use judgement`) appears.
- [ ] Header metadata block uses exactly the labels `Framework`, `Client context`, `Regulatory overlay`, `Reviewer date`, `ASDLC`, `Source artefacts read` and lists every source artefact actually read.
- [ ] Every score states evidence for and evidence against separately.
- [ ] Canonical severity thresholds and weighting (referenced from `prompt.md`, not duplicated) are used consistently throughout.
