from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_company_ledger_by_world_id_response_200 import GetCompanyLedgerByWorldIdResponse200
from ...models.get_company_ledger_by_world_id_response_404 import GetCompanyLedgerByWorldIdResponse404
from ...types import Response


def _get_kwargs(
    world_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/ledger",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]]:
    if response.status_code == 200:
        response_200 = GetCompanyLedgerByWorldIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetCompanyLedgerByWorldIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]]:
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
) -> Response[Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]]:
    """Get company ledger by world ID


    Retrieve the company ledger for the specified world environment.

    **Core Features**:
    - **World-Specific**: Get ledger for specific world environment
    - **Complete Position**: Returns cash, receivables, payables, and calculated net position
    - **Fast Lookup**: Optimized query using unique world ID index
    - **Financial Intelligence**: Access complete financial position for analysis

    **Use Cases**:
    - **Financial Dashboard**: Get current financial position for dashboards
    - **Balance Inquiry**: Check company financial position and cash flow
    - **Reporting**: Access ledger data for financial reporting and analysis
    - **Integration Support**: Provide financial position data to external systems

    **Response**: Returns null if no ledger exists for the world.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]]
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
) -> Optional[Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]]:
    """Get company ledger by world ID


    Retrieve the company ledger for the specified world environment.

    **Core Features**:
    - **World-Specific**: Get ledger for specific world environment
    - **Complete Position**: Returns cash, receivables, payables, and calculated net position
    - **Fast Lookup**: Optimized query using unique world ID index
    - **Financial Intelligence**: Access complete financial position for analysis

    **Use Cases**:
    - **Financial Dashboard**: Get current financial position for dashboards
    - **Balance Inquiry**: Check company financial position and cash flow
    - **Reporting**: Access ledger data for financial reporting and analysis
    - **Integration Support**: Provide financial position data to external systems

    **Response**: Returns null if no ledger exists for the world.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]]:
    """Get company ledger by world ID


    Retrieve the company ledger for the specified world environment.

    **Core Features**:
    - **World-Specific**: Get ledger for specific world environment
    - **Complete Position**: Returns cash, receivables, payables, and calculated net position
    - **Fast Lookup**: Optimized query using unique world ID index
    - **Financial Intelligence**: Access complete financial position for analysis

    **Use Cases**:
    - **Financial Dashboard**: Get current financial position for dashboards
    - **Balance Inquiry**: Check company financial position and cash flow
    - **Reporting**: Access ledger data for financial reporting and analysis
    - **Integration Support**: Provide financial position data to external systems

    **Response**: Returns null if no ledger exists for the world.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]]
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
) -> Optional[Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]]:
    """Get company ledger by world ID


    Retrieve the company ledger for the specified world environment.

    **Core Features**:
    - **World-Specific**: Get ledger for specific world environment
    - **Complete Position**: Returns cash, receivables, payables, and calculated net position
    - **Fast Lookup**: Optimized query using unique world ID index
    - **Financial Intelligence**: Access complete financial position for analysis

    **Use Cases**:
    - **Financial Dashboard**: Get current financial position for dashboards
    - **Balance Inquiry**: Check company financial position and cash flow
    - **Reporting**: Access ledger data for financial reporting and analysis
    - **Integration Support**: Provide financial position data to external systems

    **Response**: Returns null if no ledger exists for the world.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCompanyLedgerByWorldIdResponse200, GetCompanyLedgerByWorldIdResponse404]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
        )
    ).parsed
