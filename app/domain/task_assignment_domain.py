from pydantic import BaseModel
from typing import Optional


class AssignmentCreate(BaseModel):
    task_id: int
    worker_id: int
    allocated_hours: int
    assigned_date: str                 # "YYYY-MM-DD"
    status: str = "pending"           # pending | in_progress | completed | cancelled


class AssignmentUpdate(BaseModel):
    allocated_hours: Optional[int] = None
    assigned_date: Optional[str] = None
    status: Optional[str] = None