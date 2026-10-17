# Conventions

- Every artifact carries version pins (`v0.2` rules release vs `way-v0.1.3` frozen model) and a derived-not-canon stamp.
- Honesty stamps: evaluator manifests `status:self-declared`; `executed:true` = ran to completion here (pass/fail lives ONLY in `verdict`); thresholds labeled indicative candidates (reasoning, not measurement).
- Audit refs use SHA-pinned permalinks + audit date: Mem0 `@0724291 (2026-10-14)`, Graphiti `@aca3693 (2026-10-15)`, Letta `@cc4654a (2026-10-14)`; Way canonical `invalid_at` vs Graphiti impl `expired_at` always disambiguated.
- Outreach tone: help-not-roast, no ranking, HN as Show HN with file:line falsifiability.
- Canon gates: whitelist↔fixture lockstep (extend by commit, never silently); owner fields resolve via `schemas/spec-manifest.json` (SPEC sections) or MAQS/principle ids — dangling owner = RED; manifest `version` must equal standard `version`.
- Canon (`MAQS_Way/`) edits: owner sanction required, never commit without explicit request; leave `git status` clean (`__pycache__` removed after runs).
