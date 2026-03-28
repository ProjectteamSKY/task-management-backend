from pydantic import BaseModel, model_validator
from datetime import date, time
from typing import Optional
from math import ceil

class ScheduleCreate(BaseModel):
    worker_id: int
    task_id: Optional[int] = None      # NULL for leave slots
    date: date
    start_time: time
    end_time: time
    duration_units: int = 0            # auto-calculated: 1 unit = 15 mins
    status: str                        # allocated | leave | available

    @model_validator(mode="after")
    def calculate_duration(self):
        from datetime import datetime
        start = datetime.combine(self.date, self.start_time)
        end   = datetime.combine(self.date, self.end_time)
        diff_minutes = (end - start).seconds // 60
        self.duration_units = ceil(diff_minutes / 15)
        return self