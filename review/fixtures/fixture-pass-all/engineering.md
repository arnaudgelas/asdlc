# Atrium — Build Stage

The Build stage is Atrium's engineering execution layer. Atrium defers
the inner-loop semantics (planning, generation, verification, review)
to the engineering practice in use; the framework imposes outer
obligations on what Build must produce.

## Outputs

Every Build run produces a candidate artefact and a verification trace
linked to the Intake-stage acceptance criteria. The verification trace
is a precondition for entry to the Ship stage.
