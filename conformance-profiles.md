# Conformance Profiles

_The defined profiles under which an organisation may claim ASDLC
conformance. A profile defines the SCOPE of governance application — which
systems are claimed under ASDLC, which roles and documents are mandatory,
which cadences are observed, and which regulated-domain mappings (if any)
are in force. A profile does NOT relax gate conditions. Whatever scope an
organisation claims, the four ASDLC gates either pass at full registry
strength for every governed system, or they do not pass. A bare claim of
"ASDLC-conformant" without a named profile is not a meaningful claim;
conformance is profile-specific, and this document defines the normative
profiles and the attestation mechanism by which a profile claim is made
auditable._

See [governance/gate-registry.md](governance/gate-registry.md) and
[governance/gate-registry.yaml](governance/gate-registry.yaml) for the
canonical condition enumeration and tier-applicability rules referenced
below. See [waiver-governance.md](waiver-governance.md) for the canonical
waiver lifecycle. See [retirement-gate.md](retirement-gate.md) for the
fourth gate. See [annex-adoption-cost.md](annex-adoption-cost.md) for the
cost implications of each profile. See [asdlc.md](asdlc.md) for the
framework whose conformance is being claimed, including the "Termination
of recursion" subsection that names the accountable executive at whom the
governance recursion terminates.

---

## Normative framing: profiles are about scope, not gate relaxation

The following statements are normative and govern every other clause in
this document.

> **A gate pass is binary.** For every system within a profile's scope, the
> Specification Readiness Gate, the Release Gate, the Operational Readiness
> Gate (which evaluates the Operational Definition of Done), and the
> Retirement Gate either pass at the strength defined in
> [governance/gate-registry.yaml](governance/gate-registry.yaml), or they
> do not pass. A condition that the registry marks `blocking: true` for a
> given system's tier and context MUST be satisfied for that gate to pass.
> A condition that is unsatisfied and uncovered by a current waiver under
> [waiver-governance.md](waiver-governance.md) records a GateState other
> than `pass` (one of `fail`, `missing`, `stale`, `contradicted`,
> `waived`, or `requires-human-decision`, per the canonical
> `gate_state_enum` in the registry).

> **Profiles claim scope, not relaxation.** A profile claim states which
> systems are governed by the ASDLC, which roles are filled, which
> documents are in force, and which cadences and regulator-of-record
> relationships apply. A profile claim does NOT confer permission to omit
> a registry-blocking condition. An organisation that wishes to operate a
> system without satisfying a blocking condition MUST either bring the
> system out of scope of the profile, or carry a current waiver against
> that condition under the canonical waiver mechanism.

> **A claim that a gate was "passed at the profile-minimum subset" is not
> a valid gate pass.** It is a process violation. Any phrasing that
> presents a profile as licensing a relaxed gate, a partial gate, or a
> fractional condition set is non-conformant with this document and MUST
> be rejected at attestation review.

> **Conformance requires a profile claim.** A bare "ASDLC-conformant"
> claim without a named profile is not a meaningful claim and confers no
> conformance status. A profile claim MUST be supported by a current
> attestation made under the YAML template at the end of this document.

The remainder of this document defines the three profiles and an optional
fourth profile for Tier-4 envelope operations. Each profile is defined by
its scope, its required corpus, its required roles, its required
cadences, its waiver ceiling, and its attestation metadata. The four
gates run identically across all profiles.

---

## ASDLC-Limited

ASDLC-Limited is a *limited-conformance* profile. The organisation claims
that ASDLC governance applies to a bounded subset of its systems —
typically low-blast-radius internal tools, low-risk automation, or
pre-production prototypes — and is explicit that ASDLC does NOT apply
outside that subset. Within the claimed subset, every gate runs at the
registry's full strength for the system's tier and context.

ASDLC-Limited is the floor of conformance: an organisation operating
below it (no scope claim, no attestation, no governed gates) is not
operating ASDLC at all. ASDLC-Limited is not a "starter" profile that
escalates automatically; it may be operated indefinitely so long as the
in-scope inventory remains within its entry criteria.

| Dimension | Requirement |
|-----------|-------------|
| Scope of application | A named, enumerated subset of the organisation's systems. The attestation MUST list every in-scope system and MUST list every out-of-scope system whose governance is explicitly disclaimed. Ambiguous boundaries (a system "sometimes" in scope) are not permitted. |
| Per-system entry criteria | BlastRadiusTier BR1, or BR2 with a documented rationale for why higher-profile conformance is not required. AutonomyTier 1 or 2. No regulated-domain obligations from `domains/`. No external-facing surface unless the steward has documented compensating controls. |
| Required documents | [asdlc.md](asdlc.md), [specification-readiness.md](specification-readiness.md), [release-governance.md](release-governance.md), [operations/dod.md](operations/dod.md), [retirement-gate.md](retirement-gate.md), [governance/gate-registry.md](governance/gate-registry.md), [governance/gate-registry.yaml](governance/gate-registry.yaml), [waiver-governance.md](waiver-governance.md). |
| Required roles | Accountable Human per system (per [asdlc.md](asdlc.md) "Termination of recursion"); System Steward (may hold a portfolio of up to 20 systems at this profile); Release Manager (may be a part-time role); a named accountable executive for the conformance claim itself. |
| Required cadences | Quarterly governance review of the in-scope inventory and waiver portfolio; annual re-attestation; immediate re-attestation on any material change to scope. |
| Required gates | All four. The Specification Readiness Gate, the Release Gate, the Operational Readiness Gate (which evaluates the Operational Definition of Done), and the Retirement Gate run at full registry strength for every in-scope system. There is no "profile-relaxed gate" at ASDLC-Limited. Tier-applicable rules apply as written: RG-2 is blocking at adoption phase 4+ and for high-stakes regulated systems, RG-6 is blocking for external-facing changes and BR2/BR3, DoD-8 is blocking for BR3, RT-5 is blocking only for IGM-bearing systems, RT-6 applies where first-party consumers exist. |
| Waiver ceiling | Per-system: at most 3 active waivers per system at any time (aligned with the warning threshold in [waiver-governance.md](waiver-governance.md) Section 4). Portfolio: at most 20% of in-scope systems carrying waivers against the same condition type. All waivers MUST conform to the canonical waiver lifecycle in [waiver-governance.md](waiver-governance.md), including grantor distinction, expiry date, compensating control, and remediation plan. |
| Conformance-claim metadata | claimed_profile = `ASDLC-Limited`; conformance_period; accountable_executive; auditor_of_record (self-attestation permitted at this profile); last_attestation_date; next_attestation_due. |

Movement out of ASDLC-Limited is required when the in-scope inventory
ceases to satisfy the entry criteria — for example, the organisation
begins operating BR3 systems, comes under regulated-domain obligations,
or introduces a Tier-4 envelope. Movement is a profile transition, not a
silent re-scoping; see "Profile transitions" below.

---

## ASDLC-Standard

ASDLC-Standard is the profile under which the organisation claims that
the ASDLC applies across its production engineering portfolio. There is
no scope carve-out by tier or blast radius: every production system the
organisation operates is governed by the ASDLC unless the attestation
explicitly and substantively justifies an exclusion. All four gates run
at the registry's full strength for every governed system, and
profile-conditional conditions (RG-2 phase 4+, RG-2 high-stakes
regulated, RG-6 external-facing or BR2/BR3, DoD-8 BR3, RT-5 IGM-bearing,
RT-6 first-party consumers) are evaluated per their registry-declared
applicability rules.

| Dimension | Requirement |
|-----------|-------------|
| Scope of application | The organisation's production engineering portfolio in its entirety. Excluded systems MUST be enumerated with rationale; an unbounded "we exclude unspecified legacy" carve-out is not permitted. |
| Per-system entry criteria | Any BlastRadiusTier (BR1 through BR3); any AutonomyTier from 1 through 3 (Tier-4 envelopes require ASDLC-Tier4 — see below). No regulated-domain mapping is required at this profile, but if one is required by the organisation's industry, the organisation MUST claim ASDLC-Regulated instead. |
| Required documents | All ASDLC-Limited documents, plus: [demand/value.md](demand/value.md), [demand/intelligence.md](demand/intelligence.md), [demand/metrics.md](demand/metrics.md), [deployment-governance.md](deployment-governance.md), [maintenance-governance.md](maintenance-governance.md), [operations/governance.md](operations/governance.md), [security-governance.md](security-governance.md), [devsecops-controls.md](devsecops-controls.md), [finops-governance.md](finops-governance.md), [agent-control-plane.md](agent-control-plane.md), [governance/agents.md](governance/agents.md), [governance/graph.md](governance/graph.md), [governance/queries.md](governance/queries.md). |
| Required roles | All ASDLC-Limited roles, plus: Governance Portfolio Owner; full-time Release Manager; Governance Tooling SRE; Security Function Lead (named, with delegation chain); Compliance Function Lead (named, with delegation chain). The accountable executive is named per [asdlc.md](asdlc.md) "Termination of recursion" and accepts residual risk on the organisation's behalf. |
| Required cadences | Quarterly governance portfolio review; quarterly waiver portfolio review per [waiver-governance.md](waiver-governance.md) Section 4; quarterly DoD re-check per [operations/dod.md](operations/dod.md); annual re-attestation; immediate re-attestation on any material change to scope, profile, or framework version. |
| Required gates | All four, at full registry strength, for every in-scope system. Every blocking condition declared in [governance/gate-registry.yaml](governance/gate-registry.yaml) is evaluated against the system's tier and context; a condition that is unsatisfied and uncovered by a current waiver records a non-`pass` GateState. There is no profile-conditional reduction in scope of the gates themselves. |
| Waiver ceiling | Per-system: at most 2 active waivers per system at any time. Portfolio: at most 10% of in-scope systems carrying waivers against the same condition type. RG-1, RG-3, RG-4, RG-7, RG-8 are non-waivable as a matter of profile policy at ASDLC-Standard, in addition to any non-waivable status declared in the source documents. |
| Conformance-claim metadata | claimed_profile = `ASDLC-Standard`; conformance_period; accountable_executive; auditor_of_record (independent internal audit at minimum); last_attestation_date; next_attestation_due. |

ASDLC-Standard is the default profile for organisations that operate
agentic delivery at production scale outside a regulated industry. An
organisation in a regulated industry should not claim ASDLC-Standard;
the regulated-domain mapping work is part of ASDLC-Regulated and is not
discharged by this profile.

---

## ASDLC-Regulated

ASDLC-Regulated is ASDLC-Standard plus an explicit, attested mapping to
one or more regulated-domain files in `domains/`. The profile adds a
domain-specific compliance evidence schedule, a named
regulator-of-record per system (or per system class), and a documented
residual-risk acceptance executive whose authority and indemnity
position is recorded in the attestation. ASDLC-Regulated inherits every
requirement of ASDLC-Standard; differences below are additive, not
substitutive.

| Dimension | Requirement |
|-----------|-------------|
| Scope of application | ASDLC-Standard scope, restricted or extended to the regulated portfolio. The attestation MUST identify each in-scope system's regulated-domain mapping (one or more of the files in `domains/`). |
| Per-system entry criteria | ASDLC-Standard criteria, plus: each in-scope system MUST cite the applicable regulated-domain file(s) — for example [domains/financial-services.md](domains/financial-services.md), [domains/insurance.md](domains/insurance.md), [domains/pharma.md](domains/pharma.md), [domains/aviation.md](domains/aviation.md), [domains/automotive.md](domains/automotive.md), [domains/defense-government.md](domains/defense-government.md), [domains/hipaa.md](domains/hipaa.md), [domains/sox.md](domains/sox.md), [domains/ccpa.md](domains/ccpa.md). The system's regulator-of-record MUST be named. |
| Required documents | All ASDLC-Standard documents, plus: every applicable file in `domains/`, plus the organisation's compliance evidence schedule cross-referencing each regulated obligation to the gate condition or persistent control that satisfies it. |
| Required roles | All ASDLC-Standard roles, plus: a named **Accountable Executive for Residual Risk** (the person at whom the recursion terminates per [asdlc.md](asdlc.md)) whose name, title, and signed acceptance are recorded in the attestation; a **Regulator-of-Record Liaison** per regulated domain; a **Compliance Liaison** distinct from the Compliance Function Lead, responsible for regulator-facing evidence production. |
| Required cadences | All ASDLC-Standard cadences, plus: a domain-specific compliance evidence schedule (cadence specified in the applicable `domains/` file), regulator-facing reporting per the regulator's mandate, and an annual residual-risk acceptance re-signature by the Accountable Executive for Residual Risk. |
| Required gates | All four, at full registry strength, with no exception. Profile-conditional conditions (RG-2 phase 4+, RG-2 high-stakes regulated, RG-6 external-facing or BR2/BR3, DoD-8 BR3, RT-5 IGM-bearing, RT-6 first-party consumers) are evaluated as written; in particular, RG-2 is blocking for every regulated system regardless of phase, on the strength of the registry's `phase4_or_high_stakes_regulated` rule. |
| Waiver ceiling | Per-system: at most 1 active waiver per system at any time. Portfolio: at most 5% of in-scope systems carrying waivers against the same condition type. Any waiver against a condition that maps to a regulated obligation in `domains/` MUST carry the regulator-of-record's documented awareness or, where the regulator does not pre-approve waivers, MUST be disclosed at the next regulatory reporting cycle. |
| Conformance-claim metadata | claimed_profile = `ASDLC-Regulated`; conformance_period; accountable_executive (residual-risk signatory); auditor_of_record (independent external audit MUST be obtained at least at the cadence specified by the applicable `domains/` file, and in any case no less than every 24 months); regulator_of_record (per system or per system class); domain_files_in_force; last_attestation_date; next_attestation_due. |

ASDLC-Regulated is the profile against which the regulated-domain
mappings in `domains/` are written. An organisation in a regulated
industry that claims ASDLC-Limited or ASDLC-Standard should expect that
the regulator-facing evidence will require additional conformance work
to bridge the profile gap; the mappings are not designed for the lighter
profiles. The previous "ASDLC-Tier4" profile is collapsed into
ASDLC-Regulated where the in-scope class includes BR3 systems and
AutonomyTier-4 envelopes; organisations operating any Tier-4 envelope
MAY further claim ASDLC-Tier4 (below) to make the envelope-specific
obligations explicit.

---

## ASDLC-Tier4 (optional, inherits ASDLC-Regulated)

ASDLC-Tier4 is an optional fourth profile for organisations operating
any AutonomyTier-4 policy envelope — autonomous capabilities running
within machine-enforced policy boundaries, without per-change human
approval inside the envelope. ASDLC-Tier4 inherits ASDLC-Regulated in
full and adds the envelope-specific obligations from
[annex-aentm.md](annex-aentm.md) and
[annex-igm.md](annex-igm.md), plus the relocation evidence schema in
[release-governance.md](release-governance.md). The four gates continue
to run at full registry strength; the addition is in the artefacts they
are run against (the envelope specification, the evaluation portfolio,
the relocation record), not in the conditions themselves.

| Dimension | Requirement |
|-----------|-------------|
| Scope of application | The portfolio that includes one or more Tier-4 envelopes. Lower-tier systems within the same legal entity MAY remain on a separately-attested ASDLC-Standard or ASDLC-Regulated portfolio, with the boundary documented. |
| Per-system entry criteria | ASDLC-Regulated criteria, plus: each Tier-4 envelope MUST have a published envelope specification, an evaluation portfolio in production, and a monitoring configuration in production. A Tier-4 claim unsupported by these artefacts is not defensible. |
| Required documents | All ASDLC-Regulated documents, plus: [annex-aentm.md](annex-aentm.md) (where AEnt-M is in use), [annex-igm.md](annex-igm.md) (where IGM is in use), the per-envelope envelope specification artefacts, the relocation evidence schema in [release-governance.md](release-governance.md). |
| Required roles | All ASDLC-Regulated roles, plus: Envelope Steward (per envelope, with bounds in [annex-adoption-cost.md](annex-adoption-cost.md)); AEnt-M Escalation Authority (named per envelope and per action class, where AEnt-M is in use); IGM Substrate Authority Liaison (where IGM is in use). |
| Required cadences | All ASDLC-Regulated cadences, plus: per-envelope review cadence (default monthly during the envelope's first six months in production, quarterly thereafter); decay-boundary monitoring cadence per [annex-igm.md](annex-igm.md). |
| Required gates | All four, at full registry strength, against the envelope specification and the relocation evidence as well as against individual deployments. RT-5 is blocking for IGM-bearing envelopes. The four intelligence constraints in [annex-igm.md](annex-igm.md) are non-waivable for IGM-bearing envelopes. The relocation evidence schema in [release-governance.md](release-governance.md) is non-waivable for relocated action classes. |
| Waiver ceiling | Tier-4 envelope conditions are non-waivable. The waiver ceilings of ASDLC-Regulated apply to the non-envelope portion of the portfolio. |
| Conformance-claim metadata | claimed_profile = `ASDLC-Tier4`; all ASDLC-Regulated metadata, plus envelope_inventory, aent_m_in_use (boolean), igm_in_use (boolean). |

ASDLC-Tier4 is the most demanding profile. An organisation should claim
it only after the relocation evidence schema, the envelope
specifications, and the monitoring infrastructure are demonstrably in
production. A claim unsupported by these artefacts is not defensible
against a substantive enquiry.

---

## Profile-conformance attestation template

An organisation claiming a profile MUST publish or retain an attestation
under the YAML template below. The attestation is the artefact a
reviewer, auditor, or counterparty reads to confirm the conformance
claim. The template carries the conformance-claim metadata, the in-scope
inventory snapshot, the named roles, the documents in force, the gate
posture per system, and the waiver portfolio.

```yaml
# ASDLC Profile Conformance Attestation
asdlc_version: "<git tag or commit hash of asdlc.md at the time of attestation>"
claimed_profile: "<one of: ASDLC-Limited | ASDLC-Standard | ASDLC-Regulated | ASDLC-Tier4>"
conformance_period:
  start: "<ISO-8601 date>"
  end: "<ISO-8601 date>"
last_attestation_date: "<ISO-8601 date>"
next_attestation_due: "<ISO-8601 date>"

scope_of_application:
  organisation: "<legal entity name>"
  business_units: ["<unit-1>", "<unit-2>"]
  in_scope_systems:
    - system_id: "<identifier>"
      name: "<system name>"
      blast_radius_tier: "<BR1 | BR2 | BR3>"
      autonomy_tier: "<1 | 2 | 3 | 4>"
      external_facing: <true|false>
      adoption_phase: <1|2|3|4|5>
      regulated_domain_files: ["<domains/...md>", "..."]   # Regulated and Tier4 only
      regulator_of_record: "<regulator name or n/a>"       # Regulated and Tier4 only
      envelope_specification: "<path or n/a>"              # Tier4 only
  out_of_scope_systems_with_rationale:
    - system_id: "<identifier>"
      rationale: "<why this system is not governed under this profile>"

accountable_executive:
  name: "<person>"
  title: "<title>"
  residual_risk_acceptance_signed_on: "<ISO-8601 date>"     # Regulated and Tier4
  signature_record: "<reference-to-signed-attestation>"

auditor_of_record:
  type: "<self-attestation | internal-audit | external-audit>"
  name: "<organisation or person>"
  scope_of_review: "<what the auditor reviewed>"
  date_of_review: "<ISO-8601 date>"

required_documents_in_force:
  - path: "<path-to-document>"
    version_or_hash: "<version tag or content hash>"

roles_filled:
  accountable_humans_count: <integer>
  system_stewards: ["<person>", "..."]
  governance_portfolio_owner: "<person or n/a>"
  release_managers: ["<person>", "..."]
  governance_tooling_sre: "<person or n/a>"
  security_function_lead: "<person or n/a>"
  compliance_function_lead: "<person or n/a>"
  compliance_liaison: "<person or n/a>"                     # Regulated and Tier4
  regulator_of_record_liaisons:                             # Regulated and Tier4
    - domain: "<domains/...md>"
      person: "<person>"
  envelope_stewards: ["<person>", "..."]                    # Tier4 only
  aent_m_escalation_authorities:                            # Tier4 with AEnt-M
    - envelope: "<envelope-id>"
      action_class: "<class>"
      person: "<person>"
  igm_substrate_authority_liaison: "<person or n/a>"        # Tier4 with IGM

cadences_observed:
  governance_portfolio_review: "<e.g. quarterly>"
  waiver_portfolio_review: "<e.g. quarterly>"
  dod_recheck: "<e.g. quarterly>"
  residual_risk_re_signature: "<e.g. annual>"               # Regulated and Tier4
  domain_compliance_evidence: "<as required by domains/ file>"  # Regulated, Tier4
  envelope_review: "<e.g. monthly initially, quarterly steady>" # Tier4 only

gate_posture:
  # For each in-scope system, per gate, declare GateState per the canonical
  # gate_state_enum in governance/gate-registry.yaml. The four gates run at
  # full registry strength; this section records OUTCOMES, not relaxations.
  - system_id: "<identifier>"
    specification_readiness:
      state: "<pass|fail|missing|stale|contradicted|waived|requires-human-decision>"
      waivers_in_force: ["<waiver-record-reference>"]
    release_gate:
      state: "<...>"
      waivers_in_force: ["<...>"]
    operational_readiness:
      state: "<...>"
      waivers_in_force: ["<...>"]
    retirement_gate:
      applicable: <true|false>
      state: "<... or n/a>"
      waivers_in_force: ["<...>"]

waiver_portfolio:
  total_active_waivers: <integer>
  systems_carrying_waivers: <integer>
  most_waived_condition: "<condition-id or n/a>"
  ceiling_status: "<within-ceiling | breach with explanation>"
  reference: "waiver-governance.md"

known_gaps_under_remediation:
  - gap: "<description>"
    target_close_date: "<ISO-8601>"

attestation_statement: |
  The accountable executive named above attests that, as of the start of
  the conformance period, the organisation operates the ASDLC profile
  claimed against the in-scope systems enumerated above; that the four
  ASDLC gates run at full registry strength for every in-scope system;
  that every non-`pass` GateState is recorded in the gate_posture section
  with a current waiver under waiver-governance.md or with an explicit
  remediation plan; that no gate has been treated as "passed at a
  profile-minimum subset of conditions"; and that the waivers in force
  are current, named, dated, and within the profile's ceiling. The
  attestation is filed against the asdlc_version named at the top of
  this record; subsequent ASDLC versions do not retroactively void the
  attestation but trigger a re-attestation obligation under the
  framework's versioning policy.
```

The attestation is filed at the start of the conformance period and is
re-issued at the start of the next period or on any material change to
the in-scope inventory, the profile claimed, the named accountable
executive, or the framework version. A profile claim made publicly
without a current attestation is not a defensible claim.

---

## Profile transitions

An organisation MAY move between profiles. Transitions are governed
events, not silent re-scopings.

- **Upward transition** (Limited -> Standard, Standard -> Regulated,
  Regulated -> Tier4). Requires a new attestation against the higher
  profile. The transition date is the date the higher profile's scope,
  roles, cadences, and required documents are substantively in force,
  not the date the new attestation is published.
- **Downward transition** (Tier4 -> Regulated, Regulated -> Standard,
  Standard -> Limited). Permitted only after the systems whose
  blast-radius tier, regulated-domain mapping, or Tier-4 envelope status
  justified the higher profile have been retired (passing the Retirement
  Gate per [retirement-gate.md](retirement-gate.md)) or moved to a
  separately-attested portfolio at the higher profile. A downward
  transition while higher-scope systems remain in the attested
  portfolio is a misrepresentation; the attestation does not cover what
  the organisation is operating.

Transition records — the prior attestation, the new attestation, and the
substantive change that justified the transition — are retained for the
same period as the underlying attestations.

---

## Relationship to other ASDLC documents

This document defines the profiles against which conformance is claimed
and the attestation mechanism by which a claim is made auditable. The
condition counts, identifiers, blocking status, and tier-applicability
rules referenced in the profile definitions defer to
[governance/gate-registry.yaml](governance/gate-registry.yaml); where the
registry diverges from this document, the registry governs and this
document MUST be corrected. The waiver lifecycle and portfolio thresholds
referenced in the waiver-ceiling rows defer to
[waiver-governance.md](waiver-governance.md). The accountable executive
at whom the residual-risk recursion terminates is defined in
[asdlc.md](asdlc.md) "Termination of recursion". The Retirement Gate
referenced under every profile is defined in
[retirement-gate.md](retirement-gate.md). The Tier-4 envelope obligations
referenced under ASDLC-Tier4 are authoritative in
[annex-aentm.md](annex-aentm.md) and [annex-igm.md](annex-igm.md).
Domain-specific obligations that interact with ASDLC-Regulated and
ASDLC-Tier4 are documented in the `domains/` files, including the
financial services, insurance, pharma, aviation, automotive,
defense-government, HIPAA, SOX, and CCPA mappings. The cost implications
of operating each profile are documented in
[annex-adoption-cost.md](annex-adoption-cost.md).
