# Sub-prompt 01 — Overview

**Purpose:** Produce the overview file for a [[FRAMEWORK]] Agentic Software Delivery Lifecycle (ASDLC) alignment review, covering overall scores, scoring methodology, a framing-warning header, category-by-category score rationale, and client/industry-specific observations.

**Wave:** Wave 1a. This prompt runs in parallel with prompts 02-l1..l4, 02-g1..g3, 03, 04a, 04b, 05a, 07, and 08a. It cannot read their outputs. Use canonical Part numbers ("see Part 12") for any cross-reference whose target is produced by another agent — agent 09 (merge) will resolve cross-references at synthesis time.

**Note to orchestrator:** All `[[VARIABLE]]` placeholders in this file must be substituted before this prompt is passed to the agent. If any `[[...]]` pattern remains in your working copy, stop and resolve it before spawning.

---

## 1. Inputs — read all before scoring

Read the following files in full before producing any scores. Do not score from memory. Do not proceed if any file is inaccessible.

### [[FRAMEWORK]] source artefacts

Read every source file in the `[[FRAMEWORK_LOWER]]/` directory (or wherever `[[FRAMEWORK]]`'s source lives — the framework's own root) end-to-end. At a minimum this includes:

- The primary README (or equivalent top-level documentation file).
- All core module source files, configuration schemas, and lifecycle rule files.
- Any CHANGELOG, version history, or release notes available.
- Any internal rules, patterns, or architectural decision records included with the framework.

Score only against artefacts and capabilities present at `[[FRAMEWORK_VERSION]]`. Unmerged or unreleased work (epics in progress, ADRs in `Proposed` rather than `Accepted` state, features behind disabled feature flags, design documents not yet implemented) MUST be noted as "planned / unreleased" in the score rationale, not counted toward the score.

### ASDLC corpus

Read each of the following files end-to-end. These constitute the ASDLC corpus that this review scores against:

**Core (mandatory — abort if missing):**
- `asdlc.md` — four-layer model, gate definitions, feedback paths, ASDLC values, ASDLC-vs-APLC distinction, governance-of-governance, Tier 4 mechanics.
- `asdlc-guide.md` — recommended adoption sequence, common failure modes, integration guidance, phase-calibrated requirements.
- `README.md` — top-level entry points, gate descriptions, adoption path.

**Layer authoritative artefacts (read each end-to-end):**
- `governance/gate-registry.yaml` — **machine-readable canonical source of truth** for every ASDLC gate's condition count and condition titles. The companion `governance/gate-registry.md` is a human-readable derived view; the YAML governs. The Gates Summary Table in this overview MUST source its condition counts from the YAML registry. Any divergence between the registry and the prose sources below is surfaced in agent 03 (Part 4 / Part 5) as an integrity finding; this overview's one-sentence gate assessments cite the registry's count.
- `demand/value.md` — L1 demand validation, value definition, demand-to-specification bridge.
- `demand/intelligence.md` — Layer 0 pre-demand intelligence.
- `demand/metrics.md` — L1 metrics for value delivery, specification quality, demand health.
- `specification-readiness.md` — authoritative prose source for SR Gate (G1) conditions.
- `release-governance.md` — authoritative prose source for Release Gate (G2) and the release-approval chain.
- `deployment-governance.md` — environment promotion, feature flag governance, rollback operationalisation.
- `operations/governance.md` — L4 operational lifecycle, SLO/SLA governance, incident management.
- `operations/dod.md` — authoritative prose source for Operational Readiness Gate (G3) and the Operational DoD.
- `maintenance-governance.md` — stewardship transfer, security patching, technical debt, decommissioning.

**Cross-cutting governance (read each end-to-end):**
- `governance/agents.md` — governance agent framework, autonomy tier definitions, epistemic tier labelling.
- `governance/graph.md` — semantic governance graph: node types, edge types, GateState model.
- `governance/queries.md` — canonical governance questions and authoritative data sources.
- `agent-control-plane.md` — named governance agents and schemas.
- `waiver-governance.md` — waiver lifecycle, debt tracking, portfolio-level waiver oversight.
- `finops-governance.md` — FinOps and inference cost governance.
- `security-governance.md` — security lifecycle and NIST SSDF mapping.
- `devsecops-controls.md` — DevSecOps pipeline by autonomy tier.

**AEM cross-reference (mandatory for Layer 2 scoring):**
- `../manifesto.md` — defines L2 inner loop. Resolve via `AGENTIC_MANIFESTO_PATH` or monorepo-adjacent `../`.
- `../manifesto-principles.md` — twelve AEM principles governing L2.
- `../manifesto-done.md` — Engineering DoD that L2 produces.

If `asdlc.md`, `asdlc-guide.md`, `specification-readiness.md`, `release-governance.md`, `operations/dod.md`, or `governance/agents.md` cannot be read, abort and report the missing file. Do not proceed with scoring.

### Domain file

- `[[DOMAIN_FILE]]` — read end-to-end. Map every major finding to a specific regulation or risk type identified in this file.

### Prior reviews (peer comparison)

If `[[PRIOR_REVIEWS]]` is not `none`, treat the comma-separated paths it contains as required reading. Read each listed file end-to-end before scoring. Do not transfer scores from prior reviews — derive scores independently from `[[FRAMEWORK]]`'s artefacts. When `[[PRIOR_REVIEWS]]` is not `none`, the output MUST include a "Peer Comparison" subsection within the Industry/Client Observations section that names each prior review and states (a) one capability `[[FRAMEWORK]]` covers more strongly than the peer and (b) one capability `[[FRAMEWORK]]` covers less strongly. When `[[PRIOR_REVIEWS]]` is `none`, omit the Peer Comparison subsection entirely.

---

## 2. Methodology

### 2.1 Category scores

Score each of the twelve ASDLC weighting categories 0–100. Use the canonical 12-category weighting scheme defined in `prompt.md` (§ Score weighting scheme). Do not invent or copy alternative values. If this prompt and `prompt.md` ever disagree, `prompt.md` wins.

Use the SHORT-FORM category names from the `prompt.md` weighting table. These are canonical for this review system. The short forms are:

- L1 — Layer 1 — Demand & Value
- G1 — Specification Readiness Gate
- L2 — Layer 2 — Engineering Execution
- G2 — Release Gate
- L3 — Layer 3 — Release & Deployment beyond the gate
- G3 — Operational Readiness Gate
- L4 — Layer 4 — Operations & Maintenance
- G4 — Retirement Gate
- T4 — Tier 4 Policy Envelope & Epistemic-Tier Constraints
- CG — Cross-cutting Governance
- FS — FinOps, Security & DevSecOps
- FB — Feedback Paths Closure

For each category score, state:

1. The score (0–100, integer).
2. **Evidence for** — specific artefact names, module names, rule text, or file sections that support a higher score.
3. **Evidence against** — specific artefact names, absences, or limitations that support a lower score.

Do not conflate evidence-for and evidence-against. State them separately.

Every claim about `[[FRAMEWORK]]` MUST be grounded in a verbatim quote from a named source file, including the file path. Paraphrase without citation is forbidden. Each category's evidence-for must include at least one verbatim quote (in single backticks or double quotes, ≤30 words) from a `[[FRAMEWORK]]` artefact, with the file path in parentheses (e.g., `"delegates AI operations to Claude Code CLI"` (`README.md`)). Each category's evidence-against must include at least one specific named absence (artefact name, function name, or rule that does not exist in `[[FRAMEWORK]]` but ASDLC requires).

**Cross-prompt score authority:** The per-category scores entered in the ASDLC Categories Table in this review are the AUTHORITATIVE scores for this review run. Agents 02-l1..l4 will produce Layer scores; agents 02-g1..g3 will produce Gate scores; agent 03 will provide DoD scores. Agent 01 reconciles by using its own scores in Part 1; agent 09 (merge) detects mismatches across files. Do NOT independently re-derive scores from other agents' outputs (you cannot read them — they run in parallel).

### 2.2 Overall score

Compute `Σ(category_score × decimal_weight)` where each `category_score` is expressed as a decimal between 0 and 1 (e.g., score 52 → 0.52) and each `decimal_weight` is the integer percent weight from `prompt.md` (e.g., L1 weight 12% → 12). The product is the weighted contribution to one decimal place. Sum the twelve weighted contributions; round the total to one decimal place.

Show the calculation inline in a footnote under the ASDLC Categories Table using the format `{category} {score_decimal}×{weight_int}={weighted}` (worked example: `L1 0.52×12=6.24`). The "Overall Score" in the document header MUST equal the Total row of the categories table to one decimal place. If after rounding individual category scores to integers the header value differs from the table-arithmetic sum by ≥ 0.1, correct the header value before saving so they agree.

### 2.3 Severity mapping

Map every category score and the overall score to a severity label using the canonical severity thresholds defined in `prompt.md` (§ Severity thresholds). Do not use different thresholds. The Gates Table and the DoD Tables do NOT include a Severity column — only the ASDLC Categories Table does.

### 2.4 ASDLC Gates summary scores

Score each gate 0–100 (integer) and provide a single-sentence assessment (≤ 50 words; semicolon-joined two-clause sentences count as a single sentence):

- G1 — Specification Readiness Gate
- G2 — Release Gate
- G3 — Operational Readiness Gate
- G4 — Retirement Gate

For each gate, the one-sentence assessment must contain BOTH an evidence-for clause (a specific [[FRAMEWORK]] artefact that supports the score) AND an evidence-against clause (the specific gap or limitation against the gate's canonical pass conditions). The deep gate analysis is owned by Part 4 (agent 03). The summary in this overview is a high-level signal that must align with Part 4.

### 2.5 ASDLC Definition-of-Done summary scores

Two DoDs apply in ASDLC: the Engineering DoD (Layer 2, inherited from AEM) and the Operational DoD (Layer 4, ASDLC-specific). Score each condition 0–100 (integer) and provide a single-sentence assessment (≤ 50 words):

**Engineering DoD (7 conditions, from `../manifesto-done.md`):** Shipped, Observable, Verified, Provable, Learned from, Governed, Economical.

**Operational DoD (7 conditions, from `operations/dod.md`):** Runbook complete, SLOs defined, On-call assigned and briefed, System steward assigned, Security scan clean, License compliance confirmed, Trace retention policy set.

For each condition, the one-sentence assessment must contain BOTH an evidence-for clause (a specific [[FRAMEWORK]] artefact) AND an evidence-against clause (the specific gap against the DoD definition).

### 2.6 Layer Readiness Verdict

State `[[FRAMEWORK]]`'s Layer Readiness in the form: **Layer N operating, Gate G{M} routinely passing**, where N is the highest ASDLC layer the framework currently operates, and G{M} is the lowest gate the framework can routinely pass. The verdict is bounded by the LOWEST unmet gate, not by the highest demonstrated capability.

Specify:

- Which layers the framework operates and by which artefacts.
- Which gates the framework's evidence supports passing.
- Which gate is the LOWEST unmet gate (named explicitly), and what specific artefact, mechanism, or process would close the gap.
- Where [[ORGANIZATION]]'s context (industry hard caps, regulatory environment) affects the operational significance of the verdict.

The deep readiness analysis is owned by Part 8 (agent 05a). The verdict in this overview is a high-level summary that must align with Part 8.

---

## 3. Output specification

Write the following file exactly:

**File path:** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_01_quick_overview.md`

Create the `[[FRAMEWORK_LOWER]]/` directory if it does not exist.

When `[[INDUSTRY]]` is a long sentence (e.g., "European insurance and financial services — SR 11-7, DORA, EU AI Act, GDPR, Solvency II"), abbreviate it to a short form (e.g., "European Insurance" or "Insurance Domain") for any section heading. Use the full form in the metadata `Context:` line and in the opening sentence of the Industry/Client Observations section.

### 3.1 Required structure

Produce all sections below in this exact order, using these exact headings.

---

```
# [[FRAMEWORK]] — ASDLC Alignment Review

**Framework:** [[FRAMEWORK]] — <one-line description of what [[FRAMEWORK]] is, extracted from [[FRAMEWORK]]'s own README or top-level documentation>
**Version reviewed:** [[FRAMEWORK_VERSION]]
**Review date:** <YYYY-MM-DD; the date the agent was invoked>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`
**Reviewer methodology:** Agentic Software Delivery Lifecycle — 4 Layers (L1 Demand & Value; L2 Engineering Execution; L3 Release & Deployment; L4 Operations & Maintenance), 4 Gates (Specification Readiness; Release; Operational Readiness; Retirement), Engineering DoD (inherited from AEM), Operational DoD, Tier 4 Policy Envelope mechanics, cross-cutting governance (graph, agents, queries, control plane, waivers, epistemic tiers), FinOps + Security + DevSecOps, feedback paths, and [[INDUSTRY]] domain guidance
**Context:** [[ORGANIZATION]] — [[INDUSTRY]]
**Overall Score:** <X.X>/100
**Layer Readiness:** <Layer N operating, Gate G{M} routinely passing, with any proto-elements at higher layers/gates noted>. <One sentence stating the lowest unmet gate.>

---

## Framing Warning

### What [[FRAMEWORK]] is

<Two to four sentences. State what [[FRAMEWORK]] is, who uses it, its primary inputs and outputs, and its stated scope boundary. Quote from [[FRAMEWORK]]'s own documentation where possible.>

### What ASDLC dimensions [[FRAMEWORK]] covers by design

<Two to four sentences. State which ASDLC layers, gates, or cross-cutting concerns [[FRAMEWORK]] directly addresses, citing specific modules, commands, or artefact types. Be specific — name the artefacts.>

### What is out of scope by design (scope gap vs. failure)

<Two to four sentences. State which ASDLC dimensions are explicit scope gaps, not failures. Explain the difference between a scope gap and a failure for this framework. Reference [[FRAMEWORK]]'s own scope statements where they exist.>

### Score interpretation warning

<Three to five sentences. Warn the reader that scores measure ASDLC alignment, not fitness for purpose. Distinguish scope-gap (note the gap, do not penalise in the score) from capability-failure (score low). State the boundary explicitly: a dimension that is documented as out-of-scope is reported in the "What is out of scope by design" subsection and does not lower the score; a dimension where the framework attempts the capability but falls short of ASDLC's bar is a capability-failure and DOES lower the score. Note that low scores on out-of-scope dimensions reflect genuine alignment gaps a deployer must close through composition — not that [[FRAMEWORK]] is broken. State that [[ORGANIZATION]] must make a separate judgment about whether [[FRAMEWORK]] closes governance gaps that existing tooling leaves open. Note any dimensions where [[ORGANIZATION]]'s regulatory context (from [[DOMAIN_FILE]]) makes certain gaps more or less operationally significant.>

---

## Part 1 — Overall Scores

### ASDLC Categories Table

| # | Category | Weight | Score | Weighted | Severity |
|---|---|---|---|---|---|
| L1 | Layer 1 — Demand & Value | 12% | <score> | <weighted> | <severity> |
| G1 | Specification Readiness Gate | 10% | <score> | <weighted> | <severity> |
| L2 | Layer 2 — Engineering Execution | 18% | <score> | <weighted> | <severity> |
| G2 | Release Gate | 12% | <score> | <weighted> | <severity> |
| L3 | Layer 3 — Release & Deployment beyond the gate | 6% | <score> | <weighted> | <severity> |
| G3 | Operational Readiness Gate | 10% | <score> | <weighted> | <severity> |
| L4 | Layer 4 — Operations & Maintenance | 8% | <score> | <weighted> | <severity> |
| G4 | Retirement Gate | 4% | <score> | <weighted> | <severity> |
| T4 | Tier 4 Policy Envelope & Epistemic-Tier Constraints | 6% | <score> | <weighted> | <severity> |
| CG | Cross-cutting Governance (graph, agents, queries, control plane, waivers) | 4% | <score> | <weighted> | <severity> |
| FS | FinOps, Security & DevSecOps | 6% | <score> | <weighted> | <severity> |
| FB | Feedback Paths Closure | 4% | <score> | <weighted> | <severity> |
| **Total** | | **100%** | | **<sum>** | **<overall severity>** |

> **Weighted calculation:**
> L1 0.<score>×12=<weighted>; G1 0.<score>×10=<weighted>; L2 0.<score>×18=<weighted>; G2 0.<score>×12=<weighted>; L3 0.<score>×6=<weighted>;
> G3 0.<score>×10=<weighted>; L4 0.<score>×8=<weighted>; G4 0.<score>×4=<weighted>; T4 0.<score>×6=<weighted>; CG 0.<score>×4=<weighted>;
> FS 0.<score>×6=<weighted>; FB 0.<score>×4=<weighted> → **sum = <total>**

The Score column on the Total row is left blank. The Severity column on the Total row reflects the overall severity of `<sum>` per the canonical thresholds.

---

### ASDLC Gates Summary Table

| Gate | Score | One-sentence assessment |
|---|---|---|
| G1 — Specification Readiness Gate | <score> | <one sentence with evidence-for clause and evidence-against clause, grounded in [[FRAMEWORK]] artefacts> |
| G2 — Release Gate | <score> | <one sentence with evidence-for and evidence-against> |
| G3 — Operational Readiness Gate | <score> | <one sentence with evidence-for and evidence-against> |
| G4 — Retirement Gate | <score> | <one sentence with evidence-for and evidence-against> |

---

### Engineering DoD Summary Table (Layer 2, inherited from AEM)

| Condition | Score | One-sentence assessment |
|---|---|---|
| Shipped | <score> | <one sentence with evidence-for and evidence-against, grounded in [[FRAMEWORK]] artefacts> |
| Observable | <score> | <one sentence with evidence-for and evidence-against> |
| Verified | <score> | <one sentence with evidence-for and evidence-against> |
| Provable | <score> | <one sentence with evidence-for and evidence-against> |
| Learned from | <score> | <one sentence with evidence-for and evidence-against> |
| Governed | <score> | <one sentence with evidence-for and evidence-against> |
| Economical | <score> | <one sentence with evidence-for and evidence-against> |

---

### Operational DoD Summary Table (Layer 4, ASDLC-specific)

| Condition | Score | One-sentence assessment |
|---|---|---|
| Runbook complete and current | <score> | <one sentence with evidence-for and evidence-against, grounded in [[FRAMEWORK]] artefacts> |
| SLOs defined and monitoring configured | <score> | <one sentence with evidence-for and evidence-against> |
| On-call assigned and briefed | <score> | <one sentence with evidence-for and evidence-against> |
| System steward assigned | <score> | <one sentence with evidence-for and evidence-against> |
| Security scan clean | <score> | <one sentence with evidence-for and evidence-against> |
| License compliance confirmed | <score> | <one sentence with evidence-for and evidence-against> |
| Trace retention policy set and configured | <score> | <one sentence with evidence-for and evidence-against> |

---

### Layer Readiness Verdict

[[FRAMEWORK]] reaches **Layer <N> operating, Gate G{M} routinely passing** in the ASDLC model. The verdict is bounded by the lowest unmet gate, named in the next paragraph.

<Paragraph A: state which Layer requirements are met and cite the specific [[FRAMEWORK]] artefacts that satisfy them. List proto-elements of higher layers if present, but do not raise the verdict.>

<Paragraph B: state the lowest unmet gate by name first. For each unmet pass condition, name the specific artefact, mechanism, or process that would close the gap.>

<Paragraph C: state the relevance to [[ORGANIZATION]] specifically: how do the industry hard autonomy caps from `[[DOMAIN_FILE]]` interact with [[FRAMEWORK]]'s readiness verdict? Which gaps are most operationally critical for [[ORGANIZATION]]'s regulatory context? Which gaps are less critical because the relevant autonomy tiers are already capped?>

---

## Part 2 — Scoring Methodology

<Two to three paragraphs describing the scoring approach: which [[FRAMEWORK]] artefacts were read (enumerate them with file paths in a bullet list or comma-separated list — the reader must be able to verify that the listed artefacts cover the framework's stated scope), how scope gaps were handled (evidence of documented delegation treated as scope boundary, not failure), how the weighted scheme was applied across the 11 categories, and how the layer-and-gate readiness model was applied. Reference the ASDLC sources used. State the review date. State `[[FRAMEWORK_VERSION]]` and confirm whether the framework's actual version was verified (e.g., by reading CHANGELOG or git HEAD).>

---

## Category-by-Category Score Rationale

### L1 — Layer 1 — Demand & Value (<score>/100 — <severity>)

<One paragraph, 80–120 words. State: (a) what [[FRAMEWORK]] does that supports L1 — name specific artefacts and include at least one verbatim quote with file path; (b) what is absent or insufficient — name the specific gaps against L1's responsibilities (validated demand, measurable value, loop-readiness preparation, demand intelligence) per `demand/value.md`, `demand/intelligence.md`, `demand/metrics.md`, `specification-readiness.md`; (c) any [[ORGANIZATION]]-relevant implication from `[[DOMAIN_FILE]]`.>

### G1 — Specification Readiness Gate (<score>/100 — <severity>)

<One paragraph, 80–120 words. Same structure: what [[FRAMEWORK]] does to enforce the SR Gate conditions (count and titles per `governance/gate-registry.yaml`), what is missing per `specification-readiness.md`, [[ORGANIZATION]] implication.>

### L2 — Layer 2 — Engineering Execution (<score>/100 — <severity>)

<One paragraph, 80–120 words. ASDLC defers L2 to AEM. Score [[FRAMEWORK]]'s coverage of the AEM nine-phase loop and twelve principles per `../manifesto.md`, `../manifesto-principles.md`. Where the framework supports Tier 4, note Tier 4 envelope coverage briefly here (deep assessment is in T4 below).>

### G2 — Release Gate (<score>/100 — <severity>)

<One paragraph, 80–120 words. What [[FRAMEWORK]] does to enforce the Release Gate conditions (count and titles per `governance/gate-registry.yaml`), what is missing per `release-governance.md`, [[ORGANIZATION]] implication.>

### L3 — Layer 3 — Release & Deployment beyond the gate (<score>/100 — <severity>)

<One paragraph, 80–120 words. Beyond the gate itself: environment promotion (`deployment-governance.md`), feature flag governance, emergency-change procedure.>

### G3 — Operational Readiness Gate (<score>/100 — <severity>)

<One paragraph, 80–120 words. What [[FRAMEWORK]] does to enforce the Operational Readiness Gate conditions (count and titles per `governance/gate-registry.yaml`), what is missing per `operations/dod.md`.>

### L4 — Layer 4 — Operations & Maintenance (<score>/100 — <severity>)

<One paragraph, 80–120 words. Operational observability, incident management, stewardship, dependency drift, retirement per `operations/governance.md`, `maintenance-governance.md`.>

### G4 — Retirement Gate (<score>/100 — <severity>)

<One paragraph, 80–120 words. What [[FRAMEWORK]] does to enforce the Retirement Gate conditions (count and titles per `governance/gate-registry.yaml`), what is missing per `maintenance-governance.md`, [[ORGANIZATION]] implication.>

### T4 — Tier 4 Policy Envelope & Epistemic-Tier Constraints (<score>/100 — <severity>)

<One paragraph, 80–120 words. Does [[FRAMEWORK]] support Tier 4 envelope-level operation? Assess the four envelope elements from `annex-igm.md` (Tier 4 intelligence-substrate constraints): epistemic-tier-to-action mapping, contradiction-handling rules per type, decay boundaries per claim class, feedback-loop closure rules. For frameworks operating with relocation mechanics, additionally assess against `annex-aentm.md` (Tier 4 relocation mechanics). Note relocation accountability per action class. Paraphrase any imported terms to ASDLC-equivalent vocabulary; do not emit the bare cross-stack tokens.>

### CG — Cross-cutting Governance (<score>/100 — <severity>)

<One paragraph, 80–120 words. Coverage of governance graph (`governance/graph.md`), governance agents (`governance/agents.md`, `agent-control-plane.md`), governance queries (`governance/queries.md`), waiver lifecycle (`waiver-governance.md`), epistemic tier labelling.>

### FS — FinOps, Security & DevSecOps (<score>/100 — <severity>)

<One paragraph, 80–120 words. Coverage per `finops-governance.md`, `security-governance.md`, `devsecops-controls.md`. Map to NIST SSDF, OWASP LLM Top 10, FinOps Foundation maturity if relevant to [[ORGANIZATION]].>

### FB — Feedback Paths Closure (<score>/100 — <severity>)

<One paragraph, 80–120 words. Coverage of the four ASDLC feedback paths (L4→L1, L4→L2, L3→L2, L2→L1) per `asdlc.md` § Feedback Paths. State whether each path defines a triggering signal class, destination governance authority, latency SLO, and closing condition. The L4→IGM feedback path is out of ASDLC review scope; do not score it.>

---

## [[ORGANIZATION]] / <INDUSTRY_SHORT> Specific Observations

<Three to five paragraphs. Each paragraph must map to a specific regulatory provision (article, paragraph, or rule number) from `[[DOMAIN_FILE]]` — not just the regulation's name. Generic references ("GDPR") are insufficient; specific references ("GDPR Article 25", "DORA Article 19", "Solvency II Article 41") are required. Cover: (1) which [[FRAMEWORK]] capabilities are most valuable for [[ORGANIZATION]]'s regulatory context; (2) which ASDLC gaps are most operationally critical given [[INDUSTRY]] hard autonomy caps; (3) which gaps are less critical because the relevant use cases are already capped at lower tiers by [[DOMAIN_FILE]]; (4) any specific regulatory requirement from [[DOMAIN_FILE]] that [[FRAMEWORK]] directly addresses or structurally cannot address.>

<If `[[PRIOR_REVIEWS]]` is not `none`, append a "### Peer Comparison" subsection naming each prior review and stating one capability [[FRAMEWORK]] covers more strongly than the peer and one capability it covers less strongly. Omit this subsection entirely when `[[PRIOR_REVIEWS]]` is `none`.>
```

---

## 4. Hard rules

These rules apply without exception. They mirror the hard rules in `prompt.md`.

1. Read [[FRAMEWORK]]'s source artefacts before scoring. Every claim about `[[FRAMEWORK]]` MUST be grounded in a verbatim quote from a named source file, including the file path. Paraphrase without citation is forbidden.
2. Read ASDLC's source artefacts before scoring. Do not score from memory of ASDLC — read the current files listed in Section 1.
3. For every score, state evidence-for and evidence-against separately. Do not merge them.
4. Do not praise [[FRAMEWORK]] for things it does not demonstrably do. Distinguish "claimed capability" (documented in README, design docs, ADRs in `Proposed` state, rules files, or roadmap) from "demonstrated capability" (implemented in deployed/HEAD source code at `[[FRAMEWORK_VERSION]]`). Score against demonstrated capability only; note material claims under evidence-against.
5. Score every category against ASDLC's full bar — even if [[FRAMEWORK]] documents the area as out of scope. A documented scope boundary is reported in the Framing Warning subsection "What is out of scope by design (scope gap vs. failure)". A score below 100 reflects a gap a deployer must close through composition; it is not a moral failing of the framework. Do not penalise [[FRAMEWORK]] for problems explicitly outside its stated scope beyond the alignment gap that the scope boundary creates.
6. Every major finding must map to a specific regulatory provision (article, paragraph, or rule number) from `[[DOMAIN_FILE]]` as it applies to [[ORGANIZATION]]. Generic regulation names are insufficient.
7. Use date format YYYY-MM-DD wherever a date appears. The `Review date` line is the date the agent was invoked.
8. When cross-referencing another part of the review within the output file, use canonical part numbers (e.g., "see Part 12"). Do not use file names or agent numbers in cross-references.
9. **Out-of-scope corpus / tracked-files-only.** This review covers the Agentic Software Delivery Lifecycle (ASDLC). Do not read, cite, or reference any file untracked by git on the current branch. Specifically the following are out of scope: `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.md`, `agentic-enterprise.html`, `agentic-governance-stack.md`, `agentic-governance-stack.html`, `manifesto-evolution-plan.md`, `manifesto-evolution-plan.html`, `phase-assessment-checklist.md`, `phase-assessment-checklist.html`, `aplc-plan.md`, `aplc-plan.html`, `igm-aent-coherence-review.md`, and `igm-aent-coherence-review.html`. The output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`. Do not forward-propagate out-of-scope references from `[[DOMAIN_FILE]]` or from cross-stack files — paraphrase to ASDLC-equivalent terms. **Exception:** the ASDLC-tracked annexes `annex-aentm.md` and `annex-igm.md` are part of ASDLC and MUST be read when assessing Tier 4. Cite them by filename only; paraphrase any imported cross-stack terminology to ASDLC-equivalent vocabulary so the bare banned tokens never appear in the output prose.
10. The weighted calculation in the footnote must verify arithmetically. Check that `Σ(category_score × decimal_weight)` equals the stated total before saving, and that the header `Overall Score` equals the table sum to one decimal place.
11. The output MUST NOT contain any of the following soft-language tokens: "consider", "may", "could potentially", "it might be worth", "perhaps", "use judgement", "should ideally", "may want to", "appears to", "arguably", "seemingly". Use declarative statements. State what `[[FRAMEWORK]]` does or does not do at `[[FRAMEWORK_VERSION]]`. Do not state what `[[FRAMEWORK]]` will do, plans to do, or could do.
12. This is a regulator-credible technical review, not a vendor blog post. Do not use marketing language ("robust", "best-in-class", "industry-leading"). Do not soften findings. Do not try to please. Score the framework as it is at HEAD.
13. This agent does not produce a remediation roadmap (that is agent 06's responsibility). Do not invent S/M/L/XL effort labels — those belong to agent 06.

---

## 5. Self-check before saving

**Do not save the output file until every item below is confirmed satisfied.** Each item is a binary yes/no question. Answer yes to all before writing the file.

- [ ] Is the output file path `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_01_quick_overview.md` with `[[FRAMEWORK_LOWER]]` fully substituted (no literal `[[` remaining)?
- [ ] Have all `[[VARIABLE]]` placeholders in the output file content been substituted? (Scan the output for any remaining `[[...]]` patterns.)
- [ ] Have all template angle-bracket placeholders been replaced? (Scan for `<score>`, `<weighted>`, `<severity>`, `<one sentence...>`, `<one-line description...>`, `<YYYY-MM-DD>`, `<N>`, `<sum>`, `<total>`, `<INDUSTRY_SHORT>`, and the regex pattern `<[A-Za-z][^>]+>` more broadly.)
- [ ] Does the weighted total in the categories table Total row equal the footnote calculation arithmetically?
- [ ] Does the `Overall Score:` value in the file header metadata block equal the weighted total in the categories table footnote, rounded to one decimal place?
- [ ] Does the overall severity label in the categories-table Total row match the canonical severity threshold for the overall score (e.g., 50.6 → High because 40–54)?
- [ ] Does every severity label in every category row match the canonical thresholds defined in `prompt.md`?
- [ ] Does every category name in the ASDLC Categories Table and in the Category-by-Category Score Rationale headers use the SHORT-FORM names from the `prompt.md` weighting table (matching this prompt's Section 2.1 list verbatim)?
- [ ] Are all dates in the output file in YYYY-MM-DD format, and does the `Review date` equal the date the agent was invoked?
- [ ] Are there zero references to `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, or `igm-aent-coherence-review` anywhere in the output file? Are all source files referenced in the output tracked by git on the current branch?
- [ ] Have any soft-language tokens been removed? (Scan the output for: "consider", "may", "could potentially", "it might be worth", "perhaps", "use judgement", "should ideally", "may want to", "appears to", "arguably", "seemingly".)
- [ ] Does every category score paragraph contain both an evidence-for clause AND an evidence-against clause?
- [ ] Does every category score paragraph contain at least one verbatim quote (≤30 words, in backticks or double quotes) from a `[[FRAMEWORK]]` artefact with the file path stated?
- [ ] Does every Gate row's one-sentence assessment contain both an evidence-for clause AND an evidence-against clause?
- [ ] Does every DoD condition row's one-sentence assessment contain both an evidence-for clause AND an evidence-against clause?
- [ ] Does the ASDLC Gates Summary Table contain exactly four rows in the canonical order (G1, G2, G3, G4) and exactly three columns (Gate, Score, One-sentence assessment)?
- [ ] Does the Engineering DoD Summary Table contain exactly seven rows in the canonical order (Shipped, Observable, Verified, Provable, Learned from, Governed, Economical) and exactly three columns?
- [ ] Does the Operational DoD Summary Table contain exactly seven rows in the canonical order (Runbook, SLOs, On-call, Steward, Security, License, Trace retention) and exactly three columns?
- [ ] Does the Framing Warning section contain exactly four subsections in this order: "What [[FRAMEWORK]] is", "What ASDLC dimensions [[FRAMEWORK]] covers by design", "What is out of scope by design (scope gap vs. failure)", "Score interpretation warning"?
- [ ] Does the Layer Readiness header line name a specific Layer N AND a sentence stating the lowest unmet gate?
- [ ] Is the Layer Readiness Verdict bounded by the LOWEST unmet gate (not by the highest demonstrated feature), and does the body name that gate?
- [ ] Does the Layer Readiness Verdict name at least one specific [[FRAMEWORK]] artefact per met requirement and at least one specific gap per unmet gate condition?
- [ ] Does every major finding in the [[ORGANIZATION]] / Industry Specific Observations section cite a specific regulatory provision (article, paragraph, or rule number) from `[[DOMAIN_FILE]]`?
- [ ] If `[[PRIOR_REVIEWS]]` is not `none`, does the output include a "Peer Comparison" subsection that names each prior review and states one stronger capability and one weaker capability per peer?
- [ ] If `[[PRIOR_REVIEWS]]` is `none`, is the "Peer Comparison" subsection absent from the output?
- [ ] Do all cross-references within the output use canonical part numbers (e.g., "see Part 12") and not file names, agent numbers, or section headings?
- [ ] Is the Industry/Client Observations section heading abbreviated to a short form when `[[INDUSTRY]]` is a long sentence (e.g., "European Insurance" or "Insurance Domain"), with the full form preserved in the metadata `Context:` line?
- [ ] Is `[[FRAMEWORK_VERSION]]` in the `Version reviewed:` line either a tag, a commit SHA, a release name, `HEAD`, or `unknown` — and was the framework's actual version verified against this value?
- [ ] Has unmerged or unreleased work been noted as "planned / unreleased" in score rationales rather than counted toward scores?
