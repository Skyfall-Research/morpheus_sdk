import logging
from typing import Optional
from ...models.model_verify import ModelVerifyInputs, ModelVerifyTicketInputs, ModelVerifyEntityInputs, ModelVerifyOutput
from ...client.api.verify import Verify, AsyncVerify

logger = logging.getLogger("morpheus_sdk")

def execute_verify_sync(wrapper: Optional[Verify], inputs: ModelVerifyInputs) -> ModelVerifyOutput:
    if not wrapper:
        return ModelVerifyOutput(status=400, error="World not initialized")
        
    try:
        if isinstance(inputs, ModelVerifyTicketInputs):
            res = wrapper.ticket(ticket_id=inputs.ticket_id)
        elif isinstance(inputs, ModelVerifyEntityInputs):
            res = wrapper.entity(
                od_id=inputs.od_id,
                entity_id=inputs.entity_id,
                entity_type=inputs.entity_type
            )
        else:
            return ModelVerifyOutput(status=400, error="Invalid verify inputs")
        
        return ModelVerifyOutput(
            status=200, 
            data=res.to_dict() if hasattr(res, "to_dict") else res
        )
    except Exception as e:
        logger.error(f"Verify failed: {e}")
        return ModelVerifyOutput(status=500, error=str(e))

async def execute_verify_async(wrapper: Optional[AsyncVerify], inputs: ModelVerifyInputs) -> ModelVerifyOutput:
    if not wrapper:
        return ModelVerifyOutput(status=400, error="World not initialized")
    try:
        if isinstance(inputs, ModelVerifyTicketInputs):
            res = await wrapper.ticket(ticket_id=inputs.ticket_id)
        elif isinstance(inputs, ModelVerifyEntityInputs):
            res = await wrapper.entity(
                od_id=inputs.od_id,
                entity_id=inputs.entity_id,
                entity_type=inputs.entity_type
            )
        else:
             return ModelVerifyOutput(status=400, error="Invalid verify inputs")
        return ModelVerifyOutput(
            status=200, 
            data=res.to_dict() if hasattr(res, "to_dict") else res
        )
    except Exception as e:
        logger.error(f"Verify failed: {e}")
        return ModelVerifyOutput(status=500, error=str(e))
