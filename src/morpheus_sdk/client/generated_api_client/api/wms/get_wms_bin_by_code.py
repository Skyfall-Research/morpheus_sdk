from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_bin_by_code_response_200 import GetWMSBinByCodeResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    bin_code: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/bins/code/{bin_code}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSBinByCodeResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSBinByCodeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetWMSBinByCodeResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    bin_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSBinByCodeResponse200]]:
    """Get bin by code


    ## Get WMS Bin by Code

    Retrieve a specific warehouse bin using its human-readable bin code for operational identification
    and management.

    ### Features
    - **Code-Based Lookup**: Find bins using human-readable bin codes
    - **Warehouse Scoping**: Optional warehouse filtering for multi-facility operations
    - **Complete Bin Profile**: Returns all bin attributes including location and capacity
    - **Status Information**: Current operational status and availability
    - **Inventory Context**: Location context for inventory management operations

    ### Query Parameters
    - **warehouseId**: Optional - Scope search to specific warehouse for faster lookup

    ### Business Rules
    - binCode must be exact match (case-sensitive)
    - If warehouseId provided, search limited to that warehouse
    - Returns 404 if bin not found or not accessible
    - Includes all bin configuration and status information

    ### Use Cases
    - **Inventory Operations**: Look up bin details during putaway or picking
    - **Maintenance**: Access bin information for maintenance operations
    - **Verification**: Verify bin attributes and capacity constraints
    - **Location Services**: Support warehouse navigation and location services


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_code (str):  Example: A01-B05-L02-P03.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSBinByCodeResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_code=bin_code,
        warehouse_id=warehouse_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    bin_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSBinByCodeResponse200]]:
    """Get bin by code


    ## Get WMS Bin by Code

    Retrieve a specific warehouse bin using its human-readable bin code for operational identification
    and management.

    ### Features
    - **Code-Based Lookup**: Find bins using human-readable bin codes
    - **Warehouse Scoping**: Optional warehouse filtering for multi-facility operations
    - **Complete Bin Profile**: Returns all bin attributes including location and capacity
    - **Status Information**: Current operational status and availability
    - **Inventory Context**: Location context for inventory management operations

    ### Query Parameters
    - **warehouseId**: Optional - Scope search to specific warehouse for faster lookup

    ### Business Rules
    - binCode must be exact match (case-sensitive)
    - If warehouseId provided, search limited to that warehouse
    - Returns 404 if bin not found or not accessible
    - Includes all bin configuration and status information

    ### Use Cases
    - **Inventory Operations**: Look up bin details during putaway or picking
    - **Maintenance**: Access bin information for maintenance operations
    - **Verification**: Verify bin attributes and capacity constraints
    - **Location Services**: Support warehouse navigation and location services


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_code (str):  Example: A01-B05-L02-P03.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSBinByCodeResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        bin_code=bin_code,
        client=client,
        warehouse_id=warehouse_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    bin_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSBinByCodeResponse200]]:
    """Get bin by code


    ## Get WMS Bin by Code

    Retrieve a specific warehouse bin using its human-readable bin code for operational identification
    and management.

    ### Features
    - **Code-Based Lookup**: Find bins using human-readable bin codes
    - **Warehouse Scoping**: Optional warehouse filtering for multi-facility operations
    - **Complete Bin Profile**: Returns all bin attributes including location and capacity
    - **Status Information**: Current operational status and availability
    - **Inventory Context**: Location context for inventory management operations

    ### Query Parameters
    - **warehouseId**: Optional - Scope search to specific warehouse for faster lookup

    ### Business Rules
    - binCode must be exact match (case-sensitive)
    - If warehouseId provided, search limited to that warehouse
    - Returns 404 if bin not found or not accessible
    - Includes all bin configuration and status information

    ### Use Cases
    - **Inventory Operations**: Look up bin details during putaway or picking
    - **Maintenance**: Access bin information for maintenance operations
    - **Verification**: Verify bin attributes and capacity constraints
    - **Location Services**: Support warehouse navigation and location services


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_code (str):  Example: A01-B05-L02-P03.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSBinByCodeResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_code=bin_code,
        warehouse_id=warehouse_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    bin_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSBinByCodeResponse200]]:
    """Get bin by code


    ## Get WMS Bin by Code

    Retrieve a specific warehouse bin using its human-readable bin code for operational identification
    and management.

    ### Features
    - **Code-Based Lookup**: Find bins using human-readable bin codes
    - **Warehouse Scoping**: Optional warehouse filtering for multi-facility operations
    - **Complete Bin Profile**: Returns all bin attributes including location and capacity
    - **Status Information**: Current operational status and availability
    - **Inventory Context**: Location context for inventory management operations

    ### Query Parameters
    - **warehouseId**: Optional - Scope search to specific warehouse for faster lookup

    ### Business Rules
    - binCode must be exact match (case-sensitive)
    - If warehouseId provided, search limited to that warehouse
    - Returns 404 if bin not found or not accessible
    - Includes all bin configuration and status information

    ### Use Cases
    - **Inventory Operations**: Look up bin details during putaway or picking
    - **Maintenance**: Access bin information for maintenance operations
    - **Verification**: Verify bin attributes and capacity constraints
    - **Location Services**: Support warehouse navigation and location services


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_code (str):  Example: A01-B05-L02-P03.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSBinByCodeResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            bin_code=bin_code,
            client=client,
            warehouse_id=warehouse_id,
        )
    ).parsed
