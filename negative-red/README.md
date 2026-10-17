# Negative RED fixtures — detector self-test (Prima round 2)

`baseline-audit-20261016.json` proves the gate passes good input.
This dir proves it rejects bad input. Together = validated detector, not faith.

| Fixture | Injection | Expectation |
|---|---|---|
| `999-orphan.json` | vector file, no manifest entry | `manifest` exit 1, `orphan` |
| pindrift (runtime) | `invalid/005` similarity 0.3 → 0.99 | `pin` exit 1 `drift`, `all` GATE RED |
| dangling (runtime) | B4 owner `SPEC §2.5` → `SPEC §99` | `coverage` exit 1 `dangling`, `all` GATE RED |

Run: `python3 negative-red/replay_red.py [--maqs-way PATH]` → exit 0 only if GREEN + all three REDs behave. Temp copies only; canon untouched.

Known limit (honest): `owner`/`closes_in` free text (e.g. `SPEC §2.5`) is NOT resolved against SPEC sections today. Rules ARE resolved (`check_namespaces` + B/C8 gates: principles exist, MAQS closed list, LOG map, SCHEMA file, whitelist↔fixture lockstep). Dangling-owner fixture (`declared-but-dangling → RED`) does not exist yet — proposed as third fixture (needs owner allowlist or SPEC-section parser in canon; canon change = owner sanction).
