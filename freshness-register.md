# External-Authority Freshness Register

## Why this register exists

ASDLC is built on a substrate of external authorities — regulations,
standards, frameworks, and security guidance. Those authorities themselves
drift. ISO standards revise on a five- to ten-year cycle; OWASP reranks its
top-tens roughly annually; EU regulations gain delegated acts; NIST
publishes new generative-AI profiles; FDA guidance is reissued. If ASDLC's
citations are not periodically re-verified against authoritative sources,
the framework silently rots and produces stale conformance claims.

This register tracks every external authority ASDLC cites, with the date of
last verification and the date by which re-verification is due. The
register is itself a governance artefact and is part of the **Governance of
Governance** recursion described in `asdlc.md` and
`governance/agents.md` — the framework's own metadata is governed.

## Schema

The authoritative machine-readable register is `freshness-register.yaml`.
Every entry has:

| Field | Meaning |
| --- | --- |
| `id` | Stable, snake_case identifier; never renamed once issued. |
| `name` | Full human-readable title. |
| `document` | Citation token used in ASDLC prose (e.g. "NIST AI 100-1"). |
| `version` | Version designator as published. |
| `publication_date` | ISO 8601 date of the cited edition's publication. `unknown` if unverified, with a `publication_date_note`. |
| `authoritative_url` | Official URL where the document is published. |
| `last_verified` | Date the citation was last verified against the authoritative source. |
| `cadence` | One of `3_months`, `6_months`, `12_months`. |
| `next_review_due` | `last_verified` + cadence. |
| `owner` | Role (not a person's name) accountable for re-verification. |
| `referenced_in` | List of ASDLC files that cite this authority. |
| `applicability` | One-sentence note on why ASDLC tracks this authority. |

The register's `register_owner` (currently the **ASDLC Steward**) is the
single role accountable for the quarterly freshness review and the
freshness report.

## Cadence policy

Three cadences are recognised:

- **3 months** — security-fast-moving authorities. OWASP top-tens, OWASP
  agentic-AI guidance, and NIST adversarial-ML taxonomies fall here. New
  attack classes and mitigations appear continuously, and stale citations
  in `security-governance.md` or `devsecops-controls.md` are operationally
  dangerous.
- **6 months** — default cadence. Most NIST AI publications, EU AI Act
  (which is still gaining delegated acts and harmonised standards),
  DORA, scaling frameworks (SAFe), and supply-chain provenance specs.
- **12 months** — slow-moving foundational authorities. Long-stable ISO
  standards, decade-stable EU directives (GDPR, MiFID II), long-running US
  statutes (HIPAA, SOX, SR 11-7), and aviation/automotive certification
  standards whose revision cycles are measured in years.

The cadence is conservative by design. An authority MAY be re-verified
sooner — in particular, any authority that issues a new edition triggers
an out-of-cycle review.

## Re-verification procedure

The register owner (ASDLC Steward) runs a quarterly freshness review:

1. List entries with `next_review_due <= today + 30 days`.
2. For each entry, fetch the authoritative URL and verify:
   - The cited version is still the latest (or the latest applicable to
     ASDLC's scope).
   - The document has not been superseded.
   - Cross-references in `referenced_in` files still match the authority's
     current language.
3. If the entry is current: bump `last_verified` to today and recompute
   `next_review_due`.
4. If the entry has been superseded: open a tracked change to update the
   citation across all `referenced_in` files, then bump `last_verified`.
5. If the cited authority cannot be verified within the cadence window:
   escalate to the ASDLC Steward as a stale-authority finding. A stale
   authority is never silently retained.

The output of each quarterly review is a freshness report, archived
alongside the register.

## Integration with ASDLC governance

The register is itself governed:

- **Specification Readiness (SR Gate).** Specifications for systems
  claiming conformance to a regulated domain MUST cite authorities present
  in this register. If a specification cites an authority not in the
  register, the SR-9 (Context Thread Assembled and Reviewed) check
  triggers a register update.
- **Release Gate (RG).** Evidence bundles (RG-1) reference authorities by
  `id`. A release whose evidence bundle cites an authority whose
  `next_review_due` has lapsed produces a stale-authority warning that the
  Accountable Human (RG-4) must acknowledge or waive (RG-8).
- **Operational DoD.** Operational stewardship monitors the register's
  staleness as part of the persistent obligation; an authority that
  remains stale beyond one quarter triggers a maintenance-governance
  ticket.
- **Governance of Governance.** The register's own currency is reviewed
  whenever ASDLC itself revises. See `asdlc.md` recursion of governance
  scope.

## Summary by cadence

The full enumeration is in `freshness-register.yaml`. Grouped by cadence:

### 3-month cadence (security-fast-moving)

| Authority | Document | Current version |
| --- | --- | --- |
| NIST Adversarial-ML Taxonomy | NIST AI 100-2e2025 | 2025 edition |
| OWASP LLM Top 10 | OWASP LLM Top 10 | 2025 |
| OWASP Agentic AI — Threats and Mitigations | OWASP Agentic AI | 2025 |

### 6-month cadence (default)

| Authority | Document | Current version |
| --- | --- | --- |
| NIST AI Risk Management Framework | NIST AI 100-1 | 1.0 |
| NIST AI RMF — Generative AI Profile | NIST AI 600-1 | 1.0 |
| Secure SDF for Generative AI | NIST SP 800-218A | Initial Public Release |
| EU AI Act | Regulation (EU) 2024/1689 | as adopted |
| DORA (EU) | Regulation (EU) 2022/2554 | as adopted |
| Solvency II | Directive 2009/138/EC | consolidated |
| Insurance Distribution Directive | Directive (EU) 2016/97 | as adopted |
| MiFID II | Directive 2014/65/EU | consolidated |
| SAFe | SAFe | 6.0 |
| SLSA | SLSA | 1.0 |
| in-toto | in-toto specification | 1.0 |
| CMMC | CMMC 2.0 | 2.0 |
| FedRAMP | FedRAMP | Rev 5 baselines |
| CMU SEI 12 Foundational Practices | SEI AI Engineering | 2026 edition |

### 12-month cadence (slow-moving foundational)

| Authority | Document | Current version |
| --- | --- | --- |
| NIST SP 800-53 | NIST SP 800-53 | Revision 5 |
| NIST SP 800-37 | NIST SP 800-37 | Revision 2 |
| ISO/IEC 42001:2023 | AI Management System | First edition |
| ISO/IEC 5338:2023 | AI System Lifecycle | First edition |
| ISO/IEC 23894:2023 | AI Risk Management | First edition |
| ISO 26262 (automotive) | ISO 26262-1:2018 | Second edition |
| IEC 62304 (medical) | IEC 62304 | Edition 1.1 |
| DO-178C / ED-12C (aviation) | DO-178C | C |
| ARP 4754A (aviation) | SAE ARP 4754A | A |
| GAMP 5 (pharma) | GAMP 5 | Second edition |
| 21 CFR Part 11 | 21 CFR Part 11 | as codified |
| GDPR | Regulation (EU) 2016/679 | as adopted |
| SR 11-7 (Fed model risk) | SR 11-7 | as issued |
| Sarbanes-Oxley Act | 15 U.S.C. § 7201 et seq. | as amended |
| HIPAA | 45 CFR Parts 160, 162, 164 | as codified |
| CCPA / CPRA | Cal. Civ. Code § 1798.100 et seq. | CCPA + CPRA |
| ITIL 4 | ITIL 4 | 4 |
| Accelerate State of DevOps | DORA research | 2024 |
| DoDI 8510.01 | DoDI 8510.01 | Change 3 |
| MIL-STD-882E | MIL-STD-882E | E |
| ICAO Annexes | ICAO Annexes | current revisions |

## Internal governance artefacts

In addition to external authorities, the register tracks ASDLC's own
governance artefacts whose currency must be re-verified on cadence.

- **`ASDLC_REVIEW_SYSTEM`** — the review system at `review/` (orchestrator
  `review/prompt.md`, sub-prompts under `review/prompts/`, fixtures under
  `review/fixtures/`, harness under `review/test_harness/`). Quarterly
  cadence (3 months) because ASDLC evolves and the review system must
  track it. Owner: ASDLC Steward. Misalignment between the review
  system and the ASDLC source is itself a governance finding. The lint
  suite at `scripts/lint.py` is the mechanical check; the freshness
  entry tracks the editorial/structural review.

## Review-run tracking

`freshness-register.yaml` carries a top-level `review_runs` list
alongside `authorities`. The list tracks invocations of the review
system against external frameworks so each merged review's freshness is
itself governed.

| Field | Meaning |
| --- | --- |
| `run_id` | Stable identifier for the run; never renamed. |
| `framework` | The framework reviewed (the `[[FRAMEWORK]]` value at run time). |
| `framework_version` | The `[[FRAMEWORK_VERSION]]` value declared at run time. |
| `asdlc_hash` | The full 40-character ASDLC commit hash used to score (`[[ASDLC_HASH]]`). |
| `last_run` | ISO 8601 date the review was produced. |
| `next_review_due` | ISO 8601 date by which the review should be re-run. Recommended cadence: 6 months for framework versions believed stable; 3 months for fast-moving frameworks. |
| `owner` | Role responsible for re-running. |
| `merged_review_path` | Path to the canonical merged review file. |

The list is initially empty and is populated as reviews are run.

## Companion files

- `freshness-register.yaml` — authoritative machine-readable register
  (carries both `authorities` and `review_runs`).
- `governance/gate-registry.yaml` — gate condition registry (companion
  governance source-of-truth).
- `operations/governance.md` — Governance of Governance scope.
- `review/prompt.md` — orchestrator for the ASDLC review system entry
  above.
