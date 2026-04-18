# ASDLC Domain Guidance — Pharmaceuticals / Life Sciences

_Pharma and life sciences-specific regulatory requirements for ASDLC Layers 1,
3, and 4._

See [Pharma Manifesto Alignment](../../domains/pharma.md) for manifesto
principle mappings (GAMP 5, CSA, 21 CFR Part 11, EU Annex 11, ICH Q8-Q12). See
the [ASDLC Overview](../asdlc.md) for the full lifecycle framework.

---

## ASDLC Layer 1 — Demand & Value Regulatory Requirements (Pharmaceuticals)

The demand layer of the ASDLC ([demand/value.md](../demand/value.md)) is the
governed entry point that determines what enters the engineering execution loop.
In pharmaceutical and life sciences contexts, demand governance carries specific
regulatory obligations that must be satisfied before the specification readiness
gate opens.

**GAMP 5 — User Requirement Specifications (URS).** GAMP 5 (2nd ed. 2022)
requires that User Requirement Specifications are validated against business
processes before system development begins. The demand layer's "business need
validated" and "acceptance criteria expressible" gate conditions map directly to
the URS. The URS is the pharmaceutical equivalent of the loop-ready
specification: it establishes what the computerised system must do, in the
users' own terms, before any design or development activity starts. A demand
item that has not produced a URS-equivalent artefact has not completed the Layer
1 bridge and must not enter the Specify phase.

**21 CFR Part 11 — Electronic records and signatures.** Part 11 applicability
determination must occur at the system conception stage, not during or after
development. The "constraints identified" gate condition in
[specification-readiness.md](../specification-readiness.md) must explicitly
include a Part 11 applicability assessment: does the system create, modify,
maintain, archive, retrieve, or transmit electronic records that are required
under FDA regulations or submitted to FDA? If yes, the full scope of Part 11
requirements — audit trail, access controls, electronic signature, validation —
must be captured as constraints before the loop starts. Discovering Part 11
scope during or after the Execute phase is a demand layer failure.

**ICH Q10 — Pharmaceutical Quality System.** Quality planning must occur before
development begins. ICH Q10 requires that quality is designed in, not inspected
in, and that the lifecycle starts with planning. The demand layer's
specification readiness gate is the control: a specification that has not
addressed quality planning — risk assessment, change control implications,
performance monitoring approach — is not Q10-aligned at entry and will generate
unresolvable quality debt downstream in the lifecycle.

**GxP validation lifecycle — URS to FS bridge.** The canonical GxP lifecycle
flows from User Requirement Specification (URS) to Functional Specification (FS)
to Design Specification (DS) before implementation begins. This maps to the
ASDLC demand-to-specification bridge: the URS is the validated business need,
the FS is the machine-readable specification with acceptance criteria, and the
DS emerges from the Specify phase of the loop. Organisations attempting to merge
URS and FS into a single step introduce validation lifecycle compression that is
inconsistent with GAMP 5. The demand layer governs the URS; the Specify phase
governs the FS. These are separate artefacts with separate governance owners.

**Blast radius and validation tier alignment.** The demand layer's validation
tier (Tier 1 / Tier 2 / Tier 3) scales with blast radius. For pharmaceutical
systems, blast radius includes GxP context. A system affecting GMP batch records
has a higher blast radius than a system assisting drug discovery research, even
if the engineering scope is comparable. The ASIL-equivalent concept in pharma is
the GAMP category and GxP context: GMP systems warrant Tier 3 demand validation
(multiple evidence categories, formal regulatory assessment, business demand
sponsor sign-off) before the loop starts.

---

## ASDLC Layer 3 — Release & Deployment Regulatory Requirements (Pharmaceuticals)

The release layer ([release-governance.md](../release-governance.md)) governs
the journey from loop-complete to production-deployed. For pharmaceutical and
life sciences systems, the five release gate conditions are necessary but not
sufficient: GAMP 5 imposes additional qualification requirements that must be
satisfied at the release boundary.

**GAMP 5 Installation Qualification (IQ).** IQ requires documented verification
that a computerised system has been installed correctly in its intended
environment, that infrastructure components are as specified, and that the
installation has been formally accepted. The deployment governance's
configuration state hash (recording the exact deployed state), the evidence
bundle's infrastructure manifest, and the accountable human sign-off map to IQ
requirements. For a pharmaceutical deployment, the release Definition of Done
should be treated as the IQ record: the deployment ID, configuration state hash,
environment verification results, and the named qualified individual's
acceptance constitute the IQ documentation package. If the release artefact does
not contain these elements, IQ documentation is incomplete at the time of
deployment.

**GAMP 5 Operational Qualification (OQ).** OQ requires testing that the
installed system operates as specified — that the configured functions work
correctly within the defined operating ranges. The release gate's "evidence
bundle complete" condition (which requires evaluation reports demonstrating the
system meets its specifications) and the "smoke tests passed in production"
condition map to OQ. For regulated pharmaceutical systems, the OQ must
demonstrate that the system operates correctly in the production environment,
not only in the staging environment: production smoke tests are OQ tests, not
optional verification steps.

**21 CFR Part 11 — Audit trail requirements.** Part 11 § 11.10(e) requires that
audit trails include the date and time of operator entries and actions that
create, modify, or delete electronic records. The deployment evidence —
deployment ID, timestamp, environment, and the authorised human who accepted
production accountability — maps directly to Part 11 audit trail requirements
for system-level events. For pharmaceutical systems in Part 11 scope, the
deployment evidence record must be generated, stored, and retained as a Part 11
audit trail entry. This is not a post-deployment documentation task; it is
generated at the moment of deployment and must be immutable thereafter.

**GAMP 5 change control.** GAMP 5 requires that all changes to validated
computerised systems go through a documented change control process. The ASDLC
release gate is the change control process for agentic systems: the evidence
bundle is the change documentation, the accountable human sign-off is the change
authorisation, and the compliance documentation condition maps to the change
control record. For pharmaceutical systems, the change control record must be
filed in the organisation's quality management system (not only in the
engineering change record), and the GAMP 5 category of the change (configuration
change for prompt edits, system change for model version updates) must be
determined before the release gate is assessed.

**Deployment rollback and GxP restoration.** The rollback procedure required by
the release gate must include a GxP-specific element for pharmaceutical systems:
restoring the system to its previous validated state, not only its previous
operational state. A rollback that restores software but not configuration, or
that does not produce documentation that the system is back in its validated
state, is not a GxP-compliant rollback. The rollback procedure must be validated
— tested and documented — as part of the release preparation, and the test
result must be retained as validation evidence.

---

## ASDLC Layer 4 — Operations & Maintenance Regulatory Requirements (Pharmaceuticals)

The operations and maintenance layer
([operations/governance.md](../operations/governance.md),
[maintenance-governance.md](../maintenance-governance.md)) governs the system
from production deployment onward. For pharmaceutical and life sciences systems,
this layer carries long-term regulatory obligations that extend well beyond the
initial deployment.

**GAMP 5 Performance Qualification (PQ).** PQ requires ongoing verification that
a system performs as intended in its production environment over time, under
real production conditions with real production data. The operational layer's
output quality rate SLO and the reasoning trace completeness SLO are the
engineering controls for PQ: they confirm that the system's quality in
production matches the quality demonstrated at OQ, and that degradation is
detected before it constitutes a PQ failure. PQ is not a one-time test; it is a
continuous measurement obligation. The output quality SLO must be defined before
deployment and must be calibrated against the GxP risk context: GMP systems
require more frequent sampling and tighter quality floors than drug discovery
tooling.

**21 CFR Part 211 / GxP record retention.** GxP regulations typically require
records to be retained for 15 years for clinical data (21 CFR Part 312), the
product lifetime plus one year for GMP records (EU GMP Annex 15), and varying
periods for other GxP contexts. The ASDLC trace retention policy
([maintenance-governance.md](../maintenance-governance.md)) must be configured
to meet the applicable retention period for each GxP context. For systems
operating in the EU, this creates a potential conflict with GDPR Article 17
(right to erasure): reasoning traces that contain personal data may
simultaneously need to be retained for GxP compliance and deleted under GDPR.
This conflict must be resolved at the system design stage (not at decommission),
with appropriate legal and regulatory input, and the resolution must be
documented in the maintenance governance record.

**GAMP 5 periodic review.** GAMP 5 requires that validated systems are
periodically reviewed to confirm continued fitness for purpose — that the system
still meets its validated requirements, that its configuration has not drifted
from its validated state, and that the regulatory and business context that
governed its validation remains current. The ASDLC quarterly architectural
health review ([maintenance-governance.md](../maintenance-governance.md)) and
the steward's value realisation monitoring map to the GAMP 5 periodic review
obligation. For pharmaceutical systems, the periodic review must explicitly
confirm: that the system's GAMP category classification remains appropriate,
that the validation plan remains current, and that any changes since the last
review have been managed under change control. The quarterly cadence in the
ASDLC framework meets most pharmaceutical periodic review requirements; confirm
the applicable requirement with the organisation's quality team.

**Pharmacovigilance systems — PSUR reporting timelines.** If the agentic system
participates in pharmacovigilance — adverse event signal detection, ICSR triage,
or literature monitoring — PSUR (Periodic Safety Update Report) reporting
timelines apply under ICH E2C(R2) and EU Pharmacovigilance Regulation
(Regulation (EU) No 1235/2010). The operational incident management process must
include a classification for pharmacovigilance-related quality incidents, and
the escalation path from a quality incident to the qualified pharmacovigilance
professional must be documented. The system steward must confirm at each
periodic review that the system's contribution to pharmacovigilance processes
remains within its validated scope and that any expansion of scope (new adverse
event categories, new data sources) triggers a re-validation before the expanded
function is used.

**Decommissioning and GxP record obligations.** When a GxP-regulated agentic
system is decommissioned, the retention obligations for its records survive the
system's retirement. The post-decommission artefact retention described in the
ASDLC maintenance governance
([maintenance-governance.md](../maintenance-governance.md)) must be calibrated
to the applicable GxP retention period — not the engineering system default. For
systems in scope for EU GMP Annex 11, the retirement documentation must confirm
that all electronic records the system created or managed have been migrated to
a compliant archive system before the system is taken offline.
