from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.increment_company_ledger_balances_body import IncrementCompanyLedgerBalancesBody
from ...models.increment_company_ledger_balances_response_200 import IncrementCompanyLedgerBalancesResponse200
from ...models.increment_company_ledger_balances_response_400 import IncrementCompanyLedgerBalancesResponse400
from ...models.increment_company_ledger_balances_response_404 import IncrementCompanyLedgerBalancesResponse404
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: IncrementCompanyLedgerBalancesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/{world_id}/ledger/increment",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        IncrementCompanyLedgerBalancesResponse200,
        IncrementCompanyLedgerBalancesResponse400,
        IncrementCompanyLedgerBalancesResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = IncrementCompanyLedgerBalancesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = IncrementCompanyLedgerBalancesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = IncrementCompanyLedgerBalancesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        IncrementCompanyLedgerBalancesResponse200,
        IncrementCompanyLedgerBalancesResponse400,
        IncrementCompanyLedgerBalancesResponse404,
    ]
]:
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
    body: IncrementCompanyLedgerBalancesBody,
) -> Response[
    Union[
        IncrementCompanyLedgerBalancesResponse200,
        IncrementCompanyLedgerBalancesResponse400,
        IncrementCompanyLedgerBalancesResponse404,
    ]
]:
    """Increment company ledger balances


    Increment or decrement company ledger balances using delta values for precise financial adjustments.

    **Core Features**:
    - **Delta-Based Updates**: Use delta values for precise incremental changes
    - **Multi-Balance Support**: Update cash, receivables, and payables in single operation
    - **Auto-Calculated Net Position**: Net position recalculated automatically after increments
    - **Atomic Operations**: All balance changes applied atomically for consistency

    **Use Cases**:
    - **Transaction Processing**: Apply financial transaction impacts to ledger
    - **Payment Processing**: Increment/decrement balances based on payment activity
    - **Adjustment Entries**: Apply accounting adjustments and corrections
    - **Integration Updates**: Process incremental changes from external systems

    **Delta Logic**:
    - **Positive Values**: Increase balances
    - **Negative Values**: Decrease balances
    - **At Least One Required**: Must provide at least one delta value

    **Important**: Net position automatically recalculated as: cash + totalReceivables - totalPayables


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (IncrementCompanyLedgerBalancesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IncrementCompanyLedgerBalancesResponse200, IncrementCompanyLedgerBalancesResponse400, IncrementCompanyLedgerBalancesResponse404]]
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
    body: IncrementCompanyLedgerBalancesBody,
) -> Optional[
    Union[
        IncrementCompanyLedgerBalancesResponse200,
        IncrementCompanyLedgerBalancesResponse400,
        IncrementCompanyLedgerBalancesResponse404,
    ]
]:
    """Increment company ledger balances


    Increment or decrement company ledger balances using delta values for precise financial adjustments.

    **Core Features**:
    - **Delta-Based Updates**: Use delta values for precise incremental changes
    - **Multi-Balance Support**: Update cash, receivables, and payables in single operation
    - **Auto-Calculated Net Position**: Net position recalculated automatically after increments
    - **Atomic Operations**: All balance changes applied atomically for consistency

    **Use Cases**:
    - **Transaction Processing**: Apply financial transaction impacts to ledger
    - **Payment Processing**: Increment/decrement balances based on payment activity
    - **Adjustment Entries**: Apply accounting adjustments and corrections
    - **Integration Updates**: Process incremental changes from external systems

    **Delta Logic**:
    - **Positive Values**: Increase balances
    - **Negative Values**: Decrease balances
    - **At Least One Required**: Must provide at least one delta value

    **Important**: Net position automatically recalculated as: cash + totalReceivables - totalPayables


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (IncrementCompanyLedgerBalancesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IncrementCompanyLedgerBalancesResponse200, IncrementCompanyLedgerBalancesResponse400, IncrementCompanyLedgerBalancesResponse404]
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
    body: IncrementCompanyLedgerBalancesBody,
) -> Response[
    Union[
        IncrementCompanyLedgerBalancesResponse200,
        IncrementCompanyLedgerBalancesResponse400,
        IncrementCompanyLedgerBalancesResponse404,
    ]
]:
    """Increment company ledger balances


    Increment or decrement company ledger balances using delta values for precise financial adjustments.

    **Core Features**:
    - **Delta-Based Updates**: Use delta values for precise incremental changes
    - **Multi-Balance Support**: Update cash, receivables, and payables in single operation
    - **Auto-Calculated Net Position**: Net position recalculated automatically after increments
    - **Atomic Operations**: All balance changes applied atomically for consistency

    **Use Cases**:
    - **Transaction Processing**: Apply financial transaction impacts to ledger
    - **Payment Processing**: Increment/decrement balances based on payment activity
    - **Adjustment Entries**: Apply accounting adjustments and corrections
    - **Integration Updates**: Process incremental changes from external systems

    **Delta Logic**:
    - **Positive Values**: Increase balances
    - **Negative Values**: Decrease balances
    - **At Least One Required**: Must provide at least one delta value

    **Important**: Net position automatically recalculated as: cash + totalReceivables - totalPayables


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (IncrementCompanyLedgerBalancesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IncrementCompanyLedgerBalancesResponse200, IncrementCompanyLedgerBalancesResponse400, IncrementCompanyLedgerBalancesResponse404]]
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
    body: IncrementCompanyLedgerBalancesBody,
) -> Optional[
    Union[
        IncrementCompanyLedgerBalancesResponse200,
        IncrementCompanyLedgerBalancesResponse400,
        IncrementCompanyLedgerBalancesResponse404,
    ]
]:
    """Increment company ledger balances


    Increment or decrement company ledger balances using delta values for precise financial adjustments.

    **Core Features**:
    - **Delta-Based Updates**: Use delta values for precise incremental changes
    - **Multi-Balance Support**: Update cash, receivables, and payables in single operation
    - **Auto-Calculated Net Position**: Net position recalculated automatically after increments
    - **Atomic Operations**: All balance changes applied atomically for consistency

    **Use Cases**:
    - **Transaction Processing**: Apply financial transaction impacts to ledger
    - **Payment Processing**: Increment/decrement balances based on payment activity
    - **Adjustment Entries**: Apply accounting adjustments and corrections
    - **Integration Updates**: Process incremental changes from external systems

    **Delta Logic**:
    - **Positive Values**: Increase balances
    - **Negative Values**: Decrease balances
    - **At Least One Required**: Must provide at least one delta value

    **Important**: Net position automatically recalculated as: cash + totalReceivables - totalPayables


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (IncrementCompanyLedgerBalancesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IncrementCompanyLedgerBalancesResponse200, IncrementCompanyLedgerBalancesResponse400, IncrementCompanyLedgerBalancesResponse404]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
