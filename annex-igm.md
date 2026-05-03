# Annex — Tier 4 Operation with the Intelligence Governance Manifesto (IGM)

_An annex documenting how a Tier 4 ASDLC policy envelope operates when the
agent's actions are informed by intelligence governed under the
Intelligence Governance Manifesto (IGM). This annex carries forward, in
normative form, the Tier 4 Appendix A content that previously appeared
inline in `asdlc.md`. It is normative for organisations operating IGM; for
organisations not operating IGM, see the framework-agnostic Tier 4 envelope
description in [asdlc.md](asdlc.md)._

See [asdlc.md](asdlc.md) for the four-layer model and the Tier 4 paragraphs
in each Layer section. See [release-governance.md](release-governance.md)
for the Release Gate condition set referenced below. See
[annex-aentm.md](annex-aentm.md) for the parallel AEnt-M-specific annex.

---

## Scope

This annex is normative for organisations operating the Intelligence
Governance Manifesto (IGM) in concert with the ASDLC. IGM defines a body of
governance machinery around the epistemic substrate — the structured body
of claims that informs agent action — and the lifecycle of those claims
through tiers of confidence, contradiction, decay, and feedback. ASDLC's
Tier 4 envelope is the construct within which an agent's intelligence
boundary is operationalised at the delivery layer.

For organisations not operating IGM, this annex is non-binding. The
framework-agnostic Tier 4 envelope content in `asdlc.md` is sufficient to
govern Tier 4 operation in the absence of IGM. IGM adds the epistemic-
substrate accountability machinery; this annex documents how that
machinery integrates with the ASDLC envelope.

Where this annex references IGM concepts whose authoritative definition
lives in IGM itself, the reference is explicit ("see IGM § X"). Where this
annex restates an IGM definition, the restatement is intended to be
faithful but is not authoritative; IGM governs the meaning of its own
terms.

---

## IGM terms used in this annex

The following terms are used in this annex with the meanings stated below.

- **Epistemic substrate.** The structured body of claims and their
  supporting evidence that informs agent action across an organisation or
  a domain. The substrate is more than a knowledge base: it is a governed
  artefact whose claims carry epistemic tier, decay characteristics,
  contradiction state, and feedback receptivity. See IGM for the
  authoritative substrate model.
- **Epistemic tier.** The confidence classification of a claim within the
  substrate. The defined tiers, in ascending order, are Provisional,
  Candidate, Confirmed, High Confidence, and Authoritative. Each tier
  carries different obligations about the actions it may inform, the
  evidence required to promote a claim to that tier, and the decay
  treatment of the claim once it sits there. See IGM for the per-tier
  authoritative definitions and the promotion / demotion rules.
- **Claim.** A discrete proposition in the substrate, identified by a
  claim identifier, carrying provenance, an epistemic tier, a decay
  boundary, and a contradiction state. Claims are the unit of intelligence
  governance under IGM; an agent's action is informed by a set of claims
  whose identifiers and tiers can be enumerated.
- **Decay boundary.** The point — defined either as a temporal threshold
  or as a decay-model output — at which a claim loses its current
  epistemic tier in the absence of re-verification. A claim past its
  decay boundary is not invalid; it is unconfirmed-at-current-tier and
  must be re-verified before further action depends on it, or its
  consuming actions must be downgraded accordingly. See IGM for the
  authoritative decay-model definitions per claim class.
- **Domain graph.** The structural representation of claims, their
  relationships, and the authorities responsible for each. The domain
  graph is the queryable form of the epistemic substrate. See IGM for
  the domain graph schema and the revision/assertion/semantic-authority
  structure.
- **IGM Principle 10.** The principle that every engagement on the
  substrate — including production agent action — must produce structured
  feedback that closes the loop on the claims the action depended on. The
  feedback is the substrate's primary signal that production reality
  agrees with, contradicts, or extends the claims that informed the
  action. See IGM § Principle 10 for the authoritative formulation.
- **Structured feedback.** The artefact-format-specified, destination-
  authority-named, latency-bounded record of an action's observed
  outcome, emitted to the IGM revision, assertion, or semantic authority
  responsible for the affected claims. See IGM for the structured-
  feedback schema.

Terms whose definition lives in IGM only are marked "see IGM §" with a
topic reference, on the understanding that the IGM document governs the
meaning. This annex does not attempt to redefine IGM concepts.

---

## Tier 4 policy-envelope intelligence constraints

The four constraints below carry forward, in normative form, the Tier 4
Appendix A content that previously sat inline in `asdlc.md`. The substance
is unchanged; the location is new. For Tier 4 systems whose actions are
informed by intelligence governed under IGM, the policy envelope must
explicitly specify how the intelligence layer constrains agent action
within the envelope. Without these elements, the envelope authorises
autonomous operation against an unspecified epistemic substrate — a
configuration in which the substrate's adequacy is assumed rather than
governed.

The following elements are required components of any Tier 4 policy
envelope for an intelligence-bearing system.

### Epistemic-tier-to-action mapping

For each action class the envelope authorises, the minimum epistemic tier
(Provisional, Candidate, Confirmed, High Confidence, Authoritative) of the
claims that must inform that action. An envelope that authorises an action
class without specifying the required epistemic tier permits the action
against any claim, including Provisional ones — which is not a Tier 4
envelope; it is unconstrained autonomy.

### Contradiction-handling rules per type

For each contradiction type the system's domain is known to produce —
jurisdictional divergence, logical contradiction, temporal supersession,
scope variation, extraction error — the rule the agent applies when it
encounters the contradiction: refuse, escalate, select-by-jurisdiction-
policy, or similar typed responses. Untyped contradiction handling — a
single fallback regardless of contradiction class — does not satisfy this
element.

### Decay boundaries per claim class

For each claim class the system depends on, the decay boundary beyond
which the agent must refuse to act on the claim within the envelope, and
the latency within which the agent must observe a re-verification event
before resuming action. A decay boundary stated only as a calendar window
is insufficient; the boundary must reference the claim class's own decay
model.

### Feedback-loop closure rules

The structured feedback the agent must emit when it observes evidence that
a claim it acted on was wrong, stale, or contradicted in production. The
feedback rules must specify the artefact format, the destination IGM
authority, and the latency bound for emission. An envelope without
feedback-loop closure rules permits autonomous action that produces no
return signal to the substrate — which is incompatible with IGM Principle
10.

---

## Composition rule

These four elements are governed by the composition rule that specifies
how individual constraints compose into a coherent policy envelope and how
the envelope's effective constraint set is computed. The composition rule
is referenced in `asdlc.md` as living at `governance/composition-rule.md`.

> **Status note.** As of the current ASDLC version, `governance/composition-rule.md`
> is a planned artefact and has not yet been authored. Until it is
> authored, organisations operating an IGM-bearing Tier 4 envelope must
> compose the four required elements above by inspection and document the
> resulting effective constraint set in the envelope specification itself.
> Adopting an IGM-bearing Tier 4 envelope in advance of the composition
> rule's publication is an adopt-at-your-own-risk operating choice: the
> envelope's effective constraint set is determined by ad hoc composition
> until the rule is published, and the organisation accepts the
> consequence of any composition error that the rule, once published,
> would have prevented.

A Tier 4 envelope for an intelligence-bearing system that omits any of the
four elements above is not a complete envelope and cannot pass the Release
Gate as the envelope specification under Layer 3.

---

## Integration with the Release Gate evidence bundle

For intelligence-bearing Tier 4 envelopes, the four required elements
above are part of the evidence bundle for the Release Gate decision on the
envelope specification. This means that
[release-governance.md](release-governance.md) Condition 1 (Evidence
Bundle Complete), when applied to an envelope under release, requires
each of the following to be present and machine-readable:

1. The epistemic-tier-to-action mapping, enumerating each action class the
   envelope authorises and the minimum tier required for the claims that
   inform that action class.
2. The contradiction-handling rule set, with one rule per contradiction
   type the domain is known to produce. The rule set must name the
   contradiction types; an unnamed type is not handled.
3. The decay boundary specification per claim class the envelope's
   actions depend on, expressed against the claim class's decay model
   (not as a calendar window unless the calendar window is itself the
   claim class's decay model).
4. The feedback-loop closure rules, naming the artefact format, the
   destination IGM authority, and the latency bound per claim class on
   which the agent acts.

The envelope's Release Gate decision is on the envelope specification,
not on individual deployments within the envelope (see `asdlc.md` Tier 4
operation in Layer 3). The four elements above are therefore part of the
specification under gate, and their absence is a Condition 1 failure at
the envelope's gate.

The instruction in this annex is an integration note. It does not modify
[release-governance.md](release-governance.md) directly; that document
governs the Release Gate's framework-agnostic obligations. This annex
states how those obligations apply when the system under release is an
intelligence-bearing Tier 4 envelope.

---

## Operational obligations during continuous monitoring

The Tier 4 envelope's continuous monitoring telemetry — referenced in
`asdlc.md` Layer 4 Tier 4 paragraphs — must include, for IGM-bearing
envelopes, the following observability dimensions in addition to the
framework-agnostic envelope health signals:

- Per-claim usage telemetry: which claim identifiers were invoked in
  agent action, with epistemic tier at the time of invocation. This
  telemetry is what makes the L4 → IGM feedback path in `asdlc.md`
  operational.
- Decay-boundary crossings: the substrate-side events when a claim crosses
  its decay boundary, surfaced in operational dashboards before the agent
  next acts on the claim.
- Contradiction events observed in production: when the agent encountered
  a contradiction, the type, and the rule it applied; the count of these
  events per claim class is a primary signal that the contradiction-
  handling rules in the envelope are well-calibrated.
- Feedback emission: confirmation that the structured feedback specified
  in the envelope's feedback-loop closure rules was emitted within the
  latency bound for each qualifying production event.

A Tier 4 envelope whose continuous monitoring does not surface these
dimensions is operating against an IGM substrate that it does not actually
observe; the envelope's intelligence specification is then a paper
specification.

---

## Relationship to other ASDLC documents

This annex is normative for organisations operating IGM alongside the
ASDLC. The framework-agnostic Tier 4 envelope description in
[asdlc.md](asdlc.md) governs the envelope concept itself and the gate
treatment of envelope changes. The Release Gate evidence bundle obligation
is canonically stated in [release-governance.md](release-governance.md)
Condition 1; this annex states how that obligation applies to intelligence-
bearing envelopes without restating the framework-agnostic content. The
parallel annex for AEnt-M-governed Tier 4 systems is
[annex-aentm.md](annex-aentm.md); a Tier 4 system that is both AEnt-M-
governed and IGM-governed must satisfy the requirements of both annexes.
The composition rule on which this annex's effective-constraint-set
computation depends is `governance/composition-rule.md`, which is planned
and currently a TODO. The Retirement Gate's IGM-claim-retraction condition
(RT-5 in [retirement-gate.md](retirement-gate.md)) is the end-of-life
counterpart to the integration described in this annex.
