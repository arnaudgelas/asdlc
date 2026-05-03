#!/usr/bin/env python3
"""Umbrella linter for the ASDLC repository.

Runs every checker in ``scripts/`` and aggregates the result. Each checker
is a sibling module exposing a ``run(root: Path) -> CheckResult`` callable.

Usage::

    python3 scripts/lint.py            # run everything (text output)
    python3 scripts/lint.py --json     # machine-readable summary
    python3 scripts/lint.py --check links
    python3 scripts/lint.py --root /path/to/asdlc

The exit code is the maximum of the child exit codes, so any failure causes
a non-zero exit. The intent is that CI calls this script and fails the
build on a non-zero exit.

The ``--fix`` flag is reserved. It currently performs no automatic fixes
because the heuristics carry too much false-positive risk for unattended
edits. Future work may add per-checker fixers.
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from dataclasses import asdict
from pathlib import Path
from types import ModuleType
from typing import Callable, Sequence

# Add scripts/ to sys.path so checker modules can be imported by short name
# whether this script is run via ``python3 scripts/lint.py`` or as a module.
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


# Order is the display order; alphabetised for predictability.
CHECKERS: Sequence[str] = (
    "banned_tokens",
    "enums",
    "fixtures",
    "gate_counts",
    "graph_coverage",
    "links",
    "term_imports",
)


def load_checker(name: str) -> tuple[ModuleType, Callable]:
    """Import ``check_<name>`` and return (module, run_callable)."""
    module = importlib.import_module(f"check_{name}")
    runner = getattr(module, "run")
    return module, runner


def render_table(rows: list[tuple[str, str, int]]) -> str:
    headers = ("Check", "Status", "Findings")
    widths = [
        max(len(headers[0]), max((len(r[0]) for r in rows), default=0)),
        max(len(headers[1]), max((len(r[1]) for r in rows), default=0)),
        max(len(headers[2]), max((len(str(r[2])) for r in rows), default=0)),
    ]

    def line(parts: tuple[str, str, str]) -> str:
        return (
            f"{parts[0]:<{widths[0]}} | "
            f"{parts[1]:<{widths[1]}} | "
            f"{parts[2]:<{widths[2]}}"
        )

    sep = "-" * widths[0] + "-+-" + "-" * widths[1] + "-+-" + "-" * widths[2]

    out = [
        line(headers),
        sep,
    ]
    for name, status, findings in rows:
        out.append(line((name, status, str(findings))))
    out.append(sep)
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--root",
        type=Path,
        default=SCRIPTS_DIR.parent,
        help="ASDLC repo root (defaults to parent of scripts/).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit aggregate findings as JSON.",
    )
    parser.add_argument(
        "--check",
        choices=tuple(CHECKERS),
        action="append",
        help="Run only the named checker (repeatable).",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help=(
            "Reserved: currently a no-op. Future work may add per-checker "
            "auto-fixers."
        ),
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    selected = tuple(args.check) if args.check else CHECKERS

    if args.fix:
        print(
            "warning: --fix is reserved and currently a no-op (TODO).",
            file=sys.stderr,
        )

    results = []
    for name in selected:
        module, runner = load_checker(name)
        result = runner(root)
        results.append(result)

    aggregate_exit = max((r.exit_code for r in results), default=0)
    total_findings = sum(len(r.findings) for r in results)

    if args.json:
        payload = {
            "exit_code": aggregate_exit,
            "root": str(root),
            "total_findings": total_findings,
            "checks": [
                {
                    "name": r.name,
                    "exit_code": r.exit_code,
                    "skipped_reason": getattr(r, "skipped_reason", None),
                    "findings": [asdict(f) for f in r.findings],
                }
                for r in results
            ],
        }
        print(json.dumps(payload, indent=2))
        return aggregate_exit

    # Text output: per-checker findings, then summary table.
    for r in results:
        skipped = getattr(r, "skipped_reason", None)
        if skipped:
            print(f"[{r.name}] warning: {skipped}", file=sys.stderr)
        for finding in r.findings:
            print(finding.format())

    def status_label(r) -> str:
        if getattr(r, "skipped_reason", None):
            return "SKIPPED"
        return "PASS" if r.exit_code == 0 else "FAIL"

    rows = [(r.name, status_label(r), len(r.findings)) for r in results]
    rows.append(
        ("TOTAL", "PASS" if aggregate_exit == 0 else "FAIL", total_findings)
    )
    print()
    print(render_table(rows))
    return aggregate_exit


if __name__ == "__main__":
    sys.exit(main())
