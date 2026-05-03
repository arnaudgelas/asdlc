# Sub-prompt 04c — Adoption + Governance Synthesis (Part 6 + Part 7 Combined)

**Purpose.** Produce the canonical combined Part 6 + Part 7 file for `[[FRAMEWORK]]` by lifting Part 6 from agent 04a's output and Part 7 from agent 04b's output, harmonising headings, deduplicating gap inventories, and adding a Cross-Document Synthesis section. This is a Wave 1b agent — runs after Wave 1a is fully complete.

**Wave:** Wave 1b. Depends on Wave 1a outputs `_review_04a_adoption.md` and `_review_04b_governance.md`. Cannot read other Wave 1b outputs.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04_adoption_governance.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`.

---

## 1. Inputs to read

### 1.1 Mandatory dependencies (abort if missing)

- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04a_adoption.md` — Part 6 source.
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04b_governance.md` — Part 7 source.

Each must have ≥ 20 lines and contain its canonical Part heading. If either is missing, malformed, or empty, STOP and report — do not fabricate content.

### 1.2 Reference (read for synthesis context only — do not re-derive scores)

- `asdlc.md` — for `## Realistic Adoption Ceiling` framing and the layer-and-gate readiness model.
- `asdlc-guide.md` — for adoption-sequence implications.
- `conformance-profiles.md` — the four ASDLC conformance profiles (ASDLC-Limited, ASDLC-Standard, ASDLC-Regulated, ASDLC-Tier4) used to frame ceiling targets.
- `annex-adoption-cost.md` — calibrated adoption-cost ranges (FTE uplift, reviewer hours, ceremony cadence) used to ground the ceiling.
- `annex-igm.md` — Tier 4 + IGM intelligence constraints (the four envelope elements); referenced where synthesis touches Tier 4 obligations.
- `annex-aentm.md` — Tier 4 + AEnt-M relocation mechanics; referenced where synthesis touches Tier 4 obligations.
- `[[DOMAIN_FILE]]` — for industry context.

### 1.3 Scope guards

- Do NOT re-read `[[FRAMEWORK]]` source artefacts to re-derive scores. Synthesis only.
- Do NOT issue a determinative readiness verdict (Part 8 territory; owned by agent 05a → 05b).
- Do NOT issue a production-deployment red line (Part 9 territory; owned by agent 05b).
- Do NOT issue a remediation roadmap (Part 11 territory; owned by agent 06).

---

## 2. Methodology

### 2.1 Lift mechanics

Lift Part 6 from `_review_04a_adoption.md` verbatim, with these heading harmonisations:
- 04a's H1 (`# [[FRAMEWORK]] Review 04a — ...`) is dropped.
- 04a's `## Methodology (brief)` is dropped.
- 04a's `## Part 6 — ASDLC Adoption Sequence Alignment` becomes `## Part 6 — ASDLC Adoption Sequence Alignment` (unchanged).
- 04a's `### step-N-...` H3 subsections are preserved verbatim.
- 04a's machine-readable `<!-- GAP INVENTORY ... -->` block is dropped (will be merged into the combined file's single inventory).
- 04a's `*Sources read: ...*` footer is dropped (will be merged).

Lift Part 7 from `_review_04b_governance.md` verbatim with the same harmonisation pattern (dropping H1, Methodology, GAP INVENTORY, Sources read; preserving the Part 7 heading and 5 H3 subsections).

The order in the combined file is: Part 6 (lifted from 04a) → Part 7 (lifted from 04b) → Cross-Document Synthesis (new) → merged GAP INVENTORY → merged `*Sources read: ...*` footer.

### 2.2 Deduplication of gap inventories

Read both 04a's and 04b's `<!-- GAP INVENTORY ... -->` blocks. Merge into a single block in the combined file. If two gaps describe the same underlying issue (e.g., one in 04a step-2-sr-gate and one in 04b governance-agents that both concern the same accountability gap), preserve both entries — they reflect distinct subsection contexts.

### 2.3 Cross-Document Synthesis section (new content)

Add a `## Cross-Document Synthesis` section between Part 7 and the GAP INVENTORY block. It contains exactly two subsections:

#### 2.3.1 `### Realistic Adoption Ceiling at [[ORGANIZATION]]`

Open with the canonical verdict sentence in this exact form:

> [[FRAMEWORK]] can support adoption up to **L{N} operating, G{M} routinely passing** in `[[INDUSTRY]]` contexts without significant additional tooling.

Where `{N}` ∈ 1..4 and `{M}` ∈ {SR, Release, OpReady, none}. The verdict is bounded by the LOWEST unmet adoption-step from Part 6 OR the LOWEST unmet governance area from Part 7, whichever bounds tighter. Do not raise the ceiling above what either source supports.

After the verdict sentence, include 4–8 evidence bullets, each:
- Citing a Part 6 OR Part 7 subsection by canonical slug (e.g., `Part 6 — step-2-sr-gate`, `Part 7 — waiver-governance`).
- Naming a specific `[[FRAMEWORK]]` artefact (in backticks) supporting the ceiling.
- Stating the adoption-readiness implication for `[[ORGANIZATION]]`.

After the evidence bullets, include a single grounding paragraph (≤120 words) that:
- Names the conformance profile from `conformance-profiles.md` most achievable for `[[FRAMEWORK]]`'s declared scope at `[[ORGANIZATION]]` (one of ASDLC-Limited, ASDLC-Standard, ASDLC-Regulated, ASDLC-Tier4).
- Cites adoption-cost ranges (FTE uplift, reviewer hours, ceremony cadence) from `annex-adoption-cost.md` corresponding to that profile.
- States explicitly that the realistic ceiling is a profile + a calibrated cost range, not a percentage.
- Where the synthesis touches Tier 4 obligations, cross-references `annex-igm.md` (the four envelope elements) and `annex-aentm.md` (relocation mechanics).
- Acknowledges the four-gate cascade (SR → Release → OpReady → Retirement). Where the synthesis references the G4 (Retirement) gate, cross-reference `prompt-02-gate.md`'s G4 handling: frameworks predating retirement formalisation are not punitively zeroed but the gap is named.

Close with one single-binding-constraint sentence in the form:

> The binding constraint on this ceiling is `<lowest unmet adoption-step or governance area>` — closing it requires `<specific artefact, mechanism, or process>`.

#### 2.3.2 `### Highest-Leverage Single Change`

Identify the ONE change to `[[FRAMEWORK]]` that would raise the adoption ceiling by the largest margin. Three required attributes:

- **Specific:** name the artefact, command, capability, schema field, or rule that would change.
- **Grounded:** cite Part 6 or Part 7 by canonical part number and subsection slug.
- **Proportionate:** explain why this single change unlocks more ceiling than any other single change.

The single change MUST be tractable (effort label S, M, or L per `prompt.md`'s effort sizing); XL changes are organisation-level transformations and not "single changes" by definition.

### 2.4 Banned soft language and extended banned list

In addition to `prompt.md`'s core banned list, agent 04c MUST avoid the extended list (without an evidence anchor in the same paragraph): `robust`, `comprehensive`, `world-class`, `industry-leading`, `best-in-class`, `leverages`, `empowers`, `enables` (without naming what is enabled), `seamless`, `holistic`, `mature` (without phase number), `production-ready` (without naming what is production), `powerful` (without naming the power).

### 2.5 Idempotence

Glob output. If exists AND ≥ 20 lines AND contains both Part 6 and Part 7 H2 headings AND contains `## Cross-Document Synthesis`, exit. Otherwise rewrite.

### 2.6 STOP and report on out-of-scope token

If lifted material from 04a or 04b contains any out-of-scope-corpus token (e.g., `APLC`, `intelligence-governance-manifesto`, etc.), STOP and report — do not silently scrub the lifted material. The upstream agent should have caught this. Note: `IGM`, `AEnt-M`, and `AEnt_M` are permitted when used as part of the canonical ASDLC annex references (`annex-igm.md`, `annex-aentm.md`) or when paraphrasing the constraints those annexes encode.

---

## 3. Output structure

### 3.1 File path

```
[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04_adoption_governance.md
```

### 3.2 H1 heading and metadata

```
# [[FRAMEWORK]] Review 04 — Adoption & Governance Alignment (Combined Parts 6 + 7)

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`
**Sources lifted:**
- Part 6 — `_review_04a_adoption.md`
- Part 7 — `_review_04b_governance.md`

---

## Methodology (brief)

<2–4 sentences naming the lift sources, the synthesis approach, and stating that re-derivation of subsection scores from `[[FRAMEWORK]]` source artefacts is forbidden.>

---

<lifted Part 6 content from 04a, with H1 / Methodology / GAP INVENTORY / Sources read dropped>

---

<lifted Part 7 content from 04b, with H1 / Methodology / GAP INVENTORY / Sources read dropped>

---

## Cross-Document Synthesis

### Realistic Adoption Ceiling at [[ORGANIZATION]]

> [[FRAMEWORK]] can support adoption up to **L<N> operating, G<M> routinely passing** in `[[INDUSTRY]]` contexts without significant additional tooling.

<4–8 evidence bullets each citing a Part 6 or Part 7 subsection by canonical slug, naming a specific [[FRAMEWORK]] artefact, and stating the adoption-readiness implication.>

<one grounding paragraph (≤120 words) naming the most achievable conformance profile from `conformance-profiles.md`, citing adoption-cost ranges from `annex-adoption-cost.md`, stating that the ceiling is a profile + a calibrated cost range (not a percentage), cross-referencing `annex-igm.md` and `annex-aentm.md` where Tier 4 obligations are touched, and acknowledging the four-gate cascade with cross-reference to `prompt-02-gate.md`'s G4 handling.>

> The binding constraint on this ceiling is `<lowest unmet adoption-step or governance area>` — closing it requires `<specific artefact, mechanism, or process>`.

### Highest-Leverage Single Change

<One paragraph (120–200 words) identifying the single tractable change (S/M/L effort) that would raise the adoption ceiling most. Three required attributes: Specific (named artefact / command / capability), Grounded (Part 6 / Part 7 cross-reference), Proportionate (why this beats other single changes).>

---

<!-- GAP INVENTORY (merged from 04a and 04b)
- subsection: <name> | severity: <severity> | gap_text: <text>
... (deduplicated; one line per gap)
-->

*Sources read: <merged enumeration from 04a + 04b + this agent>*
```

---

## 4. Hard rules

1. **Preflight is non-optional.** If 04a or 04b is missing, empty, or malformed (< 20 lines or missing canonical Part heading), STOP and report — do not fabricate content.
2. **Lift verbatim.** Do not paraphrase, summarise, or re-score subsection content lifted from 04a / 04b. Heading harmonisation only.
3. **Subsection ordering is canonical** (per the sibling specs in 04a and 04b) and must not be re-ordered during lifting.
4. **GAP INVENTORY merge.** Read both upstream blocks and merge into a single block. Do not silently drop entries.
5. **No re-derivation of scores from `[[FRAMEWORK]]` source artefacts.** Synthesis only.
6. **No determinative readiness verdict** in Cross-Document Synthesis — that is Part 8 territory (agent 05a / 05b). The adoption-ceiling sentence is bounded synthesis, not a determinative verdict; it cannot exceed agent 05a's verdict line.
7. **No production-deployment red line.** Part 9 territory.
8. **No remediation roadmap.** Part 11 territory.
9. **Cross-references** use canonical part numbers (`Part 6`, `Part 7`). The synthesis-level subsection reference form is `Part 6 — <subsection-slug>` or `Part 7 — <subsection-slug>`.
10. **Date format YYYY-MM-DD** wherever a date appears.
11. **Out-of-scope corpus / tracked-files-only.** Every source file cited MUST be tracked by git on the current branch. Do not reference `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.{md,html}`, `agentic-governance-stack.{md,html}`, `manifesto-evolution-plan.{md,html}`, `phase-assessment-checklist.{md,html}`, `aplc-plan*`, or `igm-aent-coherence-review*`. Output MUST contain zero matches for the tokens `APLC`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`. The tokens `IGM`, `AEnt-M`, and `AEnt_M` are permitted ONLY when used as part of the canonical ASDLC annex references (`annex-igm.md`, `annex-aentm.md`) or when paraphrasing the constraints those annexes encode. If lifted material from 04a or 04b contains any out-of-scope token, STOP and report.
12. **Banned soft language.** Core list (`consider`, `may`, `could potentially`, `perhaps`, `use judgement`) plus extended list (per §2.4). Make falsifiable statements grounded in cited artefacts.

---

## 5. Self-check before saving

- [ ] Preflight passed: 04a and 04b both exist, both have ≥ 20 lines, both contain their canonical Part heading.
- [ ] Output file path is `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04_adoption_governance.md`.
- [ ] All `[[VARIABLE]]` placeholders in the output content are substituted; any remaining placeholder triggers STOP-and-report.
- [ ] The header block names both sibling source files explicitly.
- [ ] `## Methodology (brief)` is present, ≤120 words, and explicitly states that re-derivation is forbidden.
- [ ] Part 6 has been lifted from 04a verbatim, with the 7 canonical H3 subsections in order, and the special sub-blocks (Output Lifecycle & Version Migration in step-1; Decommissioning Readiness in step-6; Tier-4-graduation `**Fundamental incompatibility:**` sub-header where applicable).
- [ ] Part 7 has been lifted from 04b verbatim, with the 5 canonical H3 subsections in order and a `Contradictions` block inside every subsection.
- [ ] No 04a/04b H1, no 04a/04b `## Methodology`, no 04a/04b `<!-- GAP INVENTORY -->` block, and no 04a/04b `*Sources read: ...*` footer is duplicated inside the combined file's Part 6/Part 7 sections.
- [ ] The Cross-Document Synthesis section is present with both `Realistic Adoption Ceiling at [[ORGANIZATION]]` and `Highest-Leverage Single Change` subsections.
- [ ] The `Realistic Adoption Ceiling` subsection opens with the canonical verdict sentence (`L{N} operating, G{M} routinely passing` form), contains 4–8 evidence bullets each citing a Part 6 or Part 7 subsection, includes a grounding paragraph that names the most achievable conformance profile from `conformance-profiles.md` and cites adoption-cost ranges from `annex-adoption-cost.md` (with explicit statement that the ceiling is a profile + a calibrated cost range, not a percentage), cross-references `annex-igm.md` and `annex-aentm.md` where Tier 4 obligations are touched, acknowledges the four-gate cascade with a cross-reference to `prompt-02-gate.md`'s G4 handling, and closes with the single-binding-constraint sentence.
- [ ] The `Highest-Leverage Single Change` subsection identifies a Specific, Grounded, and Proportionate single change of S / M / L effort.
- [ ] At least 5 distinct regulations or risk-types from `[[DOMAIN_FILE]]` are referenced across the combined file.
- [ ] Every regulatory citation includes either an Article number, section number, or named risk-register entry.
- [ ] All dates use YYYY-MM-DD format.
- [ ] Zero matches for any out-of-scope-corpus token (`APLC`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, `igm-aent-coherence-review`) anywhere in the output file. Use of `IGM`, `AEnt-M`, `AEnt_M` is permitted ONLY when bound to the canonical ASDLC annex references (`annex-igm.md`, `annex-aentm.md`) or when paraphrasing the constraints those annexes encode. Every cited source file is tracked by git on the current branch.
- [ ] Output does NOT contain banned soft language (core list + extended list per §2.4) without an evidence anchor in the same paragraph.
- [ ] Output does NOT contain a composite [[FRAMEWORK]] score.
- [ ] Output does NOT contain a determinative readiness verdict (Part 8 territory) or a production-deployment red line (Part 9 territory).
- [ ] The merged `<!-- GAP INVENTORY ... -->` block is present at end before the `*Sources read: ...*` footer.
- [ ] Output closes with merged `*Sources read: ...*` footer.
