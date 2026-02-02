from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSZonePerformanceComparisonResponse200DataItemMetrics")


@_attrs_define
class GetWMSZonePerformanceComparisonResponse200DataItemMetrics:
    """Performance metrics for the zone

    Attributes:
        total_orders (Union[Unset, float]): Total orders processed Example: 2850.
        total_lines (Union[Unset, float]): Total lines picked Example: 19420.
        average_pick_time (Union[Unset, float]): Average hours per line picked Example: 0.0234.
        accuracy (Union[Unset, float]): Average pick accuracy percentage Example: 99.3.
    """

    total_orders: Union[Unset, float] = UNSET
    total_lines: Union[Unset, float] = UNSET
    average_pick_time: Union[Unset, float] = UNSET
    accuracy: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_orders = self.total_orders

        total_lines = self.total_lines

        average_pick_time = self.average_pick_time

        accuracy = self.accuracy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_orders is not UNSET:
            field_dict["totalOrders"] = total_orders
        if total_lines is not UNSET:
            field_dict["totalLines"] = total_lines
        if average_pick_time is not UNSET:
            field_dict["averagePickTime"] = average_pick_time
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_orders = d.pop("totalOrders", UNSET)

        total_lines = d.pop("totalLines", UNSET)

        average_pick_time = d.pop("averagePickTime", UNSET)

        accuracy = d.pop("accuracy", UNSET)

        get_wms_zone_performance_comparison_response_200_data_item_metrics = cls(
            total_orders=total_orders,
            total_lines=total_lines,
            average_pick_time=average_pick_time,
            accuracy=accuracy,
        )

        get_wms_zone_performance_comparison_response_200_data_item_metrics.additional_properties = d
        return get_wms_zone_performance_comparison_response_200_data_item_metrics

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
