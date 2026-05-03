# Demand & Value Metrics — ASDLC Layer 1

_The measurement framework for demand layer health._

See [Demand & Value](value.md) for the demand layer processes these
metrics govern. See [Specification Readiness](../specification-readiness.md) for
the gate whose health several of these metrics assess. See
[adoption-metrics.md](../../adoption/metrics.md) for the inner-loop metrics this
document complements.

---

Metrics without thresholds are accounting. Metrics without owners are
decoration. The metrics in this document each have a warning threshold, a unit
of measurement, and an implied owner — the role that must act when the metric
signals a problem. A demand layer that collects these metrics but does not act
on the warning signals is not governed; it is monitored. Governance requires
action.

---

## Value Delivery Metrics

These metrics answer the question the demand layer exists to answer: are the
things we built worth building?

### Business Value Realised per Loop Iteration

**What it measures.** The degree to which each shipped loop output achieved its
business-level success criterion, measured post-deployment within the defined
measurement window.

**How to measure it.** For each released loop output, retrieve the success
criterion defined at specification readiness. After the measurement window
closes, record the actual outcome against the criterion: exceeded, met,
partially met (with percentage), or not met. Aggregate across all releases in
the measurement period.

**The unit.** Percentage of success criteria met or exceeded per measurement
period (quarter is the typical cadence).

**Warning threshold.** Below 60% across any rolling four-release window. This is
not a precision target — it is a floor. Consistently failing to meet 40% or more
of business success criteria means the demand validation process is producing
false positives: items are passing the gate with insufficient evidence that the
need is real and the value is achievable.

**Owner.** Business demand sponsor for each individual criterion. Product owner
for the aggregate metric.

**What it is not.** This metric is not the same as the inner loop's verification
rate. Verification measures whether the loop built the specification correctly.
Business value realised measures whether the specification, correctly built,
produced the intended business outcome. Both can be 100% independently. An
organisation where verification is high and value realisation is low has a
demand layer problem, not a loop quality problem.

---

### Value Realisation Lag

**What it measures.** The time elapsed between production deployment and the
first measurable evidence of business value. This is distinct from deployment
lead time — it measures the delay between a system being live and the system
producing the outcome it was built to produce.

**How to measure it.** Record the deployment date for each loop output. Record
the date on which the first measurement of the success criterion became
available and showed movement toward the target. The lag is the interval between
these two dates.

**The unit.** Days from deployment to first measurable value signal. Track
median and P90 across a rolling window.

**Warning threshold.** Median value realisation lag exceeding 90 days for
customer-facing systems. For internal tooling at Tier 1, 45 days is the
appropriate threshold. Lag above these thresholds indicates one of three
problems: the measurement infrastructure for the success criterion does not
actually exist (a gate failure — Condition 2 requires the measurement method to
be confirmed before loop entry), the specification was scoped too large for the
value to be incremental, or the success criterion was set at the wrong
granularity.

**Owner.** Business demand sponsor, with support from the product owner on
measurement infrastructure.

---

### Demand-to-Delivery Lead Time

**What it measures.** Total elapsed time from a demand item being entered into
the validated backlog to the corresponding loop output being deployed to
production. Decomposed into four stages:

1. Time in demand backlog (entered to gate assessment initiated).
2. Time at gate (gate assessment initiated to gate passed).
3. Time in inner loop (loop entry to loop output produced).
4. Time in release (loop output produced to production deployment).

**How to measure it.** Track timestamps at each stage boundary. The stage
decomposition is required — aggregate lead time without decomposition is
unactionable because it cannot distinguish between a demand layer bottleneck and
a loop execution bottleneck.

**The unit.** Calendar days per stage, plus total. Track median and P90 per
quarter.

**Warning threshold.** Total lead time growing quarter-over-quarter while
inner-loop cycle time is stable. If inner-loop cycle time is stable or improving
but total lead time is growing, the bottleneck is in the demand layer or the
release layer. Decompose by stage to isolate.

**Owner.** Product owner for stages 1 and 2. Engineering lead for stage 3 (inner
loop). Release governance owner for stage 4.

---

## Specification Quality Metrics

These metrics answer the question: are the specifications the demand layer
produces fit for purpose when they enter the loop?

### Specification Stability at Loop Entry

**What it measures.** The percentage of specifications that enter the Specify
phase without requiring material revision to the acceptance criteria,
constraints, or success criterion during loop execution.

**How to measure it.** Track all specification changes after loop entry. A
material revision is any change that modifies: an acceptance criterion, a
constraint, the success criterion, the blast radius assessment, or the
out-of-scope declarations. Changes to implementation guidance or non-normative
description are not counted. Record the number of loop iterations that completed
without material specification revision versus those that required at least one.

**The unit.** Percentage of loop iterations with zero material specification
changes, per quarter.

**Warning threshold.** Below 80%. Any specification churn above 20% of
iterations indicates that specifications are entering the loop before they are
genuinely ready. The gate is either being passed prematurely or is miscalibrated
for the organisation's context.

**Owner.** Product owner.

**Note.** A single material specification change during a loop iteration is not
just a loop quality signal — it is a gate failure signal. The change means a
condition that should have been addressed at the gate was not. The gate decision
record for that specification should be reviewed to determine which condition
was missed.

---

### First-Pass Specification Readiness Gate Rate

**What it measures.** The percentage of specifications that pass the
specification readiness gate on first assessment, without a failed assessment
preceding the pass.

**How to measure it.** For each gate assessment, record whether the outcome was
pass or fail. For each specification, record whether the final pass was preceded
by one or more failures. First-pass rate is the percentage of specifications
where the first assessment resulted in a pass.

**The unit.** Percentage, per quarter.

**Warning threshold.** Below 60%. A first-pass rate above 60% indicates the
demand layer preparation before gate assessment is generally adequate. Below 60%
means the gate is consistently being attempted before the preparatory work is
complete — which either means the gate is being used as a checkpoint during
specification development (not its purpose) or that the team's understanding of
the gate conditions is insufficient.

**What a healthy rate looks like.** At Phase 2, a first-pass rate of 40–60% is
expected — teams are learning what the conditions require. At Phase 4, 70–80% is
achievable. At Phase 5, 85%+ with mature teams and good tooling. A first-pass
rate of 100% that is sustained over time is a warning sign: it may indicate the
gate is being treated as a formality where failures are never recorded.

**Owner.** Product owner.

---

### Validation Rate

**What it measures.** The percentage of loop outputs where the Validate phase of
the inner loop confirms that the business-level success criterion is met. This
is distinct from the verification rate (which measures whether the loop built
the specification correctly) and from the business value realised metric (which
measures outcome at the measurement window, post-deployment).

Validation rate measures whether the specification was right — whether what was
built, correctly, was the right thing. A validation failure after verification
success is always a demand layer signal: the specification passed verification
but failed to represent the actual need, or the need changed after specification
without being surfaced.

**How to measure it.** Track Validate phase outcomes across loop iterations.
Record: passed (the loop output satisfies the business need as understood at
Validate), failed — demand signal (Validate failed because the specification did
not represent the need, requiring return to Specify or to the demand layer),
failed — design signal (Validate failed because of a design flaw addressable
within the loop without demand layer involvement).

**The unit.** Percentage of loop iterations where Validate passes on first
assessment, per quarter. Track separately: demand-signal failures versus
design-signal failures.

**Warning threshold.** Validation rate below 70% over any two consecutive
quarters, or any single quarter where demand-signal failures exceed 30% of all
loop iterations. The second threshold is more diagnostic: demand-signal
validation failures mean the demand layer is consistently producing
specifications that do not match the underlying need.

**Owner.** Product owner for the demand-signal subset. Engineering lead for the
design-signal subset.

---

## Demand Health Metrics

These metrics answer the question: is the demand layer functioning as a governed
system, or is it drifting toward an ungoverned queue?

### Demand Backlog Age

**What it measures.** The age distribution of items in the demand backlog — how
long validated items are waiting between validation and loop entry.

**How to measure it.** For each item in the demand backlog, record the date it
was added as a validated item. Track the age distribution: mean, median, P75,
P90. Track separately by tier.

**The unit.** Calendar days from validation to loop entry, for items currently
in the backlog and for items that were completed in the period.

**Warning threshold.** Median backlog age growing quarter-over-quarter without a
corresponding growth in the backlog volume. Stable or growing backlog age with
stable volume indicates a throughput problem: the loop is not consuming demand
as fast as demand is being validated. Items at P90 age exceeding 180 days should
be individually reviewed — either they are lower priority than everything else
(which is a valid outcome and should be documented) or they have been forgotten
(which is a governance failure).

**Owner.** Product owner.

---

### Demand Abandonment Rate

**What it measures.** The percentage of validated demand items that are removed
from the backlog without completing a loop iteration and without being
superseded by a replacement specification.

**How to measure it.** Track all items removed from the backlog. Classify each
removal: completed (entered loop and shipped), superseded (merged with or
replaced by another item), abandoned (removed without shipping or superseding).
The abandonment rate is the proportion of removed items classified as abandoned.

**The unit.** Percentage of removed items that are abandoned, per quarter.

**What a healthy rate looks like.** Some abandonment is healthy. Demand
conditions change, business priorities shift, regulatory deadlines pass. An
abandonment rate of 10–20% per quarter is normal for a well-functioning demand
layer — it means the demand layer is responding to changes in the environment
rather than mechanically processing a queue. A rate consistently below 5% is a
warning sign: it may indicate that items are not being reviewed for continued
relevance, and the backlog contains stale demand that the prioritisation process
is politely avoiding.

**Warning threshold.** Abandonment rate consistently above 35% for two
consecutive quarters. This level of abandonment indicates one of two problems:
the validation process is not filtering effectively (items are being validated
that do not survive to loop entry), or the portfolio governance process is not
managing demand to match organisational capacity (items are being validated
faster than the organisation can act on them, leading to backlog saturation and
inevitable abandonment).

**Owner.** Product owner.

---

### Specification Churn Rate Inside the Loop

**What it measures.** The rate of specification changes made after loop entry —
changes to acceptance criteria, constraints, success criteria, or scope
boundaries during the Specify, Design, Plan, or Execute phases of the inner
loop.

**How to measure it.** Track all changes to the versioned specification document
after the gate decision record marks the specification as passed. Count the
number of specifications per quarter that experienced one or more material
changes post-gate.

**The unit.** Percentage of specifications experiencing material change after
gate entry, per quarter.

**Warning threshold.** Above 20% of specifications per quarter. Any
specification churn inside the loop is a gate failure signal — the gate was
either passed prematurely (a condition was not genuinely satisfied) or a
condition became unsatisfied after the gate (the business environment changed).
At 20% of specifications, the pattern is systemic and requires a demand layer
process review, not case-by-case investigation.

**Owner.** Product owner, with root-cause analysis responsibility for each churn
event.

---

## Warning Signals

The following combinations require escalated investigation — not routine metric
review, but a demand layer retrospective with the product owner, business demand
sponsor, and engineering lead.

**Validation rate below 60% for three consecutive releases.** At this level,
more than one in three loop iterations is producing something the Validate phase
rejects. The demand layer is not filtering effectively. Either the gate
conditions are not being applied rigorously (the evidence bar is too low), the
translation step is consistently failing to preserve business intent, or the
business environment is changing faster than the demand layer is adapting. These
require different responses, which is why root-cause classification is essential
before prescribing a fix.

**Specification churn rate above 20% for two consecutive quarters.** The gate is
consistently being passed before specifications are ready. This may reflect
stakeholder pressure (anti-pattern documented in
[Specification Readiness](../specification-readiness.md)), insufficient
specification analyst expertise, or a gap between the gate conditions as written
and the gate conditions as applied.

**Demand-to-delivery lead time growing quarter-over-quarter while inner-loop
cycle time is stable.** The bottleneck has moved outside the loop. Decompose by
stage to identify whether it is in demand backlog time (prioritisation or
capacity problem), gate time (specifications requiring multiple assessment
iterations), or release time (covered by
[Release Governance](../release-governance.md)). Growing lead time with stable
inner-loop performance means the outer governance layers are the constraint.

**Value realisation lag exceeding 90 days for customer-facing systems.** The
most likely causes are: the measurement infrastructure for the success criterion
did not exist at deployment (gate failure on Condition 2), the specification was
scoped at the wrong granularity to produce incremental value, or the success
criterion was set at the wrong level of abstraction to detect early value
signals. In any of these cases, the gate records for the affected specifications
should be reviewed to identify the common failure pattern.

**Business value realised below 60% for any rolling four-release window.** This
is the demand layer's defining health signal. Below this threshold, the
organisation is investing more loop capacity in building things that do not
achieve their stated business purpose than in things that do. No amount of
inner-loop quality improvement addresses this problem. The root cause is in
demand validation — the evidence bar is too low, the success criteria are being
defined too loosely, or the accountable human accountability structure is not
functioning as designed.

---

## Time-to-Governance Metrics

Time-to-governance is the elapsed time between when a governance concern becomes
detectable in available data and when it enters the governance record and is
acted on. It is the governance analog of mean time to detect (MTTD) in incident
management. Low time-to-governance means governance is operating ahead of or
alongside delivery. High time-to-governance means governance is lagging —
concerns are discoverable in the data but are not being surfaced.

**T2G-Demand:** Time from when a demand intelligence signal meets the draft item
threshold to when a product owner reviews and makes a validation or rejection
decision. Target: 5 business days. A signal that produces a draft item and then
sits unreviewed is governance debt accumulating — the organisation may be
missing an obligation or an opportunity while the draft waits.

**T2G-Specification:** Time from when a specification quality signal
(inconsistent success criterion, unmeasurable acceptance criteria, missing
constraint class) is detectable by governance agent analysis to when it is
acknowledged and resolved. Target: 3 business days within the loop. A
specification quality issue that is detectable at specification entry but
surfaces as a gate failure at the release gate is a T2G-Specification failure —
the signal was present, the governance did not act on it.

**T2G-Release:** Time from when a gate condition transitions to stale or
projected-stale to when the team begins evidence regeneration. Target: within
the predictive clearing lead time window (at minimum 3 business days before
gate). Teams that consistently have T2G-Release greater than 1 business day
before the gate are not operating predictive gate clearing effectively.

**T2G-Incident:** Time from when an incident's root cause is traceable to a
governance gap (missing constraint, stale threat model, evaluation that did not
cover the failure class) to when that governance gap enters the learning closure
mechanism. Target: 10 business days from root cause analysis finalisation. A
root cause analysis that identifies a governance gap but does not produce a
learning closure record within 10 days is an open governance debt item.

**T2G-Regulatory:** Time from when a regulatory source update is published to
when its impact on the organisation's deployed systems is assessed. Target: 10
business days. An unassessed regulatory update affecting deployed systems is a
compliance exposure that compounds over time.

Track all five T2G metrics at the portfolio level, not per-system.
Portfolio-level T2G trends reveal systemic governance velocity — whether the
organisation's governance is keeping pace with its delivery pace and its
regulatory environment. T2G metrics that are trending upward as delivery
velocity increases indicate that governance is not scaling with delivery — the
human governance workforce is being outpaced, and either additional governance
agents or process changes are required.

**T2G and the governance quality score relationship.** A portfolio with
consistently high GQS but consistently high T2G is exhibiting a specific failure
pattern: when governance acts, it acts thoroughly, but it is too slow to act on
emerging signals. A portfolio with low T2G but declining GQS is the inverse:
fast but shallow. The optimal position is low T2G and high GQS — governance that
is both fast and thorough. Track the joint distribution, not just each metric
independently.

---

_These metrics are the demand layer's evidence that it is governing, not just
processing. They do not substitute for judgment — a product owner who only looks
at the numbers is not governing the demand layer. But a product owner who
governs the demand layer without these numbers is making decisions on intuition
rather than evidence. The demand layer holds the engineering execution layer
accountable for building the right thing. These metrics hold the demand layer
accountable for defining what the right thing is._

---

## On Self-Report Risk

These metrics are deliberately measured, not surveyed. Becker et al.,
*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer
Productivity* (METR, 2025, https://arxiv.org/abs/2507.09089), found that
experienced developers believed AI assistance accelerated their work by ~24%
while measured completion time increased by 19%. The implication for demand
governance is direct: stakeholder reports of "this is delivering value" are
not a substitute for the value-realisation, validation-rate, and lead-time
measurements above. Where the measured outcome and the self-reported outcome
diverge, the measured outcome is the governance evidence; the divergence
itself is a demand-layer signal worth investigating.
