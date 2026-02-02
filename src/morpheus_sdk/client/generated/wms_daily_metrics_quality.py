from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDailyMetricsQuality")


@_attrs_define
class WMSDailyMetricsQuality:
    """Quality and error tracking metrics

    Attributes:
        pick_errors (Union[Unset, float]): Number of pick errors recorded Example: 7.
        pack_errors (Union[Unset, float]): Number of pack errors recorded Example: 3.
        damage_reports (Union[Unset, float]): Number of damage reports filed Example: 2.
        returns_processed (Union[Unset, float]): Number of returns processed Example: 15.
    """

    pick_errors: Union[Unset, float] = UNSET
    pack_errors: Union[Unset, float] = UNSET
    damage_reports: Union[Unset, float] = UNSET
    returns_processed: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pick_errors = self.pick_errors

        pack_errors = self.pack_errors

        damage_reports = self.damage_reports

        returns_processed = self.returns_processed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pick_errors is not UNSET:
            field_dict["pickErrors"] = pick_errors
        if pack_errors is not UNSET:
            field_dict["packErrors"] = pack_errors
        if damage_reports is not UNSET:
            field_dict["damageReports"] = damage_reports
        if returns_processed is not UNSET:
            field_dict["returnsProcessed"] = returns_processed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pick_errors = d.pop("pickErrors", UNSET)

        pack_errors = d.pop("packErrors", UNSET)

        damage_reports = d.pop("damageReports", UNSET)

        returns_processed = d.pop("returnsProcessed", UNSET)

        wms_daily_metrics_quality = cls(
            pick_errors=pick_errors,
            pack_errors=pack_errors,
            damage_reports=damage_reports,
            returns_processed=returns_processed,
        )

        wms_daily_metrics_quality.additional_properties = d
        return wms_daily_metrics_quality

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
