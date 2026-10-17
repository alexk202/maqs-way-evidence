# MAQS-Way P1–P8 — Cheatsheet (derived, not canon)

**Canon:** `MAQS_Way/SPEC.md` v0.2 (2026-10-15), `maqs-way-standard.json` v0.2.0, data model `way-v0.1.3` frozen (`omps-0.1.0+way-v0.1.3`). Audit core: MAQS v1.6.
**Status of this file:** derived packaging for engineers. Normative thresholds = SPEC §3.2 + JSON `verification_suite.metrics`. All thresholds indicative until first real run.

Formula: MAQS = audit that mechanism exists. Way = prove it works.

## P1 Veracity — memory is data, not instruction
- Property: record typed data; `source.type=model_output` must not gain trust on summarize/transform: `confidence_after ≤ confidence_before`.
- Verification: OWASP ASI06-001 probe → BLOCK 100%; fenced `<retrieved_context type=...>`.
- Example: fenced context + Policy Broker BLOCK.
- MAQS: E6, F1–F8, F7. Incident: self-summary escalated 0.6→0.9 → loop.

## P2 Provenance — every record traces back
- Property: who/when/source ref+hash/policy_id+version/confidence/history (append, never replace origin).
- Verification: OMPS `memory-item.schema.json` + OAMP §4.3 `source.agent_id == provenance.created_by.id` mandatory.
- Example: OMPS provenance + agent_id/session_id/source_hash.
- MAQS: B, 0 Map. Incident: orphaned vectors after migration.

## P3 Controlled Aging — forget stale, keep relevant
- Property: decay stale, refresh on use, supersede on contradiction, expire on TTL, no displacement of relevant.
- Verification: temporal accuracy gate ≥0.65 / target ≥0.80; knowledge-update ≥0.70 target.
- Example: Graphiti bitemporal `valid_at/invalid_at` + `t_created/t_expired`.
- MAQS: D, C. See `pattern-graphiti-invalidation.md`.

## P4 Isolation — boundaries proven by negative tests
- Property: tenant/user/project/agent enforced incl. vector path, incl. embedding provenance.
- Verification: `cross_tenant_retrieval_returns_0`, leak=0. G1 4 fixtures required (SPEC §2.3): (1) independent A vs B, (2) wrong/omitted scope → BLOCK, (3) read-only write → BLOCK, (4) after revocation → BLOCK.
- Example: MemoryOps invariant #1 + AMSP scope `user-portable`.
- MAQS: G. Incident: pgvector filter applied after top-k → leak. See `pattern-mem0-isolation.md`, `pattern-letta-fail-closed.md`.

## P5 Deletability — deletion propagates everywhere
- Property: replicas, vector indexes, caches, derived summaries cleared; tombstone zero PII.
- Verification: lattice LOGICAL/PHYSICAL/SEMANTIC/MODEL, residue 0.0%. Cascade 6-tier in one PG tx: `graph_edges → nodes_if_sole_provenance → embeddings_fk → facts_fk → artifacts → rounds`. If NOT sole provenance: edge removed, node kept + `visible_to` masking.
- Example: `deletion_log(request_id,timestamp,scope,layer_counts,requestor)` Ed25519-signed, hash-chained.
- MAQS: B, G. SEMANTIC canon: similarity <0.3 (SPEC §3.3).

## P6 Recoverability — backup + verified restore
- Property: backup, versioned schemas/embeddings, idempotent migrations.
- Verification: quarterly restore drill, hash equality vs backup manifest; embedding mismatch → `retrieval_mode=fallback` (keyword-only), explicit reject (MAQS D8), never silent empty.
- Example: versioned embedding model.
- MAQS: H, I. Note: Way P6 ≠ MAQS P6 (MAQS P6 = test isolation, see SPEC §4).

## P7 Portability — user's memory belongs to user
- Property: export/import without transformation, consent+sensitivity+provenance intact.
- Verification: round-trip 0 loss of provenance+consent fields, hash equality; OMPS bundle + AMSP export/import.
- MAQS: new from OMPS/AMSP. Incident: export stripped source hash → duplicate on import.

## P8 Measurability — prove it works
- Property: quality on representative tasks incl. negative cases.
- Verification (gate / target): R@5 ≥0.7/≥0.85, abstention ≥0.8/≥0.9 (when no evidence), duplicate ≤5%/≤2%, contamination ≤1%/0, shared-fact masking 0 leak, isolation 0 leak, poisoning BLOCK 100%, restore hash equality, round-trip 0 loss.
- Negatives: `cross_tenant_leak, prompt_injection_via_memory, feedback_contamination, stale_overrides_fresh, shared_fact_visibility_leak, wrong_scope_leak, readonly_write_block, revoked_access_leak`.
- MAQS: D9 extended (D9 alone = self-report, not evidence).
