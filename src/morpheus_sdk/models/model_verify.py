from typing import Any, Dict, Optional
from pydantic import BaseModel

class ModelVerifyInputs(BaseModel):
    ticket_id: Optional[str] = None


class ModelVerifyOutputs(BaseModel):
    status: Optional[int] = None
    data: Optional[Dict[str, Any]] = None
    success: Optional[bool] = None
    error: Optional[str] = None