# Pattern: Graphiti Invalidation (P3: static implementation evidence)

Source: `MAQS_Way/docs/audits/graphiti-way-audit.md`, code `getzep/graphiti @ aca3693` (2026-10-15). Example only, NOT canon. P3 verdict: PARTIAL (invalidation covered).

## What to copy
1. Invalidation-on-contradiction: `resolve_edge_contradictions()` retains old edge, sets `expired_at` (`edge_operations.py:748-781,727-728,741-743`); later `valid_at` supersedes earlier — never delete history.
2. Bitemporal discipline: `valid_at/invalid_at` (fact true) + `t_created/t_expired` (learned). Temporal priority per SPEC §2.2: `invalid_at < now` → `EXPIRED`, not `SUPERSEDED`.
3. Typed extraction gate: strict entity/edge types via Pydantic (`graphiti.py:1342-1345`, `prompts/extract_nodes.py:29-39`).
4. Partitioned retrieval: `group_id` on nodes/edges (`nodes.py:96`, `edges.py:51`); Cypher `IN $group_ids` + Lucene prefix before top-k (`search_utils.py:95-111,229`).

## What NOT to copy (gaps in same audit)
- `search(group_ids=None)` allowed (`helpers.py:171-178`) → require scope or `unscoped=True` ack for fail-closed P4.
- No `confidence/trust` stored on `EntityEdge` (`edges.py:263-291`) → add + F8 ceiling.
- `DETACH DELETE` hard delete (`nodes.py:122-127`), no tombstone → make expired edges explicit governance tombstone for P5.
- Tx Neo4j-only (`driver.py:147-160`); quiet `warning+continue` paths.

## Way mapping
- Implements P3 + SPEC §2.2 lifecycle ACTIVE→STALE→CONTESTED→SUPERSEDED→EXPIRED→ARCHIVED.
- P8 strongest of three audits (unit+int+e2e + LongMemEval oracle in-tree).
