# Sub-prompt 04a — ASDLC Adoption Sequence Alignment (Part 6)

**Purpose.** Produce the Part 6 file for `[[FRAMEWORK]]` against the ASDLC adoption sequence. Output is intermediate; agent 04c lifts this content into the canonical combined Part 6 + Part 7 file.

**Wave:** Wave 1a. Runs in parallel with 01, 02-l1..l4, 02-g1..g3, 03, 04b, 05a, 07, 08a. Cannot read other agents' outputs.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04a_adoption.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`.

---

## 1. Inputs to read

### 1.1 `[[FRAMEWORK]]` artefacts
Read every source file at `[[FRAMEWORK_VERSION]]`. Quote exact rule text, lifecycle stages, adoption-sequence guidance, and onboarding documentation.

### 1.2 ASDLC adoption corpus (mandatory — abort if missing)

The authoritative sources for ASDLC adoption sequence:

- `asdlc-guide.md` — the implementation guide; recommended adoption sequence; common failure modes; integration guidance with SAFe / ITIL / DORA / regulated SDLC frameworks.
- `asdlc.md` § How to Adopt (`Starting from nothing`, `Already using the manifesto`, `Regulated industry`) — starting points by team posture.
- `asdlc.md` § Tier 4 mechanics — when and how to graduate to Tier 4 envelope operation.
- `annex-igm.md` — Tier 4 + IGM intelligence constraints, governing the four envelope elements.
- `annex-aentm.md` — Tier 4 + AEnt-M relocation mechanics; Tier 3 → Tier 4 graduation event semantics.
- `conformance-profiles.md` — the four ASDLC conformance profiles (Limited / Standard / Regulated / Tier4) used to frame profile fit.
- `annex-adoption-cost.md` — calibrated adoption-cost ranges (FTE uplift, reviewer hours, ceremony cadence) per profile.
- `README.md` § Adoption Path — the 6-step sequence: (1) Establish inner-loop governance, (2) Add SR Gate, (3) Add Release Gate, (4) Add Demand Layer, (5) Add OpReady Gate and runbooks, (6) Add full maintenance governance.

### 1.3 ASDLC layer + gate authoritative artefacts (mandatory)

For each adoption step, read the corresponding authoritative artefact:

| Step | Artefact |
| --- | --- |
| Step 1 — Inner-loop governance | `../manifesto.md`, `../manifesto-principles.md`, `../manifesto-done.md` (resolve via `AGENTIC_MANIFESTO_PATH` or monorepo-adjacent `../`) |
| Step 2 — SR Gate | `specification-readiness.md`, `demand/value.md` |
| Step 3 — Release Gate | `release-governance.md`, `deployment-governance.md` |
| Step 4 — Demand Layer | `demand/value.md`, `demand/intelligence.md`, `demand/metrics.md` |
| Step 5 — OpReady Gate + runbooks | `operations/dod.md`, `operations/governance.md` |
| Step 6 — Full maintenance governance | `maintenance-governance.md`, `security-governance.md`, `devsecops-controls.md` |

### 1.4 Cross-cutting context
- `governance/agents.md` — autonomy tier definitions and the adoption progression's interaction with autonomy tiers.
- `finops-governance.md` — FinOps maturity (Crawl / Walk / Run) aligned to the adoption sequence.

### 1.5 Domain file
Read `[[DOMAIN_FILE]]` in full. Map every gap to specific regulatory provision.

### 1.6 Prior reviews
If `[[PRIOR_REVIEWS]]` is not `none`, note where `[[FRAMEWORK]]` diverges on adoption sequence.

---

## 2. Methodology

### 2.1 Subsection structure

The 6 ASDLC adoption steps are assessed as 6 separate H3 subsections in canonical order, followed by Tier 4 graduation readiness and a conformance-profile-fit assessment:

1. `### step-1-inner-loop` — Establish inner-loop governance (AEM Phase 3 minimum in at least one domain, with evidence bundles and named human accountability)
2. `### step-2-sr-gate` — Add the Specification Readiness Gate
3. `### step-3-release-gate` — Add the Release Gate
4. `### step-4-demand-layer` — Add the Demand Layer
5. `### step-5-opready-gate` — Add the Operational Readiness Gate and runbooks
6. `### step-6-maintenance` — Add full maintenance governance

After the 6 step subsections, include the following **mandatory** sub-sections:

7. `### tier-4-graduation` — Tier 4 envelope graduation readiness (assesses whether `[[FRAMEWORK]]` supports the graduation from Tier 3 to Tier 4 envelope operation per `annex-igm.md` (Tier 4 + IGM intelligence constraints, governing the four envelope elements) and `annex-aentm.md` (Tier 4 + AEnt-M relocation mechanics); this graduation is a separately-governed event per `asdlc.md` § Layer 3 Tier 4 Operation).
8. `### conformance-profile-fit` — Conformance profile assessment per `conformance-profiles.md`.

### 2.2 Per-subsection skeleton

Each subsection MUST have these labelled blocks in this order:

```
### {subsection-slug}

**Alignment grade:** Well-aligned | Partially aligned | Misaligned

**What ASDLC requires.** <one paragraph quoting verbatim from the cited authoritative artefact with file path, summarising what the adoption step demands.>

**What [[FRAMEWORK]] covers.** <one paragraph naming specific [[FRAMEWORK]] artefacts and quoting verbatim from them with file paths. State what is implemented at HEAD; mark roadmapped items as `_[Planned, not operational]_` and exclude from coverage assessment.>

**Gaps.** <bullet list. Each bullet ends with `[Severity: Critical|High|Medium|Low]` per the canonical thresholds in `prompt.md`. Each bullet quotes ASDLC's actual requirement verbatim, then names what is absent or insufficient in [[FRAMEWORK]].>

**[[ORGANIZATION]] implication.** <one paragraph citing at least one regulatory article from `[[DOMAIN_FILE]]` and stating the operational consequence for [[ORGANIZATION]].>
```

### 2.3 Step-1 sub-block (Output Lifecycle & Version Migration)

The Step 1 subsection (`step-1-inner-loop`) MUST contain a sub-subsection `**Output lifecycle & version migration.**` with 4–6 bullets that assess whether `[[FRAMEWORK]]` defines:
- How outputs (specifications, evidence bundles, agent-generated artefacts) are versioned.
- How prior outputs are migrated when ASDLC versions change.
- How outputs are revoked when their underlying claims are invalidated.
- How frozen outputs (artefacts whose underlying claims are still valid but whose framework version has moved on) are governed.

### 2.4 Step-6 sub-block (Decommissioning Readiness)

The Step 6 subsection (`step-6-maintenance`) MUST contain a sub-subsection `**Decommissioning readiness.**` with 3–5 bullets that assess whether `[[FRAMEWORK]]` defines orderly retirement against `maintenance-governance.md`'s decommissioning checklist.

### 2.5 Tier-4-graduation sub-section

The `tier-4-graduation` sub-section MUST include a `**Fundamental incompatibility:**` sub-header IF `[[FRAMEWORK]]` claims Tier 4 support but does not provide the four envelope elements from `annex-igm.md` (the four envelope elements governed under Tier 4 + IGM intelligence constraints) and the relocation mechanics from `annex-aentm.md` (Tier 4 + AEnt-M relocation mechanics). The sub-header is followed by ~3 sentences naming the missing elements and the regulatory consequence (cite at least one article from `[[DOMAIN_FILE]]`).

If `[[FRAMEWORK]]` does not claim Tier 4 support, omit the `**Fundamental incompatibility:**` sub-header and state explicitly: "Framework does not claim Tier 4 support; graduation readiness is not assessed."

### 2.5.1 Conformance-profile-fit sub-section

The `conformance-profile-fit` sub-section assesses how `[[FRAMEWORK]]` maps to ASDLC's four conformance profiles defined in `conformance-profiles.md`. This subsection MUST contain the following labelled blocks:

**Profile identification.** Identify which conformance profile from `conformance-profiles.md` most closely fits `[[FRAMEWORK]]`'s declared scope: ASDLC-Limited (bounded-subset application), ASDLC-Standard (whole production engineering portfolio), ASDLC-Regulated (Standard + domain mapping + regulator-of-record), or ASDLC-Tier4 (Regulated + envelope obligations). Quote the `[[FRAMEWORK]]` scope claim that grounds the identification.

**Scope vs gate-strength clarification.** State explicitly that all four gates (SR, Release, OpReady, Retirement) run at full registry strength under every profile. Profile fit is a scope claim — which systems the framework claims governance over — not a relaxation of gate-condition strength. A framework cannot declare a lighter profile to dilute G1–G4 conditions.

**Profile-conformance attestation test.** Test whether `[[FRAMEWORK]]` provides the artefacts required for a profile-conformance attestation: (i) declared profile, (ii) scope of application, (iii) accountable executive, (iv) attestation cadence, (v) auditor of record. If `[[FRAMEWORK]]` cannot produce a profile-conformance attestation, name the missing artefacts as a bullet list. Each missing-artefact bullet ends with `[Severity: ...]` per the canonical thresholds.

**Adoption-cost grounding.** Cross-reference `annex-adoption-cost.md` for adoption-cost ranges (FTE uplift, reviewer hours, ceremony cadence) corresponding to the identified profile. Use these ranges to ground the realistic ceiling for `[[FRAMEWORK]]` at `[[ORGANIZATION]]`. The ceiling is a profile + a calibrated cost range, not a percentage.

### 2.6 Sources Read footer

Close with an italic `*Sources read: ...*` footer.

### 2.7 Banned soft language
Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`.

### 2.8 Idempotence
Glob output. If exists AND has ≥ 20 lines AND contains all 8 H3 subsection headings (including `conformance-profile-fit`) AND each of the first seven contains the 4 mandatory labelled blocks AND `conformance-profile-fit` contains the four labelled blocks per §2.5.1, exit. Otherwise rewrite.

### 2.9 Machine-readable gap inventory

At end of file before `*Sources read: ...*` footer:

```
<!-- GAP INVENTORY
- subsection: step-1-inner-loop | severity: <severity> | gap_text: <one-line gap summary>
- ... (one line per gap)
-->
```

Agent 04c reads this block to construct the merged gap inventory.

---

## 3. Output structure

### 3.1 File path

```
[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04a_adoption.md
```

### 3.2 H1 heading and metadata

```
# [[FRAMEWORK]] Review 04a — ASDLC Adoption Sequence Alignment (Part 6)

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`

---

## Methodology (brief)

<2–4 sentences naming the adoption corpus read, the framework's source files read, and the assessment approach.>

---

## Part 6 — ASDLC Adoption Sequence Alignment

<8 H3 subsections in canonical order: step-1-inner-loop, step-2-sr-gate, step-3-release-gate, step-4-demand-layer, step-5-opready-gate, step-6-maintenance, tier-4-graduation, conformance-profile-fit. Step-1 through tier-4-graduation each carry the 4 mandatory labelled blocks per §2.2 plus the additional sub-blocks per §2.3, §2.4, §2.5. The conformance-profile-fit subsection follows the structure defined in §2.5.1.>

---

<!-- GAP INVENTORY
- subsection: <name> | severity: <severity> | gap_text: <text>
... (machine-readable; one line per gap)
-->

*Sources read: <enumerate every file actually read>*
```

---

## 4. Hard rules

1. **Read every adoption corpus file and every `[[FRAMEWORK]]` artefact before scoring.**
2. **Each subsection's first non-blank line is `**Alignment grade:**`** (one of Well-aligned / Partially aligned / Misaligned).
3. **Each subsection contains all 4 labelled blocks** (What ASDLC requires; What [[FRAMEWORK]] covers; Gaps; [[ORGANIZATION]] implication).
4. **Step 1 contains the Output Lifecycle & Version Migration sub-block.**
5. **Step 6 contains the Decommissioning Readiness sub-block.**
6. **Tier-4-graduation contains a `**Fundamental incompatibility:**` sub-header** only when [[FRAMEWORK]] claims Tier 4 but cannot provide the four envelope elements; otherwise the section explicitly states no Tier 4 claim.
7. **Every coverage statement names a specific [[FRAMEWORK]] artefact** AND quotes verbatim with file path.
8. **Every gap bullet ends with `[Severity: ...]`.**
9. **Subsection ordering is canonical and must not be re-ordered.**
10. **Date format YYYY-MM-DD** wherever a date appears.
11. **Out-of-scope corpus / tracked-files-only.** Every source file cited MUST be tracked by git on the current branch. Do not read or reference `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.{md,html}`, `agentic-governance-stack.{md,html}`, `manifesto-evolution-plan.{md,html}`, `phase-assessment-checklist.{md,html}`, `aplc-plan*`, or `igm-aent-coherence-review*`. Output MUST contain zero matches for the tokens `APLC`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`. The tokens `IGM`, `AEnt-M`, and `AEnt_M` are permitted ONLY when used as part of the canonical ASDLC annex references (`annex-igm.md`, `annex-aentm.md`) or when paraphrasing the constraints those annexes encode; standalone use referring to external repositories is forbidden.
12. **No `[[DOMAIN_FILE]]` content propagation** beyond cited regulations and risk-types.
13. **Banned soft language** — output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`.
14. **Do not produce a composite [[FRAMEWORK]] score.**
15. **Do not produce Part 7 content** (cross-cutting governance) or the Cross-Document Synthesis. Those are owned by agents 04b and 04c respectively.
16. **Close with italic `*Sources read: ...*` footer.**

---

## 5. Self-check before saving

- [ ] Output file path is `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04a_adoption.md`.
- [ ] All `[[VARIABLE]]` placeholders in the output content are substituted.
- [ ] All 8 subsections are covered in canonical order (step-1-inner-loop, step-2-sr-gate, step-3-release-gate, step-4-demand-layer, step-5-opready-gate, step-6-maintenance, tier-4-graduation, conformance-profile-fit).
- [ ] Every step / tier-4 subsection's first non-blank line is `**Alignment grade:**` with one of the three valid values.
- [ ] Every step / tier-4 subsection contains the 4 mandatory labelled blocks.
- [ ] conformance-profile-fit contains the four labelled blocks per §2.5.1 (Profile identification; Scope vs gate-strength clarification; Profile-conformance attestation test; Adoption-cost grounding) and cross-references both `conformance-profiles.md` and `annex-adoption-cost.md`.
- [ ] step-1-inner-loop contains the Output Lifecycle & Version Migration sub-block (4–6 bullets).
- [ ] step-6-maintenance contains the Decommissioning Readiness sub-block (3–5 bullets).
- [ ] tier-4-graduation contains either a `**Fundamental incompatibility:**` sub-header (when [[FRAMEWORK]] claims Tier 4 but lacks envelope elements) OR an explicit statement that no Tier 4 claim is made.
- [ ] Every gap bullet ends with `[Severity: ...]` matching canonical thresholds.
- [ ] Every coverage statement names a specific [[FRAMEWORK]] artefact AND quotes verbatim from it.
- [ ] At least 3 distinct regulations or risk-types from `[[DOMAIN_FILE]]` are referenced across Part 6.
- [ ] Every regulatory citation includes either an Article number, section number, or named risk-register entry.
- [ ] Every severity label matches canonical thresholds.
- [ ] All dates use YYYY-MM-DD format.
- [ ] Zero matches for any out-of-scope-corpus token (`APLC`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, `igm-aent-coherence-review`) anywhere in the output file. Use of `IGM`, `AEnt-M`, `AEnt_M` is permitted ONLY when bound to the canonical ASDLC annex references (`annex-igm.md`, `annex-aentm.md`) or when paraphrasing the constraints those annexes encode.
- [ ] No banned soft language appears.
- [ ] Output does NOT contain a composite [[FRAMEWORK]] score.
- [ ] Output does NOT contain Part 7 content or the Cross-Document Synthesis.
- [ ] Machine-readable gap inventory HTML comment block is present at end before `*Sources read: ...*` footer.
- [ ] Output closes with italic `*Sources read: ...*` footer.
