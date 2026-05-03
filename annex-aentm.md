# Annex — Tier 4 Operation with the Agentic Enterprise Manifesto (AEnt-M)

_An annex documenting how a Tier 4 ASDLC policy envelope operates when the
organisation also operates under the Agentic Enterprise Manifesto (AEnt-M).
This annex carries forward, in normative form, the Tier 4 relocation
mechanics that previously appeared inline in `asdlc.md`. It is normative for
organisations operating AEnt-M; for organisations not operating AEnt-M, see
the framework-agnostic Tier 4 envelope description in [asdlc.md](asdlc.md)._

See [asdlc.md](asdlc.md) for the four-layer model and the Tier 4 paragraphs
in each Layer section. See [release-governance.md](release-governance.md)
Condition 1 for the relocation evidence schema referenced below. See
[annex-igm.md](annex-igm.md) for the parallel IGM-specific annex.

---

## Scope

This annex is normative for organisations operating the Agentic Enterprise
Manifesto (AEnt-M) in concert with the ASDLC. AEnt-M defines a body of
governance machinery around relocation — the practice of replacing a
synchronous human control point with a structurally equivalent asynchronous
control objective, on demonstrated evidence of equivalence. ASDLC's Tier 4
envelope is the construct within which relocation is operationalised at the
delivery layer.

For organisations not operating AEnt-M, this annex is non-binding. The
framework-agnostic Tier 4 envelope content in `asdlc.md` — envelope
specification, machine enforcement, evaluation portfolio, monitoring — is
sufficient to govern Tier 4 operation in the absence of AEnt-M. AEnt-M adds
the relocation accountability machinery; this annex documents how that
machinery integrates with the ASDLC envelope.

Where this annex references AEnt-M concepts whose authoritative definition
lives in AEnt-M itself, the reference is explicit ("see AEnt-M § X"). Where
this annex restates an AEnt-M definition, the restatement is intended to be
faithful but is not authoritative; AEnt-M governs the meaning of its own
terms.

---

## AEnt-M terms used in this annex

The following terms are used in this annex with the meanings stated below.
Where AEnt-M is the authoritative source, the reference is given.

- **Relocation.** The replacement of a synchronous human control point by
  an asynchronous control objective whose effect is structurally equivalent
  to the synchronous control. Relocation is a governed transition, not a
  removal: the control objective itself does not change; only its placement
  in the operating timeline changes. See AEnt-M for the full relocation
  doctrine and the per-decision evidence schema.
- **Asynchronous control objective.** A control whose discharge is
  observable post hoc through monitoring, sampling, audit, or reconstruction
  rather than by gating an action at the moment of execution. The
  asynchronous control objective replaces the synchronous gate but produces
  evidence of equivalent strength. See AEnt-M for the asynchronous-control
  patterns and the equivalence-test guidance.
- **Demonstrated equivalence.** Empirical evidence — typically including a
  decision-quality baseline, an error-detection comparison, an audit-
  reconstructability validation, and a degradation-response test — that
  the asynchronous control objective performs at least as well as the
  synchronous baseline against the AEnt-M Principle 7 metrics. The
  required evidence artefacts are enumerated in
  [release-governance.md](release-governance.md) Condition 1 under
  "Governance-relocation evidence".
- **AEnt-M Principle 7 metrics.** The four metrics by which an action
  class's relocation status is monitored: decision quality, error
  detection rate, audit reconstructability, and degradation response
  latency. Each metric is monitored at the granularity of the action
  class, not the envelope as a whole. See AEnt-M § Principle 7 for the
  authoritative definitions and threshold-setting guidance.
- **AEnt-M escalation authority.** The named human (or a defined panel)
  whose approval authorises a relocation, whose notification is mandatory
  on a reversion-to-synchronous event, and whose approval is required for
  re-relocation. The escalation authority is established at the time of
  the original relocation and is recorded in the relocation decision
  record. See AEnt-M for escalation-authority criteria and reauthorisation
  triggers.
- **Action class.** A bounded class of agent action covered by a single
  relocation decision. Action classes are the unit of relocation
  accountability; an envelope contains one or more action classes.

Terms whose definition lives in AEnt-M only are marked "see AEnt-M §" with
a topic reference, on the understanding that the AEnt-M document governs
the meaning. This annex does not attempt to redefine AEnt-M concepts.

---

## Tier 4 relocation mechanics

The mechanics below carry forward, in normative form, the relocation
content that previously sat inline in `asdlc.md`. The substance is
unchanged; the location is new.

A Tier 4 policy envelope may contain multiple action classes that are at
different governance-relocation maturity stages under AEnt-M. One action
class within the envelope may be operating under fully relocated control
(synchronous gate replaced by an asynchronous control objective with
demonstrated equivalence); another within the same envelope may still be
governed by a synchronous check pending its own relocation evidence. Each
action class is independently monitored against the AEnt-M Principle 7
metrics — decision quality, error detection rate, audit reconstructability,
and degradation response latency — at the granularity of the action class,
not the envelope as a whole. Aggregated envelope-level metrics are a
useful operational view but they are not the unit of relocation
accountability.

When the AEnt-M Principle 7 metrics for a single action class degrade past
the thresholds defined in that class's `relocation_decision_record` (see
[release-governance.md](release-governance.md) Condition 1), that action
class reverts to synchronous checking automatically. The reversion does
not affect the relocation status of other action classes within the same
envelope; an envelope can simultaneously contain action classes operating
under relocated control, action classes that have just reverted to
synchronous control, and action classes that have never been relocated. The
steward signs the per-class status record as part of the envelope's
continuous monitoring telemetry; an envelope-level signature that does not
record per-class status conceals the relocation state of the action
classes it covers.

Re-relocation of a reverted class — restoring it to asynchronous control —
requires a new evidence bundle satisfying [release-governance.md](release-governance.md)
Condition 1, including a fresh `decision_quality_baseline` measured under
current operating conditions and a fresh `degradation_response_test`. The
reversion-to-synchronous event itself is an audit-relevant transition; the
AEnt-M escalation authority that originally approved the relocation must
be notified, and re-relocation requires that authority's approval on the
new evidence.

---

## Operational accountability during the reverted-but-not-yet-re-relocated window

A Tier 4 envelope contains one or more action classes; relocation status is
held at the action-class level. When an action class reverts from
relocated control to synchronous control, there is a window between the
reversion event and the eventual re-relocation (or permanent acceptance of
synchronous operation). During that window, the envelope is in a mixed
state: some action classes are relocated, others are not, and the recently-
reverted class is operating under synchronous checking that may not have
been exercised since the original relocation.

Without an explicit accountability rule for the window, the operational
accountability for that class is ambiguous. The original relocation
authority (the AEnt-M escalation authority) approved a relocated regime
that is no longer in effect; the synchronous regime that is currently in
effect was not freshly authorised by the escalation authority at the
moment of reversion. Production accountability for actions taken during
the window must rest somewhere that is unambiguously named.

The following rule is normative.

> **Reverted-window accountability rule.** Between the moment an action
> class reverts to synchronous control and the moment of either
> re-relocation approval or permanent-synchronous designation, operational
> accountability for that action class is held by the envelope's
> System Steward. Re-relocation requires the AEnt-M escalation
> authority's approval on the new evidence; both the steward and the
> escalation authority must sign the per-class transition record at the
> moment of re-relocation. Permanent synchronous designation also
> requires the escalation authority's sign-off, not only the steward's.

The rule has the following operational consequences:

- The steward's portfolio bound (see [annex-adoption-cost.md](annex-adoption-cost.md))
  must accommodate the possibility of reverted-window stewardship; an
  envelope containing several reverted classes increases the steward's
  load until re-relocation or permanent designation is reached.
- The per-class transition record carries two signatures: the steward's
  (operational accountability) and the escalation authority's
  (relocation-regime accountability). A transition record bearing only one
  signature is incomplete and the transition is not validly recorded.
- Reversion-window incidents are the steward's accountability in the
  ASDLC operational sense. The post-incident review must address whether
  the synchronous regime in effect at the time of incident was adequate to
  the action class's blast radius; a finding that the synchronous regime
  was not adequate is a finding against the original relocation evidence
  (the relocated regime should not have been authorised against this
  baseline) and is not exculpatory for the reverted-window operation.

---

## Re-relocation evidence requirement

Re-relocation requires a new evidence bundle. The bundle must satisfy
[release-governance.md](release-governance.md) Condition 1 in full,
including the relocation evidence schema enumerated there
(`relocation_decision_record`, `decision_quality_baseline`,
`error_detection_comparison`, `audit_reconstructability_validation`, and
`degradation_response_test`). The five artefacts must reflect operating
conditions at re-relocation time, not at original relocation time.

In addition, re-relocation requires:

- A documented analysis of the metric degradation that triggered the
  original reversion, naming the root cause and the corrective action
  taken in the operating environment, the agent configuration, the
  evaluation portfolio, or the monitoring thresholds.
- An explicit attestation by the AEnt-M escalation authority that the new
  evidence is sufficient to re-authorise the relocated regime in light of
  the original reversion. A re-relocation cannot be authorised by reusing
  the original authorisation record; the authorisation must be fresh.

The re-relocation passes through the Release Gate as the gate object — the
envelope's relocation specification for the action class — not the
underlying production deployment. See `asdlc.md` for the framework-
agnostic statement that Tier 4 envelope changes pass the Release Gate as
the envelope specification.

---

## Relationship to other ASDLC documents

This annex is normative for organisations operating AEnt-M alongside the
ASDLC. The framework-agnostic Tier 4 envelope description in
[asdlc.md](asdlc.md) governs the envelope concept itself and the gate
treatment of envelope changes. The relocation evidence schema is
canonically defined in [release-governance.md](release-governance.md)
Condition 1; this annex references that schema and does not duplicate it.
The parallel annex for Intelligence Governance Manifesto (IGM)-bearing
Tier 4 systems is [annex-igm.md](annex-igm.md); a Tier 4 system that is
both AEnt-M-governed and IGM-governed must satisfy the requirements of
both annexes. The conformance profile that applies to AEnt-M Tier 4
operation is ASDLC-Tier4 (see [conformance-profiles.md](conformance-profiles.md)).
