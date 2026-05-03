# /review — ASDLC Framework Alignment Review

Run a complete Agentic Software Delivery Lifecycle (ASDLC) alignment review of a framework across 14 specialised agent roles (with 4 parallel layer agents and 3 parallel gate agents) in four waves.

> **Status: ASDLC retargeting complete. Skill is invokable.**
> The orchestrator (`prompt.md`) and the 14 sub-prompts under `prompts/` are retargeted
> from the AEM review system to ASDLC. Sub-prompt Part numbering, weighting, and
> source-artefact lists match `prompt.md`. Gate condition counts and titles are
> sourced from `governance/gate-registry.md`. The self-referential-grading boundary
> is documented in `review/README.md`: this skill grades external frameworks against
> ASDLC's own assertions, not against externally-anchored regulatory source-of-truth.
> The operator must verify ASDLC's own claims against the underlying regulations or
> engineering standards in `[[DOMAIN_FILE]]` separately.

## Usage

```
/review FRAMEWORK ORGANIZATION INDUSTRY DOMAIN_FILE [PRIOR_REVIEWS]
```

## Arguments

| Argument | Required | Format | Example |
| --- | --- | --- | --- |
| `FRAMEWORK` | Yes | Name as it appears in the framework's own docs | `abcd` |
| `ORGANIZATION` | Yes | Client organisation name | `ABCD.xyz` |
| `INDUSTRY` | Yes | Industry + key regulations (quote if contains spaces) | `"European insurance — DORA, Solvency II, EU AI Act"` |
| `DOMAIN_FILE` | Yes | Path under `domains/` of the ASDLC repository (e.g., `domains/insurance.md`, `domains/automotive.md`, etc.) | `domains/insurance.md` |
| `PRIOR_REVIEWS` | No | Comma-separated paths to prior merged reviews, or `none` | `abcd/abcd_asdlc_alignment_review_merged.md` |

---

## Execution

### Step 1 — Resolve the ASDLC repository

Determine the ASDLC root path using this priority order:

1. **Current directory:** If the current working directory contains a `review/` subdirectory that itself contains both `prompt.md` and a `prompts/` subdirectory, AND it also contains `asdlc.md`, use the current working directory as the ASDLC root. **Skip clone and pull — the user is already working inside the ASDLC repository or the asdlc/ subtree of the manifesto monorepo. Do not attempt to modify it.**
2. **Env var:** If `ASDLC_PATH` is set, use that value.
3. **Default:** Use `~/.local/share/asdlc`.

**For cases 2 and 3 only — if the resolved path does not exist, clone it:**

```bash
git clone https://github.com/arnaudgelas/asdlc.git {resolved_path}
```

**For cases 2 and 3 only — if the resolved path exists, pull latest:**

```bash
git -C {resolved_path} pull --ff-only
```

If `pull` fails because there are local uncommitted changes, run `git -C {resolved_path} fetch origin` instead and warn:
> ⚠️ The local ASDLC copy has uncommitted changes. Scoring will be based on the working tree, not HEAD. Commit or stash changes before running if you need a reproducible result.

**Verify the ASDLC repository is intact** — these files must exist and be tracked by git (all three resolution paths):

```
{resolved_path}/asdlc.md
{resolved_path}/asdlc-guide.md
{resolved_path}/README.md
{resolved_path}/specification-readiness.md
{resolved_path}/release-governance.md
{resolved_path}/operations/dod.md
{resolved_path}/governance/agents.md
{resolved_path}/review/prompt.md
{resolved_path}/review/prompts/prompt-01-quick-overview.md
```

If any are missing, report the error and stop.

**Tracked-files-only.** Every source file the review system reads MUST be tracked by git on the resolved ASDLC branch. Files that appear only in the working tree (untracked, `??` in `git status`) are NOT in scope, even if they exist on disk.

### Step 1a — Resolve the AEM repository (Layer 2 cross-reference)

ASDLC defers Layer 2 (Engineering Execution) to the Agentic Engineering Manifesto. The Layer 2 review agent (02-l2) needs access to AEM source artefacts.

Determine the AEM root path using this priority order:

1. **Adjacent in monorepo:** If `{resolved_path}/../manifesto.md` exists (i.e., the ASDLC root is the `asdlc/` subtree of the manifesto monorepo), use `{resolved_path}/..` as the AEM root.
2. **Env var:** If `AGENTIC_MANIFESTO_PATH` is set, use that value.
3. **Default:** Use `~/.local/share/agentic-engineering-manifesto`.

**For cases 2 and 3 only — if the resolved AEM path does not exist, clone it:**

```bash
git clone https://github.com/arnaudgelas/agentic-engineering-manifesto.git {aem_path}
```

**For cases 2 and 3 only — if the resolved AEM path exists, pull latest:**

```bash
git -C {aem_path} pull --ff-only
```

**Verify the AEM repository is intact** — these files must exist and be tracked by git:

```
{aem_path}/manifesto.md
{aem_path}/manifesto-principles.md
{aem_path}/manifesto-done.md
{aem_path}/glossary.md
```

If any are missing, report the error and stop. Layer 2 cannot be reviewed without AEM source.

**Note:** The AEM is referenced ONLY by agent 02-l2 (and indirectly by agent 03 when assessing the Engineering DoD). All other agents read ASDLC source only. Out-of-scope corpora (APLC, IGM, AEnt-M, etc.) are not read by any agent — see the out-of-scope rules in `prompt.md`.

---

### Step 2 — Record the ASDLC hash (and AEM hash for cross-reference)

```bash
ASDLC_HASH=$(git -C {resolved_path} rev-parse HEAD)
ASDLC_HASH_SHORT=$(git -C {resolved_path} rev-parse --short HEAD)
AEM_HASH=$(git -C {aem_path} rev-parse HEAD)
AEM_HASH_SHORT=$(git -C {aem_path} rev-parse --short HEAD)
```

Display to the user:
> ASDLC: `arnaudgelas/asdlc@{ASDLC_HASH_SHORT}` ([full hash: {ASDLC_HASH}](https://github.com/arnaudgelas/asdlc/commit/{ASDLC_HASH}))
> AEM (for Layer 2 reference): `arnaudgelas/agentic-engineering-manifesto@{AEM_HASH_SHORT}`

---

### Step 3 — Validate arguments

1. **FRAMEWORK_LOWER** — Derive from `FRAMEWORK`: lowercase, replace spaces and hyphens with underscores. Must match `[a-z0-9_]+`. Report and stop if it does not.

2. **DOMAIN_FILE** — Verify `{resolved_path}/{DOMAIN_FILE}` exists. If not, list available files:
   ```bash
   ls {resolved_path}/domains/*.md
   ```
   Report the missing file and stop.

3. **PRIOR_REVIEWS** — If not `none`, verify each comma-separated path exists (relative to ASDLC root or absolute). Report any missing files and stop.

4. **Output directory** — If `{FRAMEWORK_LOWER}/` does not exist in the current working directory, create it:
   ```bash
   mkdir -p {FRAMEWORK_LOWER}
   ```

---

### Step 4 — Substitute variables

Read `{resolved_path}/review/prompt.md` and replace every `[[VARIABLE]]` placeholder:

| Placeholder | Value |
| --- | --- |
| `[[FRAMEWORK]]` | `{FRAMEWORK}` |
| `[[FRAMEWORK_LOWER]]` | `{FRAMEWORK_LOWER}` |
| `[[FRAMEWORK_VERSION]]` | Ask user, or use `unknown` |
| `[[ORGANIZATION]]` | `{ORGANIZATION}` |
| `[[INDUSTRY]]` | `{INDUSTRY}` |
| `[[DOMAIN_FILE]]` | `{DOMAIN_FILE}` |
| `[[PRIOR_REVIEWS]]` | `{PRIOR_REVIEWS}` (or `none`) |
| `[[ASDLC_HASH]]` | `{ASDLC_HASH}` |
| `[[LAYER_NUMBER]]` | (only for `prompt-02-layer.md`; values 1..4 across the 4 parallel spawns) |
| `[[LAYER_NAME]]` | (only for `prompt-02-layer.md`; per-N short name verbatim from the layer table in `prompt.md`) |
| `[[GATE_NUMBER]]` | (only for `prompt-02-gate.md`; values 1..3 across the 3 parallel spawns) |
| `[[GATE_NAME]]` | (only for `prompt-02-gate.md`; per-N short name verbatim from the gate table in `prompt.md`) |

Do the same substitution for each sub-prompt file when spawning agents (read the file from `{resolved_path}/review/prompts/`, substitute, pass to Agent tool).

**Final scan:** After substitution, verify no `[[...]]` patterns remain. If any are found, report and stop.

---

### Step 5 — Execute wave orchestration

Follow the substituted `prompt.md`'s execution order exactly.

**Wave 1a** — spawn 14 agents using the `Agent` tool with the following batching strategy:
- **Concurrency cap:** Spawn agents in batches of up to 6–8 concurrent agents per batch (Claude's standard concurrent Agent tool capacity). Do not exceed 10 concurrent spawns in a single batch.
- **Batching protocol:** If 14 agents exceed the concurrency cap:
  - Batch 1: agents 01, 02-l1..l4, 02-g1..g3 (8 agents)
  - Batch 2: agents 03, 04a, 04b, 05a, 07, 08a (6 agents)
- **Single-batch alternative:** If the Agent tool can sustain ≥ 14 concurrent spawns, issue all 14 calls in a single message for true parallelism.
- Record which batching strategy is used in the review run manifest.

For each batch, issue all Agent tool calls in the batch simultaneously. Wait for all agents in a batch to complete before spawning the next batch.

Agents in Wave 1a:
- Agent 01: `{resolved_path}/review/prompts/prompt-01-quick-overview.md`
- Agents 02-l1 through 02-l4 (4 parallel spawns): `{resolved_path}/review/prompts/prompt-02-layer.md` — for each layer N in 1..4, substitute `[[LAYER_NUMBER]]` = N and `[[LAYER_NAME]]` = the canonical short name from the layer table in `prompt.md`:
  - L1 `Demand & Value`
  - L2 `Engineering Execution`
  - L3 `Release & Deployment`
  - L4 `Operations & Maintenance`
- Agents 02-g1 through 02-g3 (3 parallel spawns): `{resolved_path}/review/prompts/prompt-02-gate.md` — for each gate N in 1..3, substitute `[[GATE_NUMBER]]` = N and `[[GATE_NAME]]` = the canonical short name from the gate table in `prompt.md`:
  - G1 `Specification Readiness Gate`
  - G2 `Release Gate`
  - G3 `Operational Readiness Gate`
- Agent 03: `{resolved_path}/review/prompts/prompt-03-gates-dods.md` (Engineering DoD + Operational DoD synthesis, cross-gate failure modes)
- Agent 04a: `{resolved_path}/review/prompts/prompt-04a-adoption.md`
- Agent 04b: `{resolved_path}/review/prompts/prompt-04b-governance.md`
- Agent 05a: `{resolved_path}/review/prompts/prompt-05a-readiness.md`
- Agent 07: `{resolved_path}/review/prompts/prompt-07-guardrails-security.md` (Parts 12 + 13)
- Agent 08a: `{resolved_path}/review/prompts/prompt-08a-enterprise-domains.md` (Part 14 §14.1–§14.15 intermediate)

**Wait for Wave 1a:** Glob + Read (first/last 5 lines, ≥20 lines each) for all 14 Wave 1a output files. If any are missing after an agent completes, offer to re-run only that agent (for a missing layer, re-run only the affected `prompt-02-layer.md` instance with the matching `[[LAYER_NUMBER]]` / `[[LAYER_NAME]]`; same for gates).

**Wave 1b** — spawn 3 agents simultaneously:
- Agent 04c: `{resolved_path}/review/prompts/prompt-04c-synthesis.md`
- Agent 05b: `{resolved_path}/review/prompts/prompt-05b-industry.md`
- Agent 08b: `{resolved_path}/review/prompts/prompt-08b-enterprise-synthesis.md` (lifts §14.1–§14.15 from 08a, adds §14.16–§14.19, writes the canonical Part 14 file)

**Wait for Wave 1b:** Verify `_review_04_adoption_governance.md`, `_review_05_readiness_industry.md`, and `_review_08_enterprise_guardrails.md` exist and are non-empty.

**Wave 2:** Spawn agent 06: `{resolved_path}/review/prompts/prompt-06-strengths-gaps.md`.

Wait for `_review_06_strengths_gaps.md`.

**Wave 3:** Spawn agent 09: `{resolved_path}/review/prompts/prompt-09-merge.md`.

Wait for `_asdlc_alignment_review_merged.md`.

---

### Step 6 — Report completion

```
✓ Review complete
  Framework:     {FRAMEWORK} ({FRAMEWORK_VERSION})
  Client:        {ORGANIZATION}
  Domain:        {DOMAIN_FILE}
  ASDLC:         arnaudgelas/asdlc@{ASDLC_HASH_SHORT}
  AEM (L2 ref):  arnaudgelas/agentic-engineering-manifesto@{AEM_HASH_SHORT}
  Output dir:    {FRAMEWORK_LOWER}/
  Files written: {N} files
  Merged review: {FRAMEWORK_LOWER}/{FRAMEWORK_LOWER}_asdlc_alignment_review_merged.md
```

---

## Run manifest

After Wave 3 completes successfully, write `{FRAMEWORK_LOWER}/review_run_manifest.json` containing:

```json
{
  "framework": "{FRAMEWORK}",
  "framework_lower": "{FRAMEWORK_LOWER}",
  "framework_version": "{FRAMEWORK_VERSION}",
  "organization": "{ORGANIZATION}",
  "industry": "{INDUSTRY}",
  "domain_file": "{DOMAIN_FILE}",
  "asdlc_hash": "{ASDLC_HASH}",
  "asdlc_hash_short": "{ASDLC_HASH_SHORT}",
  "aem_hash": "{AEM_HASH}",
  "aem_hash_short": "{AEM_HASH_SHORT}",
  "review_date": "YYYY-MM-DD",
  "layer_mapping": {
    "L1": "Demand & Value",
    "L2": "Engineering Execution",
    "L3": "Release & Deployment",
    "L4": "Operations & Maintenance"
  },
  "gate_mapping": {
    "G1": "Specification Readiness Gate",
    "G2": "Release Gate",
    "G3": "Operational Readiness Gate"
  },
  "weighting_scheme": {
    "L1_demand_value": 12,
    "G1_sr_gate": 10,
    "L2_engineering_execution": 20,
    "G2_release_gate": 12,
    "L3_release_deployment": 8,
    "G3_operational_readiness_gate": 10,
    "L4_operations_maintenance": 10,
    "tier_4_envelope": 6,
    "cross_cutting_governance": 4,
    "finops_security_devsecops": 6,
    "feedback_paths": 2
  },
  "wave_1a_batching_strategy": "single-batch | batch-1-8-agents | batch-2-6-agents",
  "total_output_files": 19,
  "merged_review_file": "{FRAMEWORK_LOWER}/{FRAMEWORK_LOWER}_asdlc_alignment_review_merged.md"
}
```

This manifest allows reproducibility and cross-reference verification across multiple reviews.

---

## Notes

- Output files go into `{FRAMEWORK_LOWER}/` relative to the working directory when the skill is invoked, not relative to the ASDLC root.
- Every output file will contain `ASDLC: arnaudgelas/asdlc@{ASDLC_HASH}` in its header — this is enforced by a hard rule in `prompt.md`.
- To check review progress at any point, use `/review-status {FRAMEWORK_LOWER}`.
- To re-run a specific agent after a failure, invoke `/review` again — agents skip files that already exist and are non-empty (idempotent).

## Troubleshooting

- **Gate condition count mismatch.** Every gate-touching agent (02-g1..g3, 03, 05a, 06, 08a, 08b) reads `governance/gate-registry.md` for canonical condition counts and titles. If an agent's output reports a count that differs from the registry, treat it as an integrity finding (the agent should have surfaced the divergence; if not, the divergence handling in the sub-prompt has regressed).
- **AEM repository not found.** Layer 2 review (agent 02-l2) requires the AEM repository to be resolvable. If you are not in the manifesto monorepo, set `AGENTIC_MANIFESTO_PATH` or accept the default clone location.
- **Out-of-scope corpus error in agent output.** Agents enforce a banned-token rule for APLC/IGM/AEnt-M and related corpora. If an agent output mentions `APLC`, `IGM`, `AEnt-M`, etc., the agent has propagated out-of-scope content; re-run with stricter prompt scrutiny.
- **Self-referential-grading caveat.** The review system grades against ASDLC's own assertions. After running, the operator MUST verify ASDLC's own claims against the underlying regulations or engineering standards in `[[DOMAIN_FILE]]`. The skill does not perform that outer verification. See `review/README.md` § Self-referential-grading disclaimer.
