from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_edi_transaction_body import CreateEdiTransactionBody
from ...models.create_edi_transaction_response_201 import CreateEdiTransactionResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateEdiTransactionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/edi",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateEdiTransactionResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateEdiTransactionResponse201.from_dict(response.json())

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
) -> Response[Union[CreateEdiTransactionResponse201, ErrorResponse]]:
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
    body: CreateEdiTransactionBody,
) -> Response[Union[CreateEdiTransactionResponse201, ErrorResponse]]:
    """Create a new EDI transaction


    ## Create EDI Transaction

    Submit a new EDI transaction for processing with automatic parsing and validation.

    ### Features
    - **Automatic Parsing**: Extract business metadata from raw EDI
    - **Idempotency Protection**: Duplicate detection and prevention
    - **Business Rule Validation**: EDI standards and business requirements
    - **Dollar Value Extraction**: Automatic monetary value calculation
    - **Control Number Tracking**: Full X12 control number hierarchy


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateEdiTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateEdiTransactionResponse201, ErrorResponse]]
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
    body: CreateEdiTransactionBody,
) -> Optional[Union[CreateEdiTransactionResponse201, ErrorResponse]]:
    """Create a new EDI transaction


    ## Create EDI Transaction

    Submit a new EDI transaction for processing with automatic parsing and validation.

    ### Features
    - **Automatic Parsing**: Extract business metadata from raw EDI
    - **Idempotency Protection**: Duplicate detection and prevention
    - **Business Rule Validation**: EDI standards and business requirements
    - **Dollar Value Extraction**: Automatic monetary value calculation
    - **Control Number Tracking**: Full X12 control number hierarchy


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateEdiTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateEdiTransactionResponse201, ErrorResponse]
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
    body: CreateEdiTransactionBody,
) -> Response[Union[CreateEdiTransactionResponse201, ErrorResponse]]:
    """Create a new EDI transaction


    ## Create EDI Transaction

    Submit a new EDI transaction for processing with automatic parsing and validation.

    ### Features
    - **Automatic Parsing**: Extract business metadata from raw EDI
    - **Idempotency Protection**: Duplicate detection and prevention
    - **Business Rule Validation**: EDI standards and business requirements
    - **Dollar Value Extraction**: Automatic monetary value calculation
    - **Control Number Tracking**: Full X12 control number hierarchy


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateEdiTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateEdiTransactionResponse201, ErrorResponse]]
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
    body: CreateEdiTransactionBody,
) -> Optional[Union[CreateEdiTransactionResponse201, ErrorResponse]]:
    """Create a new EDI transaction


    ## Create EDI Transaction

    Submit a new EDI transaction for processing with automatic parsing and validation.

    ### Features
    - **Automatic Parsing**: Extract business metadata from raw EDI
    - **Idempotency Protection**: Duplicate detection and prevention
    - **Business Rule Validation**: EDI standards and business requirements
    - **Dollar Value Extraction**: Automatic monetary value calculation
    - **Control Number Tracking**: Full X12 control number hierarchy


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateEdiTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateEdiTransactionResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
