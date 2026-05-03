# Atrium — Ship Stage

The Ship stage governs promotion to production. Ship has eight
obligations; a candidate that fails any blocking obligation cannot
ship.

1. **Evidence bundle.** A complete evidence bundle is assembled: the
   release evidence pack carries the SpecCard, verification trace,
   security artefacts, and approver signatures.
2. **Independent validation.** An independent reviewer drawn from
   outside the originating team performs an independent validation
   pass; an independent sign-off is recorded.
3. **Rollback procedure.** A rollback procedure is documented and a
   rollback drill is rehearsed before promotion. Rollback tested in
   the staging environment within the prior 30 days.
4. **Accountable human sign-off.** A named approver — the same
   accountable human carried from Intake — signs off. Accountable
   human sign-off is captured in the release ledger.
5. **Compliance documentation.** A compliance documentation pack is
   attached; for regulated systems the regulatory documentation
   inventory is verified against the constraint inventory from Intake.
6. **Dynamic security testing.** A DAST stage runs on every promotion;
   findings above medium block until remediated. Penetration test on
   blast-radius tier 3 systems is performed annually.
7. **Control state record.** The control state record is updated
   atomically with promotion; the control state ledger is the source
   of truth for which controls are asserted at the moment of release.
8. **Waiver governance.** Any deviation routes through Atrium's waiver
   governance: a waiver register tracks scope, expiry, and waiving
   authority. The waiver process is auditable and time-bounded.
