from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WMSDailyMetricsCustomFields")


@_attrs_define
class WMSDailyMetricsCustomFields:
    """Additional warehouse-specific metrics and operational data

    Example:
        {'temperatureControlledZones': 4, 'hazMatHandling': True, 'specialEquipmentUsage': 12.5,
            'sustainabilityMetrics': {'energyUsageKwh': 2450.5, 'wasteReductionPercent': 15.2}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wms_daily_metrics_custom_fields = cls()

        wms_daily_metrics_custom_fields.additional_properties = d
        return wms_daily_metrics_custom_fields

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
