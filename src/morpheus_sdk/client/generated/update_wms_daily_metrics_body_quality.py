from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWMSDailyMetricsBodyQuality")


@_attrs_define
class UpdateWMSDailyMetricsBodyQuality:
    """Updated quality metrics

    Attributes:
        pick_errors (Union[Unset, float]):  Example: 5.
        damage_reports (Union[Unset, float]):  Example: 1.
    """

    pick_errors: Union[Unset, float] = UNSET
    damage_reports: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pick_errors = self.pick_errors

        damage_reports = self.damage_reports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pick_errors is not UNSET:
            field_dict["pickErrors"] = pick_errors
        if damage_reports is not UNSET:
            field_dict["damageReports"] = damage_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pick_errors = d.pop("pickErrors", UNSET)

        damage_reports = d.pop("damageReports", UNSET)

        update_wms_daily_metrics_body_quality = cls(
            pick_errors=pick_errors,
            damage_reports=damage_reports,
        )

        update_wms_daily_metrics_body_quality.additional_properties = d
        return update_wms_daily_metrics_body_quality

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
