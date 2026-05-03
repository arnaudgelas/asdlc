#!/usr/bin/env python3
"""Validate review-system fixtures, if present.

A sibling agent in this swarm is producing review-system fixtures under
``review/fixtures/``. Each fixture directory is expected to contain a
``manifest.json`` declaring expected gate outcomes for the fixture. This
checker validates those manifests against the canonical gate registry.

If the fixtures directory does not yet exist the checker reports
``skipped_reason`` and exits 0. The ASDLC build is not blocked by the
absence of fixtures.

Validation rules per fixture manifest:

1. ``manifest.json`` must exist and parse as JSON.
2. The manifest must declare a top-level ``expected_outcomes`` object
   whose keys map to canonical gate ids in ``gate-registry.yaml``.
3. Each gate entry must declare a ``verdict`` value drawn from the
   canonical GateState enum (``gate_state_enum`` in
   ``governance/gate-registry.yaml``); any non-canonical verdict is an
   error.
4. The number of conditions enumerated for each gate
   (``passing_conditions``, ``failing_conditions``,
   ``missing_conditions``, ``waived_conditions``, all combined) must
   equal the registry's count for that gate. Identifiers must be unique
   across these lists.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass
class Finding:
    file: str
    line: int
    severity: str
    message: str

    def format(self) -> str:
        return f"{self.file}:{self.line}: {self.severity}: {self.message}"


@dataclass
class CheckResult:
    name: str
    findings: list[Finding] = field(default_factory=list)
    skipped_reason: str | None = None

    @property
    def exit_code(self) -> int:
        return 1 if self.findings else 0


def _parse_registry(registry_path: Path) -> tuple[set[str], dict[str, int]]:
    """Return (canonical gate-state enum, gate-id → condition count).

    Stdlib-only. Parses the slice of YAML this checker depends on with
    targeted regexes.
    """
    text = registry_path.read_text(encoding="utf-8")

    # gate_state_enum block: lines starting with ``  - <value>`` until a
    # blank line or non-indented heading.
    enum_match = re.search(
        r"^gate_state_enum:\s*\n((?:\s*-\s*[a-z][a-z0-9_-]*\s*\n)+)",
        text,
        re.MULTILINE,
    )
    enum_values: set[str] = set()
    if enum_match:
        enum_values = set(re.findall(r"-\s*([a-z][a-z0-9_-]*)", enum_match.group(1)))

    # gate id + count: each top-level gate entry has lines ``- id: <id>``
    # and ``count: <int>``. Pair them by order of appearance.
    counts: dict[str, int] = {}
    for m in re.finditer(
        r"-\s*id:\s*([A-Za-z][A-Za-z0-9_]*)\s*\n"
        r"(?:.*\n){0,12}?\s*count:\s*([0-9]+)\s*\n",
        text,
    ):
        gate_id, count = m.group(1), int(m.group(2))
        # Only record the first time we see this id at the top of a gate
        # block; condition entries also use ``- id:`` but never carry a
        # ``count:`` line within the next 12 lines.
        counts.setdefault(gate_id, count)
    return enum_values, counts


# Map fixture-style gate keys to gate-registry ids.
_GATE_KEY_ALIASES: dict[str, str] = {
    "specification_readiness_gate": "SR",
    "release_gate": "RG",
    "operational_definition_of_done": "DoD",
    "operational_dod": "DoD",
    "retirement_gate": "RT",
    "SR": "SR",
    "RG": "RG",
    "DoD": "DoD",
    "RT": "RT",
}

# Condition list field names that are summed to compute the per-gate
# condition coverage.
_CONDITION_LIST_FIELDS: tuple[str, ...] = (
    "passing_conditions",
    "failing_conditions",
    "missing_conditions",
    "waived_conditions",
    "stale_conditions",
    "contradicted_conditions",
    "requires_human_decision_conditions",
)


def _validate_manifest(
    manifest_path: Path,
    rel: str,
    enum_values: set[str],
    gate_counts: dict[str, int],
) -> list[Finding]:
    findings: list[Finding] = []
    try:
        with manifest_path.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        findings.append(
            Finding(
                file=rel,
                line=0,
                severity="error",
                message="fixture has no manifest.json",
            )
        )
        return findings
    except json.JSONDecodeError as exc:
        findings.append(
            Finding(
                file=rel,
                line=exc.lineno,
                severity="error",
                message=f"manifest.json is not valid JSON: {exc.msg}",
            )
        )
        return findings

    expected = data.get("expected_outcomes") or data.get(
        "expected_gate_outcomes"
    )
    if not isinstance(expected, dict):
        findings.append(
            Finding(
                file=rel,
                line=0,
                severity="error",
                message=(
                    "manifest.json missing required 'expected_outcomes' "
                    "object"
                ),
            )
        )
        return findings

    for gate_key, payload in expected.items():
        gate_id = _GATE_KEY_ALIASES.get(gate_key)
        if gate_id is None or gate_id not in gate_counts:
            findings.append(
                Finding(
                    file=rel,
                    line=0,
                    severity="error",
                    message=(
                        f"unknown gate key {gate_key!r}; expected one of "
                        f"{sorted(_GATE_KEY_ALIASES)}"
                    ),
                )
            )
            continue
        if not isinstance(payload, dict):
            findings.append(
                Finding(
                    file=rel,
                    line=0,
                    severity="error",
                    message=(
                        f"gate {gate_key!r} entry is not an object"
                    ),
                )
            )
            continue

        verdict = payload.get("verdict")
        if verdict is not None and verdict not in enum_values:
            findings.append(
                Finding(
                    file=rel,
                    line=0,
                    severity="error",
                    message=(
                        f"gate {gate_key!r} uses non-canonical verdict "
                        f"{verdict!r}; canonical set is {sorted(enum_values)}"
                    ),
                )
            )

        # Sum condition lists across all known list fields and check
        # uniqueness + total count.
        all_conditions: list[str] = []
        for field_name in _CONDITION_LIST_FIELDS:
            value = payload.get(field_name)
            if value is None:
                continue
            if not isinstance(value, list):
                findings.append(
                    Finding(
                        file=rel,
                        line=0,
                        severity="error",
                        message=(
                            f"gate {gate_key!r} field {field_name!r} is "
                            f"not a list"
                        ),
                    )
                )
                continue
            all_conditions.extend(str(v) for v in value)

        if not all_conditions:
            # No condition lists present — verdict-only expectations are
            # acceptable for negative fixtures.
            continue

        expected_count = gate_counts[gate_id]
        # Only require full enumeration when the verdict is ``pass``.
        # Negative-verdict fixtures may legitimately enumerate only the
        # subset of conditions that drove the verdict.
        if verdict == "pass" and len(all_conditions) != expected_count:
            findings.append(
                Finding(
                    file=rel,
                    line=0,
                    severity="error",
                    message=(
                        f"gate {gate_key!r} enumerates "
                        f"{len(all_conditions)} conditions; registry "
                        f"expects {expected_count}"
                    ),
                )
            )
        if len(set(all_conditions)) != len(all_conditions):
            duplicates = sorted(
                {c for c in all_conditions if all_conditions.count(c) > 1}
            )
            findings.append(
                Finding(
                    file=rel,
                    line=0,
                    severity="error",
                    message=(
                        f"gate {gate_key!r} has duplicate condition ids: "
                        f"{duplicates}"
                    ),
                )
            )
    return findings


def run(root: Path) -> CheckResult:
    result = CheckResult(name="fixtures")
    fixtures_dir = root / "review" / "fixtures"
    if not fixtures_dir.exists():
        result.skipped_reason = "fixtures directory not present"
        return result

    registry_path = root / "governance" / "gate-registry.yaml"
    if not registry_path.exists():
        result.skipped_reason = (
            f"governance/gate-registry.yaml not present at {registry_path}"
        )
        return result

    enum_values, gate_counts = _parse_registry(registry_path)
    if not enum_values or not gate_counts:
        result.skipped_reason = (
            "could not parse gate-state enum or gate counts from "
            "governance/gate-registry.yaml"
        )
        return result

    fixture_dirs = sorted(p for p in fixtures_dir.iterdir() if p.is_dir())
    if not fixture_dirs:
        result.skipped_reason = "fixtures directory contains no fixtures"
        return result

    for fdir in fixture_dirs:
        manifest = fdir / "manifest.json"
        rel = manifest.relative_to(root).as_posix()
        if not manifest.exists():
            result.findings.append(
                Finding(
                    file=rel,
                    line=0,
                    severity="error",
                    message="fixture has no manifest.json",
                )
            )
            continue
        result.findings.extend(
            _validate_manifest(manifest, rel, enum_values, gate_counts)
        )

    return result


def default_root() -> Path:
    return Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root(),
        help="ASDLC repo root (defaults to parent of scripts/).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit findings as JSON instead of text.",
    )
    args = parser.parse_args(argv)

    result = run(args.root.resolve())

    if args.json:
        payload = {
            "name": result.name,
            "exit_code": result.exit_code,
            "skipped_reason": result.skipped_reason,
            "findings": [asdict(f) for f in result.findings],
        }
        print(json.dumps(payload, indent=2))
    else:
        if result.skipped_reason:
            print(f"skipped: {result.skipped_reason}", file=sys.stderr)
        for finding in result.findings:
            print(finding.format())

    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
