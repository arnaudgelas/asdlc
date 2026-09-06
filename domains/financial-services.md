# ASDLC Domain Guidance — Financial Services

_Financial services-specific regulatory requirements for ASDLC Layers 1, 3,
and 4._

See
[Financial Services Manifesto Alignment](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/domains/financial-services.md)
for manifesto principle mappings (SR 11-7, DORA, EU AI Act, SOX, Three Lines of
Defense). See the [ASDLC Overview](../asdlc.md) for the full lifecycle
framework.

---

## ASDLC Layer 1 — Demand & Value Regulatory Requirements (Financial Services)

Layer 1 — the governed demand layer defined in
[demand/value.md](../demand/value.md) — is not merely a planning precursor to
engineering. In financial services, it is the point at which several regulatory
obligations first attach. Risk identification is a requirement of binding
instruments (EU AI Act Art. 9, DORA Art. 8). Conceptual soundness and business
need validation are **not**: they come from SR 11-7, which is supervisory
guidance written in "should" — see the note on SR 11-7's register below. The
specification readiness gate is the Layer 1 governance control that ensures
these are addressed before the engineering execution loop begins.

**Note on SR 11-7's register.** SR 11-7 is Federal Reserve *supervisory
guidance*, and it is written in "should". In the attachment held at
`inputs/20260905-arnaud/prep/D-20-primary/sources/sr1107a1.txt` (sha256
`d8ef343917…`, alongside `sr1107.pdf`) the word `should` occurs **180** times
against a single `must`; `requir*` occurs seven times and **none of the seven
places a requirement on a bank by force of this document** (they are the
advanced-approaches capital rules at 12 CFR, a bank requiring things of *its
vendors*, and a bank's own policies requiring documentation of themselves).
The successor guidance on model risk management, **SR 26-2** (17 April 2026),
states that it *"does not set forth enforceable standards or prescriptive
requirements; accordingly, non-compliance with this guidance will not result in
supervisory criticism against a banking organization"* — the sentence quoted to
its end, and it carries footnote 1: *"See 12 CFR Part 4, Subpart F,
Appendix A (OCC); 12 CFR Part 262,
Appendix A (Board); 12 CFR Part 302, Appendix A (FDIC). However, supervisory
action may result for any violations of law or unsafe or unsound practices
stemming from insufficient management of model risk."*
**That completion supports the register point rather than reversing it, and it
bounds it in the same breath**: neither instrument places a requirement on a
bank by force of the document, *and* non-enforceable is not consequence-free —
supervisory action routes through violations of law and unsafe-or-unsound
practices instead of through the guidance. Each SR 11-7 mapping below
therefore states what the guidance
says a bank **should** do, quoted, or marks itself as the ASDLC's own
construction. None of it is a compliance determination.

### SR 11-7 (Model Risk Management) — Conceptual Soundness at the Demand Stage

SR 11-7 says, in "should" form, that an effective validation framework
*"should include three core elements: • Evaluation of conceptual soundness,
including developmental evidence • Ongoing monitoring, including process
verification and benchmarking • Outcomes analysis, including back-testing"*;
that *"Comparison to alternative theories and approaches should be included"*;
that *"Key assumptions and the choice of variables should be assessed, with
analysis of their impact on model outputs and particular focus on any potential
limitations"*; and that *"Documentation of model development and validation
should be sufficiently detailed so that parties unfamiliar with a model can
understand how the model operates, its limitations, and its key assumptions."*
That is the whole of what the guidance asks for here, and it asks for it as
sound practice, not as a requirement.

The **sequencing** — that conceptual soundness is documented *before*
engineering execution begins rather than assembled afterwards — is **the
ASDLC's own construction**; SR 11-7 sets no such ordering. A team that begins
engineering execution without documenting conceptual soundness has inverted the
ASDLC's governance sequence, and has left itself without the developmental
evidence the guidance says a validation framework should evaluate.

The demand layer's specification readiness gate condition "business need
validated" maps to what SR 11-7 says conceptual-soundness evaluation should
cover. Before the gate can be passed, the business demand sponsor must have
documented why this approach is appropriate for the problem — the evidence that
makes "business need validated" true is the same evidence that makes
"conceptually sound" defensible in the guidance's own terms. The gate condition
"acceptance criteria expressible" confirms that the model's intended function is
specified precisely enough to be verified — a prerequisite for the validation
planning SR 11-7 describes.

**"Fit-for-purpose" is the ASDLC's phrase, not the guidance's**: `fit-for-purpose`
and `fit for purpose` each occur **zero** times in SR 11-7 and its attachment as
held on disk. The ASDLC's position — its own, unsourced — is that validation for
fitness of purpose begins at the demand stage. If a model's purpose is not
clearly defined at Layer 1, the Layer 2 engineering loop will produce an artefact
that cannot be validated for fitness of purpose, because no purpose was ever
governed.

### EU AI Act Article 9 — Risk Management System from Conception

EU AI Act Article 9 requires that high-risk AI systems are subject to a
documented risk management process throughout the system lifecycle. Article 9(2)
requires that process to be "planned and run throughout the entire lifecycle of a
high-risk AI system" — an entire lifecycle that begins at conception, before the
engineering loop starts. A risk management system that is initiated at the start
of engineering execution is already late.

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

### DORA Article 8(3) — ICT Risk Management Framework and Pre-Change Risk

Identification

[citation corrected 2026-09-05: this section previously cited "DORA Article 5"
for the pre-change risk-identification obligation below. Article 5 is
*Governance and organisation* — management-body duties to approve, oversee and
resource the ICT risk management framework — and contains no risk-identification
obligation. The obligation described below is DORA Article 8(3), which
requires a risk assessment upon each major change affecting the entity's
ICT-supported business functions (cited unquoted; not independently verified
verbatim by this pass). Corrected to Article 8(3); see
`inputs/20260905-arnaud/prep/asdlc-standards/`.]

DORA Article 8(3) requires that financial entities identify and classify ICT
risks before implementing changes to ICT systems. The demand layer is the
governance point at which this identification occurs. An organisation that
identifies ICT risks only after engineering execution has begun has not
satisfied Article 8(3)'s timing requirement.

The demand layer's validation of business need — including the validation tier
calibrated to blast radius — and the assessment of constraints and blast radius
at the specification readiness gate are the governance controls that implement
DORA Article 8(3) risk identification and classification at the point where it
is required: before the change begins. The classification determines which
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
| SR 11-7 | Evaluation of conceptual soundness "including developmental evidence" is one of three core elements a validation framework "should include". Documenting it *before* development begins, and the phrase "fit-for-purpose", are the ASDLC's own construction — see the note on SR 11-7's register at the top of this file. | Specification readiness gate: "business need validated" and "acceptance criteria expressible" conditions; business demand sponsor sign-off | SR 11-7 says *"Comparison to alternative theories and approaches should be included"* and that key assumptions should be assessed "with … particular focus on any potential limitations" — in "should" form, not as a requirement. The demand layer governs that a need is validated, not that all model alternatives are enumerated. The specification analyst role must explicitly prompt for alternatives documentation for model-class items.                                                         |
| EU AI Act Art. 9            | Risk management system covers the full lifecycle from conception; known and foreseeable risks identified before engineering begins | Specification readiness gate: "blast radius assessed" and "constraints identified" conditions; validation tier scaled to blast radius      | Art. 9's requirement for a continuous iterative risk management process means Layer 1 risk identification must feed back from Layer 4 operational data. Feedback protocol in [demand/value.md](../demand/value.md) provides this loop, but the connection between operational incident data and demand-layer risk assessment must be explicitly established. |
| DORA Art. 8(3)              | ICT risks identified and classified before changes are implemented                                                                 | Demand backlog entry validation; blast radius assessment at specification readiness gate; change classification by tier                    | DORA expects ICT risk classification to connect to the change management process in Layer 3. The Layer 1 classification must flow through to the Layer 3 change record. No explicit hand-off mechanism defined between the demand layer's classification and the Layer 3 compliance documentation condition.                                                 |
| MiFID II Art. 17            | Algorithmic system changes conceptually sound and documented; pre-trade controls in place                                          | Demand backlog with evidence-backed validation; business demand sponsor accountability for the business case                               | MiFID II's pre-trade controls are Layer 2 and Layer 3 concerns; the demand layer governs that the change is conceptually justified. Gap: explicit call-out for algorithmic trading system changes as a category requiring heightened demand-layer validation is not built into the standard gate.                                                            |
| Solvency II internal models | Model changes documented before execution; methodology rationale preserved                                                         | Value definition requirement in the demand layer; business demand sponsor sign-off on the success criterion                                | Solvency II requires model documentation in the format prescribed by the applicable supervisory authority. The demand layer produces a business value statement; it does not produce Solvency II model documentation format. Translation into the required format must occur at Layer 2.                                                                     |

---

## ASDLC Layer 3 — Release & Deployment Regulatory Requirements (Financial

Services)

Layer 3 — release and deployment governance as defined in
[release-governance.md](../release-governance.md) — is the primary compliance
boundary for financial services change management regulation. The eight release
gate conditions are not general good practice layered on top of regulatory
requirements; for several financial services regulations, they are the direct
implementation of specific legal obligations. This section maps those
obligations to the release gate and release Definition of Done in detail.

### DORA Article 9(4)(e) — ICT Change Management

[citation corrected 2026-09-05: this section previously cited "DORA Article
14" and three lettered sub-points of a paragraph 2, for the change-management
obligation below. That citation was withdrawn because Article 14 is
*Communication* — crisis-communication plans (¶1), communication policies for
internal staff and external stakeholders (¶2), and a named media contact (¶3)
— and carries no change-management provision; ¶2 exists but has no lettered
sub-paragraphs, so `(a)`–`(c)` do not exist. The obligation is now correctly
cited at DORA Article 9(4)(e), verified verbatim against the primary
(EUR-Lex, Regulation (EU) 2022/2554): financial entities shall "implement
documented policies, procedures and controls for ICT change management,
including changes to software, hardware, firmware components, systems or
security parameters, that are based on a risk assessment approach and are an
integral part of the financial entity’s overall change management process, in
order to ensure that all changes to ICT systems are recorded, tested,
assessed, approved, implemented and verified in a controlled manner".
Corrected further 2026-09-05: the paragraph below previously asserted a
documented rollback procedure, post-implementation review and independent
testing before production deployment for critical or important functions as
Article 9(4)(e) requirements, none of which the quotation above contains.
Against the hashed primary
(`inputs/20260905-arnaud/prep/asdlc-standards/sources/dora_fulltext.txt`,
sha256 `25328c7e…3b4d1e`) the search terms `rollback`, `post-implementation`
and `independent testing` each occur zero times, with live one-word-swap
negative controls, and `change management` occurs only in Article 9(4)(e) and
its closing subparagraph, so no other DORA provision carries them. No claim was deleted;
each is now marked in the sentence that carries it. See
`inputs/20260905-arnaud/prep/asdlc-standards/` for the verification packet.]

DORA Article 9(4)(e) requires that financial entities implement documented
policies, procedures and controls for ICT change management ensuring that all
changes to ICT systems are "recorded, tested, assessed, approved, implemented
and verified in a controlled manner", which carries pre-implementation testing
of changes. The ASDLC additionally requires a documented rollback procedure
and post-implementation review — neither of which this file sources to DORA,
because the words `rollback` and `post-implementation` each occur zero times in
the Regulation; both are ASDLC controls and must not be presented to a supervisor
as DORA requirements. Independent testing of changes before production
deployment for systems supporting critical or important functions is likewise
not sourced here to any DORA provision and must not be relied on as one; what
the Regulation states is Article 24(4), that a financial entity shall ensure
that tests "are undertaken by independent parties, whether internal or
external", and Article 24(6), that appropriate tests are conducted at least
yearly on all ICT systems and applications supporting critical or important
functions — a programme-level, periodic testing duty rather than a per-change
release condition.

The ASDLC release gate directly implements a process of this kind. The mapping
is specific — and, per the paragraph above, only the first bullet maps an
Article 9(4)(e) obligation; the other three map ASDLC controls that this file
does not source to DORA:

- Changes are tested before implementation: satisfied by
  release gate Condition 1 (evidence bundle complete, including evaluation
  reports from the engineering loop) and Condition 2 (independent validation
  passed for high-stakes systems).
- A documented rollback procedure: satisfied by release gate
  Condition 3 (rollback procedure tested, with a tested time-to-rollback on
  record).
- Post-implementation review: satisfied by the release
  Definition of Done condition requiring smoke tests in production, plus the
  operational readiness gate initiation that hands off to Layer 4 monitoring.
- Independent testing for critical/important functions: satisfied by
  release gate Condition 2 (independent validation passed), which is mandatory
  for high-stakes regulated systems regardless of phase.

For systems in DORA scope, the release gate is not optional — it implements a
documented ICT change management process of the kind DORA requires. An
organisation that has implemented the release gate and maintains the evidence
it produces has an auditable change-management compliance record. The
evidence bundle ID referenced in the change record is that change management
test documentation.

### SR 11-7 — Model Change Documentation at the Release Boundary

What SR 11-7 says about model change is said in "should": *"Material changes in
model structure or technique, and all model redevelopment, should be subject to
validation activities of appropriate range and rigor before implementation"*,
*"Material changes to models should also be subject to validation"*, and
*"Computer code implementing the model should be subject to rigorous quality and
change control procedures to ensure that the code is correct, that it cannot be
altered except by approved parties, and that all changes are logged and can be
audited."* **The three-part document — nature of the change, testing performed,
validation results — is the ASDLC's own construction and is unsourced**: the
phrases `nature of the change` and `testing performed` each occur **zero** times
in SR 11-7 and its attachment as held on disk. At the release boundary, the
evidence bundle produced by the engineering execution loop is the ASDLC's model
change document, and the release gate's Condition 1 (evidence bundle complete)
is the control that produces it.

The ASDLC's model change documentation — its own construction, not SR 11-7's —
comprises:

- The nature of the change: satisfied by the diff in the evidence bundle and the
  specification reference in the change record.
- Testing performed: satisfied by the evaluation reports in the evidence bundle,
  including the test suite, pass/fail results, and evaluation metrics.
- Validation results: for material changes to high-risk models, satisfied by
  Condition 2 (independent validation passed), which records the named
  independent validator, date, scope, and finding.

The release gate's "compliance documentation complete" condition (Condition 5)
is the ASDLC's model change record — it must reference the evidence bundle and
confirm that the change is filed in the model inventory before release proceeds.
Filing at the release boundary is the ASDLC's choice of moment; what SR 11-7
says is that banks *"should maintain a comprehensive set of information for
models implemented for use, under development for implementation, or recently
retired"*, and that the inventory *"should also indicate whether models are
functioning properly, provide a description of when they were last updated, and
list any exceptions to policy."*

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
| DORA                    | Art. 9(4)(e) ¹              | Pre-implementation testing documented                                                               | Evidence bundle complete (Condition 1): evaluation reports with pass/fail results                                                      | DORA requires specific retention of test documentation. Evidence bundle ID in change record provides the reference; retention period and format must be confirmed.                    |
| DORA                    | Art. 9(4)(e) ¹              | Rollback procedure documented and verified                                                          | Rollback procedure tested (Condition 3): tested within 48 hours of deployment, time-to-rollback on record                              | Art. 9(4)(e) requires changes to be "recorded, tested, assessed, approved, implemented and verified in a controlled manner" — it does not itself impose a rollback-specific requirement; see ¹. The ASDLC's tested rollback condition is retained here as a control regardless of that gap.                                                                                         |
| DORA                    | Art. 9(4)(e) ¹              | Independent testing of changes before production for critical/important functions — an ASDLC control, not sourced to DORA; the search term `independent testing` occurs zero times in the Regulation, and Art. 9(4)(e) draws no critical/important distinction. See ¹ | Independent validation passed (Condition 2): named independent validator, scope, pass/fail                                             | The requirement in the Release Requirement cell is not sourced to any DORA provision and must not be relied on as one. What DORA states is Art. 24(4) — tests "undertaken by independent parties, whether internal or external" — and Art. 24(6) — appropriate tests at least yearly on all ICT systems and applications supporting critical or important functions: a programme-level, periodic duty, not a per-change gate. Whether a Level-2 RTS defines "independent" for this purpose has not been checked; no delegated act was retrieved.                         |
| SR 11-7                 | Model change governance    | *"Material changes in model structure or technique, and all model redevelopment, should be subject to validation activities of appropriate range and rigor before implementation."* The three-part record (nature of change, testing performed, validation results) is the ASDLC's own construction — see the note on SR 11-7's register at the top of this file. | Evidence bundle complete (Condition 1): diff, evaluation reports, trace IDs; independent validation (Condition 2) for material changes | SR 11-7 says the model inventory *"should … provide a description of when they were last updated"*; updating it *at the release boundary* is the ASDLC's placement, not the guidance's. The change record's compliance documentation condition (Condition 5) should include model inventory update confirmation; this linkage is not explicit in the current release gate design.                                       |
| FCA PS21/3 / PRA PS6/21 | Operational resilience     | Recovery within impact tolerances for important business services; rollback capability demonstrated | Rollback procedure tested (Condition 3) with time-to-rollback within impact tolerance window; monitoring configured (release DoD)      | Impact tolerances are firm-specific and must be pre-defined. The release gate's rollback test does not automatically check whether the time-to-rollback satisfies the firm's impact tolerance for the specific important business service. This calibration step must be performed explicitly. |
| EU AI Act               | Art. 15                    | High-risk AI systems meet accuracy and robustness requirements at and after deployment              | Independent validation (Condition 2); post-deployment smoke tests (release DoD); monitoring and alerting configured (release DoD)      | Art. 15's cybersecurity requirements extend beyond functional testing. The release gate does not include a pre-release cybersecurity assessment specific to AI attack vectors (adversarial inputs, model inversion). This must be addressed in the evaluation suite design at Layer 2.         |

¹ [citation corrected 2026-09-05: the three DORA rows above previously cited
two lettered sub-points of a paragraph 2, plus "Art. 14 critical functions,"
and the second row quoted DORA as requiring documented rollback procedures.
That citation was withdrawn because DORA Article 14 is *Communication* —
crisis-communication plans (¶1), staff and stakeholder communication policies
(¶2), and a named media contact (¶3) — and carries no change-management
provision; ¶2 has no lettered sub-paragraphs, so `(a)`–`(c)` do not exist; and
the phrase "documented rollback procedures" occurs zero times in the
Regulation. The rows above are now correctly cited at DORA Article 9(4)(e),
verified verbatim against the primary (EUR-Lex, Regulation (EU) 2022/2554) —
see the section heading above for the full quotation. Art. 9(4)(e) does not
itself use the word `rollback`, nor `post-implementation` nor `independent
testing` — all three search terms occur zero times in the Regulation, with live
one-word-swap negative controls, and `change management` occurs only in
Art. 9(4)(e) and its closing subparagraph, so no other DORA provision carries them; each of the three
rows above now marks its own unsourced content in the row itself rather than
relying on this footnote. The rollback-specific gap noted in the second
row remains open. See `inputs/20260905-arnaud/prep/asdlc-standards/` for the
verification packet.]

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

[citation corrected 2026-09-05: this paragraph previously attributed
impact-classification of ICT-related incidents to "DORA Article 10." Article
10 is *Detection* — anomaly-detection mechanisms and alert thresholds; it
does not contain classification-by-impact language. Classification of
ICT-related incidents by impact is DORA Article 18, *Classification of
ICT-related incidents and cyber threats* (six criteria: clients affected,
duration, geographic spread, data loss, criticality, economic impact). See
`inputs/20260905-arnaud/prep/asdlc-standards/` for the verification packet.]

**DORA Article 10** requires that financial entities detect ICT-related
incidents and manage them through a defined incident management process.
**DORA Article 18** requires that detected incidents be classified by their
impact. The ASDLC's incident classification framework from
[operations/governance.md](../operations/governance.md) — which adds quality
incidents as a third classification category alongside infrastructure and
application incidents — maps directly to Articles 10 and 18. Specifically:

- Quality incidents (system available and responding but outputs failing the
  output quality SLO) are an ASDLC-specific classification with no DORA
  analogue; they must be explicitly mapped to DORA Article 18's classification
  criteria by the organisation, as output quality failures in financial
  services systems may constitute material ICT incidents under DORA's
  definition.
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

SR 11-7 names ongoing monitoring as one of the three core elements a validation
framework *"should include"*, and says *"Validation activities should continue
on an ongoing basis after a model goes into use, to track known model
limitations and to identify any new ones"* and *"Outcomes analysis should be
conducted on an ongoing basis"*. It does not say *continuous*: the word
`continuous` occurs **zero** times in the guidance and its attachment as held on
disk. **Reading "ongoing" as continuous production monitoring rather than
periodic review is the ASDLC's own construction.** The ASDLC's output quality
rate SLO and reasoning trace completeness SLO, defined in
[operations/governance.md](../operations/governance.md), are the ASDLC's
controls for it.

Specifically:

- The output quality rate SLO — the minimum acceptable percentage of production
  outputs meeting acceptance criteria when sampled — is the ASDLC's primary
  monitoring control. SR 11-7 lists benchmarking (under ongoing monitoring) and
  back-testing (under outcomes analysis) among the elements a validation
  framework should include; **whether this SLO satisfies them is the ASDLC's
  judgement, not the guidance's**, and it holds only when the SLO is combined
  with a sampling methodology that covers the real production input
  distribution, not just the pre-deployment evaluation suite inputs.
- The reasoning trace completeness SLO — the minimum percentage of production
  decisions with complete, inspectable traces — serves what SR 11-7 says
  documentation should achieve: that it be *"sufficiently detailed so that
  parties unfamiliar with a model can understand how the model operates, its
  limitations, and its key assumptions."* For model systems operating in
  financial decisions, the ASDLC treats a trace completeness SLO below 100% for
  material decisions as a deficiency **against this framework**; SR 11-7 sets no
  such threshold.
- The quarterly architectural health review in maintenance governance provides
  the periodic model review cadence. SR 11-7 says banks *"should conduct a
  periodic review—at least annually but more frequently if warranted—of each
  model to determine whether it is working as intended and if the existing
  validation activities are sufficient"*; `quarterly` occurs zero times in the
  guidance, so the quarterly cadence is the ASDLC's choice and exceeds the
  annual floor the guidance describes. The review must
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

GDPR Article 17 (right to erasure) and the organisation's seven-year model
documentation retention policy create a direct conflict in the decommission
protocol. Model documentation — specifications, evidence bundles, validation
records — is retained for a policy-set seven years after the model is
retired, with no instrument setting that period. SR 11-7 is supervisory
guidance written in "should" and states no retention period: the words
`retention` and `seven years` each occur zero times in the guidance and its
attachment as held at
`inputs/20260905-arnaud/prep/D-20-primary/sources/sr1107a1.txt` (sha256
`d8ef343917…`). The seven years are this organisation's own choice. GDPR
Article 17 requires that personal data be erased on request, or deleted when
the purpose for which it was collected no longer applies.

The decommission protocol's conflict resolution approach distinguishes between
two categories of retained data:

**Specification and evidence bundle artefacts** are retained for the policy-set
seven years. These artefacts — versioned specifications, evaluation reports,
trace IDs, policy check outputs, and validation records — describe what the
model did and how it was governed. They typically do not contain personal data
from production operations; they contain descriptions of the model's behaviour
and governance. The retention policy applies without GDPR conflict for this
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
| DORA       | Arts. 10, 18       | ICT incident detection (Art. 10), classification by impact (Art. 18), and management process         | ASDLC incident classification (infrastructure, application, quality incidents); output quality rate SLO with alerting; escalation path to accountable human | Quality incident classification must be explicitly mapped to DORA Article 18's classification criteria. This mapping must be documented before the system goes to production to ensure the reporting time limits are met for major ICT-related incidents. DORA itself fixes none: Art. 19(4) requires the initial notification, intermediate report and final report "within the time limits to be laid down in accordance with Article 20, first paragraph, point (a), point (ii)", so **the period is set by the RTS under Art. 20, first paragraph, point (a)(ii) — record the version relied on**. Cite that RTS, not an Article 19 deadline. *(Corrected 2026-09-06: this cell previously required *DORA reporting timelines* to be met, which implies a clock the Regulation does not carry — `4 hours` 0, `four hours` 0, `72 hours` 0, `1 month` 0 on the normalised DORA primary, sha256 prefix `25328c7e39c4`, against positive controls `time limits` 3 and `exit strategies` 5. Converged with the wording already carried by AEM `operational-templates/slo-table.md` rows 18-20 and `aplc/aplc-guide.md`; see `errata.md` (D-57).)*                                                                                                                                  |
| DORA       | Art. 11            | ICT business continuity plans tested regularly                                                      | DR testing for Tier 3 systems as part of operational DoD; rollback success rate SLO                                                                         | DORA specifies testing frequency for critical/important functions. DR testing schedule must be calibrated to DORA's required frequency for the system's classification; the ASDLC's operational DoD requires testing but does not prescribe a frequency that may satisfy DORA's requirements for all system tiers.                                                                                         |
| SR 11-7    | Ongoing monitoring | *"Validation activities should continue on an ongoing basis after a model goes into use"*; ongoing monitoring "including process verification and benchmarking" and outcomes analysis "including back-testing" are two of the three core elements a validation framework "should include". Reading this as **continuous** production monitoring is the ASDLC's own construction — see the note on SR 11-7's register at the top of this file. | Output quality rate SLO; reasoning trace completeness SLO; quarterly architectural health review                                                            | Back-testing as SR 11-7 describes it is *"the comparison of actual outcomes with model forecasts"* over a sample period, so it needs comparison against realised outcomes over time, not just sampling against acceptance criteria. The output quality SLO measures process quality; outcomes analysis measures whether agent decisions produced correct real-world results. This requires a separate outcomes tracking capability not explicitly defined in the operations governance layer. |
| EU AI Act  | Art. 17            | Quality management system including post-market monitoring; assigned monitoring responsibilities    | Output quality rate SLO; reasoning trace completeness SLO; stewardship model with named steward responsible for ongoing monitoring                          | Art. 17's QMS requirements extend to documentation, data governance, and feedback from monitoring into the risk management system (Art. 9). The operations layer's feedback from quality incidents and value misses into the demand layer (Layer 1) is the mechanism; its explicit connection to Art. 17 QMS documentation must be established.                                                            |
| GDPR       | Art. 17            | Right to erasure; personal data deleted when retention purpose expires                              | Decommission protocol distinguishing specification artefacts (policy-set seven-year retention) from production data artefacts (GDPR retention)                            | The protocol requires explicit verification that production data is identified, scoped to GDPR, and erased at decommission. No automated tool in the ASDLC currently identifies personal data in production traces and applies retention schedules; this requires integration with the organisation's data governance tooling.                                                                             |
