"""Skeleton: LlamaIndex + MAQS-Way P3 invalidation (derived)."""
from datetime import datetime, timezone
def resolve_contradiction(old: dict, new: dict):
    now = datetime.now(timezone.utc).isoformat()
    old["invalid_at"] = now  # retain, never delete history
    old["invalidated_by"] = new["id"]
    new["valid_at"] = now
    return old, new

def is_expired(rec, now: str) -> bool:
    inv = rec.get("invalid_at")
    return bool(inv and inv < now)  # → EXPIRED, not SUPERSEDED (SPEC §2.2)
