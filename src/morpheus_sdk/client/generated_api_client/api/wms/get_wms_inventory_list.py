from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inventory_list_expiring_soon import GetWMSInventoryListExpiringSoon
from ...models.get_wms_inventory_list_response_200 import GetWMSInventoryListResponse200
from ...models.get_wms_inventory_list_status_item import GetWMSInventoryListStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: Union[Unset, list[GetWMSInventoryListStatusItem]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    expiring_soon: Union[Unset, GetWMSInventoryListExpiringSoon] = UNSET,
    search: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params["warehouseId"] = warehouse_id

    json_expiring_soon: Union[Unset, str] = UNSET
    if not isinstance(expiring_soon, Unset):
        json_expiring_soon = expiring_soon.value

    params["expiringSoon"] = json_expiring_soon

    params["search"] = search

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inventory",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInventoryListResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInventoryListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetWMSInventoryListResponse200]]:
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
    status: Union[Unset, list[GetWMSInventoryListStatusItem]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    expiring_soon: Union[Unset, GetWMSInventoryListExpiringSoon] = UNSET,
    search: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, GetWMSInventoryListResponse200]]:
    """Get inventory list


    ## Get WMS Inventory List

    Retrieve a paginated list of inventory items with comprehensive filtering options for inventory
    management and monitoring.

    ### Features
    - **Paginated Results**: Efficient handling of large inventory datasets
    - **Multi-Filter Support**: Filter by status, warehouse, expiration, and search terms
    - **Search Capability**: Search by SKU or product name with case-insensitive matching
    - **Alert Filtering**: Filter for expiring items requiring attention
    - **Sorting**: Results sorted by last movement date and SKU

    ### Query Parameters
    - **status**: Filter by inventory status (supports multiple values)
    - **warehouseId**: Filter by specific warehouse facility
    - **expiringSoon**: Filter for items expiring within 7 days
    - **search**: Search by SKU or product name
    - **limit**: Maximum results per page (default: 50, max: 100)
    - **offset**: Pagination offset for result navigation

    ### Use Cases
    - **Inventory Management**: Browse and manage warehouse inventory
    - **Expiration Monitoring**: Track items approaching expiration dates
    - **Stock Lookup**: Find specific products by SKU or name
    - **Status Tracking**: Monitor inventory status distribution


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, list[GetWMSInventoryListStatusItem]]):
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        expiring_soon (Union[Unset, GetWMSInventoryListExpiringSoon]):  Example: true.
        search (Union[Unset, str]):  Example: WIDGET-001.
        limit (Union[Unset, int]):  Default: 50. Example: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryListResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        expiring_soon=expiring_soon,
        search=search,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSInventoryListStatusItem]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    expiring_soon: Union[Unset, GetWMSInventoryListExpiringSoon] = UNSET,
    search: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, GetWMSInventoryListResponse200]]:
    """Get inventory list


    ## Get WMS Inventory List

    Retrieve a paginated list of inventory items with comprehensive filtering options for inventory
    management and monitoring.

    ### Features
    - **Paginated Results**: Efficient handling of large inventory datasets
    - **Multi-Filter Support**: Filter by status, warehouse, expiration, and search terms
    - **Search Capability**: Search by SKU or product name with case-insensitive matching
    - **Alert Filtering**: Filter for expiring items requiring attention
    - **Sorting**: Results sorted by last movement date and SKU

    ### Query Parameters
    - **status**: Filter by inventory status (supports multiple values)
    - **warehouseId**: Filter by specific warehouse facility
    - **expiringSoon**: Filter for items expiring within 7 days
    - **search**: Search by SKU or product name
    - **limit**: Maximum results per page (default: 50, max: 100)
    - **offset**: Pagination offset for result navigation

    ### Use Cases
    - **Inventory Management**: Browse and manage warehouse inventory
    - **Expiration Monitoring**: Track items approaching expiration dates
    - **Stock Lookup**: Find specific products by SKU or name
    - **Status Tracking**: Monitor inventory status distribution


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, list[GetWMSInventoryListStatusItem]]):
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        expiring_soon (Union[Unset, GetWMSInventoryListExpiringSoon]):  Example: true.
        search (Union[Unset, str]):  Example: WIDGET-001.
        limit (Union[Unset, int]):  Default: 50. Example: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryListResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        warehouse_id=warehouse_id,
        expiring_soon=expiring_soon,
        search=search,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSInventoryListStatusItem]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    expiring_soon: Union[Unset, GetWMSInventoryListExpiringSoon] = UNSET,
    search: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, GetWMSInventoryListResponse200]]:
    """Get inventory list


    ## Get WMS Inventory List

    Retrieve a paginated list of inventory items with comprehensive filtering options for inventory
    management and monitoring.

    ### Features
    - **Paginated Results**: Efficient handling of large inventory datasets
    - **Multi-Filter Support**: Filter by status, warehouse, expiration, and search terms
    - **Search Capability**: Search by SKU or product name with case-insensitive matching
    - **Alert Filtering**: Filter for expiring items requiring attention
    - **Sorting**: Results sorted by last movement date and SKU

    ### Query Parameters
    - **status**: Filter by inventory status (supports multiple values)
    - **warehouseId**: Filter by specific warehouse facility
    - **expiringSoon**: Filter for items expiring within 7 days
    - **search**: Search by SKU or product name
    - **limit**: Maximum results per page (default: 50, max: 100)
    - **offset**: Pagination offset for result navigation

    ### Use Cases
    - **Inventory Management**: Browse and manage warehouse inventory
    - **Expiration Monitoring**: Track items approaching expiration dates
    - **Stock Lookup**: Find specific products by SKU or name
    - **Status Tracking**: Monitor inventory status distribution


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, list[GetWMSInventoryListStatusItem]]):
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        expiring_soon (Union[Unset, GetWMSInventoryListExpiringSoon]):  Example: true.
        search (Union[Unset, str]):  Example: WIDGET-001.
        limit (Union[Unset, int]):  Default: 50. Example: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryListResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        expiring_soon=expiring_soon,
        search=search,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSInventoryListStatusItem]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    expiring_soon: Union[Unset, GetWMSInventoryListExpiringSoon] = UNSET,
    search: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, GetWMSInventoryListResponse200]]:
    """Get inventory list


    ## Get WMS Inventory List

    Retrieve a paginated list of inventory items with comprehensive filtering options for inventory
    management and monitoring.

    ### Features
    - **Paginated Results**: Efficient handling of large inventory datasets
    - **Multi-Filter Support**: Filter by status, warehouse, expiration, and search terms
    - **Search Capability**: Search by SKU or product name with case-insensitive matching
    - **Alert Filtering**: Filter for expiring items requiring attention
    - **Sorting**: Results sorted by last movement date and SKU

    ### Query Parameters
    - **status**: Filter by inventory status (supports multiple values)
    - **warehouseId**: Filter by specific warehouse facility
    - **expiringSoon**: Filter for items expiring within 7 days
    - **search**: Search by SKU or product name
    - **limit**: Maximum results per page (default: 50, max: 100)
    - **offset**: Pagination offset for result navigation

    ### Use Cases
    - **Inventory Management**: Browse and manage warehouse inventory
    - **Expiration Monitoring**: Track items approaching expiration dates
    - **Stock Lookup**: Find specific products by SKU or name
    - **Status Tracking**: Monitor inventory status distribution


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, list[GetWMSInventoryListStatusItem]]):
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        expiring_soon (Union[Unset, GetWMSInventoryListExpiringSoon]):  Example: true.
        search (Union[Unset, str]):  Example: WIDGET-001.
        limit (Union[Unset, int]):  Default: 50. Example: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryListResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            warehouse_id=warehouse_id,
            expiring_soon=expiring_soon,
            search=search,
            limit=limit,
            offset=offset,
        )
    ).parsed
