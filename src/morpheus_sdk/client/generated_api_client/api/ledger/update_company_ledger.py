from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_company_ledger_body import UpdateCompanyLedgerBody
from ...models.update_company_ledger_response_200 import UpdateCompanyLedgerResponse200
from ...models.update_company_ledger_response_404 import UpdateCompanyLedgerResponse404
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: UpdateCompanyLedgerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/{world_id}/ledger",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]]:
    if response.status_code == 200:
        response_200 = UpdateCompanyLedgerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = UpdateCompanyLedgerResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]]:
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
    body: UpdateCompanyLedgerBody,
) -> Response[Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]]:
    """Update company ledger


    Update company ledger with partial data for financial position management.

    **Core Features**:
    - **Partial Updates**: Update specific ledger fields without replacing entire record
    - **Auto-Calculated Net Position**: Net position automatically recalculated after updates
    - **Financial Management**: Modify cash, receivables, and payables positions
    - **Validation**: Ensures updated data meets business rules and constraints

    **Use Cases**:
    - **Balance Adjustments**: Update financial positions per accounting operations
    - **Position Corrections**: Modify ledger balances for corrections or reconciliations
    - **Integration Updates**: Synchronize positions from external accounting systems
    - **Period-End Adjustments**: Update balances for month-end or year-end processes

    **Important**: Net position is recalculated automatically and cannot be manually updated.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateCompanyLedgerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]]
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
    body: UpdateCompanyLedgerBody,
) -> Optional[Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]]:
    """Update company ledger


    Update company ledger with partial data for financial position management.

    **Core Features**:
    - **Partial Updates**: Update specific ledger fields without replacing entire record
    - **Auto-Calculated Net Position**: Net position automatically recalculated after updates
    - **Financial Management**: Modify cash, receivables, and payables positions
    - **Validation**: Ensures updated data meets business rules and constraints

    **Use Cases**:
    - **Balance Adjustments**: Update financial positions per accounting operations
    - **Position Corrections**: Modify ledger balances for corrections or reconciliations
    - **Integration Updates**: Synchronize positions from external accounting systems
    - **Period-End Adjustments**: Update balances for month-end or year-end processes

    **Important**: Net position is recalculated automatically and cannot be manually updated.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateCompanyLedgerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]
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
    body: UpdateCompanyLedgerBody,
) -> Response[Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]]:
    """Update company ledger


    Update company ledger with partial data for financial position management.

    **Core Features**:
    - **Partial Updates**: Update specific ledger fields without replacing entire record
    - **Auto-Calculated Net Position**: Net position automatically recalculated after updates
    - **Financial Management**: Modify cash, receivables, and payables positions
    - **Validation**: Ensures updated data meets business rules and constraints

    **Use Cases**:
    - **Balance Adjustments**: Update financial positions per accounting operations
    - **Position Corrections**: Modify ledger balances for corrections or reconciliations
    - **Integration Updates**: Synchronize positions from external accounting systems
    - **Period-End Adjustments**: Update balances for month-end or year-end processes

    **Important**: Net position is recalculated automatically and cannot be manually updated.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateCompanyLedgerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]]
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
    body: UpdateCompanyLedgerBody,
) -> Optional[Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]]:
    """Update company ledger


    Update company ledger with partial data for financial position management.

    **Core Features**:
    - **Partial Updates**: Update specific ledger fields without replacing entire record
    - **Auto-Calculated Net Position**: Net position automatically recalculated after updates
    - **Financial Management**: Modify cash, receivables, and payables positions
    - **Validation**: Ensures updated data meets business rules and constraints

    **Use Cases**:
    - **Balance Adjustments**: Update financial positions per accounting operations
    - **Position Corrections**: Modify ledger balances for corrections or reconciliations
    - **Integration Updates**: Synchronize positions from external accounting systems
    - **Period-End Adjustments**: Update balances for month-end or year-end processes

    **Important**: Net position is recalculated automatically and cannot be manually updated.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateCompanyLedgerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateCompanyLedgerResponse200, UpdateCompanyLedgerResponse404]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
