# Operational Definition of Done — ASDLC Layer 4

*What "operationally ready" means for a system in production.*

See the [Manifesto](../manifesto.md) for the engineering Definition of Done.
See [Operations Governance](operations-governance.md) for the operational runtime layer.
See [Maintenance Governance](maintenance-governance.md) for long-term stewardship.

---

## What is the Operational Definition of Done?

The operational DoD is the set of conditions that must be true for a system to be considered operationally ready. It governs the system, not a change. A system that passes the engineering DoD for every individual change — the manifesto's Definition of Done applied at the loop level — may still fail the operational DoD if runbooks are never updated, stewards are not reassigned when personnel change, or security scans lapse between releases. The operational DoD is the persistent governance state of the system in production. It is not a one-time gate applied at the first deployment and then forgotten. It is a condition that must be maintained throughout the system's operational lifetime. A steward who leaves without a qualified replacement puts the system into operational DoD failure even if no code changed. A security scan that was clean at deployment but has not run in 60 days may no longer reflect the system's actual security posture. The operational DoD names the conditions that must be true at any point in the system's lifetime for it to be considered in good governance standing.

---

## The Operational DoD Conditions

A system is operationally ready when ALL of the following conditions are true.

---

**Runbook complete.**

The runbook exists, is current, and covers: a service overview and architecture diagram accurate to the currently deployed version; the system's SLOs and the methodology for measuring them; alerting thresholds with documented rationale for each threshold value; known failure modes with diagnostic steps and resolution procedures (populated from the Learn phase of the most recent loop iterations and updated after each incident); the escalation chain from on-call engineer to accountable human to system steward, with current contact information for each; the rollback procedure with a documented tested time-to-rollback (not just the procedure, but evidence that it was tested in a representative environment within the last release cycle); links to the specification and evidence bundle for the currently deployed version; and the contact information and acknowledgment of availability for both the accountable human and the system steward.

A runbook that has not been updated since the previous release is not current. A runbook that documents the rollback procedure but does not include evidence of testing is not satisfying the rollback requirement — documentation of a procedure is not the same as a tested procedure. A runbook that names an escalation contact who has since left the organisation is outdated and does not satisfy the escalation chain requirement.

---

**Operational observability configured.**

Dashboards are live in production and cover: service health (latency, error rate, availability per component); SLO indicators (error budget burn rate and availability window compliance for each defined SLO); output quality rate (sampled assessment of production outputs against acceptance criteria, with the sampling methodology documented and operating on its defined schedule); and cost monitoring (inference cost against baseline, with cost anomaly alerts configured). For systems with P9 reasoning trace requirements, reasoning trace completeness monitoring is configured and the completeness percentage is visible in dashboards.

Alerts are configured and routed to the on-call engineer for: SLO burn rate alerts (firing when the error budget is burning at a rate that will exhaust the budget within the SLO window at the current rate); cost anomaly alerts (firing when inference cost deviates materially from the established baseline); and output quality alerts (firing when the sampled output quality rate falls below the defined SLO threshold). Alerts that are configured but routing to an unmonitored destination are not operational. Alerts that have never been tested to confirm they fire at the specified thresholds are not operational.

Observability instrumentation should be implemented against vendor-neutral standards to ensure portability. The CNCF OpenTelemetry specification is the recommended vendor-neutral standard for traces, metrics, and logs across the instruments described above.

For systems where agents are runtime actors — not just code executors but active participants in ongoing production behaviour — AgentOps telemetry is a required component of operational observability, not an optional supplement. The service health instruments above confirm that the system is running; AgentOps telemetry confirms what the agents inside the system are doing. The following AgentOps dimensions must be instrumented and visible in production dashboards before the observability condition is satisfied: model calls (with model version and token count), tool calls (with permission denial rate tracked separately), autonomy escalation events (with the human decision recorded), and human override events. A system where agents take consequential production actions but whose model calls and tool invocations are invisible in dashboards does not satisfy this condition, regardless of how comprehensive the service health instrumentation is. For Tier 2 and above, the full AgentOps telemetry profile — including memory reads and writes, retrieval corpus access, prompt version, policy version, failed tool use, cost anomaly signals, and quality anomaly signals — as defined in the AgentOps Telemetry section of [Operations Governance](operations-governance.md) is required.

---

**On-call assignment made.**

A named on-call engineer has been assigned, has been briefed on the system's SLOs and known failure modes, and has confirmed they have access to the runbook, the specification, and the rollback procedure. The briefing is not optional and is not satisfied by the on-call engineer having access to these documents — access without active briefing leaves a gap between what the engineer can find and what they know to look for under incident pressure. For systems with complex failure modes, the briefing should include a walkthrough of at least the most critical failure modes in the runbook.

---

**System steward assigned.**

A named steward has accepted stewardship, has confirmed they can pass the P12 accountability test (can recover intent, decisions, and evidence from the specification and evidence bundle, and can reproduce the system's expected behaviour), and has been briefed on the maintenance governance requirements in [Maintenance Governance](maintenance-governance.md). A steward who has been named but has not actively reviewed the specification and evidence bundle has not accepted stewardship in the governance sense — they have accepted a title. The operational DoD requires the former.

---

**Security scan clean.**

A dependency vulnerability scan was run against the system's full dependency tree at the time of production deployment, passed at the defined severity thresholds (no unresolved Critical or High vulnerabilities unless a waiver is filed with documented justification and accountable human approval), and the scan result is filed as part of the deployment evidence. The SBOM was generated at deployment and is filed alongside the deployment evidence. A security scan that was run against an earlier version of the dependency tree, or run in a development environment with a different dependency configuration than production, does not satisfy this condition.

---

**License compliance confirmed.**

A license compatibility report was generated for the component and its full dependency tree, confirming that all dependencies are licensed compatibly with the production deployment context as defined in the specification's license constraint. The report is clean, or waivers for known exceptions have been approved by legal or compliance, documented, and filed with the release artefact. License compliance that was confirmed at a previous release but has not been re-confirmed for the current release does not satisfy this condition if dependencies have changed.

---

**Trace retention policy set.**

A trace retention policy has been defined, specifying: which production decisions produce a reasoning trace, how long traces are retained in production, what format they are stored in, and what the access path is during an incident. The policy has been configured (not just documented), and the access path has been exercised at least once in a non-incident context (e.g., during a drill or a tabletop incident simulation) to confirm that on-call engineers can actually retrieve traces under time pressure. For regulated systems, the retention period must meet any applicable regulatory requirements (see [Maintenance Governance](maintenance-governance.md) for regulatory mapping). A trace retention policy that has been written but not configured does not satisfy this condition.

---

**DR/failover tested (for Tier 3 systems).**

For systems whose failure would constitute a significant business or compliance incident — Tier 3 blast radius as defined by the P12 accountability framework — disaster recovery and failover procedures have been tested in a representative environment within 30 days of production deployment. The test must confirm that failover completes within the defined recovery time objective and that the recovered system operates correctly against the evaluation suite in the recovery environment. A DR procedure that exists on paper but has not been validated against actual recovery mechanics does not satisfy this condition. The 30-day window applies to the initial deployment; re-testing is required after any significant infrastructure change and on a defined periodic schedule (practitioner default: annually, or after any incident that touches the system's infrastructure).

**RTO/RPO targets by blast radius tier.** The following practitioner defaults represent calibration starting points, not universal mandates. They must be reviewed against the system's actual business continuity requirements, regulatory obligations, and contractual SLAs — the lower of the default or the required value governs:

- Tier 1 (low blast radius): Recovery Time Objective 24 hours; Recovery Point Objective 24 hours.
- Tier 2 (medium blast radius): Recovery Time Objective 4 hours; Recovery Point Objective 4 hours.
- Tier 3 (high blast radius): Recovery Time Objective 1 hour; Recovery Point Objective 1 hour.

RTO and RPO that are set without reference to a tested recovery process are not targets: they are aspirations. If recovery testing consistently produces times longer than the target, the target must be revised — with accountable human sign-off — or the recovery architecture must be improved. Neither is optional.

**Annual DR drill requirement.** DR procedures must be exercised on a defined cadence, not just at initial deployment. For Tier 2 and Tier 3 systems, DR drills must be conducted at minimum annually. A DR drill for an agentic system must test: restoration of the deployed artefact from its stored configuration, restoration of agent memory from its retained state, confirmation that evaluation suites pass in the restored environment, and the escalation chain's function under simulated incident conditions. The drill output — elapsed time to restore, gaps identified in the procedure, corrective actions taken — is filed with the system's maintenance governance record and updates the runbook's DR section.

Organisations requiring formal alignment of DR planning with a recognised framework should refer to NIST SP 800-34 (Contingency Planning Guide for Federal Information Systems) as the planning standard.

Regulated organizations must align DR planning with the sector-specific requirements in the applicable domain file, which may impose more stringent RTO/RPO targets, testing frequencies, and documentation requirements than the practitioner defaults above:

- Financial services: SR 11-7, DORA, EU AI Act, MiFID II — see [Financial Services Regulatory Alignment](../domains/financial-services.md)
- Medical devices: FDA, IEC 62304, ISO 14971, MDR — see [Medical Devices Regulatory Alignment](../domains/medical-devices.md)
- Aviation: DO-178C, ARP4754A, EASA — see [Aviation Regulatory Alignment](../domains/aviation.md)
- Automotive: ISO 26262, SOTIF, UNECE WP.29 — see [Automotive Regulatory Alignment](../domains/automotive.md)
- Pharmaceuticals: GxP, 21 CFR Part 11, ICH guidelines — see [Pharma Regulatory Alignment](../domains/pharma.md)
- Defense and government: CMMC, FISMA, NIST SP 800-53 — see [Defense and Government Regulatory Alignment](../domains/defense-government.md)

---

## Phase Calibration

The operational DoD is calibrated to the phase of the system's deployment, consistent with the phase-calibrated approach of the manifesto's engineering Definition of Done.

**At Phase 3:** The following conditions are required: runbook complete (at reduced scope appropriate to Phase 3 — architecture overview, known failure modes, escalation chain, rollback procedure), on-call assignment made, steward assigned, and security scan clean (full dependency vulnerability scan and SBOM). SLO configuration and operational observability are required if the system has a user-facing SLA or is deployed with external consumers. Output quality monitoring is required if the system has a defined output quality SLO. DR testing is required for Tier 3 blast radius regardless of phase.

**At Phase 5:** All conditions are required, without exception, for all production systems. The Phase 5 deployment context — Tier 3 autonomy available, full agentic loop operating, production-impacting changes governed — demands the full operational DoD. A Phase 5 team deploying a system that does not meet the full operational DoD is deploying a technically well-built system into an insufficiently governed operational context.

---

## Operational DoD vs. Engineering DoD

The engineering DoD governs a change. The operational DoD governs a system. Understanding the difference matters for how teams structure their work.

The engineering DoD asks: was this change shipped, observable, verified, validated, learned from, governed, and economical? It is applied per loop iteration, per change. A team that applies the engineering DoD rigorously produces a sequence of well-governed changes. Each change leaves the system in a better or equivalent state than it found it.

The operational DoD asks: is the system, as it currently exists in production, operationally ready? It is not applied per change. It is the state of the system at any moment. A system that has received ten perfectly-governed changes and whose steward left six months ago without a qualified replacement is not operationally ready. The engineering DoD was satisfied for each change; the operational DoD is currently failing.

This distinction has a practical implication: the operational DoD must be checked on a cadence, not just at deployment. A quarterly operational DoD review — confirming that all conditions remain satisfied — is the governance mechanism that catches operational readiness failures between releases. The steward is accountable for conducting this review and for escalating if any condition is failing.

The operational DoD is not a higher bar than the engineering DoD — it operates at a different level. Both are required. Together they ensure that the system is both well-built (engineering DoD, per change) and well-governed in production (operational DoD, per system state). Neither substitutes for the other.
