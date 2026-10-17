# Task completion

- Done = `./run_all.sh` ends `PIPELINE GREEN` with `WIRED-EXIT:0` (covers canon GREEN, 3 RED branches, shapes, evaluator e2e).
- After any canon run: delete `MAQS_Way/schemas/__pycache__`, verify `git -C MAQS_Way status` shows only intended files (spec-manifest package: `M check_b_coverage.py, M check_c8_coverage.py, ?? spec-manifest.json`, uncommitted until owner signs).
- New/changed outreach text stays `drafts only` (no auto-post, manual sanctioned send).
- Baselines: `baseline-audit-*.json` carry `_baseline{ts, maqs_way_sha, runner}`; runner-green diffs against local baseline (divergence = environment).
