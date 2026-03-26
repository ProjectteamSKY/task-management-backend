from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    estimated_hours: int
    assigned_to: Optional[int] = None
    project_name: str
    start_date: Optional[str] = None   # "YYYY-MM-DD"
    end_date: Optional[str] = None     # "YYYY-MM-DD"