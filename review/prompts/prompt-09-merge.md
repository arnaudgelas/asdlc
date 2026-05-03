# Sub-prompt 09 — Merge

**Purpose.** Produce the final merged ASDLC alignment review for `[[FRAMEWORK]]` by consolidating 15 source files into a single canonical 14-Part document. This is a Wave 3 agent — runs after all Wave 1a, Wave 1b, and Wave 2 outputs are complete.

**Wave:** Wave 3. Reads 15 canonical source files. Writes one output file.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_asdlc_alignment_review_merged.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`.

---

## 1. Inputs to read — 15 canonical source files

All must exist and be non-empty (≥ 20 lines). If any is missing, do NOT run the merge — report the missing file(s) and stop.

| Source agent | File | Provides |
| --- | --- | --- |
| 01 | `_review_01_quick_overview.md` | Part 1 (Overall Scores), Part 2 (Methodology), Framing Warning |
| 02-l1 | `_review_02_layer_l1.md` | Part 3 — L1 Demand & Value detail |
| 02-l2 | `_review_02_layer_l2.md` | Part 3 — L2 Engineering Execution detail (incl. Tier 4 envelope) |
| 02-l3 | `_review_02_layer_l3.md` | Part 3 — L3 Release & Deployment detail |
| 02-l4 | `_review_02_layer_l4.md` | Part 3 — L4 Operations & Maintenance detail |
| 02-g1 | `_review_02_gate_g1.md` | Part 4 — SR Gate detail |
| 02-g2 | `_review_02_gate_g2.md` | Part 4 — Release Gate detail |
| 02-g3 | `_review_02_gate_g3.md` | Part 4 — Operational Readiness Gate detail |
| 02-g4 | `_review_02_gate_g4.md` | Part 4 — Retirement Gate detail |
| 03 | `_review_03_gates_dods.md` | Part 4 + Part 5 (Engineering DoD + Operational DoD), cross-gate failure modes, feedback paths closure, human escalation, industry-specific DoD |
| 04c | `_review_04_adoption_governance.md` | Part 6 + Part 7 + Cross-Document Synthesis (Realistic Adoption Ceiling + Highest-Leverage Single Change) |
| 05b | `_review_05_readiness_industry.md` | Part 8 (Layer Readiness Verdict + Tier 4 Envelope) + Part 9 (Industry & Client) |
| 06 | `_review_06_strengths_gaps.md` | Part 10 (Strengths) + Part 11 (Gaps) + Prioritised Remediation Roadmap |
| 07 | `_review_07_guardrails_security.md` | Part 12 (Guardrails) + Part 13 (Security + FinOps + DevSecOps) |
| 08b | `_review_08_enterprise_guardrails.md` | Part 14 (§14.1–§14.19) |

The intermediate files `_review_04a_adoption.md`, `_review_04b_governance.md`, `_review_05a_readiness.md`, `_review_08a_domains.md` are NOT direct inputs — they are upstream of 04c, 05b, and 08b respectively.

---

## 2. Methodology

### 2.1 Preflight

#### Step 1 — File existence

Glob all 15 canonical source files. Confirm each exists, has ≥ 20 lines, contains its canonical Part heading, and contains no header-line `[[...]]` placeholder leakage. If any check fails, STOP and report — do not run the merge.

#### Step 1b — ASDLC provenance hash consistency

Every Wave 1 / Wave 2 source file MUST carry an identical `ASDLC: arnaudgelas/asdlc@<hash>` provenance line (per the orchestrator's hard rule that every output include the provenance line). Run:

```
grep -h '^ASDLC: ' [[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_*.md | sort -u
```

If the result returns more than one unique line, STOP. Do not run the merge. Report which agents ran against which hashes — for each input file, emit a row showing `<file> -> <hash>`. A divergent hash set indicates the operator performed a partial re-run with stale agents; the merge cannot reconcile review fragments scored against different ASDLC versions. The operator must re-run the stale agents against the current `[[ASDLC_HASH]]` before merging.

#### Step 2 — Score-integrity cross-checks

Perform 8 score-integrity cross-checks and record results verbatim in `## Source Integrity` per the schema in §3.4:

1. **Category-score consistency.** For each of the 12 ASDLC categories: agent 01's Part 1 score equals the authoritative agent's score (02-l1..l4 for layers, 02-g1..g4 for gates, 03 for DoDs, 05a-via-05b for T4, 04b-via-04c for CG, 07 for FS, 03 for FB) within rounding tolerance.
2. **Composite arithmetic.** Recompute `Σ(category_score × decimal_weight)` from Part 1's table; verify it equals the metadata `Overall score`.
3. **Verdict-line preservation.** The `**ASDLC Readiness: L{N} operating, G{M} routinely passing**` line in agent 05b's Part 8 is preserved verbatim in the merged file.
4. **Maturity-verdict preservation.** The `**Enterprise Guardrail Maturity: <LACKING | PARTIAL | ADEQUATE | MATURE>**` line in agent 08b's §14.19 is preserved verbatim.
5. **Determinism-verdict preservation.** The `**Determinism verdict: ...**` line in agent 07's §13.1 is preserved verbatim.
6. **Hardening-verdict preservation.** The exactly-one-of-two `Hardening is complete.` / `Hardening is not complete.` sentence in agent 03's DoD Hardening Test is preserved verbatim.
7. **Roadmap-gap-count consistency.** The Prioritised Remediation Roadmap's row count from agent 06 equals the count of Gap entries in Part 11.
8. **Severity-band consistency.** Every severity label across all merged Parts maps correctly to the canonical severity thresholds in `prompt.md`.

Any divergence is recorded as an integrity warning in `## Source Integrity`. **If any Wave 1 source contains an out-of-scope-corpus token, surface it as an integrity warning and STOP — do not silently scrub it from lifted material; the upstream agent should have caught it.**

### 2.2 Canonical Part order in the merged file

```
0. Scope of this review (self-referential-grading disclaimer callout; verbatim per §3.2)
1. Framing Warning (from agent 01)
2. Executive Verdict (synthesis; ≤ 800 words; see §2.3)
3. Part 1 — Overall Scores (from agent 01)
4. Part 2 — Scoring Methodology (from agent 01)
5. Part 3 — ASDLC Layer Coverage (from 02-l1, 02-l2, 02-l3, 02-l4 in that order)
6. Part 4 — ASDLC Gate Analysis (from 02-g1, 02-g2, 02-g3, 02-g4 + cross-gate failure modes from agent 03)
7. Part 5 — ASDLC Definitions of Done (from agent 03: Engineering DoD + Operational DoD + Hardening Test + Industry-Specific DoD Requirements)
8. Part 6 — ASDLC Adoption Sequence Alignment (from agent 04c, lifted from 04a)
9. Part 7 — Cross-cutting Governance Alignment (from agent 04c, lifted from 04b)
10. Cross-Document Synthesis (Realistic Adoption Ceiling + Highest-Leverage Single Change, from agent 04c)
11. Part 8 — Layer Readiness & Tier 4 Verdict (from agent 05b, lifted from 05a)
12. Part 9 — Industry & Client Assessment (from agent 05b)
13. Part 10 — Genuine Strengths (from agent 06)
14. Part 11 — Gap Analysis (from agent 06)
15. Part 12 — AI/Runtime Guardrails Assessment (from agent 07)
16. Part 13 — Security, FinOps & DevSecOps Assessment (from agent 07)
17. Part 14 — Enterprise Guardrail Domain Coverage (from agent 08b; §14.1–§14.19)
18. Prioritised Remediation Roadmap (from agent 06)
19. [[ORGANIZATION]] Deployment Recommendation (synthesis; see §2.4)
20. Source Integrity (the 8 cross-checks from §2.1)
21. Appendices A–E (see §2.5)
```

### 2.3 Executive Verdict (≤ 800 words; self-contained)

The Executive Verdict is a self-contained summary placed immediately after the Framing Warning and before Part 1. It MUST include:

- **(a)** Overall score and severity label.
- **(b)** Layer Readiness Verdict from Part 8 verbatim (the `**ASDLC Readiness: ...**` line).
- **(c)** Top-3 strengths from agent 06 Part 10 (short forms, ≤ 1 sentence each).
- **(d)** Top-3 highest-severity gaps from agent 06 Part 11 (short forms, ≤ 1 sentence each).
- **(e)** The Red Line verbatim from agent 05b Part 9.
- **(f)** Highest-leverage single change verbatim from agent 04c Cross-Document Synthesis.
- **(g)** Enterprise Guardrail Maturity verdict from agent 08b §14.19 verbatim.

The Executive Verdict is a self-contained reading entry point — a regulator or executive should be able to read this section and obtain the binding constraints without reading the rest of the document.

### 2.4 [[ORGANIZATION]] Deployment Recommendation

A synthesis section between the Roadmap and Source Integrity. Synthesises:

- The Layer Readiness Verdict (Part 8).
- The Deployment Path stages (Part 9).
- The Roadmap (from Part 11).
- The Red Line (Part 9).

It must address `[[INDUSTRY]]` regulatory constraints; it must not contradict the Red Line. The recommendation MUST state explicitly:
- Which workflows from `[[DOMAIN_FILE]]` are recommended for production deployment under the framework as it stands today.
- Which workflows require remediation completion before deployment (and which Roadmap entries close the gap).
- Which workflows are out of scope (Red Line) and why.

### 2.5 Appendices

| Appendix | Content | Source |
| --- | --- | --- |
| A | Adversarial Scenario | agent 07 §12.5 (verbatim) |
| B | Security Coverage Map | agent 07 §13.2 (verbatim, all 11 control-family rows) |
| C | Evidence Matrix | agent 05b Part 8 Evidence Matrix (verbatim) |
| D | Peer-Framework Comparison | agent 05b Comparison subsection (when `[[PRIOR_REVIEWS]]` ≠ `none`); else explicit "No prior reviews" entry |
| E | Glossary | `[[FRAMEWORK]]`-specific terms only (module names, command names, configuration keys, framework-internal concepts). **Contains zero entries for ASDLC vocabulary** (layer names, gate names, autonomy tier names, DoD condition names, severity labels, effort labels). Alphabetical. British English. |

### 2.6 Banned soft language and merge-time additions
Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`. The merge is editorial synthesis; new analytical claims are not permitted. Do not introduce findings, scores, severity labels, regulations, or strengths that do not appear in any Wave 1 / Wave 2 source. Do not relabel severity (Critical → High, etc.) without surfacing the change in Source Integrity.

### 2.7 Idempotence
Glob output. If exists AND ≥ 100 lines AND contains all 14 canonical Parts AND contains the Executive Verdict AND contains Source Integrity AND contains all 5 appendices, exit. Otherwise rewrite.

---

## 3. Output structure

### 3.1 File path

```
[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_asdlc_alignment_review_merged.md
```

### 3.2 H1 heading and metadata

```
# [[FRAMEWORK]] — ASDLC Alignment Review (Merged)

**Framework:** [[FRAMEWORK]]
**Framework version:** [[FRAMEWORK_VERSION]]
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Review date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`
**Overall score:** <X.X>/100 (<severity>)
**Layer Readiness:** **ASDLC Readiness: L<N> operating, G<M> routinely passing**
**Enterprise Guardrail Maturity:** <LACKING | PARTIAL | ADEQUATE | MATURE>
**Sources merged:** 15 canonical files (see Source Integrity)

---

> **Scope of this review.** This review system grades [[FRAMEWORK]] against
> ASDLC's own assertions, not against externally-anchored regulatory or
> engineering source-of-truth. When the review flags a gap in [[FRAMEWORK]]
> against an ASDLC condition, the operator must additionally verify that
> ASDLC's own claim against the underlying regulatory or engineering source
> is itself sound. The review system does not perform that outer
> verification.

---
```

`[[FRAMEWORK_VERSION]]` MUST be embedded verbatim in the metadata block (the value passed by the orchestrator at substitution time; `unknown` if not versioned). Cross-version review comparison depends on this field. The `Scope of this review` callout MUST appear immediately after the metadata block and before Part 1 (or, where the Framing Warning precedes Part 1 per §2.2, immediately after the metadata block and before the Framing Warning) — it is the self-referential-grading disclaimer carried into the merged review for stakeholders reading the document in isolation, and the wording above is the canonical paragraph lifted from the orchestrator.

### 3.3 Section order

Render the sections in the order specified in §2.2.

### 3.4 Source Integrity schema

`## Source Integrity` MUST contain entries in the following format, one per cross-check (8 fixed entries from §2.1):

```
- **[Cross-check name]:** <PASS | FAIL with annotation> — <one-sentence explanation citing the upstream source file(s)>
```

Plus any additional integrity warnings surfaced (e.g., out-of-scope-token detection in lifted material — though by §2.6 STOP rule, such cases prevent the merge from completing in the first place).

---

## 4. Hard rules

1. **Preflight is non-optional.** All 15 source files must exist, be ≥ 20 lines, and contain their canonical Part headings. All 15 source files MUST share an identical `ASDLC: arnaudgelas/asdlc@<hash>` provenance line per §2.1 Step 1b. If any check fails, STOP and report.
2. **Composite arithmetic verification.** Recompute Σ(category_score × decimal_weight); the metadata `Overall score` MUST match.
3. **Verdict-line preservation.** All four verdict lines (Layer Readiness from Part 8; Enterprise Guardrail Maturity from §14.19; Determinism from §13.1; Hardening from Part 5 DoD Hardening Test) preserved verbatim.
4. **Cross-references** use canonical part numbers only — zero matches for source-file names (e.g., `_review_03_gates_dods.md`), agent numbers (e.g., `agent 06`), or Wave designations.
5. **Editorial merge only.** Do not introduce new analytical claims, new findings, new scores, or new severity labels not present in Wave 1 / Wave 2 sources. Do not relabel severity without surfacing in Source Integrity.
6. **Executive Verdict ≤ 800 words** and self-contained — must include the seven required elements (a)–(g) per §2.3.
7. **`[[ORGANIZATION]] Deployment Recommendation` synthesises but does not contradict the Red Line.**
8. **Glossary (Appendix E) contains zero entries for ASDLC vocabulary.** Only `[[FRAMEWORK]]`-specific terms.
9. **Date format YYYY-MM-DD.** British English.
10. **Out-of-scope corpus / tracked-files-only.** Every source file referenced in the merged document MUST be tracked by git on the current branch. No references to `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.md`, `agentic-enterprise.html`, `agentic-governance-stack.md`, `agentic-governance-stack.html`, `manifesto-evolution-plan.md`, `manifesto-evolution-plan.html`, `phase-assessment-checklist.md`, `phase-assessment-checklist.html`, `aplc-plan*`, or `igm-aent-coherence-review*` anywhere in the merged document. The output file MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc`, `aplc-plan`, or `igm-aent-coherence-review`. Forward-propagation prohibition extends to `[[DOMAIN_FILE]]` and to any cross-stack file in `governance/`, `domains/`, or `operations/` that the Wave 1 sources cited: do not embed full passages from those files, do not derive IGM/AEnt-M/APLC roadmaps, and do not invent domain bridges that are not present in `[[DOMAIN_FILE]]`. **If any Wave 1 source contains an out-of-scope-corpus token, surface it in `## Source Integrity` as an integrity warning and STOP — do not silently scrub it from lifted material; the upstream agent should have caught it.**
11. **Do not praise `[[FRAMEWORK]]` for things it does not demonstrably do.** Do not penalise it for problems outside its stated scope — but note scope gaps explicitly.
12. **No banned soft language** (`consider`, `may`, `could potentially`, `perhaps`, `use judgement`).

---

## 5. Self-Check (HARD GATE before saving the output file)

**Do not save the output file until every item below is confirmed.** Each item is binary yes/no. If any item fails, fix the file content and re-verify before saving.

- [ ] All 15 source files confirmed valid by Preflight Step 1 (≥ 20 lines each, non-empty first/last 5 lines).
- [ ] Preflight Step 1b provenance-hash check returned exactly one unique `ASDLC: arnaudgelas/asdlc@<hash>` line across all 15 source files.
- [ ] Metadata block contains `**Framework version:** [[FRAMEWORK_VERSION]]` with the orchestrator-substituted value (not the literal placeholder).
- [ ] `Scope of this review` callout (the self-referential-grading disclaimer) is present in the preamble between the metadata block and Part 1.
- [ ] All 8 score-integrity cross-checks completed; results recorded verbatim in `## Source Integrity` with the fixed entry schema.
- [ ] Composite arithmetic recomputed; metadata `Overall score` equals `Σ(score × decimal_weight)` from Part 1's table, rounded to one decimal place.
- [ ] Framing Warning section (4 sub-sections) is present between metadata and Executive Verdict.
- [ ] Executive Verdict is self-contained, ≤ 800 words, and includes all seven required elements (a) through (g).
- [ ] Executive Verdict's Layer Readiness equals Part 8's verdict line verbatim.
- [ ] Executive Verdict's Red Line equals Part 9's Red Line verbatim.
- [ ] Executive Verdict's highest-leverage single change equals agent 04c's Cross-Document Synthesis verbatim; any drift is logged in Source Integrity.
- [ ] Executive Verdict's Enterprise Guardrail Maturity equals agent 08b's §14.19 verdict line verbatim.
- [ ] All 14 canonical Parts present and in order; Cross-Document Synthesis present between Part 7 and Part 8; Part 14 (Enterprise Guardrail Domain Coverage) present after Part 13 and before the Prioritised Remediation Roadmap. Part 14 contains all 19 sub-sections (§14.1–§14.15, §14.16 cross-cutting matrix, §14.17 twelve non-negotiables, §14.18 schema verification, §14.19 maturity verdict).
- [ ] Part 14 does NOT introduce any re-score of categories or restate the composite. Overlap with Part 12 / Part 13 is by cross-reference, not duplication.
- [ ] Part 14 §14.19 contains a verbatim `**Enterprise Guardrail Maturity: <LACKING | PARTIAL | ADEQUATE | MATURE>**` line lifted from `_review_08_enterprise_guardrails.md`.
- [ ] Part 5 contains exactly one of the literal phrases `Hardening is complete.` or `Hardening is not complete.` (lifted verbatim from agent 03's DoD Hardening Test).
- [ ] Part 13 §13.1 Determinism verdict line is preserved verbatim.
- [ ] `## Prioritised Remediation Roadmap` row count equals the number of gaps in Part 11. Each row cites the specific Gap N entry. Effort labels match the gap detail.
- [ ] `## [[ORGANIZATION]] Deployment Recommendation` synthesises from agents 05 and 06 and addresses `[[INDUSTRY]]` regulatory constraints; does not contradict the Red Line.
- [ ] All five appendices (A–E) populated. Appendix A reproduces agent 07 §12.5 verbatim. Appendix B preserves all 11 control-family rows. Appendix C preserves agent 05b's Evidence Matrix. Appendix D handles the `[[PRIOR_REVIEWS]] = none` case explicitly if applicable.
- [ ] Glossary (Appendix E) contains only `[[FRAMEWORK]]`-specific terms. Contains zero entries for ASDLC vocabulary (layer names, gate names, autonomy tier names, DoD condition names, severity labels, effort labels). Alphabetical, British English.
- [ ] Cross-references use canonical part numbers only — zero matches for source-file names, agent numbers, or Wave designations.
- [ ] Output file contains zero matches for `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc`, `aplc-plan`, or `igm-aent-coherence-review`. Every source file referenced in the merged document is tracked by git on the current branch.
- [ ] Output file contains zero matches for the banned soft-language tokens `consider`, `may`, `could potentially`, `perhaps`, `use judgement`.
- [ ] Output file contains zero remaining `[[...]]` placeholders.
- [ ] Output file contains no source-file metadata blocks, per-agent "Inputs to Read" sections, per-agent "Methodology" sections, or per-source-file H1 titles or footers.
