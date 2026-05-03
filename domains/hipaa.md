# ASDLC Domain Guidance — HIPAA

_US Health Insurance Portability and Accountability Act regulatory
obligations as they intersect ASDLC Layers 1, 3, and 4. This file maps
HIPAA's Privacy Rule, Security Rule, and Breach Notification Rule onto
the gate conditions and operational obligations of the ASDLC; it does not
substitute for qualified healthcare-counsel advice on HIPAA itself._

See [asdlc.md](../asdlc.md) for the four-layer model. See
[governance/gate-registry.md](../governance/gate-registry.md) for the
canonical gate condition enumeration. See
[release-governance.md](../release-governance.md) and
[operations/dod.md](../operations/dod.md) for the authoritative gate
condition definitions.

---

## Scope

This file is binding on covered entities and business associates as
defined under HIPAA, where agentic systems process Protected Health
Information (PHI) or interact with systems that do. The HIPAA components
relevant to ASDLC governance are:

- **Privacy Rule** (45 CFR Part 164, Subpart E) — uses and disclosures
  of PHI, the minimum necessary standard, individual rights.
- **Security Rule** (45 CFR Part 164, Subpart C) — administrative,
  physical, and technical safeguards for electronic PHI.
- **Breach Notification Rule** (45 CFR Part 164, Subpart D) — detection
  and notification of breaches of unsecured PHI.

ASDLC supports compliance with these rules for agentic systems whose
operation touches PHI. HIPAA imposes additional requirements (Business
Associate Agreements, Notice of Privacy Practices, individual rights
processing) that are contractual and procedural matters outside the
delivery framework.

---

## Layer 1 — Demand & Value obligations

The PHI classification of any data the system will process must be
identified at the SR Gate as part of SR-4 (Constraints Identified). PHI
classification is not an engineering implementation concern; it is a
demand-layer constraint that determines which downstream Security Rule
and Privacy Rule obligations attach to the system.

Specifically:

- **Data classification.** SR-4 must enumerate, for the proposed system,
  the data classes the system will process and whether each class
  contains PHI. The classification must be made at the demand stage
  because it determines the system's blast radius (SR-6) and the
  constraints set itself; a system that discovers it is processing PHI
  during engineering execution has produced an SR Gate pass against an
  incomplete constraint set.
- **Minimum necessary determination.** For systems that will process
  PHI, SR-4 must include a determination of the minimum necessary scope
  of PHI access required for the system's stated purpose. The
  determination is a Privacy Rule requirement (45 CFR § 164.502(b)) and
  is the input to the agent control plane's data access classification
  for the system (see [agent-control-plane.md](../agent-control-plane.md)).
- **Permitted uses and disclosures.** SR-1 (Business Need Validated)
  must reference the specific permitted use or disclosure under 45 CFR
  § 164.502 that the system's PHI processing falls under (treatment,
  payment, healthcare operations, or another permitted category). A
  system that processes PHI without a stated permitted basis has not
  validated its business need under HIPAA; the basis is part of the
  validation.

The accountable human named under SR-5 for a PHI-processing system must
be a person with named PHI-handling responsibility under the
organisation's Privacy Officer's structure — not an engineering manager
in isolation. The organisation's Privacy Officer remains the entity-
level accountability anchor; the system's accountable human is the
delivery-layer counterpart.

---

## Layer 3 — Release Gate obligations

The Release Gate's eight canonical conditions all apply to PHI-processing
systems. HIPAA adds:

- **RG-1 (Evidence Bundle Complete) — Security Rule risk analysis.** The
  evidence bundle must include a risk analysis under 45 CFR §
  164.308(a)(1)(ii)(A) covering the system as deployed. The risk
  analysis must enumerate the reasonably anticipated threats to the
  confidentiality, integrity, and availability of the ePHI the system
  processes, and must state the security measures the system implements
  in response to each. A risk analysis conducted at a prior version of
  the system, against a different deployment configuration, or against a
  different scope of PHI is not the risk analysis required for the
  current release.
- **RG-2 (Independent Validation Passed) — privacy review.** Independent
  validation for a PHI-processing system must include privacy review:
  the validator must attest that the system's PHI uses, disclosures, and
  data flows match the permitted basis recorded under SR-1. A technical
  independent validation that does not include privacy review has
  validated the engineering correctness but not the privacy correctness
  of the release.
- **RG-5 (Compliance Documentation Complete).** Compliance documentation
  for a PHI-processing system includes the risk analysis (above), the
  data flow diagram showing PHI movement, and any required updates to
  the organisation's Notice of Privacy Practices where the system
  introduces a new use or disclosure.
- **RG-6 (Dynamic Security Testing).** PHI-processing systems are
  external-facing for the purposes of RG-6 even where they are
  internally accessed only, because the threat model around PHI extends
  to the internal-network attack surface. Dynamic security testing is
  required.

The Privacy Rule's individual rights (access, amendment, accounting of
disclosures) impose response-time obligations on the entity. Where the
system is the technical mechanism for honouring those rights, the
relevant SLOs must be encoded as system requirements at the Release Gate
and exercised in DR/failover testing under DoD-8.

---

## Layer 4 — Operations & Maintenance obligations

The Operational DoD's eight conditions apply. HIPAA adds:

- **Breach detection and notification SLO.** The Breach Notification
  Rule (45 CFR § 164.402 and § 164.404) requires notification within
  defined windows from the discovery of a breach of unsecured PHI. The
  detection-to-notification SLO must be encoded into the system's
  incident handling per [operations/governance.md](../operations/governance.md).
  A system whose incident response procedure does not name the breach-
  notification SLO has not made the regulatory obligation operationally
  binding.
- **Minimum necessary in operation.** The minimum necessary standard
  applies continuously, not only at design. The agent control plane's
  `data_access_classification` for the system (see
  [agent-control-plane.md](../agent-control-plane.md)) must enforce the
  minimum necessary determination made at SR-4, and must produce an
  audit trail of agent PHI access events sufficient to confirm
  conformance. An access pattern that exceeds the minimum necessary scope
  is a Privacy Rule incident even if no breach has occurred.
- **DoD-7 (Trace Retention Policy Set).** Reasoning-trace retention for
  PHI-processing systems must satisfy 45 CFR § 164.316(b), which
  requires policies, procedures, and other documentation related to the
  Security Rule to be retained for six years from the date of creation
  or the date when last in effect, whichever is later. Reasoning traces
  that document agent decisions about PHI fall within this requirement.
- **Quarterly DoD review.** The quarterly DoD review for a PHI-
  processing system must include attestation that the Security Rule's
  administrative, physical, and technical safeguards remain in force,
  and that the minimum necessary determination remains accurate against
  the system's actual operation.

---

## Specific limitation

Business Associate Agreements remain a contractual matter. ASDLC does not
produce them. Where an agentic system depends on third-party services
that themselves process PHI on behalf of the covered entity, the BAA
between the covered entity and the third party is a contractual artefact
governed outside the framework. The framework's release gate may treat
the existence of a current BAA as a precondition to release for systems
that introduce a new third-party PHI processor, but the BAA itself is
authored, negotiated, and maintained outside the framework.

The verb is "supports compliance with"; the framework does not satisfy
HIPAA on its own.

---

## Cited authorities

- 45 CFR § 164.308 — Administrative safeguards (including § 164.308(a)(1)(ii)(A)
  risk analysis).
- 45 CFR § 164.310 — Physical safeguards.
- 45 CFR § 164.312 — Technical safeguards.
- 45 CFR § 164.316(b) — Documentation retention.
- 45 CFR § 164.402 — Definition of breach.
- 45 CFR § 164.404 — Notification to individuals.
- 45 CFR § 164.502 — Uses and disclosures of PHI: general rules
  (including § 164.502(b) minimum necessary).
- HIPAA Privacy Rule and Security Rule, codified at 45 CFR Part 164.

---

## Relationship to other ASDLC documents

This domain file augments the framework-agnostic obligations defined in
[asdlc.md](../asdlc.md), [specification-readiness.md](../specification-readiness.md),
[release-governance.md](../release-governance.md), and
[operations/dod.md](../operations/dod.md). The interaction with the
agent control plane's data access classification is documented in
[agent-control-plane.md](../agent-control-plane.md). The Retirement
Gate's RT-3 (Trace and Reasoning-Record Archival) is the natural place
to resolve any conflict between the HIPAA retention floor and a data-
subject-rights deletion request; see [retirement-gate.md](../retirement-gate.md).
The conformance profile applicable to most HIPAA-bound organisations is
ASDLC-Regulated (see [conformance-profiles.md](../conformance-profiles.md)).
