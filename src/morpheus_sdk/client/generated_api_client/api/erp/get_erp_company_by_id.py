from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_erp_company_by_id_response_200 import GetERPCompanyByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    company_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/companies/{company_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetERPCompanyByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetERPCompanyByIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetERPCompanyByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPCompanyByIdResponse200]]:
    """Get ERP company by ID


    Retrieve specific ERP company by unique company identifier for detailed business information access.

    **Core Features**:
    - **Direct Access**: Get company by unique companyId
    - **Complete Profile**: Returns full company data including addresses and financial terms
    - **Fast Lookup**: Optimized query using indexed companyId field
    - **Business Intelligence**: Access comprehensive company business data

    **Use Cases**:
    - **Company Details**: Get complete company information for business operations
    - **Reference Resolution**: Resolve company references from orders and transactions
    - **Partner Management**: Access detailed partner information for relationship management
    - **Integration Support**: Direct API access for external system integration

    **⚠️ Minor Field Naming Note**: Model uses 'duns' field but route parameter is 'dunsNumber' for
    clarity.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        company_id (str):  Example: COMP_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPCompanyByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPCompanyByIdResponse200]]:
    """Get ERP company by ID


    Retrieve specific ERP company by unique company identifier for detailed business information access.

    **Core Features**:
    - **Direct Access**: Get company by unique companyId
    - **Complete Profile**: Returns full company data including addresses and financial terms
    - **Fast Lookup**: Optimized query using indexed companyId field
    - **Business Intelligence**: Access comprehensive company business data

    **Use Cases**:
    - **Company Details**: Get complete company information for business operations
    - **Reference Resolution**: Resolve company references from orders and transactions
    - **Partner Management**: Access detailed partner information for relationship management
    - **Integration Support**: Direct API access for external system integration

    **⚠️ Minor Field Naming Note**: Model uses 'duns' field but route parameter is 'dunsNumber' for
    clarity.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        company_id (str):  Example: COMP_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPCompanyByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        company_id=company_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPCompanyByIdResponse200]]:
    """Get ERP company by ID


    Retrieve specific ERP company by unique company identifier for detailed business information access.

    **Core Features**:
    - **Direct Access**: Get company by unique companyId
    - **Complete Profile**: Returns full company data including addresses and financial terms
    - **Fast Lookup**: Optimized query using indexed companyId field
    - **Business Intelligence**: Access comprehensive company business data

    **Use Cases**:
    - **Company Details**: Get complete company information for business operations
    - **Reference Resolution**: Resolve company references from orders and transactions
    - **Partner Management**: Access detailed partner information for relationship management
    - **Integration Support**: Direct API access for external system integration

    **⚠️ Minor Field Naming Note**: Model uses 'duns' field but route parameter is 'dunsNumber' for
    clarity.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        company_id (str):  Example: COMP_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPCompanyByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPCompanyByIdResponse200]]:
    """Get ERP company by ID


    Retrieve specific ERP company by unique company identifier for detailed business information access.

    **Core Features**:
    - **Direct Access**: Get company by unique companyId
    - **Complete Profile**: Returns full company data including addresses and financial terms
    - **Fast Lookup**: Optimized query using indexed companyId field
    - **Business Intelligence**: Access comprehensive company business data

    **Use Cases**:
    - **Company Details**: Get complete company information for business operations
    - **Reference Resolution**: Resolve company references from orders and transactions
    - **Partner Management**: Access detailed partner information for relationship management
    - **Integration Support**: Direct API access for external system integration

    **⚠️ Minor Field Naming Note**: Model uses 'duns' field but route parameter is 'dunsNumber' for
    clarity.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        company_id (str):  Example: COMP_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPCompanyByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            company_id=company_id,
            client=client,
        )
    ).parsed
