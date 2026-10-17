# Tech stack

- Content: Markdown docs + single-file static HTML/JS (`evaluator/index.html`, zero deps, GitHub Pages ready).
- Scripts: Python stdlib only (`negative-red/replay_red.py`, `evaluator/e2e.py`, `references/ref-*.py` skeletons).
- CI: composite GitHub Action (`github-action/action.yml`), workflow template `maqs-audit.yml`, wired check `run_all.sh` + `.github/workflows/pipeline.yml`.
- Pins: `jsonschema>=4,<5` (canon gate dep), `actions/checkout@v4`, `actions/upload-artifact@v4`, runners `ubuntu-latest`; local python 3.12.
- Canon audit entry: `MAQS_Way/schemas/maqs_way_audit.py all` (exit 0 = GREEN).
