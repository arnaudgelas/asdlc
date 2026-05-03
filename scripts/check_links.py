#!/usr/bin/env python3
"""Check that markdown links resolve to files on disk.

Scans every ``*.md`` file for links of the form ``[text](path)``. For
relative paths (no URL scheme), the target is resolved relative to the
source file and must exist on disk. Anchors (``#section``) are accepted but
not validated.

A small alias table handles paths discovered in the strategic review where
the document refers to a sibling-framework file by short name. Aliases map
the short name to a path relative to the ASDLC repo root.

Suppress a false positive by adding the path to ``KNOWN_ALIASES`` (with a
correct target) or by adding the source file to ``WHITELIST_FILES``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable


# Aliases for sibling-framework references that resolve outside the ASDLC
# repo. Keys are the link target as written in the doc; values are the path
# the link is intended to resolve to (relative to the ASDLC repo root). The
# checker treats an aliased path as resolved if the target exists on disk.
KNOWN_ALIASES: dict[str, str] = {
    "companion-re-framework.md": "../companion/re-framework.md",
    "adoption-metrics.md": "../adoption/metrics.md",
    "adoption-roles.md": "../adoption/roles.md",
}

# Files exempt from link scanning. Path is relative to repo root.
WHITELIST_FILES: set[str] = {
    "scripts/check_links.py",
    "scripts/README.md",
}

# Match markdown links: [text](target). Avoid matching reference-style
# definitions. Allow nested parentheses sparsely (rare).
LINK_PATTERN = re.compile(r"\[(?P<text>[^\]]+)\]\((?P<target>[^)\s]+)\)")

URL_SCHEME_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9+\-.]*:")


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


def is_external(target: str) -> bool:
    if URL_SCHEME_PATTERN.match(target):
        return True
    if target.startswith("//"):
        return True
    return False


def resolve_link(
    source: Path, target: str, root: Path
) -> tuple[Path | None, str | None]:
    """Return (resolved_path, alias_used). Anchor portion is stripped."""
    if "#" in target:
        target_path, _ = target.split("#", 1)
    else:
        target_path = target

    if not target_path:
        # Pure anchor (#section); skip.
        return None, None

    alias_used: str | None = None
    if target_path in KNOWN_ALIASES:
        alias_used = target_path
        candidate = (root / KNOWN_ALIASES[target_path]).resolve()
    else:
        candidate = (source.parent / target_path).resolve()

    return candidate, alias_used


def scan_file(path: Path, root: Path) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    if rel in WHITELIST_FILES:
        return []

    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")

    for lineno, line in enumerate(text.splitlines(), start=1):
        for match in LINK_PATTERN.finditer(line):
            target = match.group("target")
            if is_external(target):
                continue

            resolved, alias_used = resolve_link(path, target, root)
            if resolved is None:
                continue

            if not resolved.exists():
                if alias_used is not None:
                    findings.append(
                        Finding(
                            file=rel,
                            line=lineno,
                            severity="error",
                            message=(
                                f"alias {alias_used!r} resolves to "
                                f"{resolved} which does not exist"
                            ),
                        )
                    )
                else:
                    findings.append(
                        Finding(
                            file=rel,
                            line=lineno,
                            severity="error",
                            message=(
                                f"broken link {target!r} -> {resolved} "
                                f"(does not exist)"
                            ),
                        )
                    )

    return findings


def run(root: Path) -> CheckResult:
    result = CheckResult(name="links")
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
