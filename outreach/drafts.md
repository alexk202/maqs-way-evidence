# Outreach — second wave (drafts only, do not auto-post)

Cycle: draft → council review → правки → sanction → send вручную, по одной площадке за раз. Порядок (пересмотрен 17.10 — reddit-автомоды банят ИИ-тексты и новичков): **HN (Show HN) → LocalLLaMA (после карма-фазы 1-2 недели) → Discussions → ML-RFC**. First wave командам (Mem0 done, Graphiti = issue #3 в своем репо как публичное приглашение, Letta done) — держать ссылки как ответ на «did you contact the vendors?».
Posting language = English (ниже финальный EN-текст; sanction на EN-версию, не на перевод).
Terminology: Way canonical `invalid_at`; Graphiti impl `expired_at`. Thresholds = one pre-registered measurement (n=50 oracle evidence-R@5, single-point) — not a normative threshold; gates stay per-deployment candidates.

Pinned sources (SHA = аудированный код, ссылки не гниют):
- Mem0 `mem0ai/mem0 @ 0724291 (audited 2026-10-14)`: `github.com/mem0ai/mem0/blob/0724291/mem0/memory/main.py#L1471-L1475` (tenant filter), `#L138-L162` (strip keys), `qdrant.py#L428-L434` (pre-top-k)
- Graphiti `getzep/graphiti @ aca3693 (audited 2026-10-15)`: `github.com/getzep/graphiti/blob/aca3693/.../edge_operations.py#L748-L781` (invalidation, `expired_at`), `search_utils.py#L95-L111` (group_ids pre-top-k)
- Letta `letta-ai/letta-code @ cc4654a (audited 2026-10-14)` (MemFS client only): `memory-paths.ts#L181-L208`, `memory.ts#L371-L397`
- Canon: SPEC.md v0.2, `maqs-way-standard.json` v0.2.0, model `way-v0.1.3`

## 1. reddit r/LocalLLaMA (first — 9/10)
Title: Context contamination is often a retrieval-order bug, not a model bug
Body (EN): pgvector incident — filter applied after top-k leaked User A → User B. Fix pattern: tenant filter BEFORE top-k (Mem0 permalink above) + strip spoofable keys. Graphiti pattern: contradiction retains history with `expired_at` (impl) = `invalid_at` (Way), never deletes. Self-audit via static Evaluator (ships as single `index.html` — run locally against your own manifest, no setup; output self-declared, not verified). No cloud needed.
Links: SPEC + 3 audits. Tone: help, not roast. No ranking.

## 2. HackerNews (second — Show HN, finding-first)
Title: Show HN: MAQS-Way — falsifiable audits of AI memory frameworks (every claim with file:line)
Body (EN): What we found: (1) Mem0 isolates correctly pre-top-k but history stays queryable after delete (no tombstone); (2) Graphiti invalidates instead of deleting — strongest P3, but unscoped search allowed; (3) Letta MemFS client is fail-closed by construction (client scope only). How we prove: `maqs_way_audit.py all` — schema 4/4 + manifest 12/12 + namespaces + canon-pin (similarity 0.3 vs SPEC §3.3) + executable replay of all 8 declared vectors (caught/missed/error, never merged) + scoreboard 24/24 (every audit claim SHA-pinned, file:line). Open gaps with gloss: B4 = multi-store atomicity missing; E10/E11 = assembly rules pending canonization; I10-I12/I14/I15 = logging/drift rules pending → all retargeted v0.3, listed openly. Honest boundaries: Static reading means we verify code paths by construction, not by execution — findings are falsifiable: every claim carries SHA-pinned file:line; if we misread, corrections land as a second commit.
Links: SPEC + 3 audits (SHA permalinks above).

## 3. Discussions (third — one at a time: LangChain → LlamaIndex → CrewAI)
Title: Long-term memory checklist (MAQS-Way v0.2, experimental)?
Body (EN): 8-principle checklist + 3 patterns (isolation pre-top-k = tenant boundaries enforced before vector search; invalidation `invalid_at`/`expired_at` = contradictions expire history instead of deleting; fail-closed roots = per-agent dirs, default-deny). Ask: would a checklist like this fit your long-term memory docs? Links SPEC v0.2 + 3 audits. Tone help, not roast. No ranking.
Door-for-no (keep): If the checklist doesn't fit your docs, that's useful feedback too — telling us what doesn't fit is as valuable as what does.

## 4. reddit r/MachineLearning RFC (last)
Title: [RFC] Common path policy→implementation for AI memory (8 principles + measurable gates, experimental)
Body (EN): Gates as CANDIDATES — one pre-registered measurement, not a normative threshold: first-50 LongMemEval-oracle evidence-R@5 = 0.98 (49/50, all 6 types, single-point Mem0@0724291 + Llama-3.1-8B, oracle haystack; within n=50 uncertainty of the temporal-slice 1.00) [historical first run — the full-500 follow-up measured 0.992, see hn-answer-bank]. The RFC asks whether gates are realistic per-deployment — argue with numbers, we'll retarget. Candidates: R@5 0.7/0.85, temporal 0.65/0.8, abstention 0.8/0.9; deletion lattice design target residue 0 (fail-closed target, not a measured benchmark); logging cost ~5-15ms estimated, not benchmarked.
Links: SPEC §3 + standard.json verification_suite.
