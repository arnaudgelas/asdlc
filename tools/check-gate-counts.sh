#!/usr/bin/env bash
# check-gate-counts.sh — regenerate every ASDLC gate/registry count from its
# authoritative document and flag any overview prose that states a different
# number.
#
# Why this exists: D-31 recorded nine instances of overview-vs-detail count
# drift, all with the same shape — an overview document restates a count in
# prose instead of pointing at (or being generated from) the document that
# actually enumerates the items. Hand-correcting each instance individually is
# the mechanism that produced the drift in the first place (a later edit to
# the authoritative list does not touch the prose that quoted its old count).
# This script is the alternative: it computes the authoritative count by
# grepping the source of truth, and greps every other ASDLC document for
# number-words tied to the same gate so a mismatch fails the check instead of
# silently going stale.
#
# Usage:
#   asdlc/tools/check-gate-counts.sh            # from repo root or asdlc/
#
# Exit status: 0 if every checked mention agrees with its authority, 1 if any
# mismatch is found. Run it after editing any of the authoritative documents
# listed below, or any document that restates one of these counts.
#
# Scope: this script only reads. It never edits files.

set -uo pipefail

# Resolve asdlc/ and the corpus root regardless of invocation directory.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASDLC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CORPUS_ROOT="$(cd "$ASDLC_DIR/.." && pwd)"

fail=0
num2word() {
  case "$1" in
    5) echo five ;; 6) echo six ;; 7) echo seven ;; 8) echo eight ;;
    9) echo nine ;; 20) echo twenty ;; 22) echo twenty-two ;;
    24) echo twenty-four ;; 26) echo twenty-six ;;
    *) echo "$1" ;;
  esac
}

# --- Authoritative counts, each derived by a command against the document
#     that actually enumerates the items (never transcribed) --------------

aem_dod_file="$CORPUS_ROOT/agentic-engineering-manifesto/manifesto/manifesto-done.md"
if [ -f "$aem_dod_file" ]; then
  aem_dod_count=$(sed -n '/^A change is \*\*done\*\* when it is:/,/^Anything less is not done/p' "$aem_dod_file" \
    | grep -c "^\*\*[A-Za-z].*\*\* —")
else
  aem_dod_count=""
fi

spec_readiness_count=$(grep -c "^### Condition" "$ASDLC_DIR/specification-readiness.md")

release_gate_count=$(sed -n '/^## Predictive Gate Clearing/,/^## Agent Participation in Release Gate/p' \
  "$ASDLC_DIR/release-governance.md" | grep -c "^### [0-9]*\. ")

operational_dod_count=$(sed -n '/^## The Operational DoD Conditions/,/^## Phase-Calibrated/p' \
  "$ASDLC_DIR/operations/dod.md" | grep -c "^\*\*.*\.\*\*$")

node_types_count=$(sed -n '/^## Node Types/,/^## Edge Types/p' "$ASDLC_DIR/governance/graph.md" | grep -c "^### ")

queries_count=$(grep -c "^\*\*Q-" "$ASDLC_DIR/governance/queries.md")

echo "Authoritative counts (computed, not transcribed):"
echo "  AEM Engineering DoD conditions   : ${aem_dod_count:-UNAVAILABLE (manifesto-done.md not found)}  <- manifesto-done.md"
echo "  ASDLC Specification Readiness    : $spec_readiness_count  <- specification-readiness.md"
echo "  ASDLC Release Gate               : $release_gate_count  <- release-governance.md"
echo "  ASDLC Operational Readiness      : $operational_dod_count  <- operations/dod.md"
echo "  Governance graph node types      : $node_types_count  <- governance/graph.md"
echo "  Governance graph canonical queries: $queries_count  <- governance/queries.md"
echo

# --- Carriers: every asdlc/ document that restates one of these counts in
#     prose. Each line below names the authoritative variable it must agree
#     with; the regex is deliberately narrow (word boundary + keyword) so it
#     does not fire on unrelated numbers in the same file. ------------------

# A carrier is a line that states an actual COUNT next to the gate's keyword
# phrase — i.e. a number-word immediately before the phrase. A line that
# merely mentions "release gate conditions" with no number attached is not a
# carrier of a count and must not be flagged. This is a grep over asdlc/,
# excluding this script's own directory so the script does not check itself.
NUMWORD_RE='(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty(-[a-z]+)?)'

check_carrier() {
  local label="$1" authoritative="$2" phrase="$3"
  local word
  word="$(num2word "$authoritative")"
  local hits
  hits=$(grep -rniE "${NUMWORD_RE}[-[:space:]]+${phrase}" "$ASDLC_DIR" 2>/dev/null | grep -v "/tools/check-gate-counts.sh:")
  if [ -z "$hits" ]; then
    echo "  (no number-bearing carriers found for $label by grep -riE '${NUMWORD_RE}[-[:space:]]+${phrase}')"
    return
  fi
  while IFS= read -r hit; do
    local text
    text="${hit#*:*:}"
    if echo "$text" | grep -qiE "\\b${word}\\b"; then
      echo "  OK    $label: $hit"
    else
      echo "  DRIFT $label (expected '$word' / $authoritative): $hit"
      fail=1
    fi
  done <<< "$hits"
}

echo "Carrier check — AEM Engineering DoD conditions (authoritative: $aem_dod_count):"
check_carrier "AEM DoD" "$aem_dod_count" "(engineering )?Definition of Done condition"
echo

echo "Carrier check — ASDLC Specification Readiness (authoritative: $spec_readiness_count):"
check_carrier "Spec Readiness" "$spec_readiness_count" "gate conditions? (naturally|defined|satisf)"
check_carrier "Spec Readiness" "$spec_readiness_count" "conditions? (satisfies|are satisfied)"
echo

echo "Carrier check — ASDLC Release Gate (authoritative: $release_gate_count):"
check_carrier "Release Gate" "$release_gate_count" "release gate conditions"
check_carrier "Release Gate" "$release_gate_count" "condition evidence bundle"
echo

echo "Carrier check — ASDLC Operational Readiness (authoritative: $operational_dod_count):"
check_carrier "Operational Readiness" "$operational_dod_count" "operational readiness gate conditions"
check_carrier "Operational Readiness" "$operational_dod_count" "operational DoD conditions? remain"
check_carrier "Operational Readiness" "$operational_dod_count" "conditions? required"
echo

if [ "$fail" -ne 0 ]; then
  echo "RESULT: DRIFT FOUND — one or more overview mentions disagree with their authority."
  exit 1
else
  echo "RESULT: all checked mentions agree with their authoritative count."
  exit 0
fi
