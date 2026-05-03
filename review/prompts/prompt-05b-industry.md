# Sub-prompt 05b — Industry & Client Assessment + Combined Part 8 + 9

**Purpose.** Produce the canonical combined Part 8 + Part 9 file for `[[FRAMEWORK]]` by lifting Part 8 verbatim from agent 05a's output and adding Part 9 (Industry & Client Assessment) below it. This is a Wave 1b agent — runs after Wave 1a is fully complete.

**Wave:** Wave 1b. Depends on Wave 1a output `_review_05a_readiness.md`. Cannot read other Wave 1b outputs.

**Output file.** `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_05_readiness_industry.md`

**Canonical thresholds.** Severity, score ranges, effort labels, and category weighting are defined in `prompt.md`.

---

## 1. Inputs to read

### 1.1 Mandatory dependency (abort if missing)

- `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_05a_readiness.md` — Part 8 source. Must exist, ≥ 20 lines, contain the canonical readiness verdict line `**ASDLC Readiness: L{N} operating, G{M} routinely passing**`. Extract `{N}` and `{M}` for use in Part 9 deployment-path sequencing.

### 1.2 ASDLC core (mandatory)
- `asdlc.md` — for ASDLC values mapping to gates, Tier 4 mechanics, ASDLC-vs-APLC distinction.
- `README.md` — for industry-specific entry points.
- `governance/agents.md` — for autonomy tier definitions and per-action-class governance.

### 1.3 Layer + gate authoritative artefacts (read for Part 9 detail)
- `specification-readiness.md`, `release-governance.md`, `operations/dod.md` — gate pass conditions referenced in deployment path stages.

### 1.4 Domain file (mandatory — Part 9 is domain-specific)
- `[[DOMAIN_FILE]]` — read in full. **All regulations, articles, use cases, and risk-types in Part 9 MUST be sourced from `[[DOMAIN_FILE]]`.** Do not import financial-services regulations (SR 11-7, DORA, Solvency II, EU AI Act) when `[[DOMAIN_FILE]]` is not a financial-services domain file. Do not invent regulations; do not extrapolate from one domain file to another.

  The recognised set of domain files is:
  - `domains/insurance.md` — insurance (jurisdiction-dependent: NAIC Model Bulletin in US, Solvency II / IDD / EU AI Act in EU).
  - `domains/financial-services.md` — financial services (SR 11-7, DORA, MiFID II, EU AI Act where applicable).
  - `domains/pharma.md` — pharmaceutical and life sciences (GxP, 21 CFR Part 11, EU Annex 11).
  - `domains/aviation.md` — civil aviation (DO-178C, DO-254, EASA / FAA airworthiness).
  - `domains/automotive.md` — automotive (ISO 26262, ISO 21434, UN R155 / R156).
  - `domains/defense-government.md` — defense and government (DoD, NIST 800-53, FedRAMP, ITAR / EAR).
  - `domains/sox.md` — US Sarbanes-Oxley financial-reporting controls (SOX §302, §404, §906; PCAOB AS 2201; ICFR, ITGC).
  - `domains/hipaa.md` — US healthcare PHI (HIPAA Privacy Rule, Security Rule, Breach Notification Rule; 45 CFR Parts 160, 162, 164).
  - `domains/ccpa.md` — California consumer privacy (CCPA / CPRA; 11 CCR §7000 et seq.; CPPA regulations).

  **Dispatch logic.** When `[[DOMAIN_FILE]]` resolves to one of the three new domain files, produce regulatory exposure grounded in that domain only:
  - `domains/sox.md` → SOX-grounded exposure: ICFR design and operating effectiveness; ITGC over agentic systems that touch financial-reporting flows; §302 / §404 management assertions; §906 certifications; PCAOB AS 2201 evidence; segregation-of-duties and change-management controls. Map to `L3 + G2` for release controls and `L4 + G3` for operational controls.
  - `domains/hipaa.md` → HIPAA-grounded exposure: PHI minimum-necessary; Security Rule administrative / physical / technical safeguards; access controls and audit controls (45 CFR §164.312); Breach Notification Rule timelines; Business Associate Agreement obligations. Map to `L1 + G1` for purpose specification, `L3 + G2` for release controls, `L4 + G3` for audit and breach detection.
  - `domains/ccpa.md` → CCPA / CPRA-grounded exposure: consumer rights to know / delete / correct / opt-out of sale or sharing / limit use of sensitive personal information; automated-decision-making disclosure obligations under CPRA regulations; risk assessments and cybersecurity audits where required. Map to `L1 + G1` for purpose and lawful-basis specification, `L4 + G3` for consumer-rights operationalisation.

### 1.5 Cross-cutting context for Part 9
- `governance/agents.md` — autonomy tier ceilings and what governance posture each tier requires.
- `finops-governance.md` — FinOps maturity sequence aligned to industry adoption.
- `security-governance.md` — security baseline obligations relevant to regulated industries.
- `eu-ai-act-mapping.md` — cross-cutting mapping of AutonomyTier × BlastRadiusTier to EU AI Act risk categories (Prohibited / High-risk / Limited-risk / Minimal-risk) and Article obligations (Art. 9 risk management, Art. 10 data governance, Art. 13 transparency, Art. 14 human oversight, Art. 15 accuracy / robustness / cybersecurity, Art. 17 quality management, Art. 26 deployer obligations, Art. 50 transparency to natural persons). **Mandatory read** when `[[INDUSTRY]]` involves EU regulatory exposure.

### 1.6 Scope guard for cross-stack files

When reading regulatory crosswalk, governance, or operational template files, lift only the ASDLC-relevant content. Do not propagate IGM, AEnt-M, or APLC vocabulary, file paths, or coverage statements into Part 9.

### 1.7 Prior reviews
If `[[PRIOR_REVIEWS]]` is not `none`, read them for peer comparison.

---

## 2. Methodology

### 2.1 Part 8 lift mechanics

Lift Part 8 from `_review_05a_readiness.md` verbatim with these heading harmonisations:
- 05a's H1 (`# [[FRAMEWORK]] Review 05a — ...`) is dropped.
- All other content (Verdict line, Tier 4 envelope assessment, Evidence Matrix, Gate-Level Non-Negotiables, Comparison with Peer Frameworks, Economics Assessment) is preserved verbatim.
- The Verdict line `**ASDLC Readiness: L{N} operating, G{M} routinely passing**` MUST appear in the combined file as a standalone bold line, character-for-character identical to the source.

Insert at the top of the lifted Part 8 (immediately after the Part 8 H2):

```
> Note: This file includes Part 8 (from agent 05a) verbatim and adds Part 9 below.
```

### 2.2 Part 9 — Industry & Client Assessment (new content)

Part 9 contains four required sections in this order:

#### 2.2.1 `### Regulatory Exposure Map`

Render as a markdown table with columns:

```
| Regulation / framework | Article / section / clause | Obligation | ASDLC layer / gate / category most affected | [[FRAMEWORK]] coverage |
```

Rows are sourced **exclusively** from `[[DOMAIN_FILE]]`'s regulatory mapping sections. Each row:
- Cites a specific article / section / clause number.
- States the operational obligation in 1–2 sentences.
- Maps to the most-affected ASDLC layer / gate / cross-cutting category (e.g., `L3 + G2`, `L4 + Tier 4 envelope`, `Cross-cutting Governance`).
- States `[[FRAMEWORK]]` coverage as `Met` / `Partial` / `Absent` / `*[Scope gap]*`.

**Framing — "supports compliance with", not "satisfies".** Per the previous-sprint domain softening, the regulatory exposure map output MUST use the framing **"supports compliance with regulation X"** or **"produces evidence aligned with regulation X"** or **"operationalises clause X"**. The output MUST NOT assert that `[[FRAMEWORK]]` "satisfies" regulation X, "is the X requirement", "meets" regulation X, or "is compliant with" regulation X. Compliance is a determination made by the regulated entity and its auditors / regulators against the entity's full control environment, not by a framework in isolation. Where `[[FRAMEWORK]]` is INSUFFICIENT to support compliance with a clause without additional artefacts, the row MUST name the additional artefacts explicitly (e.g., "supports compliance with §404 ICFR design effectiveness when paired with a documented control-owner attestation outside `[[FRAMEWORK]]` scope and a SOC 1 Type II report from the agent-platform provider").

#### 2.2.1.1 EU AI Act Risk-Category Verdict (mandatory when `[[INDUSTRY]]` involves EU regulatory exposure)

When `[[INDUSTRY]]` involves EU regulatory exposure (e.g., insurance with EU presence, financial-services with EU presence, any deployment within an EU member state, any deployment whose output reaches a natural person in the EU), the prompt MUST cross-reference `eu-ai-act-mapping.md` and produce an explicit Risk-Category verdict for `[[FRAMEWORK]]` per the AutonomyTier × BlastRadiusTier mapping in that file. The verdict:

1. States the EU AI Act risk category (`Prohibited` / `High-risk` / `Limited-risk` / `Minimal-risk`) that the framework's typical deployment surface in `[[INDUSTRY]]` falls into, citing the AutonomyTier × BlastRadiusTier cell from `eu-ai-act-mapping.md`.
2. Identifies which Article obligations the framework claims to support — drawn from the canonical set: **Art. 9** (risk management), **Art. 10** (data governance), **Art. 13** (transparency to deployers), **Art. 14** (human oversight), **Art. 15** (accuracy, robustness, cybersecurity), **Art. 17** (quality management), **Art. 26** (deployer obligations), **Art. 50** (transparency to natural persons).
3. For each Article, states whether `[[FRAMEWORK]]` `supports compliance with` / `partially supports compliance with` / `does not support compliance with` the obligation, citing the framework artefact (or stating "no evidence found").
4. Names the residual gaps the deployer MUST close with artefacts outside `[[FRAMEWORK]]` (e.g., conformity assessment under Art. 43, post-market monitoring plan under Art. 72, fundamental-rights impact assessment under Art. 27).

When `[[INDUSTRY]]` has no EU exposure, omit this subsection and state explicitly: "No EU regulatory exposure identified for `[[INDUSTRY]]` at `[[ORGANIZATION]]`; EU AI Act risk-category verdict is not produced."

#### 2.2.2 `### Use-Case Fitness Analysis`

Render as a markdown table with columns:

```
| Use case (from [[DOMAIN_FILE]]) | Autonomy tier ceiling (from `governance/agents.md`) | ASDLC layer of primary risk | [[FRAMEWORK]] fitness |
```

Rows: 4–8 use cases named **verbatim** from `[[DOMAIN_FILE]]`. Each row:
- Names the use case as it appears in `[[DOMAIN_FILE]]`.
- States the autonomy tier ceiling (Tier 1 / 2 / 3 / 4 per `governance/agents.md`'s autonomy tier definitions). The ceiling is determined by blast radius and regulatory constraint per `governance/agents.md`.
- Identifies the ASDLC layer where the primary risk concentrates (e.g., `L3 — Release & Deployment` for a use case where the consequential failure is at production cutover).
- States `[[FRAMEWORK]]` fitness as `Strong fit` / `Conditional fit` / `Mismatch` with a one-clause justification.

Do not invent use cases. If `[[DOMAIN_FILE]]` does not name use cases, state explicitly: "No use cases enumerated in `[[DOMAIN_FILE]]`; the section presents the regulatory exposure as the deployment surface instead."

#### 2.2.3 `### The Red Line`

Identify workflows or system classes that are regulator-impermissible for `[[FRAMEWORK]]` to support at `[[ORGANIZATION]]`. The Red Line is the set of deployments that the framework MUST NOT enable in `[[INDUSTRY]]`'s regulatory environment.

Render as 2–6 bullets, each:
- Names the prohibited workflow / system class verbatim from `[[DOMAIN_FILE]]` (or, when `[[DOMAIN_FILE]]` does not name a hard stop, derives from a specific article that prohibits autonomous operation of a class of decisions).
- Cites the article / section / clause that establishes the prohibition.
- States the ASDLC autonomy tier above which the workflow becomes regulator-impermissible (e.g., "Tier 3 and above" or "any autonomy beyond advisory").
- States explicitly whether `[[FRAMEWORK]]` defaults bring it close to or across the Red Line in `[[ORGANIZATION]]`'s context.

If `[[DOMAIN_FILE]]` does not name hard regulatory stops, the section MUST still be present and state: "No hard regulatory stops identified in `[[DOMAIN_FILE]]`. The deployment ceiling at `[[ORGANIZATION]]` is therefore set by the operational risk appetite, not by external regulatory prohibition."

#### 2.2.4 `### The Deployment Path`

A staged rollout sequence, each stage tied to a gate maturation. Typically 3–6 stages depending on `[[DOMAIN_FILE]]`'s regulatory complexity. Each stage MUST specify:

- **(a) Named workflows in scope** — which `[[FRAMEWORK]]`-enabled workflows are deployed at this stage. Workflows are named verbatim from `[[DOMAIN_FILE]]`.
- **(b) Gating evidence required before next stage** — what artefacts, audit results, evaluation outcomes, or SLO records must be in hand before the next stage begins. Cite the relevant ASDLC gate condition (G1 / G2 / G3) by number.
- **(c) Effort label** — `S` / `M` / `L` / `XL` per `prompt.md`'s effort sizing.

Stage 1 is bounded by `[[FRAMEWORK]]`'s current readiness verdict from Part 8 (cannot exceed `L{N} operating, G{M} routinely passing`). Subsequent stages graduate by adding a gate or maturing a layer. The final stage names the steady-state operational posture appropriate for `[[ORGANIZATION]]` in `[[INDUSTRY]]`.

The deployment path is bounded above by the Red Line — no stage can include a workflow that crosses the Red Line.

### 2.3 Banned soft language

Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`. Use declarative form.

### 2.4 Out-of-scope-vocabulary paraphrase

When `[[DOMAIN_FILE]]`, a regulatory crosswalk, a governance file, or an operational template references APLC, IGM, or AEnt-M mechanisms (e.g., `domains/insurance.md` references "the APLC's behavioural specification"), paraphrase to ASDLC-equivalent terms (e.g., "APLC behavioural specification" → "the framework's specification artefact"; "AEnt-M consequence class" → "consequence-class assessment outside ASDLC scope"; "IGM epistemic tier" → "claim-confidence tier outside ASDLC scope"). Do NOT propagate vocabulary, paths, or filenames into the output even when they appear in the cited source file.

### 2.5 Idempotence

Glob output. If exists AND ≥ 20 lines AND contains both Part 8 and Part 9 H2 headings AND Part 9 has all four required sections AND the readiness verdict line is preserved verbatim, exit. Otherwise rewrite.

---

## 3. Output structure

### 3.1 File path

```
[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_05_readiness_industry.md
```

### 3.2 H1 heading and metadata

```
# [[FRAMEWORK]] Review 05 — Layer Readiness & Industry Assessment (Combined Parts 8 + 9)

**Framework:** [[FRAMEWORK]] ([[FRAMEWORK_VERSION]])
**Client context:** [[ORGANIZATION]]
**Regulatory overlay:** [[INDUSTRY]]
**Reviewer date:** <YYYY-MM-DD>
**ASDLC:** `arnaudgelas/asdlc@[[ASDLC_HASH]]`
**Source lifted:** Part 8 — `_review_05a_readiness.md`

---

## Part 8 — Layer Readiness & Tier 4 Verdict

> Note: This file includes Part 8 (from agent 05a) verbatim and adds Part 9 below.

<lifted Part 8 content from 05a, with H1 dropped; Verdict line preserved verbatim as standalone bold line>

---

## Part 9 — Industry & Client Assessment

### Regulatory Exposure Map

<markdown table with columns Regulation/framework, Article/section/clause, Obligation, ASDLC layer/gate/category most affected, [[FRAMEWORK]] coverage; rows sourced exclusively from [[DOMAIN_FILE]]>

### Use-Case Fitness Analysis

<markdown table with columns Use case (from [[DOMAIN_FILE]]), Autonomy tier ceiling, ASDLC layer of primary risk, [[FRAMEWORK]] fitness; 4–8 rows verbatim from [[DOMAIN_FILE]] OR explicit "no use cases enumerated" statement>

### The Red Line

<2–6 bullets identifying regulator-impermissible workflows OR explicit "no hard regulatory stops identified" statement>

### The Deployment Path

<3–6 staged rollout entries, each specifying (a) named workflows in scope, (b) gating evidence required, (c) effort label. Stage 1 bounded by Part 8 verdict; final stage at steady-state posture for [[ORGANIZATION]]. No stage crosses the Red Line.>

---
```

---

## 4. Hard rules

1. **Preflight is non-optional.** If `_review_05a_readiness.md` is missing, empty, malformed, or does not contain the canonical readiness verdict line, STOP and report.
2. **Lift Part 8 verbatim.** Heading harmonisation only (drop 05a's H1, prepend the explanatory note). Verdict line MUST be preserved as a standalone bold line.
3. **Part 9 regulations are sourced exclusively from `[[DOMAIN_FILE]]`.** Do not import financial-services regulation names when `[[DOMAIN_FILE]]` is not a financial-services domain file. No invented regulations; no extrapolation.
4. **Use cases in Use-Case Fitness Analysis are named verbatim from `[[DOMAIN_FILE]]`.** No invented use cases.
5. **Autonomy tier ceiling per use case is sourced from `governance/agents.md`'s autonomy tier definitions** (Tier 1 / 2 / 3 / 4) bounded by blast radius and regulatory constraint. Cite `governance/agents.md` when stating the ceiling.
6. **Deployment Path stages cite ASDLC gate conditions** (G1 / G2 / G3) by number.
7. **Deployment Path is bounded above by the Red Line** — no stage may include a workflow that crosses the Red Line.
8. **Stage 1 cannot exceed Part 8's readiness verdict.**
9. **Date format YYYY-MM-DD** wherever a date appears.
10. **Out-of-scope corpus / tracked-files-only — including forward-propagation from `[[DOMAIN_FILE]]` and from cross-stack files.** Every source file cited MUST be tracked by git on the current branch. Do not read or reference `aplc/`, `intelligence-governance-manifesto/`, `agentic-enterprise-manifesto/`, `agentic-enterprise.md`, `agentic-enterprise.html`, `agentic-governance-stack.md`, `agentic-governance-stack.html`, `manifesto-evolution-plan.md`, `manifesto-evolution-plan.html`, `phase-assessment-checklist.md`, `phase-assessment-checklist.html`, `aplc-plan*`, or `igm-aent-coherence-review*` anywhere in the output. The output MUST contain zero matches for the tokens `APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, or `phase-assessment-checklist`. **When `[[DOMAIN_FILE]]`, a regulatory crosswalk, a governance file, or an operational template references APLC, IGM, or AEnt-M mechanisms** (e.g., `domains/insurance.md` references "the APLC's behavioural specification"), **paraphrase to ASDLC-equivalent terms** per §2.4. Do NOT propagate vocabulary, paths, or filenames into the output even when they appear in the cited source file.
11. **Banned soft language.** Output MUST NOT contain `consider`, `may`, `could potentially`, `perhaps`, `use judgement`. Make declarative claims.
12. **No `[[FRAMEWORK]]` source re-derivation.** Synthesis only — coverage statements quote from `[[FRAMEWORK]]` source artefacts that were already cited in 05a; do not introduce new framework-source quotes in Part 9 except where they directly inform the regulatory mapping.
13. **"Supports compliance with" framing — never "satisfies".** Output MUST frame `[[FRAMEWORK]]`'s relationship to a regulation as "supports compliance with regulation X" or "produces evidence aligned with regulation X" or "operationalises clause X". Output MUST NOT assert that `[[FRAMEWORK]]` "satisfies regulation X", "is the X requirement", "meets regulation X", or "is compliant with regulation X". Where `[[FRAMEWORK]]` is INSUFFICIENT for a regulator without additional artefacts, the row MUST name those additional artefacts explicitly.
14. **EU AI Act mapping is mandatory for EU exposure.** When `[[INDUSTRY]]` involves EU regulatory exposure, §2.2.1.1 (EU AI Act Risk-Category Verdict) is mandatory and MUST cross-reference `eu-ai-act-mapping.md`, identify Article obligations from {Art. 9, 10, 13, 14, 15, 17, 26, 50}, and name residual gaps the deployer must close outside `[[FRAMEWORK]]` scope.
15. **Domain dispatch.** When `[[DOMAIN_FILE]]` is `domains/sox.md`, `domains/hipaa.md`, or `domains/ccpa.md`, the regulatory exposure map MUST be SOX-grounded, HIPAA-grounded, or CCPA-grounded respectively, per §1.4 dispatch logic. Do not import EU AI Act, SR 11-7, DORA, or Solvency II content into a SOX / HIPAA / CCPA exposure map unless `[[INDUSTRY]]` independently invokes those regimes.

---

## 5. Self-check before saving

- [ ] `_review_05a_readiness.md` exists, is non-empty, has at least 20 lines, and contains a `**ASDLC Readiness: L{N} operating, G{M} routinely passing**` line that was successfully extracted. **The combined output's Part 8 verdict line matches the line read from 05a's output verbatim.**
- [ ] Output file is written to `[[FRAMEWORK_LOWER]]/[[FRAMEWORK_LOWER]]_review_05_readiness_industry.md` (the canonical combined file name).
- [ ] Part 8 content is copied verbatim from 05a's output (with H1 harmonised). The Verdict line is preserved as a standalone bold line with no annotations.
- [ ] Part 8 includes the explanatory note: `> Note: This file includes Part 8 (from agent 05a) verbatim and adds Part 9 below.`
- [ ] Regulatory Exposure Map enumerates regulations **exclusively** from `[[DOMAIN_FILE]]`'s regulatory mapping sections; no financial-services regulation names appear unless `[[DOMAIN_FILE]]` is `domains/financial-services.md` or another FS-domain file.
- [ ] Use-Case Fitness Analysis use cases are named verbatim from `[[DOMAIN_FILE]]`; no invented use cases. Each row carries an autonomy-tier ceiling sourced from `governance/agents.md`.
- [ ] Red Line section is present and cites a specific clause / section / article from `[[DOMAIN_FILE]]` for at least one prohibited workflow (or states explicitly that no hard stops exist, with regulatory justification).
- [ ] Deployment Path has a stage count appropriate to the regulatory mapping (typically 3–6 stages; more if `[[DOMAIN_FILE]]` requires it). Each stage specifies (a) named workflows in scope, (b) gating evidence required before next stage with the ASDLC gate condition cited by number, and (c) effort label (S / M / L / XL).
- [ ] No `[[...]]` placeholders remain in the output file.
- [ ] Zero matches for any out-of-scope-corpus token (`APLC`, `IGM`, `AEnt-M`, `AEnt_M`, `intelligence-governance-manifesto`, `agentic-enterprise-manifesto`, `agentic-enterprise`, `agentic-governance-stack`, `manifesto-evolution-plan`, `phase-assessment-checklist`, `aplc/`, `aplc-plan`, `igm-aent-coherence-review`) anywhere in the output file, including paraphrased forms when `[[DOMAIN_FILE]]` or any cross-stack file in `governance/`, `domains/`, or `operations/` contains the vocabulary. Every cited source file is tracked by git on the current branch.
- [ ] No banned soft language (`consider`, `may`, `could potentially`, `perhaps`, `use judgement`) appears anywhere in the output file.
- [ ] Regulatory framing uses **"supports compliance with"** / **"produces evidence aligned with"** / **"operationalises"** — never "satisfies" / "meets" / "is compliant with" / "is the X requirement". Where `[[FRAMEWORK]]` is INSUFFICIENT without additional artefacts, those artefacts are named explicitly.
- [ ] When `[[DOMAIN_FILE]]` is `domains/sox.md`, `domains/hipaa.md`, or `domains/ccpa.md`, the Regulatory Exposure Map is SOX-grounded / HIPAA-grounded / CCPA-grounded per §1.4 dispatch logic; no foreign regulatory regimes are imported.
- [ ] When `[[INDUSTRY]]` involves EU regulatory exposure, §2.2.1.1 (EU AI Act Risk-Category Verdict) is present, cross-references `eu-ai-act-mapping.md`, identifies Article obligations from {Art. 9, 10, 13, 14, 15, 17, 26, 50}, and names residual gaps the deployer must close outside `[[FRAMEWORK]]` scope. When `[[INDUSTRY]]` has no EU exposure, the subsection is explicitly stated as not produced.
