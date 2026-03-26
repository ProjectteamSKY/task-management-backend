from pydantic import BaseModel
from typing import Optional

class WorkerCreate(BaseModel):
    # id is BIGSERIAL — never passed in on create
    name: str
    email: str
    role: str
    department: str
    status: str
    avatar: Optional[str] = None
    daily_capacity_hours: int