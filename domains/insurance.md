# ASDLC Domain Guidance — Insurance

_Insurance-specific regulatory requirements for ASDLC Layers 1, 3, and 4._

See [Insurance Manifesto Alignment](../../domains/insurance.md) for manifesto
principle mappings. See the [ASDLC Overview](../asdlc.md) for the full
lifecycle framework. See
[governance/gate-registry.md](../governance/gate-registry.md) for the
canonical gate condition enumeration referenced throughout this file. See
[eu-ai-act-mapping.md](../eu-ai-act-mapping.md) for the cross-cutting EU AI
Act risk-tier mapping that this domain file's EU AI Act references should be
read alongside.

> **Conformance profile expectation.** Organisations operating in this
> regulated context typically claim the ASDLC-Regulated conformance profile
> (see [conformance-profiles.md](../conformance-profiles.md)).
>
> **Scope of regulatory claims.** This file maps ASDLC controls to insurance
> regulatory obligations. Throughout, "supports compliance with",
> "operationalises", and "produces evidence aligned with" are used in
> preference to "is" or "satisfies" because ASDLC alone is rarely sufficient
> to discharge a regulatory requirement; ASDLC artefacts contribute to a
> compliance posture that the organisation must complete with regulatory
> counsel, supervisory engagement, and additional artefacts (Solvency II
> internal model documentation in supervisory format, ORSA filings,
> actuarial validation reports, IDD POG records, and the like). Specific
> limits — including the well-known format-mismatch gap for Solvency II
> Article 115 documentation — are flagged in each section.

---

## ASDLC Layer 1 — Demand & Value Regulatory Requirements (Insurance)

Layer 1 — the governed demand layer defined in
[demand/value.md](../demand/value.md) — is the point at which several
insurance regulatory obligations first attach. For Solvency II internal models,
IDD suitability systems, and EIOPA AI guidelines compliance, the demand layer is
the earliest governance control — and failures here propagate through every
subsequent stage.

### Solvency II — Internal Model Documentation Requirements Begin at Model

Conception

Solvency II Article 115 requires that internal model documentation is
sufficient to demonstrate that the model meets the tests and standards, and
that the documentation enables the supervisory authority to assess
compliance. This documentation obligation begins at model conception — before
engineering begins. An undertaking that starts internal model development
without governing the model's purpose, methodology rationale, and intended
use at the demand stage will produce an artefact that does not support a
Solvency II documentation defence, because the conception decisions were
never recorded. ASDLC alone does not produce supervisory-format internal
model documentation; the format prescribed by the applicable supervisory
authority is an additional artefact that must be produced alongside ASDLC.
The demand-layer evidence is an input to that artefact, not a substitute
for it.

The Specification Readiness Gate conditions SR-1 (Business Need Validated)
and SR-3 (Acceptance Criteria Expressible) — see
[governance/gate-registry.md](../governance/gate-registry.md) — support
compliance with Article 115 by ensuring that the conceptual soundness and
intended purpose of the model are documented before development starts. The
business demand sponsor sign-off is, in the Solvency II context, the Chief
Actuary or Chief Risk Officer confirmation that this model is appropriate
for its intended use — the Solvency II use test requires that the model is
used in and influences the undertaking's decision-making, and the demand
layer's governance produces the first evidence of that use intent.

The Specification Readiness Gate condition SR-6 (Blast Radius Assessed) must,
for Solvency II models, explicitly identify whether the model is material to
the SCR calculation. A model that contributes to SCR calculation is in scope
for the full internal model approval process, and the blast radius assessment
triggers the IMAP governance path. Discovering that a model is SCR-material
after the engineering execution loop has started means the IMAP governance
documentation trail is already incomplete.

### IDD — Suitability Assessment Process Validated Before System Development

The IDD requires that insurance distributors carry out a suitability assessment
appropriate to the complexity and risk of the product and calibrated to the
customer's demands and needs. For an agent product that performs this function,
the suitability assessment methodology must be validated against regulatory
requirements and actuarial standards before system development begins — not
derived from the system's outputs after it is built.

The demand layer's business need validation must include, for IDD-scope agent
products: confirmation that the proposed suitability assessment approach
supports compliance with IDD expectations in the target jurisdictions;
confirmation that the demands and needs statement format aligns with the IDD
disclosure expectations; and identification of any Member State-specific
suitability requirements (such as FCA ICOBS enhanced suitability requirements
for particular product types) that must be incorporated into the behavioral
specification.

A demand item for an IDD advisory agent that has not addressed suitability
methodology validation before the Specification Readiness Gate is not ready
for loop entry: the behavioral specification cannot be written without
knowing what the suitability assessment must produce.

### EIOPA AI Guidelines — Risk Assessment Before Deployment

EIOPA's guidelines require that insurance undertakings conduct a risk
assessment of AI systems before deployment. This is a pre-deployment
obligation, but the substantive risk assessment must be conducted well
before deployment — ideally at Layer 1 (Demand). An undertaking that
conducts its EIOPA risk assessment only immediately before deployment will
discover design and governance issues that cannot be addressed at that
point.

The Specification Readiness Gate condition SR-4 (Constraints Identified)
supports compliance with the EIOPA pre-deployment risk assessment
expectation at Layer 1. For insurance AI agent products, the constraints
identified must include: the EIOPA AI guidelines risk classification for the
specific use case; the applicable conduct obligations (IDD, FCA Consumer
Duty) that constrain the agent's behavioral envelope; and the Solvency II
model governance tier applicable to the use case. A Specification Readiness
Gate that does not address these constraints for insurance agent products
is an incomplete gate.

### Layer 1 Regulatory Control Mapping

| Regulation           | Layer 1 Requirement                                                                                                                                       | ASDLC Control                                                                                                                                                                          | Gap                                                                                                                                                                                                                                                                                                        |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Solvency II Art. 115 | Internal model documentation begins at conception; use test requires documented decision-making role                                                      | Business need validated with actuarial rationale; "accountable human named" gate condition identifying actuarial sign-off responsibility; blast radius assessment triggering IMAP path | The demand layer documents the conceptual foundation; the Solvency II model documentation format requirements (as prescribed by the applicable supervisory authority) must be addressed in a translation step before the loop's artefacts are submitted as model documentation.                            |
| IDD Art. 20          | Suitability assessment methodology defined and validated before system development; demands and needs statement format confirmed for target jurisdictions | Business need validated including suitability methodology assessment; constraints identified including Member State-specific suitability requirements                                  | IDD suitability requirements vary by jurisdiction and product type. The demand layer's constraint identification must be supported by regulatory counsel in each target jurisdiction; a generic suitability assessment approach that works in one jurisdiction may not satisfy requirements in others.     |
| EIOPA AI Guidelines  | Risk assessment before deployment; AI use registered in the undertaking's risk framework                                                                  | Blast radius assessed; constraints identified including EIOPA risk classification; specification readiness gate governs pre-loop risk identification                                   | EIOPA expects the AI risk assessment to be part of the ORSA process. The demand layer's blast radius assessment must be filed into the risk management framework, not only into the APLC documentation. The connection between the demand gate record and the ORSA process must be established explicitly. |
| GDPR Art. 35         | DPIA required before processing that is likely to result in high risk (including large-scale processing of special category data)                         | Constraints identified including DPIA requirement where health/genetic data is in scope; blast radius assessment triggers DPIA flag for special category data processing               | GDPR Art. 35 DPIAs require involvement of the Data Protection Officer and, in some cases, prior consultation with the supervisory authority. The demand layer must flag the DPIA requirement; the DPIA itself is a parallel process that must complete before Stage 4 can proceed.                         |

---

## ASDLC Layer 3 — Release & Deployment Regulatory Requirements (Insurance)

Layer 3 — release and deployment governance as defined in
[release-governance.md](../release-governance.md) — is where Solvency II
model change governance and IDD product governance requirements impose
specific pre-deployment obligations. The Release Gate has eight conditions
(canonical enumeration in
[governance/gate-registry.md](../governance/gate-registry.md)); these
conditions are necessary but not sufficient for Solvency II models, since
major model changes require supervisory pre-approval that is not part of the
standard Release Gate.

### Solvency II Model Change Policy — Major vs. Minor Change Governance

Solvency II Article 115(3) requires internal model undertakings to have a
policy on model changes that governs what constitutes a major change
(requiring supervisory approval) and what constitutes a minor change
(governed by internal procedures). The Release Gate condition RG-5
(Compliance Documentation Complete) must confirm the model change
classification for every release to a Solvency II internal model: major or
minor, and the governance path followed.

For major model changes: the supervisory pre-approval is an organisation-
level prerequisite that must be obtained before the Release Gate is
assessed. A release that proceeds to the Release Gate without supervisory
pre-approval for a major change does not produce evidence aligned with the
Solvency II change policy regardless of the technical quality of the
change. The Release Gate must include a compliance documentation element
referencing supervisory approval and date.

For minor model changes: the internal governance documented in the change
record — the evidence bundle, the independent validation result, and the
accountable actuary's sign-off — supports compliance with the Solvency II
minor change governance expectation. RG-4 (Accountable Human Sign-Off) for
Solvency II minor model changes must be the Chief Actuary or a person with
delegated authority from the actuarial function, not a technology lead.

### IDD Product Oversight and Governance (POG) Requirements for Distribution

Changes

IDD Article 25 and EIOPA guidelines on product oversight and governance require
insurance manufacturers to ensure that products are designed for a specific
target market and that distribution channels are appropriate for that market.
Changes to agent products used in distribution — configuration changes that
affect the products offered, the suitability assessment logic, or the customer
segments served — are POG-relevant changes that must go through the product
governance process before deployment.

RG-5 (Compliance Documentation Complete) must confirm POG sign-off for
distribution agent product changes. POG sign-off is distinct from the
actuarial or technology sign-off: it is a Product Owner or Distribution
Governance confirmation that the change has been assessed against the
target market definition and that the revised agent product remains
appropriate for the intended target market.

For IDD-scope changes, the Release Gate must also confirm that the updated
demands and needs statement, if any, has been reviewed and approved and
that the customer-facing disclosure materials reflect the change. A
distribution agent product change that goes to production without updated
IDD disclosures is a conduct risk that the Release Gate must catch.

### Layer 3 Regulatory Control Mapping

| Regulation  | Article/Section                | Release Requirement                                                                             | ASDLC Control                                                                                                                                                         | Gap                                                                                                                                                                                                                                                                                                  |
| ----------- | ------------------------------ | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Solvency II | Art. 115(3)                    | Major model changes require supervisory pre-approval; minor changes governed by internal policy | RG-5 (Compliance Documentation Complete): model change classification; supervisory approval reference for major changes; actuarial sign-off for minor changes | Major model change classification is a judgment call that requires actuarial and legal input. ASDLC supports compliance with the documentation expectation; the classification itself is an organisation-level decision that must be confirmed before the gate is assessed.                                                                 |
| Solvency II | Art. 115                       | Model documentation updated to reflect changes before deployment                                | RG-1 (Evidence Bundle Complete): change description in evidence bundle; composite state manifest reflecting updated configuration                              | ASDLC alone does not produce supervisory-format model documentation. Model documentation update for Solvency II purposes must align with the supervisory authority's format expectations — not only describing what changed but demonstrating that the updated model still meets all six Solvency II tests. This requires a model validation update concurrent with the release, produced alongside ASDLC. |
| IDD         | Art. 25 / EIOPA POG guidelines | Distribution changes assessed against target market; POG sign-off before deployment             | RG-5 (Compliance Documentation Complete): POG sign-off confirmation; updated disclosure materials confirmed                                                   | POG sign-off involves the distribution governance function, which may not be part of the standard Release Gate stakeholder set. Ensuring POG sign-off is part of the Release Gate requires explicit inclusion in the compliance documentation checklist for IDD-scope agent products.                |
| DORA        | Art. 14                        | Changes tested before implementation; rollback procedures documented                            | RG-1 (Evidence Bundle Complete); RG-3 (Rollback Procedure Tested)                                                                                       | DORA applies to insurance undertakings. ASDLC supports compliance with DORA Art. 14 to the same extent as described in the financial services domain file; testing-before-implementation extends across functional, non-functional, integration, and (where applicable) cybersecurity dimensions and is not satisfied by rollback testing alone.                                                                                                                                                     |

---

## ASDLC Layer 4 — Operations & Maintenance Regulatory Requirements (Insurance)

Layer 4 — operational governance as defined in
[operations/governance.md](../operations/governance.md) — is where the
long-term Solvency II model monitoring, EIOPA AI guidelines performance
monitoring, and IDD product monitoring obligations attach. These are ongoing
obligations that persist throughout the agent product's operational life.

### Solvency II — Ongoing Model Monitoring and Validation Requirements

Solvency II Article 120 requires that insurance undertakings regularly validate
internal models through an annual validation cycle that includes: backtesting of
model outputs against observed outcomes; analysis of model stability;
sensitivity analysis; and assessment of the accuracy, completeness, and
appropriateness of data. This validation must be independent of the model
development function and must produce a formal report to the board.

The ASDLC output quality rate SLO and the ongoing monitoring process support
compliance with the Solvency II ongoing monitoring obligation, but they are
not sufficient on their own. The Solvency II annual validation requires:

- Backtesting against realised outcomes over the validation period — not
  sampling against acceptance criteria. The output quality rate SLO measures
  production quality; backtesting measures whether the model's outputs were
  correct in hindsight. The stewardship model must include a backtesting process
  that compares the agent product's outputs against observed outcomes with
  appropriate lag to allow outcomes to materialise.
- Independent validation by a function separate from development. ASDLC's
  RG-2 (Independent Validation Passed) at the Release Gate is the initial
  validation; the ongoing annual validation is a separate process governed
  by the actuarial function. The steward's monitoring data feeds into the
  annual validation, but the validation itself must be conducted and signed
  off by qualified actuaries independent of the development team.
- A formal validation report to the board. The steward's quarterly review
  produces operational data; the annual validation report is a distinct
  governance document that synthesises the monitoring data, the backtesting
  results, and the sensitivity analysis into a board-level report.

### EIOPA AI Guidelines — Ongoing Performance Monitoring

EIOPA expects that insurance undertakings monitor AI system performance on
an ongoing basis and that underperforming systems are remediated or
decommissioned. The output quality rate SLO and the reasoning trace
completeness SLO are the primary ASDLC instruments that support compliance
with this expectation. For EIOPA purposes, "performance" includes fairness
and conduct outcomes, not only technical accuracy: an agent product that
produces statistically accurate outputs but generates disproportionate
adverse outcomes for a protected group is underperforming from a regulatory
perspective even if its technical SLO is met. See
[eu-ai-act-mapping.md](../eu-ai-act-mapping.md) for the cross-cutting EU AI
Act risk-tier mapping that intersects with EIOPA expectations for AI systems.

The steward's value realisation monitoring must include a conduct outcome
dimension for customer-facing agent products: are customers receiving outcomes
that a reasonable person would consider fair? For IDD-scope advisory agent
products, the customer outcome review must assess whether advice is meeting
customers' demands and needs as demonstrated by outcomes, not only as stated by
the suitability assessment at the time of sale.

### IDD — Product Monitoring Requirements

IDD Article 25(1) requires insurance manufacturers to monitor their products on
a regular basis, including the distribution channels used, to identify
circumstances that could affect the appropriateness of the product for the
target market. For distribution agent products, this product monitoring
obligation applies throughout the agent product's operational life.

The steward's value realisation monitoring, when extended to include IDD
product monitoring objectives, supports compliance with this obligation:
the steward monitors whether the agent product continues to serve the
target market appropriately and routes concerning trends to the product
governance function for review. The quarterly architectural health review
should include an IDD product monitoring component for distribution agent
products, confirming that the target market remains appropriate for the
product as distributed and that the agent's performance is consistent with
the target market's needs.

### Layer 4 Regulatory Control Mapping

| Regulation          | Article/Section | Operational Requirement                                                                                         | ASDLC Control                                                                                         | Gap                                                                                                                                                                                                                                                                                   |
| ------------------- | --------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Solvency II         | Art. 120        | Annual independent model validation; backtesting against outcomes; formal report to board                       | Output quality rate SLO; reasoning trace completeness SLO; stewardship model; quarterly health review | Annual validation requires backtesting against realised outcomes (not sampling against acceptance criteria) and a formal actuarial validation report. The ASDLC monitoring provides data inputs; the actuarial validation function must own the annual validation process and report. |
| EIOPA AI Guidelines | Section 4       | Ongoing performance monitoring; fairness and conduct outcome assessment; remediation of underperforming systems | Output quality rate SLO; steward's value realisation monitoring                                       | EIOPA monitoring expectations include fairness assessment — monitoring must include a conduct outcome dimension for customer-facing agent products, not only technical accuracy metrics. The SLO calibration must explicitly include fairness metrics.                                |
| IDD                 | Art. 25(1)      | Regular product monitoring for target market appropriateness; distribution channel review                       | Steward's value realisation monitoring extended to IDD product monitoring; quarterly health review    | IDD product monitoring must produce documentation that demonstrates regular review and appropriate response to concerning trends. The steward's monitoring process must produce records that are accessible to the distribution governance function and to supervisory authorities.   |
| DORA                | Arts. 9–11      | ICT risk management; incident management; business continuity                                                   | Patch management SLOs; incident classification; DR testing (DoD-8 for blast-radius tier 3)            | DORA applies to insurance undertakings. ASDLC supports compliance with DORA Arts. 9–11 to the same extent as described in the financial services domain file.                                                                                                                                            |

---
