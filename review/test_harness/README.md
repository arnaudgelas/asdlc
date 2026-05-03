# ASDLC Review Test Harness

Deterministic, stdlib-only structural test harness for the ASDLC review
system. The harness does not run the LLM-based 14-agent review; it
performs a keyword-indicator pass over each fixture's mock framework
documents and verifies that the structural verdict matches the fixture's
declared `manifest.json`.

## Layout

- `run_fixture.py` — single-fixture runner. Invoke as
  `python3 run_fixture.py <fixture_name>`.
- `run_all_fixtures.py` — aggregate runner; iterates every fixture under
  `review/fixtures/` and prints a single JSON document. Exits 0 only if
  every fixture matches its manifest.
- `output_schema.json` — JSON Schema (draft-07) describing the
  machine-readable companion output every sub-prompt is intended to emit
  alongside its Markdown narrative. See below.

## Companion output schema

`output_schema.json` defines the structure of the `*.json` companion
document that each ASDLC review sub-prompt is intended to produce
alongside its `*.md` narrative. The schema is the contract between
sub-prompts and downstream tooling (the merge agent, conformance
assertions, cross-version comparison).

### Top-level fields

- `metadata` — `framework`, `framework_version`, `asdlc_hash`,
  `run_date`, `sub_prompt_id`, optional `accountable_human`.
- `gate_verdicts` — keyed by `G1`..`G4`. Each entry carries
  `condition_verdicts` (keyed by canonical condition id such as `SR-1`,
  `RG-3`, `DoD-2`, `RT-5` — matching `governance/gate-registry.yaml`),
  an aggregated gate `verdict` drawn from the canonical seven-state
  `GateState` enum (`pass`, `fail`, `missing`, `stale`, `contradicted`,
  `waived`, `requires-human-decision`), and `evidence_anchors`
  referencing `[[FRAMEWORK]]`'s source by file path and optional line
  range.
- `layer_scores` — keyed by `L1`..`L4`. Each carries a `score` (0-100)
  and the `weight_applied` (decimal weight per the orchestrator's
  weighting scheme — e.g., `0.18` for L2).
- `category_scores` — covers the twelve weighted categories from the
  orchestrator's revised weighting scheme (Layer 1 Demand & Value, G1
  SR Gate, Layer 2 Engineering Execution, G2 Release Gate, Layer 3
  Release & Deployment beyond the gate, G3 Operational Readiness Gate,
  Layer 4 Operations & Maintenance, G4 Retirement Gate, Tier 4 Policy
  Envelope, Cross-cutting Governance, FinOps/Security/DevSecOps,
  Feedback Paths Closure).
- `composite_score` — `Σ(category_score × decimal_weight)` rounded to
  one decimal place.
- `disclaimers` — array; the self-referential-grading disclaimer (the
  orchestrator's preamble paragraph that grades against ASDLC's own
  assertions rather than externally-anchored source-of-truth) MUST
  always be present.

### Status

This schema is **introduced** in the current sweep. Full
implementation across all 14 sub-prompts is out of scope for the sweep
that introduced it; the schema is in place so the next sub-prompt
update can wire each sub-prompt's emit step to it. Until then,
sub-prompts continue to emit only the Markdown narrative.

When wiring a sub-prompt to the schema, validate the emitted JSON
against `output_schema.json` (any draft-07 validator works; `pip
install jsonschema` is the typical choice but is **out of stdlib** and
therefore not used by the harness itself).

## Fixtures

The harness iterates every directory under `review/fixtures/` that
contains a `manifest.json`. The canonical list lives in
`run_all_fixtures.py`'s `EXPECTED_FIXTURES` constant; if discovery
diverges from the declared list, the runner exits 2.

Current fixtures:

| Fixture | Expected verdicts |
| --- | --- |
| `fixture-fail-sr` | SR fail, all gates fail |
| `fixture-pass-all` | SR/RG/DoD/RT all pass |
| `fixture-pass-all-but-retirement` | SR/RG/DoD pass; RT fail (retirement out of scope) |
| `fixture-pass-sr-fail-release` | SR pass; RG fail; DoD fail; RT fail |

## Invocation

From the ASDLC repository root:

```
python3 review/test_harness/run_all_fixtures.py
```

Exit 0 with `all_match: true` is the green signal.
