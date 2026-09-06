# Release & Deployment Governance — Layer 3

_The Agentic Software Delivery Lifecycle, Layer 3: Release & Deployment._

See [manifesto.md](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto.md) for the core values and the Agentic Loop.
See [manifesto-done.md](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto-done.md) for the Definition of Done. See
[deployment-governance.md](deployment-governance.md) for environment management
and promotion mechanics. See
[operations/governance.md](operations/governance.md) for what happens after
production deployment.

---

## What is the Release & Deployment Layer?

Layer 3 begins where the engineering execution loop ends. A loop output that has
met all eight Definition of Done conditions — Loop-Complete, Traceable,
Verified, Provable, Learned from, Governed, Economical, and Within Service
Envelope — is not yet production-ready:
it is loop-complete. Those conditions prove that the engineering work was sound.
They do not prove that deploying it to production now is the right decision, at
the right time, with the right authorisations, in the right environment state.
The release layer governs the journey from loop-complete to production-deployed,
with the accountability and compliance requirements that distinction requires.
Engineering governs what was built and whether it works. Release governance
governs whether it should be deployed, by whom, and under what conditions. Both
are necessary. Neither substitutes for the other.

---

## Release Readiness Criteria — The Release Gate

The handoff from Layer 2 (Engineering Execution) to Layer 3 (Release &
Deployment) is not automatic. A loop-complete output arrives at the release
boundary with an evidence bundle. The release layer's first job is to verify
that the bundle is complete and that each component satisfies the conditions
that make a release decision legitimate. The release layer does not produce
evidence — the loop produces evidence. The release layer verifies it.

Eight conditions constitute the release gate. All eight must be met before a
deployment decision is authorised. A partial set is not a "mostly ready" release
— it is an incomplete release that should not proceed.

---

## Predictive Gate Clearing

The release gate is a boundary, not a discovery mechanism. Its purpose is to
prevent loop-complete output from entering production before accountability,
rollback, and compliance conditions are satisfied — not to discover what
conditions are missing. In a well-instrumented agentic SDLC, gate failures
should be rare because gate readiness is continuously monitored and deficiencies
are surfaced and resolved before the gate assessment is scheduled.

Predictive gate clearing is the agentic capability that makes this possible.

**Continuous gate readiness monitoring.** From the moment a specification enters
Layer 2, a governance agent continuously monitors gate readiness for the release
gate. At any point, the gate readiness model computes:

- For each release gate condition: current GateState (from the governance
  graph), evidence artefact freshness trajectory, and projected GateState at the
  expected release gate date
- The overall gate readiness score: proportion of conditions in pass or
  projected-pass state, with conditions in missing, stale, projected-stale, or
  fail weighted by their criticality
- Blocking conditions: conditions that must be resolved before the gate can
  pass, ranked by resolution lead time (how long does it typically take to
  generate this type of evidence?)

**Gate readiness report.** The gate readiness report is updated at minimum daily
during active loop iterations and surfaced to the engineering lead and release
manager. It is not a dashboard metric — it is an actionable report: "Condition 3
(independent validation) will be missing at the current pace; the independent validation lead time for this system type is typically 5 business days; the release gate is scheduled in 7 days." Both figures in that
example are illustrative — they show the shape of an actionable report, not
lead times this document sets. The report gives enough lead time for action,
not just notification.

**Projected-stale classification.** `projected-stale` is an operational
GateState value used in predictive gate clearing, distinct from the formal
`stale` GateState, which reflects current state. A condition is
`projected-stale` when its current evidence will cross a freshness threshold
before the scheduled gate date given event-triggered staleness rules.
`projected-stale` is not a formal gate condition state — it is a planning signal
that should prompt pre-emptive evidence regeneration.

**Predictive blocking threshold, policy-set.** When the gate readiness score drops below 60% with more than 3 business days until the scheduled gate — both figures chosen by the authors rather than fitted to observed gate outcomes — the engineering lead
and release manager receive an immediate notification (not a scheduled report).
This threshold is calibrated to provide enough lead time for the most common
blocking conditions to be resolved. An engineering team that regularly encounters predictive blocking notifications in the 1–2 business day window
before a gate is accepting gate failures as a risk management choice, not
operating a governed gate process.

**Learning from prediction accuracy.** Track the accuracy of gate readiness
predictions over time. A prediction model that consistently underestimates how
many conditions will be failing at gate time has a false confidence problem — it
is not detecting leading indicators of gate failure correctly. Prediction
accuracy is tracked as a governance quality metric for the predictive clearing
function: if prediction accuracy falls below a policy-set 70% over a policy-set rolling 10-gate window, the gate readiness model requires recalibration.

---

### 1. Evidence Bundle Complete

All eight engineering Definition of Done conditions have been met, and the
artefacts that prove them are present and referenced. The evidence bundle is not
a document describing what was done. It is a collection of machine-readable
artefacts: evaluation reports with pass/fail results and metrics, trace IDs
linking to the full decision chain from specification to execution to output,
diffs showing exactly what changed, policy check outputs confirming constraint
compliance, and memory updates confirming what was learned and filed.

The release layer checks for presence and internal consistency of the bundle. A
missing trace ID, an evaluation report without a timestamp, or a policy check
output with no pass/fail status are not minor deficiencies — they are evidence
gaps. Evidence gaps mean the bundle does not prove what it claims to prove. A
release that proceeds over an evidence gap is accepting unverified output. That
is a governance failure at the boundary, not in the loop.

For changes that produce code touching external interfaces, security static
analysis results are a required bundle component. An evidence bundle that is
missing static analysis results for a change in scope is not complete — the
absence is treated as a gap, not as implicit pass.

Bundle integrity must be confirmed as part of the completeness check: the
evidence bundle's cryptographic hash or digital signature must be present and
must match the bundle as presented. A bundle that cannot be verified for
integrity fails this condition.

**Foundation model version consistency.** For loop outputs produced by agents
using externally-provided foundation models, the release gate must confirm that
the foundation model version used during evaluation testing is the same version
deployed to production. Model version pinning — specifying the exact model
version in the deployment configuration, not just the model family name — is
required. A loop output verified against one model version but deployed with a
different version has an evidence bundle that does not represent the system as
deployed.

The model version used must be recorded in the evidence bundle alongside the
dependency manifest. This creates a complete specification-to-production record:
what was built (the specification), what executed it (the agent configuration
including model version), what was verified (evaluation results against that
specific model version), and what was deployed (the deployment configuration
with the same model version). Any discrepancy between the model version in the
evidence bundle and the model version in the deployment configuration is a
bundle completeness failure.

The model provenance assessment — provider security posture, model API
dependency risk — is a specification-level constraint that belongs in
Specification Readiness Condition 4: the release gate verifies that the
constraint was set and honoured; it does not re-perform the provenance
assessment at release time.

**Control state record.** The loop must produce a control state record alongside
the evidence bundle. These are distinct artefacts. The evidence bundle contains
the artefacts that constitute the evidence. The control state record contains
the structured verdict on each control — the machine-readable summary that makes
the gate assessable programmatically.

The control state record must be generated at loop completion, not assembled
post-hoc. It must state, for every required control: the control identifier, the
status (one of: pass, fail, waived, stale, requires-human-decision), the
identifier of the evidence artefact supporting the status determination, and —
where status is waived — the waiver owner, the waiver expiry date, and the
compensating control in effect. A control state record that is missing entries
for required controls is incomplete. A control state record where the stated
status does not match the underlying artefact is contradicted and must not be
accepted.

The Evidence Bundle Agent is responsible for assembling the control state record
from the loop outputs and machine-verifiable checks. The release manager reviews
the record as part of Condition 1. A release candidate without a control state
record is treated as failing Condition 1 — not as having an absent optional
artefact.

The distinction between the two artefacts matters for how the release gate
operates. The evidence bundle answers "what was the evidence?" The control state
record answers "what was the verdict on each control?" A release gate that
receives only an evidence bundle must re-read all artefacts to derive verdicts.
A release gate that receives both can verify verdicts against artefacts and
route only exceptions — conditions in fail, contradicted, or
requires-human-decision status — to human review. This routing is what makes
human review tractable on complex bundles: the control state record concentrates
attention on what requires a decision, not on what has already been
machine-verified.

**Governance-relocation evidence (for systems with relocated governance).** For
systems whose action classes have undergone governance relocation under the
Agentic Enterprise Manifesto (AEnt-M) — where a synchronous control point has
been replaced by a structurally equivalent asynchronous control objective — the
evidence bundle must include machine-readable artefacts proving control
equivalence for each relocated action class. The required artefacts are:

- `relocation_decision_record` — the structured record of the relocation,
  including: `action_class` (the bounded class of agent action covered);
  `control_point_before` (the synchronous control point that was relocated);
  `control_point_after` (the asynchronous control objective and mechanism that
  replaced it); `control_objective_unchanged: true` (an explicit attestation
  that the control objective itself is unchanged — only its placement); the
  named `approval_authority` (the AEnt-M escalation authority that approved
  the relocation); and the `approval_date`.
- `decision_quality_baseline` — the empirical comparison establishing that
  relocated control performance is at least equivalent to the synchronous
  baseline. Must include: `sample_period`, `sample_size`, `baseline_score`
  (decision quality under the synchronous control), `post_relocation_score`
  (decision quality under the relocated control), and `p_value` for the
  equivalence or non-inferiority test applied.
- `error_detection_comparison` — the structured comparison of error detection
  rates between the synchronous and relocated control configurations, by
  error class, with sample sizes and detection latencies.
- `audit_reconstructability_validation` — evidence that, for the relocated
  control, an external auditor can reconstruct from retained artefacts the
  same audit trail that the synchronous control would have produced. Includes
  the validation method, the validator, and the date.
- `degradation_response_test` — a dated test record demonstrating that, when
  the relocated control's monitoring detects degradation against its
  pre-defined thresholds, the system reverts to synchronous control checking
  for the affected action class within the latency bound specified in the
  relocation decision record.

These five artefacts collectively constitute the relocation evidence schema.
The canonical schema definition lives in `agentic-engineering-manifesto/governance/evidence-bundle-schema.md`.
A bundle for a system with relocated governance that is
missing any of the five artefacts is incomplete and fails Condition 1. The
relocation evidence is itself subject to staleness triggers — see the Evidence
Freshness section.

**Projected-stale claim status (for systems depending on intelligence).** For
systems whose actions are informed by claims governed under the Intelligence
Governance Manifesto (IGM), the evidence bundle must include, for each claim
the system depends on at deployment time, the claim identifier, its epistemic
tier, its decay window, its next scheduled revalidation date, and its current
staleness status. A claim whose decay deadline falls within a policy-set 30 calendar days of the planned deployment time must be marked `projected-stale` in the
evidence bundle. A bundle containing one or more `projected-stale` claims
does not automatically fail Condition 1 — but it requires explicit steward
acceptance recorded as part of the gate sign-off, naming each
`projected-stale` claim and confirming that the steward has assessed the
operational risk of deploying with claims approaching decay. If the actual
claim state at deployment time differs from the projected state recorded in
the bundle — for example, a claim projected as fresh has decayed, or a
contradiction has been raised — the steward must be notified within a policy-set 4 hours of the discrepancy being detected and may trigger a rollback under the
standard rollback procedure. A `projected-stale` classification that is
neither resolved (by re-verification before deployment) nor explicitly
accepted (by steward sign-off) is a bundle completeness failure.

**Epistemic tier labelling.** Every artefact in the evidence bundle must carry
an epistemic tier label declaring how it was produced: `human-authored`,
`tool-generated`, `agent-proposed-with-human-review`, or `agent-generated`. The
release gate must verify that the tier composition of the bundle meets the
minimum requirements for the autonomy tier of the system under release.
Specifically: (a) for Tier 3 systems, validation artefacts — evaluation reports,
static analysis findings, independent validation records — may not be entirely
`agent-generated`; at least one human review event must be traceable for each
such artefact, meaning its tier must be `human-authored` or
`agent-proposed-with-human-review`; (b) for Tier 2 systems, the same requirement
applies, and additionally the control state record must be labelled
`human-authored` or `agent-proposed-with-human-review` — an `agent-generated`
control state record is not accepted at Tier 2 without a documented release
manager review event; (c) for Tier 1 systems, no tier composition restriction
applies beyond the labelling requirement itself. A bundle that lacks epistemic
tier labels on one or more artefacts is treated as having an evidence gap for
that artefact — the same as a missing artefact — and the bundle fails
Condition 1.

What goes wrong if bypassed: the deployment is based on assertion rather than
evidence. When something fails in production, there is no reliable record of
what the system was supposed to do, what it was verified against, or what the
accountable human reviewed. Incident investigation becomes archaeology.

### 2. Independent Validation Passed

For systems operating at Phase 4 or above, and for all high-stakes regulated
systems regardless of phase, independent validation (Principle 8 from
[manifesto-principles.md](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto-principles.md)) is a release gate
condition. It is not a post-release review. A team that performs independent
validation after a production deployment has not done independent validation —
it has done a post-deployment audit. The distinction matters because independent
validation that cannot block deployment is not a governance mechanism: it is a
consultation.

Independent validation answers whether the verification and validation performed
by the development team were themselves rigorous. It requires organisational
separation: the team that independently validates must not be the team that
built and verified the system. What "organisationally separate" means depends on
the organisation's structure and the system's risk profile, but the minimum
requirement is that the independent validator has no reporting relationship to
the development lead and no stake in the deployment outcome.

The evidence that independent validation was performed: a named independent
validator, the date of validation, the scope of the review, and a clear
pass/fail finding against the specification artefact as it stood when the
evaluation suite passed.

Independent validation must include at least one governance evaluation run — a
check that the governance system worked correctly for this loop iteration, not
only that the product worked. The governance evaluation verifies: (a) evidence
bundle completeness — all required fields are present and non-empty; (b)
provenance consistency — provenance fields are consistent across artefacts in
the same bundle (for example, the model version in the agentic provenance record
matches the model version in the deployment configuration); (c) control state
record accuracy — the stated pass/fail/waived/stale verdict for each control
matches the underlying artefact; (d) rollback procedure currency — the rollback
test is not stale (no staleness trigger has fired since the test was conducted,
per the trigger definitions in the Evidence Freshness section); (e) SBOM
completeness — the SBOM covers the dependency set that will be deployed, not a
prior state. When governance evaluation fails, it triggers the same remediation
sub-cycle as product evaluation failure — it is not a separate audit finding. A
governance evaluation that has never been run is a governance system that is
trusted rather than verified.

What goes wrong if bypassed: the only external check on whether the development
team's verification was genuine is removed. In regulated environments, this is
typically a compliance violation on its own. In unregulated environments, it is
still a quality failure — the same team that decided what to build, built it,
and tested it, now also decides whether the testing was adequate.

### 3. Rollback Procedure Tested

The rollback procedure must be tested, not merely documented. A documented
rollback procedure that has never been executed is a hypothesis about how to
reverse a deployment, not a tested capability. The difference between a
hypothesis and a tested capability is the thing that matters most when a
production incident is active and every minute of downtime has a cost.

The test must produce evidence: a documented record of the test execution, the
environment in which it was performed, the date, the time taken to complete the
rollback, and the name of the person who conducted the test. Time-to-rollback
must be measured during the test and must fall within the pre-agreed recovery
time window. If the rollback takes longer than the agreed window, the rollback
procedure is not acceptable — not because it failed, but because it failed to
meet the governance standard.

The rollback test may be reused from the pre-release preparation phase if none
of its staleness triggers (defined in the Evidence Freshness section) have fired
since the test was conducted. Because environment state, infrastructure
configuration, and on-call team composition can change rapidly in the period
before a deployment, a rollback test conducted more than 48 hours before the
planned production deployment should be treated as carrying elevated risk of
undetected staleness — not as automatically stale. Teams operating under release
schedules with significant pre-deployment delays should verify absence of
trigger events, not simply count elapsed hours. If any staleness trigger fires
after a rollback test is accepted, the test must be re-executed before
deployment proceeds.

What goes wrong if bypassed: when a production incident occurs and a rollback is
required, the team discovers for the first time whether the procedure actually
works. Discovery time is the worst possible time for this learning. Rollback
procedures that have never been tested fail for reasons that are entirely
preventable: missing permissions, stale scripts, environment configuration
differences, dependency state assumptions, and operator unfamiliarity.

### 4. Accountable Human Sign-Off

The named accountable human — the P12 anchor established at the start of the
loop, as described in [manifesto-principles.md](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto-principles.md) and
in the conditions for entering Specify in [manifesto.md](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto.md) — has
reviewed the evidence bundle and accepted production accountability for the
outcome. This acceptance is recorded in the release artefact as a dated, named
sign-off against a specific evidence bundle ID.

Sign-off is not a bureaucratic stamp placed on a pre-approved outcome. It is a
governance record that a named individual examined what was built, what was
tested, what was verified, and what risks were identified, and made a considered
decision that the evidence is sufficient to proceed to production. The
distinction matters because a rubber-stamped sign-off produces the legal form of
accountability without the substance. The result is that when something fails,
there is a name in the record, but no actual human who understood the risk.

Accountability at the release boundary is not separate from the P12
accountability assigned at the start of the loop. It is the same person, at the
end of the evidence chain, confirming that the evidence chain is complete and
that they accept the outcome. If the evidence bundle is so large or so complex
that the accountable human cannot meaningfully review it, the right response is
to ask why the evidence is not being surfaced at a reviewable level of
abstraction — not to reduce the review.

A sign-off that cannot be verified as a meaningful review is a rubber stamp. Two
patterns indicate rubber-stamping and should be treated as accountability
failures, not process irregularities: (1) review time anomaly — the accountable
human's sign-off timestamp is so close to the presentation of the evidence
bundle that a substantive review of the primary artefacts is implausible given
the bundle's size and complexity; (2) trace absence — no evidence exists that
the accountable human accessed the primary artefacts (evaluation reports,
control state record, static analysis results) rather than an agent-generated
summary. The empirical risk this control addresses is documented in Perry et
al., *Do Users Write More Insecure Code with AI Assistants?* (ACM CCS 2023,
https://arxiv.org/abs/2211.03622): users with AI assistance produced less
secure code while reporting higher confidence in its security. The release
gate must close that confidence-versus-evidence gap by requiring evidence —
not summaries — to be the basis of the sign-off. The release manager is responsible for tracking review-time patterns
across releases over time — a single fast review is not actionable; a pattern of
fast reviews on complex bundles is. Reference: `agentic-engineering-manifesto/adoption/metrics.md` documents the
rubber-stamping detection methodology using review-time distribution metrics.
When a rubber-stamping pattern is detected, the correct response is to raise the
evidence presentation requirements (requiring the accountable human to attest to
specific artefacts reviewed) or to reduce the autonomy tier of the system until
oversight signal quality is restored.

**Substantive-review standard for the P12 anchor.** The accountability
diffusion failure mode this condition prevents is not a missing signature;
it is a present signature that does not reflect a substantive review. The
substantive-review standard makes the review's content auditable, not only
its existence. To satisfy Condition 4, the P12 anchor's review must
include all three of the following:

- *Spot-check of evaluation results.* The P12 anchor must access at least
  one primary evaluation report — not a summary — for the release and
  must attest to the specific evaluation result they examined (the
  evaluation case identifier, the recorded outcome, and any noted
  deviation). The attestation is recorded as a structured field on the
  sign-off, not a free-text confirmation.
- *Spot-check of evidence bundle components.* The P12 anchor must access
  at least one non-evaluation primary artefact in the evidence bundle —
  the static analysis report, the SBOM, the SLSA provenance attestation,
  or the rollback test record — and attest to its contents in the same
  structured form.
- *Attestation that the control state record is accurate.* The P12 anchor
  must attest that, for every control marked `pass` in the control state
  record they reviewed, the underlying artefact supports the verdict.
  This attestation is required at minimum for the controls the anchor
  spot-checked; for the remaining controls, the attestation is that the
  anchor reviewed the control state record as a whole and saw no
  inconsistencies.

A sign-off that does not include the three structured attestations does
not satisfy Condition 4 — regardless of the time elapsed in review.

**Sampling plan for high-volume Tier 3 systems.** For Tier 3 systems with release volume exceeding a policy-set 20 deployments per quarter, applying the full
substantive-review standard to every release is operationally infeasible
and itself a rubber-stamping risk: the P12 anchor cannot meaningfully
attest to spot-checks at that volume. A documented sampling plan is
required for such systems, with a policy-set minimum sampling rate of 20% of releases per quarter (rounded up). Sampling must be stratified across
release classes — feature releases, security patches, dependency
updates, and emergency changes are each represented in proportion to
their occurrence — and the sampled releases are subject to the full
substantive-review standard, with the structured attestations recorded
on the sign-off. Releases not in the sampled set still require the P12
anchor's sign-off, but the attestation requirements are reduced to the
control state record review and a confirmation that the bundle's
machine-verifiable checks passed. The sampling plan, including the
sampling rate and the stratification rule, is a versioned artefact
filed with the system's governance specification.

**Rubber-stamp detection and escalation.** Two empirical patterns trigger
escalation under the substantive-review standard, in addition to those
named above:

- *Sub-30-minute reviews on complex bundles.* A P12 anchor whose median review time per release falls below a policy-set 30 minutes for releases with
  bundle size above a defined complexity threshold (computed from
  artefact count and control state record entry count) is producing
  signatures whose substantive content is implausible. The release
  manager escalates to the governance portfolio steward.
- *Zero-findings histories.* A P12 anchor whose sign-off history across a policy-set 20 or more releases contains no documented findings, no requested
  remediations, and no escalations is producing reviews that have
  detected nothing — which, against the empirical base rate of release
  defects, is itself a finding. Zero findings ever is not a quality
  signal; it is a detection-failure signal. The release manager
  escalates.

Escalation triggers a review of the anchor's review-time distribution
and bundle complexity history, and either an evidence-presentation
remediation (raising the structural requirements on what artefacts the
anchor must attest to) or a reduction in the autonomy tier of the
system until the anchor's review signal quality is restored.

What goes wrong if bypassed: production deployments proceed without any named
human who owns the outcome. Incident response lacks a clear accountability
anchor. Regulatory enquiries cannot be answered. And the governance pattern that
prevents rubber-stamping (described in Principle 12 of
[manifesto-principles.md](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto-principles.md)) degrades into precisely
the pattern it was designed to prevent.

### 5. Compliance Documentation Complete

All regulatory documentation required for the change is complete and filed
before the release is authorised. For organisations in regulated industries,
this includes change records, model risk documentation, installation
qualification records, and any jurisdiction-specific filings required by the
applicable regulatory framework.

"Complete" means filed, not drafted. A compliance document that exists in draft
state is not filed. A compliance document that is awaiting a second reviewer's
signature is not filed. The release gate does not open on the assumption that
filing will happen shortly after deployment.

This condition applies with particular force to changes that touch model
behaviour, inference pipelines, risk calculations, clinical decision support, or
any other capability subject to model risk governance. In those contexts, the
compliance documentation is often a condition of the authorisation to deploy,
not merely a record of having deployed.

What goes wrong if bypassed: the deployment is non-compliant from the moment it
reaches production. In regulated industries, deploying a material change without
the required compliance documentation is not a governance gap to be closed after
the fact — it is a violation. The after-the-fact normalisation effort is both
more expensive and less defensible than completing the documentation before
deployment.

### 6. Dynamic Security Testing Passed (for external-facing changes)

For loop outputs that expose or modify HTTP endpoints, process external inputs,
execute database queries on behalf of external callers, or interact with
third-party APIs, the deployed system in a representative environment must be
tested dynamically against known security attack patterns before the release
gate is assessed.

Dynamic security testing exercises the running system, not the source code. Its
purpose is to detect vulnerabilities that static analysis cannot find: injection
flaws under real request conditions, authentication and session management
weaknesses, access control failures across endpoints, and security
misconfiguration in the deployed configuration. These are the classes of
vulnerability most likely to be present in agent-generated code that was built
to pass functional evaluations without an adversarial lens.

The test must be executed against the system as deployed in the staging
environment. The test results must be included in the evidence bundle. No
unresolved High severity dynamic security findings may be present in the bundle
at the time of gate assessment. Critical severity findings block the release
without exception.

This condition applies to Tier 2 and Tier 3 systems. At Tier 1, a dynamic
security test is recommended but not required as a gate condition unless the
system processes user-supplied inputs in a way that could affect other users,
systems, or stored data.

What goes wrong if bypassed: static analysis provides no signal about how the
deployed system behaves under adversarial request patterns. Agent-generated code
that correctly implements the specification can still expose injection paths,
broken authentication, or insecure direct object references that only manifest
when the running system receives crafted inputs. Dynamic testing is the check
that static analysis cannot substitute.

### 7. Control State Record Complete and Current

The control state record — defined in Condition 1 as a distinct artefact from
the evidence bundle — must be complete and current at gate time as an
independently assessed condition. This condition makes the control state record
a first-class gate object, not a component buried within the evidence bundle
assessment.

At gate time, every required control must have exactly one of the following
statuses: `pass`, `waived-with-current-waiver`, or `deferred-to-gate`. No
control may carry a `stale` status or a `requires-human-decision` status at the
moment the gate is assessed. A control in `stale` status means its underlying
evidence has lapsed and the verdict is no longer reliable — the evidence must be
refreshed before the gate can proceed. A control in `requires-human-decision`
status means a human judgment is outstanding — that judgment must be made and
the status resolved before the gate can proceed. A control in `fail` status
means the gate does not pass.

The statuses `stale` and `requires-human-decision` are not permissible open
states at gate time. They are pre-gate states that must be resolved before gate
assessment begins. Their presence in the control state record at the moment of
gate assessment is itself a condition failure: it indicates that the loop was
submitted to the release gate with unresolved governance work.

The `deferred-to-gate` status is permitted only for controls whose resolution
genuinely requires the gate itself — for example, a final review that happens at
the gate as part of Condition 4 (Accountable Human Sign-Off). The list of
controls eligible for `deferred-to-gate` status must be defined in the system's
governance specification and must be approved as part of the system's initial
release gate configuration.

What goes wrong if bypassed: a control state record allowed to carry stale or
unresolved statuses into the gate converts the gate from a verification
mechanism into a rubber-stamp. The gate passes on the basis of a record that
does not reflect the current state of the system.

### 8. Waiver Governance

All waivers referenced in the control state record must satisfy three
requirements at the moment of gate assessment: they must be current (not
expired), they must carry the name of the human who granted the waiver, and they
must carry an explicit expiry date. A waiver that does not name its grantor is
not a waiver — it is an anonymous bypass, which has no accountability. A waiver
without an expiry date is a permanent exemption granted without deliberate
intent, which is a governance design error.

A gate pass recorded when one or more waivers in the control state record are
expired is not a valid gate pass. The gate must reject the release until each
expired waiver is either renewed by a named accountable human or the underlying
control is satisfied. "The waiver just expired" is not a reason to proceed; it
is a reason to pause and make a fresh governance decision. The grantor of the
renewed waiver must be named and must not be the same individual as the release
manager authorising the deployment — this separation prevents a single person
from both waiving a control and authorising the release over the waiver.

Waiver records must be retained as part of the release artefact for the same
retention period as the evidence bundle. A post-deployment compliance audit must
be able to reconstruct, from retained artefacts, every waiver that was in effect
at the time of each historical release gate pass.

What goes wrong if bypassed: expired waivers silently persist in the control
state record across multiple releases. What was once a deliberate, time-bounded
governance decision becomes an indefinite exemption that no current human has
reviewed or owns. Audit investigations cannot determine whether the waiver was
intentional at the time of the release.

---

## Agent Participation in Release Gate

A governance agent — one governed under the ASDLC with its own specification and
a current evaluation suite — may contribute to two aspects of the release gate:
evidence bundle assembly and machine-verifiable condition checking. In both
cases the agent's role is operational, not decisional. The gate conditions are
assessed by humans; the agent performs defined, auditable work that supports
that assessment.

The evidence bundle may be assembled by a governance agent provided that the
assembled bundle is reviewed by the release manager before the gate assessment
begins, and that each artefact in the bundle carries an epistemic tier label:
human-authored, tool-generated, agent-proposed with human review, or
agent-generated. Any artefact labeled agent-generated without a corresponding
human review is flagged for mandatory release manager spot-check before the
bundle is accepted as complete. The release manager's review and sign-off on the
assembled bundle is the human accountability event. The agent's assembly of the
bundle is a mechanical task that reduces manual effort; it does not constitute
the review. A bundle assembled by an agent and signed off by the release manager
is a release manager-reviewed bundle. A bundle assembled by an agent without
release manager review is not an accepted bundle, regardless of the agent's
assembly quality.

Governance agents operating in monitored execution mode may perform a defined
set of machine-verifiable checks and file the results in the evidence bundle as
monitored-execution outputs. These checks are: SLSA provenance attestation
verification, confirming that the signed attestation chain is valid and
correctly links the deployed artefact to its declared source repository and
build configuration; model version consistency checking, verifying that the
model version recorded in the evidence bundle matches the model version in the
deployment configuration; SBOM completeness and freshness validation, confirming
that the software bill of materials was generated against the current dependency
tree and not a stale snapshot; and certificate and dependency expiry checking
across the deployment's runtime dependencies. These checks produce outputs
equivalent in character to those produced by a governed build tool or a CI/CD
pipeline stage. Their results may be filed in the evidence bundle without
individual human review of each check result, provided that the governance agent
that performed them has a current evaluation suite demonstrating their
correctness. The evaluation suite is what makes the output trustworthy without
per-result review — the trust is placed in the evaluated agent, not in any
individual check result.

Agents may not assess any release gate condition as passed. Agents may not sign
off on releases. Agents may not override the accountable human sign-off
requirement under any circumstances, including in the emergency change
procedure. An agent that completes all machine-verifiable checks successfully
and assembles a complete evidence bundle has done useful operational work. It
has not satisfied Condition 4 — Accountable Human Sign-Off — and it cannot. That
condition exists precisely because human accountability cannot be automated: the
named accountable human who reviews the bundle and accepts production risk is
doing something that has no agent equivalent. The accountability is personal,
named, and non-delegable. The governance architecture of the release gate treats
agent participation as a capability that reduces the mechanical burden on human
reviewers, not as a capability that reduces the human accountability
requirements.

---

## Governance Failure Modes at the Release Gate

Three failure modes recur at release gates in agentic systems. They are not
hypothetical; they are the predictable results of governance structures that are
formally present but operationally hollow. Each has a name because naming it is
the first step toward detecting and preventing it.

**Approval laundering.** The accountable human reviews an agent-generated
summary of the evidence bundle rather than the primary artefacts themselves. The
summary may be accurate; it may also be incomplete, selectively framed, or
incorrect in ways that the agent did not detect. The release gate must present
primary artefacts — evaluation reports, static analysis outputs, the control
state record, the agentic provenance record — as the default review interface.
Agent-generated summaries are permitted as navigation aids but may not
substitute for primary artefact access. A Condition 4 sign-off that cannot be
traced to the reviewer having accessed the primary artefacts is a suspected
laundering event.

**Compliance theater.** Controls are added to the evidence bundle to satisfy a
checklist rather than to detect failures. Detectable by back-testing: would this
control have caught a known past failure in this system or a comparable system?
If not, the control is generating evidence without governance value. The
independent validator is responsible for flagging controls whose configuration
would not have caught plausible failures, not only controls that are absent.

**Stale-control reliance.** A control is recorded as passing in the control
state record because it has not been re-run since the system last changed, not
because the system still satisfies it. This is the `stale` GateState applied to
the release gate context. The Evidence Bundle Agent must flag any control whose
last execution predates the most recent material change to the system component
it governs.

---

## Live Gate State and Evidence Freshness

Each of the eight release gate conditions has a current GateState drawn from the
governance graph. The seven possible values are defined authoritatively in
[governance/graph.md](governance/graph.md); brief definitions follow for
reference. **pass** — the condition is satisfied by current, non-stale evidence.
**fail** — the condition is actively not met; a specific required element is
absent or incorrect. **missing** — no evidence or artefact for this condition
has been submitted yet. **stale** — evidence was previously accepted but has
exceeded its defined freshness window or a triggering event has occurred since
it was filed. **contradicted** — two pieces of evidence for this condition
conflict with each other. **waived** — the condition has been formally waived
with accountable human approval, a documented compensating control, and a
recorded expiry date. **requires-human-decision** — the condition cannot be
assessed by an agent and requires human judgment. As with the Specification
Readiness Gate, `missing` and `stale` are distinct from `fail`: they describe
different situations and require different responses. A condition that is
`missing` has never been attempted; one that is `stale` was satisfied but has
lapsed; one that is `fail` was assessed and found actively deficient. See
[governance/graph.md](governance/graph.md) for the authoritative GateState
definitions and transition rules.

Evidence freshness at the release gate is governed by triggering events, not by
calendar schedules. An artefact becomes stale when a defined triggering event
occurs — not because a fixed number of days has elapsed. Calendar-based expiry
is explicitly rejected: a 30-day-old artefact against an unchanged system is
current; a 30-minute-old artefact against a system that has had a dependency
update is stale. The governing question is always "has anything changed that
could invalidate this evidence?" not "how old is this evidence?"

The following table defines the triggering events that render each artefact
class stale. The Evidence Bundle Agent monitors for these events continuously
and transitions the relevant artefact's GateState to `stale` when a trigger
fires.

| Artefact                                       | Staleness triggers                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evidence bundle (Condition 1)                  | Any constituent artefact becomes stale                                                                                                                                                                                                                                                                                                                           |
| SBOM (Condition 1)                             | Any dependency change (direct or transitive); new build execution; infrastructure change affecting the dependency resolution environment                                                                                                                                                                                                                         |
| Security static analysis results (Condition 1) | Any commit to the release candidate; any change to the static analysis rule set; a new vulnerability published against a dependency in scope                                                                                                                                                                                                                     |
| SLSA provenance attestation (Condition 1)      | A new build execution; any change to the source repository or build configuration between attestation and deployment                                                                                                                                                                                                                                             |
| Independent validation (Condition 2)           | Specification amendment; model version change; evaluation suite change; acceptance criteria change; regulatory change affecting the validation scope; threat model update that changes the risk classification of the system                                                                                                                                     |
| Rollback procedure and test (Condition 3)      | A deployment to the target environment after the test was conducted; an infrastructure change affecting the rollback execution environment; an environment configuration change; a change to the rollback scripts or procedure; the on-call team composition changing such that the person who conducted the test is no longer on-call for the deployment window |
| Compliance documentation (Condition 5)         | Specification amendment; regulatory change; change to the compliance framework applicable to the system; any material scope change to the release                                                                                                                                                                                                                |
| Dynamic security testing (Condition 6)         | Any commit to the release candidate that modifies an externally-facing surface; a change to the representative test environment configuration; a new threat pattern published by the applicable security authority that is in scope for the tested surface                                                                                                       |
| Model version consistency check (Condition 1)  | Any change to the model version pinned in the evaluation environment or the deployment configuration                                                                                                                                                                                                                                                             |
| Waiver records (Condition 8)                   | Waiver expiry date reached; change to the control the waiver covers; change to the compensating control specified in the waiver                                                                                                                                                                                                                                  |

**Evidence bundle (Condition 1).** The evidence bundle is fresh if all its
constituent artefacts are free of triggered staleness events. The bundle's
freshness is the minimum of its parts: a bundle in which any required
constituent artefact has become stale is itself stale. The Evidence Bundle Agent
monitors constituent artefact staleness continuously and surfaces staleness
events to the release manager without requiring a manual check.

**SBOM (Condition 1).** The software bill of materials must be regenerated at
every new build or dependency change. An SBOM from a previous build is stale for
the current build regardless of how little time has elapsed, because the
deployment configuration — including transitive dependencies — may differ. The
staleness trigger is the event (dependency change, new build), not elapsed time.

**Security static analysis results (Condition 1).** Static analysis results must
be produced against the exact commit being released. Results from a prior commit
are stale for the current release, even if the intervening commits touched only
non-code artefacts. The analysis is commit-scoped and event-scoped: a new
vulnerability disclosure against an in-scope dependency also triggers staleness
even without a new commit.

**SLSA provenance attestation (Condition 1).** The provenance attestation is
generated per build and is specific to the build artefact it describes. The
attestation for a prior build is not valid for a subsequent build, even if no
source changes occurred between the two builds. Attestation freshness is
build-scoped: each deployment requires attestation against the artefact being
deployed.

**Independent validation (Condition 2).** The validation result remains current
for the release if none of its staleness triggers have fired since the
validation was conducted. The triggers are: specification amendment, model
version change, evaluation suite change, acceptance criteria change, regulatory
change affecting the validation scope, and threat model update that changes the
system's risk classification. Any one of these events renders the validation
stale and requires re-validation before the release gate can assess Condition 2
as satisfied. Time elapsed since validation is not a staleness trigger; only the
defined events are.

**Rollback test (Condition 3).** The rollback test is stale when any of its
defined triggers fire — specifically: a deployment to the target environment
after the test was conducted, an infrastructure change affecting the rollback
execution environment, a change to the rollback scripts or procedure, or the
departure of the on-call engineer who conducted the test from the on-call roster
for the planned deployment window. In practice, because environment state can
change rapidly in the period immediately before a planned deployment, the
rollback test is typically re-executed within 48 hours of the planned production
deployment window; this is a practical guideline for detecting unobserved
trigger events, not a calendar rule. The 48-hour boundary is a maximum recency
heuristic, not a freshness definition — a rollback test conducted 47 hours
before deployment against a system state that has since changed is stale
regardless of the elapsed time. If a deployment is delayed after a rollback test
and any trigger event occurs in the interval, the rollback test must be
re-executed before deployment proceeds.

**Dynamic security testing (Condition 6).** Dynamic security testing must be
conducted against the release candidate in a representative environment. Results
from a prior release candidate are stale for the current candidate if any
surface-modifying commit has occurred, the test environment configuration has
changed, or a new threat pattern in scope for the tested surface has been
published. Results may be reused across minor release delays if a diff analysis,
produced and reviewed by the security function, confirms that none of the
staleness triggers have fired. The diff analysis is itself a dated artefact
subject to staleness review.

**Model version consistency check.** The model version consistency check —
confirming that the model version in the evidence bundle matches the model
version in the deployment configuration — is stale if either the evaluation
environment model version or the production deployment model version changes
after the check was performed. A consistency check conducted against a model
version that is subsequently pinned to a different patch version is stale and
must be re-performed.

**Gate readiness score as a FinOps signal.** The gate readiness score, tracked
over time, is a FinOps signal. A release gate where multiple conditions required
last-minute evidence regeneration — predictive blocking events in the final 48 hours — represents avoidable inference cost. The governance agent's predictive
clearing function, when it works, reduces the cost of gate passage by
distributing evidence generation work across the loop rather than concentrating
it at gate time. The cost difference between predicted gate failure (evidence
generated once, correctly timed) and actual gate failure (evidence generated
multiple times under time pressure) is a measurable governance economics signal.
Teams whose gate cost patterns show a spike in evidence regeneration in the
final 48-hour window before a gate are not operating predictive clearing
effectively — regardless of whether the gate ultimately passes.

A release gate assessment conducted on stale evidence is not a valid gate
assessment. If a staleness trigger fires between a gate assessment pass and the
actual deployment — for example, if a dependency update causes the SBOM to
become stale, or if an infrastructure change fires a rollback test staleness
trigger during a delayed deployment — the affected condition reverts to `stale`
and must be re-satisfied before deployment proceeds. A gate pass does not confer
an event-free licence to deploy: it records that the conditions were satisfied
and that no staleness triggers had fired at the moment of assessment. The
current GateState of each condition records whether they remain satisfied now.

---

## Release Approval Chain

Who approves a release, and at what level of formality, depends on the autonomy
tier of the agents involved in producing the change. The autonomy tiers from
Principle 5 of [manifesto-principles.md](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto-principles.md) map
directly to release approval requirements. Merge approval and production release
approval are not the same thing and must not be treated as the same thing.
Approving a merge to the main branch approves the code change. It does not
authorise a production deployment.

**Tier 1 — Agents propose, humans execute.** Agents have analysed, recommended,
or drafted. All execution was performed by humans. No separate production
release approval is required beyond the standard merge review and change
management process that would apply to a human-authored change of equivalent
scope. The engineering output is not distinguishable at the release boundary
from a human-authored change.

**Tier 2 — Agents execute bounded tasks.** Agents have written to isolated
branches; humans have approved merges. Two separate approvals are required: the
tech lead approves the merge, confirming that the engineering output is
technically sound. The release manager authorises the production deployment as
an explicit, separate step. The release manager reviews the evidence bundle,
confirms the release gate conditions are met, and authorises the deployment to
the target environment and deployment window. Merge approval does not carry over
as production release approval. This separation exists because the engineering
quality check (merge approval) and the deployment timing and risk decision
(production release approval) are different judgements made by people with
different responsibilities and different information.

**Tier 3 — Agents execute with broad boundaries.** Both merge approval and
production release approval are required as described for Tier 2, plus the named
accountable human's explicit written acceptance of production risk is attached
to the release artefact. The acceptance must reference the specific evidence
bundle ID and the specific deployment target. Generic sign-offs not tied to a
specific evidence bundle are not acceptable. The full evidence bundle must be
attached to or referenced by the release artefact, and the release manager must
confirm they have reviewed the bundle summary before authorising.

**Tier 4 — Policy-envelope autonomous operation.** In Tier 4, individual agent
actions within a human-approved, machine-enforced policy envelope do not each
require a release gate pass. The release gate operates at a different level of
abstraction: the policy envelope approval IS the release gate for Tier 4.

The policy envelope approval must satisfy all eight release gate conditions in
this document — evidence bundle complete (Condition 1), independent validation
passed (Condition 2), rollback procedure tested (Condition 3), accountable human
sign-off (Condition 4), compliance documentation complete (Condition 5), dynamic
security testing passed where applicable (Condition 6), control state record
complete and current (Condition 7), and waiver governance satisfied (Condition
8). The policy envelope approval record is the release artefact for Tier 4. It
must reference the envelope specification (the precise description of which
change classes, blast radius ceilings, and environmental constraints the
envelope permits), the evidence bundle ID, and the named accountable human who
accepted the envelope.

The kill-switch configuration must be verified as functional as part of the
envelope approval. The verification must produce a dated test record showing
that the kill-switch, when triggered, halts agent execution within the latency
bounds specified in the envelope. A policy envelope approval without a current
kill-switch verification record is not a valid Tier 4 release.

Individual agent actions executed within an approved envelope are governed
continuously, not gated per-action. A governance audit trail of all agent
actions within the envelope — action type, timestamp, affected resource,
outcome, and the envelope version under which the action was authorised — must
be maintained in real time and retained for the same period as the release
artefact. The audit trail is not optional; its absence converts Tier 4 from
governed autonomous operation into ungoverned automation.

Any change to the policy envelope that expands its scope — adding a new change
class, increasing a blast radius ceiling, relaxing an environmental constraint,
or extending the envelope's permitted duration — constitutes a new release gate
event. The updated envelope must pass all eight release gate conditions before
the expanded scope takes effect. Narrowing the envelope (reducing permitted
scope) does not require a new gate pass but must be recorded as a change event
in the audit trail.

**For regulated systems:** a compliance officer's approval is an additional gate
where required by the applicable regulatory framework. Compliance officer
approval does not substitute for tech lead or release manager approval — it is
an additional layer for changes that carry regulatory significance. The
compliance officer's approval confirms that the compliance documentation is
complete, filed, and consistent with the change scope. It does not repeat the
engineering quality assessment.

At Phase 3 and below, the organisation's governance infrastructure is not yet
mature enough to support Tier 2 or Tier 3 agent autonomy on production-impacting
changes. The autonomy constraints from the phase table in Principle 5 of
[manifesto-principles.md](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto-principles.md) apply at the release
boundary as well as in the loop.

---

## Software Supply Chain Provenance

For Tier 2 and Tier 3 systems, SLSA (Supply-chain Levels for Software Artifacts)
provenance attestation is required as part of the evidence bundle. SLSA is a
vendor-neutral framework for verifying that software artefacts were produced
from known source material by a known, controlled build process. At SLSA Level 2
— the minimum required at these tiers — the build process must be a hosted,
auditable service (not a developer's local machine), and the build process must
produce a provenance record that identifies the source repository, the build
configuration, and the artefact that was produced.

The SLSA provenance attestation serves a specific function at the release
boundary: it provides independent confirmation that the artefact being deployed
is the artefact that the evidence bundle describes. Without provenance
attestation, the release gate must trust that the artefact presented for
deployment is the one that evaluation and verification ran against. With
attestation, that claim is machine-verifiable.

SLSA provenance attestation is generated by the CI/CD build process as a build
artefact. It is not a document produced by a person — it is a
cryptographically-signed record generated by the build system. Its presence as a
required release condition incentivises teams to operate their build processes
in governed, auditable environments rather than in local or ad-hoc
configurations. Reference: SLSA v1.2 — https://slsa.dev/spec/ (confirmed
current at slsa.dev, 05.09.2026; see also devsecops-controls.md's Normative
References).

---

## Change Management Alignment

Release governance does not replace change management. It feeds it. Most
organisations operating in regulated or enterprise environments have existing
change management processes — often ITIL-derived — that govern how changes to
production systems are authorised, scheduled, and documented. The release
governance process in this document defines what information the engineering
execution loop produces for that change management process, and what the change
management process returns.

The interface is explicit. The release layer feeds the change management system
with the following information, drawn from the evidence bundle and the release
gate assessment:

- **Specification reference:** the versioned specification artefact against
  which the change was verified and validated. This is the document the change
  implements. It is the reference against which future changes to this component
  will be assessed.
- **Evidence bundle ID:** the unique identifier for the complete evidence
  bundle. The change record references the bundle; it does not reproduce it. The
  bundle is the evidence. The change record is the authorisation record.
- **Rollback plan reference:** the unique identifier for the tested rollback
  procedure. Not the procedure itself — the reference to where it is stored and
  the test result that validates it.
- **Accountable human:** the named person who reviewed the evidence bundle and
  accepted production accountability. This is the P12 anchor. The change record
  records who is accountable; it does not transfer accountability to the change
  management system.
- **Compliance filing reference:** where applicable, the reference to the filed
  compliance documentation for regulated changes.

The change management process returns:

- **Change record ID:** the unique identifier for the authorised change. This ID
  is included in the deployment evidence (see
  [deployment-governance.md](deployment-governance.md)) and in the post-release
  compliance record.
- **Approval status:** approved, rejected, or deferred, with the reason.
- **Approved deployment window:** the time range within which the deployment is
  authorised. A deployment executed outside the approved window is not covered
  by the change record's authorisation and must be treated as an emergency
  change.

The change management process does not re-perform engineering quality
assessment. It does not re-run evaluations. It uses the evidence bundle as
evidence that the engineering quality assessment was done, verifies that the
release gate conditions were met, and applies its own governance over the
deployment timing, risk window, and change classification. The two processes
have different purposes and different owners. They share information through the
interface described here.

Duplicate documentation is waste. If a piece of information is captured in the
evidence bundle, the change record references it — it does not reproduce it. The
evidence bundle is the source of truth for engineering governance. The change
record is the source of truth for deployment authorisation.

---

## Release Definition of Done

A release is done when all of the following conditions are true. These are not
sequential steps — several run in parallel — but all must be true before the
release is considered complete.

**Deployed to target environment within the approved deployment window.** The
deployment occurred within the time range authorised by the change record. A
deployment that occurred outside the window must be documented as a deviation
and may require retrospective change management treatment depending on the
organisation's policy.

**Smoke tests passed in production.** Not in staging. Not in integration.
Production smoke tests confirm that the deployment is operational in the actual
target environment, against the actual production configuration, with access to
actual dependencies. A deployment that passes every test in staging and fails
smoke tests in production has a staging parity problem (see
[deployment-governance.md](deployment-governance.md)). Both problems — the
deployment issue and the staging parity gap — must be addressed.

**Rollback tested.** The tested rollback procedure from the release gate may
satisfy this condition if none of the rollback test staleness triggers (defined
in the Evidence Freshness section) fired between the test and the production
deployment. If a staleness trigger fired in that interval — for example, an
infrastructure change or an on-call roster change — the rollback must be tested
again in a representative environment after deployment, and the new test result
recorded in the release artefact. The test result must include the time to
complete the rollback.

**Monitoring and alerting configured.** Any new observable behaviour introduced
by the change has corresponding monitoring coverage and alerting thresholds. A
deployment that introduces new functionality without corresponding monitoring is
not done — the new behaviour cannot be governed from operations without
instrumentation. Alert thresholds must be calibrated before the deployment
completes, not left for the operations team to configure after the fact.

**Compliance record filed.** For regulated changes, the compliance documentation
filed before release has been updated to reflect the actual deployment:
deployment timestamp, deployment ID, environment, and any deviations from the
approved change record. The compliance filing is closed.

**Accountable on-call engineer notified.** The engineer responsible for on-call
coverage for the deployed system has been notified of the change, its scope, and
its blast radius. They have access to the evidence bundle reference, the
rollback procedure, and the escalation path to the accountable human. A
deployment whose on-call engineer does not know what changed and how to reverse
it if necessary is not operationally ready.

**Operational readiness gate assessment initiated.** The transition from release
to operations (Layer 4 — see
[operations/governance.md](operations/governance.md)) has been formally
initiated. This does not mean the Layer 4 assessment is complete — it means it
has started. The release is not held open pending the operations readiness
assessment, but the handoff must be formally initiated before the release is
marked done.

**Phase calibration.** At Phase 3, the release Definition of Done requires:
tests and diff (as evidence), smoke tests in production, and a change record.
The compliance record and independent validation conditions apply only where
explicitly required by the change's risk profile. At Phase 5, all conditions
above apply. Between phases 3 and 5, the release DoD scales with the maturity of
the engineering and governance infrastructure. The governing question at every
phase is the same: can you show evidence, not just assertions?

---

## Emergency Change Procedure

Certain production situations require a fix faster than the normal release
process can accommodate. A critical security vulnerability being exploited in
production, a service outage causing financial or safety harm, and a data
integrity failure with live impact are examples where the cost of delay exceeds
the cost of a reduced governance process. An emergency change procedure exists
to address these situations. It is not a bypass mechanism for inconvenient
governance. It is a structured, bounded exception with its own governance
requirements.

**Who can authorise an emergency change.** A named role — not a team, not a
group, not "on-call management" — must be empowered to authorise emergency
changes. Typically this is the on-call incident commander, the release manager,
or an explicitly designated senior engineer. The organisation must name these
roles before an emergency occurs. Discovering that no one is empowered to
authorise an emergency change during an active incident is a governance design
failure.

**What can be deferred.** Two categories of conditions can be deferred under an
emergency change: the change management pre-approval process (the change record
is created post-deployment) and the independent validation step (performed within a policy-set 24 hours of deployment where the system's risk profile requires it).
These deferrals are time-bounded. They are not permanent exemptions. Both must
be completed within the post-deployment normalisation window.

**What cannot be deferred.** Nothing relating to safety or compliance can be
deferred. Safety-critical evidence conditions cannot be deferred regardless of
the urgency of the emergency. A change that introduces an unverified safety risk
in order to remediate an operational risk has traded one problem for another,
and the new problem may be worse. Compliance filing deferrals require explicit
regulatory framework analysis — some frameworks do not permit them. If the
organisation is uncertain whether a compliance filing can be deferred, the
answer is that it cannot until that analysis is complete.

**What must still be met.** An emergency change does not eliminate the
requirement for an evidence bundle. The evidence bundle must be produced. Under
an emergency change procedure, the evidence bundle may be produced in parallel
with or immediately after the deployment rather than before it — but it must be produced and filed within a policy-set 24 hours. An evidence bundle that is never produced
converts an emergency change into an ungoverned change, which is a governance
hole, not a procedure.

The named accountable human must be identified before the emergency deployment
executes. There is no emergency procedure that permits a deployment without a
named human accepting production accountability. If no named accountable human
can be reached, the emergency procedure is not available.

**Post-hoc normalisation.** Within a policy-set 24 hours of the emergency deployment:

- The full evidence bundle is filed against the emergency change record.
- The change record is updated with actual deployment time, deployment ID, and
  configuration state.
- Any deviation from the normal release process is documented with explicit
  justification. "It was an emergency" is not a justification — the specific
  circumstances that made normal governance infeasible are the justification.
- The rollback procedure is tested (it may have been used during the incident;
  if so, the incident execution constitutes the test, and the result is
  recorded).
- The incident is classified: was this a process failure (something in normal
  governance prevented a timely response to a legitimate emergency), a
  capability failure (the system failed in a way that should have been caught
  earlier), or an external event (a threat or failure that was genuinely
  unforeseeable)?

**An emergency change procedure that allows bypassing evidence requirements is a
governance hole, not a procedure.** The difference between a governed emergency
procedure and an ungoverned bypass is the presence of post-hoc normalisation
with a hard deadline, a named accountable human, and documentation of the
specific conditions that triggered the emergency. Without those three things,
the emergency procedure is a standing invitation to skip governance under
pressure — and production environments under pressure are the environments where
governance matters most.

---

## Regulatory Release Requirements

Release governance requirements in regulated industries are not a superset of
general release governance layered on top of good practice. They are legally
binding requirements that impose specific conditions on what constitutes an
acceptable release. The following summaries identify the release-specific
requirements for primary regulated industries. They are cross-references, not
interpretations: each requires qualified regulatory counsel for the specific
jurisdiction and use case. Domain files provide the detailed mapping — see the
applicable domain file in the `domains/` directory for the full treatment.

**Financial services.** Two frameworks impose the most direct release governance
requirements.

DORA Article 9(4)(e) (Digital Operational Resilience Act) requires documented
ICT change management policies, procedures and controls ensuring that all
changes to ICT systems are "recorded, tested, assessed, approved, implemented
and verified in a controlled manner", which carries pre-implementation testing
of changes. This document additionally requires a documented rollback
procedure and post-implementation review — neither of which it sources to
DORA, because the words `rollback` and `post-implementation` each occur zero
times in the Regulation; both are ASDLC controls and must not be presented to a
supervisor as DORA requirements. Independent testing of changes before
production deployment for critical or important functions is likewise not
sourced here to any DORA provision and must not be relied on as one; what the
Regulation states is Article 24(4), that a financial entity shall ensure that
tests "are undertaken by independent parties, whether internal or external",
and Article 24(6), that appropriate tests are conducted at least yearly on all
ICT systems and applications supporting critical or important functions — a
programme-level, periodic testing duty rather than a per-change release
condition. The release gate conditions in this document are consistent with
the Article 9(4)(e) obligation and, for systems in scope, the release gate is
not optional — it implements DORA's change management process. [citation
corrected 2026-09-05: this paragraph previously cited "DORA Article 14."
That citation was withdrawn because Article 14 is *Communication* — crisis
communication plans (¶1), communication policies for staff and stakeholders
(¶2), and a named person for the media function (¶3) — and contains no
change-management provision; paragraph 2 exists but carries no lettered
sub-paragraphs, so `(a)`, `(b)` and `(c)` do not exist. The obligation
described above is now correctly cited at DORA Article 9(4)(e), verified
verbatim against the primary (EUR-Lex, Regulation (EU) 2022/2554): financial
entities shall "implement documented policies, procedures and controls for
ICT change management, including changes to software, hardware, firmware
components, systems or security parameters, that are based on a risk
assessment approach and are an integral part of the financial entity’s
overall change management process, in order to ensure that all changes to
ICT systems are recorded, tested, assessed, approved, implemented and
verified in a controlled manner". Art. 9(4)(e) does not itself use the word
"rollback" — the ASDLC's rollback condition is retained as a control
independent of that specific wording. Corrected further 2026-09-05: the
sentence above previously asserted a documented rollback procedure,
post-implementation review and independent testing of changes for critical or
important functions as Art. 9(4)(e) requirements. Against the hashed primary
(`inputs/20260905-arnaud/prep/asdlc-standards/sources/dora_fulltext.txt`,
sha256 `25328c7e…3b4d1e`) the search terms `rollback`, `post-implementation`
and `independent testing` each occur zero times, with live one-word-swap
negative controls; and `change management` occurs in the Regulation only in
Art. 9(4)(e) and its closing subparagraph, so no other provision carries those three specifics.
None of the three claims was deleted; each is now marked in the sentence that
carries it. See
`inputs/20260905-arnaud/prep/asdlc-standards/` for the verification packet.
See also `domains/financial-services.md` for the same correction.]

SR 11-7 (Federal Reserve Supervisory Guidance on Model Risk Management) is
**supervisory guidance, not a rule**, and it is written in "should": in the
attachment held at
`inputs/20260905-arnaud/prep/D-20-primary/sources/sr1107a1.txt` (sha256
`d8ef343917…`) `should` occurs 180 times against a single `must`, and the
successor guidance on model risk management, SR 26-2 (17 April 2026), states
that it *"does not set forth enforceable standards or prescriptive
requirements; accordingly, non-compliance with this guidance will not result in
supervisory criticism against a banking organization"*, a sentence that carries
footnote 1: *"See 12 CFR Part 4, Subpart F, Appendix A (OCC); 12 CFR Part 262,
Appendix A (Board); 12 CFR Part 302, Appendix A (FDIC). However, supervisory
action may result for any violations of law or unsafe or unsound practices
stemming from insufficient management of model risk."*
**The fuller quotation supports the "not a rule" reading and bounds it in the
same sentence**: non-enforceable is not consequence-free, because supervisory
action still routes through violations of law and unsafe-or-unsound practices
rather than through the guidance. What it says of model change is that *"Material changes in model
structure or technique, and all model redevelopment, should be subject to
validation activities of appropriate range and rigor before implementation"*,
and of independence that validation *"should be done by people who are not
responsible for development or use"*. The independent validation condition in
this document's release gate (Condition 2) implements that principle at the
release boundary. **SR 11-7 does not specify a release process at all** — that
the validation is evidenced *at a release gate*, and that "material change to a
high-risk model" is the trigger, are **the ASDLC's own construction and are
unsourced**, not requirements of the guidance.

**Medical devices.** IEC 62304 (Medical Device Software Lifecycle Processes) is
a **paid IEC standard that this programme has not purchased and has not read**;
it is **OPEN under `T6.5`** and **no unofficial copy was fetched, sought or
considered**. `asdlc.md` states that *"nothing here asserts what they require"*,
and nothing here does. What follows is **the ASDLC's own construction and is
unsourced**: at a release boundary in medical-device software the ASDLC expects
configuration management records for the released software version, documented
test results demonstrating the software meets its requirements, and release
authorisation by a named responsible individual — the evidence bundle
(Condition 1) and the accountable human sign-off (Condition 4). The ASDLC
further applies independent review of test documentation to its highest risk
class, mapping to the independent validation condition (Condition 2). **Whether
IEC 62304 requires any of this, and what its Class C provisions say, has not
been checked and cannot be while the standard is unread.** Confirm against a
purchased copy before relying on this mapping.

**Aviation.** DO-178C (Software Considerations in Airborne Systems and Equipment
Certification) is a **paid RTCA standard that this programme has not purchased
and has not read**; it is **OPEN under `T6.5`** and **no unofficial copy was
fetched, sought or considered**. Per `asdlc.md`, *"nothing here asserts what
they require"*. What follows is **the ASDLC's own construction and is
unsourced**, using the industry-common airborne-certification vocabulary: at a
release boundary in certified airborne software the ASDLC expects software
configuration index documentation, problem reports against the released
software, system integration testing evidence, and approval by the certification
authority or delegated representative. The evidence bundle concept in this
document is structurally consistent with what the ASDLC understands a software
configuration index to be, and the evidence expected of a certified airborne
programme is substantially more detailed and process-specific than this
document's general framework. For software in DO-178C scope, the release
governance process described here must be adapted to whatever that programme's
own certification basis requires. The agentic execution loop's evidence bundle
is a necessary but not sufficient starting point. **Whether DO-178C states any
of this has not been checked and cannot be while the standard is unread.**
Confirm against a purchased copy before relying on this mapping.

**Pharmaceutical.** GAMP 5 (Good Automated Manufacturing Practice) is a **paid
ISPE guide that this programme has not purchased and has not read**; it is
**OPEN under `T6.5`** and **no unofficial copy was fetched, sought or
considered**. Per `asdlc.md`, *"nothing here asserts what they require"*. What
follows is **the ASDLC's own construction and is unsourced**, using the
industry-common qualification vocabulary. At the release boundary the ASDLC
expects Installation Qualification: the installed system documented against its
specification, installation evidence collected, and the installation formally
accepted by a qualified individual before the system is used for production
purposes — mapping to the evidence bundle (Condition 1) and accountable sign-off
(Condition 4). It expects Operational Qualification — confirming the system
operates as specified in its installed environment — to be complete before
production use, and treats it as part of the release Definition of Done:
production smoke tests and monitoring configuration (conditions 2 and 4 of the
release DoD) are its OQ evidence components. **Whether GAMP 5 states any of
this has not been checked and cannot be while the guide is unread.** Confirm
against a purchased copy with the organisation's quality team.

For all regulated industries: domain-specific release governance requirements
may impose additional conditions beyond the eight release gate conditions
described in this document. The release gate conditions here represent the
minimum governance floor. Regulated systems require the release gate conditions
plus the domain-specific requirements. Neither satisfies the other in isolation.

---

## Normative References

- UK DSIT / Responsible Technology Adoption Unit, *Portfolio of AI assurance
  techniques* (2023):
  https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques —
  catalogue of independent validation, documentation, testing, impact
  assessment, monitoring, and audit techniques. The release gate's evidence
  bundle and independent validation conditions operationalise the relevant
  portfolio entries.
- Perry et al., *Do Users Write More Insecure Code with AI Assistants?* (ACM
  CCS 2023, https://arxiv.org/abs/2211.03622) — empirical evidence behind the
  rubber-stamping detection methodology in *Accountable Human Sign-Off*.

---

_Layer 3 is not bureaucracy layered on top of engineering. It is the governance
that makes the engineering trustworthy in production. The loop produces
evidence. The release gate verifies the evidence. The approval chain authorises
the risk. The deployment executes it. Each step is the check on the previous one
— and the record that the check was performed._
