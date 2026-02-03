import logging
from ...models.model_act import ModelActInputs, ModelActObservation
from ...client.api.act import Act, AsyncAct

logger = logging.getLogger("morpheus_sdk")

def execute_act_sync(wrapper: Act, inputs: ModelActInputs) -> ModelActObservation:
    try:
        response = wrapper.call(
            path=inputs.path,
            method=inputs.method,
            body=inputs.body,
            query_params=inputs.query_params,
            path_params=inputs.path_params
        )
        
        return ModelActObservation(
            success=True, 
            status=200, 
            data=response.to_dict() if hasattr(response, "to_dict") else response
        )
    except Exception as e:
        logger.error(f"Act failed: {e}")
        return ModelActObservation(success=False, status=500, error=str(e))

async def execute_act_async(wrapper: AsyncAct, inputs: ModelActInputs) -> ModelActObservation:
    try:
        response = await wrapper.call(
            path=inputs.path,
            method=inputs.method,
            body=inputs.body,
            query_params=inputs.query_params,
            path_params=inputs.path_params
        )
        
        return ModelActObservation(
            success=True, 
            status=200, 
            data=response.to_dict() if hasattr(response, "to_dict") else response
        )
    except Exception as e:
        logger.error(f"Act failed: {e}")
        return ModelActObservation(success=False, status=500, error=str(e))
