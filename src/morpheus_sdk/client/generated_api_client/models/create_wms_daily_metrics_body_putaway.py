from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSDailyMetricsBodyPutaway")


@_attrs_define
class CreateWMSDailyMetricsBodyPutaway:
    """Putaway operation metrics

    Attributes:
        putaway_tasks (Union[Unset, float]): Number of putaway tasks completed Example: 28.
        pallets_putaway (Union[Unset, float]): Number of pallets put away Example: 26.
        putaway_hours (Union[Unset, float]): Total putaway hours Example: 18.5.
        pallets_per_hour (Union[Unset, float]): Pallets put away per hour Example: 1.4.
    """

    putaway_tasks: Union[Unset, float] = UNSET
    pallets_putaway: Union[Unset, float] = UNSET
    putaway_hours: Union[Unset, float] = UNSET
    pallets_per_hour: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        putaway_tasks = self.putaway_tasks

        pallets_putaway = self.pallets_putaway

        putaway_hours = self.putaway_hours

        pallets_per_hour = self.pallets_per_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if putaway_tasks is not UNSET:
            field_dict["putawayTasks"] = putaway_tasks
        if pallets_putaway is not UNSET:
            field_dict["palletsPutaway"] = pallets_putaway
        if putaway_hours is not UNSET:
            field_dict["putawayHours"] = putaway_hours
        if pallets_per_hour is not UNSET:
            field_dict["palletsPerHour"] = pallets_per_hour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        putaway_tasks = d.pop("putawayTasks", UNSET)

        pallets_putaway = d.pop("palletsPutaway", UNSET)

        putaway_hours = d.pop("putawayHours", UNSET)

        pallets_per_hour = d.pop("palletsPerHour", UNSET)

        create_wms_daily_metrics_body_putaway = cls(
            putaway_tasks=putaway_tasks,
            pallets_putaway=pallets_putaway,
            putaway_hours=putaway_hours,
            pallets_per_hour=pallets_per_hour,
        )

        create_wms_daily_metrics_body_putaway.additional_properties = d
        return create_wms_daily_metrics_body_putaway

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
