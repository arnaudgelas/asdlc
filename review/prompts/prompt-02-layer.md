# Sub-prompt 02 — Single Layer Review

**Purpose.** Produce ONE layer-review file for `[[FRAMEWORK]]` against ASDLC layer **L[[LAYER_NUMBER]]**. This prompt is invoked 4 times in parallel by the orchestrator, once per layer (L1 through L4).

**Per-invocation parameters (substituted by orchestrator).**
- `[[LAYER_NUMBER]]` — integer 1–4.
- `[[LAYER_NAME]]` — the canonical short name from `prompt.md`'s layer table (e.g., `Demand & Value`).

**Placeholder reminder.** Before executing, confirm every `[[VARIABLE]]` token has been substituted by the orchestrator (including `[[LAYER_NUMBER]]` and `[[LAYER_NAME]]`). If any literal `[[...]]` pattern remains, stop and report.

**Output file.** Write exactly one file: `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_layer_l[[LAYER_NUMBER]].md`

**Canonical thresholds.** Severity labels, score ranges, effort labels, and category weightings are defined in `prompt.md`. Reference them; do not redefine.

---

## 1. Inputs to read

Before scoring, read the following in full. Do not score from memory.

### 1.1 `[[FRAMEWORK]]` artefacts
Read every source file that constitutes `[[FRAMEWORK]]` at version `[[FRAMEWORK_VERSION]]`. Include all documentation, rule files, configuration, architecture artefacts, and lifecycle definitions. Quote exact artefact names, rule identifiers, and lifecycle stages when making claims.

### 1.2 ASDLC core (mandatory — abort if missing)
- `asdlc.md` — four-layer model, gate definitions, feedback paths, values, ASDLC-vs-APLC distinction.
- `asdlc-guide.md` — recommended adoption sequence, common failure modes, integration guidance.
- `README.md` — top-level entry points and adoption path.
- `governance/agents.md` — governance agent framework, autonomy tier definitions, epistemic tier labelling.

### 1.3 Layer-specific authoritative artefacts

The following artefacts are mandatory reading for L[[LAYER_NUMBER]]:

| Layer | Mandatory artefacts |
| --- | --- |
| L1 (`Demand & Value`) | `demand/value.md`, `demand/intelligence.md`, `demand/metrics.md`, `specification-readiness.md` |
| L2 (`Engineering Execution`) | `../manifesto.md`, `../manifesto-principles.md`, `../manifesto-done.md`, `../glossary.md` (the AEM defines Layer 2; resolve via `AGENTIC_MANIFESTO_PATH` or monorepo-adjacent `../`) |
| L3 (`Release & Deployment`) | `release-governance.md`, `deployment-governance.md` |
| L4 (`Operations & Maintenance`) | `operations/governance.md`, `operations/dod.md`, `maintenance-governance.md` |

Additionally — for **all** layers — read `governance/graph.md`, `governance/queries.md`, and `agent-control-plane.md` (they cut across layers and inform every layer assessment).

If any mandatory artefact for L[[LAYER_NUMBER]] cannot be read, abort and report the missing file.

### 1.4 Layer's exit gate

Each layer except L4 has an exit gate. Each agent reviews its layer's coverage independent of the gate (the gates are reviewed by `prompt-02-gate.md`), but the gate's source artefact must be read because it defines what loop-readiness / release-readiness / op-readiness mean at the layer's boundary.

| Layer | Exit gate (read for context, scored separately by gate agent) |
| --- | --- |
| L1 | Specification Readiness Gate — `specification-readiness.md` |
| L2 | Release Gate — `release-governance.md` |
| L3 | Operational Readiness Gate — `operations/dod.md` |
| L4 | (no exit gate — L4 is governed by ongoing operational SLOs and maintenance signals) |

### 1.5 Tier 4 envelope (mandatory for L2 only; informational for others)

If `[[LAYER_NUMBER]]` is `2`, read `annex-igm.md` (the four envelope elements: epistemic-tier-to-action mapping, contradiction-handling rules per type, decay boundaries per claim class, feedback-loop closure rules) and assess whether `[[FRAMEWORK]]` provides each element. For frameworks operating with relocation mechanics, additionally read `annex-aentm.md` as a secondary reference. For other layers, note Tier 4 envelope coverage only where the layer materially constrains the envelope (e.g., L4 stewardship of envelope adequacy).

### 1.6 Cross-cutting governance (read where directly relevant to the layer)

- `finops-governance.md` — FinOps and inference cost; relevant to L1 (cost justification at SR Gate) and L4 (operational cost tracking).
- `security-governance.md` — security lifecycle; relevant to L2 (build-time security), L3 (release-time scans), L4 (production patching).
- `devsecops-controls.md` — DevSecOps pipeline by autonomy tier; relevant to L2 and L3.
- `waiver-governance.md` — waiver lifecycle; relevant to all layers as a cross-cutting governance mechanism.

### 1.7 Domain file
Read `[[DOMAIN_FILE]]` in full. Map every major finding to a specific regulation or risk type from `[[INDUSTRY]]` that applies to `[[ORGANIZATION]]`. Domain context is not decoration.

### 1.8 Prior reviews
If `[[PRIOR_REVIEWS]]` is not `none`, read those files for peer comparison. Note where `[[FRAMEWORK]]` diverges from prior-reviewed frameworks on this layer.

---

## 2. Methodology

### 2.1 Scoring
Score this layer 0–100 (integer only, no decimals). Use the canonical weighting and severity thresholds defined in `prompt.md` — do NOT re-quote them. State the score in the H1 heading and again in `## Score rationale`. The two MUST match.

The layer score reflects: **does `[[FRAMEWORK]]` cover the responsibilities of L[[LAYER_NUMBER]] as defined by ASDLC?**

1. State **evidence-for** (what `[[FRAMEWORK]]` demonstrably does that satisfies this layer's responsibilities) separately from **evidence-against** (what is absent, partial, or wrong). evidence-for is captured in `## What works`; evidence-against in `## Where it fails ASDLC's bar`.
2. Quote exact rule text, lifecycle stages, artefact filenames, or command names from `[[FRAMEWORK]]`'s own source files when claiming it asserts or fails to assert something. Every claim about `[[FRAMEWORK]]` MUST quote verbatim from a named source file with its path. Paraphrase is not evidence.
3. Do not praise undemonstrated capability. Do not penalise out-of-scope problems — but flag any scope gap explicitly.
4. Map the score to a severity label using the threshold table in `prompt.md`.

### 2.2 Layer scope reminder

| Layer | Core question | Primary stakeholder | Timescale |
| --- | --- | --- | --- |
| L1 (`Demand & Value`) | Is this the right thing to build, and do we know what success looks like? | Product owner and business demand sponsor | Weeks to months |
| L2 (`Engineering Execution`) | Was this built correctly, against the specification, with complete evidence? | Engineering lead and specification analyst | Days to weeks |
| L3 (`Release & Deployment`) | Should this be deployed now, with these authorisations, in this environment state? | Release manager, change authority, accountable human | Hours to days |
| L4 (`Operations & Maintenance`) | Is the system being governed continuously in production? | System steward, SRE/on-call, accountable human | Months to years |

Score `[[FRAMEWORK]]` against the **layer's actual responsibilities** as defined in the layer's authoritative artefacts (§1.3), not against an idealised SDLC.

### 2.3 Client-specific mapping
For `## [[ORGANIZATION]]-specific implications`, tie each bullet to a specific regulation or risk type from `[[DOMAIN_FILE]]` and `[[INDUSTRY]]`. Each bullet MUST cite at least one specific regulation, clause number, or risk framework (e.g., `DORA Art. 9`, `SR 11-7 §IV.A`, `Solvency II Art. 121`, `EU AI Act Art. 12`). Generic regulatory references are not acceptable.

### 2.4 Banned soft language
Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`, `use judgment`. Use declarative form (`is`, `is not`, `does not`, `is absent`, `enforces`, `fails to enforce`).

### 2.5 Idempotence (preflight)
Before writing, Glob `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_layer_l[[LAYER_NUMBER]].md`. If the file exists AND all of the following hold true, exit without writing:
- File has ≥ 20 lines.
- H1 line matches exactly `# L[[LAYER_NUMBER]] — [[LAYER_NAME]] | **NN/100**` (with integer score in range 0–100).
- File contains all six required section headings (see §3.3).
- `## Score rationale` section contains `Score: **NN/100**` with integer 0–100 matching H1 score.

Otherwise rewrite from scratch.

---

## 3. Output structure

### 3.1 File path

```
[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_layer_l[[LAYER_NUMBER]].md
```

### 3.2 H1 heading — exact format

```
# L[[LAYER_NUMBER]] — [[LAYER_NAME]] | **{score}/100**
```

The H1 line MUST end with the literal pattern ` | **NN/100**` where `NN` is an integer 0–100. No decimals. No surrounding text after the score. The layer name MUST be character-for-character identical to the corresponding row of `prompt.md`'s layer table.

### 3.3 Required sections (in order)

1. `## What [[FRAMEWORK]] asserts about Layer [[LAYER_NUMBER]]`
2. `## Layer-specific test` (mandatory — content depends on layer; see §4)
3. `## What works`
4. `## Where it fails ASDLC's bar`
5. `## [[ORGANIZATION]]-specific implications`
6. `## Score rationale`

#### 3.3.1 `## What [[FRAMEWORK]] asserts about Layer [[LAYER_NUMBER]]`
One short paragraph (60–120 words). Describe what `[[FRAMEWORK]]` claims or implies about this layer's responsibilities. Quote claims and name artefacts. Cite specific files, commands, or rule identifiers. Use only descriptive verbs (`asserts`, `claims`, `states`, `provides`); avoid evaluative verbs.

#### 3.3.2 `## Layer-specific test`
Apply the test from §4 matching `[[LAYER_NUMBER]]`. This is mandatory. Reproduce the section title character-for-character.

#### 3.3.3 `## What works`
4–8 bullets. Each bullet MUST:
- Be concrete and evidence-anchored — name the artefact, command, rule, or mechanism with backtick-quoted file path or identifier.
- State what `[[FRAMEWORK]]` does, not what it could do.
- Avoid hedging language that obscures whether the capability exists.

#### 3.3.4 `## Where it fails ASDLC's bar`
4–8 bullets. Each bullet MUST:
1. **Quote ASDLC's actual requirement verbatim** from the layer's authoritative artefacts (§1.3) in double quotes, with the source file path.
2. Show what `[[FRAMEWORK]]` is missing or insufficient — name the specific failure mode (absent, partial, advisory-only, convention-not-enforcement, scope-gap-with-flag).
3. Tie to a `[[ORGANIZATION]]`-specific regulatory exposure with a specific article or obligation number.

The verbatim ASDLC quote MUST come first in the bullet — paraphrase is not permitted.

#### 3.3.5 `## [[ORGANIZATION]]-specific implications`
3–5 bullets. Each bullet MUST:
- Cite at least one specific regulation, clause number, or risk framework from `[[INDUSTRY]]` / `[[DOMAIN_FILE]]`. Generic references not acceptable.
- Explain the practical consequence for `[[ORGANIZATION]]` of `[[FRAMEWORK]]`'s gap or capability on this layer.
- State what `[[ORGANIZATION]]` MUST do to address the gap.

#### 3.3.6 `## Score rationale`
One paragraph. State first: `Score: **{score}/100** ({Severity})`. Then in the same paragraph cite **evidence-for** explicitly, THEN **evidence-against** explicitly. Do not introduce a separate `Evidence` section elsewhere.

---

## 4. Layer-specific test sections (apply only the section matching `[[LAYER_NUMBER]]`)

Place the test section **immediately after** `## What [[FRAMEWORK]] asserts about Layer [[LAYER_NUMBER]]` and **before** `## What works`. Reproduce the section title character-for-character.

### 4.1 If `[[LAYER_NUMBER]]` = 1 — `## Demand & Value Coverage Test`

Assess each of the following responsibilities against `[[FRAMEWORK]]`'s artefacts:

1. **Validated demand.** Does the framework require independent, examinable evidence of business need before engineering work begins? (Reference: `demand/value.md`.)
2. **Measurable value.** Does the framework require a specific, time-bounded, quantitative success criterion with a named owner per initiative? (Reference: `demand/value.md`, `demand/metrics.md`.)
3. **Loop-readiness preparation.** Does the framework prepare specifications such that all 9 SR Gate conditions could be satisfied? (Reference: `specification-readiness.md`.)
4. **Demand intelligence.** Does the framework include a mechanism for surfacing candidate demand items from environmental signals (Layer 0)? (Reference: `demand/intelligence.md`.)
5. **Value realisation feedback (L4 → L1).** Does the framework define how production value data feeds back to demand prioritisation? (Reference: `asdlc.md` § Feedback Paths.)

For each: verdict (Met / Partially met / Absent), followed by a one-to-two sentence explanation citing specific `[[FRAMEWORK]]` evidence with file paths in backticks. If absent, state directly.

### 4.2 If `[[LAYER_NUMBER]]` = 2 — `## Engineering Execution Coverage Test`

Layer 2 is governed by the Agentic Engineering Manifesto (AEM). Assess `[[FRAMEWORK]]`'s coverage of AEM's inner loop:

1. **Agentic Loop coverage.** Does the framework instrument the nine loop phases (Specify → Design → Plan → Execute → Verify → Validate → Observe → Learn → Govern)? (Reference: `../manifesto.md`.)
2. **Engineering DoD.** Does the framework require an evidence bundle satisfying the seven AEM DoD conditions (Shipped, Observable, Verified, Provable, Learned from, Governed, Economical)? (Reference: `../manifesto-done.md`.)
3. **Twelve principles coverage.** Does the framework's design honour the twelve AEM principles, or which ones are absent / contradicted? (Reference: `../manifesto-principles.md`.)
4. **Tier 4 envelope (if framework claims Tier 4).** If the framework supports Tier 4 autonomy, does it provide all four envelope elements from `annex-igm.md`: epistemic-tier-to-action mapping, contradiction-handling rules per type, decay boundaries per claim class, feedback-loop closure rules? Absence of any one element means Tier 4 is "ungoverned production autonomy". For frameworks with relocation mechanics, additionally assess against `annex-aentm.md`. (Reference: `annex-igm.md`; secondary `annex-aentm.md`.)
5. **Validation failures → demand feedback (L2 → L1).** Does the framework define how validation failures (loop builds the wrong thing correctly) feed back to demand layer retrospectives? (Reference: `asdlc.md` § Feedback Paths.)

For each of items 1–5: verdict (Met / Partially met / Absent) plus a one-to-two sentence explanation citing specific `[[FRAMEWORK]]` evidence with file paths in backticks.

#### 4.2.1 Mandatory Release Gate Condition 1 sub-clauses (Layer 2 inner-loop evidence bundle)

The Layer 2 reviewer MUST additionally assess whether `[[FRAMEWORK]]`'s inner-loop evidence bundle records the Release Gate Condition 1 sub-clauses below. Each is scored as a discrete component with a verdict (Present / Partially present / Absent) and one-to-two sentence justification citing specific `[[FRAMEWORK]]` evidence with file paths in backticks. These are score components, not narrative.

6. **Foundation-model behavioural-drift cadence.** Does `[[FRAMEWORK]]` require re-evaluation of the agent's evaluation suite within a defined freshness window — default 7 days for AutonomyTier A2+ and 30 days otherwise — regardless of whether the provider's version-string changed? Cite `release-governance.md` Condition 1's foundation-model-drift sub-clause. Verdict: Present / Partially present / Absent.
7. **Reproducibility surface pinning.** Does `[[FRAMEWORK]]`'s evidence bundle record the full reproducibility surface — model id+version, prompt content hash (referenced as a Prompt node in the governance graph), sampling parameters (temperature, top-p, max-tokens, frequency/presence penalties, provider-specific), tool versions invoked with `ToolAuthorizationRecord` references, retrieval corpus snapshot identifier, random seed where supported, and inference timestamp — and does the deployment configuration assert equality with the evaluated reproducibility surface? Cite `release-governance.md` Condition 1. Verdict: Present / Partially present / Absent.

### 4.3 If `[[LAYER_NUMBER]]` = 3 — `## Release & Deployment Coverage Test`

Assess each of the following responsibilities against `[[FRAMEWORK]]`'s artefacts:

1. **Release approval chain.** Does the framework define an approval chain for production release? (Reference: `release-governance.md`.)
2. **Environment promotion.** Does the framework define environment promotion gates (dev → test → stage → prod)? (Reference: `deployment-governance.md`.)
3. **Feature flag governance.** Does the framework govern feature-flag introduction, expiry, and removal? (Reference: `deployment-governance.md`.)
4. **Tested rollback.** Does the framework require rollback procedure to be **tested** (not merely documented) within 48 hours of deployment, with measured time-to-rollback? (Reference: `release-governance.md`.)
5. **Emergency change procedure.** Does the framework define an emergency-change path with post-hoc evidence requirements? (Reference: `release-governance.md`.)
6. **Release failures → engineering feedback (L3 → L2).** Does the framework define how release-gate failures feed back to the engineering Govern phase? (Reference: `asdlc.md` § Feedback Paths.)

For each: verdict (Met / Partially met / Absent) plus a one-to-two sentence explanation citing specific `[[FRAMEWORK]]` evidence with file paths in backticks.

### 4.4 If `[[LAYER_NUMBER]]` = 4 — `## Operations & Maintenance Coverage Test`

Assess each of the following responsibilities against `[[FRAMEWORK]]`'s artefacts:

1. **Operational observability.** Does the framework define SLOs for service health, output quality rate, reasoning trace completeness, escalation response time, rollback success rate? (Reference: `operations/governance.md`, `operations/dod.md`.)
2. **Incident management.** Does the framework distinguish quality incidents (output-quality failures) from infrastructure / application incidents and define classification? (Reference: `operations/governance.md`.)
3. **System steward.** Does the framework require a named system steward who has actively reviewed the specification and evidence bundle and accepted ongoing accountability? (Reference: `operations/dod.md`, `governance/agents.md`.)
4. **Stewardship transfer.** Does the framework define a stewardship-transfer process when the original steward leaves? (Reference: `maintenance-governance.md`.)
5. **Dependency drift / security patching.** Does the framework define cadence and triggers for dependency updates and security patches? (Reference: `maintenance-governance.md`, `security-governance.md`.)
6. **License compliance.** Does the framework require a license compatibility report against the deployed dependency tree? (Reference: `operations/dod.md`.)
7. **Trace retention.** Does the framework configure trace retention policy for which decisions produce a trace, retention period, format, access path? (Reference: `operations/dod.md`.)
8. **Decommissioning.** Does the framework define controlled retirement (orderly decommissioning checklist)? (Reference: `maintenance-governance.md`.)
9. **Maintenance signals → engineering feedback (L4 → L2).** Does the framework define how maintenance burden, technical debt, and dependency fragility feed back to the engineering Learn / Govern phases with evaluation suite updates? (Reference: `asdlc.md` § Feedback Paths, `maintenance-governance.md`.)
10. **Tier 4 envelope health (if framework claims Tier 4).** Does the framework require continuous monitoring of envelope adequacy and re-gate cycle on environmental change? (Reference: `asdlc.md` Tier 4 in Layer 4.)

For each of items 1–10: verdict (Met / Partially met / Absent) plus a one-to-two sentence explanation citing specific `[[FRAMEWORK]]` evidence with file paths in backticks.

#### 4.4.1 Mandatory Model and Data Drift Detection sub-tests (Layer 4 production-side governance)

The Layer 4 reviewer MUST additionally assess `[[FRAMEWORK]]`'s drift-detection coverage. Each item is scored as a discrete component with a verdict (Present / Partially present / Absent) and one-to-two sentence justification citing specific `[[FRAMEWORK]]` evidence with file paths in backticks.

11. **Production-side benchmark portfolio with cadence by AutonomyTier.** Does `[[FRAMEWORK]]` define a production-side benchmark portfolio whose execution cadence scales with AutonomyTier — continuous at A4, daily at A3, weekly at A2, recommended at A1? Cite `operations/governance.md` "Model and Data Drift Detection" section. Verdict: Present / Partially present / Absent.
12. **Drift SLO by AutonomyTier.** Does `[[FRAMEWORK]]` define a drift SLO of 4h at A4, 24h at A3, 72h at A2? Cite `operations/governance.md` "Model and Data Drift Detection" section. Verdict: Present / Partially present / Absent.
13. **Drift incident classification.** Does `[[FRAMEWORK]]` define a Drift incident class distinct from Quality, Infrastructure, and Security incident classes? Cite `operations/governance.md` "Model and Data Drift Detection" section. Verdict: Present / Partially present / Absent.
14. **Champion/challenger pattern.** Does `[[FRAMEWORK]]` define a champion/challenger pattern for foundation-model-backed systems? Cite `operations/governance.md` "Model and Data Drift Detection" section. Verdict: Present / Partially present / Absent.

---

## 5. Hard rules

- **Read `[[FRAMEWORK]]`'s source files before scoring.** Do not score by analogy.
- **Use the canonical layer name from `prompt.md`'s layer table** in the H1 heading (the value of `[[LAYER_NAME]]` is taken from there).
- **Quote exact rule text, command names, or artefact names from `[[FRAMEWORK]]`** when claiming it asserts (or fails to assert) something. Inline code MUST be enclosed in backticks. You may not cite an artefact you have not read or located via Read/Grep/Glob.
- **No praise for undemonstrated capability.** Mark roadmapped capability `_[Planned, not operational]_` and assign it zero score weight.
- **No penalty for out-of-scope problems.** Mark `*[Scope gap]*` explicitly and do not deduct.
- **Do not compute or report an overall composite score.** That is agent 01's responsibility.
- **Do not include a `Gap to Next Level` section.** That section belongs in Part 8 (agent 05a).
- **YYYY-MM-DD** date format. British English throughout.
- **Cross-references** use canonical part numbers per `prompt.md` (e.g., "see Part 12"). Do not use file names or agent numbers.
- **Score consistency:** the score in `# L[[LAYER_NUMBER]] — [[LAYER_NAME]] | **{score}/100**` MUST be numerically identical to the score in `## Score rationale`. Resolve before saving.
- **Cross-file coordination:** agent 01 is the AUTHORITATIVE consumer of this score for Part 1. Agent 09 (merge) detects mismatches.
- **Out-of-scope corpus.** Do not read or cite `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.{md,html}`, `agentic-governance-stack.{md,html}`, `manifesto-evolution-plan.{md,html}`, `phase-assessment-checklist.{md,html}`, `aplc-plan*`, or `igm-aent-coherence-review*`. Output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`. **Exception:** the ASDLC-tracked annexes `annex-aentm.md` and `annex-igm.md` are part of ASDLC and MUST be read when assessing Tier 4 envelope obligations (especially when `[[LAYER_NUMBER]]` = 2). Cite them by filename only; paraphrase any imported cross-stack terminology to ASDLC-equivalent vocabulary so the bare banned tokens never appear in the output prose.
- **Do not propagate `[[DOMAIN_FILE]]` content forward beyond what is needed for layer-level regulatory citation.** Do not embed full domain-file passages, do not derive APLC roadmaps, and do not invent domain bridges that are not present in `[[DOMAIN_FILE]]`.
- **L2 cross-reference.** L2 review (`[[LAYER_NUMBER]]` = 2) requires AEM source artefacts. If `../manifesto.md` is unreachable and `AGENTIC_MANIFESTO_PATH` is unset, abort and report.

---

## 6. Self-check — HARD GATE before saving the file

Each item is binary yes/no. If any item fails, fix the file content and re-verify.

- [ ] Output path is `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_layer_l[[LAYER_NUMBER]].md`.
- [ ] H1 line ends with the literal pattern ` | **NN/100**` (single space, single pipe, single space, double-asterisk, integer 0–100, slash, `100`, double-asterisk).
- [ ] H1 layer name is character-for-character identical to the row of `prompt.md`'s layer table for L[[LAYER_NUMBER]] (the value substituted into `[[LAYER_NAME]]`). The literal string `[[LAYER_NAME]]` does not appear.
- [ ] Score in `## Score rationale` is numerically identical to score in H1.
- [ ] Severity label in `## Score rationale` matches the threshold band per `prompt.md`.
- [ ] Layer-specific test section is present immediately after `## What [[FRAMEWORK]] asserts about Layer [[LAYER_NUMBER]]` and matches the title from §4 verbatim.
- [ ] If `[[LAYER_NUMBER]]` = 2: AEM source artefacts (`../manifesto.md`, `../manifesto-principles.md`, `../manifesto-done.md`) have been read and are cited at least once each.
- [ ] No occurrence of `[[` or `]]` anywhere in the file (all placeholders substituted).
- [ ] No occurrence of any out-of-scope-corpus token (see §5).
- [ ] No occurrence of any prior-framework name (e.g., from `[[PRIOR_REVIEWS]]`) unless `[[FRAMEWORK]]` itself resolves to that name.
- [ ] No banned soft-language tokens: `consider`, `may`, `could potentially`, `perhaps`, `use judgement`, `use judgment`.
- [ ] Every bullet in `## What works` and `## Where it fails ASDLC's bar` cites at least one named `[[FRAMEWORK]]` artefact in backticks.
- [ ] Every bullet in `## Where it fails ASDLC's bar` (i) quotes ASDLC's actual requirement verbatim from a layer authoritative artefact and (ii) shows what `[[FRAMEWORK]]` is missing.
- [ ] Every bullet in `## [[ORGANIZATION]]-specific implications` cites a specific regulation, article, clause number, or risk framework from `[[DOMAIN_FILE]]`.
- [ ] All dates in `YYYY-MM-DD`. British English throughout.
- [ ] All cross-references use canonical part numbers per `prompt.md`'s part-numbering table; no agent numbers or file names appear in cross-references.
