# /review-status — Check ASDLC Review Progress

Show which output files exist, which are missing, and what wave a review is on.

> **Status: ASDLC retargeting complete. Skill is invokable.**
> The expected file list below is the live ASDLC topology (14 Wave 1a + 3 Wave 1b
> + 1 Wave 2 + 1 Wave 3 = 19 output files; `_review_04a_adoption.md`,
> `_review_04b_governance.md`, `_review_05a_readiness.md`, and
> `_review_08a_domains.md` are intermediate files lifted by Wave 1b synthesis
> agents and are not direct inputs to the merge agent).

## Usage

```
/review-status FRAMEWORK_LOWER
```

## Arguments

| Argument | Required | Description |
| --- | --- | --- |
| `FRAMEWORK_LOWER` | Yes | Lowercase underscore slug of the framework (e.g., `abcd`) |

---

## Execution

### Step 1 — Locate output files

Check for the following files in `{FRAMEWORK_LOWER}/` relative to the current working directory.

**Wave 1a outputs (14 files):**

| File | Agent |
| --- | --- |
| `{FRAMEWORK_LOWER}_review_01_quick_overview.md` | 01 |
| `{FRAMEWORK_LOWER}_review_02_layer_l1.md` … `_l4.md` (4 files) | 02-l1 … 02-l4 (parallel) |
| `{FRAMEWORK_LOWER}_review_02_gate_g1.md` … `_g3.md` (3 files) | 02-g1 … 02-g3 (parallel) |
| `{FRAMEWORK_LOWER}_review_03_gates_dods.md` | 03 |
| `{FRAMEWORK_LOWER}_review_04a_adoption.md` | 04a |
| `{FRAMEWORK_LOWER}_review_04b_governance.md` | 04b |
| `{FRAMEWORK_LOWER}_review_05a_readiness.md` | 05a |
| `{FRAMEWORK_LOWER}_review_07_guardrails_security.md` | 07 |
| `{FRAMEWORK_LOWER}_review_08a_domains.md` (intermediate; lifted by 08b) | 08a |

**Wave 1b outputs (3 files):**

| File | Agent |
| --- | --- |
| `{FRAMEWORK_LOWER}_review_04_adoption_governance.md` | 04c |
| `{FRAMEWORK_LOWER}_review_05_readiness_industry.md` | 05b |
| `{FRAMEWORK_LOWER}_review_08_enterprise_guardrails.md` (canonical Part 14) | 08b |

**Wave 2 output (1 file):**

| File | Agent |
| --- | --- |
| `{FRAMEWORK_LOWER}_review_06_strengths_gaps.md` | 06 |

**Wave 3 output (1 file):**

| File | Agent |
| --- | --- |
| `{FRAMEWORK_LOWER}_asdlc_alignment_review_merged.md` | 09 |

### Step 2 — Check each file

For each expected file: check existence and size.
- **Present and non-empty** (≥20 lines): ✓
- **Present but empty or tiny** (<20 lines): ⚠ (corrupted / incomplete)
- **Missing**: ✗

### Step 3 — Report status

Print a table of results, then a wave summary:

```
Review status: {FRAMEWORK_LOWER}/
ASDLC: arnaudgelas/asdlc@{ASDLC_HASH_SHORT}
  (resolve from the header of any existing output file, or run git in the ASDLC path)

Wave 1a  [✓ / ✗]  (N/14 files present and non-empty)
  ✓ _review_01_quick_overview.md
  ✓ _review_02_layer_l1.md … l4.md (4/4)
  ✓ _review_02_gate_g1.md … g3.md (3/3)
  ✗ _review_03_gates_dods.md   ← MISSING
  ...

Wave 1b  [waiting / ✓ / ✗]
  ...

Wave 2   [waiting / ✓ / ✗]
Wave 3   [waiting / ✓ / ✗]

Suggested next action:
  Re-run agent 03 (missing _review_03_gates_dods.md), then proceed to Wave 1b.
```

If all 19 files are present and non-empty:
```
✓ Review complete — all 19 files present.
  Merged review: {FRAMEWORK_LOWER}_asdlc_alignment_review_merged.md
```

### Step 4 — Extract ASDLC hash (optional)

If any output file exists, extract the ASDLC provenance line from its header:
```
ASDLC: arnaudgelas/asdlc@{HASH}
```
Display it in the status report so the user knows which ASDLC version produced these outputs.
