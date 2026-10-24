#!/usr/bin/env python3
"""Name-leak guard for maqs-way-evidence (companion repo, NOT the canon).

Single source rule: the pattern and skip-lists live ONLY in the canon
(MAQS_Way/.githooks/name_guard.py). This hook locates the canon checkout,
imports its `PAT` / `hits_in` / `SKIP_*`, and rebinds the scan to THIS
repository (REPO_ROOT from __file__ — never the caller's cwd). No second,
drifting copy of the pattern exists here.

Canon resolution (no home paths): $MAQS_WAY, then sibling checkouts
../maqs-way / ../MAQS_Way next to this repo.

Fail-closed: canon not found, import fails, git unavailable/errors, or an
empty tracked-file list -> RED (exit 1), never green.

Wired via `git config core.hooksPath .githooks` (pre-commit + commit-msg).
Modes: scan-all | pre-commit | commit-msg <msgfile>.
"""
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_canon_guard():
    """Import the canon name_guard module. Returns (module, canon_root)."""
    env = os.environ.get("MAQS_WAY", "").strip()
    candidates = ([env] if env else []) + [str(REPO_ROOT.parent / s)
                                          for s in ("maqs-way", "MAQS_Way")]
    for cand in candidates:
        root = Path(cand)
        guard = root / ".githooks" / "name_guard.py"
        if guard.is_file():
            spec = importlib.util.spec_from_file_location("canon_name_guard", guard)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod, root
    return None, None


def scan_files(guard, files):
    """Apply the canon PAT to files of THIS repo. Returns list of hits."""
    hits = []
    for f in files:
        if f.startswith(guard.SKIP_PREFIX) or any(s in f for s in guard.SKIP_SUBSTR):
            continue
        try:
            text = (REPO_ROOT / f).read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        h = guard.hits_in(text)
        if h:
            hits.append((f, h))
    return hits


def fail_closed(msg):
    print(f"NAME-POLICY SCAN FAILED: {msg}")
    print("name policy: FAIL-CLOSED (cannot scan -> red, never green)")
    return 1


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    guard, canon_root = load_canon_guard()
    if guard is None:
        return fail_closed(
            "canon name_guard not found (single source: maqs-way/.githooks/"
            "name_guard.py). Set MAQS_WAY or place the canon checkout as a "
            "sibling (../maqs-way or ../MAQS_Way)")
    try:
        PAT_OK = (guard.PAT is not None and callable(guard.hits_in))
    except AttributeError:
        return fail_closed("canon name_guard lacks PAT/hits_in — API drift?")
    if not PAT_OK:
        return fail_closed("canon name_guard API mismatch")

    if mode == "scan-all":
        try:
            proc = subprocess.run(["git", "-C", str(REPO_ROOT), "ls-files"],
                                  capture_output=True, text=True)
        except OSError as e:
            return fail_closed(f"git unavailable ({e.__class__.__name__})")
        if proc.returncode != 0:
            return fail_closed(f"git ls-files failed: {proc.stderr.strip()[:120]}")
        files = proc.stdout.split()
        if not files:
            return fail_closed("no tracked files — not a git repository?")
        hits = scan_files(guard, files)
        for f, h in hits:
            print(f"NAME LEAK in {f} (lines {h[:8]})")
        print(f"scan-all: {len(hits)} file(s) with leaks "
              f"(pattern imported from canon name_guard)")
        return 1 if hits else 0

    if mode == "pre-commit":
        try:
            proc = subprocess.run(
                ["git", "-C", str(REPO_ROOT), "diff", "--cached",
                 "--name-only", "--diff-filter=ACM"],
                capture_output=True, text=True)
        except OSError:
            return fail_closed("git unavailable")
        if proc.returncode != 0:
            return fail_closed(f"git diff error: {proc.stderr.strip()[:120]}")
        files = [f for f in proc.stdout.split()
                 if not f.startswith(guard.SKIP_PREFIX)
                 and not any(s in f for s in guard.SKIP_SUBSTR)]
        hits = scan_files(guard, files)
        for f, h in hits:
            print(f"NAME LEAK in {f} (lines {h[:8]}) -- fix or add to SKIP "
                  "only by owner decision")
        return 1 if hits else 0

    if mode == "commit-msg":
        if len(sys.argv) < 3:
            return fail_closed("commit-msg mode needs the message file argument")
        with open(sys.argv[2], encoding="utf-8", errors="ignore") as fh:
            text = fh.read()
        h = guard.hits_in(text)
        if h:
            print(f"NAME LEAK in commit message (lines {h[:8]}); "
                  "names are council-only in public history")
            return 1
        print("name policy: commit message clean")
        return 0

    print(f"usage: {sys.argv[0]} scan-all | pre-commit | commit-msg <msgfile>")
    return 2


if __name__ == "__main__":
    sys.exit(main())