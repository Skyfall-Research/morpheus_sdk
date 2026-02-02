from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_active_carriers_carrier_type import GetTMSActiveCarriersCarrierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    carrier_type: Union[Unset, GetTMSActiveCarriersCarrierType] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    smart_way_certified: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_carrier_type: Union[Unset, str] = UNSET
    if not isinstance(carrier_type, Unset):
        json_carrier_type = carrier_type.value

    params["carrierType"] = json_carrier_type

    params["serviceRegion"] = service_region

    params["smartWayCertified"] = smart_way_certified

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/carriers",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ErrorResponse]:
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ErrorResponse]:
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
    carrier_type: Union[Unset, GetTMSActiveCarriersCarrierType] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    smart_way_certified: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[ErrorResponse]:
    """Get active carriers with filtering


    ## Get Active TMS Carriers

    Retrieve active carriers with advanced filtering and pagination capabilities.

    ### Features
    - **Active Status Filter**: Only returns carriers with ACTIVE status
    - **Multi-Criteria Filtering**: Filter by type, region, and certifications
    - **SmartWay Certification**: Filter by EPA SmartWay certified carriers
    - **Service Region Matching**: Find carriers serving specific regions
    - **Cursor Pagination**: Efficient pagination for large carrier lists

    ### Carrier Status Values
    - **ACTIVE**: Available for shipment assignments
    - **INACTIVE**: Not accepting new assignments
    - **SUSPENDED**: Temporarily suspended
    - **PENDING_APPROVAL**: Awaiting approval process

    ### Use Cases
    - Carrier selection for shipment tendering
    - Capacity planning and sourcing
    - Compliance and certification verification
    - Regional coverage analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_type (Union[Unset, GetTMSActiveCarriersCarrierType]):  Example: FTL.
        service_region (Union[Unset, str]):  Example: GA.
        smart_way_certified (Union[Unset, bool]):  Example: True.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_type=carrier_type,
        service_region=service_region,
        smart_way_certified=smart_way_certified,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    carrier_type: Union[Unset, GetTMSActiveCarriersCarrierType] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    smart_way_certified: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[ErrorResponse]:
    """Get active carriers with filtering


    ## Get Active TMS Carriers

    Retrieve active carriers with advanced filtering and pagination capabilities.

    ### Features
    - **Active Status Filter**: Only returns carriers with ACTIVE status
    - **Multi-Criteria Filtering**: Filter by type, region, and certifications
    - **SmartWay Certification**: Filter by EPA SmartWay certified carriers
    - **Service Region Matching**: Find carriers serving specific regions
    - **Cursor Pagination**: Efficient pagination for large carrier lists

    ### Carrier Status Values
    - **ACTIVE**: Available for shipment assignments
    - **INACTIVE**: Not accepting new assignments
    - **SUSPENDED**: Temporarily suspended
    - **PENDING_APPROVAL**: Awaiting approval process

    ### Use Cases
    - Carrier selection for shipment tendering
    - Capacity planning and sourcing
    - Compliance and certification verification
    - Regional coverage analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_type (Union[Unset, GetTMSActiveCarriersCarrierType]):  Example: FTL.
        service_region (Union[Unset, str]):  Example: GA.
        smart_way_certified (Union[Unset, bool]):  Example: True.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        carrier_type=carrier_type,
        service_region=service_region,
        smart_way_certified=smart_way_certified,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    carrier_type: Union[Unset, GetTMSActiveCarriersCarrierType] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    smart_way_certified: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[ErrorResponse]:
    """Get active carriers with filtering


    ## Get Active TMS Carriers

    Retrieve active carriers with advanced filtering and pagination capabilities.

    ### Features
    - **Active Status Filter**: Only returns carriers with ACTIVE status
    - **Multi-Criteria Filtering**: Filter by type, region, and certifications
    - **SmartWay Certification**: Filter by EPA SmartWay certified carriers
    - **Service Region Matching**: Find carriers serving specific regions
    - **Cursor Pagination**: Efficient pagination for large carrier lists

    ### Carrier Status Values
    - **ACTIVE**: Available for shipment assignments
    - **INACTIVE**: Not accepting new assignments
    - **SUSPENDED**: Temporarily suspended
    - **PENDING_APPROVAL**: Awaiting approval process

    ### Use Cases
    - Carrier selection for shipment tendering
    - Capacity planning and sourcing
    - Compliance and certification verification
    - Regional coverage analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_type (Union[Unset, GetTMSActiveCarriersCarrierType]):  Example: FTL.
        service_region (Union[Unset, str]):  Example: GA.
        smart_way_certified (Union[Unset, bool]):  Example: True.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_type=carrier_type,
        service_region=service_region,
        smart_way_certified=smart_way_certified,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    carrier_type: Union[Unset, GetTMSActiveCarriersCarrierType] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    smart_way_certified: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[ErrorResponse]:
    """Get active carriers with filtering


    ## Get Active TMS Carriers

    Retrieve active carriers with advanced filtering and pagination capabilities.

    ### Features
    - **Active Status Filter**: Only returns carriers with ACTIVE status
    - **Multi-Criteria Filtering**: Filter by type, region, and certifications
    - **SmartWay Certification**: Filter by EPA SmartWay certified carriers
    - **Service Region Matching**: Find carriers serving specific regions
    - **Cursor Pagination**: Efficient pagination for large carrier lists

    ### Carrier Status Values
    - **ACTIVE**: Available for shipment assignments
    - **INACTIVE**: Not accepting new assignments
    - **SUSPENDED**: Temporarily suspended
    - **PENDING_APPROVAL**: Awaiting approval process

    ### Use Cases
    - Carrier selection for shipment tendering
    - Capacity planning and sourcing
    - Compliance and certification verification
    - Regional coverage analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_type (Union[Unset, GetTMSActiveCarriersCarrierType]):  Example: FTL.
        service_region (Union[Unset, str]):  Example: GA.
        smart_way_certified (Union[Unset, bool]):  Example: True.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            carrier_type=carrier_type,
            service_region=service_region,
            smart_way_certified=smart_way_certified,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
