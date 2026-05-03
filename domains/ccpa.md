# ASDLC Domain Guidance — CCPA / CPRA

_California Consumer Privacy Act and California Privacy Rights Act
regulatory obligations as they intersect ASDLC Layers 1, 3, and 4. This
file maps consumer-rights and data-handling requirements under California
privacy law onto the gate conditions and operational obligations of the
ASDLC; it does not substitute for qualified privacy-counsel advice on
California law itself._

See [asdlc.md](../asdlc.md) for the four-layer model. See
[governance/gate-registry.md](../governance/gate-registry.md) for the
canonical gate condition enumeration. See
[release-governance.md](../release-governance.md) and
[operations/dod.md](../operations/dod.md) for the authoritative gate
condition definitions.

---

## Scope

This file is binding on businesses subject to the California Consumer
Privacy Act (CCPA) of 2018 as amended by the California Privacy Rights
Act (CPRA) of 2020, where agentic systems process personal information
of California consumers. The components most relevant to ASDLC governance
are:

- **Consumer rights** — access, deletion, correction, opt-out of
  sale/sharing, opt-out of use of sensitive personal information for
  certain purposes (Cal. Civ. Code §§ 1798.100, 1798.105, 1798.106,
  1798.120, 1798.121).
- **Data handling principles** — purpose limitation, data minimisation,
  storage limitation (§ 1798.100(c)).
- **Notice obligations** at or before collection (§ 1798.100(a)).
- **Recordkeeping** (Cal. Code Regs. tit. 11, § 7101 et seq., as
  promulgated under CPRA).

ASDLC supports compliance with these provisions for agentic systems
whose operation involves California consumer personal information.

---

## Layer 1 — Demand & Value obligations

Consumer rights — the right to know, the right to delete, the right to
correct, and the rights to opt out of sale/sharing and of certain uses
of sensitive personal information — must be mapped onto the system's
demand validation. SR-1 (Business Need Validated) and SR-4 (Constraints
Identified) carry the relevant obligations:

- **Personal information classification.** SR-4 must enumerate the
  categories of personal information the system will collect, process,
  or share (using the categories named in Cal. Civ. Code §
  1798.140(v)). It must also state whether any of those categories
  constitute sensitive personal information under § 1798.140(ae); the
  designation triggers the additional opt-out right under § 1798.121.
- **Purpose limitation.** SR-1 must record the specific business
  purpose(s) for which the personal information will be processed. The
  purpose statement is directly referenced by the notice obligation
  under § 1798.100(a) and constrains downstream processing under §
  1798.100(c). A system whose purpose statement at SR-1 is broader than
  the business need has invited a downstream privacy violation.
- **Sale and sharing determination.** SR-1 must include an explicit
  determination of whether the system's processing constitutes a sale
  or sharing of personal information under § 1798.140(ad) and §
  1798.140(ah). The determination is a structured field, not free text.
  A system whose determination is "no sale or sharing" must state, in
  the SR record, the analysis that supports the determination.
- **Consumer rights handling.** SR-4 must enumerate how the system will
  honour each applicable consumer right. Where the system is itself the
  technical mechanism for honouring a right (for example, a system that
  performs the deletion when a consumer's deletion request is received),
  the right's response SLO is a constraint on the system's operational
  design, not only on its compliance posture.

The accountable human under SR-5 for a system processing California
consumer personal information must be a person whose role carries
California privacy accountability — typically the CPRA Chief Privacy
Officer's delegate at the system's business unit or an equivalent named
role.

---

## Layer 3 — Release Gate obligations

The Release Gate's eight canonical conditions all apply. CCPA/CPRA adds:

- **RG-1 (Evidence Bundle Complete) — data inventory.** The evidence
  bundle must include a current data inventory for the deployed system:
  the categories of personal information collected, the source of each
  category, the purposes of processing, the categories of recipients
  (if any), the retention period per category, and the legal basis or
  exception under California law that the processing relies upon. The
  inventory is the operational artefact behind the notice at collection
  obligation; a release whose inventory and notice diverge is in
  immediate non-compliance.
- **RG-1 — purpose limitations.** The evidence bundle must include the
  purpose statement filed at SR-1 in machine-readable form, with a
  cross-reference to the agent-control-plane purpose constraints (see
  [agent-control-plane.md](../agent-control-plane.md)) that enforce the
  limitation in operation. A system whose evidence bundle records a
  purpose statement but whose runtime control plane does not enforce
  the limitation has produced documentation without enforcement.
- **RG-5 (Compliance Documentation Complete).** Compliance documentation
  includes the data inventory, the notice text (or a reference to the
  consolidated organisational notice if the system contributes to it),
  and the consumer-rights handling procedures for the system.
- **RG-2 (Independent Validation Passed) — privacy review.** Where the
  system introduces new categories of personal information processing,
  new purposes, or new sale/sharing arrangements, independent validation
  must include privacy review. The reviewer must attest that the
  release's data flows match the disclosures made under the notice
  obligation.

---

## Layer 4 — Operations & Maintenance obligations

The Operational DoD's eight conditions apply. CCPA/CPRA adds:

- **Consumer-rights response SLOs.** Cal. Civ. Code § 1798.130(a)(2)
  requires response to verifiable consumer requests within 45 calendar
  days, with a permitted extension of an additional 45 days where
  reasonably necessary. The response SLO must be encoded into the
  system's incident-and-request handling and surfaced in DoD-2
  observability. A system that holds responses in a queue without an
  SLO timer has not operationalised the regulatory deadline.
- **Recordkeeping retention — 24 months.** Cal. Code Regs. tit. 11, §
  7101(a) requires businesses to maintain records of consumer requests
  and the responses thereto for at least 24 months. DoD-7 (Trace
  Retention Policy Set) for systems within scope must reflect this
  floor; where the system is the technical recipient of consumer
  requests, the retention policy must cover the request, the verification
  artefacts, and the response.
- **Sale and sharing telemetry.** For systems that participate in any
  flow of personal information that constitutes sale or sharing under
  the CPRA definitions, DoD-2 (Operational Observability Configured)
  must include telemetry sufficient to demonstrate that opt-outs have
  been honoured. A consumer who opted out of sale or sharing whose
  personal information continued to flow under the opted-out category
  is a continuing CCPA/CPRA violation; the operational observability
  must surface the violation, not only the absence of the violation.
- **Quarterly DoD review.** The quarterly DoD review for a CCPA/CPRA-
  scoped system must include attestation that the data inventory remains
  current, the purpose limitations remain enforced by the agent control
  plane, and the consumer-rights response SLOs are being met.

---

## Specific limitation

The CCPA/CPRA regulatory landscape is evolving, particularly with
respect to automated decision-making and profiling. The California
Privacy Protection Agency (CPPA) has issued and continues to refine
regulations under CPRA. As of 2025, the CPRA regulations addressing
automated decision-making technology (ADMT) and profiling impose
notice, opt-out, and access obligations that overlap with — but are not
identical to — the GDPR's Article 22 framework. A system that performs
profiling or automated decision-making affecting California consumers
must consult the CPPA regulations as they stand at the time of release,
not only the statute. The framework supports the documentation and
governance pipeline that those regulations require; it does not state
the regulations' operative text.

The verb is "supports compliance with"; the framework does not satisfy
California privacy law on its own.

---

## Cited authorities

- Cal. Civ. Code § 1798.100 et seq. — California Consumer Privacy Act,
  as amended by the California Privacy Rights Act.
- Cal. Civ. Code § 1798.105 — Right to delete personal information.
- Cal. Civ. Code § 1798.106 — Right to correct inaccurate personal
  information.
- Cal. Civ. Code § 1798.120 — Right to opt-out of sale or sharing.
- Cal. Civ. Code § 1798.121 — Right to limit use and disclosure of
  sensitive personal information.
- Cal. Civ. Code § 1798.130 — Notice, disclosure, correction, and
  deletion requirements.
- Cal. Civ. Code § 1798.140 — Definitions, including § 1798.140(d)
  ("sale"), § 1798.140(ad) ("sale" further defined), § 1798.140(ah)
  ("sharing"), § 1798.140(v) ("personal information" categories), and
  § 1798.140(ae) ("sensitive personal information").
- Cal. Code Regs. tit. 11, § 7101 et seq. — CPRA implementing
  regulations as promulgated by the California Privacy Protection
  Agency.

---

## Relationship to other ASDLC documents

This domain file augments the framework-agnostic obligations defined in
[asdlc.md](../asdlc.md), [specification-readiness.md](../specification-readiness.md),
[release-governance.md](../release-governance.md), and
[operations/dod.md](../operations/dod.md). The interaction with the
agent control plane is documented in [agent-control-plane.md](../agent-control-plane.md).
Condition RT-3 of the Retirement Gate is the natural locus for resolving
any conflict between the CCPA/CPRA deletion right and other retention
obligations; see [retirement-gate.md](../retirement-gate.md). For
organisations subject to multiple privacy regimes, see also
[domains/hipaa.md](hipaa.md) where the personal information includes PHI
and [eu-ai-act-mapping.md](../eu-ai-act-mapping.md) where the system
performs automated decision-making affecting California consumers and
is also classified as an AI system under EU law applicable to the
business. The conformance profile applicable to most CCPA/CPRA-bound
organisations is ASDLC-Regulated (see [conformance-profiles.md](../conformance-profiles.md)).
