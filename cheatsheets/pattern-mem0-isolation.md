# Pattern: Mem0 Isolation (P4 exemplary)

Source: `MAQS_Way/docs/audits/mem0-way-audit.md`, code `mem0ai/mem0 @ 0724291` (2026-10-14). Example only, NOT canon. P4 verdict in audit: COVERED.

## What to copy
1. Require tenant filter: `search/get_all` demand `user_id|agent_id|run_id`, else `ValueError` (`mem0/memory/main.py:1471-1475`).
2. Apply filter before top-k: `query_filter` into vector store with over-fetch `max(limit*4,60)` (`qdrant.py:428-434`).
3. Strip spoofable keys: `_strip_identity_keys()` cuts identity from user `metadata` (`main.py:138-162`).
4. Keep history as trail: SQLite `history(old/new_memory,event,actor_id,role,is_deleted)` (`storage.py:150-191`); `created_at` survives update (`main.py:2072-2080`).

## What NOT to copy (gaps in same audit)
- No `source.type=model_output` + trust ceiling (P1 GAP).
- History queryable after delete, no tombstone (P5 PARTIAL).
- App-level md5 dedup, no UNIQUE/tx, silent `return []` paths (B PARTIAL).
- `evaluation/` empty submodule (P8 GAP in-tree).

## Way mapping
- Closes MAQS G1 fixtures (1)+(2) when enforced; add (3) read-only BLOCK + (4) revocation BLOCK to reach full P4.
- Pair with `P1-P8-cheatsheet.md` P4: leak must be 0 incl. vector path.
