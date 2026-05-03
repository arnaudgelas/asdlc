#!/usr/bin/env python3
"""Check that every node and edge type declared in ``governance/graph.md``
is also represented in the §2.1 "Schema (formal)" exemplars or referenced
as a published schema, and that every edge type has a cardinality rule.

The graph document explicitly states that it ships exemplar JSON Schema
fragments for a subset of node types only, and that organisations must
publish full schemas for every node and edge type. Therefore this checker
emits findings at severity ``info`` for missing exemplar coverage. If
more than 50% of declared types lack any kind of coverage, the severity
is bumped to ``warning`` to draw attention to the structural gap.

Findings are grouped:

- Missing schema fragments — declared node/edge types without an
  exemplar fragment AND without a published-schema reference in §2.1.
- Missing cardinality rules — declared edge types without an entry in
  the §2.1 "Cardinality rules" subsection.

The checker never emits ``error`` severity. It is intentionally
non-blocking — the underlying contract is that organisations adopting
ASDLC must publish their own complete schema set; the document only
ships exemplars.
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
        # Coverage findings are advisory; never fail the build.
        return 0


# Section anchors used to slice graph.md.
NODE_TYPES_HEADING = re.compile(r"^##\s+Node Types\s*$", re.MULTILINE)
EDGE_TYPES_HEADING = re.compile(r"^##\s+Edge Types\s*$", re.MULTILINE)
SCHEMA_FORMAL_HEADING = re.compile(
    r"^##\s+2\.1\s+Schema\s*\(formal\)\s*$",
    re.MULTILINE,
)
CARDINALITY_HEADING = re.compile(
    r"^###\s+Cardinality\s+rules\s*$",
    re.MULTILINE,
)
NEXT_TOP_HEADING = re.compile(r"^##\s+", re.MULTILINE)
NEXT_SUB_HEADING = re.compile(r"^###\s+", re.MULTILINE)


def _slice_section(
    text: str, start_match: re.Match[str] | None, next_pattern: re.Pattern[str]
) -> str:
    """Return the body of a section, ending at the next heading."""
    if start_match is None:
        return ""
    start = start_match.end()
    nxt = next_pattern.search(text, pos=start)
    end = nxt.start() if nxt else len(text)
    return text[start:end]


def extract_subsection_names(section_body: str, depth: str) -> list[str]:
    """Return the list of subsection names at a given heading depth."""
    pattern = re.compile(rf"^{re.escape(depth)}\s+(.+?)\s*$", re.MULTILINE)
    return [m.group(1).strip() for m in pattern.finditer(section_body)]


def extract_edge_types(section_body: str) -> list[str]:
    """Return edge type names from the Edge Types section.

    The body uses a paragraph-per-edge format: ``**edge_name** runs from
    ... to ...``. Extract the bolded leading token as the edge name.
    """
    pattern = re.compile(r"^\*\*([a-z][a-z0-9_]+)\*\*\s+runs", re.MULTILINE)
    return [m.group(1) for m in pattern.finditer(section_body)]


def extract_schema_titles(schema_body: str) -> set[str]:
    """Return the set of node-type ``title`` values declared in JSON Schema
    fragments inside the schema section."""
    return set(re.findall(r'"title"\s*:\s*"([^"]+)"', schema_body))


def extract_published_schema_references(schema_body: str) -> set[str]:
    """Return the set of node/edge names declared as having a published
    schema reference in the §2.1 prose. Heuristic: a line of the form
    ``- <Name>: <url-or-pointer>`` or a sentence that names the type and
    points to a URI.

    Currently the document does not include such pointers; this function
    is forward-compatible. Returns an empty set today.
    """
    return set()


def extract_cardinality_edges(cardinality_body: str) -> set[str]:
    """Return the set of edge names that have a cardinality rule.

    The cardinality section uses bullet form ``- **edge_name** (...)``;
    extract the bolded leading token.
    """
    pattern = re.compile(
        r"^\s*-\s*\*\*([a-z][a-z0-9_]+)\*\*",
        re.MULTILINE,
    )
    return set(pattern.findall(cardinality_body))


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def run(root: Path) -> CheckResult:
    result = CheckResult(name="graph_coverage")
    graph_path = root / "governance" / "graph.md"
    if not graph_path.exists():
        result.skipped_reason = f"governance/graph.md not present at {graph_path}"
        return result

    text = graph_path.read_text(encoding="utf-8")
    rel = graph_path.relative_to(root).as_posix()

    nodes_match = NODE_TYPES_HEADING.search(text)
    edges_match = EDGE_TYPES_HEADING.search(text)
    schema_match = SCHEMA_FORMAL_HEADING.search(text)

    if not (nodes_match and edges_match and schema_match):
        result.skipped_reason = (
            "graph.md does not have the expected section structure "
            "(Node Types / Edge Types / 2.1 Schema (formal))"
        )
        return result

    node_section = _slice_section(text, nodes_match, NEXT_TOP_HEADING)
    edge_section = _slice_section(text, edges_match, NEXT_TOP_HEADING)
    schema_section = _slice_section(text, schema_match, NEXT_TOP_HEADING)

    node_types = extract_subsection_names(node_section, "###")
    edge_types = extract_edge_types(edge_section)

    schema_titles = extract_schema_titles(schema_section)
    schema_titles |= extract_published_schema_references(schema_section)

    # Cardinality rules live in a subsection inside the schema body.
    card_match = CARDINALITY_HEADING.search(schema_section)
    cardinality_edges: set[str] = set()
    if card_match:
        card_body = _slice_section(
            schema_section, card_match, NEXT_SUB_HEADING
        )
        cardinality_edges = extract_cardinality_edges(card_body)

    # ---------------- Coverage analysis ----------------
    missing_node_schemas = [n for n in node_types if n not in schema_titles]
    # Edges may have a JSON-Schema fragment too (rare today); test the
    # title set the same way.
    missing_edge_schemas = [e for e in edge_types if e not in schema_titles]
    missing_cardinality = [
        e for e in edge_types if e not in cardinality_edges
    ]

    total_types = len(node_types) + len(edge_types)
    total_missing = len(missing_node_schemas) + len(missing_edge_schemas)
    severity = "info"
    if total_types and (total_missing / total_types) > 0.5:
        severity = "warning"

    schema_line = _line_for_offset(text, schema_match.start())
    card_line = (
        _line_for_offset(text, schema_match.start() + card_match.start())
        if card_match
        else schema_line
    )

    for name in missing_node_schemas:
        result.findings.append(
            Finding(
                file=rel,
                line=schema_line,
                severity=severity,
                message=(
                    f"missing schema fragment for node type {name!r}: "
                    f"§2.1 ships exemplars only; organisations must "
                    f"publish a schema for every declared node type"
                ),
            )
        )
    for name in missing_edge_schemas:
        result.findings.append(
            Finding(
                file=rel,
                line=schema_line,
                severity=severity,
                message=(
                    f"missing schema fragment for edge type {name!r}: "
                    f"§2.1 ships exemplars only; organisations must "
                    f"publish a schema for every declared edge type"
                ),
            )
        )
    for name in missing_cardinality:
        result.findings.append(
            Finding(
                file=rel,
                line=card_line,
                severity="info",
                message=(
                    f"missing cardinality rule for edge type {name!r}: "
                    f"§2.1 'Cardinality rules' has no entry"
                ),
            )
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
            print(f"warning: {result.skipped_reason}", file=sys.stderr)
        for finding in result.findings:
            print(finding.format())

    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
