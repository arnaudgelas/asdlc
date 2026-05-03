# Graph-Lite CSV — Pilot Kit

**When to use this.** A 30-day pilot rarely justifies standing up Neo4j,
JanusGraph, or an RDF triplestore. Graph-lite is a CSV-format minimal
governance graph instance: enough nodes and edges to demonstrate ASDLC
traceability without infrastructure.

**Who fills this in.** Whoever is producing pilot artefacts — the SR Gate
fill, the release, the runbook, the evidence bundle, each becomes a node
on the graph; the relationships between them become edges.

**Deliverable.** Two CSV files:

- `graph-lite-nodes.csv`
- `graph-lite-edges.csv`

**Canonical schema authority.** `governance/graph.md`. The CSV is a
projection of the canonical schema; node and edge types MUST come from
the canonical enum lists in `governance/graph.md`.

---

## Schemas

### `graph-lite-nodes.csv`

| Column | Description |
| --- | --- |
| `node_id` | Stable unique id (e.g. `spec-001`, `release-001`). |
| `node_type` | One of the canonical node types in `governance/graph.md` (e.g. `Specification`, `Release`, `EvidenceBundle`, `Runbook`, `Waiver`, `Authority`, `Human`, `Agent`). |
| `properties_json` | JSON blob for type-specific properties (single-line, escape commas/quotes). |
| `owner` | Role accountable for the node. |
| `created_at` | ISO 8601 timestamp. |
| `content_hash` | SHA-256 of the canonical content (where applicable). |

### `graph-lite-edges.csv`

| Column | Description |
| --- | --- |
| `edge_id` | Stable unique id. |
| `edge_type` | One of the canonical edge types in `governance/graph.md` (e.g. `derives_from`, `evidences`, `signed_off_by`, `waives`, `cites_authority`, `governed_by`). |
| `source_node_id` | `node_id` of the source. |
| `target_node_id` | `node_id` of the target. |
| `created_at` | ISO 8601 timestamp. |

The CSV files in this directory ship with one row of seed sample data
each, illustrating the schema. Replace these rows with your pilot's
actual artefacts.

## How to use during the pilot

1. **Week 1 — SR Gate.** Add a `Specification` node and a `Human`
   node for the Accountable Human; add an edge `signed_off_by` from the
   spec to the human.
2. **Week 2 — Release.** Add `Release`, `EvidenceBundle`, and
   any `Waiver` nodes; add edges `derives_from` (release ->
   specification), `evidences` (evidence-bundle -> release), and
   `cites_authority` (release -> Authority) for each authority cited
   from `freshness-register.yaml`.
3. **Week 3 — Operations.** Add `Runbook` and any operational
   `Agent` nodes (per `governance/agents.md`); add `governed_by`
   edges where appropriate.
4. **Week 4 — Spot-check.** Open both CSVs in a spreadsheet or load with
   the recipe below; verify every release-stage node reaches back to a
   specification and forward to operational artefacts.

## Spot-check queries (in any tool)

Even without a graph database, the CSVs answer the canonical queries
listed in `governance/queries.md` via simple joins. Examples:

- Which authorities does release `release-001` cite? Filter
  `graph-lite-edges.csv` where `source_node_id = release-001` and
  `edge_type = cites_authority`; join target ids against the
  `Authority`-typed rows of `graph-lite-nodes.csv`.
- Which specifications lack a release node? Anti-join
  `Specification` nodes against the targets of `derives_from` edges.
- Which waivers expire within 30 days? Filter `Waiver` nodes by their
  `properties_json.expiry_date`.

## Migration to a real graph store

If the pilot succeeds and adoption proceeds, migrate the CSVs:

- **Neo4j.** `LOAD CSV WITH HEADERS FROM 'file:///graph-lite-nodes.csv'
  AS row CREATE (n {id: row.node_id, type: row.node_type, ...})`. Then
  load edges with a second `LOAD CSV` and `MATCH ... CREATE` pattern.
- **RDF triplestore.** Convert each CSV row to triples
  `<asdlc:node_id> rdf:type asdlc:node_type . <asdlc:node_id>
  asdlc:owner "owner" . ...` and edges to triples `<asdlc:source>
  asdlc:edge_type <asdlc:target> .`.

After migration, the canonical queries in `governance/queries.md`
become first-class and lint can enforce graph-level invariants on every
commit.

## Limitations of graph-lite

- No query-time index; spot-check queries scale poorly past a few hundred
  rows.
- No constraint enforcement; `node_type` and `edge_type` integrity is
  manual against `governance/graph.md`.
- No temporal queries beyond `created_at` filtering.

These limitations are acceptable for a 30-day pilot. They are NOT
acceptable for production governance; treat migration as a precondition
of adoption beyond pilot scope.
