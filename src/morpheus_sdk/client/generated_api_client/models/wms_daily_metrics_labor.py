from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDailyMetricsLabor")


@_attrs_define
class WMSDailyMetricsLabor:
    """Labor and workforce metrics

    Attributes:
        total_workers (Union[Unset, float]): Total workers on shift Example: 24.
        total_hours (Union[Unset, float]): Total labor hours worked Example: 192.
        productive_hours (Union[Unset, float]): Direct productive labor hours Example: 165.5.
        indirect_hours (Union[Unset, float]): Indirect labor hours (breaks, meetings, training) Example: 26.5.
        utilization_percent (Union[Unset, float]): Labor utilization percentage Example: 86.2.
    """

    total_workers: Union[Unset, float] = UNSET
    total_hours: Union[Unset, float] = UNSET
    productive_hours: Union[Unset, float] = UNSET
    indirect_hours: Union[Unset, float] = UNSET
    utilization_percent: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_workers = self.total_workers

        total_hours = self.total_hours

        productive_hours = self.productive_hours

        indirect_hours = self.indirect_hours

        utilization_percent = self.utilization_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_workers is not UNSET:
            field_dict["totalWorkers"] = total_workers
        if total_hours is not UNSET:
            field_dict["totalHours"] = total_hours
        if productive_hours is not UNSET:
            field_dict["productiveHours"] = productive_hours
        if indirect_hours is not UNSET:
            field_dict["indirectHours"] = indirect_hours
        if utilization_percent is not UNSET:
            field_dict["utilizationPercent"] = utilization_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_workers = d.pop("totalWorkers", UNSET)

        total_hours = d.pop("totalHours", UNSET)

        productive_hours = d.pop("productiveHours", UNSET)

        indirect_hours = d.pop("indirectHours", UNSET)

        utilization_percent = d.pop("utilizationPercent", UNSET)

        wms_daily_metrics_labor = cls(
            total_workers=total_workers,
            total_hours=total_hours,
            productive_hours=productive_hours,
            indirect_hours=indirect_hours,
            utilization_percent=utilization_percent,
        )

        wms_daily_metrics_labor.additional_properties = d
        return wms_daily_metrics_labor

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
