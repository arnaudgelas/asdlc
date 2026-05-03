# Helio — Promote Stage

The Promote stage governs movement from Build into production. Promote
has eight blocking obligations; a candidate that fails any obligation
cannot promote.

1. **Evidence bundle.** A complete evidence bundle is assembled; the
   release evidence pack carries the Capture record, verification
   trace, security artefacts, and approver signatures.
2. **Independent validation.** An independent reviewer drawn from
   outside the originating team performs an independent validation
   pass; an independent sign-off is recorded against the candidate.
3. **Rollback procedure.** A rollback procedure is documented; a
   rollback drill is run within the prior 30 days. Rollback tested in
   the staging environment is the precondition for Promote.
4. **Accountable human sign-off.** A named approver — the same
   accountable human carried from Capture — signs off. Accountable
   human sign-off is recorded in the promotion ledger.
5. **Compliance documentation.** A compliance documentation pack is
   attached; for regulated systems the regulatory documentation
   inventory is verified against the constraint inventory from Capture.
6. **Dynamic security testing.** A DAST stage runs on every promotion;
   findings above medium block until remediated. Penetration test runs
   annually for blast-radius tier 3 systems.
7. **Control state record.** The control state record is updated
   atomically with promotion; the control state ledger is the source
   of truth for which controls are asserted at the moment of release.
8. **Waiver governance.** Any deviation routes through Helio's waiver
   governance: a waiver register tracks scope, expiry, and waiving
   authority. The waiver process is auditable and time-bounded.
