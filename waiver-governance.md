# Waiver Governance — ASDLC Cross-Cutting

*Waivers as governance debt: lifecycle, accountability, and mandatory expiry.*

See [Specification Readiness](specification-readiness.md) for gate conditions that may be waived.
See [Release Governance](release-governance.md) for release gate waivers.
See [Governance Graph](governance-graph.md) for the waived GateState and the Constraint node.
See [Maintenance Governance](maintenance-governance.md) for security patch SLO waivers.

---

## Section 1: Waivers as Governance Debt

A waiver is a formal decision to proceed despite a gate condition not being fully satisfied. Waivers are necessary — business conditions change, timelines impose constraints, risk trade-offs are legitimate. What is not acceptable is treating a waiver as a permanent resolution. Every waiver is governance debt: the organization has decided that carrying the risk is acceptable for a defined period, with a defined compensating control, and with a defined plan to remediate the underlying condition. A waiver that has no expiry date, no compensating control, and no remediation plan is not a waiver — it is a silent acceptance of permanent non-compliance disguised as a procedural step.

The ASDLC requires waivers to be tracked as debt. Like financial debt, governance debt has a carrying cost. A waiver on an unreviewed threat model carries the cost of operating with uncharacterized risk. A waiver on an expired SBOM carries the cost of unknown dependency vulnerabilities. A waiver on an untested rollback procedure carries the cost of uncertain recovery time. These costs must be explicit, not assumed away by the act of filing the waiver.

Waivers normalize exceptions only when they are not managed. An organization that tracks waiver aging, reviews waiver portfolios, and enforces expiry turns waivers from an escape hatch into a governed temporary accommodation. An organization that lets waivers accumulate without review has built a shadow governance debt ledger that will eventually materialize as production incidents, audit findings, or compliance failures.

The `waived` GateState in the governance graph represents a condition that has been formally waived, not a condition that has been satisfied. A release with waived conditions is a release with documented, accepted, time-limited governance debt — not a clean release. The release record must reflect this distinction.

---

## Section 2: Waiver Requirements

Every waiver must include all of the following. A waiver missing any element is not a valid waiver and must be rejected at the gate.

**Owner.** A named HumanOwner who accepts accountability for the waived condition during the waiver period. The waiver owner is not the accountable human for the release — it is the person who is specifically accountable for the residual risk introduced by the waiver. For security condition waivers, the waiver owner must be the security function lead or a named delegate. For compliance condition waivers, the waiver owner must be the compliance function lead or a named delegate. The waiver owner cannot be the same person who requested the waiver.

**Risk description.** A statement of the specific risk introduced by not satisfying the gate condition. Not a general description of the condition — a specific statement of what could go wrong as a result of proceeding without the condition being met. "Threat model not complete" is not a risk description. "The system's handling of retrieval corpus inputs has not been assessed for RAG poisoning; an adversary who can influence the retrieval corpus may be able to alter agent outputs in ways not detected by the current evaluation suite" is a risk description.

**Expiry date.** The date on which the waiver expires. There are no permanent waivers. An expiry date more than 90 days from the waiver issue date requires additional justification and the approval of the accountable human (not just the waiver owner). An expiry date more than 180 days from issue requires the approval of the accountable human and a written escalation rationale. At expiry, the GateState of the waived condition automatically reverts to its pre-waiver state (typically `fail` or `missing`) unless the waiver has been renewed or the underlying condition has been resolved.

**Compensating control.** A specific control that is active during the waiver period to reduce the risk introduced by the unmet condition. The compensating control must be operational at the time the waiver is issued — not planned. "Enhanced monitoring of retrieval corpus access" is a compensating control. "We will add monitoring next sprint" is not. If no compensating control can be identified, the waiver must be escalated to the accountable human with an explicit risk acceptance decision, not treated as a standard waiver.

**Remediation plan.** A specific plan for satisfying the underlying gate condition before the waiver expires. The plan must name an owner, a target completion date that precedes the expiry date, and the specific action required. "Complete the threat model covering RAG poisoning and submit for security function review by [date]" is a remediation plan. "Improve security posture over time" is not.

**Linked condition.** The specific gate condition being waived, referenced by its gate document and condition identifier. A waiver is scoped to exactly one condition. If multiple conditions require waivers, each requires its own waiver record.

---

## Section 3: Waiver Lifecycle

A waiver moves through five states from approval to closure. The GateState of the underlying condition tracks this lifecycle in the governance graph.

**Issued.** The waiver has been approved by the waiver owner and the accountable human. The gate condition GateState is set to `waived`. The compensating control is active. The remediation plan is in progress.

**Active.** The waiver is within its validity period. The GateState remains `waived`. The Runbook Drift Agent (or equivalent continuous monitoring) tracks the remediation plan's progress and the compensating control's operational status.

**Expiring.** The waiver is within 30 days of its expiry date. The waiver owner and accountable human are notified. Three outcomes are possible: remediation completes before expiry (waiver closes, condition GateState updates to reflect the satisfied condition), waiver is renewed (requires the same approval process as original issuance, with documented justification for renewal), or waiver expires without renewal or remediation.

**Expired without renewal or remediation.** The GateState of the waived condition reverts immediately to its pre-waiver status. Any deployment relying on the waived condition may no longer reference the waiver as justification. If the system is in production, the expired waiver becomes an operational DoD failure requiring steward action within the remediation SLO.

**Closed.** The underlying condition has been satisfied before or at expiry. The GateState updates to `pass`. The waiver record is closed with a reference to the evidence artefact that satisfied the condition. Closed waivers are retained in the governance record for audit purposes.

---

## Section 4: Waiver Portfolio Governance

Waivers accumulate. An organization with 20 active systems, each carrying 2 waivers, has 40 open governance debt items. Without portfolio-level tracking, this debt is invisible.

Portfolio-level waiver tracking is a steward responsibility at the organizational level, not just the system level. The economics owner or a designated governance portfolio role should review the aggregate waiver portfolio quarterly: how many waivers are active, how many are in the expiring state, how many have expired without resolution, and what categories of conditions are being waived most frequently. Frequent waivers on the same condition type across multiple systems is a signal that the gate condition is either miscalibrated (too strict for the organization's current maturity) or that organizational capability to satisfy the condition is insufficient and requires investment.

Waiver counts are a governance metric: the total number of active waivers per system, per tier, and per gate condition type should be tracked and reviewed against defined warning thresholds. More than 3 active waivers per system at any time indicates a governance capacity problem. More than 20% of a tier's systems carrying waivers on the same condition type indicates a systemic gap. These thresholds are starting points, not universal limits; organizations calibrate them based on their phase and risk appetite.

The Runbook Drift Agent tracks waiver aging as part of continuous governance monitoring. For any waiver entering the expiring state, the agent surfaces it to the waiver owner and accountable human. For any waiver that expires without renewal or remediation, the agent records the GateState reversion and notifies the steward. Waiver aging and expiry are not manual processes — they are monitored-execution governance functions.

---

## Section 5: Emergency Waivers

Some gate conditions must be waived in emergency change procedures, where the normal waiver approval timeline is incompatible with the urgency of the change.

An emergency waiver follows the same structure as a standard waiver but has a compressed timeline: the waiver owner and accountable human must approve within the emergency change window (typically measured in hours, not days). An emergency waiver has a maximum validity of 14 days — sufficient to address the immediate urgency while ensuring rapid remediation. At 14 days, the emergency waiver either converts to a standard waiver (with full standard approval) or the condition must be satisfied. Conversion to a standard waiver is not automatic; it requires explicit re-approval under the standard process. An emergency waiver that reaches day 14 without either conversion or remediation expires on the same terms as a standard waiver: the GateState reverts and the operational consequences follow.

Emergency waivers may not be stacked: if a prior emergency waiver on the same condition is still active, a new emergency waiver on the same condition requires accountable human escalation, not routine approval. Stacking would allow an organization to chain emergency windows indefinitely, converting what should be a short-term accommodation into a permanent exception through procedural repetition. The prohibition on stacking closes that path. If a condition has required two consecutive emergency waivers, the organization has a systemic problem with either the condition's achievability or its remediation capability, and that problem requires a governance response — not another emergency waiver.
