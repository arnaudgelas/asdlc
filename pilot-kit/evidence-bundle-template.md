# Evidence Bundle Template — Pilot Kit

**When to use this.** Assembled at end of L2, satisfies RG-1 (Evidence
Bundle Complete). Referenced from the Release Gate template.

**Who fills this in.** Engineering lead with security and validation
contributors.

**Deliverable.** A directory or content-addressed archive containing every
evidence kind below, with this template as its index.

**Canonical sources.** RG-1 prose authority: `release-governance.md`.
Authority IDs cited herein come from `freshness-register.yaml`.

---

## Bundle metadata

- **Bundle ID:** `{{bundle_id}}`
- **Release ID:** `{{release_id}}`
- **Specification ID:** `{{spec_id}}`
- **Bundle content hash:** `<TODO>`
- **Created:** `{{YYYY-MM-DD}}`

---

## Evidence kinds

Each kind has a fillable section. If a kind is `not_applicable`, justify
why (tier, scope, regulatory inapplicability).

### 1. Specification + SR Gate decision

- Specification document: `<TODO link or path>`
- SR Gate template (filled): `<TODO>`
- SR Gate decision date and signing human: `<TODO>`

### 2. Source-control state

- Repository URL: `<TODO>`
- Commit hash of artefact build: `<TODO>`
- Branch / tag: `<TODO>`

### 3. Build provenance and supply-chain attestation

- SLSA level achieved: `<TODO>` (cite SLSA spec from
  `freshness-register.yaml#SLSA`)
- in-toto attestation: `<TODO link>` (cite
  `freshness-register.yaml#IN_TOTO`)
- SBOM (SPDX or CycloneDX): `<TODO link>`

### 4. Test evidence

- Unit test report: `<TODO>`
- Integration test report: `<TODO>`
- Coverage summary: `<TODO>`

### 5. Static analysis and secrets scanning

- SAST report: `<TODO>`
- Secrets scan report: `<TODO>`

### 6. Dynamic security testing (RG-6)

- DAST report: `<TODO>` or `not_applicable: <reason>`

### 7. Dependency / SCA scanning

- SCA tool + report: `<TODO>`
- Open vulnerabilities and triage status: `<TODO>`

### 8. Independent validation evidence (RG-2)

- Validator org unit and reporting line: `<TODO>` or
  `not_applicable: <phase + tier reason>`
- Validation report: `<TODO>`

### 9. Reproducibility surface

- Build inputs hash: `<TODO>`
- Training-data snapshot or version (where applicable): `<TODO>`
- Prompt-set hash (where applicable): `<TODO>`
- Random seeds / nondeterminism declarations: `<TODO>`

### 10. Foundation-model dependency record

For each foundation model used:

- Model id, version, hash: `<TODO>`
- Provider: `<TODO>`
- Drift status (no_drift / drift_within_tolerance / drift_exceeds_tolerance):
  `<TODO>`
- Re-evaluation record (if drift exceeds tolerance): `<TODO>`

### 11. Compliance mapping (RG-5)

- Authorities in scope (cite by `id` from `freshness-register.yaml`):
  `<TODO>`
- Mapping document: `<TODO>`

### 12. Rollback procedure and drill record

- Rollback procedure: `<TODO link>`
- Last drill date and outcome: `<TODO>`

### 13. Control State Record (RG-7)

- Control State Record: `<TODO link>`

### 14. Waivers (RG-8)

- Waiver IDs (each filled per `waiver-template.md`): `<TODO>`

### 15. Accountable Human sign-off (RG-4)

- Sign-off statement: `<TODO>`
- Date: `<TODO>`

---

## Bundle integrity

- Manifest file listing every artefact in the bundle with its content
  hash: `<TODO link>`
- Bundle storage location (immutable / WORM where required by regulated
  domain): `<TODO>`
