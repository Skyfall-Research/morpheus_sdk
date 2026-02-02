from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.search_tms_carriers_carrier_type import SearchTMSCarriersCarrierType
from ...models.search_tms_carriers_status import SearchTMSCarriersStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    search_term: str,
    carrier_type: Union[Unset, SearchTMSCarriersCarrierType] = UNSET,
    status: Union[Unset, SearchTMSCarriersStatus] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["searchTerm"] = search_term

    json_carrier_type: Union[Unset, str] = UNSET
    if not isinstance(carrier_type, Unset):
        json_carrier_type = carrier_type.value

    params["carrierType"] = json_carrier_type

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["serviceRegion"] = service_region

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/carriers/search",
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
    search_term: str,
    carrier_type: Union[Unset, SearchTMSCarriersCarrierType] = UNSET,
    status: Union[Unset, SearchTMSCarriersStatus] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[ErrorResponse]:
    r"""Search carriers by name or code


    ## Search TMS Carriers

    Full-text search across carrier names, codes, and SCAC codes with optional filtering.

    ### Features
    - **Multi-Field Search**: Search across carrier name, code, and SCAC
    - **Case-Insensitive**: Flexible matching regardless of case
    - **Advanced Filtering**: Combine search with type, status, and region filters
    - **Performance Optimized**: Indexed search for fast response times
    - **Limited Results**: Capped at 50 results for performance

    ### Search Fields
    - **carrierName**: Company name (e.g., \"FedEx\", \"UPS\")
    - **carrierCode**: Internal carrier code
    - **scacCode**: Standard Carrier Alpha Code

    ### Use Cases
    - Carrier lookup during shipment planning
    - Vendor management and selection
    - Compliance verification
    - Directory browsing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        search_term (str):  Example: FedEx.
        carrier_type (Union[Unset, SearchTMSCarriersCarrierType]):  Example: PARCEL.
        status (Union[Unset, SearchTMSCarriersStatus]):  Example: ACTIVE.
        service_region (Union[Unset, str]):  Example: CA.
        limit (Union[Unset, int]):  Example: 20.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        search_term=search_term,
        carrier_type=carrier_type,
        status=status,
        service_region=service_region,
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
    search_term: str,
    carrier_type: Union[Unset, SearchTMSCarriersCarrierType] = UNSET,
    status: Union[Unset, SearchTMSCarriersStatus] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[ErrorResponse]:
    r"""Search carriers by name or code


    ## Search TMS Carriers

    Full-text search across carrier names, codes, and SCAC codes with optional filtering.

    ### Features
    - **Multi-Field Search**: Search across carrier name, code, and SCAC
    - **Case-Insensitive**: Flexible matching regardless of case
    - **Advanced Filtering**: Combine search with type, status, and region filters
    - **Performance Optimized**: Indexed search for fast response times
    - **Limited Results**: Capped at 50 results for performance

    ### Search Fields
    - **carrierName**: Company name (e.g., \"FedEx\", \"UPS\")
    - **carrierCode**: Internal carrier code
    - **scacCode**: Standard Carrier Alpha Code

    ### Use Cases
    - Carrier lookup during shipment planning
    - Vendor management and selection
    - Compliance verification
    - Directory browsing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        search_term (str):  Example: FedEx.
        carrier_type (Union[Unset, SearchTMSCarriersCarrierType]):  Example: PARCEL.
        status (Union[Unset, SearchTMSCarriersStatus]):  Example: ACTIVE.
        service_region (Union[Unset, str]):  Example: CA.
        limit (Union[Unset, int]):  Example: 20.
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
        search_term=search_term,
        carrier_type=carrier_type,
        status=status,
        service_region=service_region,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search_term: str,
    carrier_type: Union[Unset, SearchTMSCarriersCarrierType] = UNSET,
    status: Union[Unset, SearchTMSCarriersStatus] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[ErrorResponse]:
    r"""Search carriers by name or code


    ## Search TMS Carriers

    Full-text search across carrier names, codes, and SCAC codes with optional filtering.

    ### Features
    - **Multi-Field Search**: Search across carrier name, code, and SCAC
    - **Case-Insensitive**: Flexible matching regardless of case
    - **Advanced Filtering**: Combine search with type, status, and region filters
    - **Performance Optimized**: Indexed search for fast response times
    - **Limited Results**: Capped at 50 results for performance

    ### Search Fields
    - **carrierName**: Company name (e.g., \"FedEx\", \"UPS\")
    - **carrierCode**: Internal carrier code
    - **scacCode**: Standard Carrier Alpha Code

    ### Use Cases
    - Carrier lookup during shipment planning
    - Vendor management and selection
    - Compliance verification
    - Directory browsing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        search_term (str):  Example: FedEx.
        carrier_type (Union[Unset, SearchTMSCarriersCarrierType]):  Example: PARCEL.
        status (Union[Unset, SearchTMSCarriersStatus]):  Example: ACTIVE.
        service_region (Union[Unset, str]):  Example: CA.
        limit (Union[Unset, int]):  Example: 20.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        search_term=search_term,
        carrier_type=carrier_type,
        status=status,
        service_region=service_region,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search_term: str,
    carrier_type: Union[Unset, SearchTMSCarriersCarrierType] = UNSET,
    status: Union[Unset, SearchTMSCarriersStatus] = UNSET,
    service_region: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[ErrorResponse]:
    r"""Search carriers by name or code


    ## Search TMS Carriers

    Full-text search across carrier names, codes, and SCAC codes with optional filtering.

    ### Features
    - **Multi-Field Search**: Search across carrier name, code, and SCAC
    - **Case-Insensitive**: Flexible matching regardless of case
    - **Advanced Filtering**: Combine search with type, status, and region filters
    - **Performance Optimized**: Indexed search for fast response times
    - **Limited Results**: Capped at 50 results for performance

    ### Search Fields
    - **carrierName**: Company name (e.g., \"FedEx\", \"UPS\")
    - **carrierCode**: Internal carrier code
    - **scacCode**: Standard Carrier Alpha Code

    ### Use Cases
    - Carrier lookup during shipment planning
    - Vendor management and selection
    - Compliance verification
    - Directory browsing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        search_term (str):  Example: FedEx.
        carrier_type (Union[Unset, SearchTMSCarriersCarrierType]):  Example: PARCEL.
        status (Union[Unset, SearchTMSCarriersStatus]):  Example: ACTIVE.
        service_region (Union[Unset, str]):  Example: CA.
        limit (Union[Unset, int]):  Example: 20.
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
            search_term=search_term,
            carrier_type=carrier_type,
            status=status,
            service_region=service_region,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
