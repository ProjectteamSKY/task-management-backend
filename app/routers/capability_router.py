from fastapi import APIRouter, Form
from typing import Optional
from app.services import capability_service
from app.domain.capability_domain import CapabilityCreate, CapabilityBulkCreate, CapabilityUpdate

router = APIRouter(prefix="/workers/{worker_id}/capabilities", tags=["Worker Capabilities"])


@router.get("/")
async def list_capabilities(worker_id: int):
    """All capabilities for a worker, ordered by id."""
    return await capability_service.get_capabilities(worker_id)


@router.post("/")
async def create_capability(
    worker_id: int,
    capability: str       = Form(...),
    proficiency: int      = Form(...),
):
    data = CapabilityCreate(capability=capability, proficiency=proficiency)
    return await capability_service.create_capability(worker_id, data)


@router.post("/bulk")
async def bulk_create_capabilities(worker_id: int, body: CapabilityBulkCreate):
    """Insert multiple capabilities in one shot — used on Add Worker submit."""
    return await capability_service.bulk_create_capabilities(worker_id, body)


@router.patch("/{capability_id}")
async def update_capability(
    worker_id: int,
    capability_id: int,
    capability: Optional[str] = Form(None),
    proficiency: Optional[int] = Form(None),
):
    data = CapabilityUpdate(capability=capability, proficiency=proficiency)
    return await capability_service.update_capability(worker_id, capability_id, data)


@router.delete("/{capability_id}")
async def delete_capability(worker_id: int, capability_id: int):
    """Remove a single capability row."""
    return await capability_service.delete_capability(worker_id, capability_id)


@router.delete("/")
async def delete_all_capabilities(worker_id: int):
    """Wipe all capabilities for a worker — use before re-inserting on Save Changes."""
    return await capability_service.delete_all_capabilities(worker_id)