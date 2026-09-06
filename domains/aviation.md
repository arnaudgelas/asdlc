# ASDLC Domain Guidance — Aviation

_Aviation-specific regulatory requirements for ASDLC Layers 1, 3, and 4._

See [Aviation Manifesto Alignment](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/domains/aviation.md) for manifesto
principle mappings (DO-178C, DO-330, DO-333, ARP 4754A, DO-326A). See the
[ASDLC Overview](../asdlc.md) for the full lifecycle framework.

**Note on DO-178C's register.** **DO-178C is a paid RTCA standard that this
programme has not purchased and has not read.** It is **OPEN under `T6.5`**, and
**no unofficial copy was fetched, sought or considered**. Per `asdlc.md`,
*"nothing here asserts what they require."* Every DO-178C mapping in this file —
including every section number, which is reproduced from secondary usage — is
therefore **the ASDLC's own construction and is unsourced**: what the ASDLC
understands the industry-common airborne-certification vocabulary to mean, not a
reading of the standard. **Whether DO-178C states any of it, and whether the
section numbers carry the content stated, has not been checked and cannot be
while the standard is unread.** Confirm against a purchased copy, and against
the programme's own certification basis agreed with the certification authority,
before relying on any of it. The controls themselves stand as ASDLC controls;
only the attribution is withdrawn. The instruments cited in this file that are
**not** paid — FAA Order 8110.49A, and the EASA and FAA parts — are marked
separately where they appear.

---

## ASDLC Layer 1 — Demand & Value Regulatory Requirements (Aviation)

The demand layer of the ASDLC ([demand/value.md](../demand/value.md)) governs
what enters the engineering execution loop. In aviation development contexts,
demand governance must integrate with the system-level processes established by
ARP 4754A before any software development activity starts.

**Requirements traceability at the demand boundary.** **The ASDLC's own rule,
not a reading of DO-178C or DO-330:** every software requirement should be
traceable to a system requirement, and no software requirement should exist
without a parent system requirement. The
demand-to-specification bridge's translation step — from validated business need
to machine-readable acceptance criteria — is the control that establishes this
traceability. The "acceptance criteria expressible" gate condition must
demonstrate that the derived software requirement traces to an identifiable
system-level requirement or allocated function before the specification enters
the loop. A specification that cannot demonstrate this traceability at the
demand gate will not carry the traceability record a certification programme is
assembled from. **The ASDLC associates this with DO-178C § 5.1; whether § 5.1
states it has not been checked and cannot be while the standard is unread.**

**ARP 4754A — System requirements validation preceding software development.**
ARP 4754A § 5 (System Requirements) requires that system requirements are
validated before software development starts: that they are complete, correct,
and consistent, and that they satisfy the intent of the higher-level
requirements from which they were derived. The specification readiness gate's
"business need validated" condition maps to ARP 4754A's system requirements
validation process at the software entry point. An engineering team that begins
software development before the system requirements have been through ARP 4754A
validation is not compliant with the development process that generates the DAL
assignment on which the team is relying.

**Design Assurance Level (DAL) determination.** **The ASDLC's own placement, not
a reading of DO-178C:** the DAL should be determined at the start of the
software development activity, before the loop begins, not during or after
development. The specification readiness gate's "blast radius assessed" and
"constraints identified" conditions are the ASDLC's engineering controls for DAL
determination: they require that the safety significance of the function is
established and that whichever DO-178C objectives the programme's certification
basis makes applicable at that DAL — including any independence expected at
higher levels — are identified as constraints on the loop. **What DO-178C
assigns to each DAL has not been checked here.** A specification that enters the loop
without a confirmed DAL assignment lacks its most fundamental governance
constraint.

**FAA Order 8110.49A — what the order governs.** FAA Order 8110.49A, *Software
Approval Guidelines*, effective 29 March 2018, "guides Aircraft Certification
Service (AIR) offices and designees on how to apply RTCA/DO-178B and
RTCA/DO-178C" for approving software used in airborne computers (Ch. 1 ¶1,
*Purpose*). It is direction to FAA certification staff and designees rather than
a documentation requirement imposed on an applicant, and since it cancelled
Order 8110.49 Chg 2 and deleted that order's Chapters 5–16 it retains only a
software review process (Ch. 2), software conformity inspection (Ch. 4) and the
level-of-involvement worksheets (App. A) [claim corrected 2026-09-05: this
paragraph previously asserted that "Software approval under FAA Order 8110.49
requires documentation of the software's intended function, its operating
environment, and its relationship to the airborne system's safety objectives,"
and routed that documentation into the PSAC. Against Order 8110.49A as retrieved
from faa.gov on 2026-09-05 and hashed at
`inputs/20260905-arnaud/prep/q11-federal/sources/faa-order-8110.49.pdf`, the word
"intended" occurs zero times in the order and "PSAC" occurs zero times. PSAC
content is specified by RTCA/DO-178C § 11.1 — a paid RTCA standard that was not
retrieved, is OPEN under `T6.5`, and for which no unofficial copy was fetched,
sought or considered. `[PREPARED AT PRIMARY, UNSIGNED]` — see
`inputs/20260905-arnaud/prep/q11-federal/q11_federal_packet.md`]. The demand
layer's value definition and business need documentation remain the inputs a
programme needs at PSAC preparation time: the success criterion and the
system-level justification for the software function — Layer 1 governance
artefacts — are what the intended-function statement in the PSAC is written
from, and teams that do not govern demand rigorously at Layer 1 will find that
statement incomplete or inconsistent when the PSAC is prepared. The obligation
they are measured against there is DO-178C's, not this order's.

**PSAC framing at the demand stage.** The Plan for Software Aspects of
Certification — the primary planning document for DO-178C programs — should be
initiated in parallel with the demand layer governance for significant software
developments. **On the ASDLC's understanding — § 11.1 is unread, see the note at
the head of this file —** the PSAC captures the software's intended function,
its DAL, the lifecycle standards, and the development tools and methods to be
used. Decisions
made at the demand layer (DAL assignment, constraints, intended function)
directly populate PSAC sections. Treating PSAC preparation as a separate
activity from demand governance creates duplication and inconsistency; the
demand gate record and the PSAC should be aligned documents from the start.

---

## ASDLC Layer 3 — Release & Deployment Regulatory Requirements (Aviation)

The release layer ([release-governance.md](../release-governance.md)) governs
the transition from loop-complete to production-deployed. For aviation software
in DO-178C scope, the eight release gate conditions address the engineering
quality dimension of this transition, but the certification dimension imposes
additional requirements that must be met before a release is considered
airworthiness-ready.

**Software Configuration Management at release.** **The ASDLC's own construction,
associated with DO-178C § 7 but not checked against it:** complete configuration
control of software at release — the software identified by a unique
configuration identifier, all lifecycle data associated with the release
baselined, and a software configuration index documenting the exact versions of
all software components, tools, and associated data. The deployment governance's configuration state hash is the
engineering control, and the SBOM generated at release maps to the DO-178C
software configuration index. For certified airborne software, the ASDLC
requires the configuration state hash and SBOM together to carry the
configuration identification it associates with § 7, and requires the release
artefact to include or reference these documents before the release gate closes.
**Whether that satisfies § 7 as written is not determined here.**

**Software Lifecycle Data.** **The ASDLC's own construction, not a reading of
DO-178C:** specific lifecycle data artefacts should exist at release, on the
ASDLC's understanding of the industry-common vocabulary including the Software
Accomplishment Summary (SAS), the Software Configuration Index (SCI), and the
problem report status for the released software. The evidence bundle from the engineering loop —
evaluation reports, trace IDs, policy check outputs, dependency manifest — must
include or reference all required DO-178C lifecycle data artefacts. The SAS is
the document through which, as the ASDLC understands the practice, an applicant
demonstrates to the certification authority that the software development
process satisfied the applicable DO-178C objectives. Producing an SAS that is consistent with the
engineering loop's evidence bundle, rather than prepared independently, ensures
that the SAS reflects the actual development record. For higher DAL programs,
the SAS must be reviewed by the DER or ODA unit member before the release gate
closes.

**Independent verification for higher DAL systems.** **The ASDLC's own rule for
its highest risk classes, associated with DO-178C § 6.4 but not checked against
it:** for DAL A and B software, verification activities should be performed with
independence from the development team — the people who developed the software
are not the same people who perform the verification. The release gate's
"independent validation passed" condition is where the ASDLC places that
independence at the release boundary. For DAL B and above programs, the
independent validator must be identifiable in the release artefact as a named
individual who is organisationally separate from the development team, and the
scope of the independent review must be documented. A release that proceeds to
the certification authority without demonstrable verification independence
fails this ASDLC condition; **whether it is also non-compliant with DO-178C at
DAL A or B is a determination for the certification authority, and is not made
here.**

**EASA CS-25 / FAA Part 25 — Change impact analysis.** For software changes to
certified aircraft systems, EASA CS-25 (or FAA Part 25 for transport aircraft)
requires that change impact analysis is performed before the release is
approved: the applicant must demonstrate that the change does not adversely
affect the certification basis of the type or supplemental type certificate. The
release gate's "compliance documentation complete" condition must include the
change impact analysis for any change to software on a certified aircraft.
Change impact analysis is not a post-release activity; it is a precondition for
the release authorisation. Where a programme takes a delta approach to a minor
change — the ASDLC associates this with DO-178C § 12.1 and has not checked it —
the change impact analysis determines which objectives need new evidence and
which are inherited, and the ASDLC requires that determination to be documented
in the release artefact.

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

**Configuration management through the operational lifecycle.** **The ASDLC's own
construction, associated with DO-178C § 7.3 but not checked against it:**
configuration management extends through the operational lifecycle of the
airborne software — changes to software in service are configuration-controlled,
problem reports are tracked and resolved, and the software configuration
identity is maintained. The ASDLC
stewardship model ([maintenance-governance.md](../maintenance-governance.md))
and the maintenance governance configuration controls map directly to this
requirement. The named system steward, the SBOM maintenance process, and the
change record requirement are the operational instruments for § 7.3 compliance.
A system without a named steward responsible for configuration currency does not
meet this ASDLC control; **whether it is also non-compliant with § 7.3 is not
determined here.**

**Field problem management.** **The ASDLC's own control, associated with FAA
problem-reporting practice and DO-178C § 7.2 and checked against neither:** a
documented process for identifying, tracking, and resolving software problems
discovered in the field after certification. This includes problem classification (whether the problem
constitutes a safety-relevant defect or a non-safety defect), traceability of
the problem to the relevant lifecycle data, and tracking through resolution. The
incident management process in operations governance — including the quality
incident classification and the requirement that quality incidents produce a
specification or evaluation update — maps to the FAA problem reporting
requirement. For certified systems, quality incidents that affect the software's
certified functions must be reported through the problem reporting system, and
the resolution must be managed as a DO-178C change (with appropriate CM controls
and, for safety-relevant problems, coordination with the certification
authority).

**Software lifecycle data retention.** **The ASDLC's own retention rule, not a
reading of DO-178C:** software lifecycle data should be retained for the
operational life of the aircraft. For commercial transport
aircraft, this may be 30 to 50 years after the last aircraft of a type is
retired from service — substantially longer than standard enterprise software
retention periods. The ASDLC trace retention policy must be configured with the
applicable aircraft service life in mind, not with a default technology
retention period. For software components whose certification basis includes
DO-178C lifecycle data, the evidence bundle, the evaluation reports, and the
specification artefacts are part of the software lifecycle data and must be
retained for the aircraft's service life. Organisations that plan for a 7-year retention default and then discover a 40-year aircraft service life obligation — an illustrative contrast, not figures this document sets —
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
