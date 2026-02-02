from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_erp_company_body import CreateERPCompanyBody
from ...models.create_erp_company_response_201 import CreateERPCompanyResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateERPCompanyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/erp/companies",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateERPCompanyResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateERPCompanyResponse201.from_dict(response.json())

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
) -> Response[Union[CreateERPCompanyResponse201, ErrorResponse]]:
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
    body: CreateERPCompanyBody,
) -> Response[Union[CreateERPCompanyResponse201, ErrorResponse]]:
    """Create new ERP company


    Create a new ERP company record with comprehensive business information and operational
    configuration.

    **Core Features**:
    - **Company Registration**: Complete business entity setup with legal and operational details
    - **Auto-Generated IDs**: Automatic companyId generation via generateIdByService
    - **MPC Management**: Support for Main Player Company (MPC) designation with automatic exclusivity
    - **Multi-Address Support**: Billing, shipping, and remit-to address configuration
    - **Financial Configuration**: Credit limits, payment terms, and currency management

    **Use Cases**:
    - **Partner Onboarding**: Register new customers, suppliers, and business partners
    - **ERP Integration**: Create company records for ERP system synchronization
    - **B2B Network Setup**: Establish business relationships with comprehensive company data
    - **Financial Management**: Configure credit terms and payment relationships


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPCompanyResponse201, ErrorResponse]]
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
    body: CreateERPCompanyBody,
) -> Optional[Union[CreateERPCompanyResponse201, ErrorResponse]]:
    """Create new ERP company


    Create a new ERP company record with comprehensive business information and operational
    configuration.

    **Core Features**:
    - **Company Registration**: Complete business entity setup with legal and operational details
    - **Auto-Generated IDs**: Automatic companyId generation via generateIdByService
    - **MPC Management**: Support for Main Player Company (MPC) designation with automatic exclusivity
    - **Multi-Address Support**: Billing, shipping, and remit-to address configuration
    - **Financial Configuration**: Credit limits, payment terms, and currency management

    **Use Cases**:
    - **Partner Onboarding**: Register new customers, suppliers, and business partners
    - **ERP Integration**: Create company records for ERP system synchronization
    - **B2B Network Setup**: Establish business relationships with comprehensive company data
    - **Financial Management**: Configure credit terms and payment relationships


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPCompanyResponse201, ErrorResponse]
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
    body: CreateERPCompanyBody,
) -> Response[Union[CreateERPCompanyResponse201, ErrorResponse]]:
    """Create new ERP company


    Create a new ERP company record with comprehensive business information and operational
    configuration.

    **Core Features**:
    - **Company Registration**: Complete business entity setup with legal and operational details
    - **Auto-Generated IDs**: Automatic companyId generation via generateIdByService
    - **MPC Management**: Support for Main Player Company (MPC) designation with automatic exclusivity
    - **Multi-Address Support**: Billing, shipping, and remit-to address configuration
    - **Financial Configuration**: Credit limits, payment terms, and currency management

    **Use Cases**:
    - **Partner Onboarding**: Register new customers, suppliers, and business partners
    - **ERP Integration**: Create company records for ERP system synchronization
    - **B2B Network Setup**: Establish business relationships with comprehensive company data
    - **Financial Management**: Configure credit terms and payment relationships


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPCompanyResponse201, ErrorResponse]]
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
    body: CreateERPCompanyBody,
) -> Optional[Union[CreateERPCompanyResponse201, ErrorResponse]]:
    """Create new ERP company


    Create a new ERP company record with comprehensive business information and operational
    configuration.

    **Core Features**:
    - **Company Registration**: Complete business entity setup with legal and operational details
    - **Auto-Generated IDs**: Automatic companyId generation via generateIdByService
    - **MPC Management**: Support for Main Player Company (MPC) designation with automatic exclusivity
    - **Multi-Address Support**: Billing, shipping, and remit-to address configuration
    - **Financial Configuration**: Credit limits, payment terms, and currency management

    **Use Cases**:
    - **Partner Onboarding**: Register new customers, suppliers, and business partners
    - **ERP Integration**: Create company records for ERP system synchronization
    - **B2B Network Setup**: Establish business relationships with comprehensive company data
    - **Financial Management**: Configure credit terms and payment relationships


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPCompanyResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
