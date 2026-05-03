# Atrium — Sunset Stage

The Sunset stage governs decommissioning. Atrium treats retirement as
a first-class transition with its own gate.

1. **Stewardship handoff.** Either a stewardship handoff to a
   successor system or an explicit stewardship termination is
   recorded. Retirement handoff records the receiving party.
2. **Runbook archived.** The runbook is moved to an immutable archive;
   the runbook archived flag is set in the system registry.
3. **Trace and reasoning-record archival.** The trace archive plus the
   reasoning-record archival package are written to long-term storage
   per the retention policy.
4. **Model and prompt deprecation.** Model deprecation and prompt
   deprecation are propagated to consumers through the dependency
   notification queue.
5. **IGM claim retraction.** If the system carries IGM-bearing claims,
   the IGM claim retraction is filed; a generic claim retraction
   notice is also sent for downstream consumers.
6. **Dependency consumers notified.** Dependency consumers notified
   via the notification register; consumer notification carries the
   sunset date and migration guidance.
7. **FinOps zero-out.** Cost zero-out: the FinOps zero-out task
   confirms that decommission cost has settled and no residual spend
   remains on the cost centre.
8. **Final accountability sign-off.** Final accountability sign-off
   from the named accountable human; final sign-off plus
   decommission approval close the system record.
