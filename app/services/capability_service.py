import json
from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.capability_domain import CapabilityCreate, CapabilityBulkCreate, CapabilityUpdate

q = load_queries("capability_queries")["capability"]


async def get_capabilities(worker_id: int):
    return await query(q["get_by_worker"], [worker_id], fetch_all=True)


async def create_capability(worker_id: int, data: CapabilityCreate):
    return await execute(
        q["create_one"],
        [worker_id, data.capability, data.proficiency],
        fetch_row=True,
    )


async def bulk_create_capabilities(worker_id: int, data: CapabilityBulkCreate):
    """
    Passes the list as a JSONB array so Postgres expands it into rows.
    Matches the bulk_create query that uses jsonb_to_recordset.
    """
    payload = json.dumps([c.model_dump() for c in data.capabilities])
    return await query(q["bulk_create"], [worker_id, payload], fetch_all=True)


async def update_capability(worker_id: int, capability_id: int, data: CapabilityUpdate):
    return await execute(
        q["update"],
        [data.capability, data.proficiency, capability_id, worker_id],
        fetch_row=True,
    )


async def delete_capability(worker_id: int, capability_id: int):
    return await execute(
        q["delete_one"],
        [capability_id, worker_id],
        fetch_row=True,
    )


async def delete_all_capabilities(worker_id: int):
    rows = await query(q["delete_all"], [worker_id], fetch_all=True)
    return {"deleted": len(rows)}