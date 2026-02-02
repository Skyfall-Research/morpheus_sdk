import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.schedule_od_body_type import ScheduleODBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_od_body_metadata import ScheduleODBodyMetadata


T = TypeVar("T", bound="ScheduleODBody")


@_attrs_define
class ScheduleODBody:
    """
    Attributes:
        type_ (ScheduleODBodyType): Type of schedule
        time (Union[Unset, datetime.datetime]): Required for 'once' type. ISO 8601 date string.
        interval (Union[Unset, str]): Required for 'recurring' type. Human-readable interval (e.g., '1 day').
        metadata (Union[Unset, ScheduleODBodyMetadata]): Additional metadata to attach to the job
    """

    type_: ScheduleODBodyType
    time: Union[Unset, datetime.datetime] = UNSET
    interval: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ScheduleODBodyMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        interval = self.interval

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if time is not UNSET:
            field_dict["time"] = time
        if interval is not UNSET:
            field_dict["interval"] = interval
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_od_body_metadata import ScheduleODBodyMetadata

        d = dict(src_dict)
        type_ = ScheduleODBodyType(d.pop("type"))

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        interval = d.pop("interval", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ScheduleODBodyMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ScheduleODBodyMetadata.from_dict(_metadata)

        schedule_od_body = cls(
            type_=type_,
            time=time,
            interval=interval,
            metadata=metadata,
        )

        schedule_od_body.additional_properties = d
        return schedule_od_body

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
