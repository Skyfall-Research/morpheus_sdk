import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_od_body_schedule_type import CreateODBodyScheduleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateODBodySchedule")


@_attrs_define
class CreateODBodySchedule:
    """Optional scheduling configuration

    Attributes:
        type_ (Union[Unset, CreateODBodyScheduleType]):
        time (Union[Unset, datetime.datetime]): For 'once' type: Execution time
        interval (Union[Unset, str]): For 'recurring' type: Interval string (e.g., '1 day', '30 minutes')
    """

    type_: Union[Unset, CreateODBodyScheduleType] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    interval: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        interval = self.interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if time is not UNSET:
            field_dict["time"] = time
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CreateODBodyScheduleType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateODBodyScheduleType(_type_)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        interval = d.pop("interval", UNSET)

        create_od_body_schedule = cls(
            type_=type_,
            time=time,
            interval=interval,
        )

        create_od_body_schedule.additional_properties = d
        return create_od_body_schedule

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
