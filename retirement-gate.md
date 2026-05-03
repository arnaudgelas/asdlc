# Retirement Gate

_The fourth gate of the Agentic Software Delivery Lifecycle. Boundary:
Layer 4 → end-of-life. The gate that governs the controlled, documented
removal of a system from production._

See [asdlc.md](asdlc.md) for the four-layer model and the three gates that
precede this one (Specification Readiness, Release, and Operational Readiness;
the Retirement Gate described here is the fourth and final gate). See [governance/gate-registry.md](governance/gate-registry.md)
for the canonical condition enumeration. See
[maintenance-governance.md](maintenance-governance.md) for the operational
lifecycle that leads into retirement.

---

## What is the Retirement Gate?

The Retirement Gate is the structured assessment that governs a system's
exit from production. It is the boundary between Layer 4 (Operations &
Maintenance) and end-of-life. A system that is decommissioned without
passing this gate has not been retired; it has been abandoned. The
distinction matters because retirement obligations do not end at the
moment a service stops accepting traffic. Records, claims, dependency
notifications, accountability transfers, and cost zero-outs persist as
obligations until they are explicitly discharged. A system whose service
endpoints are dark but whose retirement obligations are open is a system
in undefined operational state — and undefined operational state is the
state in which orphaned obligations and unresolved accountability accrue.

The primary question the Retirement Gate answers is: _Have all of the
system's persistent obligations been discharged or explicitly transferred
to a named successor, and is the retirement record complete enough to be
defensible against future enquiry?_

Primary stakeholder: the System Steward at the time of retirement, with
the named accountable human at the layer of authority appropriate to the
system's blast radius. Timescale: weeks. The gate is not a single meeting;
it is a structured process that produces the eight evidence artefacts
below over a defined retirement window.

---

## Pass conditions

The Retirement Gate has eight conditions. Conditions 1 through 4 and 6
through 8 are blocking for all systems. Condition 5 (IGM claim retraction)
is conditional, blocking only for systems that emitted claims into the
epistemic substrate governed under the Intelligence Governance Manifesto;
for systems not operating under IGM, Condition 5 is satisfied by attesting
that the condition does not apply.

A partial pass is a fail.

### 1. Stewardship handoff or termination

The accountable human for the system's ongoing residual obligations must
be identified, or the system must be formally retired with no successor
and no continuing residual obligations. The two cases are not equivalent
and must not be conflated. A system with no successor and continuing
residual obligations — for example, a deprecated reporting service whose
historical records remain subject to regulatory retention — has not been
retired; it has been split into a dark-service component and an ongoing-
obligation component, and the obligation component requires a named
accountable human.

The condition is satisfied by exactly one of:

- A named successor system or named accountable human, recorded in the
  retirement record, who has accepted the residual obligations and who
  has signed an acceptance attestation referencing the obligations
  enumerated in the retirement record.
- A formal termination attestation stating that no residual obligations
  remain — no records under retention, no dependency consumers, no
  outstanding claims, no remaining contractual commitments — and naming
  the human who attests that the absence is true.

### 2. Runbook archived and immutable

The final runbook version must be frozen, and the freeze must be made
auditable through a content hash recorded in the retirement record. A
runbook that is "archived" by being moved to a less-trafficked location is
not immutable: subsequent edits to that location are still possible. The
content hash is the operational mechanism by which post-retirement enquiry
can confirm that the runbook returned in archive matches the runbook as it
stood at retirement.

The condition requires:

- The final version of the runbook (including all DoD-1 components per
  [operations/dod.md](operations/dod.md)) is committed to a write-protected
  archive store.
- A content hash (SHA-256 or stronger) of the archived runbook is
  recorded in the retirement record.
- The retention period for the archived runbook is at least the retention
  period applicable under Condition 3 below; runbooks are retained for at
  least as long as the traces they reference.

### 3. Trace and reasoning-record archival

Reasoning traces and the records covered by the trace retention policy
(DoD-7) must be archived for the longer of:

- The organisation's records-retention schedule for the relevant data
  classification, and
- Any applicable regulatory mandate (financial-services records,
  healthcare records, defence records, model-risk records — each with its
  own retention floor).

Where data-subject-rights regimes (notably GDPR Art. 17 right-to-erasure
and CCPA right-to-delete) appear to conflict with retention mandates such
as SR 11-7 or the FINRA broker-dealer retention rules, the conflict must
be resolved with a documented decision, not deferred. The decision must
name the rights-holder claim and the retention obligation, identify the
controlling rule under the organisation's legal counsel's analysis, and
record which path the organisation has chosen along with the legal basis
for the choice.

The condition requires:

- A retention determination per data class within the system's traces and
  reasoning records.
- An archival mechanism appropriate to the determination: write-protected
  storage with retrieval testing, or compliant erasure with attestation,
  or both for partitioned data classes.
- A recorded decision for any conflict between deletion-right and
  retention-mandate, with the resolving legal basis named.

### 4. Model and prompt deprecation propagated

Every Agent, Model, and Prompt referenced by this system that has no
other consumer must be decommissioned in the governance graph. The
decommissioning must be propagated through the graph's `generated_by` edges
so that subsequent queries against the graph (see
[governance/graph.md](governance/graph.md)) can trace the deprecation
events to the retirement.

The condition requires:

- A query against the governance graph identifying every Agent, Model,
  and Prompt referenced by the retiring system.
- A second query identifying which of those have no other consumer.
- A deprecation event in the graph for each non-consumed artefact, with
  an edge to the retirement record.
- Verification that the consumer query was run after the system's actual
  decommissioning event, not before; pre-decommissioning queries can
  miss consumers that the system itself was concealing.

### 5. IGM claim retraction (where IGM is in use)

For systems operating under the Intelligence Governance Manifesto that
have emitted claims into the epistemic substrate, the retiring system's
claims must be:

- Retracted, where the claim was specific to the retiring system and no
  successor authority has assumed responsibility for it; or
- Refreshed by a successor authority, where a successor has assumed
  responsibility for keeping the claim current; or
- Explicitly preserved with a documented justification and a named
  accountable claim-keeper, where the claim is to remain in the
  substrate but the retiring system will no longer maintain it.

Structured feedback per IGM Principle 10 must be emitted to the
substrate's revision, assertion, and semantic authorities affected by the
retirement, with the retirement event itself as the engagement that
produces the feedback. See [annex-igm.md](annex-igm.md) for the IGM term
definitions referenced here.

For systems not operating under IGM, the condition is satisfied by an
attestation that no claims were emitted into a governed epistemic
substrate.

### 6. Dependency consumers notified

Any first-party system with a `depends_on` edge to the retiring system in
the governance graph must be notified of the retirement, given an SLO for
the notification window, and required to confirm the notification with a
recorded acknowledgement. Notification without confirmation is not
discharge: a notification email sent to a stale alias is indistinguishable
from no notification.

The condition requires:

- A query against the governance graph identifying every first-party
  consumer of the retiring system.
- A notification event per consumer, recorded in the retirement record.
- A confirmation event per consumer, recorded by a named human at the
  consumer's stewardship layer.
- An SLO for the consumer's response defined in advance of the
  notification (practitioner default: 20 business days for confirmation;
  longer windows where the consumer has substantive migration work to
  perform).

A consumer that does not confirm within the SLO is escalated to its
accountable human under the consumer's own governance; the escalation
event is recorded in the retiring system's retirement record.

### 7. FinOps zero-out

Cost attribution tags must be removed or transitioned, and a final cost
record must be filed. The condition exists because cost attribution that
persists after retirement produces a phantom: a tag that continues to
accumulate residual cost (often through retained logs, archive storage,
or background processes that did not actually stop) without a system to
which the cost can be charged.

The condition requires:

- A query against the FinOps cost attribution system identifying every
  cost tag referencing the retiring system.
- A determination per tag: removed (the cost stream has stopped) or
  transitioned (the cost stream continues against an archive or
  successor system and is now tagged accordingly).
- A final cost record covering the system's full operational lifetime,
  filed with the retirement record.
- A confirmation event 30 calendar days after retirement attesting that
  the cost stream has not unexpectedly resumed under any of the
  retired tags.

### 8. Final accountability sign-off

A named human with the authority to discharge residual risk must sign the
retirement record. The signature is not a clerical confirmation; it is a
substantive acceptance that the retirement has been conducted correctly
and that the named successor (or the standing residual-risk register) is
the appropriate destination for any obligation that survives retirement.
The signature transfers any continuing obligations to the named successor
or to the organisation's standing residual-risk register.

The signing authority must be at the layer of authority appropriate to
the retiring system's pre-retirement blast radius:

- BR1 systems: the System Steward signs.
- BR2 systems: the System Steward signs and the value-stream-level
  accountable human countersigns.
- BR3 systems: the System Steward signs and the portfolio-level
  accountable human (or LPM equivalent) countersigns.
- Tier 4 envelopes: the envelope steward signs and the AEnt-M escalation
  authority (where AEnt-M applies) or the envelope's named accountable
  human (where AEnt-M does not apply) countersigns.

The signature is recorded against a specific retirement record ID; an
unanchored signature does not satisfy the condition.

---

## Failure mode if bypassed

When the Retirement Gate is bypassed — when a system is decommissioned
without passing each of the conditions above — the failure modes are
specific and recurrent.

- **Orphaned systems.** A system whose service endpoints are dark but
  whose obligations are open. No one is accountable. Records may exist
  under retention but cannot be retrieved on enquiry because the
  retrieval path was never archived. Dependency consumers continue to
  reference an absent system and only discover the absence at next
  invocation.
- **Untraceable claims.** Claims emitted into the IGM substrate by the
  retired system remain in the substrate without a current authority.
  Subsequent agent action consumes the claims as if they were governed,
  but the governance is fictional: no authority refreshes them, retracts
  them, or accepts feedback against them.
- **Ghost dependencies.** First-party systems whose `depends_on` edges
  point at a retired system continue to reference it in the governance
  graph. Subsequent governance queries return inaccurate topology;
  decisions made on the basis of those queries — release-gate decisions,
  blast-radius assessments, lateral-learning propagation — are made
  against a misrepresentation of reality.
- **Retention-rights violations.** Records are retained beyond their
  retention period, or deletion-right requests cannot be honoured because
  the deletion path was decommissioned at retirement. Either failure is a
  regulatory exposure, not a process irregularity.

The Retirement Gate exists to prevent these failure modes. A retirement
that does not pass the gate has not prevented them; it has set them in
motion.

---

## Tier-conditioned variations

The gate's structure is the same across tiers; what changes is the unit
of retirement, the evidence required for some conditions, and the
signing authority for Condition 8.

### Tier 1, Tier 2, and Tier 3 (per-system retirement)

The unit of retirement is the system, and the conditions apply to the
system's own runbook, traces, claims, dependency edges, and cost tags.
The signing authority for Condition 8 follows the BR1 / BR2 / BR3
pattern enumerated above.

### Tier 4 (envelope retirement)

The unit of retirement is the policy envelope, not an individual deployment
within the envelope. An envelope retirement extends each condition as
follows:

- Condition 1 (Stewardship handoff or termination): the envelope steward
  hands off to a named successor envelope or attests that the envelope's
  authorised action classes have all been wound down. A partial wind-down
  — some action classes terminated, others handed off — must enumerate
  per-class status.
- Condition 2 (Runbook archived): the envelope's specification, the
  evaluation portfolio that validated the envelope, and the monitoring
  configuration are all archived as part of the runbook content; the
  hash covers the composite.
- Condition 4 (Model and prompt deprecation): the envelope's authorised
  agent configurations, including all foundation model versions ever
  pinned to the envelope, are decommissioned in the governance graph
  unless any are referenced by a successor envelope.
- Condition 5 (IGM claim retraction): the envelope's per-action-class
  intelligence constraints (see [annex-igm.md](annex-igm.md)) are
  retracted or transferred at the action-class granularity, not the
  envelope granularity.
- Condition 8 (Final accountability sign-off): the envelope steward
  signs and the AEnt-M escalation authority (where AEnt-M applies)
  countersigns; in the absence of AEnt-M, the envelope's named
  accountable human countersigns.

A Tier 4 envelope cannot be partially retired by deprecating some action
classes while leaving others active under an unchanged envelope
specification. Action-class-level deprecation within a continuing envelope
is an envelope specification change, not a retirement, and passes the
Release Gate as an envelope change (see `asdlc.md` Tier 4 in Layer 3) —
not the Retirement Gate.

---

## Relationship to other ASDLC documents

The Retirement Gate is the fourth gate in the canonical enumeration
maintained at [governance/gate-registry.md](governance/gate-registry.md).
The operational lifecycle that leads into retirement is governed by
[maintenance-governance.md](maintenance-governance.md); the present
document specifies the structured exit from that lifecycle. The
Operational Definition of Done in [operations/dod.md](operations/dod.md)
governs the conditions that must hold during operation; the Retirement
Gate governs the discharge of those conditions at exit. The IGM-claim-
retraction condition (RT-5) integrates with [annex-igm.md](annex-igm.md);
the Tier 4 envelope-retirement variation integrates with
[annex-aentm.md](annex-aentm.md). The conformance profiles in
[conformance-profiles.md](conformance-profiles.md) state which profiles
make the Retirement Gate a binding obligation; ASDLC-Tier4 in particular
makes Retirement Gate passage a profile-level conformance requirement.
