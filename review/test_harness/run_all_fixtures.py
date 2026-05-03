#!/usr/bin/env python3
"""Run the structural harness against every fixture under review/fixtures/.

Aggregates the per-fixture reports into a single JSON document and exits 0
only if every fixture's structural verdict matches its manifest.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Allow `python3 run_all_fixtures.py` invocation regardless of cwd.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from run_fixture import run  # noqa: E402


# Canonical fixture iteration list. Auto-discovery walks fixtures-dir at run
# time, but this list is the declared expectation: every fixture below MUST
# be present and a passing match for the harness to report all_match=true.
# When a new fixture is added under review/fixtures/, append it here.
EXPECTED_FIXTURES: list[str] = [
    "fixture-fail-sr",
    "fixture-pass-all",
    "fixture-pass-all-but-retirement",
    "fixture-pass-sr-fail-release",
]


def main(argv: list[str] | None = None) -> int:
    default_fixtures_dir = HERE.parent / "fixtures"
    default_registry = HERE.parent.parent / "governance" / "gate-registry.yaml"

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures-dir", type=Path, default=default_fixtures_dir)
    parser.add_argument("--registry", type=Path, default=default_registry)
    args = parser.parse_args(argv)

    fixtures_dir: Path = args.fixtures_dir
    if not fixtures_dir.is_dir():
        print(json.dumps({"error": f"fixtures dir not found: {fixtures_dir}"}))
        return 2

    fixture_dirs = sorted(
        d for d in fixtures_dir.iterdir() if d.is_dir() and (d / "manifest.json").is_file()
    )

    # Sanity-check the discovery against the canonical iteration list.
    discovered = {d.name for d in fixture_dirs}
    expected = set(EXPECTED_FIXTURES)
    missing = expected - discovered
    unexpected = discovered - expected
    if missing or unexpected:
        print(json.dumps({
            "error": "fixture set does not match EXPECTED_FIXTURES",
            "missing": sorted(missing),
            "unexpected": sorted(unexpected),
        }, indent=2))
        return 2

    reports = []
    all_match = True
    for fd in fixture_dirs:
        report = run(fd, args.registry)
        reports.append(report)
        if not report["matches"]:
            all_match = False

    aggregate = {
        "fixtures_dir": str(fixtures_dir),
        "fixture_count": len(reports),
        "all_match": all_match,
        "summary": [
            {
                "fixture": r["fixture"],
                "matches": r["matches"],
                "gate_verdicts": {
                    gid: gv["verdict"] for gid, gv in r["actual"].items()
                },
                "mismatch_count": len(r["mismatches"]),
            }
            for r in reports
        ],
        "reports": reports,
    }
    print(json.dumps(aggregate, indent=2))
    return 0 if all_match else 1


if __name__ == "__main__":
    raise SystemExit(main())
