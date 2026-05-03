# SpecCraft Release Process

SpecCraft's release process is intentionally lightweight. The framework
authors take the position that admission discipline at the front of the
loop is what matters; once a SpecCard exits engineering, release is a
local concern.

## Promotion

A candidate artefact is promoted to production by the engineer who ran
the loop, after a peer review on the diff. There is a named approver
recorded on the merge: the same engineer's nearest reviewer. Accountable
human sign-off is captured in the merge metadata.

## Deferred concerns

SpecCraft deliberately does not require:

- A formal release artefact ledger.
- An outside-team reviewer with veto authority.
- A rehearsed reversal procedure for promoted changes.
- A regulator-facing documentation pack tied to the release.

The framework's authors describe these omissions as conscious trade-offs
and recommend that adopting organisations add their own gating layer
where regulatory regimes demand it.

## Dynamic security testing

SpecCraft does run a DAST stage on every promotion. Findings above
medium severity block the promotion until acknowledged by the named
approver.

## Waivers

Waivers from the SpecCraft promotion policy are tracked in a waiver
register. Each entry names the waiving authority, the scope, and the
expiry date. Waiver governance is treated as a first-class concern.

## Control state

A control state record is generated per release and stored in the
release artefact store. The control state ledger is updated atomically
with each promotion.
