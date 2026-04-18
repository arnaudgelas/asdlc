# ASDLC Domain Guidance — Financial Services

_Financial services-specific regulatory requirements for ASDLC Layers 1, 3,
and 4._

See
[Financial Services Manifesto Alignment](../../domains/financial-services.md)
for manifesto principle mappings (SR 11-7, DORA, EU AI Act, SOX, Three Lines of
Defense). See the [ASDLC Overview](../asdlc.md) for the full lifecycle
framework.

---

## ASDLC Layer 1 — Demand & Value Regulatory Requirements (Financial Services)

Layer 1 — the governed demand layer defined in
[demand/value.md](../demand/value.md) — is not merely a planning precursor to
engineering. In financial services, it is the point at which several regulatory
obligations first attach. Conceptual soundness, risk identification, and
business need validation are regulatory requirements, not just good practice.
The specification readiness gate is the Layer 1 governance control that ensures
those requirements are met before the engineering execution loop begins.

### SR 11-7 (Model Risk Management) — Conceptual Soundness at the Demand Stage

SR 11-7 requires documentation of the conceptual soundness of a model approach:
why this model architecture, what assumptions it relies on, what alternatives
were considered, and what the theoretical limitations are. This is not a
post-build documentation obligation — it is a pre-build governance requirement.
A team that begins engineering execution without documenting conceptual
soundness has inverted the SR 11-7 governance sequence.

The demand layer's specification readiness gate condition "business need
validated" maps directly to SR 11-7's conceptual soundness requirement. Before
the gate can be passed, the business demand sponsor must have documented why
this approach is appropriate for the problem — the evidence that makes "business
need validated" true is the same evidence that makes "conceptually sound"
defensible under SR 11-7. The gate condition "acceptance criteria expressible"
confirms that the model's intended function is specified precisely enough to be
verified — a prerequisite for SR 11-7's validation planning.

SR 11-7's "fit-for-purpose" validation begins at the demand stage. If a model's
purpose is not clearly defined at Layer 1, the Layer 2 engineering loop will
produce an artefact that cannot be validated for fitness of purpose, because no
purpose was ever governed.

### EU AI Act Article 9 — Risk Management System from Conception

EU AI Act Article 9 requires that high-risk AI systems are subject to a
documented risk management process throughout the system lifecycle. "Throughout
the lifecycle" begins at conception — before the engineering loop starts. A risk
management system that is initiated at the start of engineering execution is
already late.

The specification readiness gate conditions "blast radius assessed" and
"constraints identified" (defined in [demand/value.md](../demand/value.md) under
the demand-to-specification bridge) are the Layer 1 controls that satisfy
Article 9's requirement to identify and manage known and reasonably foreseeable
risks before the engineering loop begins. The blast radius assessment
establishes the scope of potential harm if the system fails or behaves
unexpectedly; the constraint identification step surfaces the regulatory,
technical, and operational boundaries within which the system must operate. Both
are demand-layer activities; both are Article 9 requirements.

The risk management system established at Layer 1 is not a static document.
Article 9 requires it to be a continuous iterative process. The demand layer's
feedback protocol from [demand/value.md](../demand/value.md) — which requires
that operational failures and value misses from Layer 4 feed back into the
demand validation process — is the mechanism that keeps the risk management
system live across the system's lifetime.

### DORA Article 5 — ICT Risk Management Framework and Pre-Change Risk

Identification

DORA Article 5 requires that financial entities identify and classify ICT risks
before implementing changes to ICT systems. The demand layer is the governance
point at which this identification occurs. An organisation that identifies ICT
risks only after engineering execution has begun has not satisfied Article 5's
timing requirement.

The demand layer's validation of business need — including the validation tier
calibrated to blast radius — and the assessment of constraints and blast radius
at the specification readiness gate are the governance controls that implement
DORA Article 5 risk identification and classification at the point where it is
required: before the change begins. The classification determines which
validation evidence is required, which approval path applies, and what change
management procedures govern the subsequent layers.

### MiFID II / Solvency II — Algorithm and Model Documentation before Execution

Under MiFID II Article 17, investment firms must have in place effective systems
and risk controls for algorithmic trading systems, including pre- and post-trade
controls and business continuity arrangements. Algorithm and model changes must
be conceptually sound and documented before they enter execution. The demand
backlog — with its evidence-backed validation requirements and explicit business
demand sponsor sign-off — is the governance control that ensures changes to
algorithmic trading systems are governed before engineering begins.

Under Solvency II, actuarial models and internal models used for capital
assessment must have documented rationale and methodology. The demand layer's
value definition requirement — which mandates a precise, measurable business
value statement as a condition of entering the specification readiness gate —
ensures that model changes are purposeful and documented at the point of
origination, before engineering investment begins.

Portfolio governance at the demand layer (the demand backlog, prioritisation
criteria, and capacity model described in [demand/value.md](../demand/value.md))
is the operational mechanism by which these pre-execution documentation
requirements are satisfied at the organisational level, not just the individual
change level.

### Layer 1 Regulatory Control Mapping

| Regulation                  | Layer 1 Requirement                                                                                                                | ASDLC Control                                                                                                                              | Gap                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SR 11-7                     | Conceptual soundness documented before model development begins; fit-for-purpose validation planned at inception                   | Specification readiness gate: "business need validated" and "acceptance criteria expressible" conditions; business demand sponsor sign-off | SR 11-7 expects documentation of alternatives considered and theoretical limitations; the demand layer governs that a need is validated, not that all model alternatives are enumerated. The specification analyst role must explicitly prompt for alternatives documentation for model-class items.                                                         |
| EU AI Act Art. 9            | Risk management system covers the full lifecycle from conception; known and foreseeable risks identified before engineering begins | Specification readiness gate: "blast radius assessed" and "constraints identified" conditions; validation tier scaled to blast radius      | Art. 9's requirement for a continuous iterative risk management process means Layer 1 risk identification must feed back from Layer 4 operational data. Feedback protocol in [demand/value.md](../demand/value.md) provides this loop, but the connection between operational incident data and demand-layer risk assessment must be explicitly established. |
| DORA Art. 5                 | ICT risks identified and classified before changes are implemented                                                                 | Demand backlog entry validation; blast radius assessment at specification readiness gate; change classification by tier                    | DORA expects ICT risk classification to connect to the change management process in Layer 3. The Layer 1 classification must flow through to the Layer 3 change record. No explicit hand-off mechanism defined between the demand layer's classification and the Layer 3 compliance documentation condition.                                                 |
| MiFID II Art. 17            | Algorithmic system changes conceptually sound and documented; pre-trade controls in place                                          | Demand backlog with evidence-backed validation; business demand sponsor accountability for the business case                               | MiFID II's pre-trade controls are Layer 2 and Layer 3 concerns; the demand layer governs that the change is conceptually justified. Gap: explicit call-out for algorithmic trading system changes as a category requiring heightened demand-layer validation is not built into the standard gate.                                                            |
| Solvency II internal models | Model changes documented before execution; methodology rationale preserved                                                         | Value definition requirement in the demand layer; business demand sponsor sign-off on the success criterion                                | Solvency II requires model documentation in the format prescribed by the applicable supervisory authority. The demand layer produces a business value statement; it does not produce Solvency II model documentation format. Translation into the required format must occur at Layer 2.                                                                     |

---

## ASDLC Layer 3 — Release & Deployment Regulatory Requirements (Financial

Services)

Layer 3 — release and deployment governance as defined in
[release-governance.md](../release-governance.md) — is the primary compliance
boundary for financial services change management regulation. The five release
gate conditions are not general good practice layered on top of regulatory
requirements; for several financial services regulations, they are the direct
implementation of specific legal obligations. This section maps those
obligations to the release gate and release Definition of Done in detail.

### DORA Article 14 — ICT Change Management

DORA Article 14 requires that financial entities implement a documented ICT
change management process that includes: pre-implementation testing of changes,
documented rollback procedures, and post-implementation review. For changes to
systems supporting critical or important functions, independent testing before
production deployment is required.

The ASDLC release gate directly satisfies Article 14's requirements. The mapping
is specific:

- DORA Art. 14(2)(a) — changes are tested before implementation: satisfied by
  release gate Condition 1 (evidence bundle complete, including evaluation
  reports from the engineering loop) and Condition 2 (independent validation
  passed for high-stakes systems).
- DORA Art. 14(2)(b) — documented rollback procedures: satisfied by release gate
  Condition 3 (rollback procedure tested, with a tested time-to-rollback on
  record).
- DORA Art. 14(2)(c) — post-implementation review: satisfied by the release
  Definition of Done condition requiring smoke tests in production, plus the
  operational readiness gate initiation that hands off to Layer 4 monitoring.
- DORA Art. 14 critical/important functions — independent testing: satisfied by
  release gate Condition 2 (independent validation passed), which is mandatory
  for high-stakes regulated systems regardless of phase.

For systems in DORA scope, the release gate is not optional — it is the Article
14 change management process. An organisation that has implemented the release
gate and maintains the evidence it produces has an auditable Article 14
compliance record. The evidence bundle ID referenced in the change record is the
DORA Article 14 test documentation.

### SR 11-7 — Model Change Documentation at the Release Boundary

SR 11-7 requires that model changes are documented, including the nature of the
change, the testing performed, and the validation results. At the release
boundary, the evidence bundle produced by the engineering execution loop is the
primary SR 11-7 model change document. The release gate's Condition 1 (evidence
bundle complete) is the SR 11-7 compliance control.

Specifically, SR 11-7 model change documentation must include:

- The nature of the change: satisfied by the diff in the evidence bundle and the
  specification reference in the change record.
- Testing performed: satisfied by the evaluation reports in the evidence bundle,
  including the test suite, pass/fail results, and evaluation metrics.
- Validation results: for material changes to high-risk models, satisfied by
  Condition 2 (independent validation passed), which records the named
  independent validator, date, scope, and finding.

The release gate's "compliance documentation complete" condition (Condition 5)
is the SR 11-7 model change record — it must reference the evidence bundle and
confirm that the change is filed in the model inventory before release proceeds.

### FCA PS21/3 and PRA PS6/21 — Operational Resilience at the Release Boundary

The FCA's Policy Statement PS21/3 and the PRA's Policy Statement PS6/21 on
operational resilience require that important business services can be
maintained within impact tolerances during severe but plausible disruptions. At
the release boundary, this imposes specific requirements on how changes are
deployed and how their reversibility is established.

The release gate's Condition 3 (rollback procedure tested) directly satisfies
the operational resilience requirement for demonstrable recovery capability. The
"time-to-rollback" measurement from the tested rollback procedure must fall
within the pre-agreed recovery time window — and that window must be calibrated
to the system's impact tolerance for the important business service it supports.
A rollback that takes longer than the impact tolerance permits is not a
compliant rollback procedure under PS21/3/PS6/21, regardless of whether it
eventually succeeds.

The release Definition of Done condition requiring monitoring and alerting
configuration before deployment completes maps to PS21/3's requirement that
firms can detect disruptions to important business services in time to remain
within impact tolerances. A system deployed without production monitoring does
not satisfy this requirement.

### EU AI Act Article 15 — Accuracy, Robustness, and Cybersecurity of High-Risk

AI

EU AI Act Article 15 requires that high-risk AI systems achieve the levels of
accuracy, robustness, and cybersecurity appropriate to their intended purpose,
and that they remain accurate and robust after deployment. At the release
boundary, this imposes requirements on both pre-release validation and
post-deployment monitoring readiness.

Release gate Condition 2 (independent validation passed) satisfies Article 15's
pre-release accuracy and robustness requirements: the independent validation
confirms that the system meets its specified acceptance criteria, including
performance criteria that are calibrated to the system's intended purpose. The
post-deployment smoke tests in the release Definition of Done confirm that
accuracy and robustness are maintained in the production environment against
production configuration — not just in the pre-deployment validation
environment.

The release Definition of Done condition requiring monitoring and alerting
configuration maps to Article 15's requirement for ongoing accuracy. A high-risk
AI system deployed without output quality monitoring and alerting has no
mechanism to detect accuracy degradation — which means the organisation cannot
satisfy Article 15's ongoing obligations from the moment of deployment.

### Layer 3 Regulatory Control Mapping

| Regulation              | Article/Section            | Release Requirement                                                                                 | ASDLC Control                                                                                                                          | Gap                                                                                                                                                                                                                                                                                            |
| ----------------------- | -------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DORA                    | Art. 14(2)(a)              | Pre-implementation testing documented                                                               | Evidence bundle complete (Condition 1): evaluation reports with pass/fail results                                                      | DORA requires specific retention of test documentation. Evidence bundle ID in change record provides the reference; retention period and format must be confirmed against DORA RTS on ICT change management when published.                                                                    |
| DORA                    | Art. 14(2)(b)              | Rollback procedures documented and verified                                                         | Rollback procedure tested (Condition 3): tested within 48 hours of deployment, time-to-rollback on record                              | DORA's "documented rollback procedures" requirement is met; DORA does not specify that rollback must be tested, only documented. The ASDLC's tested rollback condition exceeds the regulatory minimum.                                                                                         |
| DORA                    | Art. 14 critical functions | Independent testing before production for critical/important functions                              | Independent validation passed (Condition 2): named independent validator, scope, pass/fail                                             | Organisational separation requirement for independent testing must be confirmed against DORA RTS definitions of "independent." The manifesto's independence requirement (no reporting relationship to development lead) is consistent with reasonable interpretations.                         |
| SR 11-7                 | Model change governance    | Nature of change, testing performed, validation results documented before deployment                | Evidence bundle complete (Condition 1): diff, evaluation reports, trace IDs; independent validation (Condition 2) for material changes | SR 11-7 requires model inventory update to reflect the change. The change record's compliance documentation condition (Condition 5) should include model inventory update confirmation; this linkage is not explicit in the current release gate design.                                       |
| FCA PS21/3 / PRA PS6/21 | Operational resilience     | Recovery within impact tolerances for important business services; rollback capability demonstrated | Rollback procedure tested (Condition 3) with time-to-rollback within impact tolerance window; monitoring configured (release DoD)      | Impact tolerances are firm-specific and must be pre-defined. The release gate's rollback test does not automatically check whether the time-to-rollback satisfies the firm's impact tolerance for the specific important business service. This calibration step must be performed explicitly. |
| EU AI Act               | Art. 15                    | High-risk AI systems meet accuracy and robustness requirements at and after deployment              | Independent validation (Condition 2); post-deployment smoke tests (release DoD); monitoring and alerting configured (release DoD)      | Art. 15's cybersecurity requirements extend beyond functional testing. The release gate does not include a pre-release cybersecurity assessment specific to AI attack vectors (adversarial inputs, model inversion). This must be addressed in the evaluation suite design at Layer 2.         |

---

## ASDLC Layer 4 — Operations & Maintenance Regulatory Requirements (Financial

Services)

Layer 4 — operational governance as defined in
[operations/governance.md](../operations/governance.md) — is where the long-term
regulatory obligations of financial services supervision attach: ongoing model
monitoring, incident management, business continuity, and retention. The SLOs,
incident classification structures, and maintenance governance processes in the
operations layer are not operational preferences — for several financial
services regulations, they are legal requirements.

### DORA Articles 9–11 — ICT Risk Management, Incident Management, and Business

Continuity

**DORA Article 9** requires that financial entities' ICT risk management
processes include identification and management of ICT risks on an ongoing
basis, including vulnerability management. This maps to the ASDLC maintenance
governance's security patch management process, which applies CVSS-tiered SLOs:
CVSS ≥ 9.0 vulnerabilities patched within 24 hours, CVSS 7.0–8.9 within 72
hours, CVSS 4.0–6.9 within 30 days. The patch management SLOs are the Article 9
vulnerability management controls. They must be documented as such and measured
in production — a patch management SLO that is defined but not measured does not
satisfy Article 9's ongoing risk management requirement.

**DORA Article 10** requires that financial entities detect ICT-related
incidents, classify them by their impact, and manage them through a defined
incident management process. The ASDLC's incident classification framework from
[operations/governance.md](../operations/governance.md) — which adds quality
incidents as a third classification category alongside infrastructure and
application incidents — maps directly to Article 10. Specifically:

- Quality incidents (system available and responding but outputs failing the
  output quality SLO) are an ASDLC-specific classification with no DORA
  analogue; they must be explicitly mapped to DORA's incident severity taxonomy
  by the organisation, as output quality failures in financial services systems
  may constitute material ICT incidents under DORA's definition.
- The escalation path from on-call engineer to accountable human, and from
  accountable human to the organisation's ICT incident management process, is
  the Article 10 escalation path. It must be documented and exercised.

**DORA Article 11** requires that financial entities implement and regularly
test ICT business continuity plans. The ASDLC's operational DoD condition for DR
testing of Tier 3 systems — which requires that disaster recovery procedures are
tested, not merely documented — is the Article 11 business continuity control
for agent systems. DR testing frequency must satisfy DORA's requirements for the
system's criticality tier; the ASDLC's Tier 3 designation maps to DORA's
critical or important function classification for DR testing frequency purposes.

### SR 11-7 — Ongoing Monitoring

SR 11-7 requires ongoing monitoring of model performance throughout the model's
operational life. This is not a periodic review obligation — it is a continuous
production monitoring obligation. The ASDLC's output quality rate SLO and
reasoning trace completeness SLO, defined in
[operations/governance.md](../operations/governance.md), are the SR 11-7 ongoing
monitoring controls.

Specifically:

- The output quality rate SLO — the minimum acceptable percentage of production
  outputs meeting acceptance criteria when sampled — is the primary SR 11-7
  monitoring control. SR 11-7's backtesting, benchmarking, and outcomes analysis
  requirements are satisfied when this SLO is combined with a sampling
  methodology that covers the real production input distribution, not just the
  pre-deployment evaluation suite inputs.
- The reasoning trace completeness SLO — the minimum percentage of production
  decisions with complete, inspectable traces — enables the SR 11-7 requirement
  for documentation of model decisions. For model systems operating in financial
  decisions, a trace completeness SLO below 100% for material decisions is a
  potential SR 11-7 deficiency.
- The quarterly architectural health review in maintenance governance provides
  the periodic model review cadence that SR 11-7 expects. The review must
  explicitly assess whether the model's performance against the ongoing
  monitoring metrics remains within acceptable thresholds, and must document the
  assessment.

### EU AI Act Article 17 — Quality Management System

EU AI Act Article 17 requires that providers of high-risk AI systems implement a
quality management system that includes, among other requirements, post-market
monitoring of the system's performance in production. The ASDLC's operational
observability framework — specifically the output quality rate SLO and its
associated sampling methodology, the reasoning trace completeness SLO, and the
cost anomaly detection — constitutes the monitoring component of the Article 17
quality management system.

Article 17 further requires that the quality management system assigns
responsibilities for monitoring to specific personnel. The ASDLC's stewardship
model — in which a named system steward holds ongoing responsibility for
monitoring value realisation and performance — satisfies this requirement. The
steward is the Article 17 responsible individual for post-market monitoring. The
steward's accountability for ongoing performance monitoring must be documented
in the system's technical file as the QMS monitoring responsibility assignment.

### GDPR Article 17 and Retention — Decommission Protocol Conflict Resolution

GDPR Article 17 (right to erasure) and SR 11-7's seven-year model documentation
retention requirement create a direct conflict in the decommission protocol. SR
11-7 requires that model documentation — specifications, evidence bundles,
validation records — be retained for seven years after the model is retired.
GDPR Article 17 requires that personal data be erased on request, or deleted
when the purpose for which it was collected no longer applies.

The decommission protocol's conflict resolution approach distinguishes between
two categories of retained data:

**Specification and evidence bundle artefacts** are retained for seven years to
satisfy SR 11-7. These artefacts — versioned specifications, evaluation reports,
trace IDs, policy check outputs, and validation records — describe what the
model did and how it was governed. They typically do not contain personal data
from production operations; they contain descriptions of the model's behaviour
and governance. SR 11-7 retention applies without GDPR conflict for this
category.

**Production data artefacts** — reasoning traces from live production decisions,
input-output records from production inference, and any logs containing personal
data from financial services customers — are subject to GDPR-compliant retention
at decommission. This means: applying the organisation's data retention schedule
to production data, executing erasure requests on production data, and
confirming that no personal data from the decommissioned system persists beyond
the retention period. The decommission protocol must explicitly verify that
production data is in scope for GDPR retention and that erasure has been
completed.

This conflict was identified in the maintenance governance layer; the resolution
approach here operationalises it for the decommission execution.

### Layer 4 Regulatory Control Mapping

| Regulation | Article/Section    | Operational Requirement                                                                             | ASDLC Control                                                                                                                                               | Gap                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------- | ------------------ | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DORA       | Art. 9             | ICT vulnerability management on an ongoing basis                                                    | CVSS-tiered patch management SLOs in maintenance governance (CVSS ≥ 9.0: 24h; 7.0–8.9: 72h; 4.0–6.9: 30 days)                                               | DORA's RTS on TLPT and vulnerability management may impose specific reporting obligations for vulnerabilities above certain severity thresholds. The patch management SLOs address remediation timing; regulatory reporting of critical vulnerabilities requires a separate notification workflow.                                                                                                         |
| DORA       | Art. 10            | ICT incident detection, classification, and management process                                      | ASDLC incident classification (infrastructure, application, quality incidents); output quality rate SLO with alerting; escalation path to accountable human | Quality incident classification must be explicitly mapped to DORA's incident severity taxonomy (Art. 18 classification criteria). This mapping must be documented before the system goes to production to ensure DORA reporting timelines are met for material incidents.                                                                                                                                  |
| DORA       | Art. 11            | ICT business continuity plans tested regularly                                                      | DR testing for Tier 3 systems as part of operational DoD; rollback success rate SLO                                                                         | DORA specifies testing frequency for critical/important functions. DR testing schedule must be calibrated to DORA's required frequency for the system's classification; the ASDLC's operational DoD requires testing but does not prescribe a frequency that may satisfy DORA's requirements for all system tiers.                                                                                         |
| SR 11-7    | Ongoing monitoring | Continuous production monitoring of model performance; backtesting, benchmarking, outcomes analysis | Output quality rate SLO; reasoning trace completeness SLO; quarterly architectural health review                                                            | SR 11-7 backtesting and outcomes analysis require comparison against realised outcomes over time, not just sampling against acceptance criteria. The output quality SLO measures process quality; outcomes analysis measures whether agent decisions produced correct real-world results. This requires a separate outcomes tracking capability not explicitly defined in the operations governance layer. |
| EU AI Act  | Art. 17            | Quality management system including post-market monitoring; assigned monitoring responsibilities    | Output quality rate SLO; reasoning trace completeness SLO; stewardship model with named steward responsible for ongoing monitoring                          | Art. 17's QMS requirements extend to documentation, data governance, and feedback from monitoring into the risk management system (Art. 9). The operations layer's feedback from quality incidents and value misses into the demand layer (Layer 1) is the mechanism; its explicit connection to Art. 17 QMS documentation must be established.                                                            |
| GDPR       | Art. 17            | Right to erasure; personal data deleted when retention purpose expires                              | Decommission protocol distinguishing specification artefacts (SR 11-7 retention) from production data artefacts (GDPR retention)                            | The protocol requires explicit verification that production data is identified, scoped to GDPR, and erased at decommission. No automated tool in the ASDLC currently identifies personal data in production traces and applies retention schedules; this requires integration with the organisation's data governance tooling.                                                                             |
