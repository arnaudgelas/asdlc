#!/usr/bin/env python3
"""Check gate condition counts for drift against the canonical YAML registry.

The ASDLC defines four gates: Specification Readiness, Release, Operational
Readiness (which evaluates the Operational Definition of Done), and Retirement.
The canonical condition counts and titles live in
``governance/gate-registry.yaml``. The companion ``gate-registry.md`` is a
human-readable view derived from that YAML; it is informational, not
authoritative for lint purposes.

This checker:

1. Parses ``governance/gate-registry.yaml`` directly to extract canonical
   counts, titles, and identifiers.
2. Scans every other ``*.md`` file for phrases that assert a gate condition
   count (e.g. "nine conditions", "8 conditions", "Specification Readiness
   Gate has X conditions").
3. Reports any assertion whose count does not match the registry.

False positives are acceptable. Each report includes the matched line so a
reviewer can confirm the finding. Suppress a false positive by rephrasing the
prose so the heuristic does not fire (e.g. avoid "<number> condition" near a
gate name) or by linking directly to the registry instead of restating.

We use a minimal hand-rolled YAML reader (sufficient for the registry's
shape) to avoid an external PyYAML dependency.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable


# Word -> integer for "nine conditions" style assertions.
WORD_TO_INT = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12,
}

# Files that are allowed to discuss numeric drift candidly. Paths are
# relative to repo root.
WHITELIST_FILES = {
    "governance/gate-registry.md",
    "governance/gate-registry.yaml",
    "scripts/check_gate_counts.py",
    "scripts/README.md",
}

GATE_NAMES_PATTERN = re.compile(
    r"(Specification Readiness Gate|Release Gate|"
    r"Operational Definition of Done|Operational Readiness Gate|"
    r"Retirement Gate)",
    re.IGNORECASE,
)

COUNT_PATTERN = re.compile(
    r"\b(?P<count>\d+|one|two|three|four|five|six|seven|eight|nine|ten|"
    r"eleven|twelve)\b\s+(?:blocking\s+|unconditional\s+|"
    r"unconditional\s+and\s+\w+\s+conditional\s+)?conditions?\b",
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
    skipped_reason: str | None = None

    @property
    def exit_code(self) -> int:
        return 1 if self.findings else 0


# Minimal YAML reader. The registry's shape is restricted: top-level mapping,
# nested mappings, lists of mappings, and scalar values. Comments and blank
# lines are ignored. Block scalars (`>-`, `|`) collapse to a single string.
def read_simple_yaml(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return _parse_yaml(text)


def _parse_yaml(text: str) -> dict:
    # Strip the leading document marker.
    lines = text.splitlines()
    cleaned: list[tuple[int, str]] = []  # (indent, raw)
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#") or stripped == "---":
            i += 1
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        # Handle folded/block scalars: '>-', '>', '|', '|-' on a key line.
        m = re.match(r"^([A-Za-z_][\w-]*):\s*([>|][-+]?)\s*(#.*)?$", stripped)
        if m:
            key, _marker = m.group(1), m.group(2)
            j = i + 1
            block_lines: list[str] = []
            while j < len(lines):
                next_raw = lines[j]
                next_stripped = next_raw.strip()
                if not next_stripped or next_stripped.startswith("#"):
                    j += 1
                    continue
                next_indent = len(next_raw) - len(next_raw.lstrip(" "))
                if next_indent <= indent:
                    break
                block_lines.append(next_stripped)
                j += 1
            cleaned.append((indent, f"{key}: {' '.join(block_lines)}"))
            i = j
            continue
        cleaned.append((indent, stripped))
        i += 1
    result, _ = _parse_block(cleaned, 0, 0)
    return result if isinstance(result, dict) else {}


def _parse_block(lines: list[tuple[int, str]], pos: int, base_indent: int):
    # Decide list vs. mapping by first item.
    if pos >= len(lines):
        return None, pos
    indent, first = lines[pos]
    if indent < base_indent:
        return None, pos
    if first.startswith("- "):
        return _parse_list(lines, pos, indent)
    return _parse_mapping(lines, pos, indent)


def _parse_mapping(lines, pos, base_indent):
    out: dict = {}
    while pos < len(lines):
        indent, line = lines[pos]
        if indent < base_indent:
            break
        if indent > base_indent:
            # Should be consumed by recursive call earlier
            pos += 1
            continue
        if line.startswith("- "):
            break
        m = re.match(r"^([^:]+):\s*(.*)$", line)
        if not m:
            pos += 1
            continue
        key = m.group(1).strip()
        rest = m.group(2).strip()
        if rest:
            out[key] = _scalar(rest)
            pos += 1
        else:
            # Nested block.
            pos += 1
            if pos >= len(lines):
                out[key] = None
                continue
            child_indent = lines[pos][0]
            if child_indent <= base_indent:
                out[key] = None
                continue
            child, pos = _parse_block(lines, pos, child_indent)
            out[key] = child
    return out, pos


def _parse_list(lines, pos, base_indent):
    out: list = []
    while pos < len(lines):
        indent, line = lines[pos]
        if indent < base_indent:
            break
        if indent > base_indent:
            pos += 1
            continue
        if not line.startswith("- "):
            break
        rest = line[2:].strip()
        if ":" in rest and not rest.endswith(":"):
            # Inline mapping starting on the dash line.
            first_kv = rest
            m = re.match(r"^([^:]+):\s*(.*)$", first_kv)
            item: dict = {}
            if m:
                k = m.group(1).strip()
                v = m.group(2).strip()
                item[k] = _scalar(v) if v else None
            pos += 1
            # Continue collecting same-block deeper-indented lines as more
            # mapping entries on this list item.
            while pos < len(lines):
                next_indent, next_line = lines[pos]
                if next_indent <= base_indent:
                    break
                # Treat next_indent's mapping continuation
                m2 = re.match(r"^([^:]+):\s*(.*)$", next_line)
                if not m2 or next_line.startswith("- "):
                    break
                kk = m2.group(1).strip()
                vv = m2.group(2).strip()
                if vv:
                    item[kk] = _scalar(vv)
                    pos += 1
                else:
                    pos += 1
                    if pos < len(lines):
                        deep_indent = lines[pos][0]
                        if deep_indent > next_indent:
                            child, pos = _parse_block(lines, pos, deep_indent)
                            item[kk] = child
                        else:
                            item[kk] = None
                    else:
                        item[kk] = None
            out.append(item)
        elif rest.endswith(":"):
            # Item begins a sub-mapping on the next line.
            pos += 1
            child, pos = _parse_block(lines, pos, base_indent + 2)
            out.append(child)
        else:
            out.append(_scalar(rest))
            pos += 1
    return out, pos


def _scalar(text: str):
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    if text.startswith("'") and text.endswith("'"):
        return text[1:-1]
    if text.lower() in {"true", "yes"}:
        return True
    if text.lower() in {"false", "no"}:
        return False
    if text.lower() in {"null", "~", ""}:
        return None
    if re.match(r"^-?\d+$", text):
        return int(text)
    if re.match(r"^-?\d+\.\d+$", text):
        return float(text)
    return text


def parse_registry(yaml_path: Path) -> dict[str, int] | None:
    """Return canonical counts per gate name.

    Returns ``None`` if the YAML registry is missing or malformed.
    """
    if not yaml_path.exists():
        return None

    try:
        data = read_simple_yaml(yaml_path)
    except Exception:
        return None

    gates = data.get("gates")
    if not isinstance(gates, list):
        return None

    counts: dict[str, int] = {}
    for gate in gates:
        if not isinstance(gate, dict):
            continue
        name = gate.get("name")
        # Prefer declared count; fall back to len(conditions).
        declared = gate.get("count")
        conditions = gate.get("conditions")
        if isinstance(name, str):
            if isinstance(declared, int):
                counts[name] = declared
            elif isinstance(conditions, list):
                counts[name] = len(conditions)

    # Operational Readiness Gate evaluates the DoD; same count.
    if "Operational Definition of Done" in counts:
        counts["Operational Readiness Gate"] = counts[
            "Operational Definition of Done"
        ]

    return counts


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        yield path


def normalise_count(token: str) -> int | None:
    token = token.lower()
    if token.isdigit():
        return int(token)
    return WORD_TO_INT.get(token)


def scan_file(path: Path, root: Path, counts: dict[str, int]) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    if rel in WHITELIST_FILES:
        return []

    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")

    for lineno, line in enumerate(text.splitlines(), start=1):
        gate_match = GATE_NAMES_PATTERN.search(line)
        if not gate_match:
            continue
        gate_name = canonical_gate_name(gate_match.group(1))
        expected = counts.get(gate_name)
        if expected is None:
            continue

        for count_match in COUNT_PATTERN.finditer(line):
            asserted = normalise_count(count_match.group("count"))
            if asserted is None:
                continue
            if asserted != expected:
                findings.append(
                    Finding(
                        file=rel,
                        line=lineno,
                        severity="error",
                        message=(
                            f"asserted {asserted} conditions for "
                            f"{gate_name!r}, registry says {expected}: "
                            f"{line.strip()!r}"
                        ),
                    )
                )

    return findings


def canonical_gate_name(raw: str) -> str:
    lowered = raw.lower()
    for canonical in (
        "Specification Readiness Gate",
        "Release Gate",
        "Operational Definition of Done",
        "Operational Readiness Gate",
        "Retirement Gate",
    ):
        if canonical.lower() == lowered:
            return canonical
    return raw


def run(root: Path) -> CheckResult:
    result = CheckResult(name="gate_counts")
    yaml_path = root / "governance" / "gate-registry.yaml"

    parsed = parse_registry(yaml_path)
    if parsed is None:
        result.skipped_reason = (
            f"YAML registry not found or unparsable at {yaml_path}; "
            f"no canonical counts available, skipping check"
        )
        return result
    counts = parsed

    for path in iter_markdown_files(root):
        result.findings.extend(scan_file(path, root, counts))

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
            print(f"warning: {result.skipped_reason}", file=sys.stderr)
        for finding in result.findings:
            print(finding.format())

    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
