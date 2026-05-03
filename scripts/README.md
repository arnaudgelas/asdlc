# ASDLC docs lint

This directory holds **acceptance tests for the framework's own documents**.
ASDLC audits other frameworks; these checkers audit ASDLC. They are the
governance-of-governance loop applied to ASDLC source itself.

## What is checked

| Check | Module | Question it answers |
| --- | --- | --- |
| `gate_counts` | `check_gate_counts.py` | Do any docs assert a gate condition count that disagrees with `governance/gate-registry.md`? |
| `enums` | `check_enums.py` | Are gate-state values drawn from the canonical `GateState` set, with no banned or legacy values? |
| `links` | `check_links.py` | Do all relative markdown links resolve on disk (including known sibling-framework aliases)? |
| `banned_tokens` | `check_banned_tokens.py` | Does any ASDLC source use the hedge/marketing tokens banned in `review/prompt.md`? Tokens inside fenced code blocks and inline `code spans` are exempt; `mature` is exempt next to a phase number; `enables` is exempt when followed by an object naming what is enabled; bare `may` is permitted (RFC 2119 vocabulary), but the multi-word hedges `may potentially` / `could potentially` remain banned. |
| `term_imports` | `check_term_imports.py` | Are sibling-framework terms (AEM, AEnt-M, IGM, APLC) attributed or locally defined? AEM cross-references (`manifesto`, `Layer 2`) are file-level cross_references — satisfied by any mention of the AEM in the file. IGM and AEnt-M imports are strict — satisfied by the source acronym appearing anywhere in the file or by a local definition (including a JSON-Schema `enum` field). A "Normative References" section that names the source is also accepted. |
| `graph_coverage` | `check_graph_coverage.py` | Does `governance/graph.md` §2.1 ship a JSON-Schema fragment for every node and edge type, and a cardinality rule for every edge? Severity is `info` (or `warning` when more than 50% of types are uncovered). Never blocks. |
| `fixtures` | `check_fixtures.py` | Do `review/fixtures/<name>/manifest.json` files declare an `expected_outcomes` object whose verdicts are canonical GateStates and whose condition lists match the registry counts (when the verdict is `pass`)? Skipped when the fixtures directory is absent. |

The umbrella runner `lint.py` imports every checker, aggregates findings,
prints a summary table, and exits with the maximum child exit code.

## Running locally

The scripts depend only on Python 3.11+ standard library. Either of:

```bash
python3 scripts/lint.py
uv run python scripts/lint.py
```

Run a single checker:

```bash
python3 scripts/lint.py --check links
python3 scripts/check_gate_counts.py
```

Machine-readable output for CI dashboards:

```bash
python3 scripts/lint.py --json
```

Override the repo root (defaults to the parent of `scripts/`):

```bash
python3 scripts/lint.py --root /path/to/asdlc
```

A reserved `--fix` flag exists. It is a no-op today; future work may add
per-checker auto-fixers where false-positive risk is low.

## Output format

Every finding is emitted as `file:line: severity: message`. Example:

```
asdlc.md:142: error: silent import: term 'relocation mechanics' (source: AEnt-M) used without attribution or local definition: 'Tier 4 relocation mechanics. ...'
```

This format is grep-friendly and matches the convention used by most
text editors' error parsers.

## Adding a new checker

1. Create `scripts/check_<name>.py`.
2. Expose `run(root: pathlib.Path) -> CheckResult` where `CheckResult` has
   `name: str`, `findings: list[Finding]`, optional `skipped_reason: str`,
   and a `.exit_code` property (`0` if no findings, `1` otherwise). Keep
   the dataclass shape identical to the existing checkers so the umbrella
   runner can serialise it without special cases.
3. Implement a standalone `main(argv)` with `--root` and `--json` flags
   that mirrors the existing checkers.
4. Add `<name>` to the `CHECKERS` tuple in `lint.py`.
5. Update this README's table.

## CI integration

A minimal GitHub Actions workflow:

```yaml
name: docs-lint
on:
  push:
    branches: [main]
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Run docs lint
        run: python3 scripts/lint.py
```

Because the runner uses only the standard library there is no dependency
install step. CI fails on any drift; the build log shows every finding
in `file:line: severity: message` format.

## Suppressing findings

Each checker exposes its own escape hatch:

- `check_gate_counts.py` — add the path to `WHITELIST_FILES`, or rephrase
  prose so the heuristic does not fire.
- `check_enums.py` — add the path to `WHITELIST_FILES`, or rephrase the
  state assertion.
- `check_links.py` — add the alias to `KNOWN_ALIASES` with the correct
  target, or add the path to `WHITELIST_FILES`.
- `check_banned_tokens.py` — add the path to `FILE_EXEMPTIONS`, the prefix
  to `DIR_EXEMPTIONS`, the token to `GLOBAL_TOKEN_EXEMPTIONS`, the
  per-file allowance to `PER_FILE_TOKEN_ALLOWANCES`, or annotate the line
  with the inline marker `<!-- lint:allow-banned-token reason -->`.
- `check_term_imports.py` — add the source acronym (`(IGM)`, `(AEnt-M)`)
  to the file, define the term locally, add a "Normative References"
  section that names the source, or mark the import as
  `attribution: cross_reference` in `scripts/known_imports.json`.
- `check_graph_coverage.py` — add the missing schema exemplar or
  cardinality rule to `governance/graph.md` §2.1; the checker itself has
  no per-file suppression because every finding is already advisory.
- `check_fixtures.py` — adjust the fixture's `manifest.json` so the
  verdict is in the canonical GateState enum and the condition lists
  match the registry count (only enforced when the verdict is `pass`).

## How to suppress a false positive

A genuine false positive — a banned hedge token that is not actually a
hedge in context, or a sibling-framework term that is unmistakably part
of a quoted external rule — should be suppressed at the narrowest scope
that fits:

1. **Inline suppression** (banned tokens only). Append
   `<!-- lint:allow-banned-token <one-line reason> -->` to the offending
   markdown line. The reason is for code-review auditing; the marker
   itself silences the line. Use this when only one or two lines in a
   file need the exception.
2. **Per-file token allowance** (banned tokens only). Add the relative
   file path and the token name to `PER_FILE_TOKEN_ALLOWANCES` in
   `check_banned_tokens.py`. Use this when a normative file legitimately
   quotes a token as structured vocabulary (e.g. the gate registry's
   "blocking" / "conditional" outcome enumeration).
3. **Per-file exemption** (banned tokens). Add the path to
   `FILE_EXEMPTIONS`. Reserved for the lint script itself, the prompt
   that defines the rule, and other meta-documentation that
   intentionally enumerates the banned tokens.
4. **Cross-reference attribution** (term imports). When a term is a
   first-class ASDLC cross-reference rather than a silent import, mark
   it `"attribution": "cross_reference"` in `known_imports.json`. The
   AEM terms `manifesto` and `Layer 2` are the canonical examples.
5. **Normative References section** (term imports). For a file that
   uses many imported terms from one source, add a "Normative
   References" / "References" / "Sources" / "External References"
   section that names the source framework. The checker will treat all
   imports from that source as attributed within the file.

Do not loosen the policy globally. If the same false positive appears in
many files, that usually means the policy is wrong — open a PR with the
rationale.

## Why this exists

The ASDLC review system audits external frameworks for governance drift.
The strategic review of ASDLC found that ASDLC itself had drifted: gate
condition counts disagreed across documents, links to sibling frameworks
broke, banned hedge tokens applied to review agents but not to ASDLC
source, and several sibling-framework terms were imported without
attribution. The fix is to apply the same audit discipline to ASDLC
itself, in CI, on every change.

This directory is the implementation of that fix.
