# Open Gaps — how to declare (Phase 2.2)

Copy `open-gaps.template.json` into your repo (e.g. `maqs-gaps.json`). Same shape as `MAQS_Way/schemas/b_write_integrity.json` + `c8_classes.json` `known_gap` entries. No silent gaps: every gap has owner + closes_in.
Full v0.2 reference: `open-gaps-full-v0.2.json` (all 12 gaps per SPEC §7, template-not-canon; owners there are history labels, not gate-resolvable — never feed it to coverage gates).

Fields:
- `id`: stable gap id, e.g. `B4`, `E10`, `I14`.
- `known_gap: true` always.
- `owner`: SPEC section or code owner, e.g. `SPEC §2.5`.
- `closes_in`: `v0.3` + what closes it.
- `adjacent`: Way P-ids nearby but NOT covering (honesty).
- `retarget_note`: if moved, why (no silent rollover).
