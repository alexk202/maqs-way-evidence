# Suggested commands (run from repo root)

- `./run_all.sh [--maqs-way PATH]` — the full wired check (canon GREEN → RED self-test → shapes → evaluator e2e). Default canon: `/home/aleksandr/Projects/MAQS_Way`.
- `python3 negative-red/replay_red.py [--maqs-way PATH]` — RED-branch self-test standalone.
- `python3 evaluator/e2e.py` — evaluator pre-registered e2e (GREEN/RED-path + repeatability).
- Canon audit: `python3 schemas/maqs_way_audit.py all --format [text|json]` inside `MAQS_Way/`.
- No build, no linter, no formatter in this repo (docs + stdlib scripts).
