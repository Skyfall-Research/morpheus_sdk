from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.validate_od_body import ValidateODBody
from ...models.validate_od_response_200 import ValidateODResponse200
from ...types import Response


def _get_kwargs(
    world_id: UUID,
    *,
    body: ValidateODBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/od/validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ValidateODResponse200]]:
    if response.status_code == 200:
        response_200 = ValidateODResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, ValidateODResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateODBody,
) -> Response[Union[ErrorResponse, ValidateODResponse200]]:
    """Validate an OD schema

     Validates an Operational Descriptor definition against the schema without saving it.

    Args:
        world_id (UUID):
        body (ValidateODBody): The OD definition to validate

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ValidateODResponse200]]
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
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateODBody,
) -> Optional[Union[ErrorResponse, ValidateODResponse200]]:
    """Validate an OD schema

     Validates an Operational Descriptor definition against the schema without saving it.

    Args:
        world_id (UUID):
        body (ValidateODBody): The OD definition to validate

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ValidateODResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateODBody,
) -> Response[Union[ErrorResponse, ValidateODResponse200]]:
    """Validate an OD schema

     Validates an Operational Descriptor definition against the schema without saving it.

    Args:
        world_id (UUID):
        body (ValidateODBody): The OD definition to validate

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ValidateODResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateODBody,
) -> Optional[Union[ErrorResponse, ValidateODResponse200]]:
    """Validate an OD schema

     Validates an Operational Descriptor definition against the schema without saving it.

    Args:
        world_id (UUID):
        body (ValidateODBody): The OD definition to validate

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ValidateODResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
