from typing import Any, Dict, Optional, Union
from pydantic import BaseModel

class ModelVerifyTicketInputs(BaseModel):
    ticket_id: str

class ModelVerifyEntityInputs(BaseModel):
    od_id: str
    entity_id: Optional[str] = None
    entity_type: Optional[str] = None

ModelVerifyInputs = Union[ModelVerifyTicketInputs, ModelVerifyEntityInputs]


class ModelVerifyOutput(BaseModel):
    status: Optional[int] = None
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None