# Deployment Governance — Layer 3

_The Agentic Software Delivery Lifecycle, Layer 3: Deployment Governance._

See [manifesto.md](../manifesto.md) for the core values and the Agentic Loop.
See [manifesto-done.md](../manifesto-done.md) for the Definition of Done. See
[release-governance.md](release-governance.md) for release gate conditions and
the decision to deploy. See [operations/governance.md](operations/governance.md)
for what happens after production deployment.

---

## What is Deployment Governance?

Release governance governs the decision to deploy: whether the evidence is
sufficient, whether the authorisations are in place, and whether the compliance
conditions are met. Deployment governance governs the mechanics of executing
that decision: how the software moves through the environment chain, what
conditions must be satisfied at each environment boundary, and what the
deployment process itself must produce as evidence. Both are required. Release
governance without deployment governance produces well-authorised deployments
into uncontrolled environments. Deployment governance without release governance
produces technically smooth promotions of ungoverned changes. The combination is
what makes Layer 3 coherent.

This document governs environment management and the promotion process. It does
not repeat the release gate conditions from
[release-governance.md](release-governance.md). It assumes a release has been
authorised and addresses how that authorised release moves from the source
environment to production.

---

## Environment Model

The standard environment chain is: development, test, integration, staging,
production. Each environment serves a distinct governance purpose, and each
boundary between environments is a gate — a point at which specific conditions
must be satisfied before promotion is allowed. The environments are not
development conveniences. They are governance infrastructure.

**Development** is the engineering execution environment. Agents and engineers
work here. It is the environment where the loop runs: Specify, Design, Plan,
Execute, Verify, Validate. The output of a development environment is a
loop-complete artefact with an evidence bundle. Development is not merely an
engineering sandbox — it is a governance environment. Nothing leaves development
without a complete evidence bundle.

**Test** is the first external verification environment. Test runs the
evaluation suite (defined in
[manifesto-principles.md](../manifesto-principles.md) under Principle 8) against
the loop-complete artefact in an environment that is isolated from development
but not yet integrated with other systems. Test answers: does the artefact
behave as specified in isolation? Integration concerns — cross-service
dependencies, shared databases, message queue behaviour — are out of scope for
test. Test is about the artefact itself.

**Integration** is the environment where the artefact is verified in the context
of the systems it depends on and the systems that depend on it. Integration
answers: does the artefact interact correctly with its neighbours? Integration
failures are frequently specification failures: the interfaces between systems
were not fully specified, and the failure reveals what was assumed rather than
expressed. Integration failures discovered here are far less expensive than
integration failures discovered in staging or production.

**Staging** is the pre-production environment. Its governance requirement is
parity: staging must mirror the production configuration for any change where
configuration parity is material to the change's behaviour. For regulated
industries, this parity is often compliance-mandated. It cannot be assumed — it
must be enforced and verified at each promotion cycle. A staging environment
that diverges from production in configuration state, dependency versions, data
volumes, or infrastructure parameters is not a staging environment: it is a test
environment with a different name. Evidence that passes in a misconfigured
staging environment is evidence about the staging environment's configuration,
not about the production-equivalent behaviour of the change.

**Production** is the governed target environment. The only evidence that
matters in production is production evidence. Passing every test in every
preceding environment is necessary but not sufficient. Production smoke tests
are required. Production monitoring coverage is required. The deployment is not
done until it has been verified in production.

**At regulated environment boundaries**, environment parity requirements extend
beyond configuration. For pharmaceutical and medical device systems under GAMP 5
and IEC 62304, staging must use validated test data sets, validated
configuration baselines, and in some cases validated infrastructure components.
The environment itself must be qualified, not just configured. For financial
services systems under DORA and SR 11-7, the test and integration environments
must be isolated from production data in ways that are auditable. These
requirements do not override the standard environment model — they add specific
constraints to its implementation.

**What testing must pass at each gate.** Development to test: the evaluation
suite passes, and the evidence bundle is complete. Test to integration: test
environment evaluation suite results are clean, and there are no open defects of
severity that would block integration. Integration to staging: integration tests
pass, interface contracts between the artefact and its dependencies are
verified, and any performance or capacity tests relevant to the change are
complete. Staging to production: all conditions in the release gate
([release-governance.md](release-governance.md)) are met, rollback is tested,
monitoring is configured, and smoke test scripts are ready to execute
immediately post-deployment.

**Who controls promotion.** Development to test: the engineer or agent that
completed the loop, subject to the evidence bundle check. Test to integration:
the QA lead or automated gate, with no manual override that bypasses the
evidence bundle check. Integration to staging: the release manager, with the
evidence bundle and integration test results as inputs. Staging to production:
the release manager, with full release gate authorisation and the approved
deployment window from the change record.

**What artefacts must accompany a promotion request.** Every promotion request
must carry: the evidence bundle reference (not the bundle itself — the reference
to where it is stored and what its ID is), the test results from the source
environment (the results proving the gate conditions were met), and the approval
record from the person or system authorising the promotion. A promotion request
without these three artefacts is not a valid promotion request.

---

## Promotion Gates

Each environment boundary has specific promotion conditions. The most
consequential boundary is staging to production. The others matter because
failures to catch problems early are not free — they compound at the next gate.

**Development → Test.** The evidence bundle is complete. The evaluation suite
has been run and passes. Trace IDs are present. Policy check outputs are clean.
The loop output has not been edited after the evidence bundle was assembled.
This last condition deserves emphasis: an artefact that was modified after the
evaluation suite ran against it has an evidence bundle that no longer matches
the artefact. That is not a complete evidence bundle — it is a bundle from a
different version of the artefact.

Secrets scanning is a mandatory condition at this gate. No code, configuration
file, or build artefact containing an embedded credential — API key, service
token, private key, connection string, or other secret — may pass the
Development → Test boundary. This is a blocking condition, not a best-effort
check. All source files, configuration files, and build artefacts must be
scanned by a secrets detection tool before promotion. The scan must cover common
credential patterns: API key formats, private key headers, connection string
formats, and high-entropy string detection. The scan result — pass or fail — is
a required component of the promotion artefact. A promotion request that does
not include a secrets scan result is not a complete promotion request.

Agent-generated code carries a specific risk for credential embedding. An agent
operating in an execution context that includes credentials — model API
credentials, tool API keys, database connection strings — may produce code that
references those credentials directly, whether by referencing values it
encountered in retrieved examples, in its context window, or inferred from
training patterns. The resulting embedded credentials may be invalid
placeholders or real credentials from the execution context. Either case is a
governance failure: plausible-looking invalid credentials produce brittle code
that will fail silently in production; real embedded credentials represent an
immediate security exposure. The agent cannot be relied upon to apply credential
hygiene automatically. The promotion gate is the control.

Any finding from the secrets scan, regardless of whether the team assesses it as
a false positive, is treated as a block until formally resolved. Resolution
requires either remediation — the credential is removed from the source and
replaced with a reference to a secrets management system — or a formal waiver
with documented justification reviewed and approved by the accountable human. A
waiver is not a routine administrative step; it is a documented risk acceptance.

The correct architecture for credentials in agentic systems: all secrets used by
agents at runtime — model API keys, tool API credentials, database connections —
must be provided through a dedicated secrets management system at runtime
injection, never hardcoded in source, configuration, or agent specifications.
The promotion gate enforces this as a hard constraint. Any artefact that does
not conform to this architecture cannot pass the Development → Test gate.

**Test → Integration.** Test environment evaluation results are clean. No open
severity-1 or severity-2 defects. The artefact version being promoted is exactly
the version that produced the test results — not a subsequent patch. If a patch
was applied after the test results were produced, the patch must be tested
before promotion.

**Integration → Staging.** Integration tests pass for all interface contracts in
scope for this change. Performance tests relevant to the change show no
regression against the agreed baseline. The staging environment has been
confirmed to be in parity with the production configuration for the parameters
material to this change. If staging parity cannot be confirmed, promotion to
staging must be blocked until parity is restored or the parity gap is
documented, scoped, and accepted by the release manager as a known risk.

**Staging → Production.** This is the most consequential promotion gate. All
release gate conditions from [release-governance.md](release-governance.md) must
be met. The deployment window is approved. The on-call engineer is notified and
prepared. The rollback procedure has been tested within 48 hours. Smoke test
scripts are ready to execute immediately after deployment.

The evidence-passes-staging-but-fails-production failure pattern deserves
specific treatment because it is common and its cause is frequently
misidentified. When a change that passed staging evaluation fails a production
smoke test, the instinctive response is to classify it as a deployment failure
and focus on the change. The correct first question is: is staging actually in
parity with production? If staging is not in parity — different configuration,
different dependency versions, different infrastructure parameters — then the
failure is not a deployment failure. It is a staging parity failure. The change
behaved correctly in the environment it was tested in. The deployment executed
correctly. The governance failure is that staging did not represent production
accurately. Misidentifying staging parity failures as deployment failures
produces bad rollback decisions, bad incident classifications, and no fix for
the underlying governance problem.

Skipping a gate is not a deployment risk that can be managed — it is a
governance failure. A promotion that bypasses a gate has produced an artefact in
the destination environment whose behaviour in that environment has not been
verified. If the unverified behaviour causes an incident, the incident is the
direct consequence of the skipped gate, and the incident record should reflect
that.

---

## Progressive Delivery

Progressive delivery is a deployment strategy that decouples the deployment of
new code from the full commitment of production traffic to that code. Used
correctly, it reduces deployment risk for Tier 2 and Tier 3 systems by enabling
observation of real production behaviour on a bounded subset of traffic before
full cutover. The deployment governance requirements for progressive delivery
are distinct from the feature flag governance described in the next section:
feature flags control which users or sessions see a feature; progressive
delivery controls what proportion of production infrastructure runs which
version.

**Blue/green deployment.** Both the current version (blue) and the new version
(green) run simultaneously in the production environment. Traffic is routed to
green after the new version passes production smoke tests. If the new version
fails smoke tests or produces anomalous behaviour within the observation window,
traffic is switched back to blue without requiring a rollback in the traditional
sense: the blue version was never taken offline. For Tier 3 systems where the
cost of a failed deployment is high and where rollback time is a governance
constraint, blue/green deployment is the recommended default deployment
strategy. The blue environment must remain operational and ready to receive
traffic for the full duration of the observation window. An observation window
that ends before blue is decommissioned is the minimum safe period; the
appropriate window length is determined by the system's traffic patterns and the
complexity of the change.

**Canary deployment.** A small, defined percentage of production traffic is
routed to the new version (the canary) while the remainder continues on the
current version. The canary observation period generates production evidence
before the full cutover decision is made. The following governance conditions
apply to any canary deployment.

_Traffic percentage._ The initial canary traffic percentage must be documented
in the release artefact before deployment begins. Practitioner defaults: 5% for
Tier 3 systems with high blast radius; 10–20% for Tier 2 systems. The percentage
must be set low enough that canary failures have bounded user impact but high
enough that the observation period generates statistically meaningful signal
within the defined observation window. Undocumented traffic percentages — "we'll
start small and see" — are not acceptable; the percentage is a governance
parameter, not an operational judgment made under time pressure.

_Observation window._ The minimum duration of the canary observation period
before cutover is authorised must be specified in the release artefact and is
not subject to override under business pressure. The window must be calibrated
to the system's traffic patterns: a system receiving high request volumes
achieves statistical significance more quickly; a low-traffic system requires a
longer window to generate equivalent evidence. A window that is too short to
produce meaningful signal is not an observation period — it is an accelerated
deployment with delayed attribution of failure.

_Progression criteria._ The quantitative thresholds that determine whether the
canary advances to full cutover or is rolled back must be defined before
deployment and must include: error rate versus baseline, output quality rate
versus baseline (from sampled evaluation), latency versus baseline, and cost
anomaly signal versus baseline. These criteria must be expressed as specific
numeric thresholds, not as qualitative assessments. If any criterion fails
during the observation window, the canary is rolled back — automatically if the
progression criteria include automated rollback triggers, or immediately upon
detection if monitoring is manual. Vague criteria — "we will watch it for a bit
and decide" — are not acceptable progression criteria. They transfer a
governance decision into a judgment call made under production pressure, which
is precisely the condition under which governance fails.

_Rollback authority and trigger._ The canary may be rolled back manually by the
on-call engineer or the release manager at any point during the observation
window without requiring a formal change record for the rollback. Automatic
rollback triggers — defined as part of the progression criteria — fire without
human intervention when their thresholds are breached. The rollback time for a
canary deployment must be tested before the canary is initiated; the same
rollback testing requirement that applies to the release gate applies here. A
canary deployment whose rollback has not been tested is a canary deployment
without a validated exit path.

Progressive delivery does not replace the release gate — it adds a production
validation phase after the gate has been passed. The release gate certifies that
the artefact is fit for production deployment. Progressive delivery governs how
that deployment is staged to limit the blast radius of any defects that the gate
did not catch. Both are required for Tier 2 and Tier 3 systems.

---

## Feature Flag Governance

Feature flags are a deployment mechanism, not an engineering convenience. When
used correctly, they decouple deployment (shipping the code) from release
(enabling the behaviour), which reduces deployment risk and makes rollback
faster. When governed poorly, they accumulate as flag debt: code paths that are
flagged but never cleaned up, flags whose semantics are unclear, flags with
unknown blast radii, and flags that were created by agents and never reviewed by
humans.

Feature flag debt is a particular risk in agentic systems. An agent that writes
flag-protected code to satisfy a specification may create a flag that is
coherent within the context of that loop. Subsequent loops may modify the
flagged behaviour without awareness of the flag's original scope or removal
criteria. The flag accumulates state across loops that no single loop owns.

**When to use feature flags.** Use feature flags when the deployment risk of
enabling the change immediately in full production is higher than the
operational overhead of a flag. Phased rollout to a percentage of traffic,
canary deployments with rapid rollback, and changes that need to be
dark-launched for compliance or testing reasons are good candidates. Do not use
feature flags as a substitute for completing the engineering work. A flag
protecting code that does not yet meet the Definition of Done is not a
deployment mechanism — it is a way to ship incomplete work. That is what the
Definition of Done is designed to prevent.

**Flag creation.** Every feature flag must be created with: a named owner (the
person responsible for the flag through its lifecycle), a description of what
behaviour the flag controls and why it is flagged rather than deployed
unconditionally, the conditions under which the flag will be removed (the
removal criterion), and the blast radius if the flag is stuck in either state. A
flag without a removal criterion is technical debt with a deployment mechanism.

**Flag active state.** While a flag is active in production, its owner is
responsible for monitoring the flagged behaviour. The blast radius assessment
from flag creation must be reviewed against actual production conditions. A flag
that is protecting a change that is behaving correctly in production for thirty
days has a strong removal signal. A flag that is protecting a change that is
generating anomalies has a strong rollback signal. Neither decision should wait
for an arbitrary schedule.

**Flag removal.** Flags must be removed on a schedule set at creation, not
indefinitely deferred. The removal criterion established at creation is the
trigger. Removal means: the flag is deleted from the flag management system, the
code path it protected is unconditionally enabled, and the code path it
suppressed is removed. A flag that has been "removed from the flag system" but
whose code still contains conditional branches is not removed — the code is
still conditionally branched, and the flag logic is now invisible.

Flag removal in agentic systems requires an explicit handoff: the loop that
removes the flag must verify that all code paths previously guarded by the flag
are tested unconditionally. The evidence bundle for a flag removal loop should
include explicit confirmation that no flag-conditional branches remain and that
the evaluation suite covers the previously-flagged behaviour without flag
conditions.

---

## Rollback Operationalisation

The [manifesto.md](../manifesto.md) requires rollback plans as a component of a
complete loop output. [Release-governance.md](release-governance.md) requires
that rollback procedures be tested before the release gate opens. This document
requires that rollback be operationally ready at the time of production
deployment: known to the on-call team, rehearsed, assigned, and reviewed.

A valid rollback procedure satisfies all of the following:

**Documented with specific commands or steps.** Not a description of the
approach. Not "restore from backup." The specific sequence of commands, scripts,
or operations that reverses the deployment, with the expected outcome of each
step and the success criteria that confirm the rollback completed. The
documentation must be sufficient for an on-call engineer who was not involved in
the deployment to execute the rollback under incident conditions — which means
it must be unambiguous, complete, and accessible without dependencies on the
person who wrote it.

**Tested in a representative environment within 48 hours of production
deployment.** The test result is recorded: environment, date, time, duration,
outcome, and the name of the person who conducted the test. A rollback procedure
that has not been tested is not a rollback procedure — it is a hypothesis. The
48-hour window is not arbitrary: it ensures the test reflects the current state
of the environment, the current configuration, and the current operational team.
A test conducted a week before deployment reflects a week-old state.

**Time-to-rollback measured and within the agreed window.** The time from
incident declaration to service restoration must be measured during the rollback
test and must fall within the recovery time objective agreed for the system. If
the rollback procedure exceeds the recovery time objective, the procedure is not
acceptable. The fix is to redesign the rollback, not to widen the recovery time
objective to fit the procedure.

**Assigned to the on-call engineer for the release.** The on-call engineer
responsible for the deployment knows where the rollback procedure is, has read
it, and knows how to execute it. An assignment record exists in the release
artefact. A rollback procedure that is documented somewhere but whose location
is unknown to the on-call engineer at incident time is effectively unavailable.

**Reviewed by the accountable human.** The P12 accountable human has reviewed
the rollback procedure and confirmed that it represents an acceptable risk
mitigation for the deployment. This is not a technical review — the accountable
human is not necessarily the person best placed to evaluate the technical
correctness of the rollback steps. It is a risk review: does the rollback, if
executed, restore the system to a known safe state within an acceptable time
window?

A rollback plan that has never been tested is not a rollback plan — it is a
hope. In agentic systems, this is a particularly important discipline because
agents can produce rollback procedures that are technically plausible but have
never been executed against actual system state. Agent-generated rollback
procedures must be tested by a human in a representative environment before they
are accepted as valid.

---

## Deployment Evidence

The deployment process is the final step in the Layer 3 audit trail. The loop
produces the evidence bundle. The release gate verifies it. The change
management process authorises it. The deployment process must itself produce
evidence that the authorised change was deployed correctly, at the authorised
time, in the authorised configuration.

The deployment must produce and record the following, as a minimum:

**Deployment ID.** A unique, system-generated identifier for this specific
deployment event. The deployment ID is referenced in the change record, the
compliance filing, and the operational monitoring configuration for the change.
It is the identifier against which incident reports are written if the
deployment causes a production issue.

**Deployment timestamp.** The exact UTC timestamp at which the deployment
completed, in YYYY-MM-DD HH:MM:SS UTC format. Not the time the deployment was
initiated. Not an approximation. The completion timestamp is the moment at which
the change became active in the production environment. This is the reference
point for post-deployment monitoring windows, the start of the 24-hour
post-deployment smoke test period, and the timestamp referenced in compliance
filings.

**Configuration state hash at deployment time.** A cryptographic hash of the
configuration state of the production environment at the moment of deployment,
sufficient to detect post-deployment configuration drift. The configuration
state hash is not the artefact hash — it captures the environment configuration,
not just the deployed artefact. If a subsequent configuration change produces a
production incident, the configuration state hash allows the investigation to
determine whether the environment was in the authorised state at the time of the
incident or had drifted since deployment.

**Test results in the target environment.** The results of the production smoke
tests executed after deployment. These are distinct from the staging evaluation
results in the evidence bundle. They are production-environment evidence that
the deployment is operational. Smoke test results include the timestamp of
execution, the specific tests run, and the pass/fail outcome for each.

**Named human who authorised the production deployment.** The name, role, and
timestamp of the person who authorised the production deployment in the release
manager role. This is separate from the P12 accountable human sign-off — the
release manager's authorisation is the operational decision to deploy; the P12
sign-off is the governance decision to proceed. Both names appear in the
deployment evidence.

**SLSA provenance attestation (Tier 2 and Tier 3 systems).** For systems at Tier
2 and above, a SLSA (Supply-chain Levels for Software Artifacts) provenance
attestation must be generated by the build process and included in the
deployment evidence record. The attestation is a machine-verifiable,
cryptographically-signed record that states: the source repository and commit
from which the artefact was built, the build process and configuration used to
produce it, and the identity of the build service. At SLSA Level 2 — the minimum
required for these tiers — the build must have been executed by a hosted,
auditable build service rather than a local build process. The attestation
identifier is recorded in the deployment evidence record alongside the
deployment ID and configuration state hash.

The SLSA attestation closes a specific gap in the deployment audit trail:
without it, there is no cryptographic link between the source repository, the
build process, and the deployed artefact. An adversary who can inject content
between the source and the build, or between the build and the deployment, would
not be detectable by the deployment evidence record alone — because that record
describes what was deployed, not how the deployed artefact came to be. The
provenance attestation is the control for this supply chain attack class. It
makes the artefact's lineage verifiable, not merely asserted.

For Tier 1 systems, SLSA attestation is recommended but not mandated by this
document. Teams operating Tier 1 systems in regulated industries should consult
the applicable regulatory framework to determine whether supply chain
attestation requirements apply to their context.

Reference: SLSA v1.0 framework (https://slsa.dev).

This deployment evidence forms the Layer 3 portion of the system's audit trail.
The Layer 2 audit trail is the evidence bundle from the loop. The Layer 3 audit
trail is the deployment evidence. Together, they answer the governance question
that any regulated system must be able to answer: what was deployed, when was it
deployed, who authorised it, what was the configuration state at the time, and
was the deployment verified in production?

Without complete deployment evidence, incident investigation is incomplete,
compliance filings are incomplete, and the change record cannot be closed. A
deployment that is not fully evidenced is not a deployment that governance can
stand behind.

---

_Deployment governance is the operational expression of release decisions. The
decision to deploy is only as sound as the environment it deploys into, the gate
conditions that governed its journey there, and the evidence that records what
actually happened when it arrived._
