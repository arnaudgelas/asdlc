# Helio — Operate Stage

The Operate stage carries the persistent obligations that keep a
deployed system operable. Helio's Operational Readiness Check verifies
the obligations below before a system is declared "running" and again
on a quarterly cadence thereafter.

1. **Operational runbook.** A runbook complete with diagnostic steps,
   escalation contacts, and known-failure remediation is attached to
   the system record.
2. **Operational observability.** Metrics and traces are wired to the
   monitoring substrate; observability configured before traffic is
   admitted to the system.
3. **On-call rota.** An on-call assignment is recorded; the on-call
   rota covers 24/7 with a defined escalation path.
4. **System steward.** A system steward is assigned; steward assigned
   in writing with clear scope and rotation cadence.
5. **Security scan clean.** A security scan clean result is recorded
   for the running configuration; the vulnerability scan runs nightly.
6. **License compliance.** License compliance is confirmed against the
   SBOM; every open-source licence is reviewed and approved.
7. **Trace retention policy.** A trace retention policy is set; the
   audit trace retention window matches the regulatory profile.
8. **DR/failover.** For tier-3 blast-radius systems, disaster recovery
   is designed and failover tested at least annually.

Helio considers retirement out of scope. Adopters are directed to
their own change-management process when a Helio-governed system is to
be withdrawn from service.
