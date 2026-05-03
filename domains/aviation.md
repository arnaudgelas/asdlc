# ASDLC Domain Guidance — Aviation

_Aviation-specific regulatory requirements for ASDLC Layers 1, 3, and 4._

See [Aviation Manifesto Alignment](../../domains/aviation.md) for manifesto
principle mappings (DO-178C, DO-330, DO-333, ARP 4754A, DO-326A). See the
[ASDLC Overview](../asdlc.md) for the full lifecycle framework. See
[governance/gate-registry.md](../governance/gate-registry.md) for the
canonical gate condition enumeration referenced throughout this file.

> **Conformance profile expectation.** Organisations operating in this
> regulated context typically claim the ASDLC-Regulated conformance profile
> (see [conformance-profiles.md](../conformance-profiles.md)).
>
> **Scope of regulatory claims.** This file maps ASDLC controls to aviation
> regulatory obligations. Throughout, "supports compliance with",
> "operationalises", "structurally consistent with", and "produces evidence
> aligned with" are used in preference to "is" or "satisfies" because ASDLC
> alone does not directly produce all DO-178C / DO-330 / DO-333 lifecycle
> artefacts. ASDLC's evidence bundle is structurally consistent with the
> DO-178C lifecycle data set but does not by itself produce the SAS, the
> SCI, the PSAC, the SVD, the qualified-tool documentation, or the
> Designated Engineering Representative (DER) credential required for
> certain DAL-A and DAL-B objectives. Specific gaps — including the DER
> credential gap — are flagged in each section.

---

## ASDLC Layer 1 — Demand & Value Regulatory Requirements (Aviation)

The demand layer of the ASDLC ([demand/value.md](../demand/value.md)) governs
what enters the engineering execution loop. In aviation development contexts,
demand governance must integrate with the system-level processes established by
ARP 4754A before any software development activity starts.

**DO-178C / DO-330 — Requirements traceability at the demand boundary.**
DO-178C requires that all software requirements are traceable to system
requirements, and that no software requirement exists without a parent
system requirement. The demand-to-specification bridge's translation step —
from validated business need to machine-readable acceptance criteria —
supports compliance with this expectation. The Specification Readiness
Gate condition SR-3 (Acceptance Criteria Expressible) must demonstrate
that the derived software requirement traces to an identifiable system-
level requirement or allocated function before the specification enters
the loop. A specification that cannot demonstrate this traceability at
the demand gate will not produce evidence aligned with DO-178C § 5.1
traceability expectations when the software development record is
assembled for certification.

**ARP 4754A — System requirements validation preceding software
development.** ARP 4754A § 5 (System Requirements) requires that system
requirements are validated before software development starts: that they
are complete, correct, and consistent, and that they satisfy the intent
of the higher-level requirements from which they were derived. The
Specification Readiness Gate condition SR-1 (Business Need Validated)
supports compliance with the ARP 4754A system-requirements validation
expectation at the software entry point. An engineering team that begins
software development before the system requirements have been through
ARP 4754A validation does not produce evidence aligned with the
development process that generates the DAL assignment on which the team
is relying.

**DO-178C Design Assurance Level (DAL) determination.** The DAL must be
determined at the start of the software development activity, before the
loop begins, not during or after development. The Specification Readiness
Gate conditions SR-6 (Blast Radius Assessed) and SR-4 (Constraints
Identified) support compliance with the DAL-determination expectation:
they require that the safety significance of the function is established
and that the applicable DO-178C objectives (including the independence
requirements for higher DAL levels) are identified as constraints on the
loop. A specification that enters the loop without a confirmed DAL
assignment lacks its most fundamental governance constraint.

**FAA Order 8110.49 — Intended function documentation.** Software approval under
FAA Order 8110.49 requires documentation of the software's intended function,
its operating environment, and its relationship to the airborne system's safety
objectives. The demand layer's value definition and business need documentation
are required inputs to Order 8110.49 documentation. Specifically, the success
criterion and the system-level justification for the software function — which
are Layer 1 governance artefacts — become the intended function statement that
appears in the Plan for Software Aspects of Certification (PSAC). Teams that do
not govern demand rigorously at Layer 1 will discover at PSAC preparation time
that the intended function documentation is incomplete or inconsistent.

**PSAC framing at the demand stage.** The Plan for Software Aspects of
Certification — the primary planning document for DO-178C programs — should be
initiated in parallel with the demand layer governance for significant software
developments. The PSAC captures the software's intended function, its DAL, the
lifecycle standards, and the development tools and methods to be used. Decisions
made at the demand layer (DAL assignment, constraints, intended function)
directly populate PSAC sections. Treating PSAC preparation as a separate
activity from demand governance creates duplication and inconsistency; the
demand gate record and the PSAC should be aligned documents from the start.

---

## ASDLC Layer 3 — Release & Deployment Regulatory Requirements (Aviation)

The release layer ([release-governance.md](../release-governance.md))
governs the transition from loop-complete to production-deployed. For
aviation software in DO-178C scope, the Release Gate has eight conditions
(canonical enumeration in
[governance/gate-registry.md](../governance/gate-registry.md)); these
conditions address the engineering quality dimension of this transition,
but the certification dimension imposes additional expectations that must
be met before a release is considered airworthiness-ready. ASDLC's
evidence bundle is structurally consistent with the DO-178C lifecycle data
set but does not by itself produce all DO-178C / DO-330 / DO-333 lifecycle
artefacts (in particular: the Software Accomplishment Summary (SAS), the
Software Configuration Index (SCI), the Plan for Software Aspects of
Certification (PSAC), and qualified-tool documentation under DO-330 are
artefacts the certification programme must produce alongside ASDLC).

**DO-178C § 7 — Software Configuration Management at release.** DO-178C § 7
requires complete configuration control of software at release: the
software must be identified by a unique configuration identifier, all
lifecycle data associated with the release must be baselined, and the
software configuration index must document the exact versions of all
software components, tools, and associated data. The deployment
governance's configuration state hash supports compliance with the
configuration-identification expectation, and the SBOM generated at
release is structurally consistent with the DO-178C Software
Configuration Index. For certified airborne software, the configuration
state hash and SBOM together produce evidence aligned with § 7
configuration identification expectations; the release artefact must
include or reference these documents before the Release Gate closes.
ASDLC supports the artefact pipeline; DO-178C § 7 compliance is
established with the certification authority on the basis of the
artefacts produced.

**DO-178C Software Lifecycle Data.** DO-178C requires that specific
lifecycle data artefacts exist at release, including the Software
Accomplishment Summary (SAS), the Software Configuration Index (SCI), and
the problem report status for the released software. The evidence bundle
from the engineering loop — evaluation reports, trace IDs, policy check
outputs, dependency manifest — must include or reference all required
DO-178C lifecycle data artefacts. ASDLC alone does not produce the SAS or
the SCI; these are certification-programme artefacts that consume ASDLC
evidence. The SAS is the primary document through which the applicant
demonstrates to the certification authority that the software development
process satisfied all applicable DO-178C objectives. Producing an SAS that
is consistent with the engineering loop's evidence bundle, rather than
prepared independently, helps ensure that the SAS reflects the actual
development record. For higher DAL programs, the SAS must be reviewed by
the DER or ODA unit member before the Release Gate closes — the DER /
ODA credential is a specific certification credential that ASDLC's RG-2
"independent validator" condition does not by itself confer; the
organisation must engage a credentialed DER or ODA unit member separately.

**DO-178C § 6.4 — Independent verification for higher DAL systems.** For
DAL A and B software, DO-178C requires that verification activities are
performed with independence from the development team: the people who
developed the software are not the same people who perform the
verification. The Release Gate condition RG-2 (Independent Validation
Passed) supports compliance with the DO-178C § 6.4 independence
expectation at the release boundary, and the four falsifiable
"organisationally separate" criteria in
[release-governance.md](../release-governance.md) Condition 2 are the
mechanism. For DAL B and above programs, the independent validator must
be identifiable in the release artefact as a named individual who is
organisationally separate from the development team, and the scope of
the independent review must be documented. RG-2 does not by itself
confer the DER credential or the ODA-unit-member status that DO-178C and
FAA Order 8110.49 require for the verifier in higher-DAL programs where
applicable; the credential requirement is a specific certification
credential that must be confirmed separately by the organisation. A release that
proceeds to the certification authority without demonstrable
verification independence — and, where required, without DER or ODA
credentialing — does not produce evidence aligned with DO-178C DAL A or
DAL B expectations.

**EASA CS-25 / FAA Part 25 — Change impact analysis.** For software changes
to certified aircraft systems, EASA CS-25 (or FAA Part 25 for transport
aircraft) requires that change impact analysis is performed before the
release is approved: the applicant must demonstrate that the change does
not adversely affect the certification basis of the type or supplemental
type certificate. RG-5 (Compliance Documentation Complete) must reference
the change impact analysis for any change to software on a certified
aircraft. Change impact analysis is not a post-release activity; it is a
precondition for the release authorisation. For minor changes under DO-178C's
delta approach (§ 12.1), the change impact analysis determines which
objectives require new evidence and which are inherited — this
determination must be documented in the release artefact.

**Certification authority notification.** For programs where the certification
authority has an open PSAC or is actively reviewing software development,
material changes to the development approach — including the introduction of
agentic engineering practices — should be coordinated with the authority before
the release rather than after. This is not a release gate condition in the
general sense, but it is a condition for programs with active FAA DER oversight
or EASA CRI. Issue papers or CRIs related to the agentic development approach
must be closed or agreed to be deferred before a release proceeds under a
certification program.

---

## ASDLC Layer 4 — Operations & Maintenance Regulatory Requirements (Aviation)

The operations and maintenance layer
([operations/governance.md](../operations/governance.md),
[maintenance-governance.md](../maintenance-governance.md)) governs the system
from production deployment through decommission. For airborne software and
ground-based CNS/ATM systems, this layer carries continued airworthiness
obligations that persist for the operational life of the aircraft or system —
potentially decades.

**DO-178C § 7.3 — Configuration management through the operational
lifecycle.** DO-178C § 7.3 requires that configuration management extends
through the operational lifecycle of the airborne software: changes to
software in service must be configuration-controlled, problem reports
must be tracked and resolved, and the software configuration identity
must be maintained. The ASDLC stewardship model
([maintenance-governance.md](../maintenance-governance.md)) and the
maintenance governance configuration controls support compliance with this
expectation. The named system steward, the SBOM maintenance process, and
the change record requirement operationalise § 7.3 expectations at the
engineering layer. A system without a named steward responsible for
configuration currency does not produce evidence aligned with § 7.3 for
software in DO-178C scope.

**FAA Problem Reporting and Change Control — Field problem management.**
FAA expectations and DO-178C § 7.2 require a documented process for
identifying, tracking, and resolving software problems discovered in the
field after certification. This includes problem classification (whether
the problem constitutes a safety-relevant defect or a non-safety defect),
traceability of the problem to the relevant lifecycle data, and tracking
through resolution. The incident management process in operations
governance — including the quality incident classification and the
requirement that quality incidents produce a specification or evaluation
update — supports compliance with the FAA problem reporting expectation.
For certified systems, quality incidents that affect the software's
certified functions must be reported through the problem reporting
system, and the resolution must be managed as a DO-178C change (with
appropriate CM controls and, for safety-relevant problems, coordination
with the certification authority).

**DO-178C Software Lifecycle Data retention.** Software lifecycle data must be
retained for the operational life of the aircraft. For commercial transport
aircraft, this may be 30 to 50 years after the last aircraft of a type is
retired from service — substantially longer than standard enterprise software
retention periods. The ASDLC trace retention policy must be configured with the
applicable aircraft service life in mind, not with a default technology
retention period. For software components whose certification basis includes
DO-178C lifecycle data, the evidence bundle, the evaluation reports, and the
specification artefacts are part of the software lifecycle data and must be
retained for the aircraft's service life. Organisations that plan for a 7-year
retention default and then discover a 40-year aircraft service life obligation
have a significant governance gap to close.

**EASA Part-21 / FAA Part 21 — Continued airworthiness for certified changes.**
Changes to the software of a certified aircraft system must be approved through
the applicable change approval process — a minor change or a major change
approval under EASA Part 21 or FAA Part 21 — before installation in the
certified aircraft. The maintenance governance patch management process
([maintenance-governance.md](../maintenance-governance.md)) requires that
patches go through the agentic loop as specifications. For certified systems,
this loop must include the Part 21 change approval process as a governance gate
before the patched software enters service. A security patch that has been
technically verified but not approved under Part 21 cannot be installed in a
certified aircraft, regardless of its technical quality. The compliance
documentation condition in the release gate must include Part 21 approval
evidence for all changes to certified aircraft software.

**ITAR/EAR and long-term data residency.** For avionics software subject to ITAR
(22 CFR 120-130) or EAR export controls, the trace retention and lifecycle data
retention obligations must be managed within the ITAR-compliant boundary
throughout the retention period. Data migration or format conversion during the
retention period must not move controlled technical data outside the compliant
boundary. Organisations that retain lifecycle data for 30+ years must plan for
technology migrations (format obsolescence, storage platform transitions) that
keep the data accessible without violating export control requirements. This
should be addressed in the maintenance governance record at deployment time, not
discovered when the first technology migration is required.
