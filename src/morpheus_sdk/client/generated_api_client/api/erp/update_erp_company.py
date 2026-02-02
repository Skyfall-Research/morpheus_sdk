from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_company_body import UpdateERPCompanyBody
from ...models.update_erp_company_response_200 import UpdateERPCompanyResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    company_id: str,
    *,
    body: UpdateERPCompanyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/companies/{company_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPCompanyResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPCompanyResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPCompanyResponse200]]:
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
    body: UpdateERPCompanyBody,
) -> Response[Union[ErrorResponse, UpdateERPCompanyResponse200]]:
    """Update ERP company


    Update ERP company information with partial data for business relationship maintenance.

    **Core Features**:
    - **Partial Updates**: Update specific company fields without replacing entire record
    - **MPC Management**: Handle Main Player Company designation with automatic exclusivity
    - **Business Configuration**: Modify financial terms, addresses, and operational settings
    - **Validation**: Ensures data consistency and business rule compliance

    **Use Cases**:
    - **Profile Updates**: Update company contact information and addresses
    - **Financial Changes**: Modify credit limits, payment terms, and currency settings
    - **Status Management**: Change company status for operational control
    - **Relationship Updates**: Update company type and business relationship classification


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        company_id (str):  Example: COMP_507f1f77bcf86cd799439012.
        body (UpdateERPCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPCompanyResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        company_id=company_id,
        body=body,
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
    body: UpdateERPCompanyBody,
) -> Optional[Union[ErrorResponse, UpdateERPCompanyResponse200]]:
    """Update ERP company


    Update ERP company information with partial data for business relationship maintenance.

    **Core Features**:
    - **Partial Updates**: Update specific company fields without replacing entire record
    - **MPC Management**: Handle Main Player Company designation with automatic exclusivity
    - **Business Configuration**: Modify financial terms, addresses, and operational settings
    - **Validation**: Ensures data consistency and business rule compliance

    **Use Cases**:
    - **Profile Updates**: Update company contact information and addresses
    - **Financial Changes**: Modify credit limits, payment terms, and currency settings
    - **Status Management**: Change company status for operational control
    - **Relationship Updates**: Update company type and business relationship classification


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        company_id (str):  Example: COMP_507f1f77bcf86cd799439012.
        body (UpdateERPCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPCompanyResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        company_id=company_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPCompanyBody,
) -> Response[Union[ErrorResponse, UpdateERPCompanyResponse200]]:
    """Update ERP company


    Update ERP company information with partial data for business relationship maintenance.

    **Core Features**:
    - **Partial Updates**: Update specific company fields without replacing entire record
    - **MPC Management**: Handle Main Player Company designation with automatic exclusivity
    - **Business Configuration**: Modify financial terms, addresses, and operational settings
    - **Validation**: Ensures data consistency and business rule compliance

    **Use Cases**:
    - **Profile Updates**: Update company contact information and addresses
    - **Financial Changes**: Modify credit limits, payment terms, and currency settings
    - **Status Management**: Change company status for operational control
    - **Relationship Updates**: Update company type and business relationship classification


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        company_id (str):  Example: COMP_507f1f77bcf86cd799439012.
        body (UpdateERPCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPCompanyResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        company_id=company_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    company_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPCompanyBody,
) -> Optional[Union[ErrorResponse, UpdateERPCompanyResponse200]]:
    """Update ERP company


    Update ERP company information with partial data for business relationship maintenance.

    **Core Features**:
    - **Partial Updates**: Update specific company fields without replacing entire record
    - **MPC Management**: Handle Main Player Company designation with automatic exclusivity
    - **Business Configuration**: Modify financial terms, addresses, and operational settings
    - **Validation**: Ensures data consistency and business rule compliance

    **Use Cases**:
    - **Profile Updates**: Update company contact information and addresses
    - **Financial Changes**: Modify credit limits, payment terms, and currency settings
    - **Status Management**: Change company status for operational control
    - **Relationship Updates**: Update company type and business relationship classification


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        company_id (str):  Example: COMP_507f1f77bcf86cd799439012.
        body (UpdateERPCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPCompanyResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            company_id=company_id,
            client=client,
            body=body,
        )
    ).parsed
