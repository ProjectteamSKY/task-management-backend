from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: str
    status: str                        # pending | todo | in_progress | review | backlog | done
    priority: str                      # low | medium | high | critical
    task_type: str = "GENERAL"         # GENERAL | DEVELOPMENT | BUG_FIX | TESTING | DEVOPS | DEPLOYMENT | FIELD_WORK | INSPECTION | MAINTENANCE | MEETING
    estimated_hours: int
    project_id: Optional[int] = None   # FK → projects.id
    start_date: Optional[str] = None   # "YYYY-MM-DD"
    end_date: Optional[str] = None     # "YYYY-MM-DD"