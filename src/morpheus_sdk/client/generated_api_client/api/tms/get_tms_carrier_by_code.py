from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    carrier_code: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/carriers/code/{carrier_code}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ErrorResponse]:
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

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
    carrier_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ErrorResponse]:
    """Get carrier by code


    ## Get TMS Carrier by Code

    Retrieve carrier information using the carrier's business code (SCAC or internal code).

    ### Features
    - **Code-Based Lookup**: Find carriers using business-friendly codes
    - **SCAC Integration**: Support for Standard Carrier Alpha Codes
    - **EDI Compatibility**: Perfect for EDI transaction processing
    - **Complete Profile**: Full carrier information and capabilities

    ### Use Cases
    - EDI transaction processing and mapping
    - Business partner integration
    - Legacy system integration
    - Quick carrier lookup during operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_code (str):  Example: FDXF.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_code=carrier_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    carrier_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ErrorResponse]:
    """Get carrier by code


    ## Get TMS Carrier by Code

    Retrieve carrier information using the carrier's business code (SCAC or internal code).

    ### Features
    - **Code-Based Lookup**: Find carriers using business-friendly codes
    - **SCAC Integration**: Support for Standard Carrier Alpha Codes
    - **EDI Compatibility**: Perfect for EDI transaction processing
    - **Complete Profile**: Full carrier information and capabilities

    ### Use Cases
    - EDI transaction processing and mapping
    - Business partner integration
    - Legacy system integration
    - Quick carrier lookup during operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_code (str):  Example: FDXF.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        world_id=world_id,
        carrier_code=carrier_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    carrier_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ErrorResponse]:
    """Get carrier by code


    ## Get TMS Carrier by Code

    Retrieve carrier information using the carrier's business code (SCAC or internal code).

    ### Features
    - **Code-Based Lookup**: Find carriers using business-friendly codes
    - **SCAC Integration**: Support for Standard Carrier Alpha Codes
    - **EDI Compatibility**: Perfect for EDI transaction processing
    - **Complete Profile**: Full carrier information and capabilities

    ### Use Cases
    - EDI transaction processing and mapping
    - Business partner integration
    - Legacy system integration
    - Quick carrier lookup during operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_code (str):  Example: FDXF.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_code=carrier_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    carrier_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ErrorResponse]:
    """Get carrier by code


    ## Get TMS Carrier by Code

    Retrieve carrier information using the carrier's business code (SCAC or internal code).

    ### Features
    - **Code-Based Lookup**: Find carriers using business-friendly codes
    - **SCAC Integration**: Support for Standard Carrier Alpha Codes
    - **EDI Compatibility**: Perfect for EDI transaction processing
    - **Complete Profile**: Full carrier information and capabilities

    ### Use Cases
    - EDI transaction processing and mapping
    - Business partner integration
    - Legacy system integration
    - Quick carrier lookup during operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_code (str):  Example: FDXF.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            carrier_code=carrier_code,
            client=client,
        )
    ).parsed
