"""Skeleton: LangChain + MAQS-Way P4 isolation (derived)."""
# pip install langchain qdrant-client  # not installed here
def tenant_query_filter(tenant: str):
    if not tenant: raise ValueError("tenant required (fail-closed)")
    return {"must": [{"key": "tenant_id", "match": {"value": tenant}}]}

def strip_identity_keys(md: dict) -> dict:
    return {k: v for k, v in md.items() if k not in ("user_id", "agent_id", "tenant_id")}

# use: retriever.search(query, filter=tenant_query_filter(t), limit*4) BEFORE top-k
# check: cross_tenant_retrieval_returns_0
