# Sub-prompt 06 — Strengths & Gap Analysis (Parts 10 + 11)

**Purpose.** Produce the Part 10 (Genuine Strengths) and Part 11 (Gap Analysis: Path to Next Unmet Gate / Next Unmet Layer) file for `[[FRAMEWORK]]`. This is a Wave 2 agent — runs after all Wave 1a and Wave 1b outputs are complete.

**Wave:** Wave 2. Reads all 17 Wave 1a + Wave 1b output files. Writes one output file.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_06_strengths_gaps.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`.

---

## 1. Inputs to read

### 1.1 Mandatory upstream files (abort if any missing or < 20 lines)

Read all 17 Wave 1a + Wave 1b output files. Treat each as authoritative for its domain — do NOT re-derive scores from `[[FRAMEWORK]]` source artefacts.

| Source agent | File | Authoritative for |
| --- | --- | --- |
| 01 | `_review_01_quick_overview.md` | Part 1 category scores; Part 2 methodology |
| 02-l1 … 02-l4 | `_review_02_layer_l1.md` … `_l4.md` | per-layer scores and gap detail |
| 02-g1 … 02-g3 | `_review_02_gate_g1.md` … `_g3.md` | per-gate scores and pass-condition coverage |
| 03 | `_review_03_gates_dods.md` | Part 4 gate scores; Part 5 DoD scores; cross-gate failure modes |
| 04c | `_review_04_adoption_governance.md` | Part 6 adoption + Part 7 governance + Cross-Document Synthesis |
| 05b | `_review_05_readiness_industry.md` | Part 8 readiness verdict + Part 9 industry assessment |
| 07 | `_review_07_guardrails_security.md` | Part 12 guardrails + Part 13 security |
| 08b | `_review_08_enterprise_guardrails.md` | Part 14 enterprise guardrail synthesis |

### 1.2 Reference (read for synthesis context only — do not re-derive scores)

- `asdlc.md` — for layer / gate / category framing.
- `governance/gate-registry.md` — single source of truth for gate condition counts and titles. When Part 11 names which conditions of the next unmet gate are missing, cite the registry's title verbatim.
- `[[DOMAIN_FILE]]` — for industry context.
- `governance/agents.md` — for autonomy tier ceilings.

### 1.3 Prior reviews
If `[[PRIOR_REVIEWS]]` is not `none`, peer comparison.

---

## 2. Methodology

### 2.1 Preflight

Glob all 17 upstream files. Verify each exists, has ≥ 20 lines, and contains its canonical Part heading. Verify no header-line placeholder leakage (no `[[...]]` patterns in any upstream file). If any file fails preflight, STOP and report — do not fabricate content.

### 2.2 Score Authority Table

Construct a Score Authority Table mapping each ASDLC weighting category to:
- The score reported by agent 01 (Part 1).
- The score reported by the dedicated agent for that category (e.g., L1 from agent 02-l1; G2 from agent 02-g2; Engineering DoD scores from agent 03; Operational DoD scores from agent 03).
- A divergence flag (`OK` / `DIVERGES`) if the two scores disagree by more than the rounding tolerance.

The 11 weighting categories are: L1, G1, L2, G2, L3, G3, L4, T4 (Tier 4 envelope), CG (Cross-cutting Governance), FS (FinOps + Security + DevSecOps), FB (Feedback Paths Closure).

Render as a markdown table with columns: `Category | Agent 01 score | Authoritative agent score | Divergence`.

The principle that **principle/category-file scores override overview scores for severity determinations** still holds: when computing gap severity, use the authoritative agent's score, not agent 01's.

### 2.3 Target identification

Extract the readiness verdict from agent 05b's Part 8: `**ASDLC Readiness: L{N} operating, G{M} routinely passing**`. From the verdict:

- `current_layer = N` (1, 2, 3, or 4).
- `current_gate = M` (`SR`, `Release`, `OpReady`, or `none`).

Compute targets:

- **`target_gate`** — the LOWEST unmet gate across the four-gate sequence G1 (SR) → G2 (Release) → G3 (Operational Readiness) → G4 (Retirement). Encode `current_gate` as an integer: `none` = 0, `SR` = 1, `Release` = 2, `OpReady` = 3, `Retirement` = 4. If `current_gate < 4`, target_gate = `G{current_gate + 1}`. If all four gates pass (`current_gate = 4`), target_gate = `none — the framework satisfies the full ASDLC gate sequence`. G4 (Retirement) is structurally newer than G1–G3 and many frameworks are silent on it; a framework with `current_gate = 3` that does not address retirement is at `target_gate = G4` and the gap is **structural-silence** rather than an active failure to pass — record this distinction in the gap entry (per `prompt-02-gate.md`'s G4 policy).
- **`target_layer`** — the next layer beyond `current_layer` that is not yet operating. If `current_layer < 4`, target_layer = `L{current_layer + 1}`. If `current_layer = 4`, target_layer = `none` (steady state).

The target is whichever of `target_gate` / `target_layer` represents the **lower bound** on advancement. Typically a framework progresses by closing the next unmet gate before extending into the next unmet layer — but where the layer extension blocks the gate (e.g., L1 demand layer needed before G1 SR Gate is meaningful), the layer extension is the target.

If both `target_gate` and `target_layer` are `none`, the framework is at steady state and Part 11 reframes around continuous improvement rather than gate progression.

### 2.4 Part 10 — Genuine Strengths

5–12 strengths, ordered by descending impact on closing the lowest unmet gate. Each strength MUST have:

```
### Strength {N} — {short title}

**ASDLC categories touched:** <comma-separated list, e.g., L2, G2, FS>

**Mechanism.** <1–2 paragraphs naming the [[FRAMEWORK]] mechanism (artefact, command, schema, rule). Cite verbatim from [[FRAMEWORK]] source files with backticked file paths AND verbatim from the Wave 1 source that identified the strength (Wave 1 anchor).>

**Why it is genuinely good.** <1 paragraph stating what manifesto-level / ASDLC-level requirement this satisfies, and what failure mode it prevents.>

**Evidence.** Wave 1 anchor: <Part X reference, e.g., "see Part 5, Engineering DoD condition 4 (Provable)">. Source anchor: <verbatim quote from [[FRAMEWORK]] source with file path>.

**Better than the alternative.** <1 paragraph stating what existing tooling does NOT do that [[FRAMEWORK]] does — name the alternatives.>

**Fairness note.** <1–2 sentences stating limits, partial implementation, conditions where the strength does not hold. Source from the same Wave 1 file's evidence-against section.>
```

Mark architectural strengths (`**architectural**` prefix in the title) where the strength is structural (the framework's design enables the capability) rather than configurational. Architectural strengths whose deployment gap is a `target_gate` or `target_layer` blocker MUST also appear as gaps in Part 11; cross-reference both sides by number.

**External authority freshness — required cross-check.** When a candidate strength concerns "external authority tracking" or analogous (the framework cites NIST, OWASP, DORA, EU AI Act, ISO 42001, or any other external normative source as part of its evidence base), the canonical pattern for verifying that the cited authority remains current is `freshness-register.yaml` (see `governance/freshness-register.yaml` in the ASDLC corpus). A framework that cites such authorities **without** a freshness register has a strength with **hidden-currency risk** — the citation is a snapshot, not a tracked dependency. Record this explicitly in the strength's Fairness note, AND surface a corresponding gap in Part 11 framed as "stale-control reliance / hidden-currency risk" against the freshness-register pattern.

### 2.5 Part 11 — Gap Analysis: Path to {target_gate / target_layer}

5–12 gaps, ordered by severity (descending), then by dependency (ascending — gaps with prerequisites listed AFTER their prerequisites), then by effort (ascending). Each gap MUST have:

```
### Gap {N} — {short title} *(Severity — <category>[, <category>])*

**Current state.** <1 paragraph naming what [[FRAMEWORK]] currently does (or fails to do) on this dimension. Cite Wave 1 anchor.>

**What is missing.** <1 paragraph stating what is absent. Quote ASDLC's actual requirement verbatim from the relevant authoritative artefact.>

**What {target_gate / target_layer} requires.** <1 paragraph stating what closing this gap looks like in terms of the target — which gate condition becomes routinely passable, or which layer becomes operational, when this gap is closed.>

**Why it matters for [[ORGANIZATION]] in [[INDUSTRY]].** <1 paragraph citing at least one regulatory article from `[[DOMAIN_FILE]]` and stating the operational consequence.>

**What closes it.** <3–6 numbered concrete actions. Each action names an artefact / command / process change.>

**Evidence anchor.** Wave 1 anchor: <Part X reference>. Source anchor: <verbatim quote from [[FRAMEWORK]] source or absence statement>.

**Effort.** <S / M / L / XL per `prompt.md` effort sizing>. <When non-engineering effort dominates (e.g., regulatory negotiation), annotate: "Effort dominated by <regulatory / organisational / training>".>
```

Severity is determined by the highest band among affected categories. **Severity is escalated one step** if the gap blocks `target_gate` or `target_layer`. (E.g., a Medium-band gap that blocks SR Gate progression becomes High.)

All Critical findings from the Wave 1 outputs (Part 12 / Part 13 in agent 07; any layer / gate scoring Critical) MUST appear as gaps unless explicitly justified out-of-scope. When a Critical Wave 1 finding is absent from Part 11, the Self-check fails.

Mark scope gaps with `(Scope gap — {regulation})` in the title. Scope gaps do not contribute to score deductions in Part 11 but do appear as gaps for `[[ORGANIZATION]]`'s composition planning.

### 2.6 Prioritised Remediation Roadmap

After the gap-by-gap detail, render a roadmap as a markdown table with columns:

```
| # | Gap title | Severity | Effort | Dependencies | Outcome (target gate / layer impact) |
```

Sort key (3-key): severity descending, dependency ascending, effort ascending. Row count equals gap count. Dependencies column contains only `None` or comma-separated `Gap {N}` references — no prose. No gap depends on itself directly or transitively; every dependency target precedes its dependent.

Below the roadmap, include a **Roadmap Interpretation** block with one paragraph per effort tier (S, M, L/XL combined) plus a closing adoption-ceiling paragraph. Each tier paragraph justifies sequencing by reference to regulatory exposure from `[[DOMAIN_FILE]]`.

### 2.7 Banned soft language and extended banned list

In addition to `prompt.md`'s core banned list, agent 06 MUST avoid (without an evidence anchor in the same paragraph): `robust`, `comprehensive`, `world-class`, `industry-leading`, `best-in-class`, `leverages`, `empowers`, `enables` (without naming what is enabled), `seamless`, `holistic`, `mature` (without phase number), `production-ready` (without naming what is production), `powerful` (without naming the power).

### 2.8 British English

"Prioritised", "organisation", "behaviour" — match the ASDLC corpus convention.

### 2.9 Idempotence

Glob output. If exists AND ≥ 20 lines AND contains Part 10 and Part 11 H2 headings AND Score Authority Table is present AND Roadmap is present, exit. Otherwise rewrite.

---

## 3. Output structure

```
# [[FRAMEWORK]] Review 06 — Strengths & Gap Analysis (Parts 10 + 11)

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`
**Sources read:** <enumerate all 17 Wave 1 source files plus the Wave 1 source-file footers actually consumed>

---

## Score Authority Table

| Category | Agent 01 score | Authoritative agent score | Divergence |
|---|---|---|---|
| L1 | <score> | <score from 02-l1> | <OK/DIVERGES> |
| G1 | <score> | <score from 02-g1> | <OK/DIVERGES> |
| L2 | <score> | <score from 02-l2> | <OK/DIVERGES> |
| G2 | <score> | <score from 02-g2> | <OK/DIVERGES> |
| L3 | <score> | <score from 02-l3> | <OK/DIVERGES> |
| G3 | <score> | <score from 02-g3> | <OK/DIVERGES> |
| L4 | <score> | <score from 02-l4> | <OK/DIVERGES> |
| T4 | <score> | <score from 05a> | <OK/DIVERGES> |
| CG | <score> | <score from 04b lifted by 04c> | <OK/DIVERGES> |
| FS | <score> | <score from 07> | <OK/DIVERGES> |
| FB | <score> | <score from 03> | <OK/DIVERGES> |

---

## Introduction

<2–4 paragraphs. State the readiness verdict from Part 8 (verbatim Verdict line); state the target (target_gate / target_layer); state the framing of Part 11 as a path from current readiness to that target; note any DIVERGES flags from the Score Authority Table and how they were reconciled (authoritative agent wins for severity computation).>

---

## Part 10 — Genuine Strengths

> **Self-referential-grading disclaimer.** The strengths and gaps below are scored against ASDLC's own assertions, not against externally-anchored regulatory or engineering source-of-truth. When this analysis flags a gap in the framework against an ASDLC condition, the operator must additionally verify that ASDLC's own claim against the underlying regulatory or engineering source is itself sound. This review system does not perform that outer verification. (See `review/prompt.md` lines 13–19 for the orchestrator-level statement of this disclaimer.)

<5–12 strength entries per §2.4 structure, ordered by descending impact on closing the lowest unmet gate. Where a strength concerns external authority tracking (NIST / OWASP / DORA / EU AI Act / ISO 42001 / analogous), the Fairness note MUST state whether the framework operates a freshness register (see `freshness-register.yaml`); absence of a freshness register is hidden-currency risk and the corresponding gap MUST appear in Part 11.>

---

## Part 11 — Gap Analysis: Path to <target_gate / target_layer>

> **Self-referential-grading disclaimer (reprise).** The gaps below are computed against ASDLC's own assertions. Operators must independently verify each ASDLC condition against the underlying regulatory or engineering source before treating any gap finding as authoritative.

<5–12 gap entries per §2.5 structure, ordered by severity desc, dependency asc, effort asc. Where the framework cites external normative authorities without a freshness register, include a gap framed as hidden-currency risk against the `freshness-register.yaml` pattern. Where `target_gate = G4` and the framework is silent on retirement, mark the gap as **structural-silence** (not active failure).>

---

## Prioritised Remediation Roadmap

| # | Gap title | Severity | Effort | Dependencies | Outcome (target gate / layer impact) |
|---|---|---|---|---|---|
<one row per gap>

### Roadmap Interpretation

<one paragraph per effort tier (S, M, L/XL combined), each justifying sequencing by reference to [[DOMAIN_FILE]] regulatory exposure. Closing paragraph states the adoption-ceiling implication.>

---
```

---

## 4. Hard rules

1. **Read all 17 Wave 1 outputs end-to-end before writing.** Treat each as authoritative for its domain.
2. **Do not re-derive scores from `[[FRAMEWORK]]` source artefacts.** Synthesis only.
3. **Score Authority Table is mandatory.** Compute divergence flags. Use the authoritative agent's score (not agent 01's) for severity computation.
4. **Target extraction.** Extract `target_gate` and `target_layer` from Part 8's Verdict line. If extraction fails (Verdict line missing or malformed), STOP and report.
5. **Severity escalation.** A gap that blocks `target_gate` or `target_layer` advancement gets one severity step escalation (Medium → High; High → Critical).
6. **Critical Wave 1 findings appear as gaps** unless explicitly justified out-of-scope.
7. **Gap titles tagged `(Scope gap — {regulation})`** when the gap is out of scope for `[[FRAMEWORK]]`.
8. **Roadmap Dependencies column contains only `None` or `Gap {N}` references — no prose.**
9. **Cycle prevention.** No gap depends on itself directly or transitively. Every dependency target precedes its dependent in the roadmap.
10. **Cross-references** use canonical part numbers (e.g., "see Part 12"). No file names, agent numbers in cross-references.
11. **British English** throughout.
12. **Date format YYYY-MM-DD.**
13. **Out-of-scope corpus / tracked-files-only.** Every source file cited MUST be tracked by git on the current branch. Do not mention or link to `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.{md,html}`, `agentic-governance-stack.{md,html}`, `manifesto-evolution-plan.{md,html}`, `phase-assessment-checklist.{md,html}`, `aplc-plan*`, or `igm-aent-coherence-review*`. Output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`.
14. **Banned soft language** — core list (`consider`, `may`, `could potentially`, `perhaps`, `use judgement`) plus extended list (per §2.7).
15. **Architectural strengths whose deployment gap blocks `target_gate` or `target_layer` MUST also appear as gaps; cross-reference both sides by number.**
16. **No `[[DOMAIN_FILE]]` forward-propagation** beyond cited regulations.

---

## 5. Self-check (gate)

- [ ] Step 1 preflight passed: Glob returned all 17 upstream files; each has ≥ 20 lines; no header-line placeholder leakage.
- [ ] Score Authority Table is present with 11 rows (one per ASDLC category) and Divergence flags.
- [ ] `target_gate` and `target_layer` extracted from `**ASDLC Readiness: L{N} operating, G{M} routinely passing**` in Review 05; substituted everywhere; no literal `{target_gate}` or `{target_layer}` text in output. Target-gate computation covers all four gates (G1 SR → G2 Release → G3 OpReady → G4 Retirement); when `target_gate = G4` and the framework is silent on retirement, the gap is annotated as structural-silence.
- [ ] Self-referential-grading disclaimer paragraph appears at the top of Part 10 and (in reprise) at the top of Part 11.
- [ ] Where the framework cites external normative authorities (NIST / OWASP / DORA / EU AI Act / ISO 42001 / analogous), the strengths or gaps reference `freshness-register.yaml` (or the equivalent freshness-register pattern) and surface hidden-currency risk where no register is operated.
- [ ] Every strength has: dual-anchor evidence (Wave 1 anchor + source anchor verbatim from [[FRAMEWORK]] source), Mechanism / Why genuinely good / Better than the alternative subsections, fairness note sourced from the same file's evidence-against section.
- [ ] Strength count is between 5 and 12; ordering follows §2.4.
- [ ] Every gap heading uses the exact format `### Gap {N} — {title} *(Severity — <category>[, <category>])*` with a valid severity label.
- [ ] Every gap has: Current state, What is missing, What `target_gate / target_layer` requires, Why it matters for `[[ORGANIZATION]]` in `[[INDUSTRY]]` (with article/section numbers from `[[DOMAIN_FILE]]`), What closes it (3–6 numbered concrete actions), Evidence anchor (dual: Wave 1 + source), Effort (with dominant-dimension annotation when non-engineering dominates).
- [ ] Gap count is between 5 and 12.
- [ ] Severity for every multi-category gap is the highest band of affected categories, escalated one step if a `target_gate` or `target_layer` advancement is blocked.
- [ ] All Critical Wave 1 findings (Review 07 Parts 12–13 and any layer/gate-file Critical) appear as gaps unless explicitly justified out-of-scope.
- [ ] Scope gaps tagged `(Scope gap — {regulation})` in the title.
- [ ] Architectural strengths whose deployment gap is a `target_gate / target_layer` blocker also appear as gaps; each side cross-references the other by number.
- [ ] Roadmap row count equals gap count; row ordering matches gap-section ordering.
- [ ] Roadmap Dependencies column contains only `None` or comma-separated `Gap {N}` references — no prose.
- [ ] No gap depends on itself directly or transitively; every dependency target precedes its dependent in the table.
- [ ] Roadmap Interpretation has one paragraph per effort tier (S, M, L/XL) plus a closing adoption-ceiling paragraph; tier paragraphs justify sequencing by reference to regulatory exposure.
- [ ] No banned soft language appears in the output (core list + extended list per §2.7).
- [ ] Zero matches for any out-of-scope-corpus token (`APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, `igm-aent-coherence-review`) anywhere in the output. Every source file referenced is tracked by git on the current branch.
- [ ] Every claim in strengths and gaps is anchored to a verbatim quote from a named Wave 1 source file with path.
- [ ] All cross-references use canonical part numbers; no file names or agent numbers in cross-references within output content.
