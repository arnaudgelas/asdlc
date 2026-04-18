# ASDLC Domain Guidance — Defense / Government

*Defense and government-specific regulatory requirements for ASDLC Layers 1, 3, and 4.*

See [Defense/Government Manifesto Alignment](../../domains/defense-government.md) for manifesto principle mappings (CMMC, FedRAMP, NIST SP 800-53, ITAR/EAR).
See the [ASDLC Overview](../asdlc.md) for the full lifecycle framework.

---

## ASDLC Layer 1 — Demand & Value Regulatory Requirements (Defense/Government)

The demand layer of the ASDLC ([demand-value.md](../demand-value.md))
governs what enters the engineering execution loop. In defense and government
contexts, demand governance must integrate with formal capabilities
documentation and risk management frameworks established well before software
development begins.

**MIL-STD-882E — System Safety at program conception.** MIL-STD-882E (System
Safety) requires that hazard identification and risk assessment begin at the
program conception stage, before any development activity starts. For defense
systems subject to MIL-STD-882E, the specification readiness gate's "blast
radius assessed" and "constraints identified" conditions must include a
preliminary hazard analysis (PHA) output. The PHA identifies hazards, assesses
their risk (severity × probability), and establishes the minimum risk
acceptable, which then constrains the development process and the acceptable
autonomy tier. A specification for a safety-relevant defense function that
enters the loop without a MIL-STD-882E PHA is missing its governing safety
constraint. The demand layer gate record must reference the PHA document, its
hazard classification, and the risk acceptance decision made by the program
safety officer.

**DoD 5000.02 — Defense Acquisition capabilities documents.** In the DoD
acquisition framework, software development is authorised by a series of
capabilities documents that constitute the formal demand layer: the Initial
Capabilities Document (ICD) establishes the capability gap and the solution
approach, the Capabilities Development Document (CDD) defines performance
attributes and key performance parameters, and the Capabilities Production
Document (CPD) governs production. The specification readiness gate's "business
need validated" condition must reference the appropriate capabilities document
for the acquisition phase. A software development initiative in a DoD program
that does not trace to an ICD, CDD, or CPD has not been validated through the
DoD demand process and lacks the programme authority to proceed. The ASDLC
demand layer does not replace these documents — it governs the translation from
capabilities document to engineering specification.

**NIST SP 800-37 — Risk Management Framework categorization before
development.** NIST SP 800-37 (RMF) requires that federal information systems
are categorized using FIPS 199 (defining the system's confidentiality,
integrity, and availability impact levels) and that security controls are
selected based on that categorization before system development begins. The
"constraints identified" gate condition must include RMF categorization for all
government information systems in scope. Categorization determines the control
baseline (NIST SP 800-53 Low, Moderate, or High), which in turn determines the
security controls that are mandatory for the system and therefore mandatory
constraints on the engineering loop. A specification that enters the loop
without a completed FIPS 199 categorization cannot identify its mandatory
security controls, which means its constraint set is incomplete at entry.

**DoDI 5000.87 — Adaptive Acquisition Framework for Software.** DoDI 5000.87
establishes the Software Acquisition Pathway, which requires an initial
capabilities document, documented performance goals, and development
authorisation before software development begins. Under the Software
Acquisition Pathway, the product backlog and sprint cadence are governed by the
program, with a "Capability Needs Statement" serving as the formal demand
artefact. The ASDLC demand layer's portfolio governance and specification
readiness gate are the engineering implementation of the DoDI 5000.87
governance requirements. Program managers should align the ASDLC demand gate
record with the Capability Needs Statement to maintain traceability from
program-level demand to engineering-level specification.

**Data classification as a demand gate condition.** As established in the
primary constraint section of this document, data classification is the
governing constraint in defense and government contexts. The specification
readiness gate must include a data classification determination for every
specification: what data will the system process, at what classification level,
and does the proposed infrastructure and autonomy tier comply with the handling
requirements for that classification? A specification for a system intended to
process CUI that does not identify FedRAMP Moderate as a required constraint,
or a specification for an ITAR-controlled program that does not identify export
control as a constraint, has an incomplete constraint set at the demand gate.
Data classification determination is not an engineering decision — it is a
security officer decision that must be made before the loop starts.

---

## ASDLC Layer 3 — Release & Deployment Regulatory Requirements
(Defense/Government)

The release layer ([release-governance.md](../release-governance.md))
governs the transition from loop-complete to production-deployed. In defense
and government contexts, the release boundary is also the ATO boundary: a
system cannot be deployed to a government production environment without an
Authority to Operate, and material changes to a deployed system may require ATO
reassessment before the change is authorised.

**CMMC — Change control for CUI-handling systems.** CMMC Level 2 (NIST SP
800-171 Practice 3.4.3) requires that changes to organisational systems are
controlled, documented, and audited. For systems handling CUI, the ASDLC
release gate — with its evidence bundle, accountable sign-off, and change
management alignment — is the CMMC change control process at the release
boundary. Specifically: the specification reference is the documented change
description, the evidence bundle is the change verification evidence, the
accountable human sign-off is the change authorisation, and the compliance
documentation condition ensures that CUI-related regulatory documentation is
complete before deployment. CMMC assessors reviewing the change control process
will look for these elements in the release record; organisations that maintain
them as described in [release-governance.md](../release-governance.md)
are producing CMMC-aligned change control documentation as a byproduct of sound
release governance.

**DoDI 8510.01 — ATO impact assessment before release.** DoD Instruction
8510.01 (Risk Management Framework for DoD IT) requires that software changes
to systems operating under an ATO are assessed for their impact on the existing
ATO before the changes are deployed. The assessment determines whether the
change is within the scope of the existing ATO (no new ATO action required),
constitutes a significant change requiring the Authorizing Official's review,
or exceeds the ATO boundary and requires a new or updated ATO. The release
gate's "compliance documentation complete" condition must include an ATO impact
assessment for all DoD systems in RMF scope. An ATO impact assessment that
concludes the change is within ATO scope is itself a compliance document; it
must be filed as part of the release record. A change deployed without an ATO
impact assessment is deployed outside the ATO's authorisation — the deployment
is non-compliant regardless of its technical quality.

**MIL-STD-498 / IEEE J-STD-016 — Software Version Description at release.**
MIL-STD-498 and its commercial equivalent IEEE J-STD-016 require that software
releases are accompanied by a Software Version Description (SVD): a document
identifying the software being delivered, the changes included, known problems,
and platform requirements. The deployment evidence — deployment ID,
configuration state hash, SBOM, and change record reference — maps to SVD
requirements. For DoD programs under MIL-STD-498, the release artefact should
be structured to satisfy SVD requirements: the deployment ID is the software
version identifier, the configuration state hash is the configuration
identification, the evidence bundle reference documents the changes included,
and the known issues from the Learn phase of the engineering loop are the known
problems section.

**NSA / CSS classified system requirements — scope limitation.** The ASDLC
framework explicitly excludes classified system development environments from
its scope, as established in the primary constraint section of this document.
For classified deployments — SECRET, TOP SECRET, and TS/SCI systems — software
must be approved through the appropriate Information Assurance accreditation
process before release: the Defense Information System for Security (DISS)
process, applicable security classification guides, and the cognizant security
authority's approval. The ASDLC release governance framework does not satisfy
these requirements and should not be represented as doing so. Programs that
develop software for classified deployments must engage with their Information
System Security Manager (ISSM) and the relevant security authority for the
applicable release governance requirements. This is an explicit scope
limitation, not a gap to be addressed in a future version.

**Emergency change and ATO.** The emergency change procedure
([release-governance.md](../release-governance.md)) does not waive ATO
requirements. A change that is outside the scope of the existing ATO cannot be
deployed as an emergency change — it requires ATO action, which has its own
timeline and cannot be compressed arbitrarily. The emergency change procedure
applies only to changes that are within the scope of the existing ATO but must
be deployed ahead of the normal release cycle. The distinction between "within
ATO scope" and "outside ATO scope" must be confirmed by the ISSO before the
emergency procedure is invoked.

---

## ASDLC Layer 4 — Operations & Maintenance Regulatory Requirements
(Defense/Government)

The operations and maintenance layer
([operations-governance.md](../operations-governance.md),
[maintenance-governance.md](../maintenance-governance.md)) governs the
system from production deployment through decommission. For federal and defense
systems, this layer carries continuous monitoring obligations, ongoing ATO
maintenance requirements, and FISMA compliance responsibilities that persist
throughout the system's operational lifetime.

**NIST SP 800-137 — Continuous Monitoring.** NIST SP 800-137 (Information
Security Continuous Monitoring) requires that federal information systems
implement an ongoing monitoring strategy that covers security control
assessments on a defined frequency, ongoing situational awareness, and
reporting to the Authorizing Official. The ASDLC operational observability
instruments — service health metrics, output quality rate SLO, reasoning trace
completeness, cost anomaly detection — and the maintenance governance security
patch management
([maintenance-governance.md](../maintenance-governance.md)) map to SP
800-137 requirements. Specifically: the CVSS-tiered patch SLOs satisfy SP
800-137's requirement for timely remediation of vulnerabilities, the output
quality SLO satisfies the ongoing assessment requirement for the system's
functional security controls, and the SBOM with automated vulnerability
scanning satisfies the supply chain monitoring requirement. The organisation's
Information Security Continuous Monitoring (ISCM) program should incorporate
the ASDLC operational metrics as automated monitoring inputs to the ISCM
strategy.

**DoDI 8510.01 — Ongoing ATO maintenance.** An ATO is not permanent. DoDI
8510.01 requires ongoing monitoring and periodic reassessment to confirm that
the risk posture has not changed materially since the ATO was granted. The
ASDLC stewardship model's responsibility for ongoing monitoring
([maintenance-governance.md](../maintenance-governance.md)) and the
quarterly architectural health review map to ongoing ATO maintenance
requirements. Specifically: the quarterly architectural health review is the
periodic control assessment, quality incidents and security patch events are
the ongoing monitoring inputs, and the steward's escalation to the accountable
human for governance decisions maps to the requirement for ongoing
communication with the Authorizing Official for significant risk changes. An
ATO held by a system whose steward is not performing ongoing monitoring is an
ATO that is not being actively maintained — a condition that creates regulatory
exposure and increases the risk of an ATO revocation if the system is assessed.

**FISMA — Continuous monitoring and incident response.** The Federal
Information Security Modernization Act (FISMA) requires that federal agencies
implement a continuous monitoring program and a documented incident response
capability. The ASDLC incident management process
([operations-governance.md](../operations-governance.md)) — including the
quality incident classification, the escalation chain, and the trace retention
policy — maps to FISMA incident response requirements. For FISMA-covered
systems, the incident response plan must be documented and tested, and
incidents must be reported to the appropriate authorities within defined
timeframes (US-CERT for federal civilian agency systems, DIBNet for defense
contractor systems). The ASDLC incident management process provides the
engineering governance; the organisation's FISMA incident response plan
provides the reporting and coordination requirements. Both must be in place;
neither is sufficient alone.

**MIL-STD-882E — Field safety incident reporting.** For defense systems subject
to MIL-STD-882E, safety-related incidents in the field require hazard
reporting: the system's safety documentation must be updated, the hazard risk
must be re-assessed, and corrective action must be tracked to closure. The
ASDLC quality incident classification in operations governance must include a
safety incident type for systems in MIL-STD-882E scope. A quality incident that
reveals a safety hazard is not only an engineering quality issue — it is a
MIL-STD-882E hazard report. The escalation path from a safety incident to the
program safety officer must be documented in the operational runbook before the
system goes to production. Discovering this escalation path during an active
safety incident is a governance failure that was preventable at the operational
readiness stage.

**Data retention and CUI decommissioning.** When a CUI-handling system is
decommissioned, the CUI records it processed must be handled in accordance with
32 CFR Part 2002 (Controlled Unclassified Information) and the applicable CUI
category requirements. For systems that have generated reasoning traces or
audit logs containing CUI, the decommission stage must include a CUI
disposition plan: what records must be retained (and for how long, per the
applicable CUI category), what records must be destroyed, and how destruction
is documented. The ASDLC post-decommission artefact retention
([maintenance-governance.md](../maintenance-governance.md)) must be
reconciled with CUI retention requirements at decommission time, with input
from the organisation's CUI Program Manager. Retaining traces containing CUI
beyond the applicable retention period is a CUI handling violation; destroying
records that must be retained for audit or legal purposes is an obstruction
risk.
