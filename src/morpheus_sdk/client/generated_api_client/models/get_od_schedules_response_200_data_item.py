import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_od_schedules_response_200_data_item_data import GetODSchedulesResponse200DataItemData
    from ..models.get_od_schedules_response_200_data_item_last_run_result import (
        GetODSchedulesResponse200DataItemLastRunResult,
    )


T = TypeVar("T", bound="GetODSchedulesResponse200DataItem")


@_attrs_define
class GetODSchedulesResponse200DataItem:
    """
    Attributes:
        job_id (Union[Unset, str]):
        next_run_at (Union[Unset, datetime.datetime]):
        last_run_at (Union[Unset, datetime.datetime]):
        interval (Union[Unset, str]):
        is_recurring (Union[Unset, bool]):
        last_run_result (Union[Unset, GetODSchedulesResponse200DataItemLastRunResult]):
        data (Union[Unset, GetODSchedulesResponse200DataItemData]):
    """

    job_id: Union[Unset, str] = UNSET
    next_run_at: Union[Unset, datetime.datetime] = UNSET
    last_run_at: Union[Unset, datetime.datetime] = UNSET
    interval: Union[Unset, str] = UNSET
    is_recurring: Union[Unset, bool] = UNSET
    last_run_result: Union[Unset, "GetODSchedulesResponse200DataItemLastRunResult"] = UNSET
    data: Union[Unset, "GetODSchedulesResponse200DataItemData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        next_run_at: Union[Unset, str] = UNSET
        if not isinstance(self.next_run_at, Unset):
            next_run_at = self.next_run_at.isoformat()

        last_run_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_run_at, Unset):
            last_run_at = self.last_run_at.isoformat()

        interval = self.interval

        is_recurring = self.is_recurring

        last_run_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_run_result, Unset):
            last_run_result = self.last_run_result.to_dict()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if next_run_at is not UNSET:
            field_dict["nextRunAt"] = next_run_at
        if last_run_at is not UNSET:
            field_dict["lastRunAt"] = last_run_at
        if interval is not UNSET:
            field_dict["interval"] = interval
        if is_recurring is not UNSET:
            field_dict["isRecurring"] = is_recurring
        if last_run_result is not UNSET:
            field_dict["lastRunResult"] = last_run_result
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_od_schedules_response_200_data_item_data import GetODSchedulesResponse200DataItemData
        from ..models.get_od_schedules_response_200_data_item_last_run_result import (
            GetODSchedulesResponse200DataItemLastRunResult,
        )

        d = dict(src_dict)
        job_id = d.pop("jobId", UNSET)

        _next_run_at = d.pop("nextRunAt", UNSET)
        next_run_at: Union[Unset, datetime.datetime]
        if isinstance(_next_run_at, Unset):
            next_run_at = UNSET
        else:
            next_run_at = isoparse(_next_run_at)

        _last_run_at = d.pop("lastRunAt", UNSET)
        last_run_at: Union[Unset, datetime.datetime]
        if isinstance(_last_run_at, Unset):
            last_run_at = UNSET
        else:
            last_run_at = isoparse(_last_run_at)

        interval = d.pop("interval", UNSET)

        is_recurring = d.pop("isRecurring", UNSET)

        _last_run_result = d.pop("lastRunResult", UNSET)
        last_run_result: Union[Unset, GetODSchedulesResponse200DataItemLastRunResult]
        if isinstance(_last_run_result, Unset):
            last_run_result = UNSET
        else:
            last_run_result = GetODSchedulesResponse200DataItemLastRunResult.from_dict(_last_run_result)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GetODSchedulesResponse200DataItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetODSchedulesResponse200DataItemData.from_dict(_data)

        get_od_schedules_response_200_data_item = cls(
            job_id=job_id,
            next_run_at=next_run_at,
            last_run_at=last_run_at,
            interval=interval,
            is_recurring=is_recurring,
            last_run_result=last_run_result,
            data=data,
        )

        get_od_schedules_response_200_data_item.additional_properties = d
        return get_od_schedules_response_200_data_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
