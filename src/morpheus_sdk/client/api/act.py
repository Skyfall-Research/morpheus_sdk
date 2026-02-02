from typing import Any, Dict, Optional, Union

from ...client.generated_api_client.client import Client
from ...client.generated_api_client.api.world import act
from ...client.generated_api_client.models.act_body import ActBody
from ...client.generated_api_client.models.act_body_params import ActBodyParams
from ...client.generated_api_client.models.act_body_query import ActBodyQuery
from ...client.generated_api_client.models.act_body_body import ActBodyBody
from ...client.generated_api_client.models.act_response_200 import ActResponse200

class Act:
    def __init__(self, client: Client):
        self.client = client

    def call(
        self, 
        path: str, 
        method: str = "GET", 
        query_params: Optional[Dict[str, Any]] = None, 
        path_params: Optional[Dict[str, Any]] = None, 
        body: Optional[Dict[str, Any]] = None
    ) -> Union[ActResponse200, Any]:
        """
        Execute a dynamic internal API call.
        """
        # Construct ActBody parts
        act_params_obj = None
        if path_params is not None:
            act_params_obj = ActBodyParams.from_dict(path_params)

        act_query_obj = None
        if query_params is not None:
            act_query_obj = ActBodyQuery.from_dict(query_params)

        act_body_obj = None
        if body is not None:
            act_body_obj = ActBodyBody.from_dict(body)

        # Re-construct with kwargs to be safe about UNSET
        act_body_kwargs = {
            "path": path,
            "method": method
        }
        if act_params_obj:
            act_body_kwargs["params"] = act_params_obj
        if act_query_obj:
            act_body_kwargs["query"] = act_query_obj
        if act_body_obj:
            act_body_kwargs["body"] = act_body_obj
            
        act_ref = ActBody(**act_body_kwargs)

        response = act.sync_detailed(
            client=self.client,
            body=act_ref
        )

        if response.status_code == 200:
            if isinstance(response.parsed, ActResponse200):
                return response.parsed
            return response.parsed # It might be Any
        else:
             raise Exception(f"Failed to execute act: {response.status_code} {response.content}")


class AsyncAct:
    def __init__(self, client: Client):
        self.client = client

    async def call(
        self, 
        path: str, 
        method: str = "GET", 
        query_params: Optional[Dict[str, Any]] = None, 
        path_params: Optional[Dict[str, Any]] = None, 
        body: Optional[Dict[str, Any]] = None
    ) -> Union[ActResponse200, Any]:
        """
        Execute a dynamic internal API call.
        """
        # Construct ActBody parts
        act_params_obj = None
        if path_params is not None:
            act_params_obj = ActBodyParams.from_dict(path_params)

        act_query_obj = None
        if query_params is not None:
            act_query_obj = ActBodyQuery.from_dict(query_params)

        act_body_obj = None
        if body is not None:
            act_body_obj = ActBodyBody.from_dict(body)

        # Re-construct with kwargs to be safe about UNSET
        act_body_kwargs = {
            "path": path,
            "method": method
        }
        if act_params_obj:
            act_body_kwargs["params"] = act_params_obj
        if act_query_obj:
            act_body_kwargs["query"] = act_query_obj
        if act_body_obj:
            act_body_kwargs["body"] = act_body_obj
            
        act_ref = ActBody(**act_body_kwargs)

        response = await act.asyncio_detailed(
            client=self.client,
            body=act_ref
        )

        if response.status_code == 200:
            if isinstance(response.parsed, ActResponse200):
                return response.parsed
            return response.parsed # It might be Any
        else:
             raise Exception(f"Failed to execute act: {response.status_code} {response.content}")
