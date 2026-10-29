# Cheatsheets — index (Phase 1.1)

Derived packaging. Canon stays in `MAQS_Way/`: `SPEC.md` v0.3, `maqs-way-standard.json` v0.3.0, model `way-v0.1.3` (`omps-0.1.0+way-v0.1.3`), MAQS v1.8.1.

## Files
- `P1-P8-cheatsheet.md` — 8 principles: Property / Verification / Example + MAQS link.
- `pattern-mem0-isolation.md` — pre-top-k tenant filter + anti-spoofing.
- `pattern-graphiti-invalidation.md` — bitemporal invalidation, never delete history.
- `pattern-letta-fail-closed.md` — per-agent roots, default-deny, self-edit guards (client scope).

## What this is NOT (no tails)
- NOT executable harness (SPEC §6 Backlog v0.3).
- NOT GitHub Action (Phase 2.1 next, will pin `maqs_way_audit.py all` + `schema_version` check).
- NOT RFC (Phase 4.3, will reference this folder).
- No new thresholds invented; no canon rewritten. Audits cited with commit + path; `declared` vs `executed` not conflated.

## Next logical step
Phase 2.1 Action (needs only `python3 schemas/maqs_way_audit.py all`, no model change) or Phase 1.2 Evaluator static form generating `maqs-manifest.json` from these cards.
