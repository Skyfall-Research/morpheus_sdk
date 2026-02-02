from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_replenishments_by_status_replenishment_type_item import (
    GetWMSReplenishmentsByStatusReplenishmentTypeItem,
)
from ...models.get_wms_replenishments_by_status_response_200 import GetWMSReplenishmentsByStatusResponse200
from ...models.get_wms_replenishments_by_status_status_item import GetWMSReplenishmentsByStatusStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: list[GetWMSReplenishmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    replenishment_type: Union[Unset, list[GetWMSReplenishmentsByStatusReplenishmentTypeItem]] = UNSET,
    priority: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status = []
    for status_item_data in status:
        status_item = status_item_data.value
        json_status.append(status_item)

    params["status"] = json_status

    params["warehouseId"] = warehouse_id

    params["productId"] = product_id

    json_replenishment_type: Union[Unset, list[str]] = UNSET
    if not isinstance(replenishment_type, Unset):
        json_replenishment_type = []
        for replenishment_type_item_data in replenishment_type:
            replenishment_type_item = replenishment_type_item_data.value
            json_replenishment_type.append(replenishment_type_item)

    params["replenishmentType"] = json_replenishment_type

    params["priority"] = priority

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/replenishments/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSReplenishmentsByStatusResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSReplenishmentsByStatusResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSReplenishmentsByStatusResponse200]:
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
    status: list[GetWMSReplenishmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    replenishment_type: Union[Unset, list[GetWMSReplenishmentsByStatusReplenishmentTypeItem]] = UNSET,
    priority: Union[Unset, float] = UNSET,
) -> Response[GetWMSReplenishmentsByStatusResponse200]:
    """Get replenishments by status


    ## Get Replenishments by Status

    Retrieve replenishments filtered by one or more status values with additional filtering options.

    **Status Workflow:**
    - SUGGESTED → Initial creation
    - APPROVED → Management approval
    - TASK_CREATED → Work order generated
    - IN_PROGRESS → Active execution
    - COMPLETED → Successfully finished
    - CANCELLED → Process terminated

    **Use Cases:**
    - Work queue management for operators
    - Status-based workflow processing
    - Priority-based task assignment
    - Performance monitoring by status

    **Field Mapping:**
    - Filters by `status` field using `$in` operator for multiple values
    - Supports priority filtering (greater than or equal to specified value)


    Args:
        world_id (str):
        status (list[GetWMSReplenishmentsByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        product_id (Union[Unset, str]):
        replenishment_type (Union[Unset,
            list[GetWMSReplenishmentsByStatusReplenishmentTypeItem]]):
        priority (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSReplenishmentsByStatusResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        product_id=product_id,
        replenishment_type=replenishment_type,
        priority=priority,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSReplenishmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    replenishment_type: Union[Unset, list[GetWMSReplenishmentsByStatusReplenishmentTypeItem]] = UNSET,
    priority: Union[Unset, float] = UNSET,
) -> Optional[GetWMSReplenishmentsByStatusResponse200]:
    """Get replenishments by status


    ## Get Replenishments by Status

    Retrieve replenishments filtered by one or more status values with additional filtering options.

    **Status Workflow:**
    - SUGGESTED → Initial creation
    - APPROVED → Management approval
    - TASK_CREATED → Work order generated
    - IN_PROGRESS → Active execution
    - COMPLETED → Successfully finished
    - CANCELLED → Process terminated

    **Use Cases:**
    - Work queue management for operators
    - Status-based workflow processing
    - Priority-based task assignment
    - Performance monitoring by status

    **Field Mapping:**
    - Filters by `status` field using `$in` operator for multiple values
    - Supports priority filtering (greater than or equal to specified value)


    Args:
        world_id (str):
        status (list[GetWMSReplenishmentsByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        product_id (Union[Unset, str]):
        replenishment_type (Union[Unset,
            list[GetWMSReplenishmentsByStatusReplenishmentTypeItem]]):
        priority (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSReplenishmentsByStatusResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        warehouse_id=warehouse_id,
        product_id=product_id,
        replenishment_type=replenishment_type,
        priority=priority,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSReplenishmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    replenishment_type: Union[Unset, list[GetWMSReplenishmentsByStatusReplenishmentTypeItem]] = UNSET,
    priority: Union[Unset, float] = UNSET,
) -> Response[GetWMSReplenishmentsByStatusResponse200]:
    """Get replenishments by status


    ## Get Replenishments by Status

    Retrieve replenishments filtered by one or more status values with additional filtering options.

    **Status Workflow:**
    - SUGGESTED → Initial creation
    - APPROVED → Management approval
    - TASK_CREATED → Work order generated
    - IN_PROGRESS → Active execution
    - COMPLETED → Successfully finished
    - CANCELLED → Process terminated

    **Use Cases:**
    - Work queue management for operators
    - Status-based workflow processing
    - Priority-based task assignment
    - Performance monitoring by status

    **Field Mapping:**
    - Filters by `status` field using `$in` operator for multiple values
    - Supports priority filtering (greater than or equal to specified value)


    Args:
        world_id (str):
        status (list[GetWMSReplenishmentsByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        product_id (Union[Unset, str]):
        replenishment_type (Union[Unset,
            list[GetWMSReplenishmentsByStatusReplenishmentTypeItem]]):
        priority (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSReplenishmentsByStatusResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        product_id=product_id,
        replenishment_type=replenishment_type,
        priority=priority,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSReplenishmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    replenishment_type: Union[Unset, list[GetWMSReplenishmentsByStatusReplenishmentTypeItem]] = UNSET,
    priority: Union[Unset, float] = UNSET,
) -> Optional[GetWMSReplenishmentsByStatusResponse200]:
    """Get replenishments by status


    ## Get Replenishments by Status

    Retrieve replenishments filtered by one or more status values with additional filtering options.

    **Status Workflow:**
    - SUGGESTED → Initial creation
    - APPROVED → Management approval
    - TASK_CREATED → Work order generated
    - IN_PROGRESS → Active execution
    - COMPLETED → Successfully finished
    - CANCELLED → Process terminated

    **Use Cases:**
    - Work queue management for operators
    - Status-based workflow processing
    - Priority-based task assignment
    - Performance monitoring by status

    **Field Mapping:**
    - Filters by `status` field using `$in` operator for multiple values
    - Supports priority filtering (greater than or equal to specified value)


    Args:
        world_id (str):
        status (list[GetWMSReplenishmentsByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        product_id (Union[Unset, str]):
        replenishment_type (Union[Unset,
            list[GetWMSReplenishmentsByStatusReplenishmentTypeItem]]):
        priority (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSReplenishmentsByStatusResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            warehouse_id=warehouse_id,
            product_id=product_id,
            replenishment_type=replenishment_type,
            priority=priority,
        )
    ).parsed
