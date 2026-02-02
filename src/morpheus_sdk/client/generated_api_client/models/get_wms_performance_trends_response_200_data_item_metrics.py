from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetWMSPerformanceTrendsResponse200DataItemMetrics")


@_attrs_define
class GetWMSPerformanceTrendsResponse200DataItemMetrics:
    """Complete metrics object for the specified category

    Example:
        {'ordersShipped': 125, 'linesPicked': 890, 'unitsPicked': 2240, 'pickingHours': 45.5, 'linesPerHour': 19.6,
            'unitsPerHour': 49.2, 'pickAccuracy': 99.2}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        get_wms_performance_trends_response_200_data_item_metrics = cls()

        get_wms_performance_trends_response_200_data_item_metrics.additional_properties = d
        return get_wms_performance_trends_response_200_data_item_metrics

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
