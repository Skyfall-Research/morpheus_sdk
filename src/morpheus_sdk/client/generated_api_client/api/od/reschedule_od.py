from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reschedule_od_body import RescheduleODBody
from ...models.reschedule_od_response_200 import RescheduleODResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    od_id: str,
    job_id: str,
    *,
    body: RescheduleODBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/od/descriptors/{od_id}/schedules/{job_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RescheduleODResponse200]:
    if response.status_code == 200:
        response_200 = RescheduleODResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RescheduleODResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    od_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RescheduleODBody,
) -> Response[RescheduleODResponse200]:
    """Reschedule an OD job

    Args:
        world_id (str):
        od_id (str):
        job_id (str):
        body (RescheduleODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RescheduleODResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_id=od_id,
        job_id=job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    od_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RescheduleODBody,
) -> Optional[RescheduleODResponse200]:
    """Reschedule an OD job

    Args:
        world_id (str):
        od_id (str):
        job_id (str):
        body (RescheduleODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RescheduleODResponse200
    """

    return sync_detailed(
        world_id=world_id,
        od_id=od_id,
        job_id=job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    od_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RescheduleODBody,
) -> Response[RescheduleODResponse200]:
    """Reschedule an OD job

    Args:
        world_id (str):
        od_id (str):
        job_id (str):
        body (RescheduleODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RescheduleODResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_id=od_id,
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    od_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RescheduleODBody,
) -> Optional[RescheduleODResponse200]:
    """Reschedule an OD job

    Args:
        world_id (str):
        od_id (str):
        job_id (str):
        body (RescheduleODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RescheduleODResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            od_id=od_id,
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
