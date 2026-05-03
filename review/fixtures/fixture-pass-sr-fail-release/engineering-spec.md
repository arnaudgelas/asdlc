# SpecCraft Specification Discipline

SpecCraft's Demand Shaping layer produces a governed specification
artefact called a SpecCard. A SpecCard is the only valid input to the
Engineering Loop.

## SpecCard contents

Every SpecCard must declare, before it is admissible to engineering:

1. **Validated demand** — written demand validation note from the
   business stakeholder, referencing the originating user research,
   support ticket, or strategic objective. SpecCraft treats unverified
   demand as an automatic rejection.
2. **Measurable value** — a value metric and target threshold, stated
   so the post-release outcome can be checked. Value measurable in
   either currency, time, or a counted unit.
3. **Acceptance criteria** — a set of acceptance tests, expressed as
   executable specs where feasible.
4. **Constraints identified** — a constraint inventory covering
   regulatory constraint surface, architectural boundaries, and
   data-handling rules.
5. **Named accountable** — a named accountable human, with an alternate.
   Human accountability is recorded in the SpecCard header.
6. **Blast radius** — a blast radius score on a 0-3 scale; SpecCards
   above tier 1 require additional reviewers.
7. **Out-of-scope statement** — every SpecCard declares what is
   explicitly excluded from the change.
8. **Cost ceiling** — a loop cost ceiling per run and an overall cost
   justified note for the SpecCard as a whole.
9. **Context thread** — a context thread of source artefacts, prior
   decisions, and dependency notes is assembled and human-reviewed
   before the SpecCard is admitted to engineering.

A SpecCard missing any of these nine elements is returned to the
requester. SpecCraft considers admission discipline its main
contribution.

## Engineering Loop

The Engineering Loop is a four-step cycle: plan, generate, verify,
review. The loop's output is a candidate artefact plus an evidence
trace of the verification step.
