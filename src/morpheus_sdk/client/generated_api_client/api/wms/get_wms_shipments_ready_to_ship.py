from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_shipments_ready_to_ship_response_200 import GetWMSShipmentsReadyToShipResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    warehouse_id: str,
    *,
    carrier: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    priority_orders: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["carrier"] = carrier

    params["serviceLevel"] = service_level

    params["priorityOrders"] = priority_orders

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/shipments/ready-to-ship/{warehouse_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSShipmentsReadyToShipResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSShipmentsReadyToShipResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSShipmentsReadyToShipResponse200]:
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
    carrier: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    priority_orders: Union[Unset, bool] = UNSET,
) -> Response[GetWMSShipmentsReadyToShipResponse200]:
    """Get shipments ready for dispatch


    ## Get Shipments Ready for Dispatch

    Retrieve all outbound shipments that are manifested and ready to be dispatched from a specific
    warehouse.

    **Business Logic:**
    - Filters for shipments with status **MANIFESTED**
    - Prioritizes shipments based on estimated delivery date and carrier service level
    - Ensures all required documentation is complete

    **Filtering Capabilities:**
    - Carrier-specific filtering
    - Service level filtering
    - Priority order handling

    **Sorting Logic:**
    - Priority (descending - high priority first)
    - Estimated delivery date (ascending - urgent deliveries first)
    - Created date (ascending - oldest first)


    Args:
        world_id (str):
        warehouse_id (str):
        carrier (Union[Unset, str]):
        service_level (Union[Unset, str]):
        priority_orders (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSShipmentsReadyToShipResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        carrier=carrier,
        service_level=service_level,
        priority_orders=priority_orders,
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
    carrier: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    priority_orders: Union[Unset, bool] = UNSET,
) -> Optional[GetWMSShipmentsReadyToShipResponse200]:
    """Get shipments ready for dispatch


    ## Get Shipments Ready for Dispatch

    Retrieve all outbound shipments that are manifested and ready to be dispatched from a specific
    warehouse.

    **Business Logic:**
    - Filters for shipments with status **MANIFESTED**
    - Prioritizes shipments based on estimated delivery date and carrier service level
    - Ensures all required documentation is complete

    **Filtering Capabilities:**
    - Carrier-specific filtering
    - Service level filtering
    - Priority order handling

    **Sorting Logic:**
    - Priority (descending - high priority first)
    - Estimated delivery date (ascending - urgent deliveries first)
    - Created date (ascending - oldest first)


    Args:
        world_id (str):
        warehouse_id (str):
        carrier (Union[Unset, str]):
        service_level (Union[Unset, str]):
        priority_orders (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSShipmentsReadyToShipResponse200
    """

    return sync_detailed(
        world_id=world_id,
        warehouse_id=warehouse_id,
        client=client,
        carrier=carrier,
        service_level=service_level,
        priority_orders=priority_orders,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    carrier: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    priority_orders: Union[Unset, bool] = UNSET,
) -> Response[GetWMSShipmentsReadyToShipResponse200]:
    """Get shipments ready for dispatch


    ## Get Shipments Ready for Dispatch

    Retrieve all outbound shipments that are manifested and ready to be dispatched from a specific
    warehouse.

    **Business Logic:**
    - Filters for shipments with status **MANIFESTED**
    - Prioritizes shipments based on estimated delivery date and carrier service level
    - Ensures all required documentation is complete

    **Filtering Capabilities:**
    - Carrier-specific filtering
    - Service level filtering
    - Priority order handling

    **Sorting Logic:**
    - Priority (descending - high priority first)
    - Estimated delivery date (ascending - urgent deliveries first)
    - Created date (ascending - oldest first)


    Args:
        world_id (str):
        warehouse_id (str):
        carrier (Union[Unset, str]):
        service_level (Union[Unset, str]):
        priority_orders (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSShipmentsReadyToShipResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        carrier=carrier,
        service_level=service_level,
        priority_orders=priority_orders,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    carrier: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    priority_orders: Union[Unset, bool] = UNSET,
) -> Optional[GetWMSShipmentsReadyToShipResponse200]:
    """Get shipments ready for dispatch


    ## Get Shipments Ready for Dispatch

    Retrieve all outbound shipments that are manifested and ready to be dispatched from a specific
    warehouse.

    **Business Logic:**
    - Filters for shipments with status **MANIFESTED**
    - Prioritizes shipments based on estimated delivery date and carrier service level
    - Ensures all required documentation is complete

    **Filtering Capabilities:**
    - Carrier-specific filtering
    - Service level filtering
    - Priority order handling

    **Sorting Logic:**
    - Priority (descending - high priority first)
    - Estimated delivery date (ascending - urgent deliveries first)
    - Created date (ascending - oldest first)


    Args:
        world_id (str):
        warehouse_id (str):
        carrier (Union[Unset, str]):
        service_level (Union[Unset, str]):
        priority_orders (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSShipmentsReadyToShipResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            warehouse_id=warehouse_id,
            client=client,
            carrier=carrier,
            service_level=service_level,
            priority_orders=priority_orders,
        )
    ).parsed
