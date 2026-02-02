from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inbound_order_by_id_response_200 import GetWMSInboundOrderByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    inbound_order_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inbound-orders/{inbound_order_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInboundOrderByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]]:
    """Get inbound order by ID


    ## Get WMS Inbound Order Details

    Retrieve comprehensive information about a specific inbound order including all line items,
    receiving progress, and vendor details.

    ### Features
    - **Complete Order Details**: Full order information with vendor and line items
    - **Receiving Progress**: Real-time receiving status for each product line
    - **Appointment Integration**: Associated appointment details for dock coordination
    - **Status Tracking**: Current order status and historical progression
    - **Audit Information**: Creation and modification timestamps for compliance

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - Returns complete order information including nested line items and vendor details
    - Includes receiving progress tracking for each line item
    - Shows appointment associations for dock scheduling coordination
    - Provides comprehensive order status and timing information

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Use Cases
    - **Receiving Operations**: View detailed order information during receiving process
    - **Status Verification**: Check current order status and receiving progress
    - **Vendor Coordination**: Access vendor contact information for communication
    - **Appointment Management**: Verify appointment associations and scheduling
    - **Audit Tracking**: Review order creation and modification history


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        inbound_order_id=inbound_order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]]:
    """Get inbound order by ID


    ## Get WMS Inbound Order Details

    Retrieve comprehensive information about a specific inbound order including all line items,
    receiving progress, and vendor details.

    ### Features
    - **Complete Order Details**: Full order information with vendor and line items
    - **Receiving Progress**: Real-time receiving status for each product line
    - **Appointment Integration**: Associated appointment details for dock coordination
    - **Status Tracking**: Current order status and historical progression
    - **Audit Information**: Creation and modification timestamps for compliance

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - Returns complete order information including nested line items and vendor details
    - Includes receiving progress tracking for each line item
    - Shows appointment associations for dock scheduling coordination
    - Provides comprehensive order status and timing information

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Use Cases
    - **Receiving Operations**: View detailed order information during receiving process
    - **Status Verification**: Check current order status and receiving progress
    - **Vendor Coordination**: Access vendor contact information for communication
    - **Appointment Management**: Verify appointment associations and scheduling
    - **Audit Tracking**: Review order creation and modification history


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        inbound_order_id=inbound_order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]]:
    """Get inbound order by ID


    ## Get WMS Inbound Order Details

    Retrieve comprehensive information about a specific inbound order including all line items,
    receiving progress, and vendor details.

    ### Features
    - **Complete Order Details**: Full order information with vendor and line items
    - **Receiving Progress**: Real-time receiving status for each product line
    - **Appointment Integration**: Associated appointment details for dock coordination
    - **Status Tracking**: Current order status and historical progression
    - **Audit Information**: Creation and modification timestamps for compliance

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - Returns complete order information including nested line items and vendor details
    - Includes receiving progress tracking for each line item
    - Shows appointment associations for dock scheduling coordination
    - Provides comprehensive order status and timing information

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Use Cases
    - **Receiving Operations**: View detailed order information during receiving process
    - **Status Verification**: Check current order status and receiving progress
    - **Vendor Coordination**: Access vendor contact information for communication
    - **Appointment Management**: Verify appointment associations and scheduling
    - **Audit Tracking**: Review order creation and modification history


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        inbound_order_id=inbound_order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]]:
    """Get inbound order by ID


    ## Get WMS Inbound Order Details

    Retrieve comprehensive information about a specific inbound order including all line items,
    receiving progress, and vendor details.

    ### Features
    - **Complete Order Details**: Full order information with vendor and line items
    - **Receiving Progress**: Real-time receiving status for each product line
    - **Appointment Integration**: Associated appointment details for dock coordination
    - **Status Tracking**: Current order status and historical progression
    - **Audit Information**: Creation and modification timestamps for compliance

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - Returns complete order information including nested line items and vendor details
    - Includes receiving progress tracking for each line item
    - Shows appointment associations for dock scheduling coordination
    - Provides comprehensive order status and timing information

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Use Cases
    - **Receiving Operations**: View detailed order information during receiving process
    - **Status Verification**: Check current order status and receiving progress
    - **Vendor Coordination**: Access vendor contact information for communication
    - **Appointment Management**: Verify appointment associations and scheduling
    - **Audit Tracking**: Review order creation and modification history


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrderByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            inbound_order_id=inbound_order_id,
            client=client,
        )
    ).parsed
