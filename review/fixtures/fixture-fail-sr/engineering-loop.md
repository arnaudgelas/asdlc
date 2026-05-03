# LoopForge Engineering Loop

The LoopForge loop is a four-phase inner cycle: draft, generate, test,
review.

## Inputs

A LoopForge ticket is a short free-text description of what the requester
wants. Tickets are written by anyone on the team and entered into the
queue with no formal triage.

## Acceptance Criteria

Every ticket is expected to declare an acceptance test that the
generated artefact must pass. The acceptance criteria can be expressed
as a unit test, an integration test, or a written checklist.

## Out of Scope

LoopForge does not concern itself with rollout, monitoring, or
deprecation. Those concerns are explicitly excluded from the loop.

## Cost Ceiling

Each loop run has a configurable token and runtime cost ceiling. The
loop cost justified per run is enforced by the runtime; tickets that
exceed the ceiling are auto-cancelled.

## Context Bundle

The agent receives a context bundle composed of the ticket text, the
relevant repository slice, and the previous run's diff if any. The
context bundle is assembled automatically and is not human-reviewed
before the run.

## What LoopForge does NOT do

LoopForge does not check whether the request reflects a real user
need. It does not require an owner-of-record per ticket. It does not
assess impact or downstream effects before code is generated. It does
not enumerate the rules — regulatory, operational, or architectural —
that a generated artefact must respect. It does not measure value
delivered.

These omissions are intentional in the framework's design philosophy
and are described as host-organisation responsibilities in the
LoopForge handbook.
