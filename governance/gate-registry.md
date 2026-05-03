# Gate Condition Registry

_The single normative source of truth for every ASDLC gate's condition list.
The machine-readable canonical record is **`gate-registry.yaml`** (sibling
file). This Markdown wrapper is a human-readable view that is **derived from
that YAML**; when the two diverge, the YAML governs._

See the [ASDLC Overview](../asdlc.md) for the four-layer model and the
gate-by-gate narrative. See [Specification Readiness](../specification-readiness.md),
[Release & Deployment Governance](../release-governance.md),
[Operational Definition of Done](../operations/dod.md), and
[Retirement Gate](../retirement-gate.md) for the authoritative prose
definition of each condition.

---

## Why this registry exists

Gate conditions are referenced in many places across the ASDLC corpus: the
overview, the implementation guide, the README, every domain file, every
review prompt, and the conformance profiles. Each of those locations has
historically restated the condition counts and titles inline. Restated
enumerations drift. Drift in a governance enumeration is a governance failure:
a reader who consults one document and acts on a count that differs from the
authoritative source has acted on a stale governance record.

This registry resolves that risk by becoming the single normative enumeration
in `gate-registry.yaml`. Any other ASDLC document that needs to refer to a
gate's condition count, a specific condition title, or a condition identifier
must either link to this registry, derive its content from the YAML, or
restate the YAML's content verbatim. Where verbatim restatement diverges from
the YAML, the YAML governs and the divergent document must be corrected.

The registry is normative. It is not a summary, not a quick reference, not an
informal aid. It is the canonical record. The YAML is the canonical *source*;
this Markdown is the canonical *human-readable view*.

---

## Mechanical authority

`gate-registry.yaml` defines:

- The list of gates (Specification Readiness, Release, Operational Definition
  of Done, Retirement) and their boundary, count, summary, and authoritative
  document.
- For each condition: id, title, blocking/conditional status, tier
  applicability, and any per-condition note.
- The canonical seven-state GateState enum mirror (authoritative source:
  `graph.md` "Canonical Enum Authority").
- Aliases for backward-compatible references in older prose.

The lint tool `scripts/check_gate_counts.py` reads `gate-registry.yaml`
directly. Drift between the YAML and any prose enumeration in the corpus is
reported as a CI failure. The lint is not a suggestion; it is the
enforcement mechanism for the precedence rule below.

The Markdown tables in the sections that follow are derived directly from
the YAML. If you edit them by hand, the lint will detect the divergence at
the next CI run; update the YAML instead and let the Markdown tables
re-derive.

---

## Scope

The ASDLC defines four gates across the four layers:

1. **Specification Readiness Gate** — boundary L1 → L2.
2. **Release Gate** — boundary L2 → L3.
3. **Operational Readiness Gate** — boundary L3 → L4.
4. **Retirement Gate** — boundary L4 → end-of-life.

The Operational Readiness Gate and the Operational Definition of Done share
content but are not identical. The Operational Readiness Gate is the single
boundary assessment performed once, at the L3 → L4 transition, against the
deployment under release. The Operational Definition of Done is the persistent
condition set that the system must continuously satisfy throughout its
operational lifetime; it is checked at the boundary by the Operational
Readiness Gate and re-checked periodically by the steward thereafter. A system
passes the Operational Readiness Gate by satisfying the Operational DoD at the
moment of the gate; the Operational DoD then becomes a continuous obligation,
not a one-time pass. This registry enumerates the Operational DoD condition
set. The Operational Readiness Gate is the act of evaluating that set at the
L3 → L4 boundary.

---

## Specification Readiness Gate (L1 → L2)

The Specification Readiness Gate has **9 conditions**. All are blocking. None
are conditional on system tier. A specification that does not satisfy all
nine conditions does not enter Layer 2 (the engineering execution layer
defined by the Agentic Engineering Manifesto).

| ID | Title | Blocking | Tier Applicability |
|----|-------|----------|--------------------|
| SR-1 | Business Need Validated | Yes | All tiers |
| SR-2 | Value Measurable | Yes | All tiers |
| SR-3 | Acceptance Criteria Expressible | Yes | All tiers |
| SR-4 | Constraints Identified | Yes | All tiers |
| SR-5 | Accountable Human Named | Yes | All tiers |
| SR-6 | Blast Radius Assessed | Yes | All tiers |
| SR-7 | Out-of-Scope Explicitly Stated | Yes | All tiers |
| SR-8 | Loop Cost Justified | Yes | All tiers (depth tier-calibrated) |
| SR-9 | Context Thread Assembled and Reviewed | Yes | All tiers |

Authoritative prose: [specification-readiness.md](../specification-readiness.md).

A specification with fewer than nine satisfied conditions is not loop-ready
regardless of how many conditions are satisfied. Partial passes are not
"mostly ready" — they are not ready.

---

## Release Gate (L2 → L3)

The Release Gate has **8 conditions**. Conditions RG-1, RG-3, RG-4, RG-5,
RG-7, and RG-8 are blocking for all systems. RG-2 is blocking at adoption
phase 4+ and for all high-stakes regulated systems regardless of phase. RG-6
is conditional, blocking only for external-facing changes and for
blast-radius tier 2/3.

| ID | Title | Blocking | Tier Applicability |
|----|-------|----------|--------------------|
| RG-1 | Evidence Bundle Complete | Yes | All tiers |
| RG-2 | Independent Validation Passed | Yes (phase 4+ or high-stakes regulated) | Phase 4+ regardless of tier; high-stakes regulated systems regardless of phase |
| RG-3 | Rollback Procedure Tested | Yes | All tiers |
| RG-4 | Accountable Human Sign-Off | Yes | All tiers |
| RG-5 | Compliance Documentation Complete | Yes | All tiers (scope tier-dependent) |
| RG-6 | Dynamic Security Testing Passed | Conditional | Blocking for external-facing changes and blast-radius tier 2/3; recommended at blast-radius tier 1 unless inputs can affect other users, systems, or stored data |
| RG-7 | Control State Record Complete and Current | Yes | All tiers |
| RG-8 | Waiver Governance | Yes | All tiers |

Authoritative prose: [release-governance.md](../release-governance.md).

A Release Gate pass recorded with one or more applicable conditions failed,
stale, or unresolved is not a valid pass.

---

## Operational Definition of Done (persistent; checked at the L3 → L4 Operational Readiness Gate)

The Operational DoD has **8 conditions**: 7 unconditional plus 1 conditional
(DoD-8 DR/Failover Tested, blocking only at blast-radius tier 3 unless a
regulatory or contractual mandate raises it).

| ID | Title | Blocking | Tier Applicability |
|----|-------|----------|--------------------|
| DoD-1 | Runbook Complete | Yes | All tiers |
| DoD-2 | Operational Observability Configured | Yes | All tiers |
| DoD-3 | On-Call Assignment Made | Yes | All tiers |
| DoD-4 | System Steward Assigned | Yes | All tiers |
| DoD-5 | Security Scan Clean | Yes | All tiers |
| DoD-6 | License Compliance Confirmed | Yes | All tiers |
| DoD-7 | Trace Retention Policy Set | Yes | All tiers |
| DoD-8 | DR/Failover Tested | Conditional | Blocking at blast-radius tier 3; recommended at blast-radius tier 1 and 2 unless required by regulatory or contractual mandate |

Authoritative prose: [operations/dod.md](../operations/dod.md).

The Operational DoD is a persistent obligation. A system that passed the
gate but no longer satisfies the DoD set is not in good operational standing,
even if no code changed and no incident has occurred.

---

## Retirement Gate (L4 → end-of-life)

The Retirement Gate has **8 conditions**. RT-5 (IGM claim retraction) is
conditional on IGM use. RT-6 is conditional on the system having first-party
consumers.

| ID | Title | Blocking | Tier Applicability |
|----|-------|----------|--------------------|
| RT-1 | Stewardship Handoff or Termination | Yes | All tiers |
| RT-2 | Runbook Archived and Immutable | Yes | All tiers |
| RT-3 | Trace and Reasoning-Record Archival | Yes | All tiers |
| RT-4 | Model and Prompt Deprecation Propagated | Yes | All tiers |
| RT-5 | IGM Claim Retraction | Conditional | IGM-bearing systems only |
| RT-6 | Dependency Consumers Notified | Yes | All tiers with first-party consumers |
| RT-7 | FinOps Zero-Out | Yes | All tiers |
| RT-8 | Final Accountability Sign-Off | Yes | All tiers |

Authoritative prose: [retirement-gate.md](../retirement-gate.md).

---

## The precedence rule

The following rule is normative.

> When `gate-registry.yaml`'s count, identifier, or title for a gate
> condition differs from the corresponding count, identifier, or title in
> any other ASDLC document, the YAML governs. The divergent document must
> be corrected. Until the correction is made, the YAML's enumeration is
> the operative one.

This rule applies regardless of the publication date of the divergent
document. A document published earlier than a registry update does not
override the registry; it is a candidate for correction. The registry's
versioning policy below makes update propagation auditable.

The rule does not apply to substantive prose definitions: the authoritative
document associated with each gate governs the meaning of each condition.
The YAML governs counts, identifiers, and titles. If the prose in the
authoritative document diverges from the title in the YAML, the YAML's
title is the canonical short form and the authoritative document is the
canonical explanation.

---

## Versioning policy

Changes to the registry follow the same semantic versioning conventions that
govern the ASDLC framework as a whole; see the "Framework Versioning" section
of [asdlc.md](../asdlc.md).

- Adding a condition to a gate is a major version change for the ASDLC
  framework.
- Removing a condition from a gate is a major version change. A condition
  that existed in a prior version cannot be silently dropped.
- Renaming a condition (changing its title without changing its substance)
  is a minor version change. The prior title must be retained as an alias
  in the YAML's `aliases` block for at least one minor version cycle.
- Re-classifying a condition between Blocking and Conditional, or modifying
  its tier applicability, is a major version change.
- Adjusting authoritative document references is a patch version change.

Every change to `gate-registry.yaml` must be accompanied by a synchronised
update sweep across the documents that reference the affected condition.
The sweep is governed under the same change-management process as any
other ASDLC governance infrastructure change (see the "Governance of
Governance" section of [asdlc.md](../asdlc.md)).

---

## Relationship to other ASDLC documents

The YAML is consumed by `scripts/check_gate_counts.py` (CI lint),
`conformance-profiles.md` (profile control subsets), the review system
(`review/prompts/*` and the review fixtures), and any future tooling that
needs the canonical condition list.

Documents that *reference* but do not *restate* the registry: the
[ASDLC Overview](../asdlc.md), the [Implementation Guide](../asdlc-guide.md),
the [README](../README.md), the domain files in `domains/`, the
[conformance profiles](../conformance-profiles.md), the [retirement gate
specification](../retirement-gate.md), and the review prompts in
`review/prompts/`. Each of those documents must defer to this registry for
counts, identifiers, and titles.
