from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSMetricsSummaryResponse200DataAverageMetricsPacking")


@_attrs_define
class GetWMSMetricsSummaryResponse200DataAverageMetricsPacking:
    """
    Attributes:
        avg_orders_packed (Union[Unset, float]):  Example: 115.2.
        avg_packing_hours (Union[Unset, float]):  Example: 23.1.
        avg_orders_per_hour (Union[Unset, float]):  Example: 4.98.
    """

    avg_orders_packed: Union[Unset, float] = UNSET
    avg_packing_hours: Union[Unset, float] = UNSET
    avg_orders_per_hour: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_orders_packed = self.avg_orders_packed

        avg_packing_hours = self.avg_packing_hours

        avg_orders_per_hour = self.avg_orders_per_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_orders_packed is not UNSET:
            field_dict["avgOrdersPacked"] = avg_orders_packed
        if avg_packing_hours is not UNSET:
            field_dict["avgPackingHours"] = avg_packing_hours
        if avg_orders_per_hour is not UNSET:
            field_dict["avgOrdersPerHour"] = avg_orders_per_hour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_orders_packed = d.pop("avgOrdersPacked", UNSET)

        avg_packing_hours = d.pop("avgPackingHours", UNSET)

        avg_orders_per_hour = d.pop("avgOrdersPerHour", UNSET)

        get_wms_metrics_summary_response_200_data_average_metrics_packing = cls(
            avg_orders_packed=avg_orders_packed,
            avg_packing_hours=avg_packing_hours,
            avg_orders_per_hour=avg_orders_per_hour,
        )

        get_wms_metrics_summary_response_200_data_average_metrics_packing.additional_properties = d
        return get_wms_metrics_summary_response_200_data_average_metrics_packing

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
