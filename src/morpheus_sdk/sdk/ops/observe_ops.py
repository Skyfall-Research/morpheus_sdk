import logging
from typing import Optional
from ...models.model_state import ModelStateInputs, ModelStateOutputs
from ...client.api.observation import Observation, AsyncObservation

logger = logging.getLogger("morpheus_sdk")

def execute_observe_sync(wrapper: Optional[Observation], inputs: ModelStateInputs, world_id: Optional[str]) -> ModelStateOutputs:
    if not wrapper:
         return ModelStateOutputs(success=False, status=400, error="World not initialized")
         
    try:
        data = {}
        if inputs.include.get("audit_log"):
            audit_res = wrapper.audit(
                date_start=inputs.time_start,
                date_end=inputs.time_end
            )
            data["audit_log"] = audit_res.to_dict() if hasattr(audit_res, "to_dict") else audit_res
        
        if inputs.include.get("logs"):
            logs_res = wrapper.operational(
                date_start=inputs.time_start,
                date_end=inputs.time_end,
                limit=inputs.limit if inputs.limit else 100,
                cursor=str(inputs.offset) if inputs.offset else None
            )
            data["logs"] = logs_res.to_dict() if hasattr(logs_res, "to_dict") else logs_res
        
        return ModelStateOutputs(
            success=True,
            status=200, 
            world_id=world_id,
            data=data
        )
    except Exception as e:
        logger.error(f"Observe failed: {e}")
        return ModelStateOutputs(success=False, status=500, error=str(e))

async def execute_observe_async(wrapper: Optional[AsyncObservation], inputs: ModelStateInputs, world_id: Optional[str]) -> ModelStateOutputs:
    if not wrapper:
         return ModelStateOutputs(success=False, status=400, error="World not initialized")
    try:
        data = {}
        if inputs.include.get("audit_log"):
            audit_res = await wrapper.audit(
                date_start=inputs.time_start,
                date_end=inputs.time_end
            )
            data["audit_log"] = audit_res.to_dict() if hasattr(audit_res, "to_dict") else audit_res
        
        if inputs.include.get("logs"):
            logs_res = await wrapper.operational(
                date_start=inputs.time_start,
                date_end=inputs.time_end,
                limit=inputs.limit if inputs.limit else 100,
                cursor=str(inputs.offset) if inputs.offset else None
            )
            data["logs"] = logs_res.to_dict() if hasattr(logs_res, "to_dict") else logs_res
        
        return ModelStateOutputs(
            success=True,
            status=200, 
            world_id=world_id,
            data=data
        )
    except Exception as e:
        logger.error(f"Observe failed: {e}")
        return ModelStateOutputs(success=False, status=500, error=str(e))
