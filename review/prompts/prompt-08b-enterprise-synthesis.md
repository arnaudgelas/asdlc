# Sub-prompt 08b — Enterprise Guardrail Synthesis (canonical Part 14)

**Purpose.** Produce the canonical Part 14 file for `[[FRAMEWORK]]` by lifting §14.1–§14.15 verbatim from agent 08a's intermediate file and adding §14.16 cross-cutting matrix, §14.17 fifteen non-negotiables, §14.18 Agent Card / Task Card schema verification, and §14.19 enterprise maturity verdict.

**Wave:** Wave 1b. Depends on Wave 1a output `_review_08a_domains.md`. Cannot read other Wave 1b outputs.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_08_enterprise_guardrails.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`.

---

## 1. Inputs to read

### 1.1 Mandatory dependency (abort if missing)

- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_08a_domains.md` — must exist, ≥ 20 lines, contain all 15 §14.{N} subsections.

### 1.2 ASDLC core (mandatory)

- `asdlc.md` — for layer/gate framing.
- `governance/agents.md` — for autonomy tier and epistemic tier.
- `agent-control-plane.md` — **the canonical Agent Card / Task Card schema source** for §14.18.
- `governance/graph.md` — GateState model.

### 1.3 Layer + gate authoritative artefacts (read for §14.17 non-negotiables)
- `governance/gate-registry.yaml` — machine-readable single source of truth for gate condition counts, titles, and profile names. The §14.17 non-negotiables for SR Gate / Release Gate / Operational Readiness Gate / Retirement Gate enforcement reference the registry's enumeration. The companion prose `governance/gate-registry.md` paraphrases the YAML.
- `specification-readiness.md`, `release-governance.md`, `operations/dod.md`, `retirement-gate.md` — authoritative prose sources for per-condition narrative (G1, G2, G3, G4 respectively).

### 1.4 Cross-cutting (read for §14.17)
- `waiver-governance.md`, `finops-governance.md`, `security-governance.md`, `devsecops-controls.md`, `agent-control-plane.md` (Enforcement Mechanism per AutonomyTier), `operations/governance.md` (Model and Data Drift Detection cadence and SLO), `asdlc.md` § Termination of recursion (governance-of-governance: named accountable executive).

### 1.5 Domain file
- `[[DOMAIN_FILE]]` — for §14.16 cross-cutting matrix gap entries that cite `[[ORGANIZATION]]` business workflows.

---

## 2. Methodology

### 2.1 Lift mechanics for §14.1–§14.15

Lift §14.1–§14.15 from `_review_08a_domains.md` verbatim, with these heading harmonisations:

- 08a's H1 (`# [[FRAMEWORK]] Review 08a — ...`) is dropped.
- 08a's `## Part 14 (intermediate) — Enterprise Guardrail Domains` heading becomes `## Part 14 — Enterprise Guardrail Domain Coverage` in the canonical file.
- All 15 §14.{N} subsections are preserved verbatim.

### 2.2 §14.16 Cross-cutting matrix (axes: domains × ASDLC layers + gates, plus enforcement rows)

After lifting §14.1–§14.15, insert two markdown tables and three additional cross-cutting enforcement rows.

#### Importance matrix (15 × 8)

Rows: §14.1 through §14.15. Columns: `L1 | G1 | L2 | G2 | L3 | G3 | G4 | L4`. Cells: `H` (high importance), `M` (medium), `L` (low), or empty (not applicable). The importance matrix records which ASDLC layers/gates each domain materially affects. The `G4` column reflects Retirement Gate exposure where the domain has retirement-phase obligations (e.g., §14.2 data classification → data deletion; §14.5 provenance → trace retention beyond retirement; §14.11 data lifecycle → retention/destruction; §14.14 vendor/model governance → model decommissioning).

#### Coverage matrix (15 × 8)

Same structure. Cells reflect `[[FRAMEWORK]]`'s coverage at each layer/gate intersection: `Met` / `Partial` / `Absent` / `*[Scope gap]*`.

#### Cross-cutting enforcement rows

Add a separate small table with three rows that span all layers/gates and are not domain-specific:

| Cross-cutting concern | ASDLC source | Mechanism in `[[FRAMEWORK]]` | Coverage |
|---|---|---|---|
| Retirement Gate enforcement (G4) | `retirement-gate.md`, `governance/gate-registry.yaml` | <verbatim citation or `*[Scope gap]*`> | Met / Partial / Absent / `*[Scope gap]*` |
| Enforcement Mechanism per AutonomyTier (`enforcement_mode`: post-hoc / sandbox / in-band) | `agent-control-plane.md` § Enforcement Mechanism | <verbatim citation or `*[Scope gap]*`> | Met / Partial / Absent / `*[Scope gap]*` |
| Drift Detection cadence + SLO (benchmark portfolio cadence; drift SLO; Drift incident class) | `operations/governance.md` § Model and Data Drift Detection | <verbatim citation or `*[Scope gap]*`> | Met / Partial / Absent / `*[Scope gap]*` |

#### Critical / High gaps

Below the matrices and the cross-cutting enforcement rows, list at least 3 critical/high gaps in this exact format:

```
- **{domain or cross-cutting concern} × {layer/gate}:** {gap description} — affects [[ORGANIZATION]] business workflow `<workflow-name>` (cited verbatim from [[DOMAIN_FILE]]); regulatory exposure: `<article number>`.
```

### 2.3 §14.17 Fifteen Non-Negotiables

**Decision: Option A (extension to fifteen).** The list grows from twelve to fifteen non-negotiables. Items 1–12 are preserved verbatim from the prior canonical list. Items 13–15 reflect post-2025 ASDLC additions: Retirement Gate (G4) formalisation, the `enforcement_mode` field on the Agent Control Plane, and the Drift Detection cadence + SLO in `operations/governance.md`. Rationale: the non-negotiables list is meant to be the comprehensive enforcement floor; the three additions are genuinely non-negotiable for any framework operating production agentic systems under post-2025 ASDLC, and preserving an arbitrary count of twelve would create artificial scarcity and silently drop floor controls. The §14.17 Coverage formula correspondingly becomes `N/15`.

Render as a markdown table with columns:

```
| # | Non-negotiable | ASDLC source | [[FRAMEWORK]] mechanism | Enforcement Level | Severity of gap |
```

The 15 ASDLC non-negotiables (canonical list — items 1–12 are stable; items 13–15 are post-2025 additions; do not modify without an explicit ASDLC change record):

1. **Specification Readiness Gate enforced.** SR Gate is binary; partial pass is fail. Source: `specification-readiness.md`.
2. **Release Gate enforced with tested rollback.** Rollback procedure tested in representative environment within 48 hours of planned production deployment. Source: `release-governance.md`.
3. **Operational Readiness Gate enforced.** All applicable Operational DoD conditions met before production cutover (count and titles per `governance/gate-registry.yaml`; 8 conditions = 7 unconditional plus 1 conditional DoD-8 DR/failover for blast-radius tier 3). Source: `operations/dod.md`, `governance/gate-registry.yaml`.
4. **Named accountable human at each gate boundary.** Per-gate sign-off must be a specific person, not a team or agent. Source: `governance/agents.md`, `release-governance.md`.
5. **Evidence bundle complete and queryable.** Engineering DoD evidence bundle complete; governance graph queryable per `governance/graph.md`. Source: `../manifesto-done.md`, `governance/graph.md`.
6. **Autonomy tier per action class with machine-enforced envelope at Tier 4.** Source: `governance/agents.md`, `asdlc.md` Tier 4 Appendix A.
7. **Epistemic tier labelling on all governance artefacts.** Four tiers: human-authored, tool-generated, agent-proposed-with-human-review, agent-generated. Source: `governance/agents.md`.
8. **Trace retention configured and exercised in non-incident context.** Source: `operations/dod.md` G3 condition 7.
9. **Waiver lifecycle with expiry, debt tracking, portfolio review.** No standing waivers without expiry. Source: `waiver-governance.md`.
10. **Feedback paths closed with evaluation suite update — not just hotfix.** Source: `asdlc.md` § Feedback Paths; `maintenance-governance.md`.
11. **Cost SLO at the inference layer.** Per-task / per-workflow cost SLO with FOCUS-compatible attribution. Source: `finops-governance.md`.
12. **Security scan clean at G3 with SBOM; license compliance confirmed.** Source: `operations/dod.md` G3 conditions 5 + 6; `security-governance.md`.
13. **Retirement Gate (G4) enforced.** Frameworks operating systems with retirement obligations MUST run G4 at the full registry strength enumerated in `governance/gate-registry.yaml`. Frameworks predating retirement formalisation MUST explicitly mark G4 as `Not Applicable` with rationale rather than silently omit it; silent omission is itself a finding. Source: `retirement-gate.md`, `governance/gate-registry.yaml`.
14. **Tool-authorization enforcement mode declared per AutonomyTier.** A1 may use post-hoc; A2 MUST use sandbox or in-band; A3+ MUST use in-band with sandbox for side-effecting tool calls; A4 MUST use both in-band and sandbox. The `enforcement_mode` field MUST be explicit on the Agent Card per AutonomyTier. Source: `agent-control-plane.md` § Enforcement Mechanism.
15. **Production drift detection cadence + SLO.** Benchmark portfolio cadence (continuous for A4; daily for A3; weekly for A2); drift SLO (4 h / 24 h / 72 h time-to-detect respectively); Drift incident class declared and routed. Source: `operations/governance.md` § Model and Data Drift Detection.

For each non-negotiable: cite the authoritative ASDLC source verbatim; name the `[[FRAMEWORK]]` mechanism with backticked file path; mark Enforcement Level as `Enforced (blocks)` / `Enforced (advisory)` / `Convention (documented only)` / `Absent`; map gap severity to canonical thresholds.

**Coverage = N/15** where N is the count of non-negotiables marked `Enforced (blocks)`. **Partial coverage counts as 0** in the formula. State the count explicitly: `**§14.17 Coverage: <N>/15**`. The increase from `N/12` to `N/15` reflects the post-2025 ASDLC additions of Retirement Gate (item 13), Enforcement Mechanism per AutonomyTier (item 14), and Drift Detection cadence + SLO (item 15); state this provenance in the prose preceding the table.

### 2.4 §14.18 Agent Card / Task Card Schema Verification

Render as two markdown tables. The canonical Agent Card and Task Card schema definitions live in `agent-control-plane.md`; cite verbatim.

#### Agent Card schema verification

Required fields per `agent-control-plane.md` (verify the exact field list against the source — the field set below is illustrative):

```
| Schema field | Required by ASDLC? | [[FRAMEWORK]] coverage |
```

Likely fields include: `agent_id`, `version`, `purpose`, `accountable_owner`, `allowed_autonomy_tiers`, `enforcement_mode` (per AutonomyTier; aligns to non-negotiable #14), `allowed_inputs`, `forbidden_inputs`, `allowed_tools`, `forbidden_tools`, `data_access`, `required_logs`, `kill_switch`, `evaluation_record`, `epistemic_tier_floor`, `retirement_obligations` (aligns to non-negotiable #13), `drift_detection_binding` (aligns to non-negotiable #15).

#### Task Card schema verification

Required fields per `agent-control-plane.md`:

```
| Schema field | Required by ASDLC? | [[FRAMEWORK]] coverage |
```

Likely fields include: `task_id`, `requester`, `accountable_owner`, `business_need`, `success_metric`, `acceptance_criteria`, `out_of_scope`, `risk_tier`, `blast_radius`, `data_classification`, `autonomy_tier`, `allowed_repositories`, `allowed_tools`, `allowed_environments`, `max_budget`, `required_evidence`, `rollback_expectation`, `approval_requirements`.

**Schema Coverage Score** = (covered fields / required fields) × 100, computed separately for Agent Card and Task Card. Report both. State explicitly: `**Agent Card Schema Coverage: <pct>%**` and `**Task Card Schema Coverage: <pct>%**`.

#### Verdict enumeration for §14.17 items 13–15

Following the two schema tables, the agent MUST emit an explicit verdict line for each of the three post-2025 non-negotiables (items 13, 14, 15 in §14.17), naming the `[[FRAMEWORK]]` mechanism and Enforcement Level for each. This enumeration is mandatory and machine-readable (agent 09 may extract it for cross-framework comparison):

```
**§14.17 #13 Retirement Gate (G4):** <Enforced (blocks) | Enforced (advisory) | Convention (documented only) | Absent | Not Applicable (with rationale)> — <[[FRAMEWORK]] mechanism with backticked path>.
**§14.17 #14 Enforcement Mechanism per AutonomyTier (`enforcement_mode`):** <Enforced (blocks) | Enforced (advisory) | Convention (documented only) | Absent> — <[[FRAMEWORK]] mechanism with backticked path>.
**§14.17 #15 Drift Detection cadence + SLO:** <Enforced (blocks) | Enforced (advisory) | Convention (documented only) | Absent> — <[[FRAMEWORK]] mechanism with backticked path>.
```

These three verdict lines MUST be present even if the framework's verdict is `Absent` or `Not Applicable`; silence is itself a finding.

### 2.5 §14.19 Enterprise Guardrail Maturity Verdict

Compute three inputs:

1. **Average Domain Coverage** = arithmetic mean of the 15 Domain Coverage Scores from §14.1–§14.15.
2. **§14.17 Non-Negotiables Coverage** = N/15 from §2.3 above (the count of non-negotiables marked `Enforced (blocks)`).
3. **§14.18 Schema Coverage** = average of Agent Card % and Task Card %.

Apply the verdict cascade (precedence order):

- **MATURE** — Average Domain Coverage ≥ 75 AND §14.17 Coverage = 15/15 AND §14.18 Schema Coverage ≥ 80%.
- **ADEQUATE** — Average Domain Coverage ≥ 60 AND §14.17 Coverage ≥ 11/15 AND §14.18 Schema Coverage ≥ 60%.
- **PARTIAL** — Average Domain Coverage ≥ 40 AND §14.17 Coverage ≥ 7/15.
- **LACKING** — otherwise.

Issue the verdict on its own line in the exact form:

```
**Enterprise Guardrail Maturity: <LACKING | PARTIAL | ADEQUATE | MATURE>**
```

This line is required and machine-readable — agent 09 (merge) extracts it for the Executive Verdict.

After the verdict line, add a closing paragraph (120–200 words) titled `**Highest-leverage single investment.**` that names the ONE single change which would advance the framework one verdict step. Cite at least one `[[ORGANIZATION]]` business workflow from `[[DOMAIN_FILE]]` and one regulatory article. Effort label (S/M/L) — XL excluded (the "single investment" must be tractable).

### 2.6 Banned soft language
Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`. Use declarative form.

### 2.7 STOP and report on out-of-scope token
If lifted material from 08a contains any out-of-scope-corpus token, STOP and report — do not silently scrub.

### 2.8 Idempotence
Glob output. If exists AND ≥ 20 lines AND contains all 19 sub-sections (§14.1–§14.15 lifted; §14.16; §14.17 with 15 rows; §14.18 with the three explicit §14.17 #13–#15 verdict lines; §14.19) AND the maturity verdict line is present, exit. Otherwise rewrite.

---

## 3. Output structure

```
# [[FRAMEWORK]] Review 08 — Enterprise Guardrail Synthesis (canonical Part 14)

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`
**Source lifted:** §14.1–§14.15 from `_review_08a_domains.md`

---

## Part 14 — Enterprise Guardrail Domain Coverage

<§14.1 through §14.15 lifted verbatim from 08a, with H1 / Methodology / Sources read dropped>

### §14.16 Cross-cutting Matrix (Domains × ASDLC Layers + Gates)

#### Importance matrix
<15×7 markdown table>

#### Coverage matrix
<15×7 markdown table>

#### Critical / High gaps
<≥ 3 entries in the canonical bullet format>

### §14.17 Fifteen Non-Negotiable Guardrails

<short prose noting Option A: extension to fifteen, with provenance for items 13–15>

| # | Non-negotiable | ASDLC source | [[FRAMEWORK]] mechanism | Enforcement Level | Severity of gap |
|---|---|---|---|---|---|
<15 rows in canonical order>

**§14.17 Coverage: <N>/15**

### §14.18 Agent Card / Task Card Schema Verification

#### Agent Card schema
<table>

**Agent Card Schema Coverage: <pct>%**

#### Task Card schema
<table>

**Task Card Schema Coverage: <pct>%**

**§14.17 #13 Retirement Gate (G4):** <verdict + mechanism>
**§14.17 #14 Enforcement Mechanism per AutonomyTier (`enforcement_mode`):** <verdict + mechanism>
**§14.17 #15 Drift Detection cadence + SLO:** <verdict + mechanism>

### §14.19 Enterprise Guardrail Maturity Verdict

<paragraph stating the three inputs (Average Domain Coverage, §14.17 Coverage, §14.18 Schema Coverage) and the cascade applied>

**Enterprise Guardrail Maturity: <LACKING | PARTIAL | ADEQUATE | MATURE>**

**Highest-leverage single investment.**
<120–200 words naming the single tractable change with [[ORGANIZATION]] workflow + regulation citations + S/M/L effort label>

---
```

---

## 4. Hard rules

1. **Preflight is non-optional.** If `_review_08a_domains.md` is missing, malformed, or does not contain all 15 §14.{N} subsections, STOP and report.
2. **Lift §14.1–§14.15 verbatim.** Heading harmonisation only.
3. **§14.17 is the canonical 15-non-negotiable list (Option A extension).** Items 1–12 are stable; items 13–15 are post-2025 ASDLC additions (Retirement Gate, Enforcement Mechanism per AutonomyTier, Drift Detection cadence + SLO). Do not add, remove, or substitute entries without an explicit ASDLC change record.
4. **§14.18 Agent Card / Task Card schema fields are sourced from `agent-control-plane.md`.** Verify the field set against the source; do not invent fields.
5. **§14.19 maturity verdict is computed from the cascade**, not invented. The verdict line is mandatory and machine-readable.
6. **§14.19 closing paragraph names a tractable single change** (S / M / L; not XL).
7. **Date format YYYY-MM-DD.** British English.
8. **Out-of-scope corpus / tracked-files-only.** Same prohibitions as `prompt.md`. Output MUST contain zero matches for `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`.
9. **Banned soft language.** Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`.
10. **Cross-references** use canonical part numbers.

---

## 5. Self-check before saving

- [ ] Preflight passed: 08a exists, has ≥ 20 lines, contains all 15 §14.{N} subsections.
- [ ] All 15 §14.{N} subsections lifted verbatim from 08a (with H1 / Methodology / Sources dropped).
- [ ] §14.16 contains the importance matrix (15×8), coverage matrix (15×8), the cross-cutting enforcement rows table (Retirement Gate enforcement; Enforcement Mechanism per AutonomyTier; Drift Detection cadence + SLO), and ≥ 3 Critical/High gap entries each citing an `[[ORGANIZATION]]` business workflow and a regulatory article.
- [ ] §14.17 contains exactly 15 non-negotiable rows in canonical order, with prose noting Option A extension and provenance for items 13–15. The `**§14.17 Coverage: <N>/15**` line is present with the correct count.
- [ ] §14.18 contains both Agent Card and Task Card schema verification tables, plus the three explicit verdict lines for §14.17 items 13, 14, and 15. Coverage percentages are stated explicitly for each schema.
- [ ] §14.19 contains the verdict line in the exact form `**Enterprise Guardrail Maturity: <LACKING | PARTIAL | ADEQUATE | MATURE>**` on its own line.
- [ ] §14.19 closing paragraph names a tractable single change (S / M / L) with at least one `[[ORGANIZATION]]` business workflow citation and at least one regulatory article citation.
- [ ] Zero matches for any out-of-scope-corpus token anywhere in the output.
- [ ] No banned soft language appears.
- [ ] All `[[VARIABLE]]` placeholders are substituted.
- [ ] All dates use YYYY-MM-DD format.
