from pydantic import BaseModel
from typing import Optional


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[str] = None   # "YYYY-MM-DD"
    end_date: Optional[str] = None     # "YYYY-MM-DD"
    status: str = "active"             # active | on_hold | completed | cancelled


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    status: Optional[str] = None