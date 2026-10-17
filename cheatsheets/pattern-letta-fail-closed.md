# Pattern: Letta Fail-Closed (P4 client-side exemplary)

Source: `MAQS_Way/docs/audits/letta-way-audit.md`, code `letta-ai/letta-code @ cc4654a` (2026-10-14). Scope: MemFS client/harness only (`~/.letta/agents/{id}/memory/` git-backed Markdown). Server archival/recall closed — unjudged. Example only, NOT canon.

## What to copy
1. Per-agent roots + containment: `resolveAllowedMemoryRoots()` + `isOwnMemoryWrite()` allow only own checkout, symlink-resolved, default-deny (`memory-paths.ts:181-208`, `memory-write-allowance.ts:37-61`, `memory-filesystem.ts:46-57`).
2. Reject escapes: `..`, hidden, absolute paths rejected via realpath containment (`memory.ts:371-397`); subagent sandbox writes own, not others' (`memory-confinement.ts:13-21`).
3. Self-edit guards: `read_only` frontmatter unmodifiable by agent; `.memfs.config.json` needs human approval (`memory-frontmatter.ts:55-61,91-120`, `memory-constraints.ts:142-146`).
4. Idempotent commits: `commitMemoryPaths()` → `hasStagedMemoryChanges()` else `{committed:false}` (`memory-git.ts:1184-1195`); missing-file delete = no-op success.

## What NOT to copy (gaps in same audit)
- No aging: budgets only, no TTL/expiry/decay/supersede (`memory-constraints.ts:302-308`) → add `expires_at/supersedes` + reaper for P3.
- Bodies without provenance: frontmatter only `name/description` → add `source:` + `confidence:` for P2.
- No tombstone API; git history = residue by design → state recoverability-first or add hard-purge for P5.
- Primary edits bypass file-lease; `catch{}` fallbacks; push 8s cap → metrics on every fallback (B5).

## Way mapping
- P4 COVERED client-side; P8 policy-heavy COVERED (no memory-quality benchmarks).
- Pair with Mem0 pattern for server vector-store isolation; add G1 fixtures (3)+(4) for full P4.
