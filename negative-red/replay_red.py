"""Replay the detector's RED branches against a temp copy of the canon.

GREEN proves the gate passes good input; the three REDs prove it rejects bad.
Exits 0 only if all four behave. Stdlib only. Never touches the canon.

  python3 negative-red/replay_red.py [--maqs-way PATH]

Checks:
  1. GREEN baseline: `maqs_way_audit.py all` in canon -> exit 0
  2. RED-orphan: + conformance/valid/999-orphan.json (no manifest entry)
     -> `manifest` exit 1, output contains 'orphan'
  3. RED-pindrift: fixture invalid/005 similarity 0.3 -> 0.99
     -> `pin` exit 1 ('drift'), `all` -> GATE RED exit 1
  4. RED-dangling: B4 owner 'SPEC §2.5' -> 'SPEC §99'
     -> `coverage` exit 1 ('dangling'), `all` -> GATE RED exit 1
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PIPE = Path(__file__).resolve().parent
# Canon default: a sibling checkout next to this repo (no home paths).
# Tried in order: $MAQS_WAY, ../maqs-way, ../MAQS_Way; error if none exists.
_SIBLINGS = ("maqs-way", "MAQS_Way")


def default_canon() -> Path:
    import os
    env = os.environ.get("MAQS_WAY", "").strip()
    for cand in ([env] if env else []) + [PIPE.parent.parent / s for s in _SIBLINGS]:
        p = Path(cand)
        if (p / "schemas" / "maqs_way_audit.py").is_file():
            return p
    sys.exit("ERROR: canon (maqs-way) not found. Set MAQS_WAY or pass --maqs-way PATH.\n"
             f"  tried: env MAQS_WAY={env or '<unset>'}, "
             + ", ".join(str(PIPE.parent.parent / s) for s in _SIBLINGS))


DEFAULT_CANON = default_canon()


def run(cmd, **kw):
    p = subprocess.run(cmd, capture_output=True, text=True, **kw)
    return p.returncode, p.stdout + p.stderr


def fresh_copy(src: Path) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="maqs_red_"))
    shutil.copytree(src, tmp / "canon",
                    ignore=shutil.ignore_patterns("__pycache__", ".git"))
    return tmp / "canon"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--maqs-way", default=str(DEFAULT_CANON))
    args = ap.parse_args()
    canon = Path(args.maqs_way)
    audit = canon / "schemas" / "maqs_way_audit.py"
    assert audit.exists(), f"no audit CLI at {audit}"

    rc, out = run([sys.executable, str(audit), "all", "--format", "text"])
    assert rc == 0 and "GATE GREEN" in out, f"GREEN baseline failed:\n{out}"
    print("GREEN baseline: exit 0, GATE GREEN")

    c2 = fresh_copy(canon)
    try:
        shutil.copy(PIPE / "999-orphan.json", c2 / "conformance" / "valid" / "999-orphan.json")
        rc, out = run([sys.executable, str(c2 / "schemas" / "maqs_way_audit.py"),
                       "manifest", "--format", "text"])
        assert rc == 1 and "orphan" in out.lower(), f"RED-orphan failed:\n{out}"
        print("RED-orphan: exit 1, orphan detected")
    finally:
        shutil.rmtree(c2.parent, ignore_errors=True)

    c3 = fresh_copy(canon)
    try:
        fp = c3 / "conformance" / "invalid" / "005-shared-fact-visibility-leak.json"
        d = json.loads(fp.read_text())
        assert float(d["fixture"]["similarity_threshold"]) == 0.3
        d["fixture"]["similarity_threshold"] = 0.99
        fp.write_text(json.dumps(d, indent=2))
        rc, out = run([sys.executable, str(c3 / "schemas" / "maqs_way_audit.py"),
                       "pin", "--format", "text"])
        assert rc == 1 and "drift" in out.lower(), f"RED-pindrift(pin) failed:\n{out}"
        rc, out = run([sys.executable, str(c3 / "schemas" / "maqs_way_audit.py"),
                       "all", "--format", "text"])
        assert rc == 1 and "GATE RED" in out, f"RED-pindrift(all) failed:\n{out}"
        print("RED-pindrift: exit 1, drift 0.99 != canon 0.3, GATE RED")
    finally:
        shutil.rmtree(c3.parent, ignore_errors=True)

    c4 = fresh_copy(canon)
    try:
        bp = c4 / "schemas" / "b_write_integrity.json"
        b = json.loads(bp.read_text())
        b4 = next(c for c in b if c["id"] == "B4")
        assert b4["owner"] == "SPEC §2.5", f"canon moved: {b4['owner']!r}"
        b4["owner"] = "SPEC §99"
        bp.write_text(json.dumps(b, indent=2, ensure_ascii=False))
        rc, out = run([sys.executable, str(c4 / "schemas" / "maqs_way_audit.py"),
                       "coverage", "--format", "text"])
        assert rc == 1 and "dangling" in out.lower(), f"RED-dangling failed:\n{out}"
        print("RED-dangling: exit 1, owner 'SPEC §99' resolves to nothing")
    finally:
        shutil.rmtree(c4.parent, ignore_errors=True)

    print("ALL RED-BRANCHES REPLAYED: detector fails when it must")
    return 0


if __name__ == "__main__":
    sys.exit(main())
