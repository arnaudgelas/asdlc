# ASDLC Implementation Guide

_How to build Agentic Software Delivery Lifecycle governance, layer by layer._

See [ASDLC Overview](asdlc.md) for the architecture this guide implements. See
the [Manifesto](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto.md) for the inner-loop engineering principles.

---

## Purpose and Audience

The [ASDLC overview](asdlc.md) describes the architecture: four layers, three
gates, four feedback paths. This document describes how to build it. The
sequence matters. The outer layers have genuine dependencies on the inner loop.
Attempting to operate Layer 1 demand governance without a functioning inner loop
produces well-documented specifications that the loop cannot consistently
execute. Attempting to operate Layer 3 release governance without an inner loop
that produces complete evidence bundles produces a release gate that
rubber-stamps assertion as evidence. The adoption sequence in this guide is not
a recommendation — it reflects the actual dependency structure of the framework.

This guide is for engineering managers, platform engineers, and architects
implementing ASDLC governance. It assumes familiarity with the manifesto and the
ASDLC overview. If you have not read those two documents, read them first.

### Empirical posture

Two findings frame the discipline this guide assumes. Peng et al., *The Impact
of AI on Developer Productivity: Evidence from GitHub Copilot* (2023,
https://arxiv.org/abs/2302.06590), measured material acceleration on bounded
coding tasks — the speed premise behind ASDLC adoption is real. Becker et al.,
*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer
Productivity* (METR, 2025, https://arxiv.org/abs/2507.09089), found that
experienced developers believed AI sped them up while measured completion time
increased on realistic maintenance tasks. The pair is the load-bearing reason
this guide privileges measured outcomes — DORA metrics, validation rate, MTTR
— over self-reported velocity. CMU SEI's *AI Engineering: 12 Foundational
Practices* (2026,
https://www.sei.cmu.edu/library/ai-engineering-twelve-foundational-practices/)
is the ecosystem reference for the practice discipline this guide
operationalises in the ASDLC's lifecycle structure.

---

## Incremental Adoption Path

Build ASDLC governance in this sequence. Each step has a prerequisite. The
prerequisite is real — not a formality.

---

### Step 1: Establish inner-loop governance

**What this means.** Operate the manifesto's agentic loop at Phase 3 minimum in
at least one domain: governed agentic delivery with a functioning evaluation
portfolio, a complete evidence bundle on each loop output, and named human
accountability at the Govern phase. "Functioning" means the inner loop regularly
produces loop outputs that pass the engineering Definition of Done — not
occasionally, not in ideal conditions, but as a routine outcome. A loop that
produces evidence bundles only when reminded, or passes the DoD on an illustrative 40% of
iterations, is not at Phase 3 minimum.

**Why this must come first.** Every outer-layer governance structure receives
output from the inner loop. The release gate verifies the evidence bundle; if
the evidence bundle does not exist or is routinely incomplete, the release gate
is checking nothing. The demand layer produces loop-ready specifications; if the
loop does not reliably act on those specifications, demand governance produces
input that nothing consumes. You cannot govern a loop that does not run. Build
the loop before governing its context.

**What "done" looks like.** The team can point to a policy-set minimum of three completed loop iterations in one domain where: all eight engineering DoD conditions were
met, the evidence bundle is present and internally consistent, a named human
reviewed and accepted the output, and the loop produced no untraced failures.
Phase 3 delivery pace and quality are stable enough that a product owner can
plan against loop cycle times with reasonable confidence.

**Tooling minimum.** Evaluation framework in place. Trace store capturing
decision chains. Governance record per loop iteration. These do not need to be
sophisticated — a well-structured git repository with evaluation scripts and a
markdown governance log satisfies Phase 3 minimum. Sophistication is not the
goal at Phase 3; reliability is.

---

### Step 2: Add the Specification Readiness Gate

**What this means.** Establish the L1→L2 boundary as an enforceable checkpoint.
Before any specification enters the Specify phase, it is assessed against the
nine gate conditions defined in
[Specification Readiness](specification-readiness.md). A specification that
fails any condition does not enter the loop. The gate may be informal at this
stage — a structured checklist reviewed by the product owner and specification
analyst, with a gate decision record written into the specification document
itself — but it must be enforced: failing the gate means the specification does
not start.

**Why this comes before a full demand layer.** You do not yet have the full
demand governance infrastructure — validated backlogs, prioritisation criteria,
a formal demand-to-specification bridge. You do have a functioning loop, which
means you have encountered the failure mode this gate prevents: a specification
entering the loop that was not well-enough understood. The gate is the minimum
intervention that catches this class of failure without requiring the full Layer
1 apparatus. It is also the fastest way to learn what "loop-ready" means in
practice, because gate failures teach you exactly where specifications fall
short. That learning is the foundation for the full demand layer in Step 4.

**The two sub-gate structure.** The nine gate conditions naturally divide into
two categories with different reviewer profiles, and structuring the assessment
as two sub-gates reduces the single-session bottleneck without reducing rigour.
The Product Readiness Sub-Gate covers Conditions 1, 2, 3, 5, 7, 8, and 9
(business need, value, acceptance criteria, accountability, scope, loop cost
justification, and context thread) and is assessed by the product owner and
specification analyst. The Technical Readiness Sub-Gate covers Conditions 4 and
6 (constraints including security and compliance, and blast radius) and requires
participation from security, architecture, and compliance functions. Both
sub-gates must pass before the combined gate decision record records a pass. At
Tier 2, both sub-gates can often be assessed in a single session; at Tier 3, the
Technical Readiness Sub-Gate should be scheduled separately, after the Product
Readiness Sub-Gate has passed, to avoid consuming security and compliance
reviewers' time on specifications that have not yet established their business
case.

**The most common gate failures at this step.** Condition 2 (value measurable)
and Condition 7 (out-of-scope explicitly stated) are the conditions that teams
most commonly underestimate. Most teams entering this step have been writing
specifications with vague success criteria and implicit scope boundaries. Both
patterns are immediately visible when assessed against the gate. Treat each gate
failure as a data point: record which condition failed, what was missing, and
what was required to satisfy it. After ten gate assessments, you will have a
clear picture of the specific gaps in your current specification practice —
which is exactly what you need to design the demand layer in Step 4.

**What "done" looks like.** The gate has been run on every specification
entering the loop for at least one full month. Gate decision records exist for
each assessment. At least one specification has been blocked at the gate and the
result of blocking it was positive — either the specification was strengthened
and entered the loop in better shape, or the work was deprioritised entirely
because the gate revealed it was not well-enough understood.

---

### Step 3: Add the Release Gate

**What this means.** Establish the L2→L3 boundary as an enforceable checkpoint.
A loop-complete output — one that has passed the engineering DoD — does not
proceed to production deployment without passing all eight release gate
conditions: evidence bundle complete, independent validation passed, rollback
procedure tested, accountable human sign-off, compliance documentation
complete, dynamic security testing passed, control state record complete and
current, and waiver governance satisfied. The release gate is run by the
release manager, not the
development team. The release manager is checking the evidence, not repeating
the engineering work.

**Why this comes before a full Layer 3.** The full release layer — deployment
pipelines, change management integration, environment promotion mechanics — is
substantial infrastructure. The release gate is the minimum governance structure
that prevents the most consequential failure mode at this boundary: deploying
unverified or ungoverned output to production. The gate can be run manually
against a checklist while the deployment infrastructure is being built. A
release manager reviewing an evidence bundle checklist before each production
deployment is operating a release gate. Formality and automation come later; the
gate condition comes now.

**The rollback procedure requirement deserves attention.** Most teams that add a
release gate for the first time discover that they have never tested a rollback
procedure. They may have documented one. They have not tested it. The rollback
test condition — tested in a representative environment, within a policy-set 48 hours of the
planned production deployment, with time-to-rollback measured — should be
treated as non-negotiable from the first gate run. The failure mode it prevents
— the first rollback attempt failing in production during an active incident —
is preventable exactly once. After that, it is a lesson that costs more than the
test would have.

**What "done" looks like.** Every production deployment for the past month has
passed a release gate. A release gate decision record exists for each
deployment. At least one deployment was blocked at the gate and the block was
justified — the evidence bundle was incomplete, the rollback had not been
tested, or the compliance documentation was in draft. The team treats the gate
as a quality standard, not a bureaucratic hurdle.

---

### Step 4: Add the Demand Layer

**What this means.** Establish full Layer 1 governance: a demand backlog owned
by a named product owner, validation evidence requirements proportionate to
blast radius tier, a measurable success criterion for every item, prioritisation
criteria documented and applied consistently, a capacity model that prevents
backlog oversubscription, and the demand-to-specification bridge (decomposition,
translation, gate). This is not a small step. Full demand layer governance is an
organisational change, not a tooling addition. It requires the product owner
role to shift from coordination to specification governance, and it requires
business demand sponsors to accept explicit accountability for validation
evidence and success criteria.

**Why this comes after the release gate and not before it.** The demand layer
produces loop-ready specifications. To produce them well, you need to know what
"loop-ready" means from the inside — what the loop actually needs, where
specifications fail, what the gate catches. Steps 2 and 3 give you that
knowledge. Teams that build the demand layer before operating the inner loop and
gate produce formal demand processes that generate specifications with the right
structure but the wrong content, because they have no feedback from actual loop
execution. The demand layer works best when it is calibrated against real loop
experience.

**The most important demand layer decision.** The capacity model. The number of
simultaneous loop iterations that can be governed well is bounded by the
availability of named accountable humans to review evidence bundles. Count the
evidence bundles that require human review per sprint cycle. Count the hours
available from named accountable reviewers. If the review load exceeds capacity,
the demand backlog is oversubscribed. This calculation is the forcing function
for a realistic demand layer: it makes the cost of each loop iteration visible,
and it makes the consequences of oversubscription predictable — loop quality
degradation, rubber-stamping, and evidence bundle shortcuts — rather than
invisible until they produce a failure.

**What "done" looks like.** A demand backlog exists with explicit ownership,
validation evidence attached to every item, and documented prioritisation
criteria. No specification enters the loop without a gate decision record. The
business demand sponsor for each active loop iteration is named and reachable.
The capacity model has been calculated and the number of active loop iterations
is within the calculated governance capacity.

---

### Step 5: Add Operational Readiness Gate and Runbooks

**What this means.** Establish the L3→L4 boundary as an enforceable checkpoint.
Before a deployed system transitions to steady-state operations, it must pass
all eight operational readiness gate conditions: runbook complete, SLOs defined
and monitoring configured, on-call engineer assigned and briefed, system steward
assigned, security scan clean, license compliance confirmed, trace retention
policy set and configured, and DR/failover tested (for Tier 3 systems). The gate
is assessed by the system steward, not the
release manager.

**The runbook is the most labour-intensive condition.** A runbook that satisfies
the operational DoD is not a one-page overview. It contains an architecture
diagram accurate to the deployed version, alerting thresholds with documented
rationale, known failure modes with diagnostic steps, the escalation chain with
current contact information, and a rollback procedure with tested
time-to-rollback. For agent-generated systems, the runbook must also link to the
specification and evidence bundle for the deployed version — because when an
incident occurs, the on-call engineer's reference for "what was this system
supposed to do" is the specification, not the code author.

**The system steward role.** The steward is the ongoing governance anchor for
the system in production. They are responsible for quarterly operational DoD
reviews, for ensuring the runbook stays current across releases, for owning the
escalation path when incidents require governance decisions, and for initiating
the retirement process when the system's operational lifetime ends. The steward
is not the on-call engineer. The on-call engineer handles first-triage; the
steward handles governance decisions — accepting known risks, authorising
production changes outside the normal release cycle, initiating retirement.
Naming a steward without briefing them on these responsibilities produces a
title, not an accountability.

**Steward portfolio limits.** A steward accountable for too many systems
simultaneously cannot maintain the knowledge depth and review cadence that
meaningful stewardship requires. As a policy-set practitioner default — chosen
by the authors, not measured from steward workload data, and to be calibrated to
local system complexity — no single steward should be accountable for more than
five Tier 3 systems, ten Tier 2 systems, or twenty Tier 1 systems concurrently.
A steward approaching these limits without additional support or tooling
assistance is at risk of operational DoD review gaps, knowledge degradation
between systems, and inability to pass the P12 accountability test for their
full portfolio.

Where stewardship portfolio limits are being approached, the response is either
to distribute stewardship across additional qualified stewards or to invest in
tooling-assisted monitoring for the conditions that lend themselves to
automation: security scan recency, SLO configuration state, on-call assignment
presence, and runbook modification date can be monitored automatically, reducing
the manual review burden without eliminating steward judgment. The conditions
that require active judgment — knowledge depth, specification currency, value
realisation monitoring — cannot be automated. Tooling-assisted monitoring of the
automatable conditions makes the judgment-requiring conditions manageable across
a larger portfolio.

**Observability instrumentation standards.** Operational observability
instrumentation should be implemented using vendor-neutral standards to ensure
portability across tooling choices and to prevent lock-in to specific
observability platforms. The OpenTelemetry (OTel) specification, maintained by
the Cloud Native Computing Foundation, defines the vendor-neutral standard for
traces, metrics, and logs across the observability stack. Implementing
OTel-compatible instrumentation means that the operational observability data
required by the ASDLC's Layer 4 governance conditions can be collected,
exported, and analysed independently of specific vendor platforms. This is
particularly relevant for reasoning trace capture: traces emitted in
OTel-compatible formats can be correlated with service observability data, which
makes incident investigation more tractable than maintaining separate,
incompatible trace stores.

**What "done" looks like.** Every production system has a current runbook, a
named steward who has reviewed the specification and evidence bundle, and a
named on-call engineer who has been briefed. A quarterly operational DoD review
is scheduled. The first review has been completed and its output (a confirmation
that all conditions are satisfied, or a list of conditions failing and the
remediation steps) is documented.

---

### Step 6: Add Full Maintenance Governance

**What this means.** Extend Layer 4 governance to cover the full operational
lifetime of the system: scheduled dependency update cycles, security patch SLAs,
end-of-life planning for model versions and library dependencies, stewardship
transfer procedures when personnel change, and the retirement process for
systems reaching end of operational life. See
[Maintenance Governance](maintenance-governance.md) for the full specification.

**Why this is the last step.** Maintenance governance is only meaningful if the
system is already in a governed operational state. A stewardship transfer
procedure is useless if the steward was never properly assigned. An end-of-life
retirement process is useless if the system has no operational DoD to measure
against. Step 5 establishes the operational baseline; Step 6 extends it across
the system's lifetime. Teams that add maintenance governance before establishing
the operational readiness gate produce maintenance procedures that have nothing
to maintain.

**What "done" looks like.** Every production system has a scheduled dependency
update cycle on the maintenance calendar. Security patch SLAs are defined and
monitored. The retirement trigger conditions — what would cause this system to
be decommissioned — are documented in the runbook. At least one stewardship
transfer has been performed and the transfer procedure worked: the incoming
steward can pass the P12 accountability test (can recover intent, decisions, and
evidence from the specification and evidence bundle without assistance from the
outgoing steward).

---

## Common Failure Modes

The following anti-patterns appear consistently across ASDLC adoptions. Each is
described with its symptom, root cause, and the specific fix.

---

### Outer-layer governance without inner-loop maturity

**Symptom.** The organisation has formal demand processes, release procedures,
and operational runbooks. Loop output quality is low, validation fails
consistently, and the governance overhead feels disproportionate to the value
delivered.

**Root cause.** The outer layers were built before the inner loop reached Phase
3 minimum. The demand layer is producing well-formed specifications that the
loop cannot reliably execute. The release gate is checking evidence bundles that
are routinely incomplete. The operational runbooks reference systems whose
behaviour is not well-understood because the loop's Learn and Observe phases are
not functioning.

**Fix.** Pause outer-layer governance investment and treat inner-loop
reliability as the priority. The test is: can the loop produce a policy-set three consecutive evidence-complete loop outputs in one domain without intervention? Until that
test passes, outer-layer governance is generating process overhead for a loop
that cannot satisfy it. Once the loop is reliable, the outer layers become
productive immediately because they have complete evidence to work with.

---

### Inner-loop without demand layer

**Symptom.** The loop runs reliably. Verification pass rates are high.
Validation fail rates are also high — the system built the right thing
technically but not the right thing for the business. Teams are shipping at
speed but the business success criteria are frequently not met post-deployment.

**Root cause.** The loop is receiving specifications that have not been
validated against real business need, or whose success criteria were not defined
before the loop ran. The Validate phase has nothing to validate against. High
verification pass rate combined with low validation rate is the diagnostic: the
engineering is sound; the specification was wrong from the start.

**Fix.** Add the Specification Readiness Gate (Step 2 above) immediately. The
gate's Condition 2 (value measurable) and Condition 1 (business need validated)
are the direct interventions for this failure mode. Once the gate is running,
the validation failure rate will drop — not because the loop changed, but
because the specifications entering it changed. If validation failures persist
after the gate has been running for a month, escalate to a demand layer
retrospective: the gate conditions are necessary but the validation quality
problem may have a deeper root cause in the translation step.

---

### Release governance without rollback testing

**Symptom.** The release gate is operational and the team complies with it. On
the first occasion that a production rollback is required, the rollback fails:
the procedure was documented but never tested, the environment configuration has
drifted from the test environment where the procedure was notionally valid, and
the rollback takes three times longer than the agreed window.

**Root cause.** The release gate's rollback procedure condition was satisfied by
documentation rather than testing. "We have a rollback plan" was treated as
equivalent to "the rollback procedure works." These are different claims.

**Fix.** The fix is preventative: enforce the test condition from the first gate
run. The release gate condition is tested rollback, not documented rollback. If
the team's current release gate treats documentation as sufficient, the
condition is not met. Re-run every pending release against the tested rollback
condition before the first production rollback is needed. The cost of this fix
is a few hours of testing per release. The cost of the failure it prevents is a
production incident with no working remediation path.

---

### Operations without stewardship

**Symptom.** Systems in production accumulate quietly. Nobody knows who is
responsible for which system. Runbooks are stale or absent. When an incident
occurs, escalation discovers that the named accountable human listed at
deployment no longer works at the organisation. Security vulnerabilities
accumulate because no one owns the dependency update cycle.

**Root cause.** The operational readiness gate was never established, or was run
at deployment and then treated as a one-time event rather than a maintained
state. The operational DoD requires conditions to be true at any point in the
system's lifetime, not just at first deployment. A steward who leaves without a
qualified replacement puts the system into operational DoD failure.

**Fix.** Establish the quarterly operational DoD review and make the steward
accountable for conducting it. The review is not a detailed technical assessment
— it is a confirmation that each of the eight operational DoD conditions remains
satisfied, and an identification of any that are failing. For organisations with
large fleets of production systems, the operational DoD review can be
tooling-assisted: automated checks for security scan recency, SLO configuration,
on-call assignment, and runbook update recency surface the most common
compliance gaps without requiring manual review of every condition for every
system.

---

### Feedback paths unowned

**Symptom.** The same class of failure recurs across multiple release cycles. A
pattern of validation failures that traces to underspecified success criteria
appears in retrospective after retrospective. A pattern of release gate failures
that traces to missing compliance documentation recurs despite being identified.
The feedback mechanisms exist — the feedback signals are captured — but the
failures persist.

**Root cause.** Feedback paths are unowned. When a validation failure occurs,
the post-incident review produces a finding. The finding is acknowledged. No
process change is made. The next specification entering the loop has the same
success criterion gap. The feedback loop has no owner accountable for converting
the signal into a process change.

**Fix.** Each feedback path must have a named owner accountable for acting on
the signal. L2→L1 validation failures: the product owner owns the demand layer
retrospective and the process change. L3→L2 release failures: the release
manager and the engineering lead jointly own the loop-level change. L4→L2
maintenance signals: the system steward owns the specification and evaluation
update. L4→L1 value misses: the business demand sponsor owns the demand process
retrospective. Without named ownership, feedback signals produce observations,
not changes. Observations do not prevent recurrence. A feedback path with no
time-bound SLO is not enforced — it is a suggestion. The SLOs defined in the
ASDLC overview are the minimum standard. Teams that lack the organisational
structure to meet the SLOs should treat that as a governance infrastructure gap
to be closed, not as evidence that the SLOs are too demanding. The SLOs are
calibrated to prevent the same failure class from compounding across multiple
release cycles, which is the only class of harm the feedback paths were designed
to prevent.

---

## Integration with Existing Frameworks

### SAFe

If your organisation operates SAFe, the ASDLC maps to the SAFe planning
hierarchy at each level with specific integration points.

**Layer 1 ↔ Portfolio and Program.** The demand backlog corresponds to the
Program Backlog managed by the Product Manager. ASDLC demand validation aligns
with SAFe's Lean Business Case: the validation evidence required at Tier 2 and
Tier 3 is the evidence base for a Lean Business Case. Prioritisation criteria —
value × urgency × risk × strategic alignment — map directly to WSJF (Weighted
Shortest Job First), with the ASDLC adding explicit blast radius and strategic
alignment dimensions. The capacity model corresponds to SAFe's PI Planning
capacity allocation. The integration point: treat the ASDLC demand backlog as
the input to the SAFe Program Backlog, with each item required to have passed
Tier-appropriate validation before entering PI Planning.

**Layer 2 ↔ Team.** The agentic loop is the Team level execution mechanism. Loop
iterations correspond to Team Iteration cadence. The Specification Readiness
Gate corresponds to the Feature/Story readiness definition that teams agree
before committing to PI Objectives. Integration point: make gate decision
records the artefact that proves a story is "ready" in the SAFe Definition of
Ready.

**Layer 3 ↔ Release Train.** The Release Gate corresponds to the Release Train's
release management checkpoint. The evidence bundle is the artefact that
satisfies the Release Train Engineer's release readiness review. The deployment
pipeline and change management integration described in
[Deployment Governance](deployment-governance.md) is the implementation of the
ART's Continuous Delivery Pipeline. Integration point: ASDLC release gate
conditions replace or extend the Release Train's existing release readiness
checklist.

**Layer 4 ↔ Operational Value Stream.** Layer 4 governance corresponds to SAFe's
Operational Value Stream. The system steward role corresponds to the System
Owner. Integration point: operational DoD quarterly review maps to SAFe's
Inspect and Adapt operational review cycle.

---

### ITIL

For organisations operating ITIL, the ASDLC's outer layers define what agentic
execution adds to the ITIL practices they already operate.

**Change Management (Layer 3).** The ASDLC evidence bundle is the RFC (Request
for Change) documentation for agentic system changes. The evidence bundle ID is
the RFC reference. The accountable human sign-off is the Change Authority
approval. The release approval chain maps to the Change Advisory Board for
Significant Changes and Normal Changes. The ASDLC adds to ITIL Change
Management: the requirement for a tested rollback procedure (ITIL requires a
documented back-out plan; the ASDLC requires a tested one), and the evidence
bundle structure (ITIL Change Management does not specify the content of change
evidence; the ASDLC's eight-condition evidence bundle does). Integration point:
populate ITIL change records from the ASDLC release gate artefacts — do not
duplicate documentation.

**Service Transition (Layer 3→4 boundary).** The ASDLC's Operational Readiness
Gate is the Service Transition governance checkpoint. It maps to ITIL's Service
Transition Management practice: the operational DoD conditions are the
acceptance criteria for transitioning a service from development to operations.
The system steward corresponds to the Service Owner. Integration point: treat
the operational DoD gate decision record as the Service Acceptance Criteria
assessment.

**Incident Management (Layer 4).** The ASDLC's incident classification — adding
quality incidents to the standard infrastructure and application incident
categories — extends ITIL Incident Management for agentic-specific failure
modes. Output quality SLOs and the sampling process are the detection mechanism
for quality incidents; ITIL's standard monitoring does not cover them.
Integration point: add quality incident as a formal incident classification in
your ITIL tooling, with the output quality SLO threshold as the trigger
condition.

**Problem Management (Layer 4→2 feedback path).** The L4→L2 maintenance signal
feedback path is the operational manifestation of ITIL Problem Management. ITIL
identifies root causes; the ASDLC specifies what must be updated as a result —
the specification, the evaluation portfolio, the memory — and names the owner of
that update. Integration point: ITIL Problem Records for agentic systems must
reference the specification and evidence bundle they require to be updated, and
the system steward must be the named owner of the Problem Record's resolution
action.

---

### DORA

The DORA four key metrics are outcome measures for delivery system health (see
the *Accelerate State of DevOps Report 2024*, https://dora.dev/research/2024/,
and the metrics guide at https://dora.dev/guides/dora-metrics/). The ASDLC's
gate structures are the mechanisms that produce those outcomes. The
integration is not architectural — it is about understanding which governance
conditions the metrics are sensitive to. The 2024 report's finding that AI
adoption can coexist with reduced delivery stability when fundamentals are
weak is directly relevant: the speed gain that motivates ASDLC adoption is not
self-justifying if it degrades change failure rate or mean time to restore.

**Deployment frequency.** Deployment frequency is constrained by: loop iteration
cycle time, evidence bundle completeness rate, and release gate pass rate on
first submission. If deployment frequency is below target, the most productive
diagnostic is release gate failure rate: what fraction of loop outputs fail the
release gate on first submission, and which conditions are failing? A high rate
of rollback procedure failures at first gate submission is a signal that
rollback testing is not being treated as an integral part of the loop — it is
being deferred to the gate and frequently not ready. A high rate of evidence
bundle incompleteness is a signal that the engineering DoD is not being
consistently applied inside the loop.

**Lead time for changes.** Lead time is the elapsed time from specification
readiness gate pass to production deployment. Demand layer cycle time — the time
from initial need identification to gate-ready specification — is upstream of
this metric and not captured by DORA. If demand layer cycle time is long, the
DORA lead time metric understates the total delivery latency. Measuring from
gate-ready specification is necessary for the DORA metric; measuring from
initial need identification is necessary for the full-lifecycle view.

**Change failure rate.** Change failure rate — the proportion of deployments
requiring remediation — is directly affected by: specification readiness gate
thoroughness (poorly validated specifications produce loop outputs that fail in
production), release gate completeness (missing evaluation coverage surfaces in
production), and rollback procedure quality (failed rollbacks extend incidents).
If change failure rate is high, the diagnostic is: are the failures tracing to
specification quality (demand layer gap), evaluation coverage (inner loop gap),
or infrastructure configuration (deployment governance gap)?

**Mean time to restore.** MTTR is directly governed by the operational readiness
gate conditions: tested time-to-rollback in the runbook, on-call briefing on the
rollback procedure, and the escalation chain from on-call engineer to
accountable human. Organisations that skip the operational readiness gate and
find that MTTR is high during incidents should treat the gate conditions as the
first-order diagnostic — specifically, whether the rollback procedure was
tested, whether the on-call engineer was briefed on it, and whether the
escalation chain is current.

---

### Regulated SDLC frameworks

The ASDLC is not a replacement for IEC 62304, GAMP 5, DO-178C, or equivalent
regulated SDLC frameworks. It is the governance framework that defines where
agentic execution fits within them. The following integration guidance applies
to each.

**IEC 62304 (Medical device software).** IEC 62304 is a **paid IEC standard
that this programme has not purchased and has not read**; it is **OPEN under
`T6.5`**, **no unofficial copy was fetched, sought or considered**, and per
`asdlc.md` *"nothing here asserts what they require."* The mapping below is
therefore **the ASDLC's own construction and is unsourced**, including the
clause numbers, which are reproduced from secondary usage and **have not been
checked against the standard**. The ASDLC's reading: the agentic loop's
Specify→Verify phases correspond to the software development lifecycle (5.1–5.7);
the evidence bundle is the software development record; the Specification
Readiness Gate corresponds to the software requirements activity (5.2), ensuring
software requirements are documented and consistent with the system design
inputs before development begins; and the release gate's independent validation
condition corresponds to software verification and validation (5.6, 5.7). The
ASDLC makes independent verification a blocking condition for its highest risk
class. **Whether IEC 62304 requires independent verification for Class C, and
whether these clause numbers carry the content stated, has not been checked and
cannot be while the standard is unread.** Integration point: the gate decision
records and evidence bundles in the ASDLC are intended as the primary
development records. Do not maintain separate development records — reference
the ASDLC artefacts from the IEC 62304 record structure, once that structure has
been read from a purchased copy.

**GAMP 5 (Pharmaceutical automated systems).** GAMP 5 is a **paid ISPE guide
that this programme has not purchased and has not read**; it is **OPEN under
`T6.5`**, **no unofficial copy was fetched, sought or considered**, and per
`asdlc.md` *"nothing here asserts what they require."* The correspondence below
is **the ASDLC's own construction and is unsourced** — what the ASDLC
understands the industry-common V-Model vocabulary to mean, not a reading of the
guide. On that understanding the V-Model maps to the ASDLC's inner loop and
outer layers: User Requirements Specifications correspond to demand layer
outputs (validated need, success criterion,
acceptance criteria). Functional and Design Specifications correspond to Specify
and Design phases. Factory Acceptance Testing and Site Acceptance Testing
correspond to the Verify and Validate phases. Installation Qualification is the
release gate and the Operational Readiness Gate combined. Operational
Qualification is the first production operation period (the system operating
against its SLOs in production). Performance Qualification is the steady-state
operational phase. Integration point: map GAMP 5 V-Model documents to ASDLC
artefacts one-to-one. The ASDLC artefact is produced by the loop; the GAMP 5
document reference is filed against it. **Confirm the mapping against a
purchased copy of the guide with the organisation's quality team before relying
on it; it has not been checked and cannot be while the guide is unread.**

**DO-178C (Airborne software).** DO-178C is a **paid RTCA standard that this
programme has not purchased and has not read**; it is **OPEN under `T6.5`**,
**no unofficial copy was fetched, sought or considered**, and per `asdlc.md`
*"nothing here asserts what they require."* The correspondence below is
therefore **the ASDLC's own construction and is unsourced** — what the ASDLC
understands the industry-common airborne-certification vocabulary to mean, not a
reading of the standard, and that includes the section numbers, which are
reproduced from secondary usage and **have not been checked against the
standard**. On that understanding: the objectives for software development and
verification map to the inner loop's phases and the release gate; the Software
Development Plan, Software Verification Plan, and Software Configuration
Management Plan correspond to the Design and Govern phases of the loop; software
verification evidence corresponds to the evidence bundle; and the review and
audit objectives the ASDLC associates with Section 7 correspond to the
independent validation condition at the release gate. Critical distinction: the
evidence expected of a certified airborne programme is substantially more
detailed and prescriptive than the ASDLC's general framework. For software in
DO-178C scope, the ASDLC provides the governance architecture; the programme's
own DO-178C planning documents specify what the evidence bundle must contain to
satisfy each objective. These are not interchangeable. **Whether DO-178C states
any of this, and whether these section numbers carry the content stated, has not
been checked and cannot be while the standard is unread.** Confirm against a
purchased copy before relying on this mapping. Certification is a matter for the
certification authority and the programme's DER or ODA unit member, not for
ASDLC gate compliance.

**SR 11-7 and SS1/23 (Model risk — financial services).** SR 11-7 addresses
model development and validation in US banking; PRA **SS1/23, *Model risk
management principles for banks*, May 2023** is the UK counterpart, in effect
from 17 May 2024.
**SR 11-7 is supervisory guidance written in "should", not a set of
requirements** — `should` occurs 180 times against a single `must` in the
attachment held at
`inputs/20260905-arnaud/prep/D-20-primary/sources/sr1107a1.txt` (sha256
`d8ef343917…`), and the successor guidance SR 26-2 (17 April 2026) states that
it *"does not set forth enforceable standards or prescriptive requirements;
accordingly, non-compliance with this guidance will not result in supervisory
criticism against a banking organization"* — quoted to the end of the sentence,
which carries footnote 1: *"See 12 CFR Part 4, Subpart F, Appendix A (OCC); 12 CFR Part 262,
Appendix A (Board); 12 CFR Part 302, Appendix A (FDIC). However, supervisory
action may result for any violations of law or unsafe or unsound practices
stemming from insufficient management of model risk."*
**This strengthens the "written in expectations" point and limits it in the
same breath**: the guidance is not the enforcement hook, but supervisory action
may still follow through violations of law or unsafe-or-unsound practices, so
non-enforceable does not mean consequence-free.
**SS1/23 is in the same register, and this was checked at the primary rather
than assumed.** It was retrieved free from bankofengland.co.uk on 2026-09-06
(HTTP 200, first attempt) and is held at
`inputs/20260905-arnaud/prep/ss123/sources/pra_ss1_23.pdf` (sha256
`6165a8ba69…`). Over that document `should` occurs **179** times and `must` and
`shall` occur **zero** times each; it *"sets out the PRA's expectations for
banks' model risk management"* and is *"structured around five high-level
principles"* — model identification and risk classification, governance, model
development/implementation/use, independent model validation, and model risk
mitigants. **Its scope is narrower than the US guidance's**: by its own § 1.2 it
applies
to UK-incorporated banks, building societies and PRA-designated investment firms
**with internal model approval** for regulatory capital, and *"the expectations
in this SS do not apply to firms which do not have permission to use internal
models"*, nor to credit unions, insurers or reinsurers. **Neither instrument
places a requirement on a firm by force of the document itself; both are written
in expectations.** SR 11-7 says a validation framework *"should include three core elements:
• Evaluation of conceptual soundness, including developmental evidence •
Ongoing monitoring, including process verification and benchmarking • Outcomes
analysis, including back-testing"*, that validation *"should be done by people
who are not responsible for development or use"*, and that *"Material changes in
model structure or technique, and all model redevelopment, should be subject to
validation activities of appropriate range and rigor before implementation"*.
The ASDLC maps these to the specification and design rationale in the evidence
bundle, the release gate's independent validation condition, the output quality
SLO and monitoring conditions in the operational DoD, and the release approval
chain for changes to model-bearing systems. **That the gate conditions are a
sufficient governance structure, and that high-risk models need more than the
ASDLC minimum, are the ASDLC's own judgements and are unsourced** — the gate
condition is necessary but not sufficient, and passing it is not a compliance
determination. See the financial services domain file in `domains/` for the full
mapping.

---

## Phase-Calibrated ASDLC Requirements

The outer layers are not all-or-nothing. They scale with inner-loop maturity.
The following table shows which ASDLC requirements are active at each inner-loop
phase.

| Phase     | Layer 1 (Demand)                                                                                                                                                                                | Layer 3 (Release)                                                                                                                                                                            | Layer 4 (Operations)                                                                                                                                                          |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Phase 1–2 | Informal need validation — confirm that some evidence exists before the loop runs; no formal gate required                                                                                      | Basic release record — what was deployed, when, by whom; no formal gate                                                                                                                      | No formal requirement — runbook optional, steward optional                                                                                                                    |
| Phase 3   | Specification readiness gate (informal checklist, product owner-led); success criterion required for all loop entries                                                                           | Full release gate: evidence bundle complete, rollback tested, accountable human sign-off; compliance documentation where the change's risk profile requires it                               | Runbook (reduced scope) + on-call assignment + steward assigned + security scan; SLO configuration required if external consumers exist                                       |
| Phase 4   | Formal demand governance: validated backlog with explicit ownership, documented prioritisation criteria, gate decision records for all Tier 2+ specifications, business demand sponsor sign-off | Release approval chain: tech lead + release manager for Tier 2; plus accountable human written acceptance for Tier 3; compliance officer for regulated systems; all gate conditions enforced | Full operational DoD: all eight conditions required; quarterly DoD review scheduled; maintenance cycle defined                                                                 |
| Phase 5   | Full Layer 1: formal demand governance + demand metrics (see `demand/metrics.md`); feedback path from L4 value data actively monitored; capacity model calculated and enforced                  | All release gate conditions enforced without exception; release metrics tracked; emergency change procedure tested                                                                           | Full Layer 4 with maintenance governance: stewardship transfer procedures tested, dependency update cycles scheduled, end-of-life planning current for all production systems |

The phase calibration reflects a genuine dependency: at Phase 1–2, the loop
itself is not reliable enough to benefit from full outer-layer governance. The
outer layers add process overhead; the inner loop does not yet produce the
consistent output that outer-layer governance processes. At Phase 5, the outer
layers are not bureaucratic additions — they are the governance infrastructure
that makes Phase 5 autonomy safe to operate.

**The transition decision.** Moving from Phase 3 to Phase 4 outer-layer
requirements is not automatic. It is triggered by two signals: inner-loop stability (consistent evidence-complete outputs across a policy-set minimum of ten loop iterations in the domain) and a specific outer-layer failure mode appearing that
the Phase 3 minimum does not prevent. Do not escalate outer-layer governance
requirements ahead of those signals — it creates overhead without benefit. Do
not defer escalation after those signals — it creates risk without the
governance infrastructure to manage it.

---

## Governing the ASDLC at Organisational Scale

The ASDLC adoption path in this guide assumes a team or a small set of teams
working toward a single maturity phase. Large organisations simultaneously
operate teams at different phases across different products, domains, and
geographies. The governance decisions that arise from this multi-phase,
multi-team reality are not covered by the per-team adoption path — they require
deliberate organisational-level governance decisions.

**Phase calibration across a portfolio.** When teams at different inner-loop
phases produce changes that affect shared infrastructure, the governing phase
for the shared infrastructure is the lowest phase of any team whose changes it
accepts. A shared authentication service that receives changes from both a Phase
4 team (with full evidence bundles and formal release governance) and a Phase 2
team (with informal processes) cannot operate Phase 4 release governance for
only the Phase 4 team's changes: every change to the shared service must meet
the standard of the most demanding governance requirement that applies to that
service, which in practice means meeting the higher standard for all changes.
This creates an incentive to accelerate lower-phase teams to the shared
service's required maturity level rather than accepting asymmetric governance.

**Shared infrastructure governance.** Platform teams that provide shared
infrastructure — evaluation registries, model serving layers, memory stores,
routing infrastructure — hold their own governance obligations separately from
the delivery teams that consume them. A platform change that could degrade
evaluation correctness for multiple consuming teams has a blast radius that
spans all consuming teams, not just the platform team's domain. The blast radius
assessment for platform changes must account for this aggregate impact.

**Multi-team release coordination.** When changes from multiple teams enter the
same release window, each change's evidence bundle and release gate assessment
is evaluated independently. A release gate failure for one team's change does
not automatically block another team's change unless there is a direct
dependency. Release managers coordinating multi-team releases must document the
dependency relationships between changes before the release window opens, so
that gate failures propagate correctly to dependent changes without causing
unnecessary hold-ups for independent ones.

**Cross-team feedback path ownership.** The ASDLC's feedback paths assume a
single team owns both the signal and the response. In multi-team contexts, L4
value data feeds into L1 demand governed by a different team's product owner; L3
release failures may implicate both the development team and the platform team.
Each feedback path in a multi-team context must have an explicit named owner at
each end: the team that generates the signal and the team accountable for the
process change it requires. An unowned feedback path in a multi-team context
will not route to the correct owner by default.

---

_The ASDLC is an architecture. This guide is how you build it. The sequence is
not arbitrary — each step creates the prerequisite for the next. Start where you
are. Build what the next step requires. Measure whether it worked._
