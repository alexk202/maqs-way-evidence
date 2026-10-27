# MAQS-Way v0.2 — Request for Comments (skeleton, Phase 4.3)

Status: experimental minor v0.2 (2026-10-15). Data model frozen: `way-v0.1.3` (`omps-0.1.0+way-v0.1.3`). Audit core: MAQS v1.8.1. License: Apache-2.0.

## 0. Summary (TODO: 5 lines)
Way = common path policy→implementation. MAQS checks mechanism exists, Way proves it works.

## 1. Conventions (RFC2119)
MUST/SHOULD/MAY per principles P1–P8. Thresholds indicative until first run.

## 2. Principles P1–P8 (normative refs)
See `../cheatsheets/P1-P8-cheatsheet.md`. Canon: SPEC §1.

## 3. Architecture (normative refs)
Data model, lifecycle ACTIVE→…→TOMBSTONE→null, 6-tier cascade, `visible_to` masking, temporal priority `invalid_at<now → EXPIRED`. Canon: SPEC §2.

## 4. Verification (normative refs)
Metrics gate/target (R@5 0.7/0.85, temporal 0.65/0.8, abstention 0.8/0.9, duplicate 5%/2%, contamination 1%/0, residue 0), deletion lattice, logging Art12+OTel. Canon: SPEC §3 + `maqs-way-standard.json → verification_suite`.

## 5. Profiles A/B/C
A Personal (User Wins), B Enterprise (Broker + operator 72h, legal_hold), C Ephemeral (no write).

## 6. Open gaps (must list, no silence)
B4, E10/E11, I10/I11/I12, I14, I15, P9/P10, 0.5a, 0.6a → v0.3. Template: `../gaps/open-gaps.template.json`.

## 7. Compatibility
`schema_version` pins model, not release. `invalid_at` rule frozen since v0.1.3.

## 8. References
SPEC.md, maqs-way-standard.json, conformance/manifest.json (12 vectors), audits mem0/graphiti/letta.

## Appendix: Comments requested
1. Thresholds realistic? 2. Broker appeal workable? 3. Tombstone zero-PII sufficient for GDPR?
