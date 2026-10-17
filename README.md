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
./run_all.sh [--maqs-way PATH]
```
Canon GREEN → RED self-test (detector must fail where expected) → pipeline shapes → evaluator e2e. Exit 0 only if green **and** red branches all behave. Runs in CI: [`.github/workflows/pipeline.yml`](.github/workflows/pipeline.yml) — green on the real Actions runner (python 3.12.3, jsonschema 4.10.3).

## Status (2026-10-17)
- Canon gate: GATE GREEN — schema 4/4 + manifest 12/12 + replay-vectors 8/8 + scoreboard 24/24 + canon-pin + namespaces
- Measured (WP2): evidence-R@5 = 0.98 stratified-50 / 1.00 temporal-50, single-point, pre-registered — [evals/prereg-v03.md](https://github.com/alexk202/maqs-way/blob/main/evals/prereg-v03.md) in canon
- NOT claimed: §3.2 normative thresholds (single-point ≠ normative; needs a second system or full haystack)

## Rule
Every artifact here is **derived**. Nothing silently rewrites canon: proposals wait for owner signature, measurements carry provenance, outreach stays `drafts only, do not auto-post`.