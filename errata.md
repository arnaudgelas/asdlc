# Errata

Dated corrections to previously published content in this repository. Each entry
records what was wrong, what was done about it, and when.

## 2026-09-07

- **`D-06` · The SR 26-2 non-enforceability sentence was quoted to two-thirds at
  all four of this repository's canonical carriers, and its footnote was carried
  at none of them; the sentence now runs to its end with the footnote's text, in
  the sentence that uses it.** At `asdlc.md`, `asdlc-guide.md`,
  `release-governance.md` and `domains/financial-services.md` the quotation
  stopped at *"prescriptive requirements"* and a full stop. The instrument is on
  disk and was signed at primary on 02.09.2026 by a named non-drafter:
  `inputs/20260902-arnaud/sources/SR2602a1.pdf` (sha256
  `209ce4c14cea8aab3dc2f27bae1293efb6e1b60f9577a68d9595f85e4b94b0af`, re-derived
  07.09.2026 and identical to `inputs/20260902-arnaud/SR26-2_verification_record.md`),
  with `SR2602a1.txt` (`pdftotext -layout`) beside it. **This is application of
  that signature, not a re-derivation from a secondary, and it is not a second
  signature.** Page 2, § I, in full: *"This guidance does not set forth
  enforceable standards or prescriptive requirements; accordingly, non-compliance
  with this guidance will not result in supervisory criticism against a banking
  organization."* — carrying **footnote 1**, also in full: *"See 12 CFR Part 4,
  Subpart F, Appendix A (OCC); 12 CFR Part 262, Appendix A (Board); 12 CFR Part
  302, Appendix A (FDIC). However, supervisory action may result for any
  violations of law or unsafe or unsound practices stemming from insufficient
  management of model risk."* Both strings were byte-compared against the hashed
  primary under NFKC normalisation with hyphenation rejoined; a one-word swap
  (`supervisory criticism` → `supervisory action` inside the § I sentence) missed
  on the same harness, read after the positives.
  **Direction, stated here and in each of the four sentences rather than in a
  note (`F2`):** every carrier cites the sentence in order to *disclaim* that
  SR 11-7 or SR 26-2 binds, so the completion **supports** each of the four —
  and footnote 1 bounds the same conclusion, because **non-enforceable is not
  consequence-free**: supervisory action routes through violations of law and
  unsafe-or-unsound practices instead of through the guidance. **No claim was
  deleted and no argument reversed.**
  **Deliberately not swept: this file's own three occurrences of the truncated
  form** — the SR 11-7 / IEC 62304 / GAMP 5 entry, the seven-year-retention
  entry, and the *"requires"/"expects"* entry of 2026-09-06. They are dated
  records of what earlier passes checked and wrote, not live canonical claims;
  rewriting a record to say what its pass did not say destroys the evidence of
  how the truncation travelled. A sweep keyed on `enforceable standards` hits all
  three, which is why each candidate was read in context before being edited.
  **Register note:** `D-06`'s 06.09 count block names **two** `errata.md`
  occurrences; **there are three** — a third stands in the 06.09 entry written
  after that count was taken. The block's four-canonical figure reproduces
  exactly.
  **What is not a carrier here, checked rather than assumed:** the second,
  definitional exclusion ground (`D-52` — the § II definition of *"model"*
  excluding *"simple arithmetic calculations, such as those found within
  spreadsheets, as well as deterministic rule-based processes and software where
  there are no statistical, economic, or financial theories underpinning their
  design or use"*) **has no carrier in this repository**: no document here rests
  anything on SR 26-2's scope exclusion. `command grep -rniF --include='*.md'`
  over this repository returns **0** files for `not within the scope`, `novel and
  rapidly evolving`, `footnote 3`, `traditional statistical`, `non-generative`,
  `spreadsheet` and `rule-based`, against a positive control (`gate` → **27**
  files) read first and a negative control (a ten-letter nonsense stem with
  digits and a tail → **0**) read after. The ground was therefore **not inserted
  here**, because there is no claim standing on one limb for it to complete.

## 2026-09-06

- **Two references told the reader a document was unwritten when it was written
  and substantive; the annotations are removed and neither target was changed.**
  `asdlc.md:250` read
  "`agentic-engineering-manifesto/governance/composition-rule.md` (planned)" and
  `release-governance.md:222-223` read
  "`agentic-engineering-manifesto/governance/evidence-bundle-schema.md`\n(planned
  under A1)". Both files were opened on 06.09.2026 — `composition-rule.md` 228
  lines, a normative cross-framework rule; `evidence-bundle-schema.md` 234 lines,
  a normative cross-framework artefact — so in each case the annotation, not the
  reference, was the false half. **This is the opposite repair to the one made
  the same day in `aplc/`, where references pointed at nothing and the path was
  corrected; here the path was already right and the annotation was wrong**, and
  a single sweep treating both as "the annotation is wrong" would have got the
  `aplc/` half backwards. No `(planned)`-style annotation of this form now
  remains in this repository: the pattern
  `` `[^`]*\.md` \([Pp]lanned[^)]*\) `` returns nothing over `asdlc/*.md`,
  wrap-safe, on 06.09.2026 — this errata file quotes the struck strings and is
  therefore itself a hit, which is why the claim is scoped to the framework
  documents and not stated as a repository total.
- **A row in the Contents table promised a document that has never existed, and
  is annotated rather than deleted.** `asdlc.md:944` lists
  `human-oversight-patterns.md` as a Cross-cutting document of this repository.
  `find . -iname 'human-oversight-patterns.md'` over the whole corpus returns
  nothing on 06.09.2026, against a positive control on `agent-human-oversight.md`
  which returns `aplc/agent/agent-human-oversight.md` — **a different repository
  and a different document (APLC agent-product oversight, not an ASDLC
  cross-cutting pattern taxonomy), so it is not this row's target under another
  name.** **The control had to be re-run with `-type f`, and that is worth
  recording rather than tidying away:** run without it, the same control also
  returned `./agent/agent-human-oversight.md`, which is one of the 25 empty
  directories standing at the corpus root awaiting a human decision, and it
  would have been read as a second copy of the document. Twenty-five such
  directories carry `.md` names, so **any "does this file exist under another
  name" check in this corpus that uses a bare `find -iname`, or any resolver
  testing `-e` rather than `-f`, can report a stray directory as a document.**
  `tools/link-check.sh` is not affected — it tests `-f` and resolves relative to
  the linking file's directory, both checked on 06.09.2026 — and no stray
  directory was created, deleted or altered by this pass. The row is kept and marked *(not yet written)* with the reason in the
  same cell, because a single index row is the only surviving evidence that the
  document was intended and deleting it destroys that evidence; **an index row
  is not a document, so this is an honest annotation and not a close.**
  · **Marking a genuinely-unwritten target is the correct direction and does not
  re-open the defect struck two bullets above**, whose close condition is that
  every such annotation either sits beside a genuinely unwritten target or is
  gone. The wording avoids the literal `(planned)` form so that the re-check
  pattern's count stays a measurement of the stale cases.
  · **No line was added or removed:** `asdlc.md` 989 lines and
  `release-governance.md` 1318 lines, before and after.
  · **This file is untracked in git and this repository last committed
  `0f28bb5` in May 2026, so `git diff` shows nothing for these edits and nobody
  reading `HEAD` receives them** — that is `D-73`, and this entry is not a close
  of `D-32` or `D-59` at `HEAD`.

- **No entry to make: this repository was enumerated for the annex-attribution
  defect corrected in the other three and has none.** The defect is an annex
  citation whose line names no instrument, which an attribution pass then files
  under whatever instrument the surrounding prose happens to name. Enumerated
  with `command grep` over `git ls-files -- '*.md'` plus
  `git ls-files --others --exclude-standard -- '*.md'`, **27 files scanned**,
  both line-scoped and wrap-safe, and again over whole-file text with dashes
  mapped to spaces so a citation split across a line break could not hide:
  **no annex citation of the Roman-numeral kind this defect concerns** anywhere
  in this repository, against a positive control on the identical commands that
  did hit the files carrying the bare word. Stated as a kind rather than as a
  total, because a total is wrong in both directions here: the repository does
  carry Arabic-numbered GMP annex citations, in `domains/pharma.md` and
  `README.md`, which are not of this class; and this file quotes some of them
  when it explains them, so any figure counts the errata as well as the
  content. This file is untracked in git, so `git grep` does not see it; the
  enumeration above does.
- **Re-enumerated for the remaining annex-attribution defect: still none.**
  The 2026-09-06 entry above recorded zero sites of this class in this
  repository. That enumeration was re-derived rather than trusted, because the
  class grew when it was re-measured in two of the other repositories: the
  checker's own refusal list was read in full rather than filtered to four
  instruments, `--dump-triples` was filtered to annex citations, and a
  wrap-safe and a whole-file normalised scan were run over **27 files** here.
  **No annex citation of the Roman-numeral kind this defect concerns**, and no
  refusal naming this repository, against positive controls on the identical
  commands and a fresh negative control that returned nothing. As in the entry
  above, the Arabic-numbered GMP annex citations this repository does carry are
  a different class, and are neither counted in nor counted out by a bare
  total. This file is untracked in git.
- **Annex citations hidden by a line break: none here, re-derived.** The
  adjacent class the 2026-09-06 entry above records — annex citations split
  across a line break, which the line-scoped extractor does not see at all —
  was enumerated across the corpus with a wrap-safe scan and a whole-file
  normalised scan (dashes mapped to spaces, blockquote and list markers
  stripped **before** joining adjacent lines, which is what a raw line join
  misses), over `git ls-files` **plus** `git ls-files --others
  --exclude-standard`, **27 files** here and **210** in the corpus, with no
  filter by instrument. **Zero sites in this repository**, against a positive
  control on the identical command and file set and a fresh long negative
  control returning zero. Sixteen were found elsewhere and all sixteen are
  closed. This file is untracked in git.
- **A corpus claim in this file was measuring this file: absence-and-count
  claims about this repository and about the corpus, corrected without
  substituting a new number.** The class is a claim about *this corpus* that its
  own file falsifies — a note recording that something is absent, or that it
  stands at so many sites, published into a file that is itself inside the search
  space, so that the sentence moves the number it reports. It is distinct from a
  claim about the text of an external instrument: the many notes in this file
  recording that a phrase is absent from a hashed primary are unaffected by this
  file quoting the phrase, and every one of them was left exactly as it stood.
  Three sites here were of the corpus-scoped kind and all three are corrected.
  The sharpest is the note about the brief's wording for where a binding period
  sits: it quoted the phrase in full and asserted in the same sentence that the
  phrase was nowhere in the corpus, so the sentence falsified itself as it was
  typed. It is now paraphrased rather than quoted, on the rule that a withdrawn
  or absent phrase reproduced verbatim in a correction is read by later checks as
  a live quotation. The second is the convergence note, which gave a cross-repo
  total for a locator string in the same sentence that carries the string.
  · **The third was true in one sense and false in another, and both are now
  recorded.** The annex-attribution entries at the head of this section claimed
  no annex-and-numeral citation *of any kind* here. Read as the class the entries
  are actually about — Roman-numeral annex citations of the instrument in
  question — that holds, and re-derivation confirms it. Read literally, it does
  not: this repository carries Arabic-numbered GMP annex citations in a domain
  file and in the readme, and this file quotes some of them when explaining them,
  so the literal reading was false before the entry was written and was made
  worse by writing it. The wording now states the kind rather than a total, and
  says what the repository does carry.
  · **The form of the correction is the same at every site, and it is not a
  smaller number.** A figure written "excluding this note" goes stale at the next
  entry with no word changing, which is the same trap one order out. Each
  sentence now makes a claim about named lines — what is at them, and what is
  attributed there — which nothing written elsewhere can move. Where a figure was
  dropped the sentence says why, so a reader does not read the absence as an
  oversight rather than as a choice.
  · **Controls.** A fresh two-word negative control was chosen only after
  confirming it was absent from every Markdown and HTML file in the corpus, and
  was then run with the identical command and file set as a positive control that
  hit a large share of them. Its result is deliberately not written here as a
  figure, and the string itself is not reproduced: recording a control in a
  published file is what burns it, and earlier controls in this corpus are
  already unusable for exactly that reason, some of them recorded in this file.
  That is the same effect this entry describes, one level up. **The cost of this
  form is real and is stated rather than hidden: a reader cannot re-run a control
  they cannot see.** The positive control carries the weight instead — it is
  supposed to be present, so publishing it cannot burn it, and a run in which it
  fails to hit is a broken search rather than a demonstrated absence.
  · This file is untracked under `D-57`, so `git -C asdlc diff` does not show
  this entry. It was written anyway, and this line says so.


## 2026-09-05

- **A fourth carrier of the withdrawn DORA "Article 14" change-management
  citation was missed by the 2026-09-05 withdrawal and shipped live in
  `asdlc.md:574`; it is now corrected to Article 9(4)(e), and the two other
  instruments in the same sentence are marked unsourced.** The errata entry
  below records the withdrawal as "two files, three sites". That count was a
  lower bound. `asdlc.md`'s "Regulated industry" adoption paragraph read
  *"Regulated industries have externally imposed gate conditions — DORA
  Article 14, SR 11-7, IEC 62304, GAMP 5 — that are not optional"*, which is
  the retired citation asserted as a live requirement, not quoted in order to
  withdraw it. **The site was missed because it was searched for with the
  shell's `grep` function and `--include`, which silently under-reports**:
  re-run at the corpus root on 2026-09-05, `grep -rn "DORA Article 14"
  --include='*.md' .` returns **17** lines and `command grep -rn "DORA
  Article 14" --include='*.md' .` returns **27**. Ten lines, including this
  one, were invisible to the form of the search that declared the withdrawal
  complete. Every count in this programme taken with the shell function and
  `--include` must be treated as a lower bound until re-derived with
  `command grep`.
- **What the sentence now says, and why the fix is not a renumbering.** The
  paragraph is about externally imposed *gate conditions*, so the replacement
  had to be a provision that imposes one. DORA Article 9(4)(e) does:
  *"implement documented policies, procedures and controls for ICT change
  management"*, changes *"recorded, tested, assessed, approved, implemented
  and verified in a controlled manner"*, and the closing subparagraph of
  Article 9(4), *"the ICT change management process shall be approved by
  appropriate lines of management and shall have specific protocols in
  place"* — an approval step stated in the instrument. Article 9(4)'s chapeau
  reads *"financial entities shall"*, so the "not optional" claim survives for
  DORA. Article 9(4)(b) was **not** used, because its operative words are
  *"that may include implementing automated mechanisms…"* — quoting a
  permissive clause as a requirement would reproduce the defect class rather
  than close it. All five quotations were byte-compared against the hashed
  primary `inputs/20260905-arnaud/prep/asdlc-standards/sources/dora_fulltext.txt`
  (sha256 `25328c7e39c4…3b4d1e`) under the citation checker's
  `normalizeForMatch`, each with a one-word-swap negative control
  (`policies`→`plans`, `verified`→`audited`, `shall`→`should`,
  `approved`→`signed`, `Communication`→`Change management`); all five
  positives hit and all five controls missed. `change management` occurs in
  the Regulation only at 9(4)(e) and its closing subparagraph.
- **SR 11-7, IEC 62304 and GAMP 5 stood in the same sentence unchecked, and
  "not optional" does not hold of any of them.** SR 11-7 was reached at
  primary (`inputs/20260905-arnaud/prep/D-20-primary/sources/sr1107a1.txt`,
  sha256 `d8ef343917…`): it is supervisory guidance written in *"should"*, and
  its independence language is *"Validation involves a degree of independence
  from model development and use"* and *"validation should be done by people
  who are not responsible for development or use"* — not a "validation
  requirement". The successor guidance **SR 26-2** (17 April 2026,
  `inputs/20260902-arnaud/sources/SR2602a1.txt`) states *"This guidance does
  not set forth enforceable standards or prescriptive requirements"*, which
  this repository has already established elsewhere and which contradicts
  "not optional" directly. Negative controls (`enforceable`→`binding`,
  `criticism`→`action`, `degree`→`presumption`, `should`→`must`) all missed.
  Whether SR 26-2 formally rescinds SR 11-7 is **NOT REACHED** — the letter
  attachment held here carries no rescission language, and the supersession is
  recorded in this programme's register rather than read at primary.
  **IEC 62304 and GAMP 5 are paywalled, were not purchased, and no unofficial
  copy was fetched, sought or considered — they stay OPEN.** The two mapping
  claims built on them are consequently marked as the ASDLC's own construction
  and unsourced, in the sentences that carry them, rather than deleted.

- **D-65: three DORA change-management specifics were left asserted in
  unquoted main clauses by the Article 14 withdrawal, and are now marked
  unsourced in the sentences that carry them.** The 2026-09-05 withdrawal
  replaced "DORA Article 14" with Article 9(4)(e) and quoted 9(4)(e) verbatim,
  but four sites went on asserting three things that quotation does not
  contain: a documented rollback procedure, post-implementation review, and
  independent testing of changes before production deployment for critical or
  important functions. Against the hashed primary
  `inputs/20260905-arnaud/prep/asdlc-standards/sources/dora_fulltext.txt`
  (sha256 `25328c7e39c4…`), `rollback` occurs 0 times, `post-implementation`
  0 times and `independent testing` 0 times, each with a live one-word-swap
  negative control (`recovery`, `post-incident`, `independent parties` all
  hit the same file), so the three zeros are absences and not broken
  searches; `back-out` and `roll-back` are 0 as well. The phrase "change
  management" occurs in the Regulation only inside Article 9(4)(e) and its
  closing subparagraph, so no other DORA provision carries the three
  specifics either. Pre-implementation testing is retained as a DORA
  requirement, because 9(4)(e) requires changes to be "recorded, tested,
  assessed, approved, implemented and verified in a controlled manner". For
  independent testing the nearest real DORA duties are now stated in place
  and correctly attributed: Article 24(4), that tests are "undertaken by
  independent parties, whether internal or external", and Article 24(6), that
  appropriate tests are conducted at least yearly on all ICT systems and
  applications supporting critical or important functions — a programme-level
  periodic duty, not a per-change release gate. **No claim was deleted.** All
  four sites now say the same thing: `release-governance.md` (the financial
  services release-requirements paragraph), `domains/financial-services.md`
  (the Article 9(4)(e) section, its mapping-bullet lead-in, and the Layer 3
  independent-testing table row) and `domains/insurance.md` (the Layer 3 DORA
  row and footnote 2). Deleting the claims silently is the mechanism that
  created the defect, so it was not used.

- **Every calibration default in this repository now carries its register in
  the same sentence as the number.** Three registers are used: *measured*
  (with the measurement named), *policy-set* (a chosen default, said so), and
  *illustrative* (a worked hypothetical). Where neither a measurement nor an
  authorial choice could be established from the corpus, the figure is marked
  *origin not established* rather than assigned a register on a guess. **No
  figure was changed and none was deleted.** The 60% value-realisation floor
  at all three of its sites, the demand-layer warning thresholds and
  time-to-governance targets, the four Governance Quality Score weights, the
  governance-graph push SLOs, the steward portfolio limits, the twelve-month
  tool-authorisation staleness threshold, the CVSS patch and triage SLOs, the
  waiver duration and portfolio limits, the FinOps variance and budget
  thresholds, the canary percentages, the RTO/RPO defaults and the
  rubber-stamping detection thresholds are all now marked in place.
  Regulatory figures — the DORA, NIS2, GDPR and SR 11-7 windows — were left as
  they were, on the reasoning that their origin is the instrument and is
  already named. **That reasoning did not hold for two of the four and is
  superseded by the two entries below**: SR 11-7 states no retention period at
  all, so the seven years were never the instrument's, and DORA's early-warning
  and reporting clocks are not in the Regulation either.
  The caveat is deliberately in-sentence rather than in a footnote: a
  footnoted qualifier is stripped the first time a figure is lifted into a
  slide, and a sentence is harder to strip than a footnote (`D-42`, `D-43`).
- **The rubber-stamping detection thresholds in `operations/governance.md`
  now say what they cannot do, in the sentence that sets them.** They are
  behavioural proxies for a discrimination no safety-critical field has a
  validated, non-disruptive method for making in live operations (`D-15`), so
  they are author defaults standing in for an unsolved problem rather than
  calibrated detectors.

- **Rubber-stamping detector demoted from assurance basis to screen, and tier
  restoration no longer clears on the same proxies.** `operations/governance.md`
  confirmed rubber-stamping on three conjunctive proxy conditions (approval
  time below minimum plausible review time, zero recorded challenges, approver
  concentration) and then required, for restoration, that those same proxies
  come back clean. All three are behavioural proxies an approver can satisfy
  without doing the cognitive work; clearing them shows the careless form of
  the pattern has stopped, not that engagement returned. The detector is now
  stated to be adequate to confirm an event and inadequate to clear one, and
  the section adds that a declining rate of challenges, rejections or
  interventions is not evidence of improvement -- it is a composite of the
  bundles' true defect rate and the approver's disengagement and falls
  identically under both, so it must not be offered as evidence for an
  autonomy tier increase. Restoration now requires, in addition to the 60-day
  proxy window, either a supported result from a **proposed and unvalidated**
  Engagement Falsification Protocol run (double-blind synthetic defect
  injection into gate submissions, blinded to approvers and their supervisors,
  every injected submission intercepted before release, outcomes registered as
  supported within scope / contradicted / inconclusive) or a blind post-hoc
  adjudication by adjudicators outside the approval chain -- or, failing both,
  an explicit statement in the restoration record that no measurement of
  approver engagement supports it. **Nothing in this repository authorises
  live fault injection into a production gate**, and the protocol's limits are
  stated in the text: no reach into actions inside an approved envelope, no
  irreversible or person-affecting submissions, and no power on a low-volume
  gate, where the result is inconclusive and the tier holds.
- **No numeric pass criterion is asserted for the protocol.** The research
  synthesis behind it carries one only as an embedded figure image with no
  text equivalent; the criterion is stated structurally instead and no numeral
  is quoted.
- **Adding approvers is not a restoration measure.** Stated explicitly, to
  align with the agentic engineering manifesto's adoption metrics document
  (`agentic-engineering-manifesto/adoption/metrics.md`);
  independent adjudication outside the approval chain is a different
  intervention and is what restoration rests on.
- **DORA "Article 14" change-management citation withdrawn (two files, three
  sites) and replaced with Article 9(4)(e), verified at primary.**
  `domains/financial-services.md`'s "ICT Change Management" section and its
  Layer 3 regulatory-control table footnote, and a separate, independent
  repetition of the same fabrication in `release-governance.md`, all cited
  DORA Article 14 for a change-management obligation. Article 14 is
  *Communication* — crisis-communication plans, staff/stakeholder
  communication policies, and a named media contact — and carries no
  change-management provision; the cited paragraph exists but carries no
  lettered sub-paragraphs, so the sub-clauses attributed to it do not exist.
  The obligation is now cited at DORA Article 9(4)(e), quoted in full and
  verified verbatim against the primary (EUR-Lex, Regulation (EU)
  2022/2554). `domains/insurance.md`'s DORA table row inherited the same
  fabricated Article 14 citation and was corrected to Article 9(4)(e) along
  with the other two.
- **DORA "Article 5" citation corrected to Article 8(3) for pre-change risk
  identification.** `domains/financial-services.md` attributed a
  pre-change ICT risk-identification obligation to DORA Article 5, which is
  *Governance and organisation* (management-body duties to approve, oversee,
  and resource the ICT risk management framework) and contains no
  risk-identification obligation. The obligation is now cited at DORA
  Article 8(3), cited unquoted.
- **DORA "Article 10" citation corrected to Article 18 for major-incident
  classification; Article 10 retained for detection.** The same file
  attributed classification of ICT-related incidents by impact to DORA
  Article 10, which is *Detection* and contains no classification-by-impact
  language. Classification by impact is DORA Article 18. Article 10's
  correct role — detection of ICT-related incidents — was not disturbed and
  remains cited where it already was.
- **Solvency II Article 115 fabricated paragraph number withdrawn (two
  sites).** `domains/insurance.md` appended a parenthetical "(3)" to
  citations of Solvency II Article 115. Article 115 has no numbered
  paragraphs — it is five unnumbered subparagraphs. The article and the
  substance cited (the major/minor model-change-policy requirement) were
  correct and are unaffected; only the fabricated paragraph number was cut,
  at both the prose citation and the regulatory-control table row and its
  footnote.
- **EU GMP "Annex 15" retention citation withdrawn.** `domains/pharma.md`
  cited EU GMP Annex 15 for a GMP-records retention period. Annex 15 is
  *Qualification and Validation* and contains no retention provision; none
  of "retain," "retention," or "year" occurs in it. The citation was cut.
  No replacement citation is asserted, and whether "product lifetime plus
  one year" is itself the correct retention figure has not been signed off.
- **EU AI Act Art. 9(2) paraphrase was inside quotation marks; now quoted
  exactly.** `domains/financial-services.md` wrote `"Throughout the
  lifecycle"` in quotation marks immediately after paraphrasing Article 9.
  The marks were lifting the document's own preceding paraphrase, but a
  reader takes quotation marks as the Act's words. The phrase occurs zero
  times in the hashed primary. Article 9(2) reads "planned and run
  throughout the entire lifecycle of a high-risk AI system"; the sentence
  now quotes that span exactly and attributes it to Art. 9(2). The marks
  were kept rather than dropped because the quoted span is now a true claim
  about verbatim text and carries the paragraph reference the emphasis
  lacked. A one-word divergence ("entire") is the size that survives
  review, which is why it was not left as emphasis.
- **Unsourced GMP retention period marked in the sentence that asserts it;
  the figure itself is handed back, not fixed.** The 2026-09-05 withdrawal
  of the "EU GMP Annex 15" citation in `domains/pharma.md` removed the
  citation but left "the product lifetime plus one year for GMP records"
  standing as an assertion in the main clause, outside any quotation marks
  — an unsourced regulatory assertion, which nothing marks as needing a
  source and which a quotation check cannot see by construction. The
  phrase "product lifetime" occurs zero times in every one of the 16 hashed
  pharma primary texts under `inputs/20260905-arnaud/prep/pharma/sources/`;
  the retention provisions those instruments do carry (EU GMP Chapter 4
  §4.11, 21 CFR 211.180(a)) are batch-linked and differently expressed, and
  do not state this figure. No replacement citation is asserted, because
  attributing the figure to a provision that does not state it would be a
  guess. The clause now records, in the same sentence as the claim, that
  the period is not sourced to any instrument and must not be relied on;
  the correct source and the correct figure remain not signed off.
- **`domains/pharma.md` — "15 years for clinical data (21 CFR Part 312)"
  corrected to Part 312's actual two-year periods.** 21 CFR Part 312 was
  retrieved from eCFR on 2026-09-05 (text as in force 2026-08-31) and hashed
  at `inputs/20260905-arnaud/prep/q11-federal/sources/21cfr-part312.xml`.
  Part 312 states no 15-year period: `"15 year"` occurs zero times in it, and
  the negative control `"2 years"` hits the same file, so the zero is an
  absence and not a broken search. The retention periods Part 312 does state
  are two years, anchored to a marketing-application event, at §312.57(c)
  (sponsor), §312.62(c) (investigator) and §312.120(d) (foreign studies not
  under an IND). The clause now quotes §312.57(c) and cites the two other
  sections. No origin is asserted for the 15-year figure, because attributing
  it to an instrument that was not opened would repeat the fault being
  corrected. Prepared at primary, unsigned — `T6.3` cl. 5 discharges nothing:
  `inputs/20260905-arnaud/prep/q11-federal/q11_federal_packet.md`.
- **`domains/pharma.md` — the GMP retention caveat was checked against
  21 CFR 211.180 and kept, not removed.** §211.180(a)-(f) was read in full at
  primary. (a) and (b) set the only two periods in the section — "at least
  1 year after the expiration date" of the batch, or 3 years after
  distribution for the OTC products exempt under §211.137 — and both are
  batch-linked; (c) governs availability during the retention period, (d) the
  permitted record form, (e) the at-least-annual product review (a review
  cadence, not a retention period) and (f) notification of responsible
  officials. Nothing in (a)-(f) expresses a period as a function of product
  lifetime, and `"product lifetime"` occurs zero times in Part 211. The
  caveat is therefore correct as written and is left byte-identical; only
  the connective clause outside its brackets was repaired, because the
  correction above rewrote the sentence it hung from. An honest unsourced
  marker is better than a source that does not carry the figure.
- **`domains/aviation.md` — FAA Order 8110.49 was cited for a documentation
  requirement it does not contain.** The paragraph asserted that "Software
  approval under FAA Order 8110.49 requires documentation of the software's
  intended function, its operating environment, and its relationship to the
  airborne system's safety objectives" and routed that documentation into the
  PSAC. FAA Order 8110.49A, *Software Approval Guidelines*, effective
  29 March 2018, was retrieved from faa.gov on 2026-09-05 and
  hashed at
  `inputs/20260905-arnaud/prep/q11-federal/sources/faa-order-8110.49.pdf`.
  In it the word "intended" occurs zero times and "PSAC" occurs zero times,
  with live negative controls in both cases. Its Ch. 1 §1 *Purpose* states
  that the order "guides Aircraft Certification Service (AIR) offices and
  designees on how to apply RTCA/DO-178B and RTCA/DO-178C" — it directs FAA
  staff and designees rather than imposing a documentation duty on an
  applicant — and §4-§5 record that it cancelled Order 8110.49 Chg 2 and that
  Chg 2's Chapters 5-16 were deleted, leaving a software review process, a
  software conformity inspection and the level-of-involvement worksheets.
  PSAC content is specified by RTCA/DO-178C §11.1, a paid RTCA standard that
  was not retrieved and is OPEN under `T6.5`; no unofficial copy was fetched,
  sought or considered. The paragraph now states what the order governs and
  attributes the PSAC obligation to DO-178C. Same shape as the FDA CSA
  finding at `T6.3.q7`: the instrument exists, the locator resolves, and the
  duty it was cited for is not in it.

- **Solvency II "Article 120" corrected to Article 124 for internal-model
  validation, and the "annual" validation cycle withdrawn as unsourced.**
  `domains/insurance.md:207` (prose) and `:274` (the Layer 4 control-mapping
  table) both attributed ongoing internal-model validation to Solvency II
  Article 120 and both described the obligation as an *annual* validation
  cycle. Directive 2009/138/EC was read at the hashed primary
  `inputs/20260905-arnaud/prep/domain-files/sources/sii.html.gz`, sha256
  prefix `1e6a28843ac3`, through the same `normalizeForMatch` normalisation
  `tools/citation-consistency.mjs` applies. **Article 120 is *Use test*** —
  it requires the undertaking to demonstrate that the internal model "is
  widely used in and plays an important role in their system of governance",
  and it is Article 120, not 124, that makes the administrative, management
  or supervisory body "responsible for ensuring the ongoing appropriateness
  of the design and operations of the internal model". **Validation is
  Article 124, *Validation standards***, which requires undertakings to
  "have a regular cycle of model validation which includes monitoring the
  performance of the internal model, reviewing the ongoing appropriateness of
  its specification, and testing its results against experience", together
  with a statistical validation process, stability and sensitivity analysis,
  and "an assessment of the accuracy, completeness and appropriateness of the
  data used by the internal model". Every one of those quotations was
  byte-compared and HIT once; each carries a one-word-swap negative control
  that MISSed, and the article headings "article 124 validation standards"
  and "article 120 use test" both HIT as positive controls.
  **Two faults, not one.** The article was wrong, and the cadence was
  fabricated: across the whole 1,117-character span of Article 124 the tokens
  `annual`, `year`, `yearly`, `frequency`, `independen`, `board` and
  `backtest` each occur **zero** times, with `regular cycle` occurring once —
  a demonstrated absence, since the same search returns the article's own
  words from the same span. Article 124 prescribes **no interval at all**.
  Following `F2`, the annual cadence is not deleted and not footnoted: it is
  now stated **in the same sentence as the claim** as a policy-set choice
  with no provision behind it, so the caveat cannot be stripped by quotation.
  The same treatment was applied to two further requirements the paragraph
  attributed to the article and the primary does not carry — that validation
  be independent of the model development function, and that it produce a
  formal report to the board; independence is re-stated as a policy-set
  control, and board reporting is re-attributed to the Article 120 duty of
  the administrative, management or supervisory body. "Backtesting" was
  likewise re-worded to Article 124's own phrase, "testing its results
  against experience", because `backtest` occurs zero times in the primary.
  **This defect is the reason a disagreement check nearly missed it.**
  `aplc/domains/insurance.md:124` carries the identical error — same article,
  same fabricated cadence — so the two sites **agree with each other and are
  both wrong**, and a heuristic that reports conflicts is blind to that by
  construction. It would be filed under `AGREE` and suppressed. Any
  adjudication table built over `tools/citation-consistency.mjs` §2 therefore
  needs a **`BOTH_WRONG_SAME_WAY`** class, as the `T6.3.q9.1` census
  recommends. The `aplc` twin belongs to another custodian and was **read but
  not edited**; this correction was written to converge on the primary's own
  identifiers — Article 124, *Validation standards*, "a regular cycle of
  model validation" — so that the two files describe one provision the same
  way whatever wording the other custodian chooses.
- **GDPR Article 12(3) response periods — checked across `asdlc/` and found
  absent; no correction was made here because there is nothing here to
  correct.** The corpus renders Article 12(3) as "30 calendar days" with a
  "60-day extension"; Regulation (EU) 2016/679 at the hashed primary
  `inputs/20260905-arnaud/prep/domain-files/sources/gdpr.html.gz`, sha256
  prefix `9952f3f336d4`, says the controller shall act "without undue delay
  and in any event **within one month** of receipt of the request", and that
  "that period may be extended **by two further months** where necessary".
  Both quotations HIT once; "within 30 days of receipt of the request" and a
  one-word-swap control both MISSed. **A month is not 30 days**, and a
  compliance deadline stated in the wrong unit is wrong in a way a reader
  acts on. The two live sites were enumerated by command rather than taken
  from a handover count —
  `grep -rIn --include='*.md' '12(3)' . | grep -v '/inputs/'` and a second,
  wider sweep over every non-`inputs/` Markdown line mentioning GDPR
  alongside a day-or-month figure — and both resolve **outside this repo's
  scope**: `agentic-engineering-manifesto/operational-templates/slo-table.md:71`
  and `aplc/agent/agent-maintenance.md:358`. All 22 GDPR-bearing lines in
  `asdlc/` were then read individually; none states an Article 12(3) response
  period. **Zero sites in `asdlc/`** — a demonstrated zero, not an unrun
  search. Recorded here so the finding is not lost when the other two
  custodians' repos are reviewed.
- **D-57 · "SR 11-7 requires … seven years" was an obligation attributed to an
  instrument that states no such thing; the seven years are now marked
  policy-set in the sentence that carries them, at all three sites in this
  repository.** The figure stood in `maintenance-governance.md` (the
  decommission retention paragraph) and twice in
  `domains/financial-services.md` (the GDPR Article 17 conflict-resolution
  section and its specification-artefact category), and the estate contradicted
  itself: `aplc/governance/observability.md` already adjudicates the same
  number as *"a policy-set seven years … no instrument setting that period"*.
  That file was **read but not edited** — it belongs to another custodian —
  and this correction was written to converge on its wording so the two do not
  diverge again. The attribution is not merely unsourced, it is **falsified at
  primary**: SR 11-7 and its attachment are on disk at
  `inputs/20260905-arnaud/prep/D-20-primary/sources/` (`sr1107.pdf`,
  `sr1107a1.txt`, sha256 `d8ef343917…`), and over the normalised text
  `retention` → **0**, `seven years` → **0**, `7 years` → **0**, `retain` → **1**
  (unrelated, on retaining *vendor models*). Positive controls on the same
  text: `should` → **180**, `must ` → **1**, `model risk management` → **50**;
  negative control `zebra risk management` → **0**; the cover letter separately
  gives `model risk` → **28**, `retention` → **0**, `zebra risk` → **0**. The
  guidance register is the corpus's already-held position (`D-02`/`D-06`,
  `asdlc.md` and the SR 11-7 entry above): supervisory guidance written in
  *"should"*, and SR 26-2 (17 April 2026) states *"This guidance does not set
  forth enforceable standards or prescriptive requirements"*. **Whether SR 26-2
  rescinds SR 11-7 remains NOT REACHED**, and nothing here turns on it.
  **No control was deleted** — the seven-year retention still governs
  decommission; only its attribution changed.

- **D-57 · "24 hours for early warning obligations under DORA or NIS2" —
  DORA has no early-warning obligation, and NIS2 was retrieved rather than
  left declared.** At `operations/governance.md` (security-incident Step 4).
  Over the DORA primary at
  `inputs/20260905-arnaud/prep/asdlc-standards/sources/dora_fulltext.txt`,
  normalised: `early warning` → **1**, the sole occurrence being Article
  17(3)(a) *"put in place early warning indicators"* — an internal detection
  control, **not a duty to warn an authority**. `24 hours` → **0**,
  `4 hours` → **0**, `hours` → **1**, and that one occurrence is in **Article
  15, point (b)** (the RTS mandate), not Article 9(4)(c) as an earlier note
  had it — read to its enclosing heading, not pattern-matched. Positive
  controls `notification` → **30**, `early` → **15**, `warning` → **3**;
  negative control `zebra warning` → **0**. **The Regulation sets no reporting
  clock at all**: Article 19(4) submits the initial notification, intermediate
  report and final report *"within the time limits to be laid down in
  accordance with Article 20, first paragraph, point (a), point (ii)"* — the
  delegated technical standards. The DORA Article 19 paragraph in the same
  file, which had the initial-notification timeframe *"set by the competent
  authority"*, is corrected to say so.
  **NIS2 is now on disk.** *"Not on disk" was a fact about this repository,
  not about reachability* — the Directive is free on EUR-Lex and one request
  fetched it: `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555`,
  **HTTP 200 on the first attempt** with `curl --compressed` (the flag was
  carried over from the `T-nispom` HTTP 406, which was an API precondition
  rather than an access refusal; EUR-Lex imposed no such precondition and
  nothing was swallowed), retrieved 2026-09-06, 704,490 bytes, sha256
  `95ac28172dc9766b1c964a38d56bdf47d4c6cb8226e1dbee8b079a97325fe8ac`, stored
  with its provenance at `inputs/20260905-arnaud/prep/nis2/sources/`.
  Article 23(4) read: **(a) early warning within 24 hours of becoming aware**,
  **(b) incident notification within 72 hours**, **(d) final report not later
  than one month after the submission of the notification under point (b)** —
  one month from the 72-hour notification, **not from awareness**, as this
  file had it. Reporting runs to *"the CSIRT or, where applicable, the
  competent authority"*, not to the competent authority alone; and NIS2 binds
  *"essential and important entities"* (**69** occurrences) — *"operators of
  essential services"* (**4**, in the NIS1-repeal material) is NIS1 vocabulary
  and was describing the wrong scope. NIS2 is a Directive, so the duties reach
  an entity through national transposition; that is now said in the sentence.
  Negative controls `zebra warning` → **0**, `zebra month` → **0**.
  **One checker artefact this correction creates, declared rather than left
  silent.** `tools/citation-consistency.mjs` has **no NIS2 entry in its
  `INSTRUMENTS` list**, and its attribution rule is last-named-instrument with
  a 20-line carry-forward reset only by a heading. The new `Article 23(4)(a)`,
  `(b)` and `(d)` citations therefore inherit **DORA** from the preceding
  `**DORA Article 19.**` paragraph and are reported as *"DORA Art. 23 — 5
  site(s), not checked"* (was 4 before this edit; `sub-clause citations
  checked` 497 → 498, `no structure data` 38 → 39). **They are NIS2's, not
  DORA's.** The citations are kept because a reader needs the division, and
  the misattribution is recorded here because the fix is an `INSTRUMENTS`
  entry in `tools/`, which is outside this pass's write scope. Nothing was
  suppressed to make the count look better: `fabricated` stays **1** (the
  known Solvency II case) and `truly new` stays **0** across two runs.

- **What this pass did not close — two shapes enumerated across `asdlc/`,
  recorded with their counts rather than worked.** Both were run over
  paragraph **blocks** (soft wraps joined, hard breaks ending the block) so a
  claim spanning a line break is one unit, with the sentence splitter
  protected against `Art.`, `No.`, `para.` and the like; `errata.md` is
  excluded from the counts below, being commentary rather than assertion.
  - **70** sentences name **DORA, NIS2 or SR 11-7 with no division locator in
    the same sentence** — 32 DORA, 43 SR 11-7, 1 NIS2 (a sentence may name
    two). **Eleven of the 32 DORA hits are the DevOps research programme of
    the same name** (*Accelerate State of DevOps Report*, `dora.dev`) —
    `README.md:427, :508`, `asdlc-guide.md:28, :553, :555, :576` (×3),
    `asdlc.md:639, :641` (×2) — a homonym, not the Regulation, and not a
    defect. **Twenty-one refer to Regulation (EU) 2022/2554**, and those in
    `domains/` and `release-governance.md` mostly sit within a paragraph that
    does carry an Article locator; none was read one by one here. **Eight**
    of the SR 11-7 hits are *"SR 11-7 requires / expects / does require …"*:
    `domains/financial-services.md:26, :128, :224, :299, :388, :409, :477`
    and `release-governance.md:1219`. They carry the **same defect this entry
    corrects for retention**, on the same primary — guidance written in
    *"should"*, `should` **180** against `must ` **1** — and are **flagged and
    left open**, not silently amended, because each needs its own reading of
    the provision it paraphrases.
  - **91** are **bare declaratives**: a regulatory anchor plus a duty or act
    verb, with **no modal and no risk-status word** — the blind spot the sweep
    at `inputs/20260905-arnaud/status/T6.3.q14.md` named, and the shape no
    modal-keyed matcher sees. They concentrate in
    `domains/financial-services.md` (24), `release-governance.md` (11),
    `domains/insurance.md` (10) and `domains/pharma.md` (9). **The sharpest
    thing in the set is an internal contradiction this repository has not
    noticed:** `asdlc.md` states that IEC 62304 and GAMP 5 are *"paid
    standards that this programme has not purchased and has not read;
    **nothing here asserts what they require**"* — and **ten** bare
    declaratives assert exactly that, at `domains/pharma.md:20, :78, :91,
    :111, :142, :200` and `release-governance.md:1229` (×2), `:1252` (×2).
    Neither standard is on disk, so the ten cannot be checked; the
    contradiction needs no primary. **Not corrected here** — it is a
    different finding from the two above and belongs to whoever works
    `T6.5`.

- **Eight sites said "SR 11-7 requires / expects"; SR 11-7 requires nothing.
  Twelve sites are now corrected, not eight.** The primary is on disk —
  `inputs/20260905-arnaud/prep/D-20-primary/sources/sr1107a1.txt` (sha256
  `d8ef34391721ee72be28b8cb288c0222621637eb585c4af9c5149ffecc8d57af`, verified
  this pass) with `sr1107.pdf` (sha256 `e0fa7b09…`). Re-derived, not inherited:
  `should` **180**, `must ` **1**, `retention` **0**, `seven years` **0**,
  `7 years` **0**, `retain` **1** (vendor-model selection, unrelated);
  `requir*` **7**, and **none of the seven places a requirement on a bank by
  force of this document** — they are the 12 CFR advanced-approaches capital
  rules, a bank requiring things of *its vendors*, and a bank's policies
  requiring documentation of themselves. Also **0**: `nature of the change`,
  `testing performed`, `continuous`, `fit-for-purpose`, `fit for purpose`,
  `quarterly`. Negative controls `nature of the changee`, `conceptual
  soundnesss`, `seven yearss`, `77 years`, `retentionn`, `zebra retention`,
  `zebra should`, `zebra inventory` all **0**; positive controls `should` 180,
  `model risk management` 145 (both files), `validation` 224, `conceptual
  soundness` 3, `model inventory` 2, `at least annually` 1 all non-zero. With
  **SR 26-2** (17 April 2026) stating that it *"does not set forth enforceable
  standards or prescriptive requirements"*, and this repository already holding
  that position at `D-02`/`D-06`, **"requires" and "expects" were wrong on the
  corpus's own record.**
  **What was done:** at each site the verb and the attribution were corrected
  and **no control was deleted**. Where SR 11-7 does say something, it is now
  quoted in its own register — that a validation framework *"should include
  three core elements: • Evaluation of conceptual soundness, including
  developmental evidence • Ongoing monitoring, including process verification
  and benchmarking • Outcomes analysis, including back-testing"*; that
  *"Comparison to alternative theories and approaches should be included"*;
  that *"Documentation of model development and validation should be
  sufficiently detailed so that parties unfamiliar with a model can understand
  how the model operates, its limitations, and its key assumptions"*; that
  *"Material changes in model structure or technique, and all model
  redevelopment, should be subject to validation activities of appropriate
  range and rigor before implementation"*; that *"Computer code implementing
  the model should be subject to rigorous quality and change control
  procedures … that all changes are logged and can be audited"*; that banks
  *"should maintain a comprehensive set of information for models implemented
  for use, under development for implementation, or recently retired"*; that
  *"Validation activities should continue on an ongoing basis after a model
  goes into use"*; and that banks *"should conduct a periodic review—at least
  annually but more frequently if warranted—of each model"*. Where it says
  nothing, the claim is marked **the ASDLC's own construction and unsourced**
  in the same sentence: the pre-build *sequencing* of conceptual-soundness
  documentation; the phrase "fit-for-purpose"; the three-part change record
  (nature of change / testing performed / validation results); reading
  "ongoing" as **continuous** monitoring; the 100% trace-completeness floor;
  the quarterly review cadence (which exceeds the annual floor the guidance
  describes); the release gate as the moment of inventory update; and that the
  gate conditions are a sufficient governance structure.
  **The handed-over count of 8 was low.** A wrap-safe re-enumeration
  (`command grep -rlEz --include='*.md' 'SR[[:space:]]+11-7…'` plus a
  normalised whole-file scan, dashes mapped to spaces before matching) found
  **61** SR 11-7 mentions of which **32** sit within 220 characters of a
  duty verb, and **12** were the defect: `domains/financial-services.md`
  Layer 1 framing sentence, the conceptual-soundness section (three
  paragraphs), the Layer 1 table row, the model-change section (three
  paragraphs), the Layer 3 table row, the ongoing-monitoring section and its
  three bullets, and the Layer 4 table row — the seven the sweep listed, plus
  the framing sentence at Layer 1 and the "must include" list at the release
  boundary — together with `release-governance.md` (the SR 11-7 paragraph),
  `maintenance-governance.md` (patch-governance mapping, *"its requirement for
  ongoing model performance monitoring"*), `deployment-governance.md`
  (environment isolation *"under DORA and SR 11-7"*, where DORA binds and
  SR 11-7 does not), and `asdlc-guide.md` (*"Both require: …"* and *"both
  frameworks require …"*). The sweep's `:477` is `:478`; its list omitted the
  last four files. A standing **Note on SR 11-7's register** now heads
  `domains/financial-services.md` so the sites can stay terse.
  **`asdlc-guide.md` also asserted what SS1/23 requires. SS1/23 is not on
  disk** — the file found under `D-47-primary` is PRA **SS1/21**, a different
  supervisory statement — so the sentence now says that nothing here states
  what SS1/23 says. **Nothing here is signed. A model cannot sign, and a
  paywall is never a closure.**

- **Ten declaratives asserted what IEC 62304 and GAMP 5 require, against this
  repository's own disclaimer; nineteen sites are now made consistent.**
  `asdlc.md` states that they are *"paid standards that this programme has not
  purchased and has not read; nothing here asserts what they require."*
  **This is a corpus-internal contradiction and needed no primary to resolve —
  and could not have used one:** both remain **OPEN under `T6.5`**, **no
  unofficial copy was fetched, sought or considered**, and **what they require
  was not checked, because it cannot be.**
  **What was done:** the content was retained and the attribution withdrawn —
  the same shape used tonight for the GMP retention period. `domains/pharma.md`
  gains a standing **Note on GAMP 5 and the paid standards**, and its ten GAMP 5
  sites (`:20`, `:56`, `:75`, `:78`, `:91`, `:111`, `:118`, `:142`, `:200`,
  `:206` at the pre-edit numbering) now read as what **the ASDLC understands**
  the industry-common qualification vocabulary (URS, IQ, OQ, PQ, change
  control, periodic review) to mean — its own construction, unsourced. The
  headings changed with them (*"GAMP 5 Installation Qualification (IQ)"* →
  *"Installation Qualification (IQ)"*), because a heading that names the guide
  is itself an attribution. `release-governance.md`'s IEC 62304 and GAMP 5
  blocks and `asdlc-guide.md`'s IEC 62304 and GAMP 5 blocks carry the same
  marking, including the IEC 62304 clause numbers (5.1–5.7, 5.2, 5.6, 5.7),
  which are **reproduced from secondary usage and have not been checked against
  the standard**; the Class C independent-verification claim is now stated as
  the ASDLC's own rule for its highest risk class rather than as IEC 62304's.
  `deployment-governance.md`'s *"under GAMP 5 and IEC 62304, staging must use
  validated test data sets"* is marked the same way. **No control was deleted:**
  every qualification step, every gate mapping and every retention obligation
  still stands as an ASDLC control; only the claim that a paid standard demands
  it has been withdrawn. Where a claim cannot stand without the standard, the
  sentence says so and directs the reader to confirm against a purchased copy
  with the organisation's quality team.
  **The handed-over count of 10 was low**, on the same pattern as Family 1: a
  normalised scan for `GAMP 5|IEC 62304|DO-178C` followed by a duty verb found
  the six pharma sites and the four release-governance assertions the sweep
  listed, plus `domains/pharma.md:56`, `:75`, `:118`, `:206`,
  `asdlc-guide.md`'s two blocks and `deployment-governance.md:84`. Residual
  scan after the edits returns only the negated forms (*"Whether IEC 62304
  requires … has not been checked"*, *"nothing here states what GAMP 5
  imposes"*). **DO-178C carries the same defect in `domains/aviation.md` and
  `asdlc-guide.md` and was NOT corrected in this pass** — `asdlc.md`'s
  disclaimer names only IEC 62304 and GAMP 5, `domains/aviation.md` already
  marks DO-178C § 11.1 as OPEN under `T6.5`, and extending the disclaimer is a
  separate decision. **It is flagged here, not fixed.**

- **Checker state for the two entries above.** `./tools/link-check.sh` broken
  **4** / total 1043, unchanged. `./tools/register-crossref.sh` **PASS**.
  `asdlc/tools/check-gate-counts.sh` — *"all checked mentions agree with their
  authoritative count."* `node tools/citation-consistency.mjs` run **twice,
  byte-identical**: **truly new 0**, **sub-clause fabricated 1**, **pairs 71**
  — the same 71 as before this pass, so **no net pair movement**, and none of
  the six `asdlc/` pair lines cites text written here (they are EU AI Act
  Art. 9, DORA Art. 24, MiFID II Art. 17, DORA Art. 11 and GDPR Art. 35 rows in
  sections not touched). One movement is explicitly **not** mine: *no structure
  data* fell **39 → 35** and *sub-clause citations checked* stands at **498**,
  because another agent added the **NIS2** entry to
  `tools/citation-consistency.mjs` concurrently — `tools/` is outside this
  pass's write scope and was not touched. These entries are written to a file
  that is **untracked under `D-57`, so `git -C asdlc diff` does not show them;
  they were written anyway and this line says so.**

### D-57 residuals — SS1/23 at primary, DO-178C, and the NIS2 soft wrap (2026-09-06)

- **SS1/23 — the claim rested on a document that is not the one on disk, and the
  document that is has now been read.** `asdlc-guide.md` asserted that SS1/23 is
  the UK counterpart to SR 11-7 and, in the same breath, that SS1/23 "was not
  retrieved and is not on disk; nothing here states what it says". The
  not-on-disk half was true of this repository and **false as a statement about
  reachability**. **What is actually at `inputs/20260905-arnaud/prep/D-47-primary/`
  is `pra-ss1-21.pdf`** (sha256 `a7fc20c65f…`), whose own title block reads
  *"Supervisory Statement | SS1/21 — Operational resilience: Impact tolerances
  for important business services, March 2021"*, superseded-stamped on every
  page toward SS1/22. **It is an operational-resilience statement, not a
  model-risk statement.** `SS1/2` is a string prefix of both `SS1/21` and
  `SS1/23`; the two were separated on the whole token and on the title block.
  **SS1/23 is free on bankofengland.co.uk and was retrieved at HTTP 200 on the
  first attempt** (`curl --compressed`, no non-200 at any point, URL
  corroborated against the BoE landing page, document fetched twice and the two
  downloads byte-identical), and is held at
  `inputs/20260905-arnaud/prep/ss123/sources/pra_ss1_23.pdf`, sha256
  `6165a8ba699e9c7ffb6a693711f6a07b555021aa823e1a79582d9bc2e8052de7`, with
  `SOURCES.md` and `SHA256SUMS.txt` to the NIS2 convention (`shasum -c` → OK,
  exit 0). **The claim checks out and is now sourced rather than assumed:**
  SS1/23 is PRA *Model risk management principles for banks*, May 2023, in
  effect 17 May 2024 — genuinely the UK model-risk counterpart. **It is in the
  same register as SR 11-7:** `should` **179**, `must` **0**, `shall` **0** over
  the whole document (positive control `the` **647**; negative controls
  `zebra should`, `zebra requires`, `shoulds`, `musts`, `requiress` all **0**),
  and § 1.1 says it *"sets out the PRA's expectations"*. Its **scope is narrower
  than SR 11-7's** — § 1.2 confines it to firms with internal model approval and
  excludes credit unions, insurers and reinsurers — and that is now stated.
  `operations/governance.md:500` was read and left alone: it says compliance
  floors "may" apply and tells the reader to confirm, so it asserts nothing
  about SS1/23.

- **DO-178C — the same defect as IEC 62304 and GAMP 5, now closed the same way.**
  **DO-178C is a paid RTCA standard. It was not purchased, and no unofficial
  copy was fetched, sought or considered. It stays OPEN under `T6.5`. What it
  requires was not checked, because it cannot be.** The fix is the one already
  applied 19 times to the other two families: **content retained, attribution
  withdrawn in-sentence**, matching that wording so the families do not diverge.
  **Enumeration: the wrap-safe `grep -rlEz` with a duty verb adjacent found
  ONE file** (`domains/aviation.md`); the **normalised whole-file scan — dashes
  mapped to spaces, whitespace collapsed, a 220-character window after each
  `DO 178C` tested for a duty verb — found 59 mentions and 39 duty-verb
  mentions across FOUR files**: `domains/aviation.md`, `asdlc-guide.md`,
  `release-governance.md` and `asdlc.md`. **The brief named two. The narrow grep
  found one. Both were low, for the third and fourth time tonight.**
  `release-governance.md` is the sharpest case: its **Aviation block sat
  directly between the Medical-devices and Pharmaceutical blocks that the
  previous pass fixed**, and was left asserting *"DO-178C … establishes software
  release requirements that include …"*. **15 sites were corrected** — 13 in
  `domains/aviation.md` (traceability at the demand boundary, § 5.1, DAL
  determination, PSAC content, § 7 configuration management, lifecycle data, the
  SAS "primary document" claim, § 6.4 independence, the "not DO-178C compliant"
  verdict, § 12.1 delta approach, § 7.3, § 7.2 problem reporting, and the
  lifecycle-data retention heading), one block in `asdlc-guide.md`, one block in
  `release-governance.md` — plus a standing **Note on DO-178C's register** at the
  head of `domains/aviation.md`. Every section number is now marked as
  reproduced from secondary usage and **not checked against the standard**.
  **Controls deleted: 0.** Every traceability rule, DAL gate, configuration
  identifier, independence condition, problem-reporting process and retention
  obligation still stands as an ASDLC control; only the claim that DO-178C
  demands it was withdrawn. Two compliance *verdicts* were downgraded to
  ASDLC-condition failures with the certification determination handed back to
  the certification authority, which is a correction, not a deletion.

- **`asdlc.md`'s disclaimer now names DO-178C, and that is an editorial
  judgment.** It read *"**IEC 62304** and **GAMP 5** are paid standards that this
  programme has not purchased and has not read; nothing here asserts what they
  require."* It now names **DO-178C** alongside them. **Why:** the disclaimer's
  own predicate is true of DO-178C without qualification — paid, unpurchased,
  unread, already OPEN under `T6.5` — and `asdlc.md`'s own next section is
  headed *"Regulated SDLC frameworks (IEC 62304, GAMP 5, DO-178C)"*, so the
  document already groups the three everywhere except in the one sentence that
  does the work. **The gap in the named scope is precisely what let fourteen
  DO-178C assertions stand while the other two families were being corrected**;
  leaving it would guarantee the same divergence next time. The narrower reading
  — that the disclaimer should be left as the previous pass found it — was
  rejected because a disclaimer that omits a standard it is true of is not
  conservative, it is silent.

- **NIS2 / DORA soft wrap — fixed in prose, not in the extractor.**
  `operations/governance.md` carried a genuine NIS2 citation attributed to DORA
  because *"…the NIS2"* ended one line and `Article 23(4)(a)` began the next,
  with **DORA** named later on that same line, so the extractor's
  nearest-name-on-line rule beat the carry-forward. **The NIS2 pass declined to
  patch the extractor, on the ground that loosening that rule previously
  manufactured hundreds of false disagreements and that this defect degrades to
  a declared NO_DATA and never to an accusation. That judgment stands and was
  not revisited.** The sentence was rewrapped so `NIS2 Article 23(4)(a)` sits
  whole on one line and `**DORA creates no early-warning obligation**` begins the
  next. **Measured, not asserted: `DORA Art. 23 — 1 site(s), not checked` → the
  row is gone (1 → 0), NIS2 triples 4 → 5, DORA triples 238 → 237, sub-clause
  OK 462 → 463 and *no structure data* 35 → 34** — the citation is now checked
  against the NIS2 primary and passes. Nothing else in DORA's or NIS2's prose
  changed.

- **Checker state for the entries above.** `node tools/citation-consistency.mjs`
  run **twice, byte-identical**. **Baselines held: disagreeing pairs 71 ·
  refused 17 · sub-clause fabricated 1 · truly new (unadjudicated) 0.**
  `./tools/link-check.sh` broken **4** / total 1043, unchanged.
  `./tools/register-crossref.sh` **PASS**. `asdlc/tools/check-gate-counts.sh` —
  *"all checked mentions agree with their authoritative count."*
  **Movement isolated by masking rather than asserted:** the rewrap was reverted
  in place, the checker re-run, and with it masked **the only movement from all
  the prose edits in this pass is `quoted spans detected` 2694 → 2700 (+6, the
  six spans newly quoted here), all six unattributed — attributable stays at
  597 and every other counter is at baseline.** So the whole of the DORA/NIS2
  movement above belongs to the one-paragraph rewrap and to nothing else. The
  rewrap was then restored and the report **diffed to zero** against the
  pre-mask run. One drift was caught and removed on the way: an earlier draft of
  the SS1/23 paragraph put *"SR 11-7"* within six lines of the new SS1/23
  quotations, carrying them onto `SR_11_7` (unchecked 56 → 57); the phrase was
  reworded to *"the US guidance"* and the count returned to 56.
  **Nothing here is signed. A model cannot sign, a paywall is never a closure,
  and neither is an unfetched free primary — which is why SS1/23 was fetched.**
  These entries are written to a file that is **untracked under `D-57`, so
  `git -C asdlc diff` does not show them; they were written anyway and this line
  says so.**

### D-57 · `domains/financial-services.md:540` — "DORA reporting timelines": a clock the Regulation does not fix

- **Struck.** *"This mapping must be documented before the system goes to
  production to ensure **DORA reporting timelines** are met for material
  incidents."*
- **Why.** DORA fixes no reporting timeline. Art. 19(4) requires the initial
  notification, intermediate report and final report *"within the time limits to
  be laid down in accordance with Article 20, first paragraph, point (a), point
  (ii)"* — **1** at the hashed DORA primary (sha256 prefix `25328c7e39c4`,
  303,607 normalised chars through the checker's own `normalizeForMatch`) — and
  Art. 20 first paragraph point (a)(ii) directs the ESAs to *"determine the time
  limits for the initial notification and for each report referred to in
  Article 19(4)"* (**1**). The commonly cited figures are absent, in **both digit
  and word form**: `4 hours` **0** · `four hours` **0** · `72 hours` **0** ·
  `seventy two hours` **0** · `1 month` **0** · `one month` **1**, and that one
  is Art. 31(5), read in context and not a reporting clock. Positive controls
  `time limits` **3** · `exit strategies` **5** · `termination rights` **3**;
  negative control `zorkmid frotzwibble` **0**.
- **The RTS, named, and the version recorded.** The instrument is **the RTS
  adopted under DORA Article 20, first paragraph, point (a)(ii)**, named by its
  empowering provision because **the corpus nowhere carries a verified Commission
  Regulation number for it** — a corpus-wide normalised scan returns **0** for
  any such number, and inventing one would be the D-60 fabrication shape this
  register exists to prevent. The corrected cell therefore requires the
  **version relied on to be recorded** at the point of use, which is where the
  binding period actually becomes checkable.
- **Converged with the other two repos, deliberately.** The corrected wording
  reuses the form already agreed in AEM `operational-templates/slo-table.md`
  rows 18-20 — *"firm operating target (`F2`), not a DORA Article 19 deadline"*
  and *"the period is set by the RTS under Art. 20, first paragraph, point
  (a)(ii) — record the version relied on"* — and matching `aplc/aplc-guide.md`.
  The converged form now stands at this cell as well as at the two sites named
  above; **no cross-repo total is recorded for the locator string**, because the
  sentence recording the convergence carries that string and any such search
  would count this note along with the sites it describes.
  **Note on the brief that requested this:** the brief attributed to AEM a
  phrase describing where the binding period genuinely resides. That is not
  AEM's wording, and when the brief was checked the phrase was not found in the
  corpus. It is deliberately **paraphrased rather than re-quoted here**: writing
  such a phrase down is precisely what makes it present, and a note asserting
  that a string is absent while carrying that string documents the defect
  instead of recording it. The wording converged on is the one quoted above,
  re-derived from the file rather than inherited.
- **Why this one was still open.** The AEM Art. 19/20 correction landed in AEM
  and in `aplc/aplc-guide.md:298` but **not here** — this cell was the last
  carrier of the implied clock, and it survived because it never named a figure,
  only the word "timelines". A sweep scoped to the absent figures could not
  reach it.
- **This file is untracked under `D-57`, so `git -C asdlc diff` does not show
  this entry. It was written anyway and this line says so.**

---

[← Back to README](README.md)
