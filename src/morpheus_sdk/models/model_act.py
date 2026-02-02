from typing import Optional
from typing import Literal
from pydantic import BaseModel

class ModelActInputs(BaseModel):
    action_string: str
    verb: Literal["POST", "GET", "PUT", "DELETE", "PATCH"]
    data: Optional[dict[str, Any]] = None
    params: Optional[dict[str, Any]] = None
    
class ModelActObservation(BaseModel):
    action_response: Optional[dict[str, Any]] = None
    status: Optional[int] = None
    data: Optional[dict[str, Any]] = None
    success: Optional[bool] = None
    error: Optional[str] = None