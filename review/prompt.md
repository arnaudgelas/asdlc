# Framework Review — Master Orchestration Prompt (ASDLC alignment)

> **Status: Phase 1 + Phase 2 complete; Phase 3 (alignment with the post-sprint ASDLC additions) is landing in this commit bundle.**
> The orchestrator below and the sub-prompts under `prompts/` were retargeted from the Agentic Engineering Manifesto (AEM) review system to the Agentic Software Delivery Lifecycle (ASDLC) in Phases 1–2. Phase 3, applied here, brings the orchestrator into alignment with the canonical post-sprint ASDLC additions made after the prior sprint, namely:
>
> - Four gates including the Retirement Gate G4.
> - YAML-canonical gate registry (`governance/gate-registry.yaml` is the machine-readable source of truth; `governance/gate-registry.md` is the derived human-readable view).
> - Foundation-model drift sub-clause and reproducibility surface in Release Gate Condition 1.
> - Four-criterion organisationally-separate definition in Release Gate Condition 2.
> - Tool-authorization enforcement modes per AutonomyTier.
> - Production drift detection cadences.
> - Governance-of-governance termination.
> - Canonical seven-state `GateState` enum.
> - Conformance-profile renaming (Limited / Standard / Regulated / Tier4).
> - New domains (`sox`, `hipaa`, `ccpa`, `eu-ai-act-mapping`).
>
> **Self-referential-grading disclaimer.** This review system grades external
> frameworks against ASDLC's own assertions, not against externally-anchored
> regulatory or engineering source-of-truth. When the review system flags a gap
> in `[[FRAMEWORK]]` against an ASDLC condition, the operator must additionally
> verify that ASDLC's own claim against the underlying regulatory or engineering
> source is itself sound. The review system does not perform that outer
> verification.

**Variables (replace before running):**
- `[[FRAMEWORK]]` — framework name as it appears in its own documentation (e.g., `ABCD`)
- `[[FRAMEWORK_LOWER]]` — lowercase slug using **underscores only** (no hyphens, no spaces) for file/directory naming (e.g., `abcd`)
- `[[FRAMEWORK_VERSION]]` — version, tag, or commit hash if known (e.g., `v1.2.0` or `HEAD`); use `unknown` if not versioned
- `[[ORGANIZATION]]` — client organisation name (e.g., `ABCD.xyz`)
- `[[INDUSTRY]]` — industry and regulatory context (e.g., `European insurance and financial services — SR 11-7, DORA, EU AI Act, GDPR, Solvency II`)
- `[[DOMAIN_FILE]]` — path to the relevant industry domain file (e.g., `domains/insurance.md`); must match an existing file under `domains/` in the ASDLC repository
- `[[PRIOR_REVIEWS]]` — comma-separated paths to prior review files for peer comparison, or `none` (e.g., `abcd/abcd_asdlc_alignment_review_merged.md` or `none`)
- `[[ASDLC_HASH]]` — full 40-character SHA-1 commit hash of the ASDLC repository used for this review run. **Computed automatically by the `/review` skill; do not substitute manually.** Run `git -C {asdlc_path} rev-parse HEAD` to obtain it.

**Per-invocation variables for `prompt-02-layer.md` (substituted by orchestrator at spawn time, once per layer):**
- `[[LAYER_NUMBER]]` — integer 1–4, the ASDLC layer this agent reviews.
- `[[LAYER_NAME]]` — the canonical short name from the layer table below (e.g., `Demand & Value`).

**Per-invocation variables for `prompt-02-gate.md` (substituted by orchestrator at spawn time, once per gate):**
- `[[GATE_NUMBER]]` — integer 1–4, the ASDLC gate this agent reviews.
- `[[GATE_NAME]]` — the canonical short name from the gate table below (e.g., `Specification Readiness Gate`).

---

## Preflight check

**Before spawning any agent**, scan this prompt for unreplaced placeholders. The prompt MUST NOT contain `[[FRAMEWORK]]` or any other unsubstituted variable. If any `[[...]]` pattern remains (e.g., the literal text `[[FRAMEWORK]]`, `[[FRAMEWORK_LOWER]]`, `[[FRAMEWORK_VERSION]]`, `[[ORGANIZATION]]`, `[[INDUSTRY]]`, `[[DOMAIN_FILE]]`, `[[PRIOR_REVIEWS]]`, or `[[ASDLC_HASH]]` still appears in your working copy), stop immediately and report which variables are unset. Do not proceed until all variables are substituted.

## Preflight check — Lint suite

**Lint preflight.** Before spawning any agent, run `python3 scripts/lint.py --root .` from the ASDLC repository root. The review MUST NOT proceed if any of `gate_counts`, `enums`, `links`, or `term_imports` reports a failure. (`banned_tokens` is permitted to FAIL — it surfaces prose drift in source documents that does not invalidate the review.) `graph_coverage` advisory warnings (exit 0) are informational. If a hard checker fails, report which checker failed and the specific finding(s); do not start the review until ASDLC consistency is restored.

---

## Mission

Spawn a swarm of focused agents — one per sub-prompt — to produce an extremely tough, thorough, and deep assessment of **[[FRAMEWORK]]** against the Agentic Software Delivery Lifecycle (ASDLC). Each agent writes one output file. A final agent merges all files into a master review. Do not try to please. Do not soften findings. Every score must be justified by evidence in [[FRAMEWORK]]'s own artefacts. This review is career-critical.

**Before spawning any agent:** read [[FRAMEWORK]]'s own source files. Do not score on assumptions. Quote exact artefact names, gate condition numbers, layer names, and rule text wherever possible.

## Spawn mechanism

Use the **`Agent` tool** to spawn each sub-agent. For each agent:
1. Read the corresponding sub-prompt file from `prompts/`.
2. Substitute all `[[VARIABLE]]` placeholders with the values defined above.
3. Pass the substituted text as the `prompt` parameter to the `Agent` tool.
4. Each spawned agent runs independently — do not execute sub-prompts inline in your own context.

Wave 1a agents may be spawned simultaneously by issuing all `Agent` tool calls in a single response. The same applies to Wave 1b agents (04c, 05b, 08b) once Wave 1a is fully complete.

## Output directory

All output files go into `[[FRAMEWORK_LOWER]]/`. Create the directory if it does not exist.

## Naming convention

| Agent | Output file |
| --- | --- |
| 01 — Quick Overview | `[[FRAMEWORK_LOWER]]_review_01_quick_overview.md` |
| 02-lN — Layer (4 parallel agents, N=1..4) | `[[FRAMEWORK_LOWER]]_review_02_layer_l{N}.md` × 4 |
| 02-gN — Gate (4 parallel agents, N=1..4) | `[[FRAMEWORK_LOWER]]_review_02_gate_g{N}.md` × 4 |
| 03 — Gates Synthesis & DoDs | `[[FRAMEWORK_LOWER]]_review_03_gates_dods.md` |
| 04a — Adoption (Part 6) | `[[FRAMEWORK_LOWER]]_review_04a_adoption.md` |
| 04b — Cross-cutting Governance (Part 7) | `[[FRAMEWORK_LOWER]]_review_04b_governance.md` |
| 04c — Adoption+Governance Synthesis | `[[FRAMEWORK_LOWER]]_review_04_adoption_governance.md` |
| 05a — Layer Readiness Verdict (Part 8) | `[[FRAMEWORK_LOWER]]_review_05a_readiness.md` |
| 05b — Industry + Combined (Parts 8+9) | `[[FRAMEWORK_LOWER]]_review_05_readiness_industry.md` |
| 06 — Strengths & Gaps | `[[FRAMEWORK_LOWER]]_review_06_strengths_gaps.md` |
| 07 — Guardrails, Security, FinOps & DevSecOps (Parts 12+13) | `[[FRAMEWORK_LOWER]]_review_07_guardrails_security.md` |
| 08a — Enterprise Guardrail Domains (intermediate, §14.1–§14.15) | `[[FRAMEWORK_LOWER]]_review_08a_domains.md` |
| 08b — Enterprise Guardrail Synthesis (canonical Part 14) | `[[FRAMEWORK_LOWER]]_review_08_enterprise_guardrails.md` |
| 09 — Merge | `[[FRAMEWORK_LOWER]]_asdlc_alignment_review_merged.md` |

## Canonical part numbering

All agents must use this mapping. Cross-references in any output file must use these part numbers.

| Part | Title | Source agent |
| --- | --- | --- |
| Part 1 | Overall Scores | 01 |
| Part 2 | Scoring Methodology | 01 |
| Part 3 | ASDLC Layer Coverage — L1, L2, L3, L4 | 02-l1 … 02-l4 (4 parallel agents) |
| Part 4 | ASDLC Gate Analysis — SR Gate, Release Gate, Operational Readiness Gate, Retirement Gate | 02-g1 … 02-g4 (4 parallel agents) |
| Part 5 | ASDLC Definitions of Done — Engineering DoD + Operational DoD | 03 |
| Part 6 | ASDLC Adoption Sequence Alignment | 04a (lifted by 04c) |
| Part 7 | Cross-cutting Governance Alignment | 04b (lifted by 04c) |
| Part 8 | Layer Readiness & Tier 4 Verdict | 05a (lifted by 05b) |
| Part 9 | Industry & Client Assessment | 05b |
| Part 10 | Genuine Strengths | 06 |
| Part 11 | Gap Analysis: Path to Next Layer / Gate | 06 |
| Part 12 | AI/Runtime Guardrails Assessment | 07 |
| Part 13 | Security, FinOps & DevSecOps Assessment | 07 |
| Part 14 | Enterprise Guardrail Domain Coverage | 08a (§14.1–§14.15 intermediate) + 08b (synthesis writes canonical Part 14 file) |

## Canonical layer table

| Layer | Name | Primary artefacts (under ASDLC root) |
| --- | --- | --- |
| L1 | Demand & Value | `demand/value.md`, `demand/intelligence.md`, `demand/metrics.md`, `specification-readiness.md` |
| L2 | Engineering Execution | `../manifesto.md`, `../manifesto-principles.md`, `../manifesto-done.md` (referenced from ASDLC root; ASDLC defers Layer 2 to the AEM) |
| L3 | Release & Deployment | `release-governance.md`, `deployment-governance.md` |
| L4 | Operations & Maintenance | `operations/governance.md`, `operations/dod.md`, `maintenance-governance.md` |

## Canonical gate table

> `governance/gate-registry.yaml` is the machine-readable canonical source of truth for every gate's condition list, count, and titles. `governance/gate-registry.md` is the human-readable derived view. Where the two diverge, the YAML governs. The lint at `scripts/check_gate_counts.py` reads the YAML directly.

| Gate | Name | Source-of-truth for condition count + titles | Authoritative prose source |
| --- | --- | --- | --- |
| G1 | Specification Readiness Gate | `governance/gate-registry.yaml` | `specification-readiness.md` |
| G2 | Release Gate | `governance/gate-registry.yaml` | `release-governance.md` |
| G3 | Operational Readiness Gate | `governance/gate-registry.yaml` | `operations/dod.md` |
| G4 | Retirement Gate | `governance/gate-registry.yaml` | `retirement-gate.md` |

> **Gate-condition source of truth.** `governance/gate-registry.yaml` is the single normative enumeration of every ASDLC gate's condition list. Every agent that touches gate counts (02-g1..g4, 03, 05a, 06, 08a, 08b) MUST read the registry YAML and use its counts and titles verbatim. The authoritative prose sources (`specification-readiness.md`, `release-governance.md`, `operations/dod.md`, `retirement-gate.md`) define each condition in narrative form; the YAML registry resolves any divergence. Where `asdlc.md` summary text, `README.md` enumerations, or the derived `governance/gate-registry.md` diverge from the YAML, the divergence is itself an integrity finding the agent MUST surface in its output — do not silently reconcile.

## Score weighting scheme

All agents must use this weighting when computing a composite score. Do not invent a different weighting.

| Category | Weight |
| --- | --- |
| Layer 1 — Demand & Value | 12% |
| Specification Readiness Gate (G1) | 10% |
| Layer 2 — Engineering Execution (inner-loop coverage) | 18% |
| Release Gate (G2) | 12% |
| Layer 3 — Release & Deployment beyond the gate | 6% |
| Operational Readiness Gate (G3) | 10% |
| Layer 4 — Operations & Maintenance | 8% |
| Retirement Gate (G4) | 4% |
| Tier 4 Policy Envelope & Epistemic-Tier Constraints | 6% |
| Cross-cutting Governance (graph, agents, queries, control plane, waivers) | 4% |
| FinOps, Security & DevSecOps | 6% |
| Feedback Paths Closure (4 paths, unified closure schema) | 4% |

**Total weights sum to 100%.** Overall score = Σ(category_score × weight). Round to one decimal place.

**Weighting changelog.** The prior weighting (in force during Phase 2 retargeting) summed to 100% across 11 categories without a slot for the Retirement Gate. This revision adds G4 at 4%, reduces L2 from 20% to 18% (the inner-loop is now bounded by G1 and G2 conditions that have absorbed several substantive controls), reduces L3 from 8% to 6% and L4 from 10% to 8% (retirement is no longer an L4 footnote), and raises Feedback Paths Closure from 2% to 4% to reflect the unified closure schema across all four paths. Total remains 100%.

## Severity thresholds

All agents must use this mapping for severity labels. Do not use different thresholds.

| Severity | Score range |
| --- | --- |
| Critical | 0–39 |
| High | 40–54 |
| Medium | 55–69 |
| Low | 70–100 |

## Effort sizing

All agents that produce remediation roadmaps must use this calibration. Do not use different effort labels.

| Label | Definition |
| --- | --- |
| S | Single engineer, less than one sprint (<2 weeks) |
| M | Small team, 1–4 sprints (2 weeks – 2 months) |
| L | Multi-team effort, one quarter (2–3 months) |
| XL | Organisation-level change, more than one quarter (>3 months) |

## Banned soft language

All agents must avoid hedging language in their outputs. Every output file MUST NOT contain any of the following tokens or phrases:

**Core banned list (all agents):**
- `consider`, `may`, `could potentially`, `perhaps`, `use judgement`, `use judgment`

Replace each with a specific evidenced claim or an explicit gap statement. Where a fact is unknown, state it as `unknown` — do not hedge.

The orchestrator's banned-token list for AGENT OUTPUT is intentionally stricter than the ASDLC source-prose lint policy (which permits bare `may` as RFC 2119 vocabulary); the asymmetry is deliberate, since agent output must be more direct than reference prose.

**Extended banned list (agents 04c, 06 only — applies to remediation guidance):**
In addition to the core list, avoid the following without an evidence anchor in the same paragraph:
- `robust`, `comprehensive`, `world-class`, `industry-leading`, `best-in-class`, `leverages`, `empowers`, `enables` (without naming what is enabled), `seamless`, `holistic`, `mature` (without phase number), `production-ready` (without naming what is production), `powerful` (without naming the power)

## Sub-prompt files

Each agent is fully specified in `prompts/`. All 14 files are ASDLC-shaped and match the Part numbering, weighting, and source-artefact list above.

```
prompts/prompt-01-quick-overview.md       # Wave 1a — Part 1 (Overall Scores) + Part 2 (Methodology) + Framing Warning + Layer Readiness summary
prompts/prompt-02-layer.md                # Wave 1a — single per-layer review (orchestrator spawns 4 parallel instances with [[LAYER_NUMBER]] / [[LAYER_NAME]] substituted)
prompts/prompt-02-gate.md                 # Wave 1a — single per-gate review (orchestrator spawns 3 parallel instances with [[GATE_NUMBER]] / [[GATE_NAME]] substituted)
prompts/prompt-03-gates-dods.md           # Wave 1a — Part 4 cross-gate synthesis + Part 5 (Engineering DoD + Operational DoD + Hardening Test + feedback paths)
prompts/prompt-04a-adoption.md            # Wave 1a — Part 6 intermediate (ASDLC adoption sequence; 6 steps + Tier 4 graduation)
prompts/prompt-04b-governance.md          # Wave 1a — Part 7 intermediate (5 cross-cutting governance documents)
prompts/prompt-04c-synthesis.md           # Wave 1b — Part 6 + Part 7 combined + Cross-Document Synthesis (Realistic Adoption Ceiling + Highest-Leverage Single Change)
prompts/prompt-05a-readiness.md           # Wave 1a — Part 8 intermediate (Layer Readiness Verdict + Tier 4 envelope + gate non-negotiables + economics)
prompts/prompt-05b-industry.md            # Wave 1b — Part 8 + Part 9 combined (Regulatory Exposure Map + Use-Case Fitness + Red Line + Deployment Path)
prompts/prompt-06-strengths-gaps.md       # Wave 2 — Part 10 (Strengths) + Part 11 (Gaps to next unmet gate / next unmet layer) + Prioritised Remediation Roadmap
prompts/prompt-07-guardrails-security.md  # Wave 1a — Part 12 (Guardrails) + Part 13 (Security + FinOps + DevSecOps)
prompts/prompt-08a-enterprise-domains.md  # Wave 1a — Part 14 §14.1–§14.15 intermediate (15 enterprise guardrail domains)
prompts/prompt-08b-enterprise-synthesis.md # Wave 1b — canonical Part 14 (lifts §14.1–§14.15; adds §14.16 cross-cutting matrix, §14.17 twelve non-negotiables, §14.18 schema verification, §14.19 maturity verdict)
prompts/prompt-09-merge.md                # Wave 3 — merges 14 canonical source files into the 14-Part merged review
```

## Execution order

The wave structure below is the live topology. Wave 1a spawns 15 agents in parallel (1 overview + 4 layers + 4 gates + 1 cross-gate-DoD + 2 adoption/governance intermediates + 1 readiness intermediate + 1 guardrails-security + 1 enterprise-domains intermediate). Wave 1b spawns 3 synthesis agents. Wave 2 spawns 1 strengths-and-gaps agent. Wave 3 spawns 1 merge agent. Total = 20 agent invocations across 4 waves; total output files = 20 (the canonical merged review is one of these).

### Wave 1a — spawn in parallel

Spawn the following agents simultaneously (15 distinct spawns issued in a single response):
- Agent 01 (`prompt-01-quick-overview.md`)
- 4 parallel layer agents 02-l1 … 02-l4 (each spawned from `prompt-02-layer.md` with `[[LAYER_NUMBER]]` and `[[LAYER_NAME]]` substituted per the layer table above)
- 4 parallel gate agents 02-g1 … 02-g4 (each spawned from `prompt-02-gate.md` with `[[GATE_NUMBER]]` and `[[GATE_NAME]]` substituted per the gate table above)
- Agent 03 (`prompt-03-gates-dods.md`)
- Agent 04a (`prompt-04a-adoption.md`)
- Agent 04b (`prompt-04b-governance.md`)
- Agent 05a (`prompt-05a-readiness.md`)
- Agent 07 (`prompt-07-guardrails-security.md`)
- Agent 08a (`prompt-08a-enterprise-domains.md`)

**Wait condition:** Use `Glob` + `Read` (first/last 5 lines, ≥20 lines each) to verify all 15 Wave 1a output files exist and are non-empty before proceeding to Wave 1b:

- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_01_quick_overview.md`
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_layer_l1.md` … `_l4.md` (4 files)
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_02_gate_g1.md` … `_g4.md` (4 files)
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_03_gates_dods.md`
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04a_adoption.md`
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04b_governance.md`
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_05a_readiness.md`
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_07_guardrails_security.md`
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_08a_domains.md`

**Note on the 08 file naming.** The canonical Part 14 file `_review_08_enterprise_guardrails.md` is produced in **Wave 1b by agent 08b**, not Wave 1a. Wave 1a's 08-related output is the intermediate `_review_08a_domains.md`.

**Recovery:** If any Wave 1a file is missing, re-run only the responsible agent. For a missing layer file, re-run only the affected `prompt-02-layer.md` instance with the corresponding `[[LAYER_NUMBER]]` / `[[LAYER_NAME]]`. Same for missing gate files using `prompt-02-gate.md`.

### Wave 1b — after Wave 1a is fully complete

Spawn agents 04c, 05b, and 08b simultaneously. Each has its own dependency:
- **04c** depends on: `_review_04a_adoption.md` and `_review_04b_governance.md` (both Wave 1a outputs)
- **05b** depends on: `_review_05a_readiness.md` (Wave 1a output)
- **08b** depends on: `_review_08a_domains.md` (Wave 1a output)

**Wait condition:** Use `Glob` + `Read` to verify all three Wave 1b outputs exist and are non-empty:

- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_04_adoption_governance.md`
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_05_readiness_industry.md`
- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_08_enterprise_guardrails.md`

### Wave 2 — after Wave 1b is fully complete

Spawn agent 06 using the `Agent` tool. Confirm with `Glob` that all 18 Wave 1a + 1b files exist and are non-empty before spawning.

### Wave 3 — after Wave 2 is fully complete

Spawn agent 09. The following 15 canonical files (read by agent 09) must all exist and be non-empty:

| Source | File | Count |
| --- | --- | --- |
| Agent 01 | `_review_01_quick_overview.md` | 1 |
| Agent 02-lN | `_review_02_layer_l{N}.md` for N=1..4 | 4 |
| Agent 02-gN | `_review_02_gate_g{N}.md` for N=1..4 | 4 |
| Agent 03 | `_review_03_gates_dods.md` | 1 |
| Agent 04c | `_review_04_adoption_governance.md` | 1 |
| Agent 05b | `_review_05_readiness_industry.md` | 1 |
| Agent 06 | `_review_06_strengths_gaps.md` | 1 |
| Agent 07 | `_review_07_guardrails_security.md` | 1 |
| Agent 08b (lifts §14.1–§14.15 from 08a) | `_review_08_enterprise_guardrails.md` | 1 |
| **Total** | | **15** |

Note: The intermediate files `_review_04a_adoption.md`, `_review_04b_governance.md`, `_review_05a_readiness.md`, and `_review_08a_domains.md` are NOT direct inputs to agent 09 — they are consumed by agents 04c, 05b, and 08b respectively.

Use `Glob` to confirm all 15 files before spawning agent 09. **If any source file is missing, do not run agent 09. Report the missing files and stop.**

If any output file already exists, update it in place. Replace wholesale only if [[FRAMEWORK]] has changed substantially — defined as: more than 30% of source artefacts have changed by content, or a layer, gate, or major structural element has been added or removed.

## Hard rules for all agents

- **Read [[FRAMEWORK]]'s source artefacts before scoring.** Every claim must be grounded in a specific file, rule, layer, or gate condition.
- **Read the ASDLC's own source artefacts before scoring.** At minimum: `asdlc.md`, `asdlc-guide.md`, `README.md`, `specification-readiness.md`, `release-governance.md`, `operations/dod.md`, `governance/agents.md`. Where directly relevant to the agent's task, also read the current files in `demand/`, `operations/`, `domains/`, `governance/`, plus `deployment-governance.md`, `maintenance-governance.md`, `finops-governance.md`, `security-governance.md`, `devsecops-controls.md`, `agent-control-plane.md`, `waiver-governance.md` — these are the additional normative and contextual artefacts that constitute ASDLC. Do not score from memory of ASDLC — read the current files.
- **AEM cross-reference for Layer 2.** ASDLC defers Layer 2 (Engineering Execution) to the Agentic Engineering Manifesto. Agent 02-l2 (the Layer 2 reviewer) MUST read the AEM source artefacts (`manifesto.md`, `manifesto-principles.md`, `manifesto-done.md`, `glossary.md`) when scoring Layer 2. The skill resolves the AEM path via `AGENTIC_MANIFESTO_PATH` or via `../` relative to the ASDLC root in the manifesto monorepo. Other agents do not read AEM source files unless explicitly required by their sub-prompt.
- **Tracked-files-only rule.** Every source file referenced or read by an agent MUST be tracked by git on this branch of the ASDLC repository (or, for Layer 2 cross-references, the AEM repository). Do not read, cite, or reference files that appear in `git status` as untracked (`??`), files that have been deleted, files outside the repository, or files that exist only on disk. The authoritative list of in-scope source files is `git ls-files` for the ASDLC repository (and the AEM repository for Layer 2 cross-references); if a path is not in that list, it is not in scope.
- Scores are 0–100. State the score, then state the evidence for and the evidence against separately.
- Use the canonical weighting scheme above for any composite score calculation.
- Use the canonical severity thresholds above for all severity labels.
- Use the canonical effort sizing above for all remediation roadmaps.
- Do not praise the framework for things it does not demonstrably do.
- Do not penalise the framework for problems that are out of its stated scope — but do note the scope gap explicitly.
- Include a **Gap to Next Level** section that states exactly what is missing to close the lowest unmet gate or to reach the next ASDLC layer the framework does not yet cover. Be specific: name the artefact, the mechanism, or the process that would close the gap.
- Industry context ([[INDUSTRY]]) is not decoration — map every major finding to a specific regulation or risk type that applies to [[ORGANIZATION]].
- Use date format **YYYY-MM-DD** wherever a date appears.
- When cross-referencing another part of the review, use the canonical part number (e.g., "see Part 12"). Do not use file names or agent numbers in cross-references within output content.
- **Every output file MUST include the ASDLC provenance line in its header metadata block:** `ASDLC: arnaudgelas/asdlc@[[ASDLC_HASH]]`. This ensures every review is traceable to the exact ASDLC version used for scoring.

## Out-of-scope corpus (do NOT read; do NOT reference)

This review system covers the Agentic Software Delivery Lifecycle (ASDLC) **only**. The rules below distinguish what agents may READ from what agents may EMIT in their output.

### Rule A — Read scope (IN scope to read)

ASDLC-tracked annexes `annex-aentm.md` and `annex-igm.md` are part of ASDLC. Agents reviewing Tier 4 envelope obligations MUST read these annexes. They are the authoritative location for the Tier-4 + AEnt-M relocation mechanics and the Tier-4 + IGM intelligence constraints respectively (formerly `asdlc.md` Tier 4 Appendix A; that content has been relocated).

### Rule B — Output token ban (NOT permitted in agent output)

Agent OUTPUT MUST contain zero matches for `APLC`, `aplc`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc-plan`, `igm-aent-coherence-review`. When assessing Tier 4 obligations sourced from `annex-aentm.md` or `annex-igm.md`, paraphrase the imported terms to ASDLC-equivalent vocabulary (e.g., "the policy-envelope's intelligence substrate" rather than "the IGM epistemic tier"; "the framework's escalation authority for action-class relocation" rather than "the AEnt-M escalation authority").

As the canonical example: when Agent 02-l2 and agent 05a assess whether `[[FRAMEWORK]]` provides the four envelope elements (epistemic-tier-to-action mapping, contradiction-handling rules per type, decay boundaries per claim class, feedback-loop closure rules), the assessment MUST be phrased in ASDLC terms — "the intelligence substrate the framework depends on" rather than "the IGM epistemic tier". When `[[DOMAIN_FILE]]` itself contains references to out-of-scope frameworks, paraphrase them to ASDLC-equivalent terms (e.g., "APLC behavioural specification" → "the framework's specification artefact", "AEnt-M consequence class" → "consequence-class assessment outside ASDLC scope").

### Out-of-scope corpus paths (do NOT read; do NOT cite)

The following adjacent corpora live in or alongside the same repository or organisation but are explicitly outside the scope of this review system. No agent may read them, cite them, or propagate their vocabulary into output. The annex files `annex-aentm.md` and `annex-igm.md` (no path prefix; in the ASDLC root) are NOT in these out-of-scope paths and are governed by Rule A above.

- `aplc/`, `aplc-plan.md`, `aplc-plan.html` (the Agentic Product Lifecycle is a sibling outer framework, separately governed)
- `intelligence-governance-manifesto/` (IGM is a sibling stack governing the epistemic substrate; separately governed)
- `agentic-enterprise-manifesto/`, `agentic-enterprise.md`, `agentic-enterprise.html` (AEnt-M is a sibling stack)
- `agentic-governance-stack.md`, `agentic-governance-stack.html` (cross-stack synthesis document, not ASDLC normative source)
- `manifesto-evolution-plan.md`, `manifesto-evolution-plan.html` (AEM evolution planning, not ASDLC normative source)
- `phase-assessment-checklist.md`, `phase-assessment-checklist.html` (AEM phase-assessment artefact)
- `igm-aent-coherence-review.md`, `igm-aent-coherence-review.html` (IGM/AEnt-M coherence review)
- Any file untracked by git on the current branch (verify with `git ls-files`).

When a `governance/`, `domains/`, or other ASDLC file mixes ASDLC content with imported material, lift only the ASDLC-relevant material.

**ASDLC vocabulary IS in scope.** The tokens `ASDLC`, `asdlc`, and the file paths `asdlc.md`, `asdlc-guide.md`, `agentic-sdlc-handbook` are the rubric for this review and MUST appear in outputs. Earlier review-system rules that banned these tokens have been retired.
