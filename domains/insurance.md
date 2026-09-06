# ASDLC Domain Guidance — Insurance

_Insurance-specific regulatory requirements for ASDLC Layers 1, 3, and 4._

See [Insurance Manifesto Alignment](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/domains/insurance.md) for manifesto
principle mappings. See the [ASDLC Overview](../asdlc.md) for the full lifecycle
framework.

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

Solvency II Article 115 requires that internal model documentation is sufficient
to demonstrate that the model meets the tests and standards, and that the
documentation enables the supervisory authority to assess compliance. This
documentation obligation begins at model conception — before engineering begins.
An undertaking that starts internal model development without governing the
model's purpose, methodology rationale, and intended use at the demand stage
will produce an artefact that cannot satisfy Solvency II documentation
standards, because the conception decisions were never recorded.

The demand layer's "business need validated" and "acceptance criteria
expressible" gate conditions are the controls that ensure the conceptual
soundness and intended purpose of the model are documented before development
starts. The business demand sponsor sign-off is, in the Solvency II context, the
Chief Actuary or Chief Risk Officer confirmation that this model is appropriate
for its intended use — the Solvency II use test requires that the model is used
in and influences the undertaking's decision-making, and the demand layer's
governance is the first evidence of that use intent.

The specification readiness gate's "blast radius assessed" condition must, for
Solvency II models, explicitly identify whether the model is material to the SCR
calculation. A model that contributes to SCR calculation is in scope for the
full internal model approval process, and the blast radius assessment triggers
the IMAP governance path. Discovering that a model is SCR-material after the
engineering execution loop has started means the IMAP governance documentation
trail is already incomplete.

### IDD — Suitability Assessment Process Validated Before System Development

The IDD requires that insurance distributors carry out a suitability assessment
appropriate to the complexity and risk of the product and calibrated to the
customer's demands and needs. For an agent product that performs this function,
the suitability assessment methodology must be validated against regulatory
requirements and actuarial standards before system development begins — not
derived from the system's outputs after it is built.

The demand layer's business need validation must include, for IDD-scope agent
products: confirmation that the proposed suitability assessment approach meets
IDD requirements in the target jurisdictions; confirmation that the demands and
needs statement format satisfies the IDD disclosure requirements; and
identification of any Member State-specific suitability requirements (such as
FCA ICOBS enhanced suitability requirements for particular product types) that
must be incorporated into the behavioral specification.

A demand item for an IDD advisory agent that has not addressed suitability
methodology validation before the specification readiness gate is not ready for
loop entry: the behavioral specification cannot be written without knowing what
the suitability assessment must produce.

### EIOPA AI Guidelines — Risk Assessment Before Deployment

EIOPA's guidelines require that insurance undertakings conduct a risk assessment
of AI systems before deployment. This is a pre-deployment obligation, but the
substantive risk assessment must be conducted well before deployment — ideally
at Stage 1. An undertaking that conducts its EIOPA risk assessment only at Stage
4 (pre-deployment) will discover design and governance issues that cannot be
addressed at that point.

The specification readiness gate's "constraints identified" condition is the
Layer 1 implementation of the EIOPA pre-deployment risk assessment. For
insurance AI agent products, the constraints identified must include: the EIOPA
AI guidelines risk classification for the specific use case; the applicable
conduct obligations (IDD, FCA Consumer Duty) that constrain the agent's
behavioral envelope; and the Solvency II model governance tier applicable to the
use case. A specification readiness gate that does not address these constraints
for insurance agent products is an incomplete gate.

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
model change governance and IDD product governance requirements impose specific
pre-deployment obligations. The eight release gate conditions are necessary but
not sufficient for Solvency II models; major model changes require supervisory
pre-approval that is not part of the standard release gate.

### Solvency II Model Change Policy — Major vs. Minor Change Governance

Solvency II Article 115 requires internal model undertakings to have a policy
on model changes that governs what constitutes a major change (requiring
supervisory approval) and what constitutes a minor change (governed by internal
procedures). [fabricated paragraph number withdrawn 2026-09-05: this
previously appended a parenthetical "3" to the Article 115 citation. Article
115 has no numbered paragraphs — it
is five unnumbered subparagraphs. The article and the substance cited here
are unaffected; only the "(3)" is cut.] The release gate's compliance documentation
condition (Condition 5)
must confirm the model change classification for every release to a Solvency II
internal model: major or minor, and the governance path followed.

For major model changes: the supervisory pre-approval is a gate condition that
must be obtained before the APLC release gate is assessed. A release that
proceeds to the Stage 4 gate without supervisory pre-approval for a major change
has not satisfied the Solvency II change policy regardless of the technical
quality of the change. The release gate must include a compliance documentation
element confirming supervisory approval reference and date.

For minor model changes: the internal governance documented in the change record
— the evidence bundle, the independent validation result, and the accountable
actuary's sign-off — is the Solvency II minor change governance record. The
release gate's Condition 4 (accountable human sign-off) for Solvency II minor
model changes must be the Chief Actuary or a person with delegated authority
from the actuarial function, not a technology lead.

### IDD Product Oversight and Governance (POG) Requirements for Distribution

Changes

IDD Article 25 and EIOPA guidelines on product oversight and governance require
insurance manufacturers to ensure that products are designed for a specific
target market and that distribution channels are appropriate for that market.
Changes to agent products used in distribution — configuration changes that
affect the products offered, the suitability assessment logic, or the customer
segments served — are POG-relevant changes that must go through the product
governance process before deployment.

The release gate's compliance documentation condition must confirm POG sign-off
for distribution agent product changes. POG sign-off is distinct from the
actuarial or technology sign-off: it is a Product Owner or Distribution
Governance confirmation that the change has been assessed against the target
market definition and that the revised agent product remains appropriate for the
intended target market.

For IDD-scope changes, the release gate must also confirm that the updated
demands and needs statement, if any, has been reviewed and approved and that the
customer-facing disclosure materials reflect the change. A distribution agent
product change that goes to production without updated IDD disclosures is a
conduct risk that the release gate must catch.

### Layer 3 Regulatory Control Mapping

| Regulation  | Article/Section                | Release Requirement                                                                             | ASDLC Control                                                                                                                                                         | Gap                                                                                                                                                                                                                                                                                                  |
| ----------- | ------------------------------ | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Solvency II | Art. 115 ¹                     | Major model changes require supervisory pre-approval; minor changes governed by internal policy | Compliance documentation condition (Condition 5): model change classification; supervisory approval reference for major changes; actuarial sign-off for minor changes | Major model change classification is a judgment call that requires actuarial and legal input. The release gate does not include a model change classification verification step; this must be confirmed before the gate is assessed.                                                                 |
| Solvency II | Art. 115                       | Model documentation updated to reflect changes before deployment                                | Evidence bundle complete (Condition 1): change description in evidence bundle; composite state manifest reflecting updated configuration                              | Model documentation update for Solvency II purposes must satisfy the supervisory authority's format requirements — not only document what changed but demonstrate that the updated model still meets all six Solvency II tests. This requires a model validation update concurrent with the release. |
| IDD         | Art. 25 / EIOPA POG guidelines | Distribution changes assessed against target market; POG sign-off before deployment             | Compliance documentation condition (Condition 5): POG sign-off confirmation; updated disclosure materials confirmed                                                   | POG sign-off involves the distribution governance function, which may not be part of the standard release gate stakeholder set. Ensuring POG sign-off is part of the release gate requires explicit inclusion in the compliance documentation checklist for IDD-scope agent products.                |
| DORA        | Art. 9(4)(e) ²      | Changes tested before implementation (carried by Art. 9(4)(e)'s "recorded, tested, assessed, approved, implemented and verified in a controlled manner"); rollback procedure documented — an ASDLC control, not sourced to DORA, the search term `rollback` occurring zero times in the Regulation. See ² | Evidence bundle complete (Condition 1); rollback procedure tested (Condition 3)                                                                                       | DORA applies to insurance undertakings. The DORA change management requirements are the same as described in the financial services domain file — see ² for the correction. The rollback half of the Release Requirement cell is not sourced to any DORA provision and must not be relied on as one; it is retained here as an ASDLC control.                                                                                                                                                     |

¹ [fabricated paragraph number withdrawn 2026-09-05: this row previously
appended a parenthetical "3" to the Art. 115 citation. Article 115 has no numbered paragraphs. The article and
substance are unaffected; only the "(3)" is cut.]

² [citation corrected 2026-09-05: this row previously cited DORA Article 14.
That citation was withdrawn because DORA Article 14 is *Communication* — crisis
communication plans, staff and stakeholder communication policies, and a
named media contact — and carries no change-management provision; its
paragraph 2 has no lettered sub-paragraphs, so `(a)`–`(c)` do not exist. The
row above is now correctly cited at DORA Article 9(4)(e), verified verbatim
against the primary (EUR-Lex, Regulation (EU) 2022/2554). Corrected further
2026-09-05: Article 9(4)(e) does not use the word `rollback`, and the search term
`rollback` occurs zero times in the Regulation against the hashed primary
(`inputs/20260905-arnaud/prep/asdlc-standards/sources/dora_fulltext.txt`,
sha256 `25328c7e…3b4d1e`) with a live one-word-swap negative control, so the
rollback half of the row's Release Requirement is an ASDLC control rather than
a DORA one. It was not deleted; it is marked in the row itself, matching the
same marking in `domains/financial-services.md` and `release-governance.md`.
See
`domains/financial-services.md`'s "DORA Article 9(4)(e) — ICT Change
Management" section for the full quotation and
`inputs/20260905-arnaud/prep/asdlc-standards/` for the underlying research.]

---

## ASDLC Layer 4 — Operations & Maintenance Regulatory Requirements (Insurance)

Layer 4 — operational governance as defined in
[operations/governance.md](../operations/governance.md) — is where the
long-term Solvency II model monitoring, EIOPA AI guidelines performance
monitoring, and IDD product monitoring obligations attach. These are ongoing
obligations that persist throughout the agent product's operational life.

### Solvency II — Ongoing Model Monitoring and Validation Requirements

Solvency II Article 124 (*Validation standards*) requires that insurance and
reinsurance undertakings "have a regular cycle of model validation which
includes monitoring the performance of the internal model, reviewing the ongoing
appropriateness of its specification, and testing its results against
experience". Article 124 further requires an effective statistical process for
validating the model, an analysis of the stability of the internal model
including sensitivity testing of its results to changes in key underlying
assumptions, and an assessment of the accuracy, completeness and appropriateness
of the data used. **Article 124 sets no interval: it says "a regular cycle", not
"annual".** An annual cadence is therefore a policy-set choice with no provision
behind it, and must be stated as the undertaking's own policy rather than as a
Solvency II requirement. Article 124 likewise does not prescribe that validation
be independent of the model development function or that it produce a formal
report to the board; independence and board reporting are governance
expectations sourced elsewhere — Article 120 (*Use test*) makes the
administrative, management or supervisory body "responsible for ensuring the
ongoing appropriateness of the design and operations of the internal model" —
and are treated here as such, not as Article 124 duties.

The ASDLC output quality rate SLO and the ongoing monitoring process are the
engineering controls for the Solvency II ongoing monitoring obligation, but they
are not sufficient on their own. A validation cycle satisfying Article 124 —
run at a policy-set annual cadence, an interval Article 124 does not itself
prescribe — requires:

- Testing results against experience — Article 124's own words — over the
  validation period, not sampling against acceptance criteria. The output
  quality rate SLO measures production quality; testing against experience
  measures whether the model's outputs were correct in hindsight. The
  stewardship model must include a results-against-experience process that
  compares the agent product's outputs against realised outcomes with
  appropriate lag to allow outcomes to materialise.
- Independent validation by a function separate from development — a
  policy-set control, not an Article 124 requirement, since Article 124
  prescribes no independence. The ASDLC's independent validation at Stage 3 is
  the initial validation; the ongoing validation cycle is a separate process
  governed by the actuarial function. The steward's monitoring data feeds into
  it, but the validation itself must be conducted and signed off by qualified
  actuaries independent of the development team.
- A formal validation report to the board — again a policy-set control rather
  than an Article 124 requirement, though it serves the Article 120 duty of the
  administrative, management or supervisory body to ensure the ongoing
  appropriateness of the internal model's design and operations. The steward's
  quarterly review produces operational data; the validation report is a
  distinct governance document that synthesises the monitoring data, the
  results-against-experience testing, and the sensitivity analysis into a
  board-level report.

### EIOPA AI Guidelines — Ongoing Performance Monitoring

EIOPA expects that insurance undertakings monitor AI system performance on an
ongoing basis and that underperforming systems are remediated or decommissioned.
The output quality rate SLO and the reasoning trace completeness SLO are the
primary instruments for this obligation. For EIOPA purposes, "performance"
includes fairness and conduct outcomes, not only technical accuracy: an agent
product that produces statistically accurate outputs but generates
disproportionate adverse outcomes for a protected group is underperforming from
a regulatory perspective even if its technical SLO is met.

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

The steward's value realisation monitoring, when extended to include IDD product
monitoring objectives, satisfies this obligation: the steward monitors whether
the agent product continues to serve the target market appropriately and routes
concerning trends to the product governance function for review. The quarterly
architectural health review should include a IDD product monitoring component
for distribution agent products, confirming that the target market remains
appropriate for the product as distributed and that the agent's performance is
consistent with the target market's needs.

### Layer 4 Regulatory Control Mapping

| Regulation          | Article/Section | Operational Requirement                                                                                         | ASDLC Control                                                                                         | Gap                                                                                                                                                                                                                                                                                   |
| ------------------- | --------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Solvency II         | Art. 124        | "A regular cycle of model validation" — no interval prescribed; monitoring model performance, reviewing the appropriateness of its specification, testing results against experience, stability and sensitivity analysis, and assessment of data accuracy, completeness and appropriateness | Output quality rate SLO; reasoning trace completeness SLO; stewardship model; quarterly health review | Article 124 requires testing results against experience (not sampling against acceptance criteria); the annual cadence, the independence of the validating function, and the formal actuarial validation report are policy-set controls with no Article 124 provision behind them. The ASDLC monitoring provides data inputs; the actuarial validation function must own the validation process and report. |
| EIOPA AI Guidelines | Section 4       | Ongoing performance monitoring; fairness and conduct outcome assessment; remediation of underperforming systems | Output quality rate SLO; steward's value realisation monitoring                                       | EIOPA monitoring expectations include fairness assessment — monitoring must include a conduct outcome dimension for customer-facing agent products, not only technical accuracy metrics. The SLO calibration must explicitly include fairness metrics.                                |
| IDD                 | Art. 25(1)      | Regular product monitoring for target market appropriateness; distribution channel review                       | Steward's value realisation monitoring extended to IDD product monitoring; quarterly health review    | IDD product monitoring must produce documentation that demonstrates regular review and appropriate response to concerning trends. The steward's monitoring process must produce records that are accessible to the distribution governance function and to supervisory authorities.   |
| DORA                | Arts. 9–11      | ICT risk management; incident management; business continuity                                                   | Patch management SLOs; incident classification; DR testing                                            | DORA applies to insurance undertakings. The DORA operational requirements are the same as described in the financial services domain file.                                                                                                                                            |

---
