# Pattern: Mem0 Isolation (P4: static implementation evidence; behavioral verification pending)

Source: `MAQS_Way/docs/audits/mem0-way-audit.md`, code `mem0ai/mem0 @ 0724291` (2026-10-14). Example only, NOT canon. P4 verdict in audit: static implementation evidence; behavioral verification pending (relabeled 2026-10-24 per the MAQS glossary terms, external reviewer feedback; maqs-way 469e237).

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

---

## Update 2026-10-26 (append-only): behavioral verification EXECUTED and PASSED

**Verdict: verified on mem0@0724291b, Linux CPU-only stub stand.**
Evidence: [MAQS_Way/evals/results/p4_mem0_isolation_report.json](https://github.com/alexk202/maqs-way/blob/main/evals/results/p4_mem0_isolation_report.json)
— the P4 behavioral test ([design](https://github.com/alexk202/maqs-way/blob/main/proposals/p4-mem0-behavioral-isolation.md),
owner-sanctioned run). All three scope keys (`user_id`/`agent_id`/`run_id`) × all read
channels (search / get_all / history messages): zero foreign items in every direction,
non-vacuous (own-count diagnostics recorded). Hostile queries (verbatim foreign fact
text): foreign = 0 AND own recall > 0 — the scope filter runs BEFORE top-k, now
confirmed behaviorally in addition to the static reading. Three controls fired on all
keys: shared-id (detector sanity), mutational (scope key dropped from the store-level
filter — the main scenario goes red), post-top-k filter mutation (own recall starved
to 0 vs the unmutated contrast > 0). **Boundaries**: storage channels at infer=False;
the messages channel via infer=True against a deterministic stub chat; stub embedder —
the extraction-prompt path with a real LLM was not exercised. Observed behavior
(outside the verdict): by-ID get/update/delete on a foreign record succeed — an API
contract fact, recorded without judgment.
