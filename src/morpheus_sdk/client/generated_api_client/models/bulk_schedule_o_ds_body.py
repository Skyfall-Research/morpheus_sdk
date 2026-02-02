from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_schedule_o_ds_body_schedules_item import BulkScheduleODsBodySchedulesItem


T = TypeVar("T", bound="BulkScheduleODsBody")


@_attrs_define
class BulkScheduleODsBody:
    """
    Attributes:
        schedules (list['BulkScheduleODsBodySchedulesItem']):
    """

    schedules: list["BulkScheduleODsBodySchedulesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedules = []
        for schedules_item_data in self.schedules:
            schedules_item = schedules_item_data.to_dict()
            schedules.append(schedules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedules": schedules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_schedule_o_ds_body_schedules_item import BulkScheduleODsBodySchedulesItem

        d = dict(src_dict)
        schedules = []
        _schedules = d.pop("schedules")
        for schedules_item_data in _schedules:
            schedules_item = BulkScheduleODsBodySchedulesItem.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        bulk_schedule_o_ds_body = cls(
            schedules=schedules,
        )

        bulk_schedule_o_ds_body.additional_properties = d
        return bulk_schedule_o_ds_body

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
