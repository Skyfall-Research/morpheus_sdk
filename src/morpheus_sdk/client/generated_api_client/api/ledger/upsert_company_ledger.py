from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upsert_company_ledger_body import UpsertCompanyLedgerBody
from ...models.upsert_company_ledger_response_201 import UpsertCompanyLedgerResponse201
from ...models.upsert_company_ledger_response_400 import UpsertCompanyLedgerResponse400
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: UpsertCompanyLedgerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/ledger",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]]:
    if response.status_code == 201:
        response_201 = UpsertCompanyLedgerResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = UpsertCompanyLedgerResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]]:
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
    body: UpsertCompanyLedgerBody,
) -> Response[Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]]:
    """Upsert company ledger


    Create or update the company ledger for comprehensive financial position management.

    **Core Features**:
    - **Upsert Functionality**: Creates new ledger if not exists, updates if exists
    - **Auto-Calculated Net Position**: Automatically calculates netPosition = cash + totalReceivables -
    totalPayables
    - **World-Scoped**: One ledger per world environment with unique constraint
    - **Financial Integration**: Central hub for all financial position tracking

    **Use Cases**:
    - **Initial Setup**: Create company ledger for new financial tracking
    - **Financial Updates**: Update cash, receivables, and payables positions
    - **Balance Reconciliation**: Maintain accurate financial position records
    - **Integration Support**: Synchronize with external accounting systems

    **Important**: Net position is automatically calculated and cannot be manually set.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpsertCompanyLedgerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]]
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
    body: UpsertCompanyLedgerBody,
) -> Optional[Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]]:
    """Upsert company ledger


    Create or update the company ledger for comprehensive financial position management.

    **Core Features**:
    - **Upsert Functionality**: Creates new ledger if not exists, updates if exists
    - **Auto-Calculated Net Position**: Automatically calculates netPosition = cash + totalReceivables -
    totalPayables
    - **World-Scoped**: One ledger per world environment with unique constraint
    - **Financial Integration**: Central hub for all financial position tracking

    **Use Cases**:
    - **Initial Setup**: Create company ledger for new financial tracking
    - **Financial Updates**: Update cash, receivables, and payables positions
    - **Balance Reconciliation**: Maintain accurate financial position records
    - **Integration Support**: Synchronize with external accounting systems

    **Important**: Net position is automatically calculated and cannot be manually set.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpsertCompanyLedgerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]
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
    body: UpsertCompanyLedgerBody,
) -> Response[Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]]:
    """Upsert company ledger


    Create or update the company ledger for comprehensive financial position management.

    **Core Features**:
    - **Upsert Functionality**: Creates new ledger if not exists, updates if exists
    - **Auto-Calculated Net Position**: Automatically calculates netPosition = cash + totalReceivables -
    totalPayables
    - **World-Scoped**: One ledger per world environment with unique constraint
    - **Financial Integration**: Central hub for all financial position tracking

    **Use Cases**:
    - **Initial Setup**: Create company ledger for new financial tracking
    - **Financial Updates**: Update cash, receivables, and payables positions
    - **Balance Reconciliation**: Maintain accurate financial position records
    - **Integration Support**: Synchronize with external accounting systems

    **Important**: Net position is automatically calculated and cannot be manually set.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpsertCompanyLedgerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]]
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
    body: UpsertCompanyLedgerBody,
) -> Optional[Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]]:
    """Upsert company ledger


    Create or update the company ledger for comprehensive financial position management.

    **Core Features**:
    - **Upsert Functionality**: Creates new ledger if not exists, updates if exists
    - **Auto-Calculated Net Position**: Automatically calculates netPosition = cash + totalReceivables -
    totalPayables
    - **World-Scoped**: One ledger per world environment with unique constraint
    - **Financial Integration**: Central hub for all financial position tracking

    **Use Cases**:
    - **Initial Setup**: Create company ledger for new financial tracking
    - **Financial Updates**: Update cash, receivables, and payables positions
    - **Balance Reconciliation**: Maintain accurate financial position records
    - **Integration Support**: Synchronize with external accounting systems

    **Important**: Net position is automatically calculated and cannot be manually set.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpsertCompanyLedgerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpsertCompanyLedgerResponse201, UpsertCompanyLedgerResponse400]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
