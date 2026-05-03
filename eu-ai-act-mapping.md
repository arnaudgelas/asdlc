# EU AI Act — Risk Tier Mapping

_A cross-cutting mapping document — not a domain file — that maps ASDLC's
AutonomyTier and BlastRadiusTier classifications onto the risk categories
of the European Union's Artificial Intelligence Act (Regulation (EU)
2024/1689) and identifies the obligations that attach in each risk
category. The mapping does not substitute for qualified counsel on EU
AI Act applicability; it states how ASDLC's gate and evidence machinery
relates to the Act's requirements where the requirements apply._

See [asdlc.md](asdlc.md) for the ASDLC's tier definitions. See
[governance/gate-registry.md](governance/gate-registry.md) for the
canonical gate condition enumeration. See [conformance-profiles.md](conformance-profiles.md)
for the profile under which an EU AI Act-bound organisation will
typically claim ASDLC conformance.

---

## Scope

The EU AI Act (Regulation (EU) 2024/1689 of the European Parliament and
of the Council, OJ L 1689, 12.7.2024) defines a risk-tiered regulatory
regime for AI systems placed on the market, put into service, or used in
the European Union. The Act's application is determined by the system's
category (prohibited, high-risk, limited-risk, minimal-risk, or general-
purpose AI) and by the role of the actor (provider, deployer, importer,
distributor, authorised representative).

This document maps ASDLC's tier model onto the Act's risk categories so
that an organisation operating ASDLC-governed agentic systems can identify
which Act obligations attach to which systems in its portfolio and which
ASDLC artefacts contribute to the documentation pipeline that the Act
requires.

The mapping is not a determination of Act applicability for any specific
system. Applicability depends on the system's purpose, its classification
under Annex I and Annex III, the role of the actor, and the system's
intended deployment. Qualified counsel determines applicability; this
mapping describes how ASDLC supports the documentation pipeline once
applicability is determined.

---

## Risk-tier mapping

The matrix below maps ASDLC's AutonomyTier × BlastRadiusTier combinations
onto the EU AI Act's risk categories. The mapping is indicative: an
organisation's specific systems may fall into different categories
depending on their purpose and classification under the Act's annexes.
The matrix is a starting point for the per-system assessment, not a
substitute for it.

| AutonomyTier × BlastRadiusTier | Typical EU AI Act category |
|--------------------------------|----------------------------|
| A1 × BR1 | Minimal risk |
| A1 × BR2 | Minimal or limited risk; depends on use case |
| A1 × BR3 | Limited risk; high-risk if Annex III applies |
| A2 × BR1 | Minimal or limited risk |
| A2 × BR2 | Limited risk |
| A2 × BR3 | High-risk if Annex III applies; limited otherwise |
| A3 × BR1 | Limited risk |
| A3 × BR2 | High-risk if Annex III applies; limited otherwise |
| A3 × BR3 | High-risk; assess against Annex III |
| A4 × any BR | High-risk by default; assess against Annex III; Tier 4 envelopes operating fully autonomously over consequential decisions are high-risk by structure |
| Any × any | Prohibited if Article 5 applies (e.g., social scoring, real-time remote biometric identification with the named exceptions, manipulative or exploitative practices); General-purpose AI obligations apply at the model layer per Articles 51–55 in addition to the system-level category |

The Annex III categories of high-risk systems include biometrics, critical
infrastructure, education and vocational training, employment and worker
management, access to essential services, law enforcement, migration and
border control, administration of justice and democratic processes, and
the categories enumerated in Annex III of the Regulation as it stands at
the time of assessment. Systems in those categories are high-risk
regardless of the AutonomyTier × BlastRadiusTier matrix above; the matrix
is the floor, Annex III is the binding determinant.

General-purpose AI models — foundation models within the Act's meaning —
carry their own obligations at the model provider layer (Articles 51–55).
Where an ASDLC-governed system uses an externally-provided foundation
model, the model-provider obligations sit with the provider, but the
deployer obligations under Article 26 attach to the deploying organisation.

---

## High-risk system obligations and ASDLC artefact mapping

The table below enumerates the principal high-risk system obligations
under the Act and identifies the ASDLC artefact(s) that contribute to
each. "Contributes to" does not mean "fully satisfies"; the Act's
documentation requirements have specific format mandates that ASDLC
artefacts may not produce verbatim.

| Act obligation | Substance | Contributing ASDLC artefacts | Gap notes |
|----------------|-----------|--------------------------------|-----------|
| Annex III (high-risk system list) | Determines high-risk applicability for systems in enumerated categories | The system's SR-4 constraint set must reference the applicable Annex III category if any | The Annex III determination is a legal determination, not a delivery artefact |
| Article 9 (risk management system) | Continuous, iterative risk management throughout the system lifecycle | SR-6 blast radius assessment; the OWASP LLM Top 10 threat modelling at SR-4; the feedback paths in [asdlc.md](asdlc.md) | The Article 9 RMS is a management system in the ISO sense; ASDLC contributes to it but does not constitute it |
| Article 10 (data and data governance) | Quality, relevance, representativeness, and bias examination of training, validation, and test data | The evaluation portfolio specification at Layer 2 (manifesto P8); the data classification at SR-4; the dataset provenance records in the evidence bundle | The Act's specific data-governance examination obligations (e.g., examination for biases that could affect health, safety, or fundamental rights) require dedicated assessment artefacts that ASDLC's evaluation portfolio supports but does not specifically format |
| Article 11 (technical documentation) | Documentation conforming to Annex IV, kept up to date | The evidence bundle and control state record provide most of the substantive content; the runbook (DoD-1) provides the operational documentation | Annex IV has a specified format that ASDLC does not produce verbatim; a documentation-shaping step is required to convert ASDLC artefacts into Annex IV form |
| Article 12 (record-keeping) | Logs of events automatically generated throughout the system's lifetime | Reasoning traces, AgentOps telemetry (DoD-2), and the trace retention policy (DoD-7) | The retention period under DoD-7 must satisfy the Act's record-keeping period; for high-risk systems, the floor is the Act's requirement, not the ASDLC default |
| Article 13 (transparency and provision of information to deployers) | Instructions for use, intended purpose, level of accuracy, robustness and cybersecurity | The system's runbook (DoD-1), the SR-1 business need record, the evaluation portfolio's accuracy and robustness artefacts | The instructions-for-use format under the Act may differ from the runbook format; a documentation-shaping step is required |
| Article 14 (human oversight) | Effective human oversight by natural persons during use | The autonomy-tier model and the agent control plane (see [agent-control-plane.md](agent-control-plane.md)); the named accountable human at SR-5 and RG-4; the human-oversight pattern taxonomy referenced in [asdlc.md](asdlc.md) | The Act's Article 14(4) specifies oversight measures that the ASDLC's tier model supports; the determination that the measures are "effective" remains a judgment by the deployer's compliance function |
| Article 15 (accuracy, robustness, cybersecurity) | Appropriate levels of accuracy, robustness, and cybersecurity throughout the lifecycle | The evaluation portfolio's accuracy results, the adversarial evaluation portfolio (P8), the dynamic security testing condition RG-6, the security-governance pipeline | The Act's "appropriate level" standard is contextual; the ASDLC produces the evidence pipeline that the deployer's risk owner uses to make the appropriateness judgment |
| Article 17 (quality management system) | Documented QMS for providers of high-risk AI systems | The full ASDLC governance infrastructure, the conformance profile attestation, and the quarterly DoD review cadence | The QMS framing is broader than ASDLC; ASDLC is the delivery-side QMS for agentic systems, but provider QMSs typically include sales, post-market monitoring, and customer-management functions outside the framework |
| Article 26 (deployer obligations) | Deployer obligations including human oversight, monitoring, and reporting | The operational DoD, the maintenance governance, the L4 → L1 and L4 → L2 feedback paths | Deployer-specific reporting (e.g., serious incident reporting under Article 73) is operational; the framework supports the reporting pipeline |
| Article 50 (transparency for users of certain AI systems) | Disclosure to natural persons that they are interacting with an AI system; disclosure of deepfakes; disclosure of emotion-recognition systems; disclosure of biometric categorisation | The system's user-facing disclosures, governed at SR-4 as constraints | The disclosures are user-experience artefacts outside the framework; ASDLC ensures the constraint is captured at the demand layer |

### Obligations ASDLC does not satisfy

The following obligations require artefacts or processes that ASDLC does
not produce verbatim. An organisation operating ASDLC must augment the
framework's outputs to satisfy them:

- **Annex IV technical documentation in the prescribed format.** ASDLC
  produces the substance (evidence bundle, control state record,
  runbook, evaluation portfolio results); a documentation-shaping
  process must convert the substance into the Annex IV layout.
- **Conformity assessment under Article 43.** Conformity assessment is
  performed by a notified body for high-risk systems falling within the
  scope of Article 43(1) or by the provider under internal control for
  systems falling within Article 43(2). The conformity-assessment
  determination is an external matter; ASDLC supports the documentation
  pipeline that the conformity assessment evaluates.
- **CE marking.** The CE mark and the related Declaration of Conformity
  are regulatory artefacts produced as the output of conformity
  assessment, not the input. ASDLC supports the inputs.
- **Post-market monitoring system under Article 72.** Post-market
  monitoring is a structured surveillance system that the provider
  operates. ASDLC's Layer 4 feedback paths and operational governance
  contribute substantively but do not constitute the post-market
  monitoring system on their own; an organisation must define its
  post-market monitoring artefact and tie it to the framework's
  feedback mechanisms.
- **Serious incident reporting under Article 73.** Serious-incident
  reporting is a regulatory reporting obligation with specified content
  and timing. ASDLC's incident management governance produces the
  underlying incident records; the conversion of those records into the
  Article 73 report format is a separate process.

---

## General-purpose AI (GPAI) considerations

Where an ASDLC-governed system uses an externally-provided foundation
model, the model-provider obligations under Articles 51–55 attach to the
model provider, not to the deploying organisation. The deploying
organisation's obligations attach at the deployer layer (Article 26 and
the system-level obligations enumerated above for high-risk systems).

ASDLC's evidence bundle requirement (RG-1) for foundation model version
pinning supports the deployer's ability to demonstrate which specific
model version was deployed and was validated against. Where the deployed
model is itself a GPAI model with systemic risk under Article 51, the
deployer should expect that the model provider's obligations under
Articles 53–55 produce artefacts (model evaluation results, adversarial
testing results, systemic-risk assessments) that the deployer's
evidence bundle should reference, not duplicate.

---

## Cited authorities

- Regulation (EU) 2024/1689 of the European Parliament and of the
  Council of 13 June 2024 laying down harmonised rules on artificial
  intelligence and amending various Regulations and Directives
  (Artificial Intelligence Act). OJ L 1689, 12.7.2024.
- Specific articles cited above: Article 5 (prohibited practices),
  Article 9 (risk management system), Article 10 (data and data
  governance), Article 11 (technical documentation), Article 12 (record-
  keeping), Article 13 (transparency and provision of information to
  deployers), Article 14 (human oversight), Article 15 (accuracy,
  robustness, cybersecurity), Article 17 (quality management system),
  Article 26 (deployer obligations), Article 43 (conformity
  assessment), Article 50 (transparency obligations for providers and
  deployers of certain AI systems), Articles 51–55 (general-purpose AI
  models), Article 72 (post-market monitoring), Article 73 (reporting
  of serious incidents).
- Annex III (high-risk AI systems referred to in Article 6(2)) and
  Annex IV (technical documentation referred to in Article 11(1)) of
  the Regulation.

---

## Specific limitation

Conformity assessment under Article 43 is a notified-body matter for
systems within the scope of Article 43(1). ASDLC does not perform
conformity assessment; it supports the documentation pipeline that the
conformity assessment evaluates. The verb in any conformance claim is
"supports compliance with"; the framework does not on its own satisfy
the EU AI Act's obligations.

---

## Relationship to other ASDLC documents

This document is a cross-cutting mapping that interacts with multiple
ASDLC artefacts. The high-risk system obligations cited above are
operationalised through SR Gate conditions (see
[specification-readiness.md](specification-readiness.md) and
[governance/gate-registry.md](governance/gate-registry.md)), Release
Gate conditions (see [release-governance.md](release-governance.md)),
and Operational DoD conditions (see [operations/dod.md](operations/dod.md)).
The interaction with the agent control plane is documented in
[agent-control-plane.md](agent-control-plane.md). For organisations whose
systems also process personal information under California or US
healthcare privacy law, see [domains/ccpa.md](domains/ccpa.md) and
[domains/hipaa.md](domains/hipaa.md). The Tier 4-specific obligations
that an EU AI Act high-risk system operating with substantial autonomy
will attract are documented in [annex-aentm.md](annex-aentm.md) and
[annex-igm.md](annex-igm.md). The conformance profile applicable to
most EU AI Act high-risk-system operators is ASDLC-Regulated or, for
Tier 4 envelopes, ASDLC-Tier4 (see [conformance-profiles.md](conformance-profiles.md)).
