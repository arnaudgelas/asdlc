# Maintenance Governance — ASDLC Layer 4

_Long-term stewardship of agentic systems in production._

See the [Manifesto](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto.md) for the engineering execution layer (Layer
2). See [Operations Governance](operations/governance.md) for the operational
runtime layer. See [Operational Definition of Done](operations/dod.md) for the
Layer 4 readiness conditions.

---

## What is Maintenance Governance?

Maintenance governance is what happens after the system is operationally
running. It is the stewardship of the system's long-term health: keeping it
current as its environment changes, managing its security surface as
vulnerabilities are discovered, governing its technical debt before it
compounds into architectural failure, and managing the eventual controlled
retirement of a system that has served its purpose. The operational layer (see
[Operations Governance](operations/governance.md)) governs the system's runtime
behaviour — incidents, SLOs, on-call. Maintenance governance governs the
system's structural health over a policy-set 12–36 month horizon after
deployment. The two are not the same, and the failure mode of conflating them
is a maintenance backlog that grows invisibly until a security incident or
architectural crisis forces it into view.

---

## Ownership and Stewardship Model

Every production component must have a named steward. The steward is not the
same person as the accountable human who accepted production accountability at
the release decision. The accountable human owned the release: the evidence
review, the deployment approval, the acceptance of production risk at a point in
time. The steward owns the system from deployment onward, indefinitely, until
either the system is retired or ownership is formally transferred to a qualified
incoming steward. The distinction matters because the accountable human's
obligation was time-bounded; the steward's obligation is open-ended.

Steward responsibilities cover five areas:

**Specification currency.** Keeping the specification current as the system's
operating environment changes. A specification that was accurate at deployment
but has not been updated as the system's inputs, dependencies, or regulatory
context have changed is a misleading document. A misleading specification
produces misleading evaluations — the evaluation suite tests for behaviour that
is no longer the correct behaviour. The steward is responsible for triggering
specification reviews when the environment changes materially, and for ensuring
that specification updates go through the loop (Specify → Verify → Govern)
rather than being made as informal documentation edits.

**Re-verification triggering.** When the operating environment changes
materially — a dependency is updated, a regulatory requirement shifts, input
distribution drifts from the deployment baseline, or the system is extended to
cover new use cases — the steward is responsible for determining whether
re-verification is required and, if so, for initiating a loop iteration. The
threshold for "materially changed" should be defined at deployment time and
documented in the maintenance governance record; a steward who is trying to make
this judgment without a predefined threshold is making a governance decision
each time rather than applying a governance policy.

**Security patch lifecycle.** Managing the security patch process for the
component and its dependencies. See the Security Patch Management section below
for the specific patch governance requirements. The steward is not necessarily
the person who applies patches, but they are accountable for ensuring the patch
SLOs are met.

**Value realisation monitoring.** Monitoring the system's performance against
the original success criterion defined in Layer 1 and carried through the
delivery lifecycle. The system was built to achieve a measurable business
outcome. The steward is responsible for confirming that outcome is still being
achieved, or for escalating if performance against the success criterion is
degrading. This is not a performance management function — it is a governance
function. A system that is technically healthy but is no longer delivering its
intended value is a candidate for re-specification or retirement.

**Deprecation decision.** When the conditions for deprecation are met (see
Deprecation and Decommission section below), the steward makes or escalates the
deprecation decision. The steward has the information to make this call: they
know the system's maintenance cost, its value realisation trend, and its
technical health. The business demand sponsor who validated the original need
must concur on the deprecation decision, but the steward initiates it.

**Substrate diversity audit (for systems depending on intelligence).** For
systems whose actions are informed by claims in the domain graph governed
under the Intelligence Governance Manifesto (IGM), the steward conducts a
quarterly substrate diversity audit alongside the architectural health review.
The audit examines three dimensions of the intelligence the system depends on:

- *Source diversity in load-bearing claims.* The percentage of the system's
  load-bearing claims — the claims that, if wrong, would cause the system's
  most consequential actions to be wrong — that derive from different
  organisations, vendors, or jurisdictions. A substrate that is corroborated
  predominantly by sources from a single origin is not corroborated; it is
  one source restated.
- *Contradiction preservation rate.* The proportion of claims in domains with
  known divergences (regulatory interpretation differences, vendor-specific
  practice, cross-jurisdictional conflict) that retain at least one recorded
  contradiction in the domain graph. A domain known to be contested whose
  graph contains no contradictions is a substrate that has been flattened —
  by ingest filtering, by silent overwrite, or by adversarial pruning.
- *Expert-network health.* The currency, breadth, and peer-consultation rate
  of the named experts who serve as assertion authorities for the claims the
  system depends on. An expert network whose consultation rate has declined
  is a network whose judgments are increasingly being inherited rather than
  refreshed.

Warning signals from the audit, both figures policy-set and chosen rather than
measured: more than 80% of load-bearing claims sourced from a single
organisation, vendor, or jurisdiction; less than 2% contradiction density in a
domain with known divergences; or a sustained decline in expert peer
consultation against the deployment baseline. Any warning signal triggers a
documented remediation plan with a defined window: expand the IGM Harvest or
Capture acquisition modes to broaden the source base; activate cross-domain
linking to surface analogous contradictions from adjacent domains; or escalate
to the IGM revision, assertion, or semantic governance authority responsible
for the affected claim class. A substrate diversity audit that surfaces a
warning signal without producing a remediation plan within a policy-set 20
business days is itself a steward governance failure, equivalent to leaving an
architectural health degradation unaddressed.

### Ownership Transfer Protocol

When a steward changes — personnel moves, team reorganisation, role change — the
transfer must satisfy a specific accountability test before the incoming steward
accepts ownership. The test is the P12 accountability test applied to
maintenance: can the incoming steward, using the specification, evidence bundle,
and deployment artefacts, recover the system's intent, understand the decisions
made during development, and reproduce the system's expected behaviour? If not,
the knowledge gap must be closed before the transfer is accepted as complete.

Closing a knowledge gap before a steward transfer may require: a session with
the outgoing steward to walk through the specification and known failure modes;
a review of the evidence bundle and the Learn phase documentation from the most
recent loop iterations; a review of any post-incident updates to the
specification or evaluation suite; and confirmation that the incoming steward
can access the specification, evidence bundle, trace retention store, and
rollback procedure. The incoming steward should complete a documented review of
each of these artefacts and confirm access before the transfer record is closed.

A transfer that bypasses this test does not transfer accountability — it
abandons it. An organisation that allows stewardship of production components to
lapse without a qualified transfer has a governance gap that will be discovered
at the worst possible time: during an incident, a security audit, or a
regulatory review.

### Steward vs. On-Call Engineer

The steward is not the on-call engineer, though they may be the same person for
small teams. The on-call engineer handles runtime incidents. The steward governs
the system's long-term health. The steward's obligations are not
incident-driven; they operate on a planned cadence (quarterly architectural
health reviews, defined patch SLOs, scheduled value realisation reviews). Define
the boundary between these roles explicitly in the operational runbook. In
practice, the steward is typically the person who knows the system most deeply;
involving them as an escalation point for complex incidents (rather than as
on-call first responder) is usually the right design.

### Steward Capacity and Portfolio Governance

The stewardship model assumes that the named steward maintains active knowledge
of the system's specification, operating environment, and maintenance
obligations. This assumption fails when a steward is accountable for more
systems than their available time and cognitive bandwidth can support. The
result is not a sudden governance collapse — it is a gradual degradation:
operational DoD reviews that confirm conditions without genuinely checking them,
knowledge gaps that accumulate until the steward can no longer pass the P12
accountability test, and maintenance obligations that slip past their scheduled
cadence without detection.

**Portfolio limits as governance signals.** As a policy-set practitioner
calibration starting point — chosen by the authors rather than derived from
measured steward load — a single steward should not be accountable for more than
five Tier 3 systems, ten Tier 2 systems, or twenty Tier 1 systems concurrently. These
are not hard limits — they are signals. A steward approaching these limits
without additional support, tooling assistance, or workload reduction is at
elevated risk of the gradual degradation described above. The portfolio limit is
a conversation trigger, not an enforcement threshold.

**Portfolio limits for intelligence-bearing systems.** The limits above
assume systems whose maintenance burden is bounded by the system's own
operational and architectural surface. For systems that depend on
intelligence governed under the Intelligence Governance Manifesto (IGM) —
where the steward must additionally track claim epistemic tier, decay
windows, contradiction state, and feedback-loop closure to the IGM
revision/assertion/semantic authorities — the steward's effective load per
system is materially higher. The reason is the concurrent lifecycles a
steward must hold in mind: the system's operational lifecycle, the system's
specification lifecycle, and the lifecycles of every load-bearing claim the
system depends on. Composite-state tracking — knowing at any moment which
claims are fresh, which are projected-stale, which carry unresolved
contradictions, and which have outstanding re-verification work — cannot be
handled at the same density as routine operational stewardship.

For intelligence-bearing systems, the portfolio limit is reduced to a policy-set
no more than three systems per steward, regardless of autonomy tier — again a
chosen default, not a measured capacity. This reduction
is not a refinement of the tier-calibrated limits — it supersedes them for
the intelligence-bearing class. A steward accountable for three Tier 3
intelligence-bearing systems is at the limit; a steward accountable for one
Tier 3 intelligence-bearing system and four Tier 1 non-intelligent systems
is also approaching limit, because the intelligence-bearing system imposes
the IGM-coordination overhead regardless of its tier. The portfolio steward
function (see below) tracks intelligence-bearing system count separately
from total system count for each steward.

**Tooling-assisted stewardship.** Several of the operational DoD conditions that
the steward must verify quarterly lend themselves to automated monitoring:
security scan recency (was the last scan within the required window?), SLO
configuration state (are all required SLOs configured and alerting?), on-call
assignment presence (is a named engineer currently assigned?), and runbook
modification date (has the runbook been updated since the last release?).
Automating the monitoring of these conditions reduces the steward's routine
review burden without removing the steward's accountability. The conditions that
require steward judgment — specification currency, knowledge depth, value
realisation monitoring, and the quality of the runbook's known failure modes —
cannot be automated. Freeing the steward from routine checks makes the
judgment-requiring conditions manageable across a larger portfolio.

**Portfolio-level stewardship.** Organisations with large fleets of production
agentic systems may establish a portfolio steward function to track aggregate
operational DoD compliance across the fleet, identify individual stewards at
capacity risk, and coordinate stewardship transfers before they become
emergencies. The portfolio steward does not hold per-system accountability —
that remains with the named steward for each system — but holds accountability
for the health of the stewardship function itself: are all systems stewarded?
Are stewards at capacity operating with tooling support? Are stewardship
transfer procedures being followed? A fleet of production systems where every
system nominally has a steward but many stewards are over-capacity is a fleet
with de facto stewardship gaps.

**Steward communities of practice.** Stewardship expertise — the ability to
assess specification currency, govern dependency updates, oversee value
realisation monitoring, and conduct meaningful operational DoD reviews — is not
a skill most engineers arrive with. It is developed through practice and through
access to others facing similar governance challenges. Organisations that
develop stewardship as an organisational capability — through documented
governance decision libraries, shared runbook templates calibrated to their
environment, and periodic steward retrospectives that surface recurring
challenges — build stewardship expertise that survives individual personnel
changes. Organisations that treat stewardship as an individual responsibility
with no organisational infrastructure around it will lose the accumulated
knowledge each time a steward moves on.

---

## Agent-Assisted Stewardship

The stewardship model's core assumption — that the named steward maintains
active, current knowledge of the system across its full maintenance lifecycle —
places an increasing cognitive demand on stewards as portfolios grow and systems
age. Governance agents can assist with specific, well-bounded stewardship tasks:
initial vulnerability triage, dependency update impact modelling, and
portfolio-level state monitoring. In each case, the agent performs the
analytical work; the steward makes the governance decision. The agent's
involvement reduces the routine analytical burden on the steward; it does not
transfer the steward's accountability.

**Vulnerability triage assistance.** For each disclosed vulnerability reaching
the steward, a governance agent may perform an initial exploitability assessment
against the system's specific deployment context. This assessment checks whether
the vulnerable code path is reachable given the system's actual dependency
usage, whether the system's configuration includes mitigating controls that
reduce or eliminate exploitability, and whether a VEX status of "not affected"
or "affected" is determinable from available information without human judgment.
The agent produces a triage recommendation with its full reasoning documented —
the code path reachability analysis, the mitigating control inventory checked,
and the basis for any VEX status recommendation. The steward reviews this
recommendation and makes the final VEX status determination. The triage SLOs
defined in the Vulnerability Disclosure and Response section — Critical: 4
hours, High: 24 hours — measure time to steward determination, not to agent
recommendation. An agent recommendation produced within the SLO window that sits
unreviewed does not satisfy the SLO.

**Dependency update impact analysis.** When a dependency update is available —
whether for a security patch or routine maintenance — a governance agent may
model the update's impact before the steward decides on timing and scope. The
impact model identifies which parts of the system use the updated dependency
(including transitive dependents), estimates the test surface affected by the
update, and projects the blast radius of the update based on the specification's
blast radius assessment for the affected components. The steward uses this
analysis to prioritise the update within the patch SLO cadence and to scope the
required evaluation suite run: a dependency update whose impact is confined to a
low-coupling module with limited downstream dependents warrants a narrower
verification scope than one whose impact propagates across module boundaries.
The governance agent's impact analysis is an input to the steward's decision;
the steward's determination of update timing and verification scope is the
governance act that is recorded.

**Steward portfolio monitoring.** For stewards managing multiple systems, a
governance agent may continuously track portfolio-level governance state across
the full fleet the steward is accountable for. The agent monitors which systems
have operational DoD conditions failing based on continuous monitoring data,
which systems have patch SLOs approaching or breached, which systems have
steward assignment gaps or unresolved ownership transfer records, and whether
the steward's portfolio is approaching the tier-calibrated portfolio limits
defined in the Steward Capacity and Portfolio Governance section. The output of
portfolio monitoring is a governance state dashboard — a structured view of what
requires the steward's attention, ordered by urgency and SLO proximity. It is
not a set of automated actions: the agent surfaces; the steward reviews and
acts. A dashboard showing an approaching SLO does not extend the SLO; it gives
the steward the visibility to act before the SLO is breached.

**Epistemic requirements for maintenance governance agents.** Governance agents
performing stewardship assistance are subject to the governance agent framework
defined in [governance/agents.md](governance/agents.md). Their outputs are
labeled agent-proposed and require documented steward review before they are
recorded as governance evidence. The steward's determinations — VEX status,
patch timing, specification update decisions, portfolio prioritisation calls —
are human decisions recorded in the governance record. They are not agent
outputs that happen to be approved: the steward's review and determination is
the governance act, and the record must reflect that. An agent triage
recommendation that the steward adopts without independent review is not a
steward determination — it is an agent determination with the steward's name on
it, which does not satisfy the VEX status assignment requirement.

---

## Security Patch Management

Agent-generated systems have two distinct security patch surfaces that must be
governed separately.

### Patch Surface 1: The Generated Component

Vulnerabilities in the code the agent wrote. The agent may have generated code
with security flaws: injection vulnerabilities, insecure defaults, improper
error handling, or logic errors that create exploitable conditions. These
vulnerabilities may not be visible at deployment time and may be discovered
through subsequent analysis, security research, or incident.

Govern this surface with:

**Automated static analysis on a defined schedule.** Not just at deployment —
continuously, on a defined cadence. Static analysis that runs only at deployment
misses vulnerabilities introduced through dependency updates, environmental
changes, or newly-discovered attack patterns that postdate the deployment
analysis. Schedule automated static analysis weekly for active systems and
monthly for stable, low-change systems. The schedule should be documented in the
maintenance governance record and the results should be reviewed by the steward.

**Time-to-patch SLOs by severity.** Define the maximum acceptable time between
vulnerability identification and patch deployment, by severity tier.
Policy-set practitioner defaults, chosen by the authors against no named industry source: Critical vulnerabilities (CVSS 9.0+): 48 hours. High severity (CVSS 7.0–8.9): 7 calendar
days. Medium severity (CVSS 4.0–6.9): 30 calendar days. Low severity (CVSS below
4.0): next planned maintenance window, with a ceiling of 90 days. These defaults
should be calibrated to the system's regulatory context: DORA Article 9 (ICT
vulnerability management for financial entities) and equivalent frameworks in
other regulated industries may impose stricter requirements. Where regulation
imposes a stricter SLO, the regulatory requirement supersedes these defaults.

**Patch process through the loop.** Patches are specifications. A security patch
to an agent-generated component should enter the agentic loop — Specify (what
vulnerability is being patched, what the fix must achieve), Execute, Verify —
not be applied as a manual edit that bypasses the governance process. Manual
edits to agent-generated code outside the loop create undocumented divergence
between the specification, the evidence bundle, and the running code. That
divergence compounds: a future loop iteration based on the pre-patch
specification will not know about the manual change and may overwrite or
conflict with it.

### Patch Surface 2: Agent-Chosen Dependencies

Libraries, packages, and APIs that the agent selected during the Execute phase.
The agent's dependency choices may not align with what the team would have
chosen deliberately: the agent may have selected a library that was popular in
its training data but has since been abandoned, a version with a known
vulnerability, or a licence that is incompatible with the production
environment.

Govern this surface with:

**SBOM generation at deployment.** A software bill of materials, generated at
deployment, listing every dependency the system includes, its version, and its
provenance. The SBOM is a condition of the operational DoD (see
[Operational Definition of Done](operations/dod.md)). For systems deployed in
the EU, SBOM generation is required for compliance with the EU Cyber Resilience
Act. The SBOM is not just a compliance artefact — it is the operational
instrument that makes dependency patch governance tractable. Without an accurate
SBOM, dependency vulnerability scanning cannot reliably identify what needs to
be patched.

**Automated dependency vulnerability scanning on a defined schedule.** The SBOM
is the input to automated vulnerability scanning tools that identify known
vulnerabilities in listed dependencies. Schedule scanning on the same cadence as
static analysis. Scan against the current SBOM, not the SBOM from the last
release: dependencies can introduce vulnerabilities through transitive
dependency updates that do not change the direct dependency version.

**SBOM maintenance and re-verification.** When a dependency patch is applied,
the SBOM must be updated to reflect the new dependency state, and the evidence
bundle's verification must be re-run against the patched dependency
configuration. A patch that updates a dependency without updating the SBOM
creates an inaccurate compliance record and may miss transitive dependency
changes that the patch introduced.

### Regulatory Mapping

Map patch governance obligations explicitly to applicable regulatory frameworks.
For financial services: DORA Article 9 (ICT risk management, vulnerability
management) and Article 11 (ICT business continuity). For systems processing
personal data in the EU: GDPR Article 32 (security of processing) and the EU
Cyber Resilience Act SBOM requirements. For US financial institutions: SR 11-7
(model risk management), which is supervisory guidance written in "should" and
which says *"Validation activities should continue on an ongoing basis after a
model goes into use"* — a practice it recommends, not a requirement it
imposes. This is not an exhaustive regulatory mapping — the applicable
obligations depend on the system's jurisdiction, data classification, and use
case. Confirm applicable obligations with qualified regulatory counsel before
defining patch SLOs for regulated systems.

---

## Vulnerability Disclosure and Response

Security patch management governs the planned, scheduled response to known
vulnerabilities. Vulnerability disclosure governance covers the unscheduled
path: a report arrives — from an internal team, an external researcher, or an
automated scanner — and the system must respond with defined structure, defined
timelines, and defined accountability.

### Disclosure Intake

Every production system must have a defined disclosure channel: a named point of
contact and a documented method for receiving vulnerability reports. The channel
must accept reports from internal teams, external security researchers, and
automated scanning pipelines. The channel and its contact details must be
documented in the system's operational runbook. The steward is accountable for
the channel remaining operational — an unreachable or unmonitored disclosure
channel is a governance gap that the steward owns.

### Severity Triage

Every received disclosure must be triaged within defined SLOs from the time of
receipt:

- **Critical:** initial assessment within a policy-set 4 hours.
- **High:** initial assessment within a policy-set 24 hours.
- **Medium:** initial assessment within a policy-set 5 business days.
- **Low:** initial assessment within a policy-set 10 business days.

Triage produces four outputs, all documented in the maintenance governance
record: a confirmed or not-confirmed status for the reported vulnerability; a
CVSS score or equivalent severity rating; an exploitability assessment — is the
vulnerability exploitable in this system's specific deployment configuration?;
and assignment of a named remediation owner.

### VEX Status Assignment

For every disclosed vulnerability, a VEX (Vulnerability Exploitability eXchange)
status must be assigned and documented. The four recognised statuses are:

**Not affected.** The system is not affected by the vulnerability in its
deployed configuration. The exploitability assessment must support this
determination.

**Affected.** The system is affected; remediation is required. The triage output
must document the basis for this determination and the assigned remediation
owner.

**Fixed.** The vulnerability has been remediated. The patch deployment record
and updated evidence bundle constitute evidence of this status.

**Under investigation.** Exploitability is being assessed. This status requires
a re-triage date — the investigation cannot remain open-ended.

VEX status must be updated as the investigation progresses; a status recorded at
triage that is not updated to reflect subsequent findings is an incomplete
governance record. For systems with published SBOMs, VEX documents should be
published alongside the SBOM so that downstream consumers of the SBOM can assess
their own exposure.

### Remediation and Emergency Change Path

Remediation follows the normal patch SLO schedule where the severity permits.
For Critical or High vulnerabilities assessed as exploitable in the system's
deployment context, an emergency change path is available. The emergency change
path bypasses the normal gate scheduling queue — releases are not deferred to
the next scheduled release window — but it does not bypass gate conditions.
Evidence must be complete; no gate condition is waived under the emergency path.

The emergency change path requires:

**Accountable human approval.** A named accountable human must explicitly
authorise the use of the emergency change path, with the rationale documented.
This approval is not delegatable to an automated process.

**Evidence bundle completion.** The evidence bundle for the emergency release
must be completed before deployment. The urgency of the change does not relax
the verification requirements.

**Abbreviated canary deployment.** Where the urgency permits, a canary
deployment should precede full rollout. The canary scope and duration may be
abbreviated from the standard canary configuration, but rollback must be
pre-tested and confirmed ready before the canary proceeds. Where the urgency
genuinely precludes canary deployment, the accountable human's approval must
explicitly acknowledge this and document the accepted risk.

### Notification

For vulnerabilities in production systems that may affect users or data
subjects, the accountable human determines what notification obligations apply.
Regulated systems must apply the breach notification timelines and procedures
defined in [Operations Governance](operations/governance.md). The notification
obligation assessment is not optional: even where the determination is that no
notification is required, that determination and its basis must be documented.

Regulated organizations must consult the applicable domain file for
sector-specific breach notification timelines, regulatory escalation
requirements, and incident documentation obligations beyond the general
requirements in this section. Each domain file maps the general ASDLC
maintenance requirements to the regulatory framework applicable in that sector:

- Financial services: SR 11-7, DORA, EU AI Act, MiFID II — see
  [Financial Services Regulatory Alignment](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/domains/financial-services.md)
- Medical devices: FDA, IEC 62304, ISO 14971, MDR — see
  [Medical Devices Regulatory Alignment](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/domains/medical-devices.md)
- Aviation: DO-178C, ARP4754A, EASA — see
  [Aviation Regulatory Alignment](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/domains/aviation.md)
- Automotive: ISO 26262, SOTIF, UNECE WP.29 — see
  [Automotive Regulatory Alignment](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/domains/automotive.md)
- Pharmaceuticals: GxP, 21 CFR Part 11, ICH guidelines — see
  [Pharma Regulatory Alignment](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/domains/pharma.md)
- Defense and government: CMMC, FISMA, NIST SP 800-53 — see
  [Defense and Government Regulatory Alignment](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/domains/defense-government.md)

### Root Cause Analysis and Prevention

Every Critical or High vulnerability that reached production — whether through a
newly disclosed vulnerability or through a vulnerability that was present at
deployment and not detected — triggers a root cause analysis (RCA).

The RCA must answer three questions: Which ASDLC control should have caught this
vulnerability before it reached production? Was that control present and
functioning at the relevant stage? What change to the control, or to the
evaluation suite, would prevent a similar vulnerability from reaching production
in a future loop iteration?

The RCA output must produce three changes:

**Evaluation suite update.** A new adversarial test case is added to the
affected system's evaluation suite that would catch this class of vulnerability.
The evaluation suite must be updated before the next loop iteration runs.

**Gate condition update.** If the RCA identifies a control gap — a gate
condition that was absent, inadequately specified, or present but not
functioning as designed — the relevant gate condition documentation must be
updated to address the gap.

**Specification update for the next iteration.** The RCA's findings must be
reflected in the specification for the system's next loop iteration, so that the
agent's execution context includes the constraint or pattern that the RCA
identified as missing.

An RCA that produces a written analysis but does not produce these three outputs
has not completed the prevention cycle. The steward is accountable for ensuring
all three outputs are produced and integrated before the RCA record is closed.

---

## Vendor and External Dependency Management

Agent-generated systems differ from hand-authored systems in one specific
dimension of dependency governance: the agent selects dependencies based on what
was available and appropriate in its execution context, not based on a
deliberate strategic decision by the organisation. This includes the foundation
models the agents invoke, the external API services the agents call as tools,
the retrieval and knowledge services the agents query, and the third-party data
sources the agents use. Each of these represents an external dependency with its
own lifecycle, reliability profile, and discontinuation risk.

**Dependency inventory requirement.** Every production agentic system must
maintain a live inventory of its external dependencies, distinct from the SBOM's
dependency tree (which captures software libraries). The external dependency
inventory covers: foundation model providers and the specific model versions in
use, third-party tool APIs and their API version, retrieval and knowledge
service providers, and external data source providers. The inventory is
maintained by the system steward and reviewed at each quarterly operational DoD
check.

**Foundation model lifecycle risk.** Foundation model providers deprecate
models, change API interfaces, and modify model behaviour across versions
without always providing the advance notice that software library maintainers
provide. The steward must document, for each foundation model in use: the model
version pinned in the production deployment, the provider's published model
lifecycle policy and deprecation timeline, the provider's SLA for API
availability, and the expected impact on the system if the model is deprecated
without notice. Where a provider does not publish a formal deprecation policy,
this absence is itself a risk that must be documented.

**Dependency health monitoring.** External dependencies are monitored on a
defined cadence — monthly is the minimum — for: deprecation notices published by
the provider, API changelog announcements that could affect the system's
behaviour or integration contracts, pricing changes that affect cost
projections, and SLA revisions. Monitoring is the steward's responsibility. A
dependency health change that affects system behaviour, cost, or availability
triggers the same re-verification assessment that an operating environment
change triggers.

**Migration plan requirement.** For Tier 2 and Tier 3 systems, a live migration
plan must be maintained for each critical external dependency — a dependency
whose failure or discontinuation would prevent the system from delivering its
business purpose. The migration plan documents: the identified replacement
capability (or alternatives assessed), the estimated time required to migrate,
the specification and evaluation changes migration would require, and the data
migration considerations if the dependency holds persistent state. The migration
plan is reviewed and updated annually. A migration plan that was accurate at
deployment but has not been updated as the ecosystem evolved is not a live plan
— it is a historical document.

**Vendor concentration risk.** Where multiple production agentic systems in the
organisation's portfolio depend on the same external provider — the same
foundation model provider, the same tool API, the same retrieval service — the
shared dependency creates correlated failure risk. A provider outage or API
deprecation that affects one system affects all systems sharing that dependency
simultaneously. The steward function for each affected system must be aware of
this concentration, and portfolio-level dependency management should track
provider concentration explicitly. A portfolio where more than half of
production agentic systems depend on a single foundation model provider carries
a systemic risk that individual system stewards cannot see from their per-system
view.

---

## Technical Debt Lifecycle

Technical debt in agentic systems accumulates differently from hand-authored
code. A human engineer writing code over time tends to introduce debt through
shortcuts, deferred decisions, and knowledge gaps that are visible to code
review. An agent generating code tends to make locally optimal decisions — the
best implementation of the immediate specification — that may produce globally
suboptimal architecture that is not visible at the unit test or integration test
level. The agent does not have a holistic view of the system's evolutionary
trajectory; it has the specification it was given and the context it retrieved.

The result is architectural debt that can be invisible to the evaluation suite:
coupling that grows across releases, module boundaries that drift as
specifications evolve, and change amplification that compounds until a routine
change to component A requires changes to B, C, and D.

### Measuring Architectural Health

Three signals indicate architectural health is degrading:

**Coupling growth.** Is module-to-module coupling — the number of inter-module
dependencies, the tightness of those dependencies, or the frequency with which
they change together — increasing across releases? Coupling growth is not always
problematic, but uncontrolled coupling growth is: it indicates the system's
module boundaries are eroding, which increases the blast radius of future
changes and the difficulty of targeted verification.

**Boundary stability.** Are module boundaries changing frequently? Boundaries
that are stable are well-defined; boundaries that shift in every loop iteration
indicate specification drift, inadequate domain boundary enforcement (P3), or
architectural decisions that were not durable. Boundary instability is a signal
to review the domain model, not to apply more patches.

**Change amplification.** Does a change to one component require changes to
multiple other components? Change amplification greater than 1:1 consistently
indicates that the module decomposition is incorrect for the change patterns the
system actually experiences. The correct response is refactoring, not
acceptance.

These signals should be captured as part of the quarterly architectural health
review (see below) using static analysis tools appropriate to the system's
technology stack. The exact thresholds for "concerning" vary by system size and
complexity; the right approach is to establish the baseline at deployment and
treat sustained deterioration from that baseline as a governance trigger.

The long-horizon maintenance risk these signals are intended to surface is
documented empirically in Chen et al., *SWE-CI: Evaluating Agent Capabilities
in Maintaining Codebases via Continuous Integration* (2026,
https://arxiv.org/abs/2603.03823): on a benchmark spanning ~233 days and ~71
consecutive commits per repository, agents introduced behavioral regressions
in the majority of CI iterations. Treat this as a calibration point, not a
universal regression-rate law: SWE-CI measures behavioral regressions on a
specific benchmark, not the architectural-debt signals above, and the two are
distinct. The behavioral regression risk justifies regression-suite breadth at
each refactoring step; the architectural-health signals justify the
refactoring trigger itself.

### Debt Governance Process

On a quarterly cadence for active systems, review architectural health metrics.
If deteriorating, trigger a refactoring specification. The refactoring
specification enters the loop — Specify (what structural problem is being
addressed, what architectural properties the refactoring must restore), Execute,
Verify, Govern — not as a manual intervention that bypasses governance.
Refactoring outside the loop produces undocumented changes to agent-generated
code, creates divergence between the specification and the running system, and
invalidates the evidence bundle.

The refactoring specification's acceptance criteria must include two conditions
that cannot be relaxed: architectural health metrics must return to baseline
(the refactoring must actually solve the structural problem it was specified to
solve), and no functional behaviour changes (the regression evaluation suite
must pass at 100%, confirming that the refactoring did not alter observable
behaviour). A refactoring that improves architecture at the cost of functional
regression is not a successful refactoring — it is a new bug combined with
structural improvement.

For systems with low change frequency and stable environments, the quarterly
cadence may be extended to biannual, with the steward's documented
justification. For systems with high change frequency or significant complexity,
quarterly may not be frequent enough: monitor the architectural health signals
continuously and trigger a review when any signal shows sustained deterioration,
not just on the scheduled cadence.

### Technical Debt Triage

Not all technical debt warrants immediate remediation. Classify accumulated debt
by its operational impact:

**Blocking debt.** Debt that is actively preventing changes that the system's
stakeholders need to make. Blocking debt has an immediate cost measured in
slowed delivery and increased blast radius for routine changes. Remediate within
the current quarter.

**Risk debt.** Debt that is not yet blocking but is increasing the blast radius
of future changes, degrading security posture, or creating conditions for a
future incident. Remediate within a policy-set 1–2 quarters, prioritised by the steward
against other maintenance obligations.

**Cosmetic debt.** Debt that increases the cognitive overhead of working with
the system but does not materially affect reliability, security, or change
velocity. Remediate opportunistically during scheduled maintenance loops.

A debt triage record should be maintained and updated at each quarterly
architectural health review. The steward is accountable for the accuracy of this
record.

---

## Deprecation and Decommission

Every system has an end of life. Managing that end deliberately, with adequate
notice and a controlled wind-down, is materially better for the system's users,
consumers, and the organisation's governance record than allowing a system to
lapse into unmaintained operation until it fails. Define the deprecation and
decommission lifecycle in five stages, and apply this structure to every system
managed under the ASDLC.

### Stage 1: Deprecation Decision

The deprecation decision is triggered when one or more of the following
conditions is met:

The success criterion from Layer 1 is no longer achievable — the system cannot
deliver the business outcome it was built for, because the context has changed,
the underlying need has shifted, or the system's performance has degraded below
the acceptable threshold and cannot be cost-effectively restored.

The business need has changed — the organisation no longer has the use case the
system was built to serve, or serves it more effectively through a different
mechanism.

The maintenance cost exceeds the value delivered — the ongoing cost of security
patching, architectural health maintenance, and operational support exceeds the
value the system produces when assessed against its current success criterion
performance. This is a quantitative test: cost and value must both be measured,
not estimated.

A replacement exists and has been validated — a new system has been verified,
released, and is delivering the same or greater value at lower total cost. The
existence of a replacement does not trigger deprecation automatically; the
replacement must be validated as adequate before the original system is
deprecated.

The deprecation decision is owned jointly by the system steward and the business
demand sponsor who validated the original need. The steward brings the technical
and operational cost picture; the demand sponsor brings the business value and
strategic alignment picture. The decision requires documented evidence that at
least one trigger condition has been met — it is not a judgment call without
evidence.

### Stage 2: Deprecation Notice

Once the deprecation decision is made, a deprecation notice is issued to all
users and consumers of the system. The notice includes: the reason for
deprecation (which trigger condition was met and what evidence supports it), the
sunset date (the date the system will be taken offline), and the migration path
(what the consumers are expected to do before the sunset date — migrate to a
replacement system, adapt their integration, or accept that the capability will
no longer be available). Regulated systems may have minimum notice periods
defined by their regulatory framework or contractual obligations; confirm
applicable requirements before setting the sunset date.

The deprecation notice is the point at which the system's lifecycle becomes
externally visible. Issue it accurately and completely: an unclear migration
path or an unrealistic sunset date creates operational risk for consumers that
the organisation is responsible for.

### Stage 3: Wind-Down Period

During the wind-down period, the system remains fully operational. Its SLOs
remain in force. Its patch SLOs remain in force. The on-call and steward
assignments remain in force. There is no operational degradation during the
wind-down period: the decision to deprecate does not change the system's
obligations to its current users until the sunset date.

The steward monitors migration progress during the wind-down: what percentage of
consumers have migrated, whether the migration path is working as documented,
and whether the sunset date is still achievable given actual migration velocity.
If migration is significantly behind the pace required to reach full wind-down
by the sunset date, the steward escalates to the business demand sponsor and the
accountable human. The sunset date may be extended; the migration path may
require remediation; or consumers who cannot migrate may require support from
the organisation.

### Stage 4: Decommission

At the sunset date, the system is taken offline. The operational artefacts —
runbook, on-call assignment, monitoring dashboards — are archived. The system's
change record is closed.

Artefact retention at decommission must reconcile potentially conflicting
obligations. For US financial institutions, model documentation is retained
for a policy-set minimum of seven years after the model is retired, with no
instrument setting that period. SR 11-7 is supervisory guidance written in
"should", and it states no retention period at all: the words `retention`
and `seven years` each occur zero times in the guidance and its attachment
as held at `inputs/20260905-arnaud/prep/D-20-primary/sources/sr1107a1.txt`
(sha256 `d8ef343917…`). The seven years are this organisation's own choice
and must not be presented to a supervisor as an SR 11-7 requirement. GDPR
requires personal data to be deleted when no longer necessary for the
purpose it was collected for — which, at decommission, typically means data
processed by the system should be deleted or anonymised unless there is a
legal basis for retention. These obligations can conflict: a reasoning trace
that includes personal data from a GDPR-covered subject may simultaneously
need to be deleted (GDPR) and retained (the seven-year retention policy).
Reconcile these conflicts explicitly at decommission time, with qualified
legal and compliance input for regulated systems. Document the
reconciliation decision and retain the documentation.

The artefacts that must be retained (subject to the above reconciliation): the
specification at the time of final release, the evidence bundle from the final
release, the deployment record, and the maintenance governance record including
the deprecation decision and its evidence. These are the records that allow a
future audit to establish what the system did, why it was built, and why it was
retired.

### Stage 5: Post-Decommission Audit

Within a policy-set 30 days of decommission, the steward and the business
demand sponsor conduct a brief post-decommission audit. The questions are: Did
the system deliver the value it was built for, and what is the evidence? What
would have been done differently in the specification, development, or
maintenance phase? What failure modes, if any, were discovered in production
that were not anticipated at deployment? The output of this audit is a brief
document — not a lengthy retrospective — that is filed in the demand layer
(Layer 1) as a learning for future demand governance. Systems that delivered
their intended value under manageable maintenance cost are positive evidence
for similar specifications in the future. Systems that fell short of their
success criterion, accumulated unexpected maintenance cost, or encountered
failure modes that could have been anticipated at the specification stage are
inputs into how the organisation governs similar work in future.

This closes the ASDLC lifecycle loop: Layer 1 (demand) receives a learning from
Layer 4 (operations/maintenance) that improves the quality of future demand
governance. The learning should be documented in a form that future product
owners and demand sponsors can access when similar work enters the demand
backlog.

---

## License Compliance

Agent-generated code may introduce license-incompatible dependencies. The agent
selects dependencies based on what it knows and what was available in its
context; it does not perform a license compatibility analysis against the
organisation's production deployment context unless that constraint is
explicitly part of the specification.

### License Governance

**License constraint in the specification.** Before the loop runs for any
component destined for production, include an explicit license constraint in the
specification: which license families are permitted in this production context
(e.g., MIT, Apache 2.0, BSD), and which are forbidden (e.g., GPL v3 for
commercial production code, AGPL for code that will be deployed as a service).
The constraint must be specific enough for the agent to evaluate candidate
dependencies against it. "No copyleft licences" is a valid constraint; "use good
licences" is not.

**License compatibility report as a release gate.** Before production release,
generate a license compatibility report for the component and its full
dependency tree. The report must confirm that every dependency, at every level
of the dependency tree, has a license that is compatible with the production
context's constraints. The license compatibility report is a pre-release gate
condition: a component with a license-incompatible dependency in its dependency
tree does not satisfy the release conditions, regardless of its technical
verification status. Waivers are acceptable for known, documented exceptions —
for example, a GPL-licensed tool that is invoked as a process rather than linked
— but waivers must be reviewed and approved by legal or compliance, documented,
and filed with the release artefact.

**Ongoing license monitoring.** A dependency's license can change between
versions. A library that was MIT-licensed on the version the system was built
with may adopt a GPL or SSPL licence on a major version update. Dependency
vulnerability scanning (see Security Patch Management) should include license
change detection: when a dependency update changes the license, flag it for
steward review before the update is applied. Applying a dependency update that
changes the license without review is a license compliance gap.

Ongoing license monitoring should be integrated with the SBOM maintenance
process: the SBOM records the license for each dependency at a point in time,
and license change detection compares the current license against the SBOM's
recorded value at each scan.

---

## L4→L2 Learning Mechanism

The ASDLC flowchart shows a dashed arrow from Layer 4 (Operations & Maintenance)
back to Layer 2 (Engineering Execution). This section operationalises that
arrow. The arrow is not a metaphor for "lessons are learned". It is a governed
feedback path: production signals enter Layer 2 as structured inputs, and the
loop closes only when the specification, evidence bundle, and gate record have
been updated to reflect the learning.

### Artefact Types That Carry L4 Signals

Production signals reach Layer 2 through five artefact types. Each has a defined
owner and a defined destination.

**Incident retrospective record.** Produced after every P1 or P2 incident, or
any incident that triggers an RCA under the Vulnerability Disclosure and
Response section. The retrospective documents the failure mode, the detection
path, the contributing conditions, and the gap in specification, evaluation, or
gate condition that allowed the incident to occur or go undetected. The incident
retrospective record is the primary carrier of operational learning back to the
engineering layer.

**Model performance degradation report.** Produced when the system's performance
against its Layer 1 success criterion degrades below a defined threshold, or
when drift detection indicates that input distribution has moved materially
beyond the deployment baseline. The report documents the degradation trend, the
drift magnitude, and the specification assumptions that the degradation calls
into question.

**Drift detection alert.** A structured alert produced by the monitoring
infrastructure when a monitored signal — input distribution, output quality
metric, latency profile, or dependency health metric — crosses a defined
threshold. The alert is not a learning artefact by itself; it becomes one when
the steward produces a written assessment of what the drift implies for the
specification and whether re-verification is required.

**Dependency health signal.** Produced by the dependency monitoring process (see
Vendor and External Dependency Management) when a dependency reaches a
governance trigger: a deprecation notice, an API behaviour change, a license
change, or an SLA revision. The signal documents the change and the steward's
assessment of its impact on the specification's assumptions about the
dependency.

**Governance pattern report.** Produced periodically — at minimum annually, or
after any governance tier change — by the steward or portfolio steward. The
report identifies recurring patterns in the system's governance record: which
gate conditions are consistently waived, which evaluation suite areas are
consistently borderline, which specification sections are updated most
frequently, and what those patterns suggest about the original specification's
adequacy.

### Translation Ownership

The system steward owns the translation from operational signal to engineering
input. This is not a collective team responsibility. The steward receives the
artefact, assesses whether it crosses the threshold for Layer 2 entry (see
below), and if so, produces a Layer 2 demand item in the format required by
[Demand & Value](demand/value.md). The steward documents the chain from the
operational signal to the demand item: which artefact triggered the item, what
the signal said, and what the steward assessed as the engineering implication.
The translation record is retained alongside the demand item.

Where the steward is uncertain whether a signal's implications are within their
specification expertise — for example, a model performance degradation that may
require re-grounding of the foundation model's fine-tuning rather than a
specification update — the steward may involve the original engineering lead as
an assessment resource. The engineering lead's assessment is input; the
steward's translation decision is the governance act.

### What "Loop Closed" Means

A production signal's feedback loop is closed when all three of the following
conditions are satisfied:

**The specification has been updated.** The specification section whose
assumption the signal invalidated has been revised to reflect the learning. This
is not a comment or annotation — it is a substantive update to the specification
text, going through the Specify → Verify → Govern path, not applied as a
documentation edit.

**The evidence bundle reflects the learning.** The evidence bundle for the next
loop iteration includes an explicit reference to the production signal and
documents how the new specification addresses the condition that the signal
identified. A loop iteration whose evidence bundle does not acknowledge the
prior production signal has not completed the feedback path.

**The gate record acknowledges the production history.** The gate record for the
next release includes a section on production learning: what signals arrived
since the last release, what specification updates those signals produced, and
what evaluation suite additions or modifications address the conditions those
signals exposed. A gate record that treats the next release as if the production
signal history does not exist has not closed the loop.

### Threshold for Layer 1 Entry

Not every production signal warrants a specification update. Some signals are
handled at Layer 4 as maintenance actions without requiring a new demand item.
The threshold for Layer 1 entry is defined by three criteria, any one of which
is sufficient:

**Severity threshold.** Any P1 or P2 incident that reveals a gap in the
specification, evaluation suite, or gate conditions must enter Layer 1 as a
demand item. Handling a P1 or P2 incident with a hotfix that does not update the
specification, evidence bundle, and gate record is not loop closure — it is
technical debt against the governance record.

**Governance tier change.** Any event that causes the system's governance tier
to be lowered — a change in the risk profile, a regulatory reclassification, a
material change in the system's autonomy scope — must enter Layer 1. A tier
change means the original specification was written for a different risk
context; the specification must be updated to reflect the current context.

**Recurring pattern threshold.** Any failure mode, degradation pattern, or
governance gap that appears across three or more incidents or quarterly
architectural health reviews — even if each individual event was below the P1/P2
threshold — must enter Layer 1. A recurring pattern that is handled as
maintenance-only across multiple occurrences is a specification gap, not an
operational anomaly. The pattern recognition responsibility belongs to the
steward; the governance pattern report (see Artefact Types above) is the
instrument for surfacing recurring patterns before they compound into a P1
event.

When a signal meets the Layer 1 entry threshold, the steward creates a demand
item within a policy-set five business days of the signal being received. The
demand item references the triggering artefact and documents the steward's
assessment of the engineering scope. Layer 1 then governs the prioritisation of
the demand item alongside other demand — the steward does not unilaterally
determine when the engineering work begins, but they are responsible for
ensuring the demand item enters the queue.

---

## Learning Closure: From Process Change to Agent Behavior Change

The L4→L2 learning mechanism produces process change documents: updated
specifications, revised gate conditions, evaluation suite additions. These are
necessary outputs. They are not sufficient. A new checklist item in a process
document does not change what an executing agent will do next time it runs the
loop. Process documents govern human reviewers and the loop's gate conditions.
They do not change the agent's generative behavior.

Agent behavior changes when: the agent's evaluation suite changes (which drives
prompting or fine-tuning changes), the agent's system prompt is updated to
reflect the new behavioral guidance, or the agent is retrained. The translation
from "process should be updated" to "agent behavior should change" requires a
governed learning closure step. Without it, an organisation can maintain a
perfect process governance record while operating agents whose generative
behavior is unchanged by any of the learning the process has accumulated.

### The Three Learning Closure Pathways

**Pathway 1: Prompt update** (fastest, least durable). For learning that can be
expressed as an explicit behavioral instruction: update the agent's system
prompt to reflect the new behavior pattern. File the prompt change as a governed
change to the Prompt node in the governance graph. Run a targeted evaluation to
confirm the prompt change produces the desired behavior on the relevant input
class and does not regress existing behavior. Validity: prompt updates are fast
but fragile. They can be overridden by conflicting context and may not
generalise to novel input variations. Use this pathway for well-bounded, stable
behavioral instructions; do not use it as the default pathway for all learning
on the grounds that it is fast.

**Pathway 2: Evaluation suite update** (medium durability). For learning that
reveals a gap in what the agent is tested against: add new evaluation cases
covering the failure class. The evaluation suite update is the primary learning
artefact — it encodes what "correct behavior" means for this input class in a
machine-verifiable form. Combine with a prompt update if the agent's current
behavior on these cases is below threshold. The evaluation suite update must be
reviewed and approved by the accountable human before it takes effect as a gate
condition. A proposed evaluation case that has not passed this review is not a
gate condition; it is a draft.

**Pathway 3: Training corpus contribution** (most durable, highest cost). For
learning that is fundamental enough to warrant inclusion in future model
fine-tuning: document the case as a structured training example (input, correct
output, rationale) and add it to the organisation's governed training corpus.
See "The ASDLC Record Set as a Governed Training Corpus" section below. This
pathway is not triggered by every incident; it is triggered by incidents that
reveal a systematic behavioral gap that evaluation-and-prompting alone cannot
reliably correct.

### Learning Closure Requirements

All three pathways require:

**A learning closure record.** The record documents: which incident or feedback
signal triggered the learning; which pathway was chosen and why; what specific
change was made (prompt delta, evaluation case added, corpus entry filed); and
what evaluation evidence confirms the change is effective. The learning closure
record is filed as an EvidenceArtifact on the Incident or feedback signal node
in the governance graph.

**Evaluation confirmation.** A learning closure is not complete when the process
document is updated. A learning closure is complete when the evaluation suite
confirms that the failure class is now caught. An incident whose root cause
analysis produced a process change but no evaluation evidence of behavioral
correction has a closed RCA and an open learning closure. The steward tracks
these separately.

**Non-regression.** Every pathway requires a non-regression check: the change
that corrects the identified failure class must not introduce regression on the
evaluation cases covering adjacent behavior. Non-regression is part of the
evidence requirement for the learning closure record, not a separate optional
step.

---

## Cross-System Lateral Learning

When a production incident in System A reveals a failure class that is also
present in Systems B and C — same architecture class, same dependency set, same
autonomy tier — the learning should propagate laterally to B and C without
waiting for them to experience the same incident. The default outcome without a
defined lateral learning process is that each system waits for its own incident.
This is preventable harm.

### Lateral Learning Process

**Pattern detection.** After each incident's root cause analysis is finalised,
the governance agent performs a graph query: which other deployed systems in the
portfolio share the same architecture class, dependency set, and autonomy tier
as the affected system? This query produces a candidate propagation list. The
query is automated; its output is structured for steward review, not for
automated action.

**Propagation assessment.** The incident's accountable human reviews the
candidate list and determines which systems are genuinely analogous — the same
failure mode is credibly present — versus superficially similar — same
technology class but different operational context, different input
distribution, or different constraint set. The accountable human classifies each
candidate as: propagate, investigate further, or not applicable. This
classification is documented and filed as part of the incident's governance
record.

**Propagation execution.** For systems classified as "propagate," the evaluation
suite update from the learning closure mechanism is proposed to each system's
steward. The steward reviews the proposed update and approves it, modifies it
for their system's context, or rejects it with documented rationale. The
propagation is not automatic — each steward makes a system-specific
determination. A steward who approves the proposed evaluation case without
reviewing it against their system's context has not made a steward
determination; they have accepted an external change without governance.

**Propagation record.** A propagation record is filed as an EvidenceArtifact
linking the originating incident to each receiving system's evaluation suite
update. This makes lateral learning traceable: a future incident investigation
can determine whether the learning from a past incident was propagated, whether
the propagation was accepted or rejected, and whether the propagation proved
effective.

### Lateral Learning SLOs

The cross-system lateral learning loop has defined service level objectives:

- The candidate propagation query must be completed within a policy-set 10 business days of an incident's root cause analysis being finalised.
- Stewards of candidate systems must be notified of the propagation assessment within a policy-set 5 business days of the assessment being completed.
- Each steward's approval, modification, or rejection of the proposed update must be recorded within a policy-set 20 business days of notification.

A propagation assessment not completed within its SLO is a governance staleness
event. The portfolio steward is notified.

---

## Regulatory Co-Evolution Maintenance

For deployed systems with regulatory-derived constraints, the maintenance layer
must detect when the regulatory source underlying a constraint has evolved and
assess whether the constraint still accurately reflects the current regulatory
requirement. A constraint that was accurate at deployment but references a
superseded regulation is not a valid compliance control — it is a document that
creates the appearance of compliance without the substance.

### Regulatory Source Monitoring

The maintenance governance record for each system must list the regulatory
sources — document identifier, article or section, version, and effective date —
that underpin each regulatory constraint on that system. This listing is
maintained by the steward and updated at each quarterly operational DoD review.

The regulatory intelligence function (Layer 0 demand intelligence) monitors
listed regulatory sources and pushes a notification to the relevant system
stewards when any listed source is updated, proposed for revision, or
superseded. The monitoring obligation is at the portfolio level; per-system
stewards are consumers of this signal, not its producers.

### Impact Assessment

Within a policy-set 10 business days of receiving a regulatory source
notification, the system steward and the compliance function assess: does the
update change the interpretation of the current constraint? Does it create a
new obligation not currently reflected in the constraint set? Does it relax an
existing obligation in a way that may allow the constraint to be narrowed? The
assessment is documented in full and filed as an EvidenceArtifact on the
relevant Constraint node in the governance graph.

### Maintenance Action Classification

Based on the impact assessment, one of three actions is taken:

**Constraint confirmed current.** The regulatory update does not change the
constraint's validity. No change to the constraint is required. Update the
regulatory source version and effective date in the constraint record to reflect
the current source. File the assessment as evidence that the constraint was
reviewed following the update.

**Constraint requires update.** The regulatory update changes the meaning or
scope of the constraint. Enter the L4→L2 maintenance feedback path to update the
specification section governing this constraint and re-run the affected
evaluations. The constraint update follows the full Specify → Verify → Govern
path; it is not applied as a documentation edit outside the loop.

**New obligation identified.** The regulatory update creates an obligation not
currently covered by any constraint. Create a Layer 0 draft demand item for the
compliance function to validate and promote. The draft demand item documents the
regulatory source, the article creating the obligation, the compliance
function's initial interpretation, and the system scope to which the obligation
applies.

### Regulatory Co-Evolution Escalation

A regulatory source notification that has not received a completed impact
assessment within that policy-set 10 business days is a governance staleness
event. The governance portfolio owner is notified. A regulatory source
notification on a high-blast-radius system that remains unassessed beyond the
SLO window is an immediate governance concern requiring escalation to the
accountable human. Regulatory co-evolution that is not tracked is not a
compliance posture — it is an accumulating compliance gap whose existence the
organisation cannot document.

---

## The ASDLC Record Set as a Governed Training Corpus

The ASDLC's governance record — every loop iteration, gate decision, incident
analysis, value realization record, and feedback loop closure — is high-quality
structured data about what governed delivery looks like in this organisation's
specific context. No external training dataset can replicate it: it reflects the
organisation's specific regulatory environment, architecture patterns, risk
tolerance, and quality standards.

This data is a training asset. An organisation that has operated the ASDLC for
two years has structured examples of: specifications that led to clean gate
passes versus gate failures, evaluation portfolios that caught versus missed
production incidents, blast radius assessments that proved accurate versus
underestimated, value delivery that met versus missed success criteria. These
examples, properly structured, can train future governance agents to be
calibrated to the organisation's specific patterns. Organisations that treat
their ASDLC record set as an infrastructure archive and not as a governed asset
are leaving its highest-value use unrealised.

### Corpus Stewardship

The training corpus is a governed system with its own named steward and its own
lifecycle governance. The corpus steward is distinct from the governance
infrastructure steward: the governance infrastructure steward is accountable for
the tooling; the corpus steward is accountable for the quality, completeness,
and appropriate use of the training asset. The corpus steward role may be held
by the same individual for organisations where portfolio scale does not support
a dedicated function, but the accountability is explicitly assigned and
documented.

### Inclusion Criteria

Not all records are included in the training corpus. A record is eligible for
inclusion when three conditions are met: the outcome is known (there is a
verified determination of whether the gate decision was correct, whether the
incident analysis was accurate, whether the blast radius assessment proved
accurate at production); the record is complete (all linked artefacts referenced
in the governance graph are present and resolvable); and the record reflects a
decision that a future governance agent should learn from. Eligible decision
types include: a correct gate pass, a correctly identified gate failure, a
well-executed learning closure, a lateral propagation that proved effective, and
a detected false positive from a governance agent that was correctly overridden
by the accountable human.

### Exclusion Policy

Records from periods where governance quality was demonstrably low — periods
with elevated GQS degradation, documented rubber-stamping events, or governance
infrastructure integrity failures — are excluded from the training corpus or
labeled as negative examples with explicit annotation. Including poor governance
in training produces governance agents that learn poor governance. The corpus
steward maintains a governance quality map of the record set and applies
exclusion or labeling based on it. The exclusion policy is documented and its
application is auditable.

### Privacy and Confidentiality Review

Training corpus entries must be reviewed for sensitive content before inclusion:
personal data, proprietary technical specifics, security-relevant configuration
details, and commercially sensitive values. Sensitive content is redacted at the
structural level, not the content level. The structure of the decision — the
decision type, the evidence categories present, the gate outcome, the learning
pathway chosen — is the training value. The specific values of sensitive fields
are replaced with synthetic equivalents that preserve structural fidelity
without exposing the underlying content. A redacted corpus entry must be
reviewed by the corpus steward for structural integrity before inclusion.

### Version and Provenance

Each corpus entry records the governance agent versions and foundation model
versions active at the time the record was produced. This allows training
examples to be filtered by technology generation: examples produced under a
significantly older model generation may encode behavioral patterns that are no
longer representative of current agent capabilities or current governance
infrastructure behaviour.

### Usage and Sharing

The training corpus is made available to authorised model training functions
within the organisation. Access is governed by the corpus steward. The training
corpus is not shared externally — with model providers, research partners, or
other organisations — without an explicit per-entry review for confidentiality
and competitive sensitivity conducted by the corpus steward and approved by the
governance portfolio owner. Bulk transfer of the corpus to an external party
without per-entry review is not permitted under any circumstance.

---

## Meta-Governance of Governance Infrastructure

The governance infrastructure — the governance graph, the control evaluation
pipeline, the waiver management system, the gate tooling, and the operational
DoD monitoring system — is itself a system. It has dependencies, failure modes,
and a maintenance surface. It is subject to the same degradation pressures as
any production system. This section specifies how the governance infrastructure
is governed as a production system in its own right.

### Governance Infrastructure Has a Named Steward

The governance infrastructure has a named system steward, distinct from the
stewards of the systems it governs. This role — the governance infrastructure
steward — is accountable for the health of the governance tooling across the
full portfolio of governed systems. The governance infrastructure steward is not
accountable for the governance decisions made using the tooling; those remain
with the per-system stewards and accountable humans. The governance
infrastructure steward is accountable for the tooling's availability, accuracy,
and integrity.

Where the organisation's scale does not support a dedicated governance
infrastructure steward, the role is formally assigned to a named individual who
holds it alongside other responsibilities. The assignment is documented. An
organisation where the governance infrastructure has no named steward has a
governance gap — the infrastructure can degrade without a defined escalation
path.

### Changes to Governance Tooling Require Evidence

Changes to the governance infrastructure — adding new controls, modifying
evaluation thresholds, changing gate conditions, revising the governance graph
schema, updating waiver management rules — are not administrative actions. They
are engineering changes to a production system and must be governed as such.

A change to a gate condition or control threshold requires: a specification of
the change and its rationale (why is this threshold changing?), evidence that
the change has been evaluated against the systems it governs (what gate passage
rates would have changed under the new threshold, applied retrospectively to
recent releases?), and a gate record for the change itself. The gate record must
be approved by the governance infrastructure steward and a second named reviewer
who is not the person proposing the change.

The rationale requirement is not satisfied by operational convenience. "This
threshold was causing too many gate failures" is not a rationale — it is a
symptom that either the threshold was miscalibrated at the outset (in which case
the rationale is the calibration error and the correction), or the systems being
governed are not meeting the governance standard (in which case the correct
response is engineering improvement, not threshold relaxation). A change
rationale that cannot be distinguished from threshold relaxation for convenience
does not satisfy the evidence requirement.

### Governance Infrastructure Degradation Is a Production Incident

Degradation of the governance infrastructure is treated as a production
incident, not a backlog item. The following conditions constitute governance
infrastructure degradation events and trigger the incident response path:

**Stale governance graph nodes.** A system node in the governance graph whose
last verification record is older than the applicable re-verification cadence
for its tier. A stale node means the governance graph no longer accurately
represents the system's verified state. This is a data integrity failure, not a
housekeeping gap.

**Broken control evaluations.** A control evaluation in the pipeline that is
producing errors, returning null results, or has not run within its scheduled
cadence. A broken control evaluation means the governance infrastructure is
silently failing to assess the condition it was designed to assess — which means
gate decisions made while the control evaluation was broken may have been made
on incomplete evidence.

**Expired governance graph edges.** A relationship in the governance graph — a
dependency edge, an accountability assignment, a waiver linkage — whose validity
period has expired without renewal. Expired edges mean the governance graph's
relational model is stale, which may cause control evaluations that traverse
those edges to produce incorrect assessments.

**Waiver management system inconsistencies.** Waivers that reference gate
conditions or system versions that no longer exist, or active waivers whose
review dates have passed without renewal. An inconsistent waiver record means it
is not possible to determine from the governance infrastructure alone whether a
current gate passage is clean or is operating under an undocumented exception.

Each of these conditions is reported to the governance infrastructure steward
and assigned an incident severity using the same severity model applied to
production systems. The incident is resolved when the degradation condition is
corrected and confirmed — not when a ticket is created.

### Governance Infrastructure Cannot Be Silently Degraded

The governance infrastructure cannot be modified to make gate passage easier
without the same accountability as the systems it governs. Silent degradation —
reducing a control's sensitivity, removing a gate condition, narrowing the scope
of an evaluation — without a documented rationale, an evidence record, and a
second reviewer is a governance integrity failure.

This applies in both directions: raising governance requirements without
evidence and review is equally subject to this constraint. The point is not that
governance infrastructure must never change — it is that changes require the
same accountability as the systems it governs.

The governance infrastructure steward is accountable for maintaining an audit
log of all changes to the governance infrastructure, including the rationale,
the evidence, and the second reviewer's approval. The audit log is retained
under the same retention obligations as the governance records of the systems
the infrastructure governs. An organisation whose governance infrastructure has
no audit log of its own changes cannot demonstrate that its gate decisions were
made under consistent, documented governance conditions — which undermines the
evidential value of those gate records for audit, regulatory review, or incident
investigation.

---

## Cross-References

This document is part of the ASDLC Layer 4 governance suite alongside
[Operations Governance](operations/governance.md) and
[Operational Definition of Done](operations/dod.md). The
[Manifesto Principles](https://github.com/arnaudgelas/agentic-engineering-manifesto/blob/main/manifesto/manifesto-principles.md) P12 (accountability), P3
(architecture as defence-in-depth), and P10 (containment) are most directly
expressed in maintenance governance. The long-term ownership and stewardship
model operationalises the P12 accountability principle across the system's
entire lifetime, not just at the deployment decision point. The
[Demand & Value](demand/value.md) layer receives the post-decommission audit
output and uses it to improve future demand governance. The L4→L2 learning
mechanism operationalises the Observe phase of the manifesto's learning loop
(P9), closing the feedback path from production into engineering demand. The
meta-governance section above operationalises P12 accountability applied to the
governance infrastructure itself.
