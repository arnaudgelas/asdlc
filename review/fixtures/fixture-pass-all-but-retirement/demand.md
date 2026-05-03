# Helio — Capture Stage

The Capture stage is Helio's admissibility boundary. A request enters
Build only after the Capture Reviewer has signed every obligation
below.

## Obligations

1. **Demand validation.** The originating team records a demand
   validation note tying the request to a verified user need. Helio
   labels this "validated demand" on the Capture record.
2. **Measurable value.** Each request carries a value metric and a
   target threshold; the value measurable in currency, in time saved,
   or in a counted unit.
3. **Acceptance criteria.** Acceptance criteria are required in
   executable form where feasible; the acceptance test set is the
   contract between Capture and Build.
4. **Constraints identified.** A constraint inventory is attached
   covering regulatory constraint, internal policy, and architectural
   boundaries.
5. **Named accountable human.** The Capture record names an
   accountable human (and an alternate). Human accountability is
   carried forward unchanged through every later stage.
6. **Blast radius.** A blast radius score (0–3) is computed at Capture
   time; tier 2 and 3 systems escalate to additional reviewers.
7. **Out-of-scope statement.** Every request carries an "explicitly
   excluded" section; Capture rejects requests whose out-of-scope
   surface is undeclared.
8. **Loop cost ceiling.** A per-iteration loop cost ceiling is set; the
   cost justified note records the rationale and the assumptions.
9. **Context thread.** A context thread is assembled — source documents,
   prior decisions, dependency notes — and is human-reviewed before
   admission.

A Capture record missing any obligation is returned to the requester.
