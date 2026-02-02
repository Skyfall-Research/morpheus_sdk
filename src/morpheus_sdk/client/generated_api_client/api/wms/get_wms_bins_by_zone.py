from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_bins_by_zone_abc_classification_item import GetWMSBinsByZoneAbcClassificationItem
from ...models.get_wms_bins_by_zone_bin_type_item import GetWMSBinsByZoneBinTypeItem
from ...models.get_wms_bins_by_zone_location_type_item import GetWMSBinsByZoneLocationTypeItem
from ...models.get_wms_bins_by_zone_response_200 import GetWMSBinsByZoneResponse200
from ...models.get_wms_bins_by_zone_status_item import GetWMSBinsByZoneStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    zone_id: str,
    *,
    status: Union[Unset, list[GetWMSBinsByZoneStatusItem]] = UNSET,
    bin_type: Union[Unset, list[GetWMSBinsByZoneBinTypeItem]] = UNSET,
    location_type: Union[Unset, list[GetWMSBinsByZoneLocationTypeItem]] = UNSET,
    abc_classification: Union[Unset, list[GetWMSBinsByZoneAbcClassificationItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_bin_type: Union[Unset, list[str]] = UNSET
    if not isinstance(bin_type, Unset):
        json_bin_type = []
        for bin_type_item_data in bin_type:
            bin_type_item = bin_type_item_data.value
            json_bin_type.append(bin_type_item)

    params["binType"] = json_bin_type

    json_location_type: Union[Unset, list[str]] = UNSET
    if not isinstance(location_type, Unset):
        json_location_type = []
        for location_type_item_data in location_type:
            location_type_item = location_type_item_data.value
            json_location_type.append(location_type_item)

    params["locationType"] = json_location_type

    json_abc_classification: Union[Unset, list[str]] = UNSET
    if not isinstance(abc_classification, Unset):
        json_abc_classification = []
        for abc_classification_item_data in abc_classification:
            abc_classification_item = abc_classification_item_data.value
            json_abc_classification.append(abc_classification_item)

    params["abcClassification"] = json_abc_classification

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/bins/zone/{zone_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSBinsByZoneResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSBinsByZoneResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSBinsByZoneResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSBinsByZoneStatusItem]] = UNSET,
    bin_type: Union[Unset, list[GetWMSBinsByZoneBinTypeItem]] = UNSET,
    location_type: Union[Unset, list[GetWMSBinsByZoneLocationTypeItem]] = UNSET,
    abc_classification: Union[Unset, list[GetWMSBinsByZoneAbcClassificationItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSBinsByZoneResponse200]]:
    """Get bins by zone with filtering


    ## Get WMS Bins by Zone

    Retrieve all bins within a specific warehouse zone with comprehensive filtering capabilities for
    operational management and planning.

    ### Features
    - **Zone-Based Retrieval**: Get all bins within a specific warehouse zone
    - **Multi-Status Filtering**: Filter by one or multiple bin status values
    - **Type-Based Filtering**: Filter by bin types for operational compatibility
    - **Location Type Filtering**: Filter by functional location types
    - **ABC Classification**: Filter by inventory velocity classification
    - **Comprehensive Results**: Returns complete bin profiles with all attributes

    ### Query Parameters
    - **status**: Optional - Filter by bin status (supports multiple values)
    - **binType**: Optional - Filter by bin types (supports multiple values)
    - **locationType**: Optional - Filter by location types (supports multiple values)
    - **abcClassification**: Optional - Filter by ABC classification (supports multiple values)

    ### Available Status Values
    - **AVAILABLE**: Ready for inventory storage
    - **OCCUPIED**: Currently contains inventory
    - **RESERVED**: Reserved for specific operations
    - **DAMAGED**: Physically damaged, unusable
    - **BLOCKED**: Temporarily blocked from use

    ### Business Rules
    - zoneId must be valid and accessible
    - All filter parameters support multiple values (comma-separated)
    - Results include complete bin configuration and current status
    - Sorted by aisle, bay, level, and position for operational efficiency

    ### Use Cases
    - **Zone Operations**: Manage all bins within a specific zone
    - **Capacity Analysis**: Analyze zone capacity and utilization
    - **Maintenance Planning**: Identify bins requiring maintenance
    - **Operational Planning**: Plan putaway and picking operations by zone
    - **Slotting Analysis**: Support slotting optimization within zones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZONE_PICK_A.
        status (Union[Unset, list[GetWMSBinsByZoneStatusItem]]):  Example: ['AVAILABLE',
            'OCCUPIED'].
        bin_type (Union[Unset, list[GetWMSBinsByZoneBinTypeItem]]):  Example: ['PICK_FACE',
            'SHELF'].
        location_type (Union[Unset, list[GetWMSBinsByZoneLocationTypeItem]]):  Example:
            ['STORAGE'].
        abc_classification (Union[Unset, list[GetWMSBinsByZoneAbcClassificationItem]]):  Example:
            ['A', 'B'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSBinsByZoneResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_id=zone_id,
        status=status,
        bin_type=bin_type,
        location_type=location_type,
        abc_classification=abc_classification,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSBinsByZoneStatusItem]] = UNSET,
    bin_type: Union[Unset, list[GetWMSBinsByZoneBinTypeItem]] = UNSET,
    location_type: Union[Unset, list[GetWMSBinsByZoneLocationTypeItem]] = UNSET,
    abc_classification: Union[Unset, list[GetWMSBinsByZoneAbcClassificationItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSBinsByZoneResponse200]]:
    """Get bins by zone with filtering


    ## Get WMS Bins by Zone

    Retrieve all bins within a specific warehouse zone with comprehensive filtering capabilities for
    operational management and planning.

    ### Features
    - **Zone-Based Retrieval**: Get all bins within a specific warehouse zone
    - **Multi-Status Filtering**: Filter by one or multiple bin status values
    - **Type-Based Filtering**: Filter by bin types for operational compatibility
    - **Location Type Filtering**: Filter by functional location types
    - **ABC Classification**: Filter by inventory velocity classification
    - **Comprehensive Results**: Returns complete bin profiles with all attributes

    ### Query Parameters
    - **status**: Optional - Filter by bin status (supports multiple values)
    - **binType**: Optional - Filter by bin types (supports multiple values)
    - **locationType**: Optional - Filter by location types (supports multiple values)
    - **abcClassification**: Optional - Filter by ABC classification (supports multiple values)

    ### Available Status Values
    - **AVAILABLE**: Ready for inventory storage
    - **OCCUPIED**: Currently contains inventory
    - **RESERVED**: Reserved for specific operations
    - **DAMAGED**: Physically damaged, unusable
    - **BLOCKED**: Temporarily blocked from use

    ### Business Rules
    - zoneId must be valid and accessible
    - All filter parameters support multiple values (comma-separated)
    - Results include complete bin configuration and current status
    - Sorted by aisle, bay, level, and position for operational efficiency

    ### Use Cases
    - **Zone Operations**: Manage all bins within a specific zone
    - **Capacity Analysis**: Analyze zone capacity and utilization
    - **Maintenance Planning**: Identify bins requiring maintenance
    - **Operational Planning**: Plan putaway and picking operations by zone
    - **Slotting Analysis**: Support slotting optimization within zones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZONE_PICK_A.
        status (Union[Unset, list[GetWMSBinsByZoneStatusItem]]):  Example: ['AVAILABLE',
            'OCCUPIED'].
        bin_type (Union[Unset, list[GetWMSBinsByZoneBinTypeItem]]):  Example: ['PICK_FACE',
            'SHELF'].
        location_type (Union[Unset, list[GetWMSBinsByZoneLocationTypeItem]]):  Example:
            ['STORAGE'].
        abc_classification (Union[Unset, list[GetWMSBinsByZoneAbcClassificationItem]]):  Example:
            ['A', 'B'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSBinsByZoneResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        zone_id=zone_id,
        client=client,
        status=status,
        bin_type=bin_type,
        location_type=location_type,
        abc_classification=abc_classification,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSBinsByZoneStatusItem]] = UNSET,
    bin_type: Union[Unset, list[GetWMSBinsByZoneBinTypeItem]] = UNSET,
    location_type: Union[Unset, list[GetWMSBinsByZoneLocationTypeItem]] = UNSET,
    abc_classification: Union[Unset, list[GetWMSBinsByZoneAbcClassificationItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSBinsByZoneResponse200]]:
    """Get bins by zone with filtering


    ## Get WMS Bins by Zone

    Retrieve all bins within a specific warehouse zone with comprehensive filtering capabilities for
    operational management and planning.

    ### Features
    - **Zone-Based Retrieval**: Get all bins within a specific warehouse zone
    - **Multi-Status Filtering**: Filter by one or multiple bin status values
    - **Type-Based Filtering**: Filter by bin types for operational compatibility
    - **Location Type Filtering**: Filter by functional location types
    - **ABC Classification**: Filter by inventory velocity classification
    - **Comprehensive Results**: Returns complete bin profiles with all attributes

    ### Query Parameters
    - **status**: Optional - Filter by bin status (supports multiple values)
    - **binType**: Optional - Filter by bin types (supports multiple values)
    - **locationType**: Optional - Filter by location types (supports multiple values)
    - **abcClassification**: Optional - Filter by ABC classification (supports multiple values)

    ### Available Status Values
    - **AVAILABLE**: Ready for inventory storage
    - **OCCUPIED**: Currently contains inventory
    - **RESERVED**: Reserved for specific operations
    - **DAMAGED**: Physically damaged, unusable
    - **BLOCKED**: Temporarily blocked from use

    ### Business Rules
    - zoneId must be valid and accessible
    - All filter parameters support multiple values (comma-separated)
    - Results include complete bin configuration and current status
    - Sorted by aisle, bay, level, and position for operational efficiency

    ### Use Cases
    - **Zone Operations**: Manage all bins within a specific zone
    - **Capacity Analysis**: Analyze zone capacity and utilization
    - **Maintenance Planning**: Identify bins requiring maintenance
    - **Operational Planning**: Plan putaway and picking operations by zone
    - **Slotting Analysis**: Support slotting optimization within zones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZONE_PICK_A.
        status (Union[Unset, list[GetWMSBinsByZoneStatusItem]]):  Example: ['AVAILABLE',
            'OCCUPIED'].
        bin_type (Union[Unset, list[GetWMSBinsByZoneBinTypeItem]]):  Example: ['PICK_FACE',
            'SHELF'].
        location_type (Union[Unset, list[GetWMSBinsByZoneLocationTypeItem]]):  Example:
            ['STORAGE'].
        abc_classification (Union[Unset, list[GetWMSBinsByZoneAbcClassificationItem]]):  Example:
            ['A', 'B'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSBinsByZoneResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_id=zone_id,
        status=status,
        bin_type=bin_type,
        location_type=location_type,
        abc_classification=abc_classification,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSBinsByZoneStatusItem]] = UNSET,
    bin_type: Union[Unset, list[GetWMSBinsByZoneBinTypeItem]] = UNSET,
    location_type: Union[Unset, list[GetWMSBinsByZoneLocationTypeItem]] = UNSET,
    abc_classification: Union[Unset, list[GetWMSBinsByZoneAbcClassificationItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSBinsByZoneResponse200]]:
    """Get bins by zone with filtering


    ## Get WMS Bins by Zone

    Retrieve all bins within a specific warehouse zone with comprehensive filtering capabilities for
    operational management and planning.

    ### Features
    - **Zone-Based Retrieval**: Get all bins within a specific warehouse zone
    - **Multi-Status Filtering**: Filter by one or multiple bin status values
    - **Type-Based Filtering**: Filter by bin types for operational compatibility
    - **Location Type Filtering**: Filter by functional location types
    - **ABC Classification**: Filter by inventory velocity classification
    - **Comprehensive Results**: Returns complete bin profiles with all attributes

    ### Query Parameters
    - **status**: Optional - Filter by bin status (supports multiple values)
    - **binType**: Optional - Filter by bin types (supports multiple values)
    - **locationType**: Optional - Filter by location types (supports multiple values)
    - **abcClassification**: Optional - Filter by ABC classification (supports multiple values)

    ### Available Status Values
    - **AVAILABLE**: Ready for inventory storage
    - **OCCUPIED**: Currently contains inventory
    - **RESERVED**: Reserved for specific operations
    - **DAMAGED**: Physically damaged, unusable
    - **BLOCKED**: Temporarily blocked from use

    ### Business Rules
    - zoneId must be valid and accessible
    - All filter parameters support multiple values (comma-separated)
    - Results include complete bin configuration and current status
    - Sorted by aisle, bay, level, and position for operational efficiency

    ### Use Cases
    - **Zone Operations**: Manage all bins within a specific zone
    - **Capacity Analysis**: Analyze zone capacity and utilization
    - **Maintenance Planning**: Identify bins requiring maintenance
    - **Operational Planning**: Plan putaway and picking operations by zone
    - **Slotting Analysis**: Support slotting optimization within zones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZONE_PICK_A.
        status (Union[Unset, list[GetWMSBinsByZoneStatusItem]]):  Example: ['AVAILABLE',
            'OCCUPIED'].
        bin_type (Union[Unset, list[GetWMSBinsByZoneBinTypeItem]]):  Example: ['PICK_FACE',
            'SHELF'].
        location_type (Union[Unset, list[GetWMSBinsByZoneLocationTypeItem]]):  Example:
            ['STORAGE'].
        abc_classification (Union[Unset, list[GetWMSBinsByZoneAbcClassificationItem]]):  Example:
            ['A', 'B'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSBinsByZoneResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            zone_id=zone_id,
            client=client,
            status=status,
            bin_type=bin_type,
            location_type=location_type,
            abc_classification=abc_classification,
        )
    ).parsed
