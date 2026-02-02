from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_task_body import CreateWMSTaskBody
from ...models.create_wms_task_response_201 import CreateWMSTaskResponse201
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSTaskBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/tasks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateWMSTaskResponse201]:
    if response.status_code == 201:
        response_201 = CreateWMSTaskResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateWMSTaskResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSTaskBody,
) -> Response[CreateWMSTaskResponse201]:
    """Create task


    ## Create WMS Task

    Creates a new warehouse task for specific operations like picking, putaway, replenishment, etc.

    **Business Process:**
    - Creates structured work instructions for warehouse staff
    - Assigns task with priority-based sequencing
    - Supports various task types with detailed tracking
    - Enables performance measurement and optimization

    **Use Cases:**
    - Order fulfillment picking tasks
    - Inventory putaway operations
    - Replenishment movement tasks
    - Cycle counting assignments
    - Cross-docking operations

    **Field Mapping:**
    - Uses `taskId` as primary identifier (auto-generated using WMS service prefix)
    - Complex nested structures for assignment, timing, and performance tracking
    - Detailed product, location, and quantity specifications


    Args:
        world_id (str):
        body (CreateWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWMSTaskResponse201]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSTaskBody,
) -> Optional[CreateWMSTaskResponse201]:
    """Create task


    ## Create WMS Task

    Creates a new warehouse task for specific operations like picking, putaway, replenishment, etc.

    **Business Process:**
    - Creates structured work instructions for warehouse staff
    - Assigns task with priority-based sequencing
    - Supports various task types with detailed tracking
    - Enables performance measurement and optimization

    **Use Cases:**
    - Order fulfillment picking tasks
    - Inventory putaway operations
    - Replenishment movement tasks
    - Cycle counting assignments
    - Cross-docking operations

    **Field Mapping:**
    - Uses `taskId` as primary identifier (auto-generated using WMS service prefix)
    - Complex nested structures for assignment, timing, and performance tracking
    - Detailed product, location, and quantity specifications


    Args:
        world_id (str):
        body (CreateWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWMSTaskResponse201
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSTaskBody,
) -> Response[CreateWMSTaskResponse201]:
    """Create task


    ## Create WMS Task

    Creates a new warehouse task for specific operations like picking, putaway, replenishment, etc.

    **Business Process:**
    - Creates structured work instructions for warehouse staff
    - Assigns task with priority-based sequencing
    - Supports various task types with detailed tracking
    - Enables performance measurement and optimization

    **Use Cases:**
    - Order fulfillment picking tasks
    - Inventory putaway operations
    - Replenishment movement tasks
    - Cycle counting assignments
    - Cross-docking operations

    **Field Mapping:**
    - Uses `taskId` as primary identifier (auto-generated using WMS service prefix)
    - Complex nested structures for assignment, timing, and performance tracking
    - Detailed product, location, and quantity specifications


    Args:
        world_id (str):
        body (CreateWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWMSTaskResponse201]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSTaskBody,
) -> Optional[CreateWMSTaskResponse201]:
    """Create task


    ## Create WMS Task

    Creates a new warehouse task for specific operations like picking, putaway, replenishment, etc.

    **Business Process:**
    - Creates structured work instructions for warehouse staff
    - Assigns task with priority-based sequencing
    - Supports various task types with detailed tracking
    - Enables performance measurement and optimization

    **Use Cases:**
    - Order fulfillment picking tasks
    - Inventory putaway operations
    - Replenishment movement tasks
    - Cycle counting assignments
    - Cross-docking operations

    **Field Mapping:**
    - Uses `taskId` as primary identifier (auto-generated using WMS service prefix)
    - Complex nested structures for assignment, timing, and performance tracking
    - Detailed product, location, and quantity specifications


    Args:
        world_id (str):
        body (CreateWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWMSTaskResponse201
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
