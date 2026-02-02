from typing import Optional, Dict, Any, Literal
from datetime import datetime
from pydantic import BaseModel

class ModelTaskFilters(BaseModel):
    task_id: Optional[str] = None
    status: Literal["new", "open", "in_progress", "on_hold", "resolved", "closed"] = "new"
    priority: Literal["low", "medium", "high", "critical"] = "low"
    include_process: Optional[bool] = False
    cursor: Optional[str] = None
    limit: Optional[int] = None


class ModelTaskInputs(BaseModel):
    time_start: Optional[datetime] = None
    time_end: Optional[datetime] = None
    filters: Optional[ModelTaskFilters] = None
    

class ModelTaskOutputs(BaseModel):
    status: Optional[int] = None
    data: Optional[Dict[str, Any]] = None
    success: Optional[bool] = None
    error: Optional[str] = None
    

    