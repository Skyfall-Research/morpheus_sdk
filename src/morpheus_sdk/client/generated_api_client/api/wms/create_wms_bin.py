from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_bin_body import CreateWMSBinBody
from ...models.create_wms_bin_response_201 import CreateWMSBinResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSBinBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/bins",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSBinResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSBinResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateWMSBinResponse201, ErrorResponse]]:
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
    body: CreateWMSBinBody,
) -> Response[Union[CreateWMSBinResponse201, ErrorResponse]]:
    """Create new warehouse bin


    ## Create WMS Bin

    Create a new warehouse bin for inventory storage and management with comprehensive location and
    capacity configuration.

    ### Features
    - **Location Management**: Define precise warehouse location with aisle, bay, level, and position
    - **Capacity Configuration**: Set weight, volume, and pallet capacity constraints
    - **Type Classification**: Configure bin type for operational workflow optimization
    - **ABC Classification**: Support inventory velocity classification for efficient picking
    - **Status Management**: Initialize bin with appropriate operational status
    - **Warehouse Integration**: Link bin to specific warehouse and zone structures

    ### Bin Type Categories
    - **PALLET**: Full pallet storage locations
    - **SHELF**: Shelf-based case or piece picking locations
    - **FLOOR**: Floor-level storage for large items
    - **CASE_FLOW**: Dynamic case flow storage systems
    - **RESERVE**: Reserve or bulk storage locations
    - **PICK_FACE**: Forward pick face locations

    ### Location Type Categories
    - **STORAGE**: General inventory storage locations
    - **STAGING**: Temporary staging areas for operations
    - **DOCK**: Dock door staging and loading areas
    - **QC**: Quality control inspection areas
    - **RETURN**: Return merchandise processing areas

    ### Status Values
    - **AVAILABLE**: Ready for inventory storage
    - **OCCUPIED**: Currently contains inventory
    - **RESERVED**: Reserved for specific operations
    - **DAMAGED**: Physically damaged, unusable
    - **BLOCKED**: Temporarily blocked from use

    ### Business Rules
    - binId is auto-generated with unique identifier if not provided
    - binCode must be unique within the warehouse
    - warehouseId and zoneId are required for location hierarchy
    - Capacity settings define operational constraints
    - Custom fields support warehouse-specific requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSBinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSBinResponse201, ErrorResponse]]
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
    body: CreateWMSBinBody,
) -> Optional[Union[CreateWMSBinResponse201, ErrorResponse]]:
    """Create new warehouse bin


    ## Create WMS Bin

    Create a new warehouse bin for inventory storage and management with comprehensive location and
    capacity configuration.

    ### Features
    - **Location Management**: Define precise warehouse location with aisle, bay, level, and position
    - **Capacity Configuration**: Set weight, volume, and pallet capacity constraints
    - **Type Classification**: Configure bin type for operational workflow optimization
    - **ABC Classification**: Support inventory velocity classification for efficient picking
    - **Status Management**: Initialize bin with appropriate operational status
    - **Warehouse Integration**: Link bin to specific warehouse and zone structures

    ### Bin Type Categories
    - **PALLET**: Full pallet storage locations
    - **SHELF**: Shelf-based case or piece picking locations
    - **FLOOR**: Floor-level storage for large items
    - **CASE_FLOW**: Dynamic case flow storage systems
    - **RESERVE**: Reserve or bulk storage locations
    - **PICK_FACE**: Forward pick face locations

    ### Location Type Categories
    - **STORAGE**: General inventory storage locations
    - **STAGING**: Temporary staging areas for operations
    - **DOCK**: Dock door staging and loading areas
    - **QC**: Quality control inspection areas
    - **RETURN**: Return merchandise processing areas

    ### Status Values
    - **AVAILABLE**: Ready for inventory storage
    - **OCCUPIED**: Currently contains inventory
    - **RESERVED**: Reserved for specific operations
    - **DAMAGED**: Physically damaged, unusable
    - **BLOCKED**: Temporarily blocked from use

    ### Business Rules
    - binId is auto-generated with unique identifier if not provided
    - binCode must be unique within the warehouse
    - warehouseId and zoneId are required for location hierarchy
    - Capacity settings define operational constraints
    - Custom fields support warehouse-specific requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSBinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSBinResponse201, ErrorResponse]
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
    body: CreateWMSBinBody,
) -> Response[Union[CreateWMSBinResponse201, ErrorResponse]]:
    """Create new warehouse bin


    ## Create WMS Bin

    Create a new warehouse bin for inventory storage and management with comprehensive location and
    capacity configuration.

    ### Features
    - **Location Management**: Define precise warehouse location with aisle, bay, level, and position
    - **Capacity Configuration**: Set weight, volume, and pallet capacity constraints
    - **Type Classification**: Configure bin type for operational workflow optimization
    - **ABC Classification**: Support inventory velocity classification for efficient picking
    - **Status Management**: Initialize bin with appropriate operational status
    - **Warehouse Integration**: Link bin to specific warehouse and zone structures

    ### Bin Type Categories
    - **PALLET**: Full pallet storage locations
    - **SHELF**: Shelf-based case or piece picking locations
    - **FLOOR**: Floor-level storage for large items
    - **CASE_FLOW**: Dynamic case flow storage systems
    - **RESERVE**: Reserve or bulk storage locations
    - **PICK_FACE**: Forward pick face locations

    ### Location Type Categories
    - **STORAGE**: General inventory storage locations
    - **STAGING**: Temporary staging areas for operations
    - **DOCK**: Dock door staging and loading areas
    - **QC**: Quality control inspection areas
    - **RETURN**: Return merchandise processing areas

    ### Status Values
    - **AVAILABLE**: Ready for inventory storage
    - **OCCUPIED**: Currently contains inventory
    - **RESERVED**: Reserved for specific operations
    - **DAMAGED**: Physically damaged, unusable
    - **BLOCKED**: Temporarily blocked from use

    ### Business Rules
    - binId is auto-generated with unique identifier if not provided
    - binCode must be unique within the warehouse
    - warehouseId and zoneId are required for location hierarchy
    - Capacity settings define operational constraints
    - Custom fields support warehouse-specific requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSBinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSBinResponse201, ErrorResponse]]
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
    body: CreateWMSBinBody,
) -> Optional[Union[CreateWMSBinResponse201, ErrorResponse]]:
    """Create new warehouse bin


    ## Create WMS Bin

    Create a new warehouse bin for inventory storage and management with comprehensive location and
    capacity configuration.

    ### Features
    - **Location Management**: Define precise warehouse location with aisle, bay, level, and position
    - **Capacity Configuration**: Set weight, volume, and pallet capacity constraints
    - **Type Classification**: Configure bin type for operational workflow optimization
    - **ABC Classification**: Support inventory velocity classification for efficient picking
    - **Status Management**: Initialize bin with appropriate operational status
    - **Warehouse Integration**: Link bin to specific warehouse and zone structures

    ### Bin Type Categories
    - **PALLET**: Full pallet storage locations
    - **SHELF**: Shelf-based case or piece picking locations
    - **FLOOR**: Floor-level storage for large items
    - **CASE_FLOW**: Dynamic case flow storage systems
    - **RESERVE**: Reserve or bulk storage locations
    - **PICK_FACE**: Forward pick face locations

    ### Location Type Categories
    - **STORAGE**: General inventory storage locations
    - **STAGING**: Temporary staging areas for operations
    - **DOCK**: Dock door staging and loading areas
    - **QC**: Quality control inspection areas
    - **RETURN**: Return merchandise processing areas

    ### Status Values
    - **AVAILABLE**: Ready for inventory storage
    - **OCCUPIED**: Currently contains inventory
    - **RESERVED**: Reserved for specific operations
    - **DAMAGED**: Physically damaged, unusable
    - **BLOCKED**: Temporarily blocked from use

    ### Business Rules
    - binId is auto-generated with unique identifier if not provided
    - binCode must be unique within the warehouse
    - warehouseId and zoneId are required for location hierarchy
    - Capacity settings define operational constraints
    - Custom fields support warehouse-specific requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSBinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSBinResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
