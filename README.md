# maqs-way-evidence

Companion repo for [MAQS-Way v0.2](https://github.com/alexk202/maqs-way) — the megaphone, not the canon. Canon (SPEC, standard, gates) lives in the main repo; this repo holds the artifacts that make it visible and testable.

## Layers (top-down, the path a person from outside takes)
- [`cheatsheets/`](cheatsheets/) — learn: P1–P8 + 3 worked patterns (Mem0 isolation, Graphiti invalidation, Letta fail-closed), SHA-pinned to audited commits
- [`evaluator/`](evaluator/) — try: static self-audit (single `index.html`, zero deps) → `maqs-manifest.json`, stamped **self-declared, not verified**; every check carries a how-to-verify command
- [`github-action/`](github-action/) — embed: composite action template + workflow example (no secrets, no network)
- [`gaps/`](gaps/) — extend: open-gaps templates + full v0.2 reference (all 12 gaps per SPEC §7)
- [`references/`](references/) — adopt: minimal LangChain/LlamaIndex/CrewAI patterns
- [`rfc/`](rfc/) — propose: RFC skeleton
- [`outreach/`](outreach/) — reach: platform posts (drafts only, manual send)
- [`negative-red/`](negative-red/) — trust: the gate's own RED self-test (orphan, pin-drift, dangling-owner)
- [`proposals/`](proposals/) — upstream: canon-package drafts awaiting owner signature

## Wired check (one command)
```
./run_all.sh [--maqs-way PATH]        # or: --maqs-way=PATH
```
Canon GREEN → RED self-test (detector must fail where expected) → pipeline shapes → evaluator e2e. Exit 0 only if green **and** red branches all behave. Unknown arguments are an error, never silently ignored. Canon path: `$MAQS_WAY`, else a sibling checkout (`../maqs-way` / `../MAQS_Way`), else a clear error — no home paths. Runs in CI: [`.github/workflows/pipeline.yml`](.github/workflows/pipeline.yml) — green on the real Actions runner (python 3.12.3, jsonschema 4.10.3).

## Name guard
After cloning: `git config core.hooksPath .githooks` — pre-commit + commit-msg scan staged files / the commit message with the canon's name-leak pattern ([maqs-way/.githooks/name_guard.py](https://github.com/alexk202/maqs-way/blob/main/.githooks/name_guard.py), single source — this repo's [`.githooks/name_guard.py`](.githooks/name_guard.py) only imports it; fail-closed if the canon checkout is not found).

## Status (2026-10-26)
- Canon gate (as the canon prints it today): **GATE GREEN** — `schema 4/4 + manifest 12/12 + declared 8/8 + executed (canon-pin) 1/1 + replay-vectors 8/8 + scoreboard 24/24 + namespaces ok`; `name policy: 0 leaks in tracked files -- GREEN (bound to MAQS_Way, any cwd)`; open gaps stay enumerated, not folded (B4 → owner SPEC §2.5; I11 bridge)
- Measured (WP2, HEADLINE — isolated re-measurement 2026-10-25/26): full-500-iso evidence-R@5 = **0.988** (494/500, Wilson [0.974, 0.994]) — the first ISOLATED full-500 (per-question history isolation, H5 guard, signed prereg) — artifacts: [evals/results/pilot_evidence_n500_iso.json](https://github.com/alexk202/maqs-way/blob/main/evals/results/pilot_evidence_n500_iso.json) + [verdicts](https://github.com/alexk202/maqs-way/blob/main/evals/results/full500iso_verdicts.md) in canon
- Measured (WP2, Oct-17, PRE-isolation): full-500 evidence-R@5 = **0.992** (496/500, Wilson [0.980, 0.997], within pre-registered [0.90, 1.00]) — measured under the shared-history confound (annotated 2026-10-25); superseded as the headline by the isolated 0.988 per the owner's headline rule — artifact: [evals/results/pilot_evidence_n500.json](https://github.com/alexk202/maqs-way/blob/main/evals/results/pilot_evidence_n500.json) in canon
- Confound found and re-measured (2026-10-25): R@5 unaffected — the shared-history contamination measured at 14.8% of stored facts; the isolated re-measurement (g1-iso-b) held evidence-R@5 = 1.000 (156/156): [maqs-way/evals/results/g1iso_verdicts.md](https://github.com/alexk202/maqs-way/blob/main/evals/results/g1iso_verdicts.md)
- Three framework audits: [Mem0](https://github.com/alexk202/maqs-way/blob/main/docs/audits/mem0-way-audit.md) / [Graphiti](https://github.com/alexk202/maqs-way/blob/main/docs/audits/graphiti-way-audit.md) / [Letta](https://github.com/alexk202/maqs-way/blob/main/docs/audits/letta-way-audit.md) — `docs/audits/` in canon
- **P4 behavioral verification (2026-10-26): verified on mem0@0724291b, Linux CPU-only stub stand** — cross-subject isolation (user_id/agent_id/run_id × search/get_all/history channels) executed and passed with three firing controls; boundaries: stub embedder + stub chat, extraction path with a real LLM not exercised — [report](https://github.com/alexk202/maqs-way/blob/main/evals/results/p4_mem0_isolation_report.json) in canon; cheatsheet: [pattern-mem0-isolation.md](cheatsheets/pattern-mem0-isolation.md)
  - Retrieval isolation — verified; authorization of ID-addressed operations (get/update/delete) is outside mem0's contract and must be enforced by the integrating application.
- Reproduction: [maqs-way/evals/REPRODUCE.md §8](https://github.com/alexk202/maqs-way/blob/main/evals/REPRODUCE.md) — the external reproduction protocol (failed attempts recorded same as successful)
- Discussion: [alexk202/maqs-way discussion #1](https://github.com/alexk202/maqs-way/discussions/1)
- NOT claimed: §3.2 normative thresholds (gates stay per-deployment candidates, not norms; needs a second system)

## Rule
Every artifact here is **derived**. Nothing silently rewrites canon: proposals wait for owner signature, measurements carry provenance, outreach stays `drafts only, do not auto-post`.