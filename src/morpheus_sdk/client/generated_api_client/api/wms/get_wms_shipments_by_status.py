import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_shipments_by_status_response_200 import GetWMSShipmentsByStatusResponse200
from ...models.get_wms_shipments_by_status_status_item import GetWMSShipmentsByStatusStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: list[GetWMSShipmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    carrier_id: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status = []
    for status_item_data in status:
        status_item = status_item_data.value
        json_status.append(status_item)

    params["status"] = json_status

    params["warehouseId"] = warehouse_id

    params["carrierId"] = carrier_id

    params["serviceLevel"] = service_level

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/shipments/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSShipmentsByStatusResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSShipmentsByStatusResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSShipmentsByStatusResponse200]:
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
    status: list[GetWMSShipmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    carrier_id: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetWMSShipmentsByStatusResponse200]:
    """Get shipments filtered by status with advanced filtering


    **Status-Based Shipment Filtering**

    Retrieve outbound shipments filtered by status with comprehensive query capabilities.

    **Advanced Filtering Options:**
    - Multiple status selection
    - Warehouse-specific filtering
    - Carrier-specific filtering (uses carrier.name field)
    - Service level filtering
    - Date range filtering

    **Sorting Logic:**
    - Primary: Created date (descending - newest first)

    **Field Mapping Verified:**
    - Status field: `shipmentStatus` (consistent throughout model)
    - Carrier filter: `carrier.name` field mapping


    Args:
        world_id (str):
        status (list[GetWMSShipmentsByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        carrier_id (Union[Unset, str]):
        service_level (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSShipmentsByStatusResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        carrier_id=carrier_id,
        service_level=service_level,
        date_start=date_start,
        date_end=date_end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSShipmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    carrier_id: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetWMSShipmentsByStatusResponse200]:
    """Get shipments filtered by status with advanced filtering


    **Status-Based Shipment Filtering**

    Retrieve outbound shipments filtered by status with comprehensive query capabilities.

    **Advanced Filtering Options:**
    - Multiple status selection
    - Warehouse-specific filtering
    - Carrier-specific filtering (uses carrier.name field)
    - Service level filtering
    - Date range filtering

    **Sorting Logic:**
    - Primary: Created date (descending - newest first)

    **Field Mapping Verified:**
    - Status field: `shipmentStatus` (consistent throughout model)
    - Carrier filter: `carrier.name` field mapping


    Args:
        world_id (str):
        status (list[GetWMSShipmentsByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        carrier_id (Union[Unset, str]):
        service_level (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSShipmentsByStatusResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        warehouse_id=warehouse_id,
        carrier_id=carrier_id,
        service_level=service_level,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSShipmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    carrier_id: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetWMSShipmentsByStatusResponse200]:
    """Get shipments filtered by status with advanced filtering


    **Status-Based Shipment Filtering**

    Retrieve outbound shipments filtered by status with comprehensive query capabilities.

    **Advanced Filtering Options:**
    - Multiple status selection
    - Warehouse-specific filtering
    - Carrier-specific filtering (uses carrier.name field)
    - Service level filtering
    - Date range filtering

    **Sorting Logic:**
    - Primary: Created date (descending - newest first)

    **Field Mapping Verified:**
    - Status field: `shipmentStatus` (consistent throughout model)
    - Carrier filter: `carrier.name` field mapping


    Args:
        world_id (str):
        status (list[GetWMSShipmentsByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        carrier_id (Union[Unset, str]):
        service_level (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSShipmentsByStatusResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        carrier_id=carrier_id,
        service_level=service_level,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSShipmentsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    carrier_id: Union[Unset, str] = UNSET,
    service_level: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetWMSShipmentsByStatusResponse200]:
    """Get shipments filtered by status with advanced filtering


    **Status-Based Shipment Filtering**

    Retrieve outbound shipments filtered by status with comprehensive query capabilities.

    **Advanced Filtering Options:**
    - Multiple status selection
    - Warehouse-specific filtering
    - Carrier-specific filtering (uses carrier.name field)
    - Service level filtering
    - Date range filtering

    **Sorting Logic:**
    - Primary: Created date (descending - newest first)

    **Field Mapping Verified:**
    - Status field: `shipmentStatus` (consistent throughout model)
    - Carrier filter: `carrier.name` field mapping


    Args:
        world_id (str):
        status (list[GetWMSShipmentsByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        carrier_id (Union[Unset, str]):
        service_level (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSShipmentsByStatusResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            warehouse_id=warehouse_id,
            carrier_id=carrier_id,
            service_level=service_level,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
