# Atrium — Intake Stage

The Intake stage governs the boundary between business demand and
engineering work. A request is admissible to Build only if every
Intake obligation is satisfied and the Intake Reviewer has signed.

## Obligations

1. **Demand validation.** The requester records a demand validation
   note tying the request to a verified user need or strategic
   objective. Atrium calls this "validated demand" on the Intake form.
2. **Measurable value.** The Intake form carries a value metric and
   target threshold. Value measurable in either currency, time, or a
   counted unit; uncountable benefits are rejected.
3. **Acceptance criteria.** Every request declares acceptance criteria,
   ideally as executable acceptance tests.
4. **Constraints identified.** A constraint inventory is attached
   covering regulatory constraint surface, internal policy, and
   architectural boundaries.
5. **Named accountable human.** The Intake form names an accountable
   human, plus an alternate. Human accountability is recorded in the
   Intake header and propagates to every later artefact.
6. **Blast radius.** The blast radius score (0-3) is computed and
   reviewed; tier 2 and 3 escalate to additional reviewers.
7. **Out-of-scope statement.** The form has a mandatory "explicitly
   excluded" section listing what is out-of-scope.
8. **Loop cost ceiling.** A per-iteration cost ceiling is set; the
   loop cost justified note records the rationale.
9. **Context thread.** A context thread is assembled — source documents,
   prior decisions, dependency notes — and human-reviewed before the
   request is admitted.

A request missing any obligation is returned to the requester.
