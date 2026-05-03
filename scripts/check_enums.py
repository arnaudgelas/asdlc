#!/usr/bin/env python3
"""Check that gate-state enum values are drawn from the canonical set.

The ASDLC defines a single canonical ``GateState`` enumeration:

- pass
- fail
- missing
- stale
- contradicted
- waived
- requires-human-decision

Other documents must not introduce alternative state values. In particular:

- ``waived-with-current-waiver`` is forbidden — it must be expressed as a
  derived predicate over ``waived`` plus a waiver-validity check, not as a
  state.
- ``deferred-to-gate`` is a workflow status, not a ``GateState``; it must
  not appear in any enum declaration.
- Legacy values (e.g. ``approved``, ``rejected``, ``pending``) must be
  migrated.

This checker scans every ``*.md`` file for state assertions that look like
enum declarations or YAML-style ``status:`` fields and reports any value not
in the canonical set.

Suppress a false positive by adding the file path to ``WHITELIST_FILES`` or
by rephrasing the line so the heuristic does not fire.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable


CANONICAL_GATE_STATES: frozenset[str] = frozenset({
    "pass",
    "fail",
    "missing",
    "stale",
    "contradicted",
    "waived",
    "requires-human-decision",
})

# State values that are explicitly banned and have a known canonical
# expression. Reported with a hint.
BANNED_STATES_WITH_HINT: dict[str, str] = {
    "waived-with-current-waiver": (
        "express as a derived predicate over `waived` plus a waiver-validity "
        "check; do not declare as a GateState"
    ),
    "deferred-to-gate": (
        "this is a workflow status, not a GateState; declare it elsewhere"
    ),
    "approved": "legacy value; migrate to `pass`",
    "rejected": "legacy value; migrate to `fail`",
    "pending": "legacy value; migrate to `missing` or `requires-human-decision`",
    "in-progress": "legacy value; migrate to `missing`",
    "blocked": "legacy value; migrate to `fail` or `requires-human-decision`",
}

# Files exempt from enum scanning. Path is relative to repo root.
WHITELIST_FILES: set[str] = {
    "scripts/check_enums.py",
    "scripts/README.md",
}

# Patterns for places where a single state value is asserted.
PATTERNS: list[tuple[re.Pattern[str], str]] = [
    # YAML-style: "status: <value>" or "state: <value>".
    (
        re.compile(
            r"^\s*(?:status|state|gate_state|GateState)\s*[:=]\s*"
            r"['\"]?(?P<value>[A-Za-z0-9_\-]+)['\"]?\s*$",
            re.IGNORECASE,
        ),
        "status assignment",
    ),
    # Code-style assignment: GateState = <value> (whitespace tolerated).
    (
        re.compile(
            r"\bGateState\s*=\s*['\"`]?(?P<value>[a-z][a-z0-9_\-]*)['\"`]?",
        ),
        "GateState assignment",
    ),
    # Attribute-style: GateState.<VALUE> where value is a kebab/snake token.
    # Require no intervening whitespace so "GateState. At" does not match.
    (
        re.compile(
            r"\bGateState\.(?P<value>[a-z][a-z0-9_\-]*)\b",
        ),
        "GateState attribute",
    ),
]

# Pattern for prose enumerations like "one of: a, b, c, d" appearing on one
# line. This matches the values inside the colon-comma list.
ENUM_LIST_PATTERN = re.compile(
    r"\b(?:one of|values?|states?|enum)\s*[:=]\s*"
    r"(?P<list>[A-Za-z0-9_\-`'\", ]+)$",
    re.IGNORECASE,
)


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

    @property
    def exit_code(self) -> int:
        return 1 if self.findings else 0


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        yield path


def looks_like_state_token(token: str) -> bool:
    """Heuristic: a token looks like a state if it is in the canonical set,
    in the banned set, or matches a kebab/snake state-shaped string of
    reasonable length."""
    if token in CANONICAL_GATE_STATES or token in BANNED_STATES_WITH_HINT:
        return True
    return False


def scan_line(line: str, lineno: int, rel: str) -> list[Finding]:
    findings: list[Finding] = []

    # Direct state-assignment patterns.
    for pattern, label in PATTERNS:
        match = pattern.search(line)
        if not match:
            continue
        value = match.group("value").strip().lower()
        if value in BANNED_STATES_WITH_HINT:
            findings.append(
                Finding(
                    file=rel,
                    line=lineno,
                    severity="error",
                    message=(
                        f"{label} uses banned state {value!r}: "
                        f"{BANNED_STATES_WITH_HINT[value]} "
                        f"(line: {line.strip()!r})"
                    ),
                )
            )
        elif value not in CANONICAL_GATE_STATES:
            # Only flag values that are state-shaped (kebab-case and short).
            # This avoids false positives on "status: open" in unrelated
            # YAML-ish text.
            if re.fullmatch(r"[a-z][a-z0-9\-]{1,40}", value):
                # Ignore if the line names a non-gate context.
                if not any(
                    word in line.lower()
                    for word in ("gate", "gatestate", "gate_state")
                ):
                    return findings
                findings.append(
                    Finding(
                        file=rel,
                        line=lineno,
                        severity="error",
                        message=(
                            f"{label} uses non-canonical GateState {value!r}; "
                            f"canonical set is {sorted(CANONICAL_GATE_STATES)}"
                            f" (line: {line.strip()!r})"
                        ),
                    )
                )

    # Prose enumerations of state values.
    list_match = ENUM_LIST_PATTERN.search(line)
    if list_match and any(
        word in line.lower()
        for word in ("gatestate", "gate state", "gate-state")
    ):
        raw = list_match.group("list")
        tokens = re.findall(r"[A-Za-z][A-Za-z0-9_\-]*", raw)
        for token in tokens:
            value = token.lower()
            if value in BANNED_STATES_WITH_HINT:
                findings.append(
                    Finding(
                        file=rel,
                        line=lineno,
                        severity="error",
                        message=(
                            f"prose enum lists banned state {value!r}: "
                            f"{BANNED_STATES_WITH_HINT[value]}"
                        ),
                    )
                )

    return findings


def scan_file(path: Path, root: Path) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    if rel in WHITELIST_FILES:
        return []

    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), start=1):
        findings.extend(scan_line(line, lineno, rel))
    return findings


def run(root: Path) -> CheckResult:
    result = CheckResult(name="enums")
    for path in iter_markdown_files(root):
        result.findings.extend(scan_file(path, root))
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
            "findings": [asdict(f) for f in result.findings],
        }
        print(json.dumps(payload, indent=2))
    else:
        for finding in result.findings:
            print(finding.format())

    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
