# ASDLC Domain Guidance — Sarbanes-Oxley (SOX)

_US Sarbanes-Oxley Act regulatory obligations as they intersect ASDLC
Layers 1, 3, and 4. This file maps SOX requirements onto the gate
conditions and operational obligations of the ASDLC; it does not
substitute for qualified securities-counsel advice on SOX itself._

See [asdlc.md](../asdlc.md) for the four-layer model. See
[governance/gate-registry.md](../governance/gate-registry.md) for the
canonical gate condition enumeration referenced below. See
[release-governance.md](../release-governance.md) and
[operations/dod.md](../operations/dod.md) for the authoritative gate
condition definitions.

---

## Scope

This file is binding on organisations subject to the US Sarbanes-Oxley Act
of 2002 (SOX). SOX applies to public companies registered with the U.S.
Securities and Exchange Commission and, with specific provisions, to
their auditors. SOX is implemented through the Public Company Accounting
Oversight Board's (PCAOB) auditing standards, the SEC's implementing
rules, and the Internal Control over Financial Reporting (ICFR) regime.

The SOX provisions most relevant to agentic delivery in scope of ICFR are:

- **Section 302** — CEO/CFO certification of the accuracy of periodic
  reports and the effectiveness of disclosure controls.
- **Section 404(a)** — management assessment of ICFR.
- **Section 404(b)** — external auditor opinion on ICFR for accelerated
  and large accelerated filers.
- **Section 906** — criminal penalties for false certifications.
- **SEC Rule 13a-15** — implementing rule requiring disclosure controls
  and procedures and ICFR.

ASDLC supports compliance with these provisions for agentic systems whose
behaviour can affect financial reporting. ASDLC does not itself satisfy
SOX: SOX requires audited management assessment and, for accelerated
filers, an external auditor opinion. The framework provides the
governance evidence pipeline that the SOX assessment and audit are
conducted against. The verb is "supports compliance with"; not
"satisfies".

---

## Layer 1 — Demand & Value obligations

A change to an agentic system that may affect financial reporting must,
at the SR Gate, identify the specific ICFR control(s) the change
interacts with. This obligation attaches at SR-4 (Constraints Identified)
and SR-6 (Blast Radius Assessed): a change touching the period-close
process, the general ledger, financial calculations, audit-relevant
configuration, or any control that financial reporting depends upon is
not BR1 by default. The blast radius reflects the financial-reporting
exposure, and the constraints set must enumerate the relevant ICFR
controls.

The COSO 2013 framework's five components — control environment, risk
assessment, control activities, information and communication, and
monitoring — provide the structural reference for the control
identification at the demand layer. A change whose constraint set does
not name the COSO component(s) it touches is incomplete with respect to
SOX.

For systems that produce or modify financial-reporting outputs, SR-1
(Business Need Validated) must include a determination, recorded in the
demand record, of whether the change is in scope of ICFR. The
determination is a structured field, not free text; it is the input to
subsequent SOX-specific gate obligations.

The SR Gate's standard nine conditions otherwise apply unchanged. The
SOX-specific obligations augment SR-1, SR-4, and SR-6; they do not
replace any condition.

---

## Layer 3 — Release Gate obligations

The Release Gate's eight canonical conditions all apply to ICFR-in-scope
changes. SOX adds the following augmentations:

- **RG-1 (Evidence Bundle Complete) — change-management documentation.**
  The evidence bundle must include change-management documentation that
  satisfies COSO 2013's control activity requirements (CC5.1 — selection
  and development of control activities; CC5.2 — selection and
  development of general controls over technology; CC5.3 — deployment
  through policies and procedures). The documentation must show the
  control activity that was applied to the change, the artefact that
  evidences its application, and the named individual who performed it.
- **RG-3 (Rollback Procedure Tested) — period-close timing.** Rollback
  testing for an ICFR-in-scope change must extend to the financial
  reporting cycle's period-close timing. A rollback procedure tested
  against a steady-state environment but not against the period-close
  environment has not been tested against the conditions under which the
  rollback would actually be executed in a financial-reporting incident.
  The rollback test record must state which period-close phase (cut-off,
  sub-ledger close, consolidation, reporting) the test was conducted
  against.
- **RG-2 (Independent Validation Passed).** ICFR-in-scope changes are
  high-stakes regulated systems for the purposes of RG-2; independent
  validation is required regardless of the system's autonomy phase. The
  independent validator must be organisationally separate from the
  development team and must have no reporting relationship to the
  function whose financial reporting the change touches.
- **RG-5 (Compliance Documentation Complete).** Compliance documentation
  for an ICFR-in-scope change includes the change record, the impact
  assessment naming the affected controls, and the testing evidence the
  change-management process produced. "Filed" means filed in the
  organisation's controls register, not drafted.

The SR-5 named accountable human for an ICFR-in-scope system must be a
person whose role carries financial-reporting accountability — typically
a Controller, a Finance director with named ICFR responsibility, or an
equivalent named role. A purely engineering accountable human does not
satisfy the substantive requirement, even though the gate condition's
text requires only "a named human".

---

## Layer 4 — Operations & Maintenance obligations

The Operational Definition of Done's eight conditions all apply.
SOX adds the following:

- **DoD-7 (Trace Retention Policy Set) — extended retention.** Trace and
  reasoning-record retention extends to the longer of seven years or the
  organisation's records-retention policy for financial-reporting
  records. The seven-year baseline is the SOX baseline; an organisation
  whose own retention policy is longer governs at the longer period.
  Trace records that fall outside the retention window cannot be
  produced in a SOX audit, and their absence is a control deficiency
  even if no incident occurred during the window.
- **Segregation-of-duties for agentic actions affecting financial data.**
  The agent control plane (see [agent-control-plane.md](../agent-control-plane.md))
  must enforce segregation of duties for agent actions that affect
  financial-data systems: an agent that prepares a financial entry must
  not be the same agent (or the same agent configuration) that approves
  the entry. The DoD's runbook (DoD-1) must document how segregation is
  enforced and how breaches are detected and escalated. A breach of
  segregation by an agent action is a control failure under COSO and
  must be reported to the system steward and to the named accountable
  human at the layer of authority appropriate to the breach's
  materiality.
- **DoD-3 (On-Call Assignment Made).** The on-call escalation chain for
  an ICFR-in-scope system includes a finance-side escalation contact in
  addition to the engineering on-call. An incident whose impact on
  financial reporting cannot be assessed without finance-side judgment
  cannot be triaged correctly without that escalation contact in the
  chain.
- **Quarterly DoD review.** The standard quarterly DoD review for an
  ICFR-in-scope system must include explicit attestation that the SOX-
  specific augmentations above remain satisfied. A DoD review that
  attests only to the framework-agnostic conditions has not addressed
  the SOX-specific obligations.

---

## Specific limitation

The ASDLC supports compliance with SOX. It does not satisfy SOX.

- SOX Section 404(a) requires management to assess the effectiveness of
  ICFR. The assessment is a management activity, not a deliverable of
  the ASDLC. The framework produces evidence; the management assessment
  consumes it.
- SOX Section 404(b) requires, for accelerated and large accelerated
  filers, an external auditor opinion on ICFR. The external auditor's
  testing is an audit activity outside the framework. The framework's
  evidence bundles and control state records are inputs to the audit;
  they are not a substitute for it.
- SOX Section 302 and Section 906 certifications are executive
  certifications. The named accountable human at the system level is not
  the certifying officer; the certifying officer is the CEO and CFO at
  the entity level. The framework's accountability chain is upstream of
  the certification, not the certification itself.

The verb in any conformance claim must be "supports compliance with",
not "satisfies", "ensures", or "achieves" SOX compliance.

---

## Cited authorities

- Sarbanes-Oxley Act of 2002, Section 302 (Corporate Responsibility for
  Financial Reports), Section 404(a) (Management Assessment of Internal
  Controls), Section 404(b) (Auditor Attestation), and Section 906
  (Corporate Responsibility for Financial Reports — criminal
  liability).
- SEC Rule 13a-15 (17 CFR § 240.13a-15) — Controls and procedures.
- COSO 2013 Internal Control — Integrated Framework.
- PCAOB Auditing Standard No. 2201 (formerly AS 5) — An Audit of
  Internal Control Over Financial Reporting That Is Integrated with an
  Audit of Financial Statements.

---

## Relationship to other ASDLC documents

This domain file augments the framework-agnostic obligations defined in
[asdlc.md](../asdlc.md), [specification-readiness.md](../specification-readiness.md),
[release-governance.md](../release-governance.md), and
[operations/dod.md](../operations/dod.md). The SOX-specific augmentations
above do not modify the underlying gate condition set; they specify how
the conditions apply when the system is in scope of ICFR. The Retirement
Gate's RT-3 (Trace and Reasoning-Record Archival) condition is
particularly sensitive in a SOX context because the retention floor is
seven years; see [retirement-gate.md](../retirement-gate.md). For
organisations whose SOX obligations are part of a broader regulated
profile, see also [domains/financial-services.md](financial-services.md)
for the financial-services-wide regulatory mapping. The conformance
profile applicable to most SOX-bound organisations is ASDLC-Regulated
(see [conformance-profiles.md](../conformance-profiles.md)).
