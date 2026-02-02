import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_shipments_by_warehouse_response_200 import GetWMSShipmentsByWarehouseResponse200
from ...models.get_wms_shipments_by_warehouse_status_item import GetWMSShipmentsByWarehouseStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    warehouse_id: str,
    *,
    status: Union[Unset, list[GetWMSShipmentsByWarehouseStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    carrier: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params["carrier"] = carrier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/shipments/warehouse/{warehouse_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSShipmentsByWarehouseResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSShipmentsByWarehouseResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSShipmentsByWarehouseResponse200]:
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
    status: Union[Unset, list[GetWMSShipmentsByWarehouseStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    carrier: Union[Unset, str] = UNSET,
) -> Response[GetWMSShipmentsByWarehouseResponse200]:
    """Get shipments by warehouse with filtering


    ## Get Shipments by Warehouse

    Retrieve all outbound shipments for a specific warehouse with optional status filtering.

    **Use Cases:**
    - Warehouse shipping dock management
    - Daily shipping volume analysis
    - Carrier pickup coordination
    - Outbound logistics planning

    **Field Mapping:**
    - Filters by `warehouseId`
    - Optional status filtering using `shipmentStatus` field


    Args:
        world_id (str):
        warehouse_id (str):
        status (Union[Unset, list[GetWMSShipmentsByWarehouseStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        carrier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSShipmentsByWarehouseResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        status=status,
        date_start=date_start,
        date_end=date_end,
        carrier=carrier,
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
    status: Union[Unset, list[GetWMSShipmentsByWarehouseStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    carrier: Union[Unset, str] = UNSET,
) -> Optional[GetWMSShipmentsByWarehouseResponse200]:
    """Get shipments by warehouse with filtering


    ## Get Shipments by Warehouse

    Retrieve all outbound shipments for a specific warehouse with optional status filtering.

    **Use Cases:**
    - Warehouse shipping dock management
    - Daily shipping volume analysis
    - Carrier pickup coordination
    - Outbound logistics planning

    **Field Mapping:**
    - Filters by `warehouseId`
    - Optional status filtering using `shipmentStatus` field


    Args:
        world_id (str):
        warehouse_id (str):
        status (Union[Unset, list[GetWMSShipmentsByWarehouseStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        carrier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSShipmentsByWarehouseResponse200
    """

    return sync_detailed(
        world_id=world_id,
        warehouse_id=warehouse_id,
        client=client,
        status=status,
        date_start=date_start,
        date_end=date_end,
        carrier=carrier,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSShipmentsByWarehouseStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    carrier: Union[Unset, str] = UNSET,
) -> Response[GetWMSShipmentsByWarehouseResponse200]:
    """Get shipments by warehouse with filtering


    ## Get Shipments by Warehouse

    Retrieve all outbound shipments for a specific warehouse with optional status filtering.

    **Use Cases:**
    - Warehouse shipping dock management
    - Daily shipping volume analysis
    - Carrier pickup coordination
    - Outbound logistics planning

    **Field Mapping:**
    - Filters by `warehouseId`
    - Optional status filtering using `shipmentStatus` field


    Args:
        world_id (str):
        warehouse_id (str):
        status (Union[Unset, list[GetWMSShipmentsByWarehouseStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        carrier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSShipmentsByWarehouseResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        status=status,
        date_start=date_start,
        date_end=date_end,
        carrier=carrier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSShipmentsByWarehouseStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    carrier: Union[Unset, str] = UNSET,
) -> Optional[GetWMSShipmentsByWarehouseResponse200]:
    """Get shipments by warehouse with filtering


    ## Get Shipments by Warehouse

    Retrieve all outbound shipments for a specific warehouse with optional status filtering.

    **Use Cases:**
    - Warehouse shipping dock management
    - Daily shipping volume analysis
    - Carrier pickup coordination
    - Outbound logistics planning

    **Field Mapping:**
    - Filters by `warehouseId`
    - Optional status filtering using `shipmentStatus` field


    Args:
        world_id (str):
        warehouse_id (str):
        status (Union[Unset, list[GetWMSShipmentsByWarehouseStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        carrier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSShipmentsByWarehouseResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            warehouse_id=warehouse_id,
            client=client,
            status=status,
            date_start=date_start,
            date_end=date_end,
            carrier=carrier,
        )
    ).parsed
