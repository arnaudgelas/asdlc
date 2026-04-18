# Demand Intelligence — ASDLC Layer 0

_The continuously running agentic layer that surfaces candidate demand before
Layer 1 validation begins._

See [Demand & Value](value.md) for Layer 1 demand governance. See
[Specification Readiness](../specification-readiness.md) for the Layer 1→2 gate.
See [asdlc.md](../asdlc.md) for the full four-layer model.

---

## What is the Demand Intelligence Layer?

Layer 1 governs demand validation. Layer 0 governs demand generation. The
distinction matters because the ASDLC, as originally specified, assumes demand
items arrive at Layer 1 from human sources — product owners, stakeholders,
regulatory leads, or operations teams who have already identified a need and
framed it. That assumption is not wrong, but it is incomplete. Human demand
identification is episodic, attention-dependent, and prone to organisational
amnesia. Needs surface when someone is paying attention to the right signals at
the right time. Needs that fall outside anyone's current line of sight do not
surface at all.

Layer 0 makes demand generation governed rather than ad hoc. Demand intelligence
agents continuously monitor environmental signals, pattern-match against the
governance graph's DemandItem and Incident history, and surface candidate demand
items with supporting evidence pre-assembled — ready for human validation, not
human discovery. The product owner's time is spent evaluating a candidate need
with evidence already assembled, not searching for the need in the first place.

The distinction between the two layers is precise. Layer 1 asks: is this need
real? Layer 0 asks: what needs might be emerging that we haven't articulated
yet?

Layer 0 outputs are always **draft demand items** — candidate items that a
product owner reviews and either promotes to Layer 1 validation or rejects with
documented rationale. Layer 0 agents may not create confirmed demand items. The
human product owner's validation gate at Layer 1 remains the entry point for all
engineering investment. Layer 0 reduces discovery cost; it does not transfer
validation authority.

---

## Demand Intelligence Signal Categories

Demand intelligence agents monitor six categories of signal. Each category maps
to a distinct source of organisational need that human attention does not
reliably capture without continuous monitoring.

**Regulatory signal monitoring.** Continuous monitoring of regulatory feed
sources relevant to the organisation's deployed systems — guidance updates,
enforcement actions against comparable organisations, consultation papers,
legislative changes. When a regulatory signal may create a new compliance
obligation or change the interpretation of an existing constraint, a draft
demand item is created with the regulatory citation as evidence. The agent does
not interpret whether the organisation is currently non-compliant; that
judgement belongs to qualified human reviewers. The agent's job is to ensure the
signal reaches the product owner before it becomes an incident.

**Production anomaly pattern intelligence.** Analysis of the governance graph's
Incident and CostRecord history to identify patterns that indicate unmet
structural needs. A class of incident recurring across multiple systems with the
same root cause pattern is evidence of a systemic need, not a per-system
maintenance issue. The demand intelligence agent identifies the pattern and
proposes a demand item for the structural fix rather than leaving teams to
repeatedly patch the same class of failure. The evidence is the pattern itself:
incident identifiers, affected systems, common root cause signatures, and
cumulative operational cost where computable from CostRecord data.

**Backlog archaeology.** Analysis of DemandItem nodes in "abandoned" or
"deferred" status to identify whether their staleness triggers have resolved. A
demand item abandoned because a dependency wasn't available may become viable
when that dependency is resolved. An item deferred for strategic reasons may
become relevant when the strategy changes. Backlog archaeology prevents
organisational amnesia about real needs the organisation chose not to pursue
previously. The agent surfaces the original item, its abandonment or deferral
rationale, and the specific condition that now appears to have changed.

**Specification gap intelligence.** Analysis of HITL override patterns,
validation failure patterns, and post-deployment value realisation shortfalls to
identify classes of specification that consistently fail to capture what they
should. These patterns suggest systemic gaps in how the organisation specifies
certain types of work — not individual specification quality issues but
structural patterns that recur across teams, systems, or specification authors.
The demand item proposed is for the process or tooling change that addresses the
gap, not for the individual specification that failed.

**Cross-system dependency risk signals.** Monitoring of Dependency nodes across
the governed portfolio for patterns that indicate systemic risk — a dependency
used by many systems approaching end-of-life, a shared model provider whose
terms are changing, a common library with a newly disclosed vulnerability class.
These signals may not be incidents yet; they are structural risks that warrant
proactive demand items before the risk materialises as production failures. The
agent estimates blast radius from the governance graph's system topology: how
many systems depend on this dependency, and at what tier.

**External intelligence signals.** Market and technology signals from
configurable external sources — standards body publications, technology
end-of-life announcements, notable incidents at organisations operating
comparable systems. These signals require explicit human judgement to connect to
specific organisational needs. The demand intelligence agent surfaces them as
contextual signals with plausible demand hypotheses, not as confirmed needs. The
confidence indicator for items in this category is always Medium or Low. High
confidence requires corroboration from an internal signal category.

---

## Draft Demand Item Format

A draft demand item produced by Layer 0 must contain the following fields. Items
missing any mandatory field are not surfaced to the product owner; they are
flagged as malformed output in the agent's evaluation log.

**Candidate need statement.** A clear, single-paragraph statement of the
candidate need. Written in terms of what is needed, not in terms of the signal
that triggered it. If the need cannot be stated independently of the signal, the
item is not ready to surface.

**Signal category.** The signal category from the six defined above that
triggered the draft item. One category per item. If multiple signal categories
support the same candidate need, they are listed as corroborating signals, not
as separate trigger categories.

**Supporting evidence.** The specific evidence or pattern that supports the
candidate need, with governance graph references where applicable — DemandItem
node identifiers, Incident identifiers, Dependency node identifiers. For
regulatory signals, the citation, publication date, and jurisdiction. Evidence
must be specific enough that the product owner can verify it independently.

**Initial blast radius estimate.** Tier 1, 2, or 3, derived from the governance
graph's system topology. The agent must document its derivation — which systems
are affected and why — not merely assert the tier.

**Confidence indicator.** High, Medium, or Low, reflecting how directly the
evidence supports the candidate need versus how much inference is involved. High
means the evidence directly supports the need with minimal interpretation.
Medium means the evidence supports the need but requires some interpretive step.
Low means the evidence is suggestive but indirect — a hypothesis with supporting
context, not a documented pattern.

**Recommended validation approach.** What evidence a product owner should
collect to validate this need at Layer 1 — specifically what would confirm or
refute the candidate need, not a generic suggestion to "review with
stakeholders."

**Agent provenance.** The demand intelligence agent identifier and GASH at the
time of generation. Required for auditability and for calibration review.

Draft items at Low confidence with no corroborating signal from a second
category require explicit product owner acknowledgement before they consume any
validation attention. High-volume Low-confidence items from a single agent
signal a calibration problem in that agent's signal processing. When more than
30% of items surfaced by a single agent in any rolling 30-day window carry Low
confidence, the agent's accountable human is notified and a calibration review
is opened.

---

## Governed Agent Operation

Layer 0 agents are governed under the ASDLC like any other agentic system. The
fact that they support the governance process does not exempt them from it.

Each demand intelligence agent has a specification defining its signal sources,
monitoring cadence, draft item thresholds, and blast radius estimation
methodology. The specification is subject to the same Specification Readiness
Gate as any other system specification. Changes to signal sources or thresholds
are versioned changes to the specification and require product owner approval.

Epistemic tier labels apply to all Layer 0 outputs. The draft demand item itself
carries the `agent-generated` tier. Governance graph queries and regulatory
database queries carry the `tool-generated` tier. An item carries the
`agent-proposed-with-human-review` tier only after the product owner has
reviewed and validated it and promoted it to Layer 1. Layer 0 agents may not
self-assign a higher epistemic tier to their outputs.

Tool authorisation for Layer 0 agents is restricted to: Read-governance-graph,
External-regulatory-query, Model-invocation, Notification-send. No write access
to the governance graph. No specification-write access. An agent that requests
write access to the governance graph has an incorrect specification and must be
corrected before deployment.

Evaluation suites for demand intelligence agents must include four case classes:

- **False positive cases:** signals that should not produce draft demand items —
  noise patterns, signals outside the organisation's operating domain,
  regulatory changes with no plausible connection to deployed systems.
- **False negative cases:** genuine needs that a poorly calibrated agent would
  miss — known patterns that fall just below naive detection thresholds,
  regulatory signals described in indirect language.
- **Adversarial cases:** spurious signals constructed to appear like genuine
  needs — fabricated incident patterns, out-of-context regulatory citations,
  synthetic anomaly sequences.
- **Recall cases:** known past needs with documented histories, to verify the
  agent would have surfaced them at the time with the evidence then available.

Draft items consistently rejected by product owners without promotion to Layer 1
are a calibration signal. A rejection rate above 80% for any signal category
over a rolling 90-day window requires an agent evaluation review. The review
examines whether the signal source is miscalibrated, whether the candidate need
formulation is systematically off, or whether the product owner's rejection
pattern itself reveals a domain assumption that should be encoded in the agent's
specification.

---

## Integration with Organisational Memory

Layer 0 agents actively use organisational memory to improve signal quality. A
demand intelligence agent that does not query memory before surfacing a
candidate need is operating without context that the organisation already holds.

**Episodic memory query.** Before surfacing a draft item, the agent queries
episodic memory for similar past demand items. Has this pattern been seen
before? What happened? Was the need validated? Did the delivered solution
produce measurable value? A pattern that has been raised, built, and delivered
with documented value realisation has a higher confidence indicator than one
with no history. A pattern that has been raised and rejected multiple times is
surfaced with that history attached — the product owner receives the candidate
need and the reasons it was previously declined.

**Episodic memory write.** When a product owner rejects a draft item, the
rejection rationale is written to episodic memory — not merely logged in an
audit trail. Future agents querying similar patterns will have the rejection
rationale as context, reducing re-generation of items the organisation has
consciously declined. An agent that repeatedly surfaces items with documented
rejection rationale in memory is not retrieving memory correctly — a calibration
defect, not a minor operational issue.

**Semantic memory query.** Domain knowledge about the organisation's regulatory
environment, technology constraints, and architectural patterns informs signal
interpretation. A regulatory signal in a domain the organisation does not
operate in should not produce a draft item. A technology signal about a
component the organisation has already migrated away from should not produce a
draft item. Semantic memory is the agent's knowledge of the organisation's
operating context; without it, signal interpretation is context-free and
produces high false positive rates.

---

## Relationship to Layer 1

Layer 0 is not a replacement for Layer 1 demand governance. It is a reduction in
the discovery cost of demand. Layer 1 remains the accountability boundary: no
demand item enters the engineering backlog without human validation of the need,
value definition, and success criterion. That boundary does not move because an
agent has pre-assembled supporting evidence.

The product owner review of a Layer 0 draft item is not a rubber stamp. It is a
genuine validation judgement: does this signal represent a real need for our
users and our organisation? The supporting evidence in the draft item
accelerates that judgement; it does not replace it. A product owner who
consistently promotes Layer 0 items without independent validation is not using
Layer 0 correctly and is weakening the accountability guarantee that Layer 1
provides.

Draft items that the product owner promotes to Layer 1 enter the standard
validation process. The Layer 0 evidence is the starting point for that
validation, not the conclusion. The product owner must confirm the evidence is
current and sufficient for the blast radius tier before the item clears the
Specification Readiness Gate. Evidence assembled by a demand intelligence agent
is evidence of record once the product owner has confirmed it — until then, it
is a draft with no formal standing in the governance record.
