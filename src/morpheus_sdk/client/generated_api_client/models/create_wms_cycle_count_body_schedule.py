import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSCycleCountBodySchedule")


@_attrs_define
class CreateWMSCycleCountBodySchedule:
    """
    Attributes:
        scheduled_date (datetime.datetime): Date and time when count is scheduled to begin Example:
            2024-01-25T08:00:00.000Z.
        start_date (Union[Unset, datetime.datetime]): Actual start date/time when count begins Example:
            2024-01-25T08:15:00.000Z.
        completed_date (Union[Unset, datetime.datetime]): Date/time when count was completed Example:
            2024-01-25T16:30:00.000Z.
    """

    scheduled_date: datetime.datetime
    start_date: Union[Unset, datetime.datetime] = UNSET
    completed_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheduled_date = self.scheduled_date.isoformat()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        completed_date: Union[Unset, str] = UNSET
        if not isinstance(self.completed_date, Unset):
            completed_date = self.completed_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduledDate": scheduled_date,
            }
        )
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheduled_date = isoparse(d.pop("scheduledDate"))

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _completed_date = d.pop("completedDate", UNSET)
        completed_date: Union[Unset, datetime.datetime]
        if isinstance(_completed_date, Unset):
            completed_date = UNSET
        else:
            completed_date = isoparse(_completed_date)

        create_wms_cycle_count_body_schedule = cls(
            scheduled_date=scheduled_date,
            start_date=start_date,
            completed_date=completed_date,
        )

        create_wms_cycle_count_body_schedule.additional_properties = d
        return create_wms_cycle_count_body_schedule

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
