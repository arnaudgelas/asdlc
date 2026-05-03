#!/usr/bin/env python3
"""Structural test harness for ASDLC review-system fixtures.

This script does NOT run the LLM-based 14-agent review. It performs a
deterministic, keyword-based *structural* assessment of a fixture's mock
framework documents and verifies that the structural verdict matches the
fixture's declared `manifest.json`.

Per condition (SR-N, RG-N, DoD-N, RT-N) the harness searches the fixture's
.md files for a small dictionary of indicative phrases. If at least one
indicative phrase is found the condition is marked `pass`, otherwise `fail`.
The aggregate gate verdict is `pass` only if every condition for that gate
is `pass`; otherwise `fail`.

Exit code 0 if the structural verdict matches the manifest, 1 otherwise.

Usage:
    python3 run_fixture.py <fixture_name>
    python3 run_fixture.py --fixtures-dir <dir> <fixture_name>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable


# Canonical gate names, per governance/gate-registry.yaml.
GATE_NAMES: dict[str, str] = {
    "SR": "Specification Readiness Gate",
    "RG": "Release Gate",
    "DoD": "Operational Definition of Done",
    "RT": "Retirement Gate",
}

# Manifest key -> registry gate id.
MANIFEST_KEY_TO_GATE_ID: dict[str, str] = {
    "specification_readiness_gate": "SR",
    "release_gate": "RG",
    "operational_definition_of_done": "DoD",
    "retirement_gate": "RT",
}

# Indicative phrases per canonical condition id. A condition is considered
# structurally addressed if any of its phrases appears (case-insensitive,
# word-boundary tolerant) in any fixture .md file.
CONDITION_INDICATORS: dict[str, list[str]] = {
    # Specification Readiness Gate
    "SR-1": ["business need validated", "demand validation", "validated demand"],
    "SR-2": ["value measurable", "measurable value", "value metric"],
    "SR-3": ["acceptance criteria", "acceptance test"],
    "SR-4": ["constraints identified", "constraint inventory", "regulatory constraint"],
    "SR-5": ["accountable human", "named accountable", "human accountability"],
    "SR-6": ["blast radius", "impact tier"],
    "SR-7": ["out-of-scope", "out of scope", "explicitly excluded"],
    "SR-8": ["loop cost", "cost justified", "cost ceiling"],
    "SR-9": ["context thread", "context bundle", "context assembly"],
    # Release Gate
    "RG-1": ["evidence bundle", "release evidence"],
    "RG-2": ["independent validation", "independent reviewer", "independent sign-off"],
    "RG-3": ["rollback procedure", "rollback tested", "rollback drill"],
    "RG-4": ["accountable human sign-off", "named approver", "human approver"],
    "RG-5": ["compliance documentation", "regulatory documentation", "compliance pack"],
    "RG-6": ["dynamic security testing", "dast", "penetration test"],
    "RG-7": ["control state record", "control state ledger"],
    "RG-8": ["waiver governance", "waiver register", "waiver process"],
    # Operational Definition of Done
    "DoD-1": ["runbook complete", "operational runbook"],
    "DoD-2": ["operational observability", "observability configured", "metrics and traces"],
    "DoD-3": ["on-call assignment", "on-call rota", "on-call schedule"],
    "DoD-4": ["system steward", "steward assigned"],
    "DoD-5": ["security scan clean", "vulnerability scan", "security scanning"],
    "DoD-6": ["license compliance", "sbom", "open-source licence"],
    "DoD-7": ["trace retention", "audit trace retention", "log retention policy"],
    "DoD-8": ["dr/failover", "disaster recovery", "failover tested"],
    # Retirement Gate
    "RT-1": ["stewardship handoff", "stewardship termination", "retirement handoff"],
    "RT-2": ["runbook archived", "immutable archive"],
    "RT-3": ["trace archival", "reasoning-record archival", "trace archive"],
    "RT-4": ["model deprecation", "prompt deprecation"],
    "RT-5": ["igm claim retraction", "claim retraction"],
    "RT-6": ["dependency consumers notified", "consumer notification"],
    "RT-7": ["finops zero-out", "cost zero-out", "decommission cost"],
    "RT-8": ["final accountability sign-off", "final sign-off", "decommission approval"],
}


@dataclass
class ConditionVerdict:
    condition_id: str
    verdict: str  # pass | fail | missing | uncertain
    matched_phrases: list[str] = field(default_factory=list)
    matched_files: list[str] = field(default_factory=list)


@dataclass
class GateVerdict:
    gate_id: str
    gate_name: str
    verdict: str  # pass | fail
    conditions: list[ConditionVerdict] = field(default_factory=list)


def load_registry(registry_path: Path) -> dict[str, list[str]]:
    """Parse gate-registry.yaml to extract {gate_id -> [condition_id, ...]}.

    A tiny line-based parser; avoids a yaml dependency to honour the
    stdlib-only constraint.
    """
    text = registry_path.read_text(encoding="utf-8")
    gate_to_conditions: dict[str, list[str]] = {}
    current_gate: str | None = None
    in_conditions = False
    for raw in text.splitlines():
        stripped = raw.strip()
        m_gate = re.match(r"-\s*id:\s*(SR|RG|DoD|RT)\s*$", stripped)
        if m_gate and raw.startswith("  - "):
            current_gate = m_gate.group(1)
            gate_to_conditions[current_gate] = []
            in_conditions = False
            continue
        if current_gate and stripped == "conditions:":
            in_conditions = True
            continue
        if in_conditions:
            m_cond = re.match(r"-\s*id:\s*((?:SR|RG|DoD|RT)-\d+)\s*$", stripped)
            if m_cond:
                gate_to_conditions[current_gate].append(m_cond.group(1))
                continue
            # A new top-level gate entry will reset above; nothing to do here.
    return gate_to_conditions


def gather_fixture_text(fixture_dir: Path) -> dict[str, str]:
    """Return {relative_path -> lowercased text} for every .md file."""
    docs: dict[str, str] = {}
    for md_path in sorted(fixture_dir.rglob("*.md")):
        docs[md_path.name] = md_path.read_text(encoding="utf-8").lower()
    return docs


def assess_condition(
    condition_id: str, docs: dict[str, str]
) -> ConditionVerdict:
    indicators = CONDITION_INDICATORS.get(condition_id, [])
    if not indicators:
        return ConditionVerdict(condition_id, "uncertain")
    matched_phrases: list[str] = []
    matched_files: list[str] = []
    for phrase in indicators:
        for filename, text in docs.items():
            if phrase in text:
                matched_phrases.append(phrase)
                if filename not in matched_files:
                    matched_files.append(filename)
                break
    verdict = "pass" if matched_phrases else "fail"
    return ConditionVerdict(condition_id, verdict, matched_phrases, matched_files)


def assess_gate(
    gate_id: str, condition_ids: Iterable[str], docs: dict[str, str]
) -> GateVerdict:
    conditions = [assess_condition(cid, docs) for cid in condition_ids]
    overall = "pass" if all(c.verdict == "pass" for c in conditions) else "fail"
    return GateVerdict(gate_id, GATE_NAMES[gate_id], overall, conditions)


def compare_to_manifest(
    actual: dict[str, GateVerdict], manifest: dict
) -> tuple[bool, list[dict]]:
    mismatches: list[dict] = []
    expected = manifest.get("expected_outcomes", {})
    for manifest_key, gate_id in MANIFEST_KEY_TO_GATE_ID.items():
        exp = expected.get(manifest_key)
        if exp is None:
            mismatches.append(
                {"gate": gate_id, "issue": f"manifest missing key {manifest_key}"}
            )
            continue
        exp_verdict = exp.get("verdict")
        act_verdict = actual[gate_id].verdict
        if exp_verdict != act_verdict:
            mismatches.append(
                {
                    "gate": gate_id,
                    "expected_verdict": exp_verdict,
                    "actual_verdict": act_verdict,
                    "actual_failing_conditions": [
                        c.condition_id
                        for c in actual[gate_id].conditions
                        if c.verdict != "pass"
                    ],
                }
            )
            continue
        # Optional deeper check: failing_conditions must be a subset of actual
        # failing conditions when the manifest enumerates them.
        exp_failing = set(exp.get("failing_conditions", []))
        if exp_failing:
            act_failing = {
                c.condition_id for c in actual[gate_id].conditions if c.verdict != "pass"
            }
            if not exp_failing.issubset(act_failing):
                mismatches.append(
                    {
                        "gate": gate_id,
                        "issue": "expected failing_conditions not all observed",
                        "expected_failing": sorted(exp_failing),
                        "actual_failing": sorted(act_failing),
                    }
                )
    return (len(mismatches) == 0), mismatches


def run(fixture_dir: Path, registry_path: Path) -> dict:
    manifest_path = fixture_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    gate_to_conditions = load_registry(registry_path)
    docs = gather_fixture_text(fixture_dir)

    actual: dict[str, GateVerdict] = {}
    for gate_id, condition_ids in gate_to_conditions.items():
        actual[gate_id] = assess_gate(gate_id, condition_ids, docs)

    matches, mismatches = compare_to_manifest(actual, manifest)

    actual_serialisable = {
        gid: {
            "gate_name": gv.gate_name,
            "verdict": gv.verdict,
            "conditions": [asdict(c) for c in gv.conditions],
        }
        for gid, gv in actual.items()
    }

    return {
        "fixture": manifest.get("fixture_name", fixture_dir.name),
        "fixture_path": str(fixture_dir),
        "expected": manifest.get("expected_outcomes", {}),
        "actual": actual_serialisable,
        "matches": matches,
        "mismatches": mismatches,
    }


def main(argv: list[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    default_fixtures_dir = here.parent / "fixtures"
    default_registry = here.parent.parent / "governance" / "gate-registry.yaml"

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture_name", help="Name of fixture directory under fixtures-dir")
    parser.add_argument(
        "--fixtures-dir",
        type=Path,
        default=default_fixtures_dir,
        help=f"Fixtures root (default: {default_fixtures_dir})",
    )
    parser.add_argument(
        "--registry",
        type=Path,
        default=default_registry,
        help=f"Path to gate-registry.yaml (default: {default_registry})",
    )
    args = parser.parse_args(argv)

    fixture_dir = args.fixtures_dir / args.fixture_name
    if not fixture_dir.is_dir():
        print(json.dumps({"error": f"fixture not found: {fixture_dir}"}))
        return 2

    report = run(fixture_dir, args.registry)
    print(json.dumps(report, indent=2))
    return 0 if report["matches"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
