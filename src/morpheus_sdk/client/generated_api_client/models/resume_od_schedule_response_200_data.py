import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResumeODScheduleResponse200Data")


@_attrs_define
class ResumeODScheduleResponse200Data:
    """Updated job details

    Attributes:
        message (Union[Unset, str]):
        job_id (Union[Unset, str]):
        next_run_at (Union[Unset, datetime.datetime]):
        disabled (Union[Unset, bool]):
    """

    message: Union[Unset, str] = UNSET
    job_id: Union[Unset, str] = UNSET
    next_run_at: Union[Unset, datetime.datetime] = UNSET
    disabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        job_id = self.job_id

        next_run_at: Union[Unset, str] = UNSET
        if not isinstance(self.next_run_at, Unset):
            next_run_at = self.next_run_at.isoformat()

        disabled = self.disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if next_run_at is not UNSET:
            field_dict["nextRunAt"] = next_run_at
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        job_id = d.pop("jobId", UNSET)

        _next_run_at = d.pop("nextRunAt", UNSET)
        next_run_at: Union[Unset, datetime.datetime]
        if isinstance(_next_run_at, Unset):
            next_run_at = UNSET
        else:
            next_run_at = isoparse(_next_run_at)

        disabled = d.pop("disabled", UNSET)

        resume_od_schedule_response_200_data = cls(
            message=message,
            job_id=job_id,
            next_run_at=next_run_at,
            disabled=disabled,
        )

        resume_od_schedule_response_200_data.additional_properties = d
        return resume_od_schedule_response_200_data

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
