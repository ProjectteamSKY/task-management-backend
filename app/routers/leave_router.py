from fastapi import APIRouter
from app.services import leave_service as svc

# ── Global router (not worker-scoped) ─────────────────────────────────────────
global_router = APIRouter(prefix="/leaves", tags=["Leave Requests"])


@global_router.get("/")
async def list_all_leave_requests():
    """All leave requests across every worker (admin view)."""
    return await svc.get_all_leaves()


# ── Worker-scoped router ───────────────────────────────────────────────────────
router = APIRouter(prefix="/workers/{worker_id}/leaves", tags=["Leave Requests"])


@router.get("/")
async def list_leave_requests(worker_id: int):
    """All leave requests for a specific worker."""
    return await svc.get_leaves(worker_id)


@router.get("/{approval_status}")
async def list_leaves_by_approval(worker_id: int, approval_status: str):
    """Filter by approval_status: pending | approved | rejected"""
    return await svc.get_leaves_by_approval(worker_id, approval_status)


@router.put("/{record_id}/approve")
async def approve_leave(worker_id: int, record_id: int):
    return await svc.approve_leave(worker_id, record_id)


@router.put("/{record_id}/reject")
async def reject_leave(worker_id: int, record_id: int):
    return await svc.reject_leave(worker_id, record_id)