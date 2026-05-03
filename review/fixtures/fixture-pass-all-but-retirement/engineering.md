# Helio — Build Stage

The Build stage is Helio's engineering execution layer. Helio does not
prescribe inner-loop semantics (planning, generation, verification,
review) and defers to whatever engineering practice the adopting team
already runs. The framework imposes outer obligations on what Build
must produce.

## Outputs

Every Build run produces a candidate artefact and a verification trace
linked to the Capture-stage acceptance criteria. The verification
trace is a precondition for entry to the Promote stage.
