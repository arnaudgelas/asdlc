# Sub-prompt 04b — Cross-cutting Governance Alignment (Part 7)

**Purpose.** Produce the Part 7 file for `[[FRAMEWORK]]` against the ASDLC cross-cutting governance corpus. Output is intermediate; agent 04c lifts this content into the canonical combined Part 6 + Part 7 file.

**Wave:** Wave 1a. Runs in parallel with 01, 02-l1..l4, 02-g1..g3, 03, 04a, 05a, 07, 08a. Cannot read other agents' outputs.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04b_governance.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`.

---

## 1. Inputs to read

### 1.1 `[[FRAMEWORK]]` artefacts
Read every source file at `[[FRAMEWORK_VERSION]]`. Quote exact rule text, schema fields, governance agent definitions, autonomy tier rules, waiver lifecycle, and observability instrumentation.

### 1.2 ASDLC cross-cutting governance corpus (mandatory — abort if any missing)

The five governance documents that define ASDLC's cross-cutting governance posture:

1. `governance/agents.md` — governance agent framework, autonomy tier definitions, epistemic tier labelling, governance-agent accountability.
2. `governance/graph.md` — semantic governance graph: node types, edge types, GateState model, continuous governance state inspection.
3. `governance/queries.md` — canonical governance questions and their authoritative data sources.
4. `agent-control-plane.md` — named governance agents, schemas, human decision points.
5. `waiver-governance.md` — waiver lifecycle, expiry requirements, debt tracking, portfolio-level waiver oversight.

These documents collectively constitute Part 7's source material. Agent 04b assesses how `[[FRAMEWORK]]` aligns with each.

### 1.3 ASDLC core (mandatory)
- `asdlc.md` — § Governance of Governance (the meta-governance posture, including the "Termination of recursion" paragraph naming the accountable executive who accepts residual risk on the governance infrastructure); § Governance Agents.
- `asdlc-guide.md` — adoption sequence implications for governance.
- `governance/gate-registry.yaml` — machine-readable canonical gate registry (source of truth for gate IDs, conditions, and severity).
- `freshness-register.yaml` and `freshness-register.md` — canonical register of external authorities (NIST, OWASP, EU AI Act, DORA, etc.) with `version`, `last_verified`, `next_review_due`, and `owner` fields.

### 1.4 AEM cross-reference (when `[[FRAMEWORK]]` is governance-adjacent)
- `../manifesto-principles.md` — particularly P9 (observability covers reasoning), P12 (accountability requires intelligibility), P10 (assume emergence, engineer containment) — which set the governance bar that ASDLC inherits and extends.

### 1.5 Domain file
Read `[[DOMAIN_FILE]]` in full. Map every gap to specific regulatory provision.

### 1.6 Prior reviews
If `[[PRIOR_REVIEWS]]` is not `none`, note where `[[FRAMEWORK]]` diverges on governance.

---

## 2. Methodology

### 2.1 Subsection structure

Each of the 5 governance documents is assessed as a separate H3 subsection in canonical order:

1. `### governance-agents` — alignment to `governance/agents.md`
2. `### governance-graph` — alignment to `governance/graph.md`
3. `### governance-queries` — alignment to `governance/queries.md`
4. `### agent-control-plane` — alignment to `agent-control-plane.md`
5. `### waiver-governance` — alignment to `waiver-governance.md`

### 2.2 Per-subsection skeleton

Each subsection MUST have these labelled blocks in this order:

```
### {subsection-slug}

**Alignment grade:** Well-aligned | Partially aligned | Misaligned

**What the document requires.** <one paragraph quoting verbatim from the cited governance document with its file path, summarising what ASDLC requires of any framework that operates governance.>

**What [[FRAMEWORK]] covers.** <one paragraph naming specific [[FRAMEWORK]] artefacts and quoting verbatim from them with file paths. State what is implemented; do not state what is roadmapped (mark roadmap as `_[Planned, not operational]_` and exclude from coverage assessment).>

**Gaps.** <bullet list. Each bullet ends with `[Severity: Critical|High|Medium|Low]` per the canonical thresholds in `prompt.md`. Each bullet quotes ASDLC's actual requirement verbatim from the governance document, then names what is absent or insufficient in [[FRAMEWORK]].>

**Contradictions.** <bullet list. Each bullet identifies a place where [[FRAMEWORK]]'s behaviour explicitly contradicts or undermines the governance document's guidance. If none identified, the entire block reads exactly: `**Contradiction:** None identified.`>

**[[ORGANIZATION]] implication.** <one paragraph citing at least one regulatory article from `[[DOMAIN_FILE]]` and stating the operational consequence for [[ORGANIZATION]].>
```

### 2.3 Contradictions — distinct from gaps

A **gap** is "[[FRAMEWORK]] does not address X". A **contradiction** is "[[FRAMEWORK]] explicitly does Y, where Y conflicts with ASDLC requirement X". The Contradictions block is mandatory; if none exist, state `**Contradiction:** None identified.` — never omit the block.

Candidate contradiction patterns:
- Default autonomy tier higher than what `governance/agents.md` permits without machine-enforced envelope.
- Governance agent output treated as gate-passing without documented human review (contradicts the epistemic tier framework in `governance/agents.md`).
- Waivers without expiry, accountable human, or debt tracking (contradicts `waiver-governance.md`).
- GateState not queryable / not exposed to external observers (contradicts `governance/graph.md`).
- Governance graph drift not surfaced as an integrity finding (contradicts `governance/queries.md`).

### 2.4 Mandatory cross-cutting tests

In addition to the per-document subsections, the Part 7 output MUST include the following three cross-cutting tests. Place each test as a labelled bullet block inside the most relevant per-document subsection (governance-agents for the recursion-termination test; governance-graph for the canonical-enum test; governance-queries for the freshness-register test) OR, if none of the five subsections is the natural home, append a final H3 sub-section `### cross-cutting-tests` after `waiver-governance` carrying these three tests.

**Test 1 — Governance-of-governance termination of recursion** (anchored to `asdlc.md` § Governance of Governance, "Termination of recursion" paragraph).

- Does `[[FRAMEWORK]]` define a named accountable executive who holds residual-risk acceptance on the framework's own governance infrastructure?
- Is the acceptance renewed on a defined cadence (recommended: quarterly, aligned to the operational-DoD-review cadence)?
- Is the acceptance recorded as a governance artefact (an EvidenceArtifact with an `approved_by` edge to a HumanOwner, or equivalent) with a verifiable trace to a named human?
- A framework with no named residual-risk-acceptance executive is in unbounded governance recursion — name this as a gap with `[Severity: ...]` per canonical thresholds.

**Test 2 — Canonical Enum Authority** (anchored to `governance/graph.md` § Canonical Enum Authority).

- Does `[[FRAMEWORK]]` define a canonical state enum for governance assertions (the seven-state GateState model: pass, fail, missing, stale, contradicted, waived, requires-human-decision, or an equivalent)?
- Is the enum authoritatively documented in a single source-of-truth document?
- Does the framework forbid silent introduction of new enum values without a major-version registry update?
- Does the framework express compound conditions (e.g., "waived AND waiver expiry > now()") as derived predicates rather than as new enum values (e.g., a forbidden compound state like "waived-with-current-waiver")?
- A framework that admits ad-hoc enum extension or compound enum values is in registry drift — name this as a gap with `[Severity: ...]`.

**Test 3 — Authority freshness register** (anchored to `freshness-register.yaml` and `freshness-register.md`).

- Does `[[FRAMEWORK]]` track the external authorities its claims depend on (e.g., NIST AI RMF, OWASP, EU AI Act, DORA, ISO standards)?
- Is each authority tagged with a version, a last-verified date, and a `next_review_due` date?
- Is each authority assigned to a named owner role responsible for re-verification?
- A framework that cites NIST AI RMF 1.0 or DORA Article 14 without an external authority freshness register is exposed to silent regulatory drift — name this as a gap with `[Severity: ...]` per canonical thresholds.

### 2.5 Sources Read footer

Close the output with an italic `*Sources read: ...*` footer enumerating every source file actually read. Include every governance document plus every `[[FRAMEWORK]]` artefact cited.

### 2.6 Banned soft language
Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`. Make falsifiable statements grounded in cited artefacts.

### 2.7 Idempotence

Glob output. If exists AND has ≥ 20 lines AND contains all 5 H3 subsection headings AND each subsection has all 5 mandatory labelled blocks AND the three cross-cutting tests from §2.4 are present, exit. Otherwise rewrite.

### 2.8 Machine-readable gap inventory

At end of file, before the `*Sources read: ...*` footer, embed a machine-readable HTML comment block in this exact form:

```
<!-- GAP INVENTORY
- subsection: governance-agents | severity: <severity> | gap_text: <one-line gap summary>
- subsection: governance-graph | severity: <severity> | gap_text: <one-line gap summary>
- ... (one line per gap; subsections may have multiple gaps)
-->
```

Agent 04c reads this block to construct the merged gap inventory.

---

## 3. Output structure

### 3.1 File path

```
[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04b_governance.md
```

### 3.2 H1 heading and metadata

```
# [[FRAMEWORK]] Review 04b — Cross-cutting Governance Alignment (Part 7)

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`

---

## Methodology (brief)

<2–4 sentences naming the 5 governance documents read, the framework's source files read, and the assessment approach. Do not duplicate prompt.md or this prompt's content.>

---

## Part 7 — Cross-cutting Governance Alignment

<5 H3 subsections in canonical order: governance-agents, governance-graph, governance-queries, agent-control-plane, waiver-governance. Each with the 5 mandatory labelled blocks per §2.2.>

---

<!-- GAP INVENTORY
- subsection: <name> | severity: <severity> | gap_text: <text>
... (machine-readable; one line per gap)
-->

*Sources read: <enumerate every file actually read>*
```

---

## 4. Hard rules

These rules apply without exception.

1. **Read every governance document and every `[[FRAMEWORK]]` artefact before scoring.** Do not score by analogy.
2. **Each subsection's first non-blank line is `**Alignment grade:** Well-aligned` / `Partially aligned` / `Misaligned`** (one of these three values exactly).
3. **Each subsection contains all 5 labelled blocks in canonical order** (What the document requires, What [[FRAMEWORK]] covers, Gaps, Contradictions, [[ORGANIZATION]] implication).
4. **Contradictions block is mandatory** — even when none exist (`**Contradiction:** None identified.`).
5. **Every coverage statement names a specific [[FRAMEWORK]] artefact** (file path, command name, rule, module) AND quotes verbatim from that artefact.
6. **Every gap bullet ends with `[Severity: <Critical|High|Medium|Low>]`** per canonical thresholds.
7. **Subsection ordering is canonical and must not be re-ordered.**
8. **Date format YYYY-MM-DD** wherever a date appears.
9. **Out-of-scope corpus / tracked-files-only.** Every source file cited MUST be tracked by git on the current branch. Do not read or reference `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.{md,html}`, `agentic-governance-stack.{md,html}`, `manifesto-evolution-plan.{md,html}`, `phase-assessment-checklist.{md,html}`, `aplc-plan*`, or `igm-aent-coherence-review*`. Output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`.
10. **No `[[DOMAIN_FILE]]` content propagation** beyond cited regulations and risk-types.
11. **Banned soft language** — output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`.
12. **Do not produce a composite [[FRAMEWORK]] score.** Part 1 is owned by agent 01.
13. **Do not produce Part 6 content** (adoption alignment) or the Cross-Document Synthesis. Those are owned by agents 04a and 04c respectively.
14. **Close the output file with an italic `*Sources read: ...*` footer** listing every source file actually read.

---

## 5. Self-check before saving

**Do not save the output file until every item below is confirmed.**

- [ ] Output file path is `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04b_governance.md`.
- [ ] All `[[VARIABLE]]` placeholders in the output content are substituted.
- [ ] All 5 governance documents are covered, each as a separate H3 subsection in canonical order (governance-agents, governance-graph, governance-queries, agent-control-plane, waiver-governance).
- [ ] Every subsection's first non-blank line is `**Alignment grade:** Well-aligned` / `Partially aligned` / `Misaligned`.
- [ ] Every subsection contains all 5 labelled blocks (What the document requires; What [[FRAMEWORK]] covers; Gaps; Contradictions; [[ORGANIZATION]] implication).
- [ ] Every gap bullet ends with `[Severity: ...]` matching canonical thresholds.
- [ ] Every coverage statement names a specific [[FRAMEWORK]] artefact AND quotes verbatim from it.
- [ ] Every Contradictions block is present (or states `**Contradiction:** None identified.`).
- [ ] The three §2.4 cross-cutting tests are present: Termination of recursion (named accountable executive on governance-of-governance, renewed on a defined cadence, recorded as a governance artefact); Canonical Enum Authority (seven-state GateState; single source-of-truth; no silent enum extension; compound conditions expressed as derived predicates); authority freshness register (external authorities tracked with version, last-verified, next_review_due, named owner).
- [ ] At least 3 distinct regulations or risk-types from `[[DOMAIN_FILE]]` are referenced across Part 7. No single regulation accounts for the majority of subsections.
- [ ] Every regulatory citation includes either an Article number, section number, or named risk-register entry.
- [ ] Every severity label matches the canonical thresholds from `prompt.md`.
- [ ] All dates use YYYY-MM-DD format.
- [ ] Zero matches for any out-of-scope-corpus token (`APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, `igm-aent-coherence-review`) anywhere in the output file. Every cited source file is tracked by git on the current branch.
- [ ] No banned soft language (`consider`, `may`, `could potentially`, `perhaps`, `use judgement`) appears.
- [ ] Output does NOT contain a composite [[FRAMEWORK]] score.
- [ ] Output does NOT contain Part 6 content or the Cross-Document Synthesis.
- [ ] Machine-readable gap inventory HTML comment block is present at end of file before the `*Sources read: ...*` footer.
- [ ] Output closes with italic `*Sources read: ...*` footer enumerating every source file actually read.
