# Sub-prompt 02 — Single Gate Review

**Purpose.** Produce ONE gate-review file for `[[FRAMEWORK]]` against ASDLC gate **G[[GATE_NUMBER]]**. This prompt is invoked 4 times in parallel by the orchestrator, once per gate (G1 through G4).

**Per-invocation parameters (substituted by orchestrator).**
- `[[GATE_NUMBER]]` — integer 1–4.
- `[[GATE_NAME]]` — the canonical short name from `prompt.md`'s gate table (e.g., `Specification Readiness Gate`).

**Placeholder reminder.** Before executing, confirm every `[[VARIABLE]]` token has been substituted by the orchestrator (including `[[GATE_NUMBER]]` and `[[GATE_NAME]]`). If any literal `[[...]]` pattern remains, stop and report.

**Output file.** Write exactly one file: `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_gate_g[[GATE_NUMBER]].md`

**Canonical thresholds.** Severity labels, score ranges, effort labels, and category weightings are defined in `prompt.md`. Reference them; do not redefine.

---

## 1. Inputs to read

Before scoring, read the following in full. Do not score from memory.

### 1.1 `[[FRAMEWORK]]` artefacts
Read every source file that constitutes `[[FRAMEWORK]]` at version `[[FRAMEWORK_VERSION]]`. Include all documentation, rule files, configuration, gating logic, approval-chain definitions, and any pipeline / CI / release-pipeline configuration. Quote exact artefact names, gate names, condition identifiers, and rule text when making claims.

### 1.2 ASDLC core (mandatory — abort if missing)
- `asdlc.md` — four-layer model with gate definitions, gate failure modes, ASDLC values mapping to gates.
- `README.md` — top-level gate definitions and entry points.

### 1.3 Gate-condition source of truth (mandatory — abort if missing)

`governance/gate-registry.yaml` is the canonical, normative, machine-readable enumeration of every ASDLC gate's condition list. **It is the single source of truth for condition counts and condition titles.** Read it first; every condition cited in this output MUST match the registry's count and title verbatim. The companion `governance/gate-registry.md` is the derived human-readable view of the YAML registry; where the two diverge, the YAML file wins.

| Gate | Source of truth (counts + titles) | Authoritative prose source | Summary source (may diverge — surface as integrity finding) |
| --- | --- | --- | --- |
| G1 (`Specification Readiness Gate`) | `governance/gate-registry.yaml` | `specification-readiness.md` | `asdlc.md` § Specification Readiness Gate |
| G2 (`Release Gate`) | `governance/gate-registry.yaml` | `release-governance.md` | `asdlc.md` § Release Gate |
| G3 (`Operational Readiness Gate`) | `governance/gate-registry.yaml` | `operations/dod.md` | `asdlc.md` § Operational Readiness Gate |
| G4 (`Retirement Gate`) | `governance/gate-registry.yaml` | `retirement-gate.md` | `asdlc.md` § Retirement Gate |

**Divergence handling.** Where the authoritative prose source or `asdlc.md`/`README.md` summary text shows a different count or wording than `governance/gate-registry.yaml`, the registry wins. Surface every such divergence as an integrity finding in `## Where it fails ASDLC's bar` — do not silently smooth it over. The registry's existence does not eliminate ASDLC's internal divergences; it makes them auditable.

### 1.4 Adjacent gate context (read for cross-gate failure modes)

| Gate | Adjacent context to read |
| --- | --- |
| G1 | `demand/value.md`, `demand/intelligence.md`, `demand/metrics.md` (these define what the gate's input is) |
| G2 | `release-governance.md`, `deployment-governance.md`, `../manifesto-done.md` (the AEM Engineering DoD is the input to G2) |
| G3 | `operations/governance.md`, `maintenance-governance.md` (these define what the gate's output is) |
| G4 | `retirement-gate.md`, `maintenance-governance.md` (the operational lifecycle that leads INTO retirement), `governance/graph.md` (the seven-state canonical GateState enum used by RT-* conditions) |

### 1.5 Cross-cutting governance (read where directly relevant to the gate)

- `governance/agents.md` — governance agent framework, autonomy tier definitions, epistemic tier labelling. Relevant to all four gates: gate evaluation may be performed by a governance agent at advisory tier, but final gate-pass decisions are accountable-human-only.
- `agent-control-plane.md` — named governance agents and their schemas (including `ToolAuthorizationRecord` referenced by the G2 reproducibility surface).
- `waiver-governance.md` — formal condition waivers and the waiver lifecycle. Relevant to all four gates.
- `governance/queries.md` — canonical governance questions and their data sources. Relevant for understanding how gate state is queryable.
- `finops-governance.md` (G1 mainly) — cost justification at SR Gate.
- `security-governance.md` (G2, G3 mainly) — security scans at release and operational readiness.
- `devsecops-controls.md` (G2 mainly) — DevSecOps pipeline by autonomy tier.

### 1.6 Domain file
Read `[[DOMAIN_FILE]]` in full. Map every major finding to a specific regulation or risk type from `[[INDUSTRY]]` that applies to `[[ORGANIZATION]]`. Domain context is not decoration.

### 1.7 Prior reviews
If `[[PRIOR_REVIEWS]]` is not `none`, read those files for peer comparison. Note where `[[FRAMEWORK]]` diverges from prior-reviewed frameworks on this gate.

---

## 2. Methodology

### 2.1 Scoring
Score this gate 0–100 (integer only, no decimals). Use the canonical weighting and severity thresholds defined in `prompt.md`. State the score in the H1 heading and again in `## Score rationale`. The two MUST match.

The gate score reflects: **does `[[FRAMEWORK]]` enforce or support each of this gate's canonical pass conditions?**

A gate is binary by construction: a partial pass is a fail. The score reflects the proportion of pass conditions that the framework demonstrably enforces, weighted by the operational consequence of each condition for `[[ORGANIZATION]]`.

1. State **evidence-for** (what `[[FRAMEWORK]]` demonstrably does that satisfies a pass condition) separately from **evidence-against** (what is absent, partial, advisory-only, or convention-not-enforcement). evidence-for is captured in `## What works`; evidence-against in `## Where it fails ASDLC's bar`.
2. Quote exact rule text, command names, or artefact names from `[[FRAMEWORK]]` when claiming it enforces (or fails to enforce) a condition. Inline code MUST be enclosed in backticks. You may not cite an artefact you have not read.
3. Distinguish between **enforcement** (the framework blocks progress when the condition fails — pipeline halts, command exits non-zero, gate state is `BLOCKED`) and **convention** (the framework documents the condition but does not technically prevent bypass). A convention is not enforcement. Score conventions lower than enforced conditions.
4. Map the score to a severity label using the threshold table in `prompt.md`.

### 2.2 Pass conditions by gate

The pass-condition counts and titles for every gate are defined by `governance/gate-registry.yaml`. **Do not enumerate counts from this prompt's body** — read the registry, use its enumeration verbatim, and flag any divergence between the registry and the authoritative prose sources (`specification-readiness.md`, `release-governance.md`, `operations/dod.md`, `retirement-gate.md`) or summary sources (`asdlc.md`, `README.md`) as an integrity finding.

| Gate | Source-of-truth file (counts + titles) | Authoritative prose source |
| --- | --- | --- |
| G1 (`Specification Readiness Gate`) | `governance/gate-registry.yaml` | `specification-readiness.md` |
| G2 (`Release Gate`) | `governance/gate-registry.yaml` | `release-governance.md` |
| G3 (`Operational Readiness Gate`) | `governance/gate-registry.yaml` | `operations/dod.md` |
| G4 (`Retirement Gate`) | `governance/gate-registry.yaml` | `retirement-gate.md` |

### 2.3 Tier 4 modification

For systems operating at Tier 4 autonomy, the gate's object changes:
- **G1:** unchanged — the SR Gate still applies to specifications.
- **G2:** the Release Gate applies to the **policy envelope specification**, not to individual deployments within an approved envelope. Subsequent agent-executed deployments within an approved envelope do not require a separate G2 pass. (Reference: `asdlc.md` § Layer 3 Tier 4 Operation.)
- **G3:** the Operational Readiness Gate applies to the envelope's monitoring configuration and steward stewardship arrangement, not to per-action ops readiness.
- **G4:** the Retirement Gate applies at envelope-decommissioning time; agent-executed actions within a now-retired envelope MUST be quiesced as part of the retirement flow.

If `[[FRAMEWORK]]` claims or supports Tier 4, assess the gate's enforcement at the envelope level. State explicitly whether the envelope-level gate is supported.

### 2.4 Per-gate dispatch logic

This sub-prompt is invoked once per gate. The dispatch below names the gate-specific source files to read and the gate-specific score components to test. Read every file named for the active `[[GATE_NUMBER]]` before scoring.

#### 2.4.1 If `[[GATE_NUMBER]]` = 1 (Specification Readiness Gate)

Read `specification-readiness.md` for the prose specification, and `governance/gate-registry.yaml` for the canonical SR-* condition list. Score the gate against the registry's condition enumeration verbatim.

#### 2.4.2 If `[[GATE_NUMBER]]` = 2 (Release Gate)

Read `release-governance.md` for the prose specification, `governance/gate-registry.yaml` for the canonical RG-* condition list, `deployment-governance.md` for the deployment-time application of the gate, and `../manifesto-done.md` for the AEM Engineering Definition of Done that constitutes the input to G2.

In addition to scoring against each registry-listed RG-* condition, the agent MUST evaluate the following named score sub-components introduced by recent extensions to Condition 1 and Condition 2 of `release-governance.md`. Each sub-component receives a separate verdict of `present` / `partially-present` / `absent` with cited evidence, and contributes to the G2 score in proportion to the weighting given by the registry.

##### 2.4.2.1 Foundation-model behavioural-drift cadence (Condition 1 sub-clause)

- Does `[[FRAMEWORK]]` require periodic re-evaluation of the agent's evaluation suite (or a behavioural-equivalence subset) within a defined freshness window — default 7 days for AutonomyTier A2+, 30 days otherwise — regardless of provider version-string change?
- Does the gate fail if the re-run window has elapsed without re-evaluation, even when the provider has issued no version-string change?
- Does `[[FRAMEWORK]]` cite OWASP Agentic AI guidance and NIST AI 600-1 Generative AI Profile (or comparable named authority) as the rationale for monitoring provider-side drift?

Render a verdict of `present` / `partially-present` / `absent` with quoted evidence, and name the cited authority where present.

##### 2.4.2.2 Reproducibility surface (Condition 1 sub-clause)

- Does the evidence bundle record, at the moment evidence was generated, the FULL reproducibility surface: model identifier and version; prompt content hash (Prompt node reference); sampling parameters (temperature, top-p, max-tokens, frequency penalty, presence penalty, any provider-specific parameters); tool versions invoked (with `ToolAuthorizationRecord` references per `agent-control-plane.md`); retrieval corpus snapshot identifier where retrieval is used; random seed where the model API supports seed pinning; inference timestamp?
- Does the deployment configuration assert equality with the evaluated reproducibility surface for every gate-relevant agent invocation?
- Does drift on any field of the reproducibility surface produce a `contradicted` `GateState` (using the canonical seven-state enum from `governance/graph.md` § Canonical Enum Authority) and block the gate?
- Where the provider does not expose a parameter (e.g., closed-source random seeds), is the gap recorded explicitly as part of the surface rather than silently omitted?

Render a verdict of `present` / `partially-present` / `absent` with quoted evidence, and enumerate which surface fields are recorded and which are missing.

##### 2.4.2.3 Four-criterion organisationally-separate independent validator (Condition 2 sub-clause)

`release-governance.md` Condition 2 defines "organisationally separate" through four falsifiable criteria. The agent MUST report a separate verdict — `present` (with evidence) / `absent` (with the specific gap) / `unverifiable` (with the named missing organisational-chart or compensation-pool reference) — for each of the four criteria below:

1. No shared first-line manager with any member of the engineering team that produced the evidence.
2. No shared compensation pool, performance-review pool, or bonus pool with that team.
3. No tasking from the specification analyst.
4. No accountability obligation contingent on the validation outcome being a pass.

Where `[[FRAMEWORK]]`'s "independent validation" claim cannot be verified against all four criteria, mark the claim as `unverified` rather than accepted. If `[[FRAMEWORK]]` cites SR 11-7 effective-challenge or DORA Article 14 independent-testing satisfaction, the four-criterion check is the basis on which that citation is accepted; without it, those regulatory citations are reasonable inferences and not satisfied requirements (per the previous-sprint domain-claim softening to "supports compliance with"). Each criterion contributes as a separate sub-component to the G2 score.

#### 2.4.3 If `[[GATE_NUMBER]]` = 3 (Operational Readiness Gate)

Read `operations/dod.md` for the prose specification, `governance/gate-registry.yaml` for the canonical OR-* condition list, `operations/governance.md` for the operations governance model, and `maintenance-governance.md` for the post-release maintenance lifecycle.

#### 2.4.4 If `[[GATE_NUMBER]]` = 4 (Retirement Gate)

Read `retirement-gate.md` for the prose specification, `governance/gate-registry.yaml` for the canonical RT-1 through RT-8 condition list, and `maintenance-governance.md` for the operational lifecycle that leads INTO retirement (the maintenance-to-retirement transition mechanics).

Score the gate against each of RT-1 through RT-8 in registry order, with the following conditional applicability rules:

- **RT-5 (claim retraction).** If `[[FRAMEWORK]]` operates with intelligence-bearing systems (i.e., systems that publish or rely upon claims analogous to those governed by an intelligence-governance regime), assess RT-5. Otherwise mark RT-5 `Not Applicable` rather than `Failed`, and state explicitly in the row that the framework does not operate with claim-publishing intelligence-bearing systems.
- **RT-6 (first-party-consumer notification).** If `[[FRAMEWORK]]` operates with first-party consumers, assess RT-6. Otherwise mark RT-6 `Not Applicable` rather than `Failed`, and state explicitly in the row that the framework does not have first-party consumers in scope.

For G4 specifically, recognise that most external frameworks predate the formalisation of agent-system retirement. **A framework that does not address retirement is not necessarily failing G4 in the absolute sense — it is silent on a recently-formalised concern.** Score the gate against what the framework provides, but in the Gap Analysis (`## Where it fails ASDLC's bar`) name the absence as a gap to next level rather than as a critical regression. The full G4 weight applies; do not zero the gate, but do not over-penalise structural silence either. State this framing explicitly in `## Score rationale`.

### 2.5 Client-specific mapping
For `## [[ORGANIZATION]]-specific implications`, tie each bullet to a specific regulation or risk type from `[[DOMAIN_FILE]]` and `[[INDUSTRY]]`. Each bullet MUST cite at least one specific regulation, clause number, or risk framework. Generic regulatory references are not acceptable.

### 2.6 Banned soft language
Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`, `use judgment`. Use declarative form (`is`, `is not`, `does not`, `is absent`, `enforces`, `fails to enforce`).

### 2.7 Idempotence (preflight)
Before writing, Glob `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_gate_g[[GATE_NUMBER]].md`. If the file exists AND all of the following hold true, exit without writing:
- File has ≥ 20 lines.
- H1 line matches exactly `# G[[GATE_NUMBER]] — [[GATE_NAME]] | **NN/100**` (with integer score in range 0–100).
- File contains all six required section headings (see §3.3).
- `## Score rationale` section contains `Score: **NN/100**` with integer 0–100 matching H1 score.

Otherwise rewrite from scratch.

---

## 3. Output structure

### 3.1 File path

```
[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_gate_g[[GATE_NUMBER]].md
```

### 3.2 H1 heading — exact format

```
# G[[GATE_NUMBER]] — [[GATE_NAME]] | **{score}/100**
```

The H1 line MUST end with the literal pattern ` | **NN/100**` where `NN` is an integer 0–100. No decimals. No surrounding text after the score. The gate name MUST be character-for-character identical to the corresponding row of `prompt.md`'s gate table.

### 3.3 Required sections (in order)

1. `## What [[FRAMEWORK]] asserts about Gate [[GATE_NUMBER]]`
2. `## Pass-condition coverage table` (mandatory — see §4)
3. `## What works`
4. `## Where it fails ASDLC's bar`
5. `## [[ORGANIZATION]]-specific implications`
6. `## Score rationale`

#### 3.3.1 `## What [[FRAMEWORK]] asserts about Gate [[GATE_NUMBER]]`
One short paragraph (60–120 words). Describe what `[[FRAMEWORK]]` claims or implies about the gate's purpose, mechanism, and enforcement. Quote claims and name artefacts. Cite specific files, commands, or rule identifiers. Use only descriptive verbs.

#### 3.3.2 `## Pass-condition coverage table`
Render as a markdown table with the following columns and one row per canonical pass condition. The row count is taken verbatim from `governance/gate-registry.yaml` for the active `[[GATE_NUMBER]]` (one row per registry-listed condition; for G4 this is RT-1 through RT-8). Use the exact column headers shown:

```
| # | Pass condition | [[FRAMEWORK]] mechanism | Enforcement level | Verdict |
```

- **Pass condition** — quote verbatim from the gate's authoritative source (§1.3) or use the canonical short form from §2.2. Cite the source file path in a footnote-style reference (e.g., `(specification-readiness.md)`).
- **`[[FRAMEWORK]]` mechanism** — name the artefact, command, rule, or schema field. Include backticked file path or identifier. If absent, state `(none)`.
- **Enforcement level** — one of: `Enforced (blocks progress)` / `Enforced (advisory failure flag)` / `Convention (documented only)` / `Absent`.
- **Verdict** — one of: `Met` / `Partially met` / `Absent` / `Not Applicable`. Use `Partially met` only when the framework partially addresses the condition; do not use it as a hedge. Use `Not Applicable` only where this prompt's per-gate dispatch logic (§2.4) explicitly permits it (currently RT-5 and RT-6 in G4 under the named conditional rules).

After the table, write a short paragraph (60–120 words) that summarises the coverage pattern: which conditions are enforced, which are convention-only, which are absent, and what the **lowest covered condition** implies for the gate's operational adequacy. Name the lowest covered condition explicitly.

#### 3.3.3 `## What works`
3–8 bullets. Each bullet MUST:
- Be concrete and evidence-anchored — name the artefact, command, rule, or mechanism with backtick-quoted file path or identifier.
- State what `[[FRAMEWORK]]` does at gate evaluation time, not what it could do.
- Avoid hedging language that obscures whether the capability exists.

#### 3.3.4 `## Where it fails ASDLC's bar`
3–8 bullets. Each bullet MUST:
1. **Quote ASDLC's actual pass condition verbatim** from the gate's authoritative source (§1.3) in double quotes, with the source file path.
2. Show what `[[FRAMEWORK]]` is missing or insufficient — name the specific failure mode (absent, advisory-only, convention-not-enforcement, scope-gap-with-flag, partial-bypass-permitted).
3. Tie to a `[[ORGANIZATION]]`-specific regulatory exposure with a specific article or obligation number.

The verbatim ASDLC quote MUST come first in the bullet — paraphrase is not permitted.

If the gate's authoritative source disagrees with `asdlc.md` summary text, surface the inconsistency as one of these bullets and cite both sources.

#### 3.3.5 `## [[ORGANIZATION]]-specific implications`
3–5 bullets. Each bullet MUST:
- Cite at least one specific regulation, clause number, or risk framework from `[[INDUSTRY]]` / `[[DOMAIN_FILE]]`. Generic references not acceptable.
- Explain the practical consequence for `[[ORGANIZATION]]` of `[[FRAMEWORK]]`'s gate enforcement gap.
- State what `[[ORGANIZATION]]` MUST do to address the gap.

#### 3.3.6 `## Score rationale`
One paragraph. State first: `Score: **{score}/100** ({Severity})`. Then in the same paragraph cite **evidence-for** explicitly (which conditions are enforced and how), THEN **evidence-against** explicitly (which conditions are absent, advisory-only, or convention-only). Reference the lowest covered condition by name.

---

## 4. Pass-condition table — registry as source of truth

Read `governance/gate-registry.yaml` and extract the row set for the gate with number `[[GATE_NUMBER]]`. The registry's enumeration is normative: counts, titles, and ordinal positions are authoritative. The companion `governance/gate-registry.md` is the derived human-readable view; where the two diverge, the YAML file wins.

For each registry-listed condition, render one row in the `## Pass-condition coverage table` (per §3.3.2) in the registry's own order. The "Pass condition" cell text MUST quote the registry's title verbatim (or, where the authoritative prose source uses richer wording, quote the prose source verbatim with the file path; the registry title and the prose source's lead-line title MUST agree — if they do not, surface the divergence as an integrity finding).

**If `[[GATE_NUMBER]]` = 1**, the SR Gate condition count is the registry's count. `asdlc.md` summary text and bullet list have historically diverged (the summary text says one count; the bullet list shows another); cite `governance/gate-registry.yaml` as the resolution. State the registry's count explicitly in `## What works` or `## Where it fails ASDLC's bar`. Surface any persistent divergence between the registry and `asdlc.md` summary text or `README.md` enumerations as an integrity finding in `## Where it fails ASDLC's bar`.

**If `[[GATE_NUMBER]]` = 4**, the Retirement Gate condition count is RT-1 through RT-8 per `governance/gate-registry.yaml`. The conditional applicability rules in §2.4.4 govern the verdict for RT-5 and RT-6: where the framework is out of scope for the condition, the row's verdict is `Not Applicable` and the row text states the basis for that designation. State the registry's RT-* count explicitly in `## What works` or `## Where it fails ASDLC's bar`. Surface any divergence between the registry and `retirement-gate.md` or `asdlc.md` summary text as an integrity finding.

---

## 5. Hard rules

- **Read `[[FRAMEWORK]]`'s source files before scoring.** Do not score by analogy.
- **Use the canonical gate name from `prompt.md`'s gate table** in the H1 heading.
- **Quote exact rule text, command names, or artefact names from `[[FRAMEWORK]]`.** Inline code MUST be enclosed in backticks.
- **Quote each pass condition verbatim from the gate's authoritative source** in `## Where it fails ASDLC's bar`. Paraphrase is not permitted.
- **No praise for undemonstrated capability.** Mark roadmapped capability `_[Planned, not operational]_` and assign it zero score weight.
- **No penalty for out-of-scope problems.** Mark `*[Scope gap]*` explicitly and do not deduct.
- **Convention is not enforcement.** When `[[FRAMEWORK]]` documents a condition without enforcing it (no blocking pipeline step, no command exits non-zero, no `BLOCKED` gate state), label as `Convention (documented only)`. Convention scores lower than enforcement.
- **Surface inconsistencies between authoritative source and `asdlc.md` summary** as integrity findings — do not silently reconcile.
- **Do not compute or report an overall composite score.** That is agent 01's responsibility.
- **Do not include a `Gap to Next Level` section.** That section belongs in Part 8 (agent 05a).
- **YYYY-MM-DD** date format. British English throughout.
- **Cross-references** use canonical part numbers per `prompt.md` (e.g., "see Part 12"). Do not use file names or agent numbers.
- **Score consistency:** the score in `# G[[GATE_NUMBER]] — [[GATE_NAME]] | **{score}/100**` MUST be numerically identical to the score in `## Score rationale`.
- **Out-of-scope corpus.** Do not read or cite `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.{md,html}`, `agentic-governance-stack.{md,html}`, `manifesto-evolution-plan.{md,html}`, `phase-assessment-checklist.{md,html}`, `aplc-plan*`, or `igm-aent-coherence-review*`. Output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`.

---

## 6. Self-check — HARD GATE before saving the file

Each item is binary yes/no. If any item fails, fix the file content and re-verify.

- [ ] Output path is `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_gate_g[[GATE_NUMBER]].md`.
- [ ] H1 line ends with the literal pattern ` | **NN/100**` (single space, single pipe, single space, double-asterisk, integer 0–100, slash, `100`, double-asterisk).
- [ ] H1 gate name is character-for-character identical to the row of `prompt.md`'s gate table for G[[GATE_NUMBER]] (the value substituted into `[[GATE_NAME]]`). The literal string `[[GATE_NAME]]` does not appear.
- [ ] Score in `## Score rationale` is numerically identical to score in H1.
- [ ] Severity label in `## Score rationale` matches the threshold band per `prompt.md`.
- [ ] `## Pass-condition coverage table` is present, has the canonical column headers exactly, and has one row per registry-listed pass condition (count and ordering taken from `governance/gate-registry.yaml` for the gate with number `[[GATE_NUMBER]]`).
- [ ] If `[[GATE_NUMBER]]` = 1: any divergence between `governance/gate-registry.yaml` and `asdlc.md` summary text or `README.md` enumerations is surfaced as an integrity finding in `## Where it fails ASDLC's bar` (or, if the source files now agree, the agreement is stated explicitly).
- [ ] If `[[GATE_NUMBER]]` = 2: the output names a separate, evidence-cited verdict (`present` / `partially-present` / `absent`) for each of (i) the foundation-model behavioural-drift cadence sub-clause (§2.4.2.1, including the 7-day / 30-day freshness window and the OWASP Agentic AI / NIST AI 600-1 citation test), (ii) the reproducibility-surface sub-clause (§2.4.2.2, enumerating which surface fields are recorded and which are missing, and confirming whether drift produces a `contradicted` `GateState`), and (iii) each of the four organisationally-separate criteria (§2.4.2.3) with `present` / `absent` / `unverifiable` per criterion.
- [ ] If `[[GATE_NUMBER]]` = 4: the output names a verdict for each of RT-1 through RT-8 in registry order; RT-5 is marked `Not Applicable` with stated basis where `[[FRAMEWORK]]` does not operate with intelligence-bearing claim-publishing systems (otherwise assessed); RT-6 is marked `Not Applicable` with stated basis where `[[FRAMEWORK]]` has no first-party consumers in scope (otherwise assessed); and `## Score rationale` states explicitly the structural-silence framing (G4 silence is named as a gap to next level rather than as a critical regression, but the gate is not zeroed).
- [ ] No occurrence of `[[` or `]]` anywhere in the file (all placeholders substituted).
- [ ] No occurrence of any out-of-scope-corpus token (see §5).
- [ ] No banned soft-language tokens: `consider`, `may`, `could potentially`, `perhaps`, `use judgement`, `use judgment`.
- [ ] Every bullet in `## What works` and `## Where it fails ASDLC's bar` cites at least one named `[[FRAMEWORK]]` artefact in backticks.
- [ ] Every bullet in `## Where it fails ASDLC's bar` (i) quotes the gate's authoritative pass condition verbatim and (ii) shows what `[[FRAMEWORK]]` is missing.
- [ ] Every bullet in `## [[ORGANIZATION]]-specific implications` cites a specific regulation, article, clause number, or risk framework from `[[DOMAIN_FILE]]`.
- [ ] All dates in `YYYY-MM-DD`. British English throughout.
- [ ] All cross-references use canonical part numbers per `prompt.md`'s part-numbering table; no agent numbers or file names appear in cross-references.
