#!/usr/bin/env python3
"""Check that ASDLC source documents do not use banned hedge/marketing tokens.

The banned-token list is defined in ``review/prompt.md`` under the
"Banned soft language" section. The list is split into a core set (applies
to every output) and an extended set (originally scoped to specific review
agents). The strategic review found that the rule was applied to review
agents but not to ASDLC source documents themselves; this checker closes
that gap.

The script parses ``review/prompt.md`` heuristically to extract the token
list, then scans every other ``*.md`` file for occurrences. Each match is
reported as ``file:line: severity: <message including line context>``.

Policy tuning notes (post-strategic-review hardening):

- The bare token ``may`` is removed from the effective banned list. RFC 2119
  uses ``MAY`` as normative vocabulary and bare ``may`` is ordinary English;
  the strict ban produced almost-pure noise. Multi-word hedges that do
  signal hedging (``may potentially``, ``could potentially``) remain banned.
- ``enables`` only fires when used without an immediate object that names
  what is enabled. A pattern like ``enables the correlation`` is allowed;
  bare ``it enables.`` is not.
- ``mature`` only fires when not adjacent to an explicit phase number. The
  prompt itself defines the rule as ``mature (without phase number)``; this
  checker now honours that qualifier.
- Tokens inside fenced code blocks and inline code spans (``backticks``)
  are ignored. Banned-token policy is a prose policy.
- Per-file exceptions live in ``FILE_EXEMPTIONS``; documentation files
  that legitimately enumerate banned tokens (the lint script README, the
  review-system README, the prompt that defines the list) are exempted.

False positives are common because some banned tokens are ordinary English.
Suppress them by:

- Adding a per-file exemption to ``FILE_EXEMPTIONS`` for files that quote
  external material directly.
- Adding a token to ``GLOBAL_TOKEN_EXEMPTIONS`` if the project decides a
  token is no longer banned.
- Annotating a line with the inline marker ``<!-- lint:allow-banned-token
  reason -->`` to suppress that specific line.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable


# Files that are allowed to contain banned tokens (e.g. the prompt that
# defines the ban itself, license texts, third-party quotes). Path is
# relative to repo root.
FILE_EXEMPTIONS: set[str] = {
    "review/prompt.md",
    "review/README.md",
    "scripts/check_banned_tokens.py",
    "scripts/README.md",
}

# Path prefixes that are exempt. Review prompts quote example phrasing.
DIR_EXEMPTIONS: tuple[str, ...] = (
    "review/prompts/",
    "review/skills/",
    ".claude/",
)

# Tokens that the project has decided to permit globally despite appearing
# in review/prompt.md. ``may`` is removed because RFC 2119 uses MAY as
# normative vocabulary and bare ``may`` is ordinary English; the multi-word
# hedge ``may potentially`` is still banned via PHRASE_TOKENS below. The
# checker also applies context-aware narrowing for ``enables`` and
# ``mature`` (see scan_file).
GLOBAL_TOKEN_EXEMPTIONS: set[str] = {"may"}

# Per-file token allowances. Files that legitimately need to use a specific
# banned token in prose (e.g. registry tables that mention "blocking" near
# "conditional"). Map of file path (relative to repo root) -> set of
# permitted tokens.
PER_FILE_TOKEN_ALLOWANCES: dict[str, set[str]] = {
    # The gate registry quotes "blocking" / "conditional" as a structural
    # outcome enumeration; these are not hedge-words there.
    "governance/gate-registry.md": {"conditional"},
}

# Multi-word hedges that should always fire even when their constituent
# tokens are individually exempted. The prompt lists ``could potentially``
# in the core list; ``may potentially`` is added here because removing
# bare ``may`` from the banned list must not also exempt ``may potentially``.
EXTRA_PHRASE_BANS: tuple[str, ...] = (
    "may potentially",
)

# Inline suppression marker.
INLINE_SUPPRESS = "lint:allow-banned-token"


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


def parse_banned_tokens(prompt_path: Path) -> tuple[list[str], list[str]]:
    """Parse the banned-token section of review/prompt.md.

    Returns ``(core_tokens, extended_tokens)``. Each token is a literal
    phrase as written in the prompt (lowercased, leading/trailing whitespace
    stripped, surrounding backticks removed).
    """
    if not prompt_path.exists():
        return [], []

    text = prompt_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    core: list[str] = []
    extended: list[str] = []

    in_section = False
    current_bucket: list[str] | None = None

    for line in lines:
        stripped = line.strip()
        # Detect the section header.
        if re.match(r"^##\s+Banned soft language", stripped, re.IGNORECASE):
            in_section = True
            continue
        if not in_section:
            continue
        # Stop at the next top-level section.
        if stripped.startswith("## ") and not stripped.lower().startswith(
            "## banned"
        ):
            break

        # Bucket routing by sub-headers in bold.
        if "**Core banned list" in line:
            current_bucket = core
            continue
        if "**Extended banned list" in line:
            current_bucket = extended
            continue

        if current_bucket is None:
            continue

        # Token line: "- `tok1`, `tok2`, `tok3`, ..." or sentences starting
        # with "- ". Extract every backtick-wrapped token.
        if stripped.startswith("- "):
            tokens = re.findall(r"`([^`]+)`", stripped)
            for tok in tokens:
                normalised = tok.strip().lower()
                if normalised:
                    current_bucket.append(normalised)

    return core, extended


def is_exempt(rel: str) -> bool:
    if rel in FILE_EXEMPTIONS:
        return True
    return any(rel.startswith(prefix) for prefix in DIR_EXEMPTIONS)


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        yield path


def compile_token_pattern(tokens: list[str]) -> re.Pattern[str] | None:
    """Build a single regex that matches any of the tokens as a phrase."""
    cleaned = [t for t in tokens if t and t not in GLOBAL_TOKEN_EXEMPTIONS]
    cleaned.extend(EXTRA_PHRASE_BANS)
    if not cleaned:
        return None
    # Sort longest first so multi-word phrases match before single words.
    cleaned.sort(key=len, reverse=True)
    parts = []
    for token in cleaned:
        # If token contains spaces, match as phrase with flexible whitespace.
        # Word-boundary at the edges where token starts/ends with a word char.
        escaped = re.escape(token).replace(r"\ ", r"\s+")
        left = r"\b" if token[0].isalnum() else ""
        right = r"\b" if token[-1].isalnum() else ""
        parts.append(f"{left}{escaped}{right}")
    pattern = "(?P<token>" + "|".join(parts) + ")"
    return re.compile(pattern, re.IGNORECASE)


# Regex used to strip inline ``code spans`` from a line before scanning.
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")

# Regex matching a phase-number reference adjacent to ``mature``. The
# strategic-review directive is "Phase 3 mature" passes; "mature
# governance" fires.
_MATURE_PHASE_RE = re.compile(
    r"\bphase\s*[0-9]+\b|\b[0-9]+\s*phase\b",
    re.IGNORECASE,
)

# Regex testing whether ``enables`` is followed by an object that names
# what is enabled. We accept any of: a noun-phrase continuation (one or
# more words on the same line), a definite/indefinite article + word, or
# a ``the`` / ``a`` / ``an`` followed by anything. Bare ``enables.`` or
# ``enables,`` at end of clause fires.
_ENABLES_OBJECT_RE = re.compile(
    r"\benables?\s+[A-Za-z][A-Za-z0-9_-]+",
    re.IGNORECASE,
)


def _strip_inline_code(line: str) -> str:
    """Replace inline `code spans` with spaces of equal length.

    Preserving length keeps regex match offsets meaningful relative to the
    original line, but masks the content so banned tokens inside backticks
    do not fire.
    """
    return _INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), line)


def _is_token_in_inline_code(line: str, start: int, end: int) -> bool:
    """Return True if [start:end] in line falls inside a `code span`."""
    for m in _INLINE_CODE_RE.finditer(line):
        if m.start() <= start and end <= m.end():
            return True
    return False


def _should_skip_token(token: str, line: str) -> bool:
    """Apply context-aware narrowing for tokens that have qualifiers in
    the canonical prompt list.

    Returns True when the occurrence should NOT be reported as a finding.
    """
    lower = token.lower()
    # ``mature (without phase number)`` — pass when phase number is nearby.
    if lower == "mature" and _MATURE_PHASE_RE.search(line):
        return True
    # ``enables (without naming what is enabled)`` — pass when an object
    # follows the verb on the same line.
    if lower in {"enables", "enable"} and _ENABLES_OBJECT_RE.search(line):
        return True
    return False


def scan_file(
    path: Path,
    root: Path,
    pattern: re.Pattern[str],
    extended_set: set[str],
) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    if is_exempt(rel):
        return []

    per_file_allowed = PER_FILE_TOKEN_ALLOWANCES.get(rel, set())

    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")

    in_code_fence = False

    for lineno, line in enumerate(text.splitlines(), start=1):
        # Toggle fenced-code state. Banned-token rules apply to prose only.
        if line.lstrip().startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue

        if INLINE_SUPPRESS in line:
            continue

        for match in pattern.finditer(line):
            token = match.group("token").lower()
            # Skip tokens that fall inside inline `code spans`.
            if _is_token_in_inline_code(line, match.start(), match.end()):
                continue
            # Per-file allowances.
            if token in per_file_allowed:
                continue
            # Context-aware narrowing for ``mature`` and ``enables``.
            if _should_skip_token(token, line):
                continue
            tier = "extended" if token in extended_set else "core"
            findings.append(
                Finding(
                    file=rel,
                    line=lineno,
                    severity="error",
                    message=(
                        f"banned-{tier} token {token!r} found: "
                        f"{line.strip()!r}"
                    ),
                )
            )

    return findings


def run(root: Path) -> CheckResult:
    result = CheckResult(name="banned_tokens")
    prompt_path = root / "review" / "prompt.md"
    core, extended = parse_banned_tokens(prompt_path)

    if not core and not extended:
        result.skipped_reason = (
            f"could not parse banned-token list from {prompt_path}"
        )
        return result

    pattern = compile_token_pattern(core + extended)
    if pattern is None:
        return result

    extended_set = set(extended)
    for path in iter_markdown_files(root):
        result.findings.extend(scan_file(path, root, pattern, extended_set))

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
