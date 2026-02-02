from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_mpc_erp_company_response_200 import GetMpcERPCompanyResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/companies/mpc",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetMpcERPCompanyResponse200]]:
    if response.status_code == 200:
        response_200 = GetMpcERPCompanyResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetMpcERPCompanyResponse200]]:
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
) -> Response[Union[ErrorResponse, GetMpcERPCompanyResponse200]]:
    """Get Main Player Company (MPC)


    Retrieve the designated Main Player Company (MPC) for the world environment.

    **Core Features**:
    - **MPC Identification**: Get the single MPC designated for the world
    - **Exclusive Access**: Returns the company marked with isMpcCompany=true
    - **World Scoping**: Ensures world-specific MPC isolation
    - **Complete Profile**: Returns full company data including addresses and contacts

    **Use Cases**:
    - **System Configuration**: Identify the primary company for world operations
    - **Business Rules**: Access MPC data for business logic and workflows
    - **Financial Operations**: Use MPC information for internal financial processes
    - **Integration Points**: Primary company reference for external system integration

    **Important**: Only one MPC can exist per world environment.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetMpcERPCompanyResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetMpcERPCompanyResponse200]]:
    """Get Main Player Company (MPC)


    Retrieve the designated Main Player Company (MPC) for the world environment.

    **Core Features**:
    - **MPC Identification**: Get the single MPC designated for the world
    - **Exclusive Access**: Returns the company marked with isMpcCompany=true
    - **World Scoping**: Ensures world-specific MPC isolation
    - **Complete Profile**: Returns full company data including addresses and contacts

    **Use Cases**:
    - **System Configuration**: Identify the primary company for world operations
    - **Business Rules**: Access MPC data for business logic and workflows
    - **Financial Operations**: Use MPC information for internal financial processes
    - **Integration Points**: Primary company reference for external system integration

    **Important**: Only one MPC can exist per world environment.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetMpcERPCompanyResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetMpcERPCompanyResponse200]]:
    """Get Main Player Company (MPC)


    Retrieve the designated Main Player Company (MPC) for the world environment.

    **Core Features**:
    - **MPC Identification**: Get the single MPC designated for the world
    - **Exclusive Access**: Returns the company marked with isMpcCompany=true
    - **World Scoping**: Ensures world-specific MPC isolation
    - **Complete Profile**: Returns full company data including addresses and contacts

    **Use Cases**:
    - **System Configuration**: Identify the primary company for world operations
    - **Business Rules**: Access MPC data for business logic and workflows
    - **Financial Operations**: Use MPC information for internal financial processes
    - **Integration Points**: Primary company reference for external system integration

    **Important**: Only one MPC can exist per world environment.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetMpcERPCompanyResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetMpcERPCompanyResponse200]]:
    """Get Main Player Company (MPC)


    Retrieve the designated Main Player Company (MPC) for the world environment.

    **Core Features**:
    - **MPC Identification**: Get the single MPC designated for the world
    - **Exclusive Access**: Returns the company marked with isMpcCompany=true
    - **World Scoping**: Ensures world-specific MPC isolation
    - **Complete Profile**: Returns full company data including addresses and contacts

    **Use Cases**:
    - **System Configuration**: Identify the primary company for world operations
    - **Business Rules**: Access MPC data for business logic and workflows
    - **Financial Operations**: Use MPC information for internal financial processes
    - **Integration Points**: Primary company reference for external system integration

    **Important**: Only one MPC can exist per world environment.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetMpcERPCompanyResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
        )
    ).parsed
