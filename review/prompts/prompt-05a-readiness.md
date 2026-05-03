# Sub-prompt 05a — Layer Readiness & Tier 4 Verdict (Part 8 / pre-industry)

**Purpose.** Produce the framework-only Part 8 file for `[[FRAMEWORK]]` — the Layer Readiness Verdict, the Tier 4 envelope assessment, and the gate-level non-negotiables analysis. Output is intermediate; agent 05b lifts this content into the canonical combined Part 8 + Part 9 file.

**Wave:** Wave 1a. Runs in parallel with 01, 02-l1..l4, 02-g1..g3, 03, 04a, 04b, 07, 08a. Cannot read other agents' outputs.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_05a_readiness.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`. Reference; do not redefine.

---

## 1. Inputs to read

### 1.1 `[[FRAMEWORK]]` artefacts
Read every source file at `[[FRAMEWORK_VERSION]]`. Quote exact rule text, gate names, autonomy tier definitions, layer responsibilities, and lifecycle stages.

### 1.2 ASDLC core (mandatory — abort if missing)
- `asdlc.md` — four-layer model, four gates (SR / Release / Operational Readiness / Retirement), feedback paths, ASDLC values. **Tier 4 mechanics live in two annexes**, not in `asdlc.md` itself: `annex-aentm.md` (Tier 4 + AEnt-M relocation mechanics) and `annex-igm.md` (Tier 4 + IGM intelligence constraints — the four envelope elements that previously appeared as the policy-envelope appendix). Read both for the Tier 4 envelope assessment in §2.3.
- `asdlc-guide.md` — recommended adoption sequence, common failure modes.
- `README.md` — entry points, adoption path.

### 1.3 Layer authoritative artefacts (mandatory)
- `governance/gate-registry.yaml` — **single source of truth (canonical machine-readable registry) for every gate's condition count and titles.** All gate-level non-negotiables analysis MUST source counts and condition titles from this YAML registry; any divergence with prose sources (including `governance/gate-registry.md`) is surfaced as an integrity finding.
- `demand/value.md`, `demand/intelligence.md`, `demand/metrics.md`, `specification-readiness.md` — L1 + G1.
- `release-governance.md`, `deployment-governance.md` — L3 + G2 (including foundation-model behavioural-drift cadence and reproducibility surface pinning under Release Gate Condition 1, and four-criterion organisationally-separate validator under Release Gate Condition 2).
- `operations/governance.md`, `operations/dod.md`, `maintenance-governance.md` — L4 + G3, including "Model and Data Drift Detection" benchmark portfolio cadence, drift SLO, drift incident classification, and champion/challenger pattern.
- `agent-control-plane.md` — per-AutonomyTier tool-authorization enforcement-mode requirements (A1..A4) and `ToolAuthorizationRecord` semantics.
- `annex-aentm.md` — Tier 4 + AEnt-M relocation mechanics.
- `annex-igm.md` — Tier 4 + IGM intelligence constraints; the four envelope elements that previously appeared as the policy-envelope appendix in `asdlc.md`.
- `conformance-profiles.md` — Limited / Standard / Regulated / Tier4 profile definitions and per-profile attestation artefacts.
- `annex-adoption-cost.md` — cost-grounded ceiling on credible profile claims.

### 1.4 AEM cross-reference (mandatory for L2 readiness)
- `../manifesto.md`, `../manifesto-principles.md`, `../manifesto-done.md` — L2 inner loop, AEM Phase × tier matrix in P5.

If unreachable and `AGENTIC_MANIFESTO_PATH` is unset, abort.

### 1.5 Cross-cutting governance (mandatory for verdict)
- `governance/agents.md` — autonomy tier definitions; epistemic tier labelling; named accountable human requirements.
- `governance/graph.md` — GateState model.
- `agent-control-plane.md` — named governance agents.
- `waiver-governance.md` — waiver lifecycle and the "exception, not rule" posture.

### 1.6 FinOps + security (read for FinOps Maturity sub-section)
- `finops-governance.md` — FinOps maturity (Crawl / Walk / Run aligned to Phase 1–5 in the FinOps Foundation model).
- `security-governance.md`, `devsecops-controls.md` — security baseline.

### 1.7 Domain file
**This agent does NOT use `[[DOMAIN_FILE]]` in scoring.** The framework-only verdict is produced here; the domain-specific industry assessment is owned by agent 05b. Do NOT name regulations from `[[DOMAIN_FILE]]` in this output. Do NOT name use cases from `[[DOMAIN_FILE]]`. Do NOT propagate any client-specific content. Agent 05b will lift this file's Part 8 verbatim and add Part 9 (industry assessment) below it.

---

## 2. Methodology

### 2.1 Verdict form

State `[[FRAMEWORK]]`'s readiness as a single standalone bold line of the exact form:

```
**ASDLC Readiness: L{N} operating, G{M} routinely passing**
```

Where:
- `{N}` is a single digit 1–4, the highest layer the framework operates with substantial coverage. A layer is "operating" when the framework's evidence supports the layer's core responsibilities (per `prompt-02-layer.md` §4 tests) at ≥ 70% coverage AND the layer's exit gate is at least Partially-met.
- `{M}` is one of `SR`, `Release`, `OpReady`, or `none`. It is the lowest gate the framework can routinely pass (i.e., where ≥ 80% of the gate's pass conditions are enforced — convention does not count). If no gate is routinely passing, use `none`.

**This line is required and machine-readable — agents 05b and 06 will fail to extract it if absent or malformed.** It MUST appear as a standalone bold line with no annotations.

### 2.2 Verdict bounding rule

The verdict is bounded by the **lowest unmet gate**, not by the highest demonstrated capability. A framework that has rich Layer 4 features but cannot routinely pass G1 is bounded at "L1 operating, G1 unmet" until G1 enforcement is in place. Proto-elements of higher layers / gates may be noted in the body but do not raise the verdict line.

### 2.3 Tier 4 envelope assessment (mandatory)

Apply the Tier 4 envelope test from `annex-igm.md` (the four envelope elements relocated from the former policy-envelope appendix in `asdlc.md`). For systems that claim or support Tier 4 autonomy, all four envelope elements MUST be present:

1. **Epistemic-tier-to-action mapping** — for each action class the envelope authorises, the minimum epistemic tier of the claims that must inform that action.
2. **Contradiction-handling rules per type** — for each contradiction type the system's domain produces (jurisdictional divergence, logical contradiction, temporal supersession, scope variation, extraction error), the rule the agent applies.
3. **Decay boundaries per claim class** — for each claim class the system depends on, the decay boundary beyond which the agent must refuse to act.
4. **Feedback-loop closure rules** — the structured feedback the agent must emit when it observes evidence that a claim it acted on was wrong, stale, or contradicted in production.

Per `annex-igm.md` (relocated from the former policy-envelope appendix in `asdlc.md`): "A Tier 4 envelope for an intelligence-bearing system that omits any of the four elements above is not a complete envelope and cannot pass the Release Gate as the envelope specification under Layer 3."

Verdict per element: Met / Partially met / Absent. If `[[FRAMEWORK]]` does not claim Tier 4 support, state explicitly: "Framework does not claim Tier 4 support; envelope elements are not assessed." This is not a deduction — Tier 4 support is optional.

If the framework claims Tier 4 but any element is Absent, state explicitly: "Tier 4 claim is unsupported by complete envelope specification; per `annex-igm.md`, this is ungoverned production autonomy." Do not soften.

In addition to the four envelope elements above, the Tier 4 envelope assessment MUST also produce a Met / Partially met / Absent verdict for each of the following two operational tests. These tests apply to all frameworks that declare any AutonomyTier (not only Tier 4 claimants); they bound the envelope's enforceability in production.

5. **Tool-authorization enforcement mode per AutonomyTier.** Per `agent-control-plane.md` "Enforcement Mechanism" section, the per-tier minimum enforcement modes are:
   - **A1** — post-hoc audit is permitted.
   - **A2** — sandbox OR in-band token is required.
   - **A3** — in-band token AND sandbox are required for side-effecting tools.
   - **A4** — both in-band token AND sandbox are required.

   Test which enforcement mode `[[FRAMEWORK]]` declares per autonomy tier and whether the declared choice meets the per-tier requirement above. Cite the `[[FRAMEWORK]]` artefact that declares the mode (or state explicitly that no evidence was found). A framework whose declared mode is below the per-tier requirement at any tier it claims to support fails this test.

6. **Production drift detection cadence and SLO.** Per `operations/governance.md` "Model and Data Drift Detection" section, an A2+ system MUST define:
   - **Benchmark portfolio cadence** — continuous (A4) / daily (A3) / weekly (A2).
   - **Drift SLO** — 4h (A4) / 24h (A3) / 72h (A2) from drift detection to mitigation or rollback.
   - **Drift incident classification** — drift events MUST be classified as incidents under the operations incident model.
   - **Champion/challenger pattern** — a parallel-evaluation pattern where a challenger model or configuration is scored against the production champion before promotion.

   Test whether `[[FRAMEWORK]]` defines all four sub-elements at the cadence and SLO appropriate to its highest claimed AutonomyTier. Cite the `[[FRAMEWORK]]` artefact (or state explicitly that no evidence was found).

### 2.3.1 Conformance-profile-fit test (mandatory)

After the Tier 4 envelope assessment, identify which conformance profile from `conformance-profiles.md` (`Limited` / `Standard` / `Regulated` / `Tier4`) `[[FRAMEWORK]]` most credibly claims, given the envelope and enforcement evidence assessed above. State the claimed profile as a verdict and answer:

1. Does `[[FRAMEWORK]]` produce the specific artefacts that `conformance-profiles.md` requires for a profile-conformance attestation at the claimed level? Enumerate the artefacts the profile requires; mark each as `present` / `partial` / `absent` with a citation.
2. Does the cost-grounded ceiling in `annex-adoption-cost.md` constrain the profile claim — i.e., does the framework's declared cost or operational footprint place the realistic profile below the claimed level? If so, state the cost-grounded ceiling and name the profile the framework can credibly attest to.

If `[[FRAMEWORK]]` does not declare a conformance profile, state explicitly: "no conformance profile is declared in `[[FRAMEWORK]]`'s source artefacts at `[[FRAMEWORK_VERSION]]`" and assign the profile the evidence supports (default: `Limited`).

### 2.4 Gate-level non-negotiables table

Render as a markdown table (NOT a flat bulleted list) with the exact column headers:

```
| Gate condition | Required to reach next gate level | [[FRAMEWORK]] status | Severity |
```

Use `met` / `partial` / `unmet` in the status column. The "Required to reach next gate level" column states what closes the gap — name the artefact, mechanism, or process. The Severity column uses the canonical thresholds from `prompt.md`.

Include rows for: every G1 condition (9), every G2 condition (8), every G3 condition (8: 7 unconditional plus DoD-8 DR/Failover Tested for blast-radius tier 3) — total 25 rows. (Counts and titles per `governance/gate-registry.yaml`; the literal counts here are derived and must match the registry.) Where `[[FRAMEWORK]]` has scope-gapped a condition, mark status as `*[Scope gap]*` and severity as `Low`.

In addition to the 21 canonical rows, the gate-level non-negotiables table MUST include explicit named tests for the three G2 sub-clauses below. Each is rendered as its own row with a verdict of `met` / `partial` / `unmet` (the verbal form `present` / `partially-present` / `absent` is equivalent and may be used in the body paragraph). These rows feed the gate-level non-negotiables score for G2.

1. **G2 Release Gate Condition 1 — Foundation-model behavioural-drift cadence (sub-clause).** Does `[[FRAMEWORK]]` enforce a re-evaluation cadence for foundation-model behavioural drift independent of any provider version-string change? The default cadence is **7 days for AutonomyTier A2 and above**, **30 days otherwise**. A framework that re-evaluates only when the provider publishes a new version string fails this test. Cite the `[[FRAMEWORK]]` artefact that declares the cadence (or state explicitly that no evidence was found).

2. **G2 Release Gate Condition 1 — Reproducibility surface pinning (sub-clause).** Does `[[FRAMEWORK]]` pin the full reproducibility surface for every release-gated evaluation? The full surface comprises: model id and version, prompt content hash, sampling parameters, tool versions with `ToolAuthorizationRecord` references, retrieval corpus snapshot, random seed, and inference timestamp. A framework that pins a strict subset (e.g., model id only) is `partial`; a framework that pins none is `unmet`. Cite the `[[FRAMEWORK]]` artefact (or state explicitly that no evidence was found).

3. **G2 Release Gate Condition 2 — Four-criterion organisationally-separate validator.** Does `[[FRAMEWORK]]` enforce **all four** of the following independence criteria for the validator that accepts the release evidence:
   - **(a)** no shared first-line manager with the spec analyst,
   - **(b)** no shared compensation pool with the spec analyst,
   - **(c)** no tasking from the spec analyst,
   - **(d)** no contingent accountability — i.e., the validator's accountability is not contingent on the spec analyst's outcome.

   A framework that enforces a strict subset is `partial`; a framework that defines independence by reporting line alone (e.g., "different team") is `unmet`. Cite the `[[FRAMEWORK]]` artefact (or state explicitly that no evidence was found).

### 2.5 Evidence Matrix

Render as a markdown table with rows for all four layers and the three release-bearing gates assessed in this prompt (SR / Release / OpReady — 7 rows total) and the columns:

```
| ASDLC element | Met by [[FRAMEWORK]]? | Authoritative source | Lowest unmet sub-condition |
```

Use `Yes` / `Partially` / `No` in the second column. Cite the authoritative source file path in the third column. The fourth column names the lowest unmet sub-condition for the row (or `n/a` if `Yes`).

### 2.6 Comparison with peer frameworks

If `[[PRIOR_REVIEWS]]` is not `none`, include a `## Comparison with Peer Frameworks` subsection that names each peer and states (a) one ASDLC dimension `[[FRAMEWORK]]` covers more strongly and (b) one dimension it covers less strongly. Otherwise omit.

### 2.7 Economics Assessment (mandatory)

Anchored to category **FS** (FinOps, Security & DevSecOps) and `finops-governance.md`. Four required sub-sections (each 60–120 words):

1. **Model-Tier Selection Maturity** — does `[[FRAMEWORK]]` support per-task model-tier selection (e.g., cheaper model for low-stakes summarisation, premium model for adversarial evaluation)?
2. **Token-Cost Attribution per Workflow** — does `[[FRAMEWORK]]` attribute token cost per workflow / per agent / per evaluation?
3. **Cost-SLO Existence** — does `[[FRAMEWORK]]` define a cost SLO for inference per work unit?
4. **Dynamic Routing Capability** — does `[[FRAMEWORK]]` route tasks to the appropriate model tier based on task class, blast radius, or autonomy tier?

Each sub-section MUST quote verbatim from a named source file with path or state explicitly: "no evidence was found in `[[FRAMEWORK]]`'s source artefacts at `[[FRAMEWORK_VERSION]]`."

### 2.8 Banned soft language
Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`, `use judgment`. Use declarative form.

### 2.9 Idempotence

Glob output. If exists AND has ≥ 20 lines AND contains canonical Verdict line AND has the four required tables / sub-sections, exit. Otherwise rewrite.

---

## 3. Output structure

### 3.1 File path

```
[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_05a_readiness.md
```

### 3.2 Required sections (in order)

```
# [[FRAMEWORK]] Review 05a — Layer Readiness & Tier 4 Verdict

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`

---

## The Verdict

**ASDLC Readiness: L<N> operating, G<M> routinely passing**

<Body paragraph (120–200 words): explain which layers and gates support this verdict. Name the LOWEST unmet gate explicitly. Cite specific [[FRAMEWORK]] artefacts (or absences) demonstrating non-compliance. Note proto-elements of higher layers / gates if present.>

---

## Tier 4 Envelope Assessment

<If [[FRAMEWORK]] does not claim Tier 4 support: one paragraph stating so for the four envelope elements; the two operational tests below remain mandatory. Otherwise: four sub-paragraphs, one per envelope element from `annex-igm.md` (the four envelope elements that previously appeared as the policy-envelope appendix in `asdlc.md`). Each sub-paragraph: name the element, state Met / Partially met / Absent, cite [[FRAMEWORK]] evidence with backticked file path. Conclude with verdict statement on Tier 4 envelope completeness.>

<Then two additional mandatory sub-paragraphs (apply at any AutonomyTier the framework claims, not only Tier 4):

- **Tool-authorization enforcement mode per AutonomyTier** — name the per-tier mode `[[FRAMEWORK]]` declares (post-hoc audit / sandbox / in-band token / both), test against the per-tier minimum from `agent-control-plane.md` (A1 post-hoc audit; A2 sandbox or in-band token; A3 in-band token + sandbox for side-effecting tools; A4 both). Verdict: Met / Partially met / Absent.
- **Production drift detection cadence and SLO** — name the benchmark portfolio cadence (continuous A4 / daily A3 / weekly A2), drift SLO (4h / 24h / 72h), drift incident classification, and champion/challenger pattern that `[[FRAMEWORK]]` defines per `operations/governance.md`. Verdict: Met / Partially met / Absent.>

#### Conformance Profile Fit

<One paragraph identifying which profile from `conformance-profiles.md` (Limited / Standard / Regulated / Tier4) [[FRAMEWORK]] most credibly claims; enumerate required artefacts as present / partial / absent; reference `annex-adoption-cost.md` for the cost-grounded ceiling and state whether it constrains the profile claim downward. If no profile is declared, state so explicitly and assign the profile the evidence supports.>

---

## Evidence Matrix

| ASDLC element | Met by [[FRAMEWORK]]? | Authoritative source | Lowest unmet sub-condition |
|---|---|---|---|
| L1 — Demand & Value | <Yes / Partially / No> | `demand/value.md` | <name or n/a> |
| L2 — Engineering Execution | <Yes / Partially / No> | `../manifesto.md` | <name or n/a> |
| L3 — Release & Deployment | <Yes / Partially / No> | `release-governance.md` | <name or n/a> |
| L4 — Operations & Maintenance | <Yes / Partially / No> | `operations/governance.md` | <name or n/a> |
| G1 — Specification Readiness Gate | <Yes / Partially / No> | `specification-readiness.md` | <name or n/a> |
| G2 — Release Gate | <Yes / Partially / No> | `release-governance.md` | <name or n/a> |
| G3 — Operational Readiness Gate | <Yes / Partially / No> | `operations/dod.md` | <name or n/a> |

---

## Gate-Level Non-Negotiables

| Gate condition | Required to reach next gate level | [[FRAMEWORK]] status | Severity |
|---|---|---|---|
<21 canonical rows: 9 G1 + 5 G2 + 7 G3, in canonical order; followed by 3 additional named-test rows for G2 sub-clauses (foundation-model behavioural-drift cadence; reproducibility surface pinning; four-criterion organisationally-separate validator) per §2.4.>

---

## Comparison with Peer Frameworks

<Include only if [[PRIOR_REVIEWS]] != none. One row per peer with (a) one ASDLC dimension this framework covers more strongly and (b) one dimension it covers less strongly. Omit otherwise.>

---

## Economics Assessment

### Model-Tier Selection Maturity
<60–120 words; verbatim quote from [[FRAMEWORK]] source with backticked file path, OR explicit "no evidence found" statement.>

### Token-Cost Attribution per Workflow
<60–120 words; same form.>

### Cost-SLO Existence
<60–120 words; same form.>

### Dynamic Routing Capability
<60–120 words; same form.>

---
```

---

## 4. Hard rules

- **Read `[[FRAMEWORK]]`'s source files before scoring.** Do not score by analogy.
- **Verdict line is machine-readable.** Must appear as exactly `**ASDLC Readiness: L{N} operating, G{M} routinely passing**` with `{N}` ∈ 1..4 and `{M}` ∈ {SR, Release, OpReady, none}. Standalone bold line. No annotations.
- **Verdict bounded by lowest unmet gate, not highest demonstrated feature.**
- **Do not include Part 9 content.** Industry / client assessment is owned by agent 05b.
- **No `[[DOMAIN_FILE]]` content.** No regulations named, no use cases named, no client-specific content. Agent 05b adds Part 9 below this file's Part 8.
- **No banned soft language** (`consider`, `may`, `could potentially`, `perhaps`, `use judgement`).
- **Out-of-scope corpus / tracked-files-only.** Every source file cited MUST be tracked by git on the current branch. Do not read or reference `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.{md,html}`, `agentic-governance-stack.{md,html}`, `manifesto-evolution-plan.{md,html}`, `phase-assessment-checklist.{md,html}`, `aplc-plan*`, or `igm-aent-coherence-review*`. Output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`.
- **Tier 4 envelope assessment** is mandatory when `[[FRAMEWORK]]` claims Tier 4 support. If the framework does not claim Tier 4, state so explicitly — do not omit the section entirely.

---

## 5. Self-Check Before Writing

- [ ] Output written to `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_05a_readiness.md` (NOT the canonical combined file).
- [ ] Verdict line is a single standalone bold line of the exact form `**ASDLC Readiness: L{N} operating, G{M} routinely passing**` with valid `{N}` and `{M}`.
- [ ] Verdict is bounded by the lowest unmet gate, not the highest demonstrated feature. Body paragraph names at least one unmet gate and cites a specific `[[FRAMEWORK]]` artefact (or absence).
- [ ] Tier 4 Envelope Assessment section is present. If the framework does not claim Tier 4, the section explicitly states so for the four envelope elements. The two operational tests (tool-authorization enforcement mode per AutonomyTier per `agent-control-plane.md`; production drift detection cadence and SLO per `operations/governance.md`) are assessed regardless of Tier 4 claim. If the framework claims Tier 4, all four envelope elements (sourced from `annex-igm.md`) are also assessed.
- [ ] Conformance Profile Fit subsection is present, names the profile from `conformance-profiles.md` (Limited / Standard / Regulated / Tier4) [[FRAMEWORK]] credibly claims, enumerates required artefacts as present / partial / absent, and references `annex-adoption-cost.md` for the cost-grounded ceiling.
- [ ] Gate-Level Non-Negotiables table includes the three additional named-test rows for G2 sub-clauses: foundation-model behavioural-drift cadence (default 7 days A2+, 30 days otherwise); reproducibility surface pinning (model id+version, prompt content hash, sampling parameters, tool versions with ToolAuthorizationRecord references, retrieval corpus snapshot, random seed, inference timestamp); four-criterion organisationally-separate validator ((a) no shared first-line manager, (b) no shared compensation pool, (c) no tasking from spec analyst, (d) no contingent accountability).
- [ ] Evidence Matrix contains rows for all 4 layers and all 3 gates (7 rows). Authoritative source paths are cited.
- [ ] Gate-Level Non-Negotiables table is rendered as a markdown table (NOT a bulleted list) with the canonical column headers and 21 rows (9 G1 + 5 G2 + 7 G3).
- [ ] Economics Assessment is anchored to category **FS** and contains all four required sub-sections (Model-Tier Selection Maturity; Token-Cost Attribution per Workflow; Cost-SLO Existence; Dynamic Routing Capability), each with a verbatim quote or explicit "no evidence found" statement.
- [ ] **No `[[DOMAIN_FILE]]` content is referenced anywhere in the output.** No regulations are named (no SR 11-7, DORA, EU AI Act, GDPR, Solvency II, IDD, HIPAA, etc.). No use cases are named. No client-specific content.
- [ ] No `[[...]]` placeholders remain in the output file.
- [ ] Zero matches for any out-of-scope-corpus token (`APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, `igm-aent-coherence-review`) anywhere in the output file. Every source file referenced is tracked by git on the current branch.
- [ ] No banned soft language (`consider`, `may`, `could potentially`, `perhaps`, `use judgement`) appears anywhere in the output file.
- [ ] Every claim in the output quotes verbatim from a named source file with path, OR states explicitly "no evidence found in [[FRAMEWORK]]'s source artefacts at [[FRAMEWORK_VERSION]]".
