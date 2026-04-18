# Operations & Governance — ASDLC Layer 4

*The operational governance layer of the Agentic Software Delivery Lifecycle.*

See the [Manifesto](../manifesto.md) for the engineering execution layer (Layer 2).
See [Release Governance](release-governance.md) for the Layer 3 release layer.
See [Maintenance Governance](maintenance-governance.md) for the long-term stewardship layer.
See [Operational Definition of Done](operations-dod.md) for the Layer 4 readiness conditions.

---

## What is the Operations & Maintenance Layer?

Layer 4 begins where Layer 3 ends — at production deployment. The release layer hands over an evidence-backed deployable and a named accountable human; the operational layer takes that handover and governs the system for the rest of its life: running it reliably, detecting and responding to incidents, maintaining it as the environment changes, and eventually retiring it in a controlled and documented manner. For agentic systems, operations carries specific challenges that traditional service operations does not face. The system's reasoning may not be fully visible at runtime. The code was generated, not hand-authored. The "developer who built this" is an agent. Incident escalation paths, rollback procedures, and post-incident investigations all require adaptations that standard service operations does not anticipate. This document defines those adaptations, tells operations engineers and SREs what must be in place before a system is considered operationally ready, and establishes the governance structures that keep a system governable across its entire operational lifetime.

---

## Operational Observability vs. Development Observability

The manifesto's Principle 9 is concerned with development-time observability: reasoning traces, decision chains, evaluation results, and the instrumentation that allows a team to understand why the system made the decisions it did during the engineering loop. That instrumentation is essential. It is also not operational observability.

Operational observability is production-runtime observability. Its instruments answer different questions: Is the system healthy? Is it meeting its service level objectives? Are users experiencing failures? Is inference cost within expected bounds? Are outputs meeting quality standards? The two disciplines are related — P9 traces are the audit trail for decisions; operational telemetry is the health monitor for behaviour — but they are not substitutes for each other, and the failure mode of treating them as substitutes is common and consequential. An organisation that implements P9 trace instrumentation and believes it has operational observability has not covered the production health dimension at all. It has instrumented the reasoning; it has not instrumented the service.

The following operational instruments are required in production in addition to whatever P9 development traces the system captures:

**Service health metrics.** Latency, error rate, and availability per component. These are the foundation of any service operations regime and apply to agentic systems without modification. Instrumented at the component level, not the system level: a degraded agent in a multi-agent system must be identifiable independently of overall system availability.

**SLO indicators.** The signals that determine whether service level objective budgets are within threshold. These are distinct from raw service health metrics: SLO indicators are computed signals (error budget burn rate, availability window compliance) that drive alerting and incident classification. See the SLO governance section below for what SLOs to define for agentic systems.

**Output quality rate.** The percentage of production outputs that meet acceptance criteria when sampled and assessed. This is distinct from availability and latency: a system can be fully available, responding within latency targets, with low error rates, and still be producing outputs that fail its quality criteria. Output quality rate is a production measurement of what the Verify phase assessed before deployment — it confirms that quality is maintained in the production environment across the full range of real inputs, not just the inputs in the evaluation suite. Define the sampling methodology and frequency at deployment; do not leave it undefined and assume quality is stable.

**Reasoning trace completeness.** The percentage of production decisions for which a complete, inspectable reasoning trace is retrievable. P9 mandates that traces exist; this metric confirms they are actually being captured and retained in production. For post-incident investigation to be possible, the trace must exist at the time of the incident — not just in development. For systems operating in regulated industries, reasoning trace completeness may be a compliance requirement independent of operational preference.

**Cost anomaly detection.** Alerts that fire when inference cost deviates materially from the established baseline. Cost anomalies are often the first observable signal of a system behaving abnormally: a runaway loop, a routing misconfiguration, a context expansion that inflates token consumption, or an unexpected increase in request volume. Cost monitoring is not a finance function; it is an operational health signal.

These five instruments are not a complete observability platform — they are the minimum floor below which a production agentic system is considered insufficiently observable for the operational DoD to be satisfied. See [Operational Definition of Done](operations-dod.md) for the full conditions.

Operational observability instrumentation should be implemented against vendor-neutral standards to ensure that observability data remains portable as tooling choices evolve. The OpenTelemetry (OTel) specification, maintained by the Cloud Native Computing Foundation, defines the vendor-neutral standard for traces, metrics, and logs and is the recommended instrumentation standard for the operational instruments described in this section. OTel-compatible instrumentation produces observability data that is exportable to any OTel-compatible backend, preventing lock-in to specific observability platforms and enabling the correlation of reasoning traces with service health metrics in a unified observability model.

### Agent-Assisted Monitoring

Governance agents operating in monitored execution mode may perform the following continuously, not just at scheduled review points.

**SLO burn rate trajectory analysis.** A governance agent may calculate the current error budget consumption rate and project the time to budget exhaustion under the current rate, surfacing trajectory warnings when the projected exhaustion falls within the current SLO window. This is a calculation, not a judgment: the agent produces a projection; the on-call engineer or SRE decides what corrective action, if any, to take. The projection is presented as a leading indicator, not as a remediation instruction.

**Alert correlation and deduplication.** When multiple alerts fire within a short window, a governance agent may correlate alerts by system, component, and timing — grouping related alerts and presenting a coherent incident picture to the on-call engineer rather than a flood of individual notifications. The agent groups alerts; it does not suppress them. All alerts are still recorded; the grouping is a presentation of likely correlation, not a filtering of signals. The on-call engineer retains full visibility into the individual alerts and may discard the agent's grouping hypothesis if the evidence does not support it.

**Incident timeline reconstruction.** During an active incident, a governance agent may assemble a chronological event timeline from available traces, logs, metric change events, and deployment records — presenting the assembled timeline to the incident commander as an input rather than as the authoritative account. The timeline must be clearly labeled as agent-generated. The incident commander verifies it against their own understanding of events and against the participant accounts gathered during the incident. The agent-generated timeline does not replace the human incident chronology in the post-incident review; it supplements the initial reconstruction effort and reduces the manual assembly burden during the acute phase.

**Runbook drift detection.** A governance agent may compare the current deployment configuration — model version, tool manifest, component versions, environment configuration — against the configuration described in the runbook, and flag discrepancies as runbook staleness indicators. The steward receives the drift report and determines whether the runbook needs updating or whether the configuration change falls within acceptable drift bounds. The agent identifies the discrepancy; the steward decides whether it constitutes a problem.

Governance agents performing these tasks operate within the bounds defined in [governance-agents.md](governance-agents.md). They do not make incident response decisions, suppress alerts, or update the runbook autonomously.

### AgentOps Telemetry

Standard service observability answers one set of questions: Is the system up? Is it fast? Is it returning errors? For most services, these three dimensions — availability, latency, error rate — constitute a reasonable operational health picture. For systems where agents are first-class runtime actors — not just code executors but active participants in ongoing production behaviour — this picture is incomplete in a materially significant way. A dashboard showing latency, error rate, and availability tells you that the system is up; it does not tell you what the agents inside the system are doing. An agent may be making expensive model calls, accumulating context past the intended boundary, invoking tools outside its expected scope, or producing outputs that silently degrade quality — all while the system-level health metrics remain green. AgentOps telemetry fills this gap.

AgentOps telemetry is the runtime observation of agent behaviour within a production system. It is distinct from P9 development-time reasoning traces, which record the agent's decision chain during the engineering loop. AgentOps telemetry is production-runtime instrumentation: the continuous capture of agent actions, resource consumption, permission interactions, and output quality signals as they occur in the live system. For systems using agents in production, the following dimensions must be instrumented and available in production dashboards:

- **Model calls:** each call to a foundation model API or locally deployed model, with model identifier and version, token count (prompt, completion, total), latency, and outcome (success, error, timeout).
- **Tool calls:** each tool invocation by an agent, with tool identifier, input summary (not full content, to avoid logging sensitive data), outcome, and latency. Tool calls that were denied (by policy or permission boundary) must be logged separately as permission denial events.
- **Permission denials:** any attempt by an agent to access a tool, resource, or capability outside its permitted scope, logged with the requesting agent's identifier, the denied resource, the policy that denied it, and a timestamp.
- **Memory reads and writes:** any access to or modification of the agent's persistent memory store, with operation type, memory segment identifier, and timestamp. For systems with P9 reasoning trace requirements, memory modification events must be included in the reasoning trace.
- **Retrieval corpus access:** any query to a retrieval system (vector store, knowledge base, document corpus), with query identifier (not query content), corpus version accessed, number of results returned, and timestamp.
- **Prompt version:** the version identifier of the system prompt or prompt template active during the model call. A prompt version change in production is a material configuration event.
- **Policy version:** the version identifier of the behavioural policy or safety policy active during the agent's operation. A policy version change in production is a material configuration event.
- **Autonomy escalation events:** any instance where the agent requested expanded scope, elevated permissions, or human approval for an action that exceeded its defined autonomy tier. The escalation request, the requesting agent's state, and the human decision (approved, denied, or unanswered) must all be logged.
- **Human override events:** any instance where a human operator overrode an agent's proposed action, halted an in-progress agent action, or invoked the system's kill switch. These events are significant governance signals and must be retained for post-incident review.
- **Failed tool use:** tool invocations that returned errors, timeouts, or malformed outputs. Failed tool use is a system health signal distinct from permission denials.
- **Cost anomaly signals:** inference cost events that deviate significantly from the established baseline per model call, per agent session, or per production period (as defined in finops-governance.md thresholds).
- **Quality anomaly signals:** agent output quality scores falling below the defined SLO threshold, as measured by the output quality sampling methodology.

AgentOps telemetry must be implemented against vendor-neutral standards to ensure that telemetry data is portable as tooling choices evolve and as the instrumentation community matures. OpenTelemetry (OTel), maintained by the Cloud Native Computing Foundation, is the recommended instrumentation standard for traces, metrics, and logs. The AgentOps dimensions listed above map to OTel span attributes and metric dimensions: model calls become spans with token count and latency attributes; tool calls become child spans of the model call span; permission denials become structured log events correlated to their parent span; escalation and override events become spans in the governance trace. This mapping enables the correlation of agent operational behaviour with service health metrics in a unified observability model, and prevents lock-in to specific observability platforms.

AgentOps telemetry is not optional for systems at Tier 2 and above. The action surface of a Tier 2 or Tier 3 system — its ability to take consequential actions in production, access external resources, invoke tools with real effects — makes agent behaviour a first-class operational concern, not a debugging convenience. A Tier 2 or Tier 3 system whose model calls and tool invocations are invisible in production dashboards is a system whose operational health cannot be assessed. For Tier 1 systems, model calls and tool calls are required minimums; the remaining dimensions are recommended and should be added as the system's operational maturity develops.

### Governance State Observability

AgentOps telemetry instruments what agents do at runtime. Governance state observability instruments whether the governance system is working. These are distinct. A system with perfect AgentOps telemetry — full model call traces, tool call logs, permission denial records — may have governance state that is completely dark: evidence bundles that have gone stale without detection, controls that failed weeks ago with no recorded resolution timeline, accountability owners who left the organisation without a replacement being named. Runtime observability and governance state observability require separate instrumentation.

The following five signals must be instrumented and visible in production dashboards for Tier 2 and above systems. For Tier 1 systems, these signals are recommended.

**Stale artefacts in active evidence bundles.** For each production deployment, the evidence bundle filed at the release gate has constituent artefacts with defined freshness windows. Any artefact that has passed its freshness window since the release gate assessment is stale. This signal must be surfaced continuously — not through a quarterly review — using the freshness rules defined in the Definition of Done. A stale threat model, a stale SBOM, a rollback test that has lapsed: each must be visible as a governance state alert without requiring a human to audit the evidence bundle manually.

**Controls in failed or waived state with no recorded resolution timeline or expiry.** Any control in the control state record that is in `fail` or `waived` status and has no recorded remediation timeline (for `fail`) or no recorded expiry date (for `waived`) is a governance state anomaly. It means the system is operating with an acknowledged governance gap and no plan to close it. This signal must be surfaced immediately when the gap is detected, not at the next scheduled review.

**Accountability ownership gaps.** Any active production component — a deployed system, a governance agent, a tool integration — that has no named current accountable human or steward is an ownership gap. Gaps arise when personnel change without triggering a reassignment. This signal requires comparing the HumanOwner nodes in the governance graph against the organisation's current personnel records. For regulated systems, an ownership gap is a compliance exposure. The signal must fire when a named owner's status changes in a way that affects their availability for their governance role.

**Rubber-stamping patterns.** Review-time distribution anomalies and approval-without-trace events at the release gate and specification readiness gate. A single fast review is not a signal; a pattern of anomalously short review times on complex evidence bundles is. This signal requires tracking review timestamps and bundle complexity metrics over time. The Runbook Drift Agent or an equivalent monitoring agent tracks this signal and surfaces patterns to the governance portfolio owner. The methodology for rubber-stamping detection is defined in adoption-metrics.md.

#### Rubber-Stamping Response: Autonomy Tier Adjustment

Detected rubber-stamping is not merely a reporting signal — it is a governance failure that degrades the assurance basis for the affected domain's autonomy tier. When review activity cannot be distinguished from approval activity, the evidence base that justified a given autonomy level is no longer being maintained. The correct operational response is tier adjustment: lowering the autonomy tier for the affected domain until governance quality is restored and re-demonstrated.

**Detection threshold.** A rubber-stamping pattern is confirmed when all three of the following conditions hold over a rolling 90-day window for a given domain or system:

1. The median approval time for gate submissions is shorter than the defined minimum plausible review time for evidence bundles of observed complexity — where minimum plausible review time is defined as the time required to open, navigate, and read the material evidence in the bundle at an informed reader's pace.
2. No gate submission in the window has a recorded challenge, clarifying question, conditional approval, or rejection from the approver.
3. At least 80% of gate submissions in the window share the same approver or approver chain.

A pattern that meets two of three conditions is a preliminary warning; all three conditions met is a confirmed rubber-stamping event requiring action.

**Authorization required to lower a tier.** Tier adjustment downward requires approval from the governance portfolio owner (one level above the system steward). It does not require the system steward's agreement — the steward's domain is the system; the portfolio owner's domain includes the governance quality of the steward's approval chain. The portfolio owner documents the tier reduction decision with: the detection evidence, the date of the rubber-stamping pattern confirmation, the new tier designation, and the conditions required for restoration.

**Governance record required.** A tier adjustment event must produce a governance record containing: the system identifier, the domain affected, the prior tier and new tier, the detection evidence summary (review time distribution, challenge rate, approver chain homogeneity), the authorising portfolio owner, the date of effect, and the restoration conditions. This record is appended to the system's governance graph node as an evidence edge and must be visible in governance state observability dashboards.

**Evidence required to restore the original tier.** Tier restoration is not automatic and cannot be self-certified by the domain's own approvers. Restoration requires:

1. A minimum 60-day observation window after the tier reduction, during which gate reviews in the affected domain demonstrate: review times consistent with genuine engagement, recorded challenges or questions on at least 30% of submissions, and approver chain diversity (no single approver handling more than 60% of submissions).
2. A restoration assessment conducted by the governance portfolio owner reviewing the 60-day evidence record.
3. A new governance record documenting the restoration decision, the evidence reviewed, and the portfolio owner's rationale.

A system operating at a reduced tier retains all production obligations of that lower tier — the reduction is not nominal. Capabilities and autonomy levels that depend on the prior tier are suspended until restoration is confirmed.

**Model, prompt, or tool manifest changes that have not triggered an evaluation re-run.** Any production deployment where the agentic provenance record from the current deployment differs from the previous deployment in model version, prompt hash, tool manifest, or retrieval corpus version — and no corresponding evaluation re-run is recorded in the evidence bundle — is a governance state gap. The evaluation validity does not transfer across configuration changes. This signal must be derived from comparing provenance records across deployments and checking for matching evaluation artefacts.

These five signals make the difference between a system that is governed and a system that appears governed. If none of these signals can be answered from instrumentation alone, the system's governance state is opaque between scheduled review events. For Tier 3 systems, governance state opaqueness is not an acceptable steady state — the operational risk of operating with undetected stale evidence or unmapped accountability gaps is too high.

### Governance Graph Queryability

The governance graph is a semantic, queryable model of governance state. Its nodes are artefacts, gates, agents, and humans; its edges are evidence links, accountability assignments, and waiver grants. A system that is operationally governed must exist as a node in the governance graph — and that node must be current, linked, and queryable. A system that cannot be located in the governance graph, or whose governance graph node has stale or missing edges, is not operationally governed regardless of what its dashboards report.

**Operational DoD condition:** The governance graph must be able to answer the question "is this system in a governed state right now?" for every system at Tier 2 and above. This condition is met when all of the following hold:

- The governance node for this system exists in the governance graph and was updated no later than the most recent release gate.
- All gate records (specification readiness gate, release gate, and any intermediate gate records) link to the system's governance node as evidence edges.
- The current system steward is assigned as an accountability edge on the governance node, pointing to a current personnel record.
- The governance graph node reflects the currently deployed version, not a prior release.

The governance graph queryability condition is checked as part of the quarterly steward review. It is also checked at every release gate: a release cannot advance to the operational layer if the governance graph cannot be updated with the new gate record. A system whose governance graph node is stale by more than one release cycle is in a governance gap state and must be raised to the governance portfolio owner for resolution.

This condition belongs to the "periodically reviewed (human steward required)" category defined in the Continuous vs. Event-Driven Governance section below, because confirming graph accuracy requires a human who can verify that named stewards and accountability assignments reflect organisational reality — a configuration check alone is insufficient.

---

## SLO/SLA Governance for Agentic Systems

Standard service level objectives — latency percentiles, error rate ceilings, availability targets — are necessary for agentic systems and should be defined using the same methodology as any other service. They are not sufficient. Agentic systems introduce epistemic uncertainty in their outputs: the system may be available, fast, and returning HTTP 200 while producing outputs that are incorrect, low-quality, or non-compliant. An SLO regime that covers only availability and latency is not governing the output quality dimension at all. The following SLOs must be defined in addition to the standard service level objectives, calibrated to the system's risk tier and regulatory context.

**Output quality rate SLO.** Define the minimum acceptable percentage of production outputs that must satisfy the acceptance criteria when sampled. Define the sampling methodology: how frequently samples are drawn, what sample size is required to be statistically meaningful for the system's output volume, how sampled outputs are evaluated (automated evaluation, human review, or a combination), and who is responsible for executing the sampling process. The output quality SLO is not satisfied by the pre-deployment evaluation suite — those evaluations cover the inputs the team anticipated. The production sampling methodology must cover the distribution of real inputs the system encounters, which will diverge from the evaluation suite over time.

**Reasoning trace completeness SLO.** Define the minimum acceptable percentage of production decisions that must have a complete, inspectable reasoning trace retained and retrievable. For most systems, this target should be 100% for Tier 3 decision classes (high-risk, production-impacting actions per the P12 accountability framework) and should be set proportionate to risk for lower-tier decisions. For regulated systems subject to model documentation requirements — SR 11-7, SS1/23, or equivalent — trace completeness may be a hard compliance floor, not a soft target. Confirm the regulatory requirement before setting the SLO value.

**Escalation response time SLO.** For systems that flag cases for human review — the Tier 2 and Tier 3 decision classes in the P12 accountability framework — define the maximum acceptable time from flagging to human response. This SLO governs the human-in-the-loop, not the agent. A system that correctly identifies a case requiring human review and flags it promptly has done its part; the escalation response SLO ensures the human side of that loop is governed with the same rigour as the agent side. Define separate targets for business hours and out-of-hours if the system operates continuously.

**Rollback success rate SLO.** For changes that require rollback, the percentage of rollback operations that complete successfully within the defined time-to-rollback window. This SLO is a check on the rollback procedure's reliability: a rollback procedure that has never been validated in production (only in representative environments at release time) may have a lower success rate than expected. Monitor rollback outcomes and use the data to improve rollback procedure quality.

These SLOs must be defined before deployment, not after incidents reveal their absence. They are part of the operational readiness gate. A system whose output quality SLO has not been defined is not operationally ready, regardless of how comprehensively it was verified before release. The readiness conditions are specified in [Operational Definition of Done](operations-dod.md).

### SLA Alignment

Where the system's SLOs are the basis for a service level agreement with a customer or internal consumer, the relationship between the two must be explicit. An SLO is an internal engineering target; an SLA is a contractual commitment. The SLO target should be stricter than the SLA floor to create a buffer: if the SLO is met, the SLA is not at risk. If the SLO is breached, the SLA is at risk but not yet broken. This buffer is the operational margin. Size it according to the system's variability and the cost of an SLA breach.

---

## Incident Management for Agentic Systems

Incident management for agentic systems follows the lifecycle defined in NIST SP 800-61 (Computer Security Incident Handling Guide): Preparation, Detection and Analysis, Containment, Eradication, and Recovery, followed by Post-Incident Activity. The three incident classifications defined in this section — Quality, Infrastructure/Application, and Security — represent different response paths within this lifecycle. All three share the same lifecycle phases; the classification determines the response procedure, escalation chain, and evidence preservation requirements within each phase. The NIST lifecycle applies in full to all three classifications.

Beyond this lifecycle, three characteristics of agentic systems require specific handling.

### Reasoning Traces May Not Be Production-Available

Development-time traces are stored in the loop's trace store during the engineering execution phase. Production-runtime reasoning may not be captured, may not be retained past a short window, or may be stored in a location that on-call engineers do not have access to during an incident. For post-incident investigation to be possible, the deployment must include a defined trace retention policy before the system goes to production. The retention policy must specify: which decisions produce a trace, how long traces are retained in production, what format they are retained in, and what the access path is during an incident. A retention policy that exists on paper but whose access path has never been exercised during a drill is not operational — it is documentation.

The failure mode: a production incident occurs, the on-call engineer determines that the agent produced a bad output, and there is no accessible trace. The investigation cannot proceed. The root cause cannot be determined. The specification and evaluation suite cannot be updated because the failure mode is unknown. This is a governance failure that was preventable at deployment time.

### Agent-Generated Code Has Implicit Dependencies

Hand-authored code is typically understood by its author. The author can be queried during an incident: why did you choose this approach? What edge cases did you consider? What does this depend on? Agent-generated code has no author to query. The specification, the evidence bundle, and the agent's reasoning traces during the Execute phase are the only records of why the code was written the way it was.

Runbooks for components built through the agentic loop must include: a link to the specification as it stood when the component was built, a link to the evidence bundle (evaluation reports, trace IDs, policy check outputs), the component's dependency manifest as generated at deploy time, and any known constraints or edge cases documented in the Learn phase of the loop. These are not nice-to-haves; they are the operational documentation for a component that has no human author available for escalation.

For agent-generated code, the dependency manifest is especially important. An agent may have chosen a library based on what was available in its training data or retrieval context at the time of execution. That choice may introduce dependencies that the team would not have chosen deliberately. The runbook must surface these dependencies so that when a dependency-related incident occurs, the on-call engineer can identify the dependency and its origin.

### The "Developer Who Wrote This" Is an Agent

Traditional escalation paths include the step "escalate to the author." For agentic systems, this step has no valid target: the agent that generated the code is not reachable, is not accountable, and may not be the same agent configuration that exists today. The escalation path for agent-generated systems must go to the accountable human who accepted production accountability at the release decision — the P12 accountability anchor from the release layer. That person accepted accountability for the evidence bundle and the deployment; they are the human point of escalation when the system behaves unexpectedly.

This does not mean the accountable human is available on-call at all times. It means the escalation path from on-call engineer to accountable human is defined, documented in the runbook, and the accountable human's availability expectations are known. The P12 accountability principle is not satisfied by naming a human at deployment and then treating that name as unreachable.

### Incident Classification

Standard incident classification covers infrastructure incidents (hardware failure, network outage, resource exhaustion) and application incidents (software bugs, configuration errors, dependency failures). For agentic systems, add a third classification: quality incidents. A quality incident is one where the system is available, responding within latency targets, and returning non-error responses, but its outputs fail the output quality SLO. Quality incidents are not captured by standard incident monitoring; they require the output quality sampling process to be running and generating alerts. A quality incident may be more harmful than an availability incident: a system that is down is visibly broken; a system that is producing low-quality outputs at scale may be causing damage before anyone notices.

Quality incidents require the same post-incident review as infrastructure and application incidents. The output of the review must include: identification of the input distribution or context change that caused quality degradation, an update to the specification or evaluation suite to cover the degraded cases, and re-verification before the fix is deployed. A quality incident that closes without a specification or evaluation update has not closed — it has been deferred.

**Security Incident classification.** A security incident is one where evidence exists or is suspected that the system's security properties have been violated: an adversarial input appears to have manipulated agent behaviour contrary to its specification (prompt injection), agent outputs appear to have been generated with access to data outside the agent's authorised scope, credentials or secrets appear to have been exposed in logs, outputs, or traces, a dependency appears to have been compromised at its source, or an agent has taken actions that exceed its authorised blast radius in ways consistent with adversarial intent rather than specification failure.

Security incidents require a response procedure distinct from operational incident response, because the goal of operational incident response — restore service as quickly as possible — can conflict with the goal of security incident response: preserve forensic evidence, contain the breach, and determine the full scope of compromise before remediation. Restoring service before the scope of a security incident is understood can destroy evidence and enable attacker persistence.

**Security incident response procedure:**

*Step 1 — Classification and isolation.* When indicators of a security incident are detected, the on-call engineer must classify the incident as a potential security incident before taking remediation actions. If classified as a security incident, the affected agent or system component is isolated from further production impact — not necessarily taken offline, but prevented from taking additional actions that could expand the scope of compromise or destroy evidence.

*Step 2 — Forensic preservation.* Before any modification of system state, reasoning traces, input logs, output logs, and configuration state are preserved in a tamper-evident store. This step must occur before the rollback procedure is executed: rolling back a system potentially overwrites the state that would have explained the incident. Where rollback is required for safety or availability reasons before forensic preservation is complete, the decision to prioritise rollback over forensic preservation requires explicit accountable human approval and must be documented.

*Step 3 — Legal and compliance escalation.* Within one hour of security incident classification, the security function (or security point of contact for the system) and the legal/compliance function must be notified. This escalation path must be documented in the runbook separately from the operational escalation chain — the on-call engineer and the P12 accountable human are not the appropriate final escalation points for a security incident.

*Step 4 — Breach notification obligation assessment.* In parallel with containment and forensic investigation, the legal/compliance function assesses whether the incident triggers regulatory breach notification obligations. This assessment must be completed within the shortest applicable notification window — which may be as short as 24 hours for early warning obligations under DORA or NIS2. The assessment cannot be deferred until the incident is fully resolved: notification obligations are time-bound from the moment of awareness, not from the moment of resolution.

*Step 5 — Post-incident investigation.* The security incident post-incident investigation follows forensic investigation principles: it must not be conflated with the operational post-mortem process, it must produce a finding on whether the incident was the result of a new attack class not covered by the threat model, and it must feed back into the specification's threat model and the evaluation portfolio with new adversarial test cases covering the attack class observed.

A security incident that closes without updating the threat model and evaluation portfolio has not closed — it has been deferred.

### Breach Notification Requirements

Several regulatory frameworks impose mandatory notification obligations when a security incident constitutes a personal data breach or a major operational incident. These obligations are time-bound from the moment of awareness — not from the moment of resolution or full investigation. They are not optional, and they cannot be satisfied post-hoc. The following obligations must be documented in the runbook as escalation triggers:

**GDPR Article 33 and 34.** Where the incident involves personal data processed under GDPR jurisdiction, the supervisory authority must be notified within 72 hours of the controller becoming aware of the breach (Article 33). Where the breach is likely to result in high risk to the rights and freedoms of natural persons, affected data subjects must be notified "without undue delay" (Article 34). The 72-hour clock starts at awareness, not at classification. If notification cannot be made within 72 hours, the reasons for the delay must accompany the notification.

**DORA Article 19.** For entities in scope of the Digital Operational Resilience Act, major ICT-related incidents must be reported to the competent authority. The reporting timeline comprises: an initial notification within the timeframe set by the competent authority after classification as a major incident; an intermediate report within 72 hours of the initial notification; and a final report within one month. DORA defines major incident in terms of criteria including number of clients affected, data losses, and duration of service disruption — confirm applicable thresholds with compliance counsel.

**NIS2 Directive.** For entities in scope of the NIS2 Directive (operators of essential services, digital service providers), a significant incident requires: an early warning to the competent authority within 24 hours of becoming aware; an incident notification within 72 hours; and a final report within one month.

These timelines vary by jurisdiction and framework. The applicable obligations depend on the system's data classification, the jurisdiction of operation, and the regulatory scope of the organisation. Confirm applicable obligations with qualified legal and compliance counsel before deploying any Tier 2 or Tier 3 system that processes personal data or provides essential services. The obligations must appear in the system's runbook as a notification checklist, not as a reference to this document — the on-call engineer must be able to initiate the notification process without navigating to governance documentation under time pressure.

### Post-Incident Review Structure

Post-incident reviews for agentic systems follow a blameless, structured format. The blameless principle means that the review assesses systems, processes, and conditions — not individual decisions made under pressure by people operating with incomplete information in a high-stress environment. Blameless reviews are more effective at identifying systemic improvements than blame-assigning reviews because they elicit honest accounts rather than defensive accounts.

The facilitator of the post-mortem must be a person who was not the incident commander — the person who managed the incident response should not also structure the retrospective. This separation ensures that the review can assess the response process itself, including decisions made by the incident commander, without self-protective filtering.

**Required sections:**

*Incident timeline.* A factual, chronological account of when events occurred, what was detected, what actions were taken, and what effects those actions had. The timeline is constructed from logs, traces, alert records, and participant accounts — it is not an interpretation, it is a reconstruction. Where accounts conflict, both accounts are recorded with the discrepancy noted.

*Contributing factors analysis.* The systemic, environmental, and process conditions that made the incident possible or made the response harder. Contributing factors are not root causes — complex incidents have multiple contributing factors, not a single root cause. The contributing factors analysis asks: what conditions existed that, if different, would have prevented the incident or reduced its impact? Typical contributing factors in agentic systems: threat model gap (an attack category not included in the threat model), evaluation portfolio gap (a failure class not covered by the evaluation suite), runbook gap (a failure mode not in the known failure modes section), escalation path gap (the chain was unclear under pressure), specification drift (the system's behaviour had diverged from its specification before the incident occurred).

*Impact statement.* What users, systems, data, or compliance obligations were affected. Quantified where possible: number of users affected, duration of degradation, number of outputs that failed quality criteria, any regulatory notification obligations triggered.

*Action items.* Each action item has: a specific description of the change to be made, a named owner, and a due date. Generic action items ("be more careful about input validation") are not acceptable — the action must specify what will change. The action items from a post-mortem are governance obligations, not suggestions.

*Specification and evaluation updates required.* For every post-mortem, identify which specification conditions or evaluation cases would have caught the failure before it reached production. The specification or evaluation update required is itself an action item — not a separate retrospective but a mandatory post-mortem output.

---

## On-Call Practices

On-call for agentic systems requires a specific briefing. The on-call engineer must know, for each system they are on-call for:

**The system's SLOs and the alerting structure.** What alerts fire, at what thresholds, and what initial triage steps each alert warrants. An on-call engineer who receives an alert they do not understand will escalate immediately, defeating the purpose of having on-call coverage for first-triage actions.

**The location of the specification and evidence bundle.** When diagnosing an unexpected behaviour, the on-call engineer's first reference is the specification — what was the system intended to do? The evidence bundle — what was it verified against? — is the second reference. If neither is findable within the first ten minutes of an incident, the runbook is incomplete.

**The rollback procedure, including tested time-to-rollback.** The on-call engineer must be able to execute the rollback procedure without assistance. The procedure must include the specific commands or interface steps required, the expected time to complete, and verification steps that confirm the rollback succeeded. A rollback procedure documented only at a high level is not executable under incident pressure.

**The escalation chain.** On-call engineer → accountable human → system steward. All three must be named with current contact information. The escalation chain for an agentic system must be explicit about what triggers escalation to the accountable human (not every P1 alert; specifically, alerts indicating quality incidents, reasoning trace gaps, or unexplained output behaviour) vs. what the on-call engineer handles independently.

**Known failure modes.** The Learn phase of the loop documents what was discovered during development. Incidents, near-misses, and edge cases observed during development must be captured in the runbook as known failure modes with diagnostic steps. An on-call engineer encountering a known failure mode for the first time — because it was never documented — is a runbook failure.

**Breach notification obligations.** For systems that process personal data or operate as essential services under applicable legislation, the on-call engineer must know the notification trigger criteria, the notification timelines, and the escalation path to the legal/compliance function — all within the runbook, not in external references. The first 24–72 hours of a security incident are the window in which regulatory notification obligations must be initiated. A runbook that does not contain this information leaves the on-call engineer without the ability to fulfil an obligation that cannot be delegated or deferred.

**DR drill outcomes.** DR procedures are not tested only at deployment — they are exercised on the defined cadence, and drill outcomes are treated as operational signals. A drill that reveals a recovery time significantly longer than the target, or a recovery gap not covered by the procedure, must produce a runbook update and, for significant gaps, a loop iteration to address the architectural issue. The on-call engineer must be familiar with the most recent drill outcome, including any open corrective actions, and must know whether any gap identified in the last drill remains unresolved.

### Accountable Human vs. On-Call Engineer

The P12 accountable human is the accountability anchor for the system. They are not necessarily the on-call engineer. Clarifying this relationship is important: the on-call engineer handles first-triage and routine operational response; the accountable human is involved in incidents that require a governance decision — accepting a known risk, approving a deviation from standard procedure, authorising an emergency production change outside the normal release cycle, or accepting responsibility for a quality incident's root cause. Define the boundary explicitly in the runbook. Ambiguity about who makes what decision during an incident is resolved by having decided in advance.

---

## Resilience Testing

Operational procedures documented in a runbook and tested in controlled pre-deployment environments reflect assumptions about how the system will fail. Production failure modes frequently differ from those assumptions: infrastructure behaves differently under real load, agent behaviour under degraded conditions diverges from staging behaviour, and escalation chains reveal gaps that tabletop exercises do not surface. Resilience testing — controlled, hypothesis-driven experiments that inject failures into production or production-equivalent environments — is the mechanism for discovering these gaps before incidents do.

**Chaos engineering principles.** Resilience experiments follow a structured hypothesis format: define the steady state (what normal behaviour looks like in measurable terms), hypothesise the impact of a specific failure condition, introduce the failure in a controlled scope (a single component, a fraction of traffic, a simulated dependency failure), observe whether the steady state is maintained or degraded, and document the finding. Each experiment produces either confirmation that the system handles the failure correctly or a gap requiring remediation. Neither outcome is failure — the experiment is working correctly in both cases.

**Game days.** A game day is a structured, facilitated exercise in which the team subjects the system to planned failure scenarios in a controlled environment and validates that runbook procedures, escalation paths, and recovery mechanisms function as documented. For Tier 2 systems, game days must be conducted annually. For Tier 3 systems, game days must be conducted at minimum biannually. A game day is not an ad-hoc incident simulation — it requires pre-planned scenarios drawn from the runbook's known failure modes, a facilitator separate from the on-call engineer, and a documented outcome report.

The minimum scenarios for an agentic system game day: agent output quality degradation without availability failure (validating that quality incident monitoring detects the failure); escalation chain execution under time pressure (validating that the escalation from on-call engineer to accountable human to system steward functions within defined timeframes); rollback procedure execution (confirming the tested time-to-rollback measured at the pre-deployment test still reflects production reality); and reasoning trace retrieval under incident conditions (confirming that the on-call engineer can access relevant traces within the first ten minutes of a simulated incident).

Game day outputs update the runbook's known failure modes section and identify any gaps in recovery procedures. A game day that produces no runbook updates and no identified gaps is either a sign of an exceptionally well-governed system or a sign that the scenarios were insufficiently challenging — distinguish between the two before accepting the outcome.

---

## Production Change Management

Changes deployed outside the normal release cycle — hotfixes, emergency patches, configuration changes, out-of-band security fixes — require a governance structure proportionate to their risk. The agentic loop's full evidence bundle and verification cycle may not be achievable under time pressure; the governance structure must define what is required at a minimum, what may be compressed, and what must be completed post-deployment.

### Risk-Tiered Minimum Loop

**Configuration-only change.** A change that modifies runtime configuration without altering code: environment variables, feature flags, routing weights, threshold values. Required: Specify phase (documenting what is being changed and why) and Verify phase (confirming the change has the intended effect and no unintended side effects, using the existing evaluation suite). A reduced evidence bundle is acceptable — the evaluation run against the changed configuration, plus documentation of what changed and the business justification. The Govern phase is required: the accountable human must approve the configuration change before it is applied. Rollback must be documented: how to revert the configuration change and what the expected effect of reversion is.

**Minimal code change.** An isolated, well-tested code change with a contained blast radius: a bug fix in a single component, a dependency version update, a security patch to a specific module. Required: Specify, Execute, and Verify phases. Evidence bundle required at reduced scope: the evaluation run against the patched code, the diff, and the dependency manifest if changed. Govern required: accountable human approval before deployment. A reduced evaluation suite that covers the affected component is acceptable if the change is demonstrably isolated; the runbook must document which evaluations were run and why the scope reduction was justified.

**Significant code change under time pressure.** A change that touches multiple components, alters system behaviour, or has a non-trivial blast radius, but must be deployed ahead of the normal release cycle. Required: full agentic loop at accelerated pace. No phase may be skipped; phases may be compressed. A compressed Verify phase with known-incomplete evaluation coverage is acceptable under time pressure if and only if the incompleteness is documented: which evaluations were not run, what risk that incompleteness represents, and who accepted that risk. Full verification against the complete evaluation suite is required within 48 hours of deployment.

### Post-Hoc Normalisation

Any change executed under emergency procedures must be treated as technically incomplete at the time of deployment. Within 24 hours of deployment: the full evidence bundle must be completed and filed, the abbreviated process must be documented with its justification, and the risk acceptance for any evaluation gaps must be recorded by the accountable human. Within 48 hours: full evaluation verification must be complete. If the full verification reveals issues, they are treated as a quality incident and handled accordingly — not silently accepted because the change is already in production.

Post-hoc normalisation is not a loophole. It is a structured acknowledgement that time pressure is a real operational constraint, combined with a firm commitment to close the governance gap within a defined window. A team that regularly deploys under emergency procedures without completing post-hoc normalisation is not using the emergency process legitimately — it is using emergency procedures to bypass governance permanently.

### Change Records

All production changes — whether through the normal release cycle or emergency procedures — must produce a change record. The change record for agentic system changes includes: the specification reference (what was the intent?), the evidence bundle reference (what was verified?), the accountable human's approval, the deployment identifier, and the rollback procedure reference. Change records are the operational audit trail. They are distinct from the engineering evidence bundle: the evidence bundle proves the change was built correctly; the change record proves the governance process was followed.

---

## Continuous vs. Event-Driven Governance

The operational DoD, as defined in [operations-dod.md](operations-dod.md), is currently verified at defined events: initial deployment and the quarterly steward review. These verification points are deliberate governance gates, not arbitrary schedule choices — they ensure that a named, accountable human has actively assessed the system's operational posture at regular intervals. With governance agents, however, certain operational DoD conditions can be verified continuously: not replacing the periodic review, but supplementing it with real-time state monitoring that surfaces condition failures between review cycles rather than only at them.

The following classification separates operational DoD conditions into two monitoring modes based on the nature of the check required.

**Continuously monitored (governance agent eligible).** The following conditions can be assessed by a deterministic check or calculation against observable system state, making them suitable for continuous monitoring by a governance agent:

- *Security scan recency:* the date of the most recent security scan measured against the defined scan frequency — a factual comparison that requires no judgment.
- *SLO configuration state:* whether dashboards are live, alerts are configured, and alert routing is directed to a monitored destination — a configuration presence check.
- *On-call assignment presence:* whether a named on-call engineer is recorded as current in the runbook — a data presence check.
- *Runbook modification date:* whether the runbook's last update date is more recent than the deployed version's release date — a timestamp comparison.
- *Certificate and credential expiry:* SBOM and dependency freshness against defined maximum age thresholds — an expiry date calculation.
- *Trace retention policy configuration state:* whether the trace retention policy is configured as defined at deployment — a configuration presence and value check.

A governance agent may monitor these conditions continuously and surface condition failures in real time, without waiting for the quarterly review. A condition failure surfaced by a continuous monitoring agent triggers an immediate notification to the steward, who must resolve or document the failure within the defined remediation SLO. The condition failure is recorded in the governance log regardless of how quickly it is resolved — prompt resolution does not erase the record that the condition was not met.

**Periodically reviewed (human steward required).** The following conditions require human judgment that continuous monitoring cannot substitute. They remain on the quarterly steward review cadence:

- *Specification currency:* whether the specification still accurately reflects the deployed system's behaviour — a judgment about whether observed production behaviour has diverged from the documented intent in ways that matter, which requires a human familiar with the system's domain context.
- *Steward knowledge depth:* whether the steward can pass the accountability test — an assessment that requires active interrogation of the steward's understanding, not a configuration check.
- *Value realisation monitoring:* whether the system is achieving its stated business outcome — a judgment about business context, user experience, and outcome measurement that involves interpretation, not just data retrieval.
- *Accountable human availability confirmation:* whether the named accountable human is reachable and their contact information and availability expectations remain current — a confirmation that requires human participation.

The distinction between these two categories is not about the importance of the condition — all operational DoD conditions are required, and a failure on any of them is a governance failure regardless of its classification. The distinction is about whether the condition can be assessed by a deterministic check or calculation versus whether it requires human judgment about evolving system behaviour and organisational context. Classifying a condition as governance-agent eligible does not reduce the condition's governance weight; it determines only whether real-time monitoring is technically feasible. The quarterly steward review covers all conditions in both categories: continuously monitored conditions appear in the review with their real-time history included.

---

## Tier 4 Operational Model

Tiers 1 through 3 share an operational assumption: the unit of governance accountability is the agent action. A human reviews, approves, or monitors individual actions or classes of actions. At Tier 4 — policy-envelope autonomous operation — this assumption changes. Agents execute within a human-approved, machine-enforced policy envelope. The accountability unit shifts from the individual action to the envelope design. This shift changes how operations governance works in every dimension: SLOs, audit trail obligations, steward accountability, incident response, and operational signals.

### SLOs Apply to the Policy Envelope's Outcomes, Not Individual Agent Actions

A Tier 4 system may execute thousands of agent actions per hour, none of which individually requires human review. Defining SLOs at the action level is neither feasible nor meaningful — the action volume defeats meaningful human assessment. Instead, SLOs for Tier 4 systems are defined at the outcome level: what the policy envelope is designed to produce, measured against what it actually produces.

A Tier 4 SLO regime must define: the outcome class the policy envelope governs, the quality and compliance criteria for outputs in that class, the measurement methodology (sampling, automated evaluation, downstream signal integration), and the envelope-level error budget. A Tier 4 system that meets its envelope-level outcome SLOs is performing as governed; a system whose outcome SLOs are breached has a policy envelope failure, not necessarily an individual agent failure.

This framing matters for incident classification: a Tier 4 SLO breach is an envelope review event, not an action-level rollback event. The response is to assess whether the envelope's constraints are still producing the intended outcome distribution, not to review the individual action that preceded the breach signal.

### Governance Audit Trail of Agent Actions as an Operational Artefact

The fact that individual agent actions do not require per-action human review does not remove the obligation to record them. The governance audit trail of agent actions in a Tier 4 system is an operational artefact — not a debugging convenience — and carries the following obligations:

**Retention.** The audit trail must be retained for a period consistent with the system's regulatory context and risk tier. For systems in regulated industries, this minimum is typically the longer of the system's operational lifetime or the applicable record retention period under the governing regulatory framework.

**Periodic review.** The audit trail must be reviewed on a defined schedule — not only when an incident occurs. The steward or a designated reviewer samples the trail periodically to confirm that agent actions remain consistent with the policy envelope's intent, that no novel action patterns have emerged that the envelope did not anticipate, and that the envelope's machine-enforcement layer is functioning as designed. The review frequency is a governance commitment, not a discretionary practice. Define it at deployment; include it in the quarterly steward review agenda.

**Accessibility during incidents.** The audit trail must be accessible within the incident response timeframe — if the trail cannot be retrieved within the first hour of a Tier 4 incident, it is not operationally available. Verify accessibility as part of game days and DR drills.

### The Steward is Accountable for the Envelope, Not Each Action

In Tiers 1–3, the P12 accountable human can be associated with individual action approvals or escalation decisions. In Tier 4, the P12 accountable human's primary accountability surface is the policy envelope design, its enforcement configuration, and its fitness for the operational context.

This means: the steward is accountable for whether the envelope was correctly designed to constrain the agents to the intended behaviour space; whether the envelope's enforcement layer was correctly implemented and is functioning as designed; whether the envelope remains appropriate as the operational context evolves; and whether the periodic audit trail review is being conducted as committed.

The steward is not individually accountable for each agent action the system takes within the envelope. They are accountable for the envelope that governs those actions. This is accountability at a higher level of abstraction — it is not less demanding than action-level accountability; it requires a deeper understanding of the system's operational context, the envelope's design assumptions, and the ways in which the envelope could fail to constrain behaviour as intended.

### Policy Envelope Drift as an Operational Signal

Policy envelope drift occurs when agents consistently operate near the boundaries of the policy envelope — approaching but not violating defined limits — over a sustained period. Drift is an operational signal, not an operational failure: it indicates that the envelope's boundary conditions are being regularly encountered and that the agent's operational pressures are pushing toward the envelope's edges.

Sustained envelope drift requires a steward review. The review determines one of three findings: the drift is expected given the operational context and the envelope is appropriately sized; the envelope needs adjustment because the operational context has changed and the boundaries are no longer correctly calibrated; or the agent's behaviour is diverging from specification in ways that explain why envelope boundaries are being approached.

**Drift detection.** AgentOps telemetry must include envelope boundary approach events — instances where an agent's proposed action was within a defined proximity threshold of a policy limit, even if not a violation. The threshold and telemetry definition are set at deployment. A rolling frequency of envelope boundary approach events, when it exceeds the defined threshold, triggers a steward review obligation. The steward must document the review finding and, if adjustment is warranted, initiate the envelope redesign through the appropriate loop iteration.

### Kill-Switch Operability as an SLO Condition

A kill switch that has never been exercised in production is not reliably operational — it is a documented capability whose production behaviour is unknown. For Tier 4 systems, kill-switch operability is an SLO condition, not a deployment checkbox.

**Testing schedule.** Kill-switch operability must be tested on a defined schedule established at deployment. For Tier 4 systems, the minimum testing frequency is quarterly. Testing must exercise the full kill-switch path: the invocation mechanism, the enforcement layer's response, the confirmation signal, and the audit trail entry that records the exercise. A test that terminates before the enforcement layer's response is confirmed is not a complete test.

**SLO definition.** The kill-switch SLO specifies: the maximum time from invocation to confirmed agent action cessation, the required confirmation signal format, and the expected audit trail entry. If a quarterly test produces a time-to-cessation that exceeds the SLO, it is a governance failure requiring immediate remediation — not a note in the next quarterly review. The kill-switch SLO failure triggers the same response as any other SLO breach: incident record, remediation commitment, and re-test before the system is considered operationally governed at Tier 4.

### Incident Response for Tier 4: Envelope First

For Tiers 1–3, incident response for behavioural anomalies begins with the agent action: what did the agent do, why did it do it, and what should it have done instead? For Tier 4, this sequence changes. The policy envelope is the first diagnostic, not the individual agent action.

When a Tier 4 system produces an unexpected outcome, the first questions in incident response are envelope questions: Did the agent's action fall within the policy envelope? If yes, the envelope produced an outcome it was designed to permit — the incident is an envelope design failure, not an agent compliance failure. If no, the agent violated the envelope — the incident is a machine-enforcement failure and potentially a more serious governance event.

**Envelope-first incident procedure:**

*Step 1 — Envelope compliance check.* Before investigating the individual agent action, determine whether the action that produced the incident outcome fell within the policy envelope as defined and as enforced. This check should be executable from the audit trail within the first fifteen minutes of incident classification.

*Step 2 — Branch based on compliance determination.* If within envelope: the investigation proceeds as an envelope design review — the envelope permitted a behaviour that produced an unacceptable outcome. The remediation path is envelope revision, not agent-level rollback. If outside envelope: the investigation proceeds as an enforcement layer failure — a constraint that should have prevented the action did not. The remediation path includes immediate enforcement layer assessment, potential system isolation pending remediation, and a review of whether other actions since the last enforcement layer validation also escaped constraint.

*Step 3 — Audit trail reconstruction.* Using the governance audit trail, reconstruct the sequence of agent actions leading to the incident outcome. For envelope-compliance cases, this reconstruction should reveal the pattern of boundary approach events that preceded the incident — drift that the operational signal monitoring should have surfaced. For enforcement failure cases, the reconstruction identifies when the enforcement gap first appeared.

*Step 4 — Post-incident findings.* A Tier 4 incident post-mortem must produce a finding on the envelope — whether it requires revision, whether its enforcement layer requires remediation, or whether it was appropriately designed and the incident represents a class of operational context not anticipated in the envelope design. A Tier 4 post-mortem that closes without an envelope assessment finding has not met the post-incident review standard for this operational model.

---

## Cross-References

This document is Layer 4, operational governance. It receives systems from [Release Governance](release-governance.md) (Layer 3) and hands off long-term stewardship responsibilities to [Maintenance Governance](maintenance-governance.md). The [Operational Definition of Done](operations-dod.md) defines the readiness conditions that a system must meet before the operational layer accepts it. The [Manifesto Principles](../manifesto-principles.md) P9 (observability), P12 (accountability), and P5 (autonomy tiers) are the engineering principles most directly expressed in operational governance; their minimum bars apply in production as in development.
