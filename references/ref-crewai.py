"""Skeleton: CrewAI + MAQS-Way P4 fail-closed (derived)."""
from pathlib import Path
def resolve_root(base: Path, agent_id: str) -> Path:
    root = (base / agent_id).resolve()
    assert str(root).startswith(str(base.resolve())), "escape BLOCK"
    return root
def can_write(root: Path, target: Path) -> bool:
    try: target.resolve().relative_to(root); return True
    except ValueError: return False  # default-deny
