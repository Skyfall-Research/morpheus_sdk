from typing import Any, Dict, Optional
from pydantic import BaseModel

class ModelVerifyTicketInputs(BaseModel):
    ticket_id: Optional[str] = None


class ModelVerifyOutput(BaseModel):
    status: Optional[int] = None
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None