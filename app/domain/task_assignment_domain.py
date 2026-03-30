from pydantic import BaseModel
from typing import Optional


class AssignmentCreate(BaseModel):
    task_id:         int
    worker_id:       int
    allocated_hours: int
    status:          str = "pending"  
    start_date:      str              
    end_date:        str              
    start_time:      str               
    end_time:        str               
    duration_units:  int = 2           


class AssignmentUpdate(BaseModel):
    allocated_hours: Optional[int] = None
    status:          Optional[str] = None
    start_date:      Optional[str] = None
    end_date:        Optional[str] = None
    start_time:      Optional[str] = None
    end_time:        Optional[str] = None
    duration_units:  Optional[int] = None