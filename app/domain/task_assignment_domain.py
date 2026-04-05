from pydantic import BaseModel
from typing import Optional


class AssignmentCreate(BaseModel):
    task_id:         int
    worker_id:       int
    allocated_hours: float        # ✅ changed from int
    status:          str = "pending"  
    start_date:      str              
    end_date:        str              
    start_time:      str               
    end_time:        str               
    duration_units:  float = 2.0      # ✅ changed from int (e.g. 1.5 days)


class AssignmentUpdate(BaseModel):
    allocated_hours: Optional[float] = None   # ✅ changed from int
    status:          Optional[str] = None
    start_date:      Optional[str] = None
    end_date:        Optional[str] = None
    start_time:      Optional[str] = None
    end_time:        Optional[str] = None
    duration_units:  Optional[float] = None   # ✅ changed from int