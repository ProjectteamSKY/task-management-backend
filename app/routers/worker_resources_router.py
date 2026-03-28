from app.services import worker_resources_service
from fastapi import APIRouter
from app.domain.worker_domain import ShiftScheduleCreate, EquipmentCreate, TrainingDevelopmentCreate
router = APIRouter(prefix="/workers", tags=["Workers"])
# ── Shift 

@router.put("/{worker_id}/shift")
async def upsert_shift(worker_id: int, data: ShiftScheduleCreate):
    return await worker_resources_service.upsert_shift(worker_id, data)

@router.get("/{worker_id}/shift")
async def get_shift(worker_id: int):
    return await worker_resources_service.get_shift(worker_id)

@router.delete("/{worker_id}/shift")
async def delete_shift(worker_id: int):
    return await worker_resources_service.delete_shift(worker_id)


# ── Equipment ──────────────────────────────────────────────────────────────────

@router.post("/{worker_id}/equipment")
async def add_equipment(worker_id: int, data: EquipmentCreate):
    return await worker_resources_service.add_equipment(worker_id, data)

@router.get("/{worker_id}/equipment")
async def get_equipment(worker_id: int):
    return await worker_resources_service.get_equipment(worker_id)

@router.put("/{worker_id}/equipment/{equipment_id}")
async def update_equipment(worker_id: int, equipment_id: int, data: EquipmentCreate):
    return await worker_resources_service.update_equipment(worker_id, equipment_id, data)

@router.delete("/{worker_id}/equipment/{equipment_id}")
async def delete_equipment(worker_id: int, equipment_id: int):
    return await worker_resources_service.delete_equipment(worker_id, equipment_id)


# ── Training & Goals ───────────────────────────────────────────────────────────

@router.post("/{worker_id}/training-development")
async def add_training_development(worker_id: int, data: TrainingDevelopmentCreate):
    return await worker_resources_service.add_training_development(worker_id, data)

@router.get("/{worker_id}/training-development")
async def get_training_development(worker_id: int):
    return await worker_resources_service.get_training_development(worker_id)

@router.put("/{worker_id}/training-development/{record_id}")
async def update_training_development(worker_id: int, record_id: int, data: TrainingDevelopmentCreate):
    return await worker_resources_service.update_training_development(worker_id, record_id, data)

@router.delete("/{worker_id}/training-development/{record_id}")
async def delete_training_development(worker_id: int, record_id: int):
    return await worker_resources_service.delete_training_development(worker_id, record_id)