# Proposal (canon package, NOT applied): owner-reference validation + third negative fixture

Status: draft for owner sanction. Location if sanctioned: canon-adjacent package in MAQS_Way (self-check belongs to the standard, not to its megaphone). Promotion repo does NOT implement it.

## Problem
`owner`/`closes_in` in `b_write_integrity.json` / `c8_classes.json` known-gap entries are free text. `B4 → SPEC §2.5` passes the gate even as `SPEC §99` (verified by reading `check_b_coverage.py:71-77`, `check_c8_coverage.py:61-68`: owner presence checked, target existence not). Rules ARE resolved (`check_namespaces`, whitelist↔fixture lockstep); owners are not. Part of `declared 8/8` is decorative.

## Options (price-tagged, per council round 3)

| Mechanism | Essence | Price | Drift |
|---|---|---|---|
| owner-allowlist | closed list of valid owners, extended by commit (prec. 740c304) | cheap | duplicates SPEC structure, rots on renumbering |
| **spec-manifest (recommended)** | machine-readable index of SPEC sections, `owner ∈ manifest` | medium | zero by construction (third instance of the accepted whitelist↔fixture lockstep pattern) |
| SPEC-parser | parse section headers at gate time | expensive | brittle to formatting |

Recommendation: **spec-manifest** — owner sanctions what already worked twice.

## Third fixture (ships with the mechanism, one sanction)
`declared-but-dangling`: known_gap entry whose `owner` does not resolve → `coverage` exit 1, GATE RED. Mirrors existing REDs (orphan, pindrift): green passes good, red rejects bad, replay proves both.

## Status quo (option 0 — on the table explicitly)
If owner says no: dangling owners keep passing silently, limit lives in `negative-red/README.md`, `declared 8/8` stays partly decorative. Cost: zero. Risk: honesty gap persists by decision, not by oversight.

## How we will know zero-drift worked
Same lockstep assertion as the first two instances: manifest↔fixture exact-set match, mismatch → RED. Proven the same way: replay injects a dangling owner → expects exit 1. Third instance reuses the proof pattern, not just the code pattern.

## Non-goals
No silent canon edits from promotion repo. No behavior change to thresholds, lifecycle, or pins. `schema_version way-v0.1.3` untouched.
