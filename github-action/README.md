# GitHub Action (Phase 2.1) — template, not published

- `action.yml`: composite, pins RULES via `maqs_way_ref` (release = code+rules). Data model `omps-0.1.0+way-v0.1.3` + release `0.3.0` checked at runtime in Python (drift = RED, not echo). Deps: stdlib + `jsonschema>=4,<5` only (`check_conformance.py:25` needs it; tested range `>=4,<5`).
- `maqs-audit.yml`: copy to `.github/workflows/` in consumer repo. Option B works today without marketplace.
- Outputs: `verdict` (GATE GREEN/RED, always written even on RED), `report_path` (`audit-output.txt/json` for artifact upload / PR comment).
- Runners: `ubuntu-latest` tested; macOS OK; Windows via Git Bash untested — use ubuntu for now.
- Security: no secrets required, no network calls in audit (file checks only). Minimal permissions:
  ```yaml
  permissions:
    contents: read
  ```
- Scope honesty: this replays the CANON self-check (`declared` stays declared; only `canon-pin invalid-005` similarity 0.3 vs SPEC §3.3 is executed). It does NOT audit your product code. Your self-audit via `evaluator/index.html` stays `self-declared, not verified` by design.

## Ref pinning warning
Use tags or SHA (`v0.3`, commit SHA). NEVER a branch (`main`): branches move, reproducibility breaks, GATE GREEN stops meaning anything.

## Example workflow
```yaml
name: MAQS-Way Self-Check
on: [push, pull_request]
permissions:
  contents: read
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ./github-action  # or your-org/maqs-way-audit@v0.3 after publish
        id: maqs
        with:
          maqs_way_ref: v0.3  # tag or SHA, not branch
          command: all
          format: json
      - uses: actions/upload-artifact@v4
        with:
          name: maqs-report
          path: ${{ steps.maqs.outputs.report_path }}
```

## Verdict interpretation
- `GATE GREEN` = canon self-consistent + model/release pins match (`way-v0.1.3` / `0.3.0`).
- `GATE RED` = version drift OR audit gate failed. What to do: (1) check your `maqs_way_ref` (tag/SHA?), (2) read `report_path` artifact, (3) if drift is in canon itself → open issue in MAQS_Way with the report attached; if your ref is stale → bump to `v0.3`.
