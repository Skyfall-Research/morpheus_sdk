from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_orders_ready_for_picking_order_type_item import GetWMSOrdersReadyForPickingOrderTypeItem
from ...models.get_wms_orders_ready_for_picking_priority_item import GetWMSOrdersReadyForPickingPriorityItem
from ...models.get_wms_orders_ready_for_picking_response_200 import GetWMSOrdersReadyForPickingResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    warehouse_id: str,
    *,
    priority: Union[Unset, list[GetWMSOrdersReadyForPickingPriorityItem]] = UNSET,
    order_type: Union[Unset, list[GetWMSOrdersReadyForPickingOrderTypeItem]] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_priority: Union[Unset, list[str]] = UNSET
    if not isinstance(priority, Unset):
        json_priority = []
        for priority_item_data in priority:
            priority_item = priority_item_data.value
            json_priority.append(priority_item)

    params["priority"] = json_priority

    json_order_type: Union[Unset, list[str]] = UNSET
    if not isinstance(order_type, Unset):
        json_order_type = []
        for order_type_item_data in order_type:
            order_type_item = order_type_item_data.value
            json_order_type.append(order_type_item)

    params["orderType"] = json_order_type

    params["customerId"] = customer_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/outbound-orders/ready-for-picking/{warehouse_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSOrdersReadyForPickingResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSOrdersReadyForPickingResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSOrdersReadyForPickingResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    priority: Union[Unset, list[GetWMSOrdersReadyForPickingPriorityItem]] = UNSET,
    order_type: Union[Unset, list[GetWMSOrdersReadyForPickingOrderTypeItem]] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
) -> Response[GetWMSOrdersReadyForPickingResponse200]:
    """Get orders ready for picking


    ## Get Orders Ready for Picking

    Retrieve all outbound orders that are fully allocated and ready to be picked in a specific
    warehouse.

    **Business Logic:**
    - Filters for orders with status **ALLOCATED** or **PARTIALLY_PICKED**
    - Ensures inventory is reserved and available for picking
    - Prioritizes orders based on ship date and priority level

    **Use Cases:**
    - Warehouse floor operations planning
    - Wave picking generation
    - Labor resource allocation


    Args:
        world_id (str):
        warehouse_id (str):
        priority (Union[Unset, list[GetWMSOrdersReadyForPickingPriorityItem]]):
        order_type (Union[Unset, list[GetWMSOrdersReadyForPickingOrderTypeItem]]):
        customer_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSOrdersReadyForPickingResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        priority=priority,
        order_type=order_type,
        customer_id=customer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    priority: Union[Unset, list[GetWMSOrdersReadyForPickingPriorityItem]] = UNSET,
    order_type: Union[Unset, list[GetWMSOrdersReadyForPickingOrderTypeItem]] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
) -> Optional[GetWMSOrdersReadyForPickingResponse200]:
    """Get orders ready for picking


    ## Get Orders Ready for Picking

    Retrieve all outbound orders that are fully allocated and ready to be picked in a specific
    warehouse.

    **Business Logic:**
    - Filters for orders with status **ALLOCATED** or **PARTIALLY_PICKED**
    - Ensures inventory is reserved and available for picking
    - Prioritizes orders based on ship date and priority level

    **Use Cases:**
    - Warehouse floor operations planning
    - Wave picking generation
    - Labor resource allocation


    Args:
        world_id (str):
        warehouse_id (str):
        priority (Union[Unset, list[GetWMSOrdersReadyForPickingPriorityItem]]):
        order_type (Union[Unset, list[GetWMSOrdersReadyForPickingOrderTypeItem]]):
        customer_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSOrdersReadyForPickingResponse200
    """

    return sync_detailed(
        world_id=world_id,
        warehouse_id=warehouse_id,
        client=client,
        priority=priority,
        order_type=order_type,
        customer_id=customer_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    priority: Union[Unset, list[GetWMSOrdersReadyForPickingPriorityItem]] = UNSET,
    order_type: Union[Unset, list[GetWMSOrdersReadyForPickingOrderTypeItem]] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
) -> Response[GetWMSOrdersReadyForPickingResponse200]:
    """Get orders ready for picking


    ## Get Orders Ready for Picking

    Retrieve all outbound orders that are fully allocated and ready to be picked in a specific
    warehouse.

    **Business Logic:**
    - Filters for orders with status **ALLOCATED** or **PARTIALLY_PICKED**
    - Ensures inventory is reserved and available for picking
    - Prioritizes orders based on ship date and priority level

    **Use Cases:**
    - Warehouse floor operations planning
    - Wave picking generation
    - Labor resource allocation


    Args:
        world_id (str):
        warehouse_id (str):
        priority (Union[Unset, list[GetWMSOrdersReadyForPickingPriorityItem]]):
        order_type (Union[Unset, list[GetWMSOrdersReadyForPickingOrderTypeItem]]):
        customer_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSOrdersReadyForPickingResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        priority=priority,
        order_type=order_type,
        customer_id=customer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    priority: Union[Unset, list[GetWMSOrdersReadyForPickingPriorityItem]] = UNSET,
    order_type: Union[Unset, list[GetWMSOrdersReadyForPickingOrderTypeItem]] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
) -> Optional[GetWMSOrdersReadyForPickingResponse200]:
    """Get orders ready for picking


    ## Get Orders Ready for Picking

    Retrieve all outbound orders that are fully allocated and ready to be picked in a specific
    warehouse.

    **Business Logic:**
    - Filters for orders with status **ALLOCATED** or **PARTIALLY_PICKED**
    - Ensures inventory is reserved and available for picking
    - Prioritizes orders based on ship date and priority level

    **Use Cases:**
    - Warehouse floor operations planning
    - Wave picking generation
    - Labor resource allocation


    Args:
        world_id (str):
        warehouse_id (str):
        priority (Union[Unset, list[GetWMSOrdersReadyForPickingPriorityItem]]):
        order_type (Union[Unset, list[GetWMSOrdersReadyForPickingOrderTypeItem]]):
        customer_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSOrdersReadyForPickingResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            warehouse_id=warehouse_id,
            client=client,
            priority=priority,
            order_type=order_type,
            customer_id=customer_id,
        )
    ).parsed
