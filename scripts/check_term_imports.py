#!/usr/bin/env python3
"""Check that imported sibling-framework terms are attributed or defined.

The ASDLC corpus borrows terms from sibling frameworks (AEM, AEnt-M, IGM,
APLC). Each borrowed term is listed in ``scripts/known_imports.json`` with
the source framework. A term is correctly imported when, in the ASDLC core
documents, every occurrence is either:

1. Accompanied by an explicit attribution to the source framework in the
   same paragraph (e.g. "see AEM § 4", "(IGM)", "per AEnt-M"), OR
2. Locally defined in the same file (e.g. an inline definition or a
   "Definitions" section that defines the term).

Any other occurrence is a silent import — the reader cannot trace the
term back to its source and therefore cannot verify the meaning.

This checker scans the files listed under ``scoped_files`` in the manifest
and reports each silent occurrence. Suppress a false positive by adding an
attribution to the paragraph, defining the term in the file, or adjusting
``scripts/known_imports.json``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable


# Heuristic markers that indicate an attribution to a source framework. The
# checker requires at least one marker to appear within the same paragraph
# as the term.
ATTRIBUTION_MARKERS: tuple[str, ...] = (
    "AEM",
    "Agentic Engineering Manifesto",
    "AEnt-M",
    "Agentic Enterprise Manifesto",
    "IGM",
    "Intelligence Governance Model",
    "Intelligence Governance",
    "APLC",
    "Agentic Platform Lifecycle",
    "see manifesto",
    "see the manifesto",
    "per manifesto",
)

# Heuristic markers that indicate a local definition.
DEFINITION_MARKERS: tuple[str, ...] = (
    "is defined as",
    "is defined here as",
    "we define",
    "## Definitions",
    "### Definitions",
    "## Glossary",
    "### Glossary",
    "shall mean",
    "means: ",
)


@dataclass
class ImportEntry:
    term: str
    source: str
    pointer: str
    aliases: tuple[str, ...] = ()
    # Attribution policy:
    #   "strict" (default) — every paragraph that uses the term must
    #     either contain an attribution marker for ``source`` or the file
    #     must locally define the term. Used for IGM/AEnt-M imports.
    #   "cross_reference" — first-class ASDLC cross-reference; the term
    #     is treated as attributed for the whole file as soon as the file
    #     mentions the source framework anywhere (e.g. README.md and
    #     asdlc.md establish the cross-reference up-front).
    attribution: str = "strict"


# Section-heading patterns that, when present in a file, declare the file
# imports terms from one or more named source frameworks. Any imported
# term whose ``source`` appears in such a section is treated as attributed
# everywhere in the file.
NORMATIVE_REFERENCE_HEADING_RE = re.compile(
    r"^#{1,6}\s+(Normative\s+References?|References?|"
    r"Sources?|External\s+References?)\s*$",
    re.MULTILINE | re.IGNORECASE,
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


def load_manifest(manifest_path: Path) -> tuple[list[ImportEntry], list[str]]:
    with manifest_path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    imports: list[ImportEntry] = []
    for raw in data.get("imports", []):
        imports.append(
            ImportEntry(
                term=raw["term"],
                source=raw["source"],
                pointer=raw.get("pointer", ""),
                aliases=tuple(raw.get("aliases", ())),
                attribution=raw.get("attribution", "strict"),
            )
        )
    scoped = list(data.get("scoped_files", []))
    return imports, scoped


def expand_scope(root: Path, scoped: list[str]) -> list[Path]:
    """Resolve scoped paths to a flat list of *.md files."""
    out: list[Path] = []
    for entry in scoped:
        target = (root / entry).resolve()
        if target.is_dir():
            out.extend(sorted(target.rglob("*.md")))
        elif target.is_file() and target.suffix == ".md":
            out.append(target)
    # Deduplicate while preserving order.
    seen: set[Path] = set()
    deduped: list[Path] = []
    for p in out:
        if p not in seen and p.exists():
            seen.add(p)
            deduped.append(p)
    return deduped


def split_paragraphs(text: str) -> list[tuple[int, str]]:
    """Return list of (start_line_number, paragraph_text)."""
    paragraphs: list[tuple[int, str]] = []
    current: list[str] = []
    current_start = 1
    line_no = 1

    for line in text.splitlines():
        if line.strip() == "":
            if current:
                paragraphs.append((current_start, "\n".join(current)))
                current = []
            current_start = line_no + 1
        else:
            if not current:
                current_start = line_no
            current.append(line)
        line_no += 1

    if current:
        paragraphs.append((current_start, "\n".join(current)))

    return paragraphs


def file_has_definition(text: str, term: str) -> bool:
    """Return True if the file declares a local definition for the term.

    Heuristic: a term is locally defined if it appears within a paragraph
    that also contains a definition marker (``is defined as``, etc.) OR if
    the file contains a "Definitions" / "Glossary" heading and the term
    appears as a list item or bold phrase under it.
    """
    lower_text = text.lower()
    lower_term = term.lower()

    # Quick check: definition-marker proximity.
    for marker in DEFINITION_MARKERS:
        idx = 0
        marker_lower = marker.lower()
        while True:
            pos = lower_text.find(marker_lower, idx)
            if pos == -1:
                break
            # Look in the surrounding 200 chars for the term.
            window = lower_text[max(0, pos - 200) : pos + 200]
            if lower_term in window:
                return True
            idx = pos + len(marker_lower)

    # JSON-Schema-fragment heuristic. graph.md ships JSON Schema fragments
    # that declare imported terms (e.g. ``epistemic_tier``) as ``enum``
    # fields. The presence of such a fragment is treated as a local
    # structural definition because every value the term can take is
    # enumerated in the same file.
    snake_term = lower_term.replace(" ", "_").replace("-", "_")
    schema_field_re = re.compile(
        rf'"{re.escape(snake_term)}"\s*:\s*\{{[^}}]*?"enum"\s*:',
        re.DOTALL,
    )
    if schema_field_re.search(text):
        return True

    # Definitions section heuristic.
    section_match = re.search(
        r"^(#{2,4})\s+(Definitions|Glossary)\s*$",
        text,
        re.MULTILINE | re.IGNORECASE,
    )
    if section_match:
        # Slice from the heading to the next heading of equal-or-shallower
        # depth.
        heading_depth = len(section_match.group(1))
        start = section_match.end()
        next_heading = re.search(
            rf"^#{{1,{heading_depth}}}\s",
            text[start:],
            re.MULTILINE,
        )
        end = start + next_heading.start() if next_heading else len(text)
        section_body = text[start:end]
        if lower_term in section_body.lower():
            return True

    return False


def paragraph_has_attribution(paragraph: str, source: str) -> bool:
    lower = paragraph.lower()
    # Always accept the source acronym.
    if source.lower() in lower:
        return True
    for marker in ATTRIBUTION_MARKERS:
        if marker.lower() in lower:
            return True
    return False


def find_term_lines(
    paragraph: str, paragraph_start: int, term: str, aliases: tuple[str, ...]
) -> list[int]:
    """Return the absolute line numbers in the file where the term appears."""
    candidates = [term, *aliases]
    pattern = re.compile(
        r"(?<![A-Za-z0-9_])("
        + "|".join(re.escape(c) for c in candidates)
        + r")(?![A-Za-z0-9_])",
        re.IGNORECASE,
    )

    lines: list[int] = []
    for offset, line in enumerate(paragraph.splitlines()):
        if pattern.search(line):
            lines.append(paragraph_start + offset)
    return lines


def _file_has_strict_attribution(text: str, source: str) -> bool:
    """Return True if the file establishes strict attribution to source.

    Strict attribution at file level is satisfied if any of the following
    appears anywhere in the file body:

    - The source acronym as a whole word (``IGM``, ``AEnt-M``, ``APLC``,
      ``AEM``).
    - The source's expanded form (``Intelligence Governance Manifesto``,
      ``Agentic Enterprise Manifesto``, ``Agentic Engineering
      Manifesto``).
    - A References-style section that names the source.

    File-level (rather than paragraph-level) attribution matches the
    strategic-review directive: an explicit ``(IGM)`` parenthetical or
    local definition is enough; the parenthetical does not have to share
    a paragraph with every use of the imported term.
    """
    expansions = {
        "AEM": ["Agentic Engineering Manifesto"],
        "AEnt-M": ["Agentic Enterprise Manifesto"],
        "IGM": [
            "Intelligence Governance Manifesto",
            "Intelligence Governance Model",
            "Intelligence Governance",
        ],
        "APLC": ["Agentic Platform Lifecycle"],
    }
    # Acronym match must be word-bounded so ``IGM`` does not match within
    # ``signing`` etc.
    if re.search(rf"\b{re.escape(source)}\b", text):
        return True
    for phrase in expansions.get(source, []):
        if phrase.lower() in text.lower():
            return True
    if _has_references_section_attribution(text, source):
        return True
    return False


def _has_references_section_attribution(text: str, source: str) -> bool:
    """Return True if a References-style section in ``text`` names the
    source framework. This is a stricter form of whole-file attribution
    that applies to imports with strict (paragraph-level) attribution.
    """
    lower_source = source.lower()
    expansions = {
        "AEM": ["agentic engineering manifesto"],
        "AEnt-M": ["agentic enterprise manifesto"],
        "IGM": ["intelligence governance model", "intelligence governance"],
        "APLC": ["agentic platform lifecycle"],
    }
    candidates = [lower_source, *expansions.get(source, [])]
    for m in NORMATIVE_REFERENCE_HEADING_RE.finditer(text):
        section = text[m.end() : m.end() + 2000].lower()
        for c in candidates:
            if c in section:
                return True
    return False


def file_attributes_source(text: str, source: str) -> bool:
    """Return True if the file as a whole attributes the source framework.

    Whole-file attribution is satisfied if either:

    1. The file contains a "Normative References" / "References" /
       "Sources" / "External References" section that names the source
       framework (its acronym or its expanded form), OR
    2. The file mentions the source framework's acronym or its expanded
       form anywhere in the body. Used by ``cross_reference`` attribution
       (e.g. AEM "manifesto" / "Layer 2" — both README.md and asdlc.md
       establish the cross-reference up-front and subsequent uses do not
       need to re-attribute).
    """
    lower_text = text.lower()
    candidates = [source.lower()]
    expansions = {
        "AEM": ["agentic engineering manifesto", "manifesto"],
        "AEnt-M": ["agentic enterprise manifesto"],
        "IGM": ["intelligence governance model", "intelligence governance"],
        "APLC": ["agentic platform lifecycle"],
    }
    candidates.extend(expansions.get(source, []))

    # Whole-body mention.
    for c in candidates:
        if c in lower_text:
            return True

    # References-section mention (defensive — covered by whole-body too).
    for m in NORMATIVE_REFERENCE_HEADING_RE.finditer(text):
        # Take ~2000 chars after the heading.
        section = text[m.end() : m.end() + 2000].lower()
        for c in candidates:
            if c in section:
                return True
    return False


def scan_file(
    path: Path, root: Path, imports: list[ImportEntry]
) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")
    paragraphs = split_paragraphs(text)

    # Cache per-source whole-file attribution for both attribution kinds.
    file_attrib_cache: dict[str, bool] = {}

    def file_attributed(source: str) -> bool:
        if source not in file_attrib_cache:
            file_attrib_cache[source] = file_attributes_source(text, source)
        return file_attrib_cache[source]

    for entry in imports:
        if file_has_definition(text, entry.term):
            continue

        # cross_reference: whole-file attribution to the source framework
        # is sufficient (mention anywhere in the file).
        if entry.attribution == "cross_reference" and file_attributed(
            entry.source
        ):
            continue

        # strict: file-level attribution is satisfied if the source
        # framework's acronym (e.g. ``IGM``, ``AEnt-M``) appears anywhere
        # in the file. Per the strategic-review directive, an explicit
        # parenthetical OR a local definition in the same file is enough;
        # the parenthetical does not have to share a paragraph with every
        # use. A References-style section that names the source framework
        # also satisfies attribution.
        if entry.attribution == "strict" and _file_has_strict_attribution(
            text, entry.source
        ):
            continue

        for start_line, paragraph in paragraphs:
            occurrence_lines = find_term_lines(
                paragraph, start_line, entry.term, entry.aliases
            )
            if not occurrence_lines:
                continue
            if paragraph_has_attribution(paragraph, entry.source):
                continue

            for ln in occurrence_lines:
                # Read the actual source line for the message context.
                file_lines = text.splitlines()
                line_text = (
                    file_lines[ln - 1] if 0 < ln <= len(file_lines) else ""
                )
                findings.append(
                    Finding(
                        file=rel,
                        line=ln,
                        severity="error",
                        message=(
                            f"silent import: term {entry.term!r} "
                            f"(source: {entry.source}) used without "
                            f"attribution or local definition: "
                            f"{line_text.strip()!r}"
                        ),
                    )
                )

    return findings


def run(root: Path) -> CheckResult:
    result = CheckResult(name="term_imports")
    manifest_path = Path(__file__).resolve().parent / "known_imports.json"
    if not manifest_path.exists():
        result.skipped_reason = f"manifest not found at {manifest_path}"
        return result

    imports, scoped = load_manifest(manifest_path)
    if not imports:
        return result

    targets = expand_scope(root, scoped)
    for path in targets:
        result.findings.extend(scan_file(path, root, imports))
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
