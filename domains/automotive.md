# ASDLC Domain Guidance — Automotive

_Automotive-specific regulatory requirements for ASDLC Layers 1, 3, and 4._

See [Automotive Manifesto Alignment](../../domains/automotive.md) for
manifesto principle mappings (ISO 26262, ASPICE, UN Regulation 157). See
the [ASDLC Overview](../asdlc.md) for the full lifecycle framework. See
[governance/gate-registry.md](../governance/gate-registry.md) for the
canonical gate condition enumeration referenced throughout this file.

> **Conformance profile expectation.** Organisations operating in this
> regulated context typically claim the ASDLC-Regulated conformance
> profile (see [conformance-profiles.md](../conformance-profiles.md)).
>
> **Scope of regulatory claims.** This file maps ASDLC controls to
> automotive regulatory obligations. Throughout, "supports compliance
> with", "operationalises", and "produces evidence aligned with" are used
> in preference to "is" or "satisfies" because ASDLC alone does not
> directly produce all ISO 26262, SOTIF (ISO 21448), ASPICE, or UNECE
> WP.29 lifecycle artefacts. ASDLC artefacts contribute to a compliance
> posture that the organisation must complete with safety-case
> documentation, ASPICE process records, SOTIF triggering-condition
> registries, and UNECE WP.29 R155/R156 management-system descriptions.
> Specific limits — including the SOTIF formal feedback-loop requirement
> that exceeds ASDLC's L4→L1/L4→L2 mechanics — are flagged in each
> section.

---

## ASDLC Layer 1 — Demand & Value Regulatory Requirements (Automotive)

The demand layer of the ASDLC ([demand/value.md](../demand/value.md)) governs
what enters the engineering execution loop. In automotive development contexts,
ISO 26262 and SOTIF impose concept-phase obligations that must be completed
before software development begins.

**ISO 26262 Part 3 — Concept Phase and ASIL determination.** ISO 26262
Part 3 requires that an item definition, Hazard Analysis and Risk
Assessment (HARA), and safety goals be established at the concept phase,
before software development starts. The HARA determines the ASIL — the
single most consequential constraint on the engineering loop's governance
— for each safety function. The Specification Readiness Gate conditions
SR-6 (Blast Radius Assessed) and SR-4 (Constraints Identified) — see
[governance/gate-registry.md](../governance/gate-registry.md) — must
include ASIL determination for any specification that touches a safety-
relevant function. A specification that enters the loop without a
confirmed ASIL assignment lacks the governing constraint for all
subsequent engineering decisions: verification depth, tool confidence
level, independence requirements, and autonomy-tier-ceiling (autonomy
tier 1 / 2 / 3 / 4) are all determined by ASIL. The demand layer must not
release a safety-relevant specification into the loop until the HARA
output and the resulting ASIL allocation are documented and agreed.
SR-4 / SR-6 support compliance with the concept-phase expectation; ASDLC
does not produce the HARA itself.

**ISO 26262 Part 8.6 — Software Requirements Specification traceability.**
ISO 26262 Part 8.6 requires that software requirements are traceable to
the system requirements from which they were derived, and that the
derivation is documented. The demand-to-specification bridge's
translation step — from validated business need to machine-readable
acceptance criteria — supports compliance with this expectation. The
Specification Readiness Gate condition SR-3 (Acceptance Criteria
Expressible) must demonstrate that each software requirement in the
specification traces to a system-level requirement or safety goal before
the specification enters the loop. Traceability established during the
loop is not sufficient: the traceability chain must be demonstrable at
specification entry. This is the difference between traceability as an
engineering output (DO-178C approach) and traceability as a precondition
for engineering (ISO 26262 approach).

**SOTIF (ISO 21448) — Performance limitations and triggering conditions
at concept stage.** For ADAS and automated driving functions subject to
ISO 21448, the concept stage must identify performance limitations and
triggering conditions — the scenarios where the system may fail or
behave inadequately despite having no fault. The Specification Readiness
Gate condition SR-4 (Constraints Identified) must include SOTIF
triggering-condition analysis for any specification affecting an ADAS or
AV function; SR-4 supports compliance with the concept-stage SOTIF
expectation. Triggering conditions discovered after the loop has started
require loop restart if they affect the specification's scope or
acceptance criteria. Discovering SOTIF triggering conditions during
system integration testing — after all software development and unit
verification is complete — is a demand-layer governance failure.

**UNECE WP.29 R155 — Cybersecurity risk assessment at concept stage.** UN
Regulation 155 (UNECE WP.29 R155) requires that cybersecurity risk
assessment is integrated into the development lifecycle from the concept
stage. For road vehicles subject to R155, the Cybersecurity Management
System (CSMS) must be in place and the cybersecurity risk assessment for
the item must begin at the concept stage. The Specification Readiness
Gate condition SR-4 (Constraints Identified) must include the WP.29
cybersecurity risk assessment output — specifically, the Threat Analysis
and Risk Assessment (TARA) results for the function being specified.
SR-4 supports compliance with the R155 concept-stage expectation; a
specification for a connectivity-relevant automotive function that
enters the loop without a completed TARA does not produce evidence
aligned with R155 at the demand gate.

**Capacity model and ASIL-rated concurrent initiatives.** The demand layer's
capacity model must account for the governance overhead of ASIL-rated functions.
An organisation attempting to run multiple concurrent ASIL D or ASIL C
development initiatives will encounter governance bottlenecks at the independent
reviewer capacity: qualified functional safety engineers capable of performing
independent verification are scarce, and their review capacity constrains how
many ASIL-rated loop iterations can be governed simultaneously. The demand
backlog prioritisation must explicitly model this constraint; an oversubscribed
ASIL-rated loop is not a loop quality problem — it is a demand layer governance
failure.

---

## ASDLC Layer 3 — Release & Deployment Regulatory Requirements (Automotive)

The release layer ([release-governance.md](../release-governance.md))
governs the transition from loop-complete to production-deployed. The
Release Gate has eight conditions (canonical enumeration in
[governance/gate-registry.md](../governance/gate-registry.md)). In
automotive development, release governance intersects with ISO 26262
product development expectations and, for production vehicles, with the
UNECE WP.29 Software Update Management System (SUMS) regulation; ASDLC
supports compliance with these regimes but does not by itself satisfy
them.

**ISO 26262 Part 8.3 — Configuration Management at release.** ISO 26262
Part 8.3 requires that software releases are configuration-controlled
and that all released artefacts are traceable. The software release must
be uniquely identified, the development and verification artefacts must
be baselined at the release point, and the configuration state must be
documented. The deployment governance's configuration state hash supports
compliance with the configuration-identification expectation, and the
evidence bundle's version references (specification version, evaluation
suite version, dependency manifest) constitute a configuration baseline
aligned with Part 8.3 expectations. For ASIL-relevant releases, the
configuration state hash and the evidence bundle together produce
evidence aligned with the ISO 26262 CM release record. Both must be
present and consistent before the Release Gate closes.

**UNECE WP.29 R156 — Software Update Management System (SUMS).** UN
Regulation 156 requires that vehicle manufacturers establish a Software
Update Management System capable of managing over-the-air software
updates safely. SUMS expectations include: documentation of the change
and its impact, verification that the update does not introduce new
risks, a rollback capability, and post-update verification that the
system performs as expected. The ASDLC release governance and deployment
governance ([release-governance.md](../release-governance.md)) support
compliance with SUMS expectations. Specifically: the evidence bundle
operationalises the change documentation and impact assessment, RG-3
(Rollback Procedure Tested) operationalises the SUMS rollback capability,
and the production smoke tests support the post-update verification. For
OTA-capable vehicles in R156 scope, the ASDLC release process supports
the SUMS release process; the SUMS description submitted with the
vehicle type approval must reference ASDLC as the engineering-layer
implementation, with the manufacturer's organisation-level SUMS
governance documented separately.

**ISO 26262 Parts 5 and 6 — Safety manager review for ASIL B and above.**
ISO 26262 § 5 and § 6 require that the safety manager or a designated
qualified safety professional reviews releases for safety-relevant
functions at ASIL B and above. RG-4 (Accountable Human Sign-Off) must
include safety manager review for all ASIL B, C, and D functions. The
safety manager's review is not the same as the tech lead's release
approval: the safety manager confirms that the evidence bundle
demonstrates satisfaction of the safety goals allocated to this software,
that the ASIL constraints were maintained throughout development, and
that no known safety issue is present in the release. A release that has
tech lead approval but no safety manager review for an ASIL B+ function
does not produce evidence aligned with ISO 26262 expectations.

**ASPICE — Release management process.** Automotive SPICE (ASPICE)
requires a documented software release management process (SUP.8) with
defined release criteria. The ASDLC release Definition of Done supports
compliance with ASPICE release-criteria expectations: the evidence
bundle aligns with SUP.8's release documentation, RG-4 (Accountable
Human Sign-Off) operationalises SUP.8's release authorisation, and the
configuration baseline aligns with SUP.8's configuration-management
obligations. For OEM programs that mandate ASPICE assessment, the ASDLC
release governance documentation must be structured to align with
ASPICE SUP.8 assessment criteria. Assessors will look for: documented
release criteria that were applied, evidence that the criteria were
satisfied, named individuals who authorised the release, and
traceability between the released software version and the development
and verification artefacts. ASDLC supplies these inputs; the ASPICE
assessment itself is conducted by ASPICE-qualified assessors against the
process records the organisation maintains.

**Emergency change and safety manager coordination.** The emergency change
procedure ([release-governance.md](../release-governance.md)) — which allows
certain governance steps to be deferred — does not waive the safety manager
review for ASIL B and above functions. Safety review is in the category of
obligations that cannot be deferred under the emergency procedure. An emergency
patch to an ASIL D function that bypasses safety manager review is not a
governed emergency — it is an ungoverned change to a safety-critical system. The
emergency procedure for ASIL-relevant functions must include a provision for
accelerated safety manager review, not elimination of it.

---

## ASDLC Layer 4 — Operations & Maintenance Regulatory Requirements

(Automotive)

The operations and maintenance layer
([operations/governance.md](../operations/governance.md),
[maintenance-governance.md](../maintenance-governance.md)) governs the system
from production deployment through the end of the vehicle's operational life.
Automotive regulatory obligations at this layer span functional safety
monitoring, SOTIF field learning, cybersecurity operations, and — for ASIL-rated
systems — decommissioning safety requirements.

**ISO 26262 Part 7 — Production and Operation Phase.** ISO 26262 Part 7
requires that the operational phase includes monitoring of field
behaviour against safety goals, a process for managing field reports of
safety-relevant incidents, and a mechanism for initiating corrective
actions when safety goals are at risk. The ASDLC output quality rate
SLO and the steward's ongoing monitoring responsibilities support
compliance with the Part 7 field-monitoring expectation. Specifically:
the output quality SLO must include acceptance criteria derived from
the safety goals (not only from functional requirements), quality
incidents that affect safety-relevant outputs must be escalated to the
safety manager and logged as potential Part 7 field incidents, and the
steward's quarterly review must assess whether the safety goals are
still being met. An output quality degradation that falls below the
safety-goal-derived floor is a Part 7 field incident, not only an
engineering quality issue.

**SOTIF (ISO 21448) — Field monitoring for triggering conditions.** ISO
21448 requires systematic collection and analysis of operational data
to identify triggering conditions discovered in the field that were not
anticipated at the concept stage. ISO 21448 imposes formal feedback-loop
expectations: identified triggering conditions must be assessed,
classified, integrated into the verification and validation portfolio
where appropriate, and tracked through resolution. The quality incident
classification in operations governance must include a SOTIF incident
type: an incident where the system behaved inadequately (not due to a
fault, but due to an unanticipated triggering condition) is a SOTIF
field finding. ASDLC's L4→L1 and L4→L2 feedback paths support
compliance with the ISO 21448 feedback-loop expectation by routing SOTIF
field findings back to the demand layer (Layer 1) as validated evidence
of new requirements: the triggering condition becomes a constraint that
must be addressed in the next relevant specification. ASDLC's feedback
mechanics support the loop but do not by themselves produce the
ISO 21448-prescribed triggering-condition registry, the assessment
record, or the verification-and-validation portfolio update; these are
SOTIF artefacts that consume ASDLC feedback signals and must be produced
alongside ASDLC. An operations layer that classifies SOTIF field
findings as generic quality incidents, without routing them back to the
demand layer, breaks the feedback loop that ISO 21448 expects.

**UNECE WP.29 R155 — Cybersecurity operations.** R155 requires that the
vehicle manufacturer's CSMS includes ongoing monitoring for
cybersecurity threats and vulnerabilities, a process for assessing the
risk of newly discovered vulnerabilities to deployed vehicles, and a
mechanism for deploying software updates to address cybersecurity risks.
The ASDLC maintenance governance's security patch management
([maintenance-governance.md](../maintenance-governance.md)) — including
CVSS-tiered SLOs, SBOM maintenance, and automated dependency
vulnerability scanning — supports compliance with R155 cybersecurity
monitoring expectations. For production vehicles, the patch time-to-
deploy SLOs must be calibrated to R155's cybersecurity risk management
expectations: a CVSS 9.0+ vulnerability in vehicle software may require
faster remediation than the 48-hour default if the vulnerability is
exploitable in the vehicle's deployed operating environment. The CSMS
documentation should reference the ASDLC patch SLOs as the engineering-
layer implementation supporting R155 vulnerability-management
obligations.

**ISO 26262 — Decommissioning safety requirements.** ISO 26262 Part 7 requires
that the decommissioning of safety-relevant software is managed to prevent
unsafe states: the removal of a safety function must not leave the vehicle in a
state that violates its safety goals. The ASDLC deprecation and decommission
process ([maintenance-governance.md](../maintenance-governance.md)) must include
a safety impact assessment for all ASIL-rated systems before the deprecation
decision is finalised. The safety impact assessment must answer: does
decommissioning this function affect any safety goal? Is there a replacement
function that provides equivalent or better safety coverage? What is the vehicle
state during the transition from the deprecated function to its replacement? The
safety manager must review and approve the decommission plan for ASIL-relevant
functions before the deprecation notice is issued.
