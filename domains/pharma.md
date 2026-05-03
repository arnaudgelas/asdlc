# ASDLC Domain Guidance — Pharmaceuticals / Life Sciences

_Pharma and life sciences-specific regulatory requirements for ASDLC Layers 1,
3, and 4._

See [Pharma Manifesto Alignment](../../domains/pharma.md) for manifesto
principle mappings (GAMP 5, CSA, 21 CFR Part 11, EU Annex 11, ICH Q8-Q12).
See the [ASDLC Overview](../asdlc.md) for the full lifecycle framework. See
[governance/gate-registry.md](../governance/gate-registry.md) for the
canonical gate condition enumeration referenced throughout this file. See
[retirement-gate.md](../retirement-gate.md) for the canonical resolution of
the data-subject-rights vs. retention conflict (Condition 3).

> **Conformance profile expectation.** Organisations operating in this
> regulated context typically claim the ASDLC-Regulated conformance profile
> (see [conformance-profiles.md](../conformance-profiles.md)).
>
> **Scope of regulatory claims.** This file maps ASDLC controls to pharma /
> life sciences regulatory obligations. Throughout, "supports compliance
> with", "operationalises", and "produces evidence aligned with" are used
> in preference to "is" or "satisfies" because ASDLC alone is rarely
> sufficient to discharge a regulatory requirement; ASDLC artefacts
> contribute to a compliance posture that the organisation must complete
> with regulatory counsel, supervisory engagement, and additional
> artefacts (the GAMP 5 Design Specification with its specific contents,
> 21 CFR Part 11 audit-trail format, GxP validation reports, and the
> like). Specific limits — including the GAMP 5 Design Specification gap
> at Layer 2 — are flagged in each section.

---

## ASDLC Layer 1 — Demand & Value Regulatory Requirements (Pharmaceuticals)

The demand layer of the ASDLC ([demand/value.md](../demand/value.md)) is the
governed entry point that determines what enters the engineering execution loop.
In pharmaceutical and life sciences contexts, demand governance carries specific
regulatory obligations that must be satisfied before the specification readiness
gate opens.

**GAMP 5 — User Requirement Specifications (URS).** GAMP 5 (2nd ed. 2022)
requires that User Requirement Specifications are validated against business
processes before system development begins. The Specification Readiness Gate
conditions SR-1 (Business Need Validated) and SR-3 (Acceptance Criteria
Expressible) — see
[governance/gate-registry.md](../governance/gate-registry.md) — support
compliance with the URS expectation. The URS is the pharmaceutical
equivalent of the loop-ready specification: it establishes what the
computerised system must do, in the users' own terms, before any design or
development activity starts. A demand item that has not produced a URS-
equivalent artefact has not completed the Layer 1 bridge and must not enter
the Specify phase. ASDLC alone does not produce all GAMP 5 lifecycle
documents: GAMP 5 also requires Functional Specification (FS) and Design
Specification (DS) documents with specific contents that ASDLC artefacts do
not directly produce. The bridge from ASDLC's machine-readable specification
to the GAMP 5 DS sits at Layer 2 and must be operationalised by the
organisation alongside ASDLC.

**21 CFR Part 11 — Electronic records and signatures.** Part 11
applicability determination must occur at the system conception stage, not
during or after development. The Specification Readiness Gate condition
SR-4 (Constraints Identified), defined in
[specification-readiness.md](../specification-readiness.md), must explicitly
include a Part 11 applicability assessment: does the system create, modify,
maintain, archive, retrieve, or transmit electronic records that are
required under FDA regulations or submitted to FDA? If yes, the full scope
of Part 11 requirements — audit trail, access controls, electronic
signature, validation — must be captured as constraints before the loop
starts. SR-4 supports compliance with the applicability-determination
expectation; it does not by itself produce the Part 11 audit-trail format
(an additional artefact at Layers 2 and 3). Discovering Part 11 scope
during or after the Execute phase is a demand-layer failure.

**ICH Q10 — Pharmaceutical Quality System.** Quality planning must occur before
development begins. ICH Q10 requires that quality is designed in, not inspected
in, and that the lifecycle starts with planning. The demand layer's
specification readiness gate is the control: a specification that has not
addressed quality planning — risk assessment, change control implications,
performance monitoring approach — is not Q10-aligned at entry and will generate
unresolvable quality debt downstream in the lifecycle.

**GxP validation lifecycle — URS to FS bridge.** The canonical GxP
lifecycle flows from User Requirement Specification (URS) to Functional
Specification (FS) to Design Specification (DS) before implementation
begins. The ASDLC demand-to-specification bridge is structurally
consistent with the URS-to-FS portion of this lifecycle: the URS is the
validated business need, and the FS is the machine-readable specification
with acceptance criteria. The DS — which GAMP 5 expects to capture
specific contents (architectural design, interface specifications,
validation criteria, traceability to FS) — is not directly produced by
the Specify phase of the ASDLC loop; the Specify phase produces the
loop-ready specification, and the GAMP 5 DS is an additional artefact
that consumes ASDLC's specification and adds the GAMP 5-prescribed DS
contents. Organisations attempting to merge URS and FS into a single
step introduce validation-lifecycle compression that is inconsistent
with GAMP 5. The demand layer governs the URS; the Specify phase
governs the FS; the DS is produced alongside ASDLC at Layer 2. These
are separate artefacts with separate governance owners.

**Blast radius and validation tier alignment.** The demand layer's
validation tier scales with blast radius (blast-radius tier 1 / 2 / 3). For
pharmaceutical systems, blast radius includes GxP context. A system
affecting GMP batch records has a higher blast radius than a system
assisting drug discovery research, even if the engineering scope is
comparable. The ASIL-equivalent concept in pharma is the GAMP category and
GxP context: GMP systems warrant blast-radius tier 3 demand validation
(multiple evidence categories, formal regulatory assessment, business demand
sponsor sign-off) before the loop starts.

---

## ASDLC Layer 3 — Release & Deployment Regulatory Requirements (Pharmaceuticals)

The release layer ([release-governance.md](../release-governance.md))
governs the journey from loop-complete to production-deployed. For
pharmaceutical and life sciences systems, the Release Gate has eight
conditions (canonical enumeration in
[governance/gate-registry.md](../governance/gate-registry.md)); these
conditions are necessary but not sufficient, because GAMP 5 imposes
additional qualification expectations that must be addressed at the release
boundary.

**GAMP 5 Installation Qualification (IQ).** IQ requires documented
verification that a computerised system has been installed correctly in its
intended environment, that infrastructure components are as specified, and
that the installation has been formally accepted. The deployment
governance's configuration state hash (recording the exact deployed state),
the evidence bundle's infrastructure manifest, and the accountable human
sign-off support compliance with IQ expectations. For a pharmaceutical
deployment, the release Definition of Done produces evidence aligned with
the IQ record: the deployment ID, configuration state hash, environment
verification results, and the named qualified individual's acceptance
contribute to the IQ documentation package. If the release artefact does
not contain these elements, the IQ documentation pipeline is incomplete at
the time of deployment.

**GAMP 5 Operational Qualification (OQ).** OQ requires testing that the
installed system operates as specified — that the configured functions work
correctly within the defined operating ranges. RG-1 (Evidence Bundle
Complete; which requires evaluation reports demonstrating the system meets
its specifications) and the smoke-tests-passed-in-production element of the
release Definition of Done support compliance with OQ. For regulated
pharmaceutical systems, the OQ must demonstrate that the system operates
correctly in the production environment, not only in the staging
environment: production smoke tests are OQ tests, not optional verification
steps.

**21 CFR Part 11 — Audit trail requirements.** Part 11 § 11.10(e) requires
that audit trails include the date and time of operator entries and actions
that create, modify, or delete electronic records. The deployment evidence
— deployment ID, timestamp, environment, and the authorised human who
accepted production accountability — supports compliance with Part 11
audit-trail expectations for system-level events. For pharmaceutical
systems in Part 11 scope, the deployment evidence record must be generated,
stored, and retained as a Part 11 audit trail entry. This is not a post-
deployment documentation task; it is generated at the moment of deployment
and must be immutable thereafter. Note that Part 11 § 11.10(e) also
prescribes specific contents for record-level audit trails (operator
identity, time-stamp, original-and-changed-value capture); ASDLC supports
the system-level event capture and the immutability discipline, but the
record-level audit-trail format is an organisation-level artefact produced
alongside ASDLC.

**GAMP 5 change control.** GAMP 5 requires that all changes to validated
computerised systems go through a documented change control process. The
ASDLC Release Gate supports compliance with the change control expectation
for agentic systems: the evidence bundle is the change documentation, RG-4
(Accountable Human Sign-Off) is the change authorisation, and RG-5
(Compliance Documentation Complete) produces evidence aligned with the
change control record. For pharmaceutical systems, the change control
record must be filed in the organisation's quality management system (not
only in the engineering change record), and the GAMP 5 category of the
change (configuration change for prompt edits, system change for model
version updates) must be determined before the Release Gate is assessed.
Filing the record into the QMS is an organisation-level step; ASDLC
supplies the inputs.

**Deployment rollback and GxP restoration.** The rollback procedure
required by RG-3 (Rollback Procedure Tested) must include a GxP-specific
element for pharmaceutical systems: restoring the system to its previous
validated state, not only its previous operational state. A rollback that
restores software but not configuration, or that does not produce
documentation that the system is back in its validated state, does not
produce evidence aligned with GxP rollback expectations. The rollback
procedure must be validated — tested and documented — as part of the
release preparation, and the test result must be retained as validation
evidence.

---

## ASDLC Layer 4 — Operations & Maintenance Regulatory Requirements (Pharmaceuticals)

The operations and maintenance layer
([operations/governance.md](../operations/governance.md),
[maintenance-governance.md](../maintenance-governance.md)) governs the system
from production deployment onward. For pharmaceutical and life sciences systems,
this layer carries long-term regulatory obligations that extend well beyond the
initial deployment.

**GAMP 5 Performance Qualification (PQ).** PQ requires ongoing verification
that a system performs as intended in its production environment over
time, under real production conditions with real production data. The
operational layer's output quality rate SLO and the reasoning trace
completeness SLO support compliance with PQ expectations: they confirm
that the system's quality in production matches the quality demonstrated
at OQ, and that degradation is detected before it constitutes a PQ
failure. PQ is not a one-time test; it is a continuous measurement
obligation. The output quality SLO must be defined before deployment and
must be calibrated against the GxP risk context: GMP systems require more
frequent sampling and tighter quality floors than drug discovery tooling.

**21 CFR Part 211 / GxP record retention.** GxP regulations typically
require records to be retained for 15 years for clinical data (21 CFR Part
312), the product lifetime plus one year for GMP records (EU GMP Annex 15),
and varying periods for other GxP contexts. The ASDLC trace retention
policy ([maintenance-governance.md](../maintenance-governance.md)) must be
configured to align with the applicable retention period for each GxP
context. For systems operating in the EU, this creates a potential
conflict with GDPR Article 17 (right to erasure): reasoning traces that
contain personal data may simultaneously need to be retained for GxP
compliance and deleted under GDPR. This conflict must be resolved at the
system design stage (not at decommission), with appropriate legal and
regulatory input, and the resolution must be documented in the maintenance
governance record. The Retirement Gate's Condition 3 (Trace and Reasoning-
Record Archival) — see [retirement-gate.md](../retirement-gate.md) —
formalises the resolution requirement at the gate boundary: the conflict
between deletion-rights and retention-mandates must be resolved with a
documented decision that names the rights-holder claim, the retention
obligation, and the controlling rule under the organisation's legal
counsel's analysis. Pharma systems that defer this decision to retirement
will fail Retirement Gate Condition 3.

**GAMP 5 periodic review.** GAMP 5 requires that validated systems are
periodically reviewed to confirm continued fitness for purpose — that the system
still meets its validated requirements, that its configuration has not drifted
from its validated state, and that the regulatory and business context that
governed its validation remains current. The ASDLC quarterly architectural
health review ([maintenance-governance.md](../maintenance-governance.md)) and the
steward's value realisation monitoring support compliance with the GAMP 5
periodic review expectation. For pharmaceutical systems, the periodic
review must explicitly confirm: that the system's GAMP category
classification remains appropriate, that the validation plan remains
current, and that any changes since the last review have been managed
under change control. The quarterly cadence in the ASDLC framework aligns
with most pharmaceutical periodic review expectations; confirm the
applicable requirement with the organisation's quality team.

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
