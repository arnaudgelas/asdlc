# ASDLC Framework Alignment Review System

This directory contains a multi-agent review system that scores third-party frameworks against the **Agentic Software Delivery Lifecycle (ASDLC)** — the four-layer governance lifecycle defined in this repository.

## What this is

A swarm of 14 parallel agents, orchestrated across 4 waves, that produce a regulator-credible alignment review of an external framework against ASDLC. The review covers:

- **4 Layers** — L1 Demand & Value; L2 Engineering Execution; L3 Release & Deployment; L4 Operations & Maintenance.
- **3 Gates** — Specification Readiness; Release; Operational Readiness.
- **2 Definitions of Done** — Engineering DoD (inherited from the Agentic Engineering Manifesto, the inner loop of L2); Operational DoD (ASDLC-specific).
- **Tier 4 Policy Envelope** — the four-element envelope assessment from `asdlc.md` Tier 4 Appendix A.
- **Cross-cutting Governance** — governance graph, governance agents, governance queries, agent control plane, waivers.
- **FinOps + Security + DevSecOps** — operational financial governance, security lifecycle, DevSecOps pipeline by autonomy tier.
- **5 Feedback Paths** — L4→L1, L4→L2, L3→L2, L2→L1 (closure assessment); L4→IGM (out of scope, noted only).
- **15 Enterprise Guardrail Domains** — identity, data, tooling, autonomy, provenance, specification, cost, monitoring, evidence, security, data lifecycle, incidents, human guardrails, vendor/model, learning/memory.
- **Industry mapping** — every major finding mapped to a specific regulatory provision from the chosen domain file.

## What this is NOT

This system reviews against ASDLC. It does **not** review against:

- **The Agentic Engineering Manifesto (AEM)** — for AEM reviews, use the parent monorepo's review system at `../.claude/skills/review.md` or the standalone manifesto repository at <https://github.com/arnaudgelas/agentic-engineering-manifesto>. ASDLC defers Layer 2 to AEM, so this system reads AEM source artefacts when scoring L2 — but the rubric is ASDLC, not AEM.
- **The Agentic Product Lifecycle (APLC)** — APLC is a sibling outer framework for agent-as-product systems. See <https://github.com/arnaudgelas/aplc>.
- **The Intelligence Governance Manifesto (IGM)** — IGM governs the epistemic substrate; out of scope for ASDLC framework reviews.
- **The Agentic Enterprise Manifesto (AEnt-M)** — out of scope.

The orchestrator (`prompt.md`) and every sub-prompt explicitly forbid APLC, IGM, AEnt-M, and related vocabulary in outputs. This is enforced by the banned-token rule. ASDLC vocabulary IS the rubric and IS expected in outputs.

## Self-referential-grading disclaimer

This review system grades external frameworks against ASDLC's own assertions, not against externally-anchored regulatory or engineering source-of-truth. ASDLC asserts what each layer, gate, and Definition-of-Done condition demands; the review system measures `[[FRAMEWORK]]` against those assertions. ASDLC's own claims rest on a separate evidence base (NIST SSDF, NIST AI RMF, NIST AI 100-2e2025, OWASP Agentic AI, OWASP LLM Top 10, CISA Secure by Design, FinOps Foundation, plus the AEM for Layer 2 inner-loop semantics). The review system does not re-verify ASDLC's claims against that outer evidence base on each run.

When the review system flags a gap in `[[FRAMEWORK]]` against an ASDLC condition, the operator must additionally verify that ASDLC's own claim against the underlying regulatory or engineering source is itself sound. The review system does not perform that outer verification. This is a deliberate scope boundary: ASDLC alignment is one input to a deployment decision, not a substitute for the deployer's regulator-credible mapping back to the named regulations or engineering standards in `[[DOMAIN_FILE]]`.

## Scope guard

When the chosen domain file references APLC, IGM, or AEnt-M mechanisms (e.g., `domains/insurance.md` references "the APLC's behavioural specification"), the prompts paraphrase to ASDLC-equivalent terms. Vocabulary is not propagated.

## How to invoke

```
/review FRAMEWORK ORGANIZATION INDUSTRY DOMAIN_FILE [PRIOR_REVIEWS]
```

Example:

```
/review mle Allianz "European insurance — DORA, Solvency II, EU AI Act" domains/insurance.md none
```

The `/review` skill (defined at `skills/review.md` here, and mirrored at `../.claude/skills/review.md` once installed):

1. Resolves the ASDLC repository (current directory if it contains `asdlc.md`, else `ASDLC_PATH`, else clones `arnaudgelas/asdlc`).
2. Resolves the AEM repository for L2 cross-reference (monorepo-adjacent `../`, else `AGENTIC_MANIFESTO_PATH`, else clones `arnaudgelas/agentic-engineering-manifesto`).
3. Records both git hashes for reproducibility.
4. Spawns 14 Wave 1a agents in parallel (1 overview + 4 layers + 3 gates + 1 cross-gate-DoD + 1 adoption + 1 governance + 1 readiness + 1 guardrails-security + 1 enterprise-domains).
5. Spawns 3 Wave 1b agents in parallel (adoption-governance synthesis; readiness-industry synthesis; enterprise-guardrails synthesis).
6. Spawns 1 Wave 2 agent (strengths-and-gaps).
7. Spawns 1 Wave 3 agent (merge).
8. Produces 19 output files in `{FRAMEWORK_LOWER}/`, with the canonical merged review at `{FRAMEWORK_LOWER}/{FRAMEWORK_LOWER}_asdlc_alignment_review_merged.md`.

Total agents = 14 + 3 + 1 + 1 = 19. Total output files = 19.

To check progress mid-flight: `/review-status FRAMEWORK_LOWER`.

## Score weighting

The 11 weighting categories sum to 100%. The weighting reflects ASDLC's load-bearing emphasis on engineering execution + release governance:

| Category | Weight |
| --- | --- |
| Layer 2 — Engineering Execution | 20% |
| Release Gate | 12% |
| Layer 1 — Demand & Value | 12% |
| Specification Readiness Gate | 10% |
| Operational Readiness Gate | 10% |
| Layer 4 — Operations & Maintenance | 10% |
| Layer 3 — Release & Deployment beyond the gate | 8% |
| Tier 4 Policy Envelope & Epistemic-Tier Constraints | 6% |
| FinOps, Security & DevSecOps | 6% |
| Cross-cutting Governance | 4% |
| Feedback Paths Closure | 2% |

## Severity thresholds

| Severity | Score range |
| --- | --- |
| Critical | 0–39 |
| High | 40–54 |
| Medium | 55–69 |
| Low | 70–100 |

## Effort sizing

| Label | Definition |
| --- | --- |
| S | Single engineer, less than one sprint (<2 weeks) |
| M | Small team, 1–4 sprints (2 weeks – 2 months) |
| L | Multi-team effort, one quarter (2–3 months) |
| XL | Organisation-level change, more than one quarter (>3 months) |

## Files in this directory

| Path | Purpose |
| --- | --- |
| `prompt.md` | Master orchestrator — variables, mission, sub-prompt list, wave execution, hard rules, out-of-scope corpus |
| `prompts/prompt-01-quick-overview.md` | Wave 1a — Part 1 (Overall Scores) + Part 2 (Methodology) + Framing Warning |
| `prompts/prompt-02-layer.md` | Wave 1a — single per-layer review (4 parallel spawns, L1..L4) |
| `prompts/prompt-02-gate.md` | Wave 1a — single per-gate review (3 parallel spawns, G1..G3) |
| `prompts/prompt-03-gates-dods.md` | Wave 1a — Part 4 (Gate Analysis) + Part 5 (Engineering DoD + Operational DoD + Hardening Test) |
| `prompts/prompt-04a-adoption.md` | Wave 1a — Part 6 intermediate (ASDLC adoption sequence; 7 subsections including Tier 4 graduation) |
| `prompts/prompt-04b-governance.md` | Wave 1a — Part 7 intermediate (cross-cutting governance; 5 subsections) |
| `prompts/prompt-04c-synthesis.md` | Wave 1b — Part 6 + Part 7 combined + Cross-Document Synthesis |
| `prompts/prompt-05a-readiness.md` | Wave 1a — Part 8 intermediate (Layer Readiness Verdict + Tier 4 Envelope + Evidence Matrix + Gate-Level Non-Negotiables + Economics Assessment) |
| `prompts/prompt-05b-industry.md` | Wave 1b — Part 8 + Part 9 combined (industry assessment; Regulatory Exposure Map + Use-Case Fitness + Red Line + Deployment Path) |
| `prompts/prompt-06-strengths-gaps.md` | Wave 2 — Part 10 (Strengths) + Part 11 (Gaps) + Prioritised Remediation Roadmap |
| `prompts/prompt-07-guardrails-security.md` | Wave 1a — Part 12 (Guardrails) + Part 13 (Security + FinOps + DevSecOps) |
| `prompts/prompt-08a-enterprise-domains.md` | Wave 1a — Part 14 §14.1–§14.15 intermediate |
| `prompts/prompt-08b-enterprise-synthesis.md` | Wave 1b — canonical Part 14 (lifts §14.1–§14.15; adds §14.16 cross-cutting matrix, §14.17 twelve non-negotiables, §14.18 schema verification, §14.19 maturity verdict) |
| `prompts/prompt-09-merge.md` | Wave 3 — final merge into `{FRAMEWORK_LOWER}_asdlc_alignment_review_merged.md` |
| `skills/review.md` | The `/review` skill definition |
| `skills/review-status.md` | The `/review-status` skill definition |

## Distinctive ASDLC tests built into this review system

These tests differentiate the ASDLC review system from a generic SDLC review:

1. **Tier 4 envelope test** — agent 02-l2 and agent 05a assess the four envelope elements from `asdlc.md` Tier 4 Appendix A: epistemic-tier-to-action mapping, contradiction-handling rules per type, decay boundaries per claim class, feedback-loop closure rules. A framework that claims Tier 4 but lacks any of these is flagged as ungoverned production autonomy.
2. **Feedback paths closure test** — agent 03 assesses each of the four ASDLC feedback paths (L4→L1, L4→L2, L3→L2, L2→L1) for triggering signal class, destination governance authority, latency SLO, and closing condition. The L4→IGM path is noted as out of scope.
3. **SR-Gate condition-count integrity check** — agent 02-g1 (the SR Gate reviewer) reads `specification-readiness.md` (canonical) and surfaces any inconsistency with `asdlc.md` summary text (which says "nine conditions" but lists only 7 in the bullet section).
4. **Governance failure modes coverage** — agent 07 §12.4 assesses six modes: evidence laundering, approval laundering, compliance theater, stale-control reliance, automated rubber-stamping, waiver accumulation. ASDLC inherits these from manifesto P10 and operationalises them across `governance/agents.md`, `waiver-governance.md`, and `governance/queries.md`.
5. **ASDLC values mapping to gates** — the three ASDLC values (Validated demand before execution; Governed release over shipped artefacts; Operated outcomes over deployed systems) map directly to G1, G2, G3 respectively (per `asdlc.md` § Values). Gate scoring respects this anchor.

## Fixtures and tests

The review system is backed by a small, deterministic test layer that
asserts the prompt bundle's machine-readable contract — gate names,
condition IDs, and `GateState` enum values — against three mock
frameworks. This is the unit-test layer below the LLM-based 14-agent
review; it does not run any agents.

### Fixture frameworks

Three mock external frameworks live under `review/fixtures/`. Each
fixture is a self-contained directory of small Markdown documents plus
a `manifest.json` that declares the expected outcome at every gate.

| Fixture | Mock framework | Expected outcome |
| --- | --- | --- |
| `review/fixtures/fixture-fail-sr/` | LoopForge — engineering-loop only, no demand validation | Fails Specification Readiness Gate (SR-1, SR-2, SR-4, SR-5, SR-6) |
| `review/fixtures/fixture-pass-sr-fail-release/` | SpecCraft — strong intake, lightweight release | Passes SR; fails Release Gate (RG-1, RG-2, RG-3, RG-5) |
| `review/fixtures/fixture-pass-all/` | Atrium — full Intake / Build / Ship / Run / Sunset lifecycle | Passes all four gates |

Every manifest uses canonical gate names ("Specification Readiness Gate",
"Release Gate", "Operational Definition of Done", "Retirement Gate"),
canonical condition IDs (`SR-N`, `RG-N`, `DoD-N`, `RT-N`), and canonical
`GateState` enum values (`pass`, `fail`, `missing`, `stale`,
`contradicted`, `waived`, `requires-human-decision`) — all sourced from
`governance/gate-registry.yaml`.

### Test harness

The harness lives at `review/test_harness/` and uses the Python 3.11+
standard library only.

| Path | Purpose |
| --- | --- |
| `review/test_harness/run_fixture.py` | Runs a structural assessment of one fixture and compares it to its manifest. |
| `review/test_harness/run_all_fixtures.py` | Runs every fixture and emits an aggregate JSON report. |

The harness is *structural*, not LLM-based: for each gate condition it
searches the fixture's Markdown for a small dictionary of indicative
phrases. A condition passes if any indicator is present; the gate
passes only if every condition passes. The harness's guarantee is that
the fixture's declared manifest is internally consistent with what a
keyword-driven structural pass would find — not that the fixture is
correctly graded by the full review system. The 14-agent review is the
upper layer; this is the unit-test layer below it.

Run the full suite from the repo root:

```
python3 review/test_harness/run_all_fixtures.py
```

The aggregate output is JSON; the script exits 0 only if every
fixture's structural verdict matches its manifest, 1 otherwise.

### CI hook

The `scripts/lint.py` chain does not yet wire the harness in; the
preferred integration is via a `scripts/check_fixtures.py` checker that
loads each manifest and validates it against the registry. A minimal
inline invocation, until that lands, is:

```bash
python3 review/test_harness/run_all_fixtures.py > /dev/null
```

`check_fixtures.py` (when present) MUST validate that every manifest's
`GateState` values come from `gate-registry.yaml.gate_state_enum`, every
condition ID matches the registry's canonical IDs, and every gate name
matches the registry's canonical names. The harness presumes those
properties; the linter enforces them.

## Provenance

This review system was retargeted from the AEM review system in three phases:

- **Phase 1** (orchestrator + skill + banned-token cleanup) — rewrote `prompt.md`, `skills/review.md`, `skills/review-status.md`; surgical edits across 13 sub-prompts to remove ASDLC tokens from banned lists.
- **Phase 2** (sub-prompt rewrites) — full rewrites of 5 structurally-new sub-prompts (`prompt-02-layer.md`, `prompt-02-gate.md`, `prompt-03-gates-dods.md`, `prompt-04b-governance.md`, `prompt-05a-readiness.md`); heavy retargets of 9 retained-name sub-prompts; deletion of 4 orphaned AEM-shaped originals (`prompt-02-principle.md`, `prompt-03-loop-dod.md`, `prompt-04b-companion.md`, `prompt-05a-maturity.md`).
- **Phase 3** (gate-registry wiring + skill unblock + self-referential-grading disclaimer) — pointed every gate-touching sub-prompt at `governance/gate-registry.md` as the source of truth for gate condition counts and titles; removed the stale "Phase 2 pending" warnings from `prompt.md`, `skills/review.md`, `skills/review-status.md` (the skill is invokable); added the self-referential-grading disclaimer here and in `prompt.md`'s status block; ran the banned-token sweep (core list `consider, may, could potentially, perhaps, use judgement, use judgment` and extended list `robust, comprehensive, world-class, seamless, holistic, mature without phase number, production-ready, powerful, enables without naming what is enabled`) across the 14 sub-prompts. The only banned-token matches found are inside enforcement instruction text (e.g., the literal phrase `Output MUST NOT contain ...`) and the canonical category labels `Layer 2 — Engineering Execution`; no occurrences leak into output templates.

The phase boundaries and the per-recommendation rationale are retained for audit. To review against the AEM, use the parent monorepo's review system or clone the manifesto repository directly.
