import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inventory_adjustments_response_200 import GetWMSInventoryAdjustmentsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inventory-transactions/adjustments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInventoryAdjustmentsResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]]:
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
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]]:
    r"""Get inventory adjustments


    ## Get WMS Inventory Adjustments

    Retrieve inventory adjustment transactions for audit, compliance, and variance analysis.

    ### Features
    - **Adjustment-Specific Filtering**: Automatically filters for transactionType = \"ADJUST\"
    - **Comprehensive Filtering**: Filter by warehouse, date range, and user
    - **Audit Trail**: Complete adjustment history for compliance requirements
    - **User Tracking**: Identify who made specific adjustments for accountability
    - **Temporal Analysis**: Date-based filtering for trend analysis and reporting

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **dateStart/dateEnd**: Optional - Filter by adjustment date range
    - **userId**: Optional - Filter adjustments by specific user

    ### Business Logic
    - Automatically filters transactions where transactionType = \"ADJUST\"
    - Results ordered by transaction date (newest first)
    - Date filtering based on transactionDate field
    - User filtering for accountability and audit purposes

    ### Use Cases
    - **Audit Compliance**: Review all inventory adjustments for audit purposes
    - **Variance Analysis**: Analyze adjustment patterns and identify trends
    - **User Accountability**: Track adjustments made by specific users
    - **Cycle Count Impact**: Review adjustments resulting from cycle counts
    - **Financial Reporting**: Generate adjustment reports for financial impact analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        user_id (Union[Unset, str]):  Example: user_inventory_manager_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]]:
    r"""Get inventory adjustments


    ## Get WMS Inventory Adjustments

    Retrieve inventory adjustment transactions for audit, compliance, and variance analysis.

    ### Features
    - **Adjustment-Specific Filtering**: Automatically filters for transactionType = \"ADJUST\"
    - **Comprehensive Filtering**: Filter by warehouse, date range, and user
    - **Audit Trail**: Complete adjustment history for compliance requirements
    - **User Tracking**: Identify who made specific adjustments for accountability
    - **Temporal Analysis**: Date-based filtering for trend analysis and reporting

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **dateStart/dateEnd**: Optional - Filter by adjustment date range
    - **userId**: Optional - Filter adjustments by specific user

    ### Business Logic
    - Automatically filters transactions where transactionType = \"ADJUST\"
    - Results ordered by transaction date (newest first)
    - Date filtering based on transactionDate field
    - User filtering for accountability and audit purposes

    ### Use Cases
    - **Audit Compliance**: Review all inventory adjustments for audit purposes
    - **Variance Analysis**: Analyze adjustment patterns and identify trends
    - **User Accountability**: Track adjustments made by specific users
    - **Cycle Count Impact**: Review adjustments resulting from cycle counts
    - **Financial Reporting**: Generate adjustment reports for financial impact analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        user_id (Union[Unset, str]):  Example: user_inventory_manager_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]]:
    r"""Get inventory adjustments


    ## Get WMS Inventory Adjustments

    Retrieve inventory adjustment transactions for audit, compliance, and variance analysis.

    ### Features
    - **Adjustment-Specific Filtering**: Automatically filters for transactionType = \"ADJUST\"
    - **Comprehensive Filtering**: Filter by warehouse, date range, and user
    - **Audit Trail**: Complete adjustment history for compliance requirements
    - **User Tracking**: Identify who made specific adjustments for accountability
    - **Temporal Analysis**: Date-based filtering for trend analysis and reporting

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **dateStart/dateEnd**: Optional - Filter by adjustment date range
    - **userId**: Optional - Filter adjustments by specific user

    ### Business Logic
    - Automatically filters transactions where transactionType = \"ADJUST\"
    - Results ordered by transaction date (newest first)
    - Date filtering based on transactionDate field
    - User filtering for accountability and audit purposes

    ### Use Cases
    - **Audit Compliance**: Review all inventory adjustments for audit purposes
    - **Variance Analysis**: Analyze adjustment patterns and identify trends
    - **User Accountability**: Track adjustments made by specific users
    - **Cycle Count Impact**: Review adjustments resulting from cycle counts
    - **Financial Reporting**: Generate adjustment reports for financial impact analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        user_id (Union[Unset, str]):  Example: user_inventory_manager_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]]:
    r"""Get inventory adjustments


    ## Get WMS Inventory Adjustments

    Retrieve inventory adjustment transactions for audit, compliance, and variance analysis.

    ### Features
    - **Adjustment-Specific Filtering**: Automatically filters for transactionType = \"ADJUST\"
    - **Comprehensive Filtering**: Filter by warehouse, date range, and user
    - **Audit Trail**: Complete adjustment history for compliance requirements
    - **User Tracking**: Identify who made specific adjustments for accountability
    - **Temporal Analysis**: Date-based filtering for trend analysis and reporting

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **dateStart/dateEnd**: Optional - Filter by adjustment date range
    - **userId**: Optional - Filter adjustments by specific user

    ### Business Logic
    - Automatically filters transactions where transactionType = \"ADJUST\"
    - Results ordered by transaction date (newest first)
    - Date filtering based on transactionDate field
    - User filtering for accountability and audit purposes

    ### Use Cases
    - **Audit Compliance**: Review all inventory adjustments for audit purposes
    - **Variance Analysis**: Analyze adjustment patterns and identify trends
    - **User Accountability**: Track adjustments made by specific users
    - **Cycle Count Impact**: Review adjustments resulting from cycle counts
    - **Financial Reporting**: Generate adjustment reports for financial impact analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        user_id (Union[Unset, str]):  Example: user_inventory_manager_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryAdjustmentsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            date_start=date_start,
            date_end=date_end,
            user_id=user_id,
        )
    ).parsed
