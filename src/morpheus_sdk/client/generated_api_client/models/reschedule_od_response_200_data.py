import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RescheduleODResponse200Data")


@_attrs_define
class RescheduleODResponse200Data:
    """
    Attributes:
        job_id (Union[Unset, str]):
        new_scheduled_time (Union[Unset, datetime.datetime]):
        previous_time (Union[Unset, datetime.datetime]):
    """

    job_id: Union[Unset, str] = UNSET
    new_scheduled_time: Union[Unset, datetime.datetime] = UNSET
    previous_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        new_scheduled_time: Union[Unset, str] = UNSET
        if not isinstance(self.new_scheduled_time, Unset):
            new_scheduled_time = self.new_scheduled_time.isoformat()

        previous_time: Union[Unset, str] = UNSET
        if not isinstance(self.previous_time, Unset):
            previous_time = self.previous_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if new_scheduled_time is not UNSET:
            field_dict["newScheduledTime"] = new_scheduled_time
        if previous_time is not UNSET:
            field_dict["previousTime"] = previous_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId", UNSET)

        _new_scheduled_time = d.pop("newScheduledTime", UNSET)
        new_scheduled_time: Union[Unset, datetime.datetime]
        if isinstance(_new_scheduled_time, Unset):
            new_scheduled_time = UNSET
        else:
            new_scheduled_time = isoparse(_new_scheduled_time)

        _previous_time = d.pop("previousTime", UNSET)
        previous_time: Union[Unset, datetime.datetime]
        if isinstance(_previous_time, Unset):
            previous_time = UNSET
        else:
            previous_time = isoparse(_previous_time)

        reschedule_od_response_200_data = cls(
            job_id=job_id,
            new_scheduled_time=new_scheduled_time,
            previous_time=previous_time,
        )

        reschedule_od_response_200_data.additional_properties = d
        return reschedule_od_response_200_data

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
