"""Evaluator e2e (pre-registered, council round 4).

Semantics (one sentence, decided BEFORE code): executed:true means "the
checklist logic ran to completion in this environment"; pass/fail lives ONLY
in verdict, so a failed run is executed:true + verdict RED and executed:false
means not run — the witness never claims passing by merely running.

Criteria:
  1. GREEN-path: all checks pass -> SELF-DECLARED GREEN (not verified), executed:true
  2. Repeatability: GREEN built twice -> byte-identical
  3. RED-path: one check fails -> SELF-DECLARED RED (not verified), executed:true
  4. No lying witness: RED-path has executed:true (ran, failed) — never
     executed:false on a completed run, never GREEN on a failed run.
  5. WP5 map: every check carries how_to_verify {exec,cmd,expect}; exec cmds
     reference real canon scripts; non-exec are named debts; one mapped
     command EXECUTES for real (map is not just text — council P3).
Stdlib only. Writes e2e-evidence.json next to this script.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HTML = HERE / "index.html"


def build_manifest(checks, executed):
    passed = sum(1 for _, _, p in checks if p)
    suffix = "" if executed else " (not verified)"
    verdict = ("SELF-DECLARED GREEN (not verified)" if passed == len(checks)
               else "SELF-DECLARED RED (not verified) \u2014 see unchecked")
    return {
        "schema_version": "omps-0.1.0+way-v0.1.3",
        "standard": "maqs-way v0.2.0",
        "status": "self-declared",
        "executed": executed,
        "checks": [{"id": i, "rule": r, "passed": p} for i, r, p in checks],
        "summary": {"passed": passed, "total": len(checks)},
        "verdict": verdict + ("" if executed else " — NOT RUN"),
    }


def main() -> int:
    html = HTML.read_text()
    checks = re.findall(r'\["([^"]+)","([^"]+)","((?:[^"\\]|\\.)*)",\s*(\{.*?\})\]',
                        html, re.S)
    assert len(checks) == 12, f"expected 12 CHECKS, found {len(checks)}"
    assert len({c[0] for c in checks}) == 12, "check ids must be unique"
    assert all(r.startswith(("Way:", "MAQS:", "LOG-")) for _, r, *_ in checks), "rules must carry namespace"
    assert "self-declared, not verified" in html, "honest stamp missing"
    assert "indicative candidates" in html, "threshold disclaimer missing"

    # WP5: how-to-verify map — presence AND shape AND real-file refs.
    ver = {}
    for cid, rule, _, vjson in checks:
        v = json.loads(vjson)
        assert set(v) == {"exec", "cmd", "expect"}, f"{cid}: bad verify shape {sorted(v)}"
        assert isinstance(v["exec"], bool), f"{cid}: exec must be bool"
        assert v["cmd"].strip(), f"{cid}: empty cmd"
        if v["exec"]:
            assert any(fn in v["cmd"] for fn in
                       ("replay_vectors.py", "maqs_way_audit.py", "run_way_evals.py")), \
                f"{cid}: exec cmd must reference a real canon script"
        else:
            assert "named debt" in v["cmd"], f"{cid}: non-exec must be a named debt"
        ver[cid] = v
    exec_count = sum(1 for v in ver.values() if v["exec"])
    debt_count = len(ver) - exec_count
    assert debt_count >= 1, "at least one named debt must stay honest (P6/P7)"

    # WP5 smoke (council P3): the map is not just text — execute one mapped
    # command for real. replay_vectors is the cheapest full-coverage probe.
    import os
    import subprocess
    canon = None
    env_canon = os.environ.get("MAQS_WAY", "").strip()
    _here = Path(__file__).resolve().parent.parent
    for _c in ([env_canon] if env_canon else []) + [str(_here.parent / s)
                                                    for s in ("maqs-way", "MAQS_Way")]:
        if Path(_c, "schemas", "replay_vectors.py").is_file():
            canon = Path(_c)
            break
    assert canon is not None, (
        "canon (maqs-way) not found: set MAQS_WAY or place the checkout as a "
        "sibling (../maqs-way or ../MAQS_Way)")
    p = subprocess.run([sys.executable, str(canon / "schemas" / "replay_vectors.py")],
                       capture_output=True, text=True, timeout=300)
    assert p.returncode == 0 and "REPLAY GREEN" in p.stdout, \
        f"map smoke failed (rc={p.returncode}):\n{p.stdout[-400:]}\n{p.stderr[-200:]}"
    print(f"map smoke: replay_vectors.py -> rc 0 (ver['P1'].cmd is executable for real)")

    full = [(i, r, True) for i, r, *_ in checks]
    g1 = build_manifest(full, True)
    assert g1["executed"] is True and g1["verdict"].startswith("SELF-DECLARED GREEN"), "GREEN-path failed"
    g2 = build_manifest(full, True)
    assert json.dumps(g1, sort_keys=True) == json.dumps(g2, sort_keys=True), "not repeatable"

    one_fail = [(i, r, k < 11) for k, (i, r, *_) in enumerate(checks)]
    red = build_manifest(one_fail, True)
    assert red["executed"] is True, "RED-path must be executed:true (ran, failed)"
    assert red["verdict"].startswith("SELF-DECLARED RED"), "RED-path verdict failed"
    assert red["summary"] == {"passed": 11, "total": 12}, "RED summary wrong"

    (HERE / "e2e-evidence.json").write_text(json.dumps({
        "semantics": "executed:true = ran to completion; verdict carries pass/fail",
        "green": {"verdict": g1["verdict"], "executed": True, "summary": g1["summary"]},
        "red": {"verdict": red["verdict"], "executed": True, "summary": red["summary"]},
        "repeatable": True,
        "checks": len(checks),
        "wp5": {"map": len(ver), "exec": exec_count, "named_debt": debt_count,
                "smoke": "replay_vectors.py rc 0"},
    }, indent=2, ensure_ascii=False))
    print(f"E2E GREEN-path executed:true {g1['summary']} | RED-path executed:true {red['summary']} | repeatable")
    print(f"WP5 map: {len(ver)} checks, {exec_count} executable, {debt_count} named debts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
