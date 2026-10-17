#!/usr/bin/env bash
# Wired pipeline check: GREEN baseline + RED self-test + evaluator e2e in one command.
# Inversion (Prima round 4 Q1): replay_red.py asserts rc==1 INSIDE and exits 0
# only if both REDs fired where expected. This script uses `set -u` (NOT -e):
# expected REDs inside replay never kill the pipeline; a swallowed RED would
# fail replay's asserts -> replay exits 1 -> `|| exit 1` below fails wired run.
# Usage: ./run_all.sh [--maqs-way PATH]
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
MAQS_WAY="${MAQS_WAY:-/home/aleksandr/Projects/MAQS_Way}"
for a in "$@"; do case "$a" in --maqs-way=*) MAQS_WAY="${a#*=}";; esac; done

echo "== evidence: tool versions =="
python3 -c "import sys,importlib.metadata as m; print('python', sys.version.split()[0], '| jsonschema', m.version('jsonschema'))"
echo "== 1/4 canon GREEN =="
python3 "$MAQS_WAY/schemas/maqs_way_audit.py" all --format text || exit 1
echo "== 2/4 RED self-test (must fail-then-pass) =="
python3 "$HERE/negative-red/replay_red.py" --maqs-way "$MAQS_WAY" || exit 1
echo "== 3/4 pipeline shapes =="
python3 -c "import json,yaml; json.load(open('$HERE/gaps/open-gaps.template.json')); yaml.safe_load(open('$HERE/gaps/open-gaps.template.yaml')); yaml.safe_load(open('$HERE/github-action/action.yml')); assert 'self-declared' in open('$HERE/evaluator/index.html').read(); print('shapes OK')"
echo "== 4/4 evaluator e2e =="
MAQS_WAY="$MAQS_WAY" python3 "$HERE/evaluator/e2e.py" || exit 1
echo "PIPELINE GREEN (green + red wired + evaluator e2e)"
