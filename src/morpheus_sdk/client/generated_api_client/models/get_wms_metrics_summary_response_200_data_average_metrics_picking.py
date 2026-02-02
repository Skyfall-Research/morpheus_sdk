from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSMetricsSummaryResponse200DataAverageMetricsPicking")


@_attrs_define
class GetWMSMetricsSummaryResponse200DataAverageMetricsPicking:
    """
    Attributes:
        avg_orders_shipped (Union[Unset, float]):  Example: 118.3.
        avg_lines_picked (Union[Unset, float]):  Example: 845.6.
        avg_lines_per_hour (Union[Unset, float]):  Example: 18.9.
        avg_pick_accuracy (Union[Unset, float]):  Example: 99.1.
    """

    avg_orders_shipped: Union[Unset, float] = UNSET
    avg_lines_picked: Union[Unset, float] = UNSET
    avg_lines_per_hour: Union[Unset, float] = UNSET
    avg_pick_accuracy: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_orders_shipped = self.avg_orders_shipped

        avg_lines_picked = self.avg_lines_picked

        avg_lines_per_hour = self.avg_lines_per_hour

        avg_pick_accuracy = self.avg_pick_accuracy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_orders_shipped is not UNSET:
            field_dict["avgOrdersShipped"] = avg_orders_shipped
        if avg_lines_picked is not UNSET:
            field_dict["avgLinesPicked"] = avg_lines_picked
        if avg_lines_per_hour is not UNSET:
            field_dict["avgLinesPerHour"] = avg_lines_per_hour
        if avg_pick_accuracy is not UNSET:
            field_dict["avgPickAccuracy"] = avg_pick_accuracy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_orders_shipped = d.pop("avgOrdersShipped", UNSET)

        avg_lines_picked = d.pop("avgLinesPicked", UNSET)

        avg_lines_per_hour = d.pop("avgLinesPerHour", UNSET)

        avg_pick_accuracy = d.pop("avgPickAccuracy", UNSET)

        get_wms_metrics_summary_response_200_data_average_metrics_picking = cls(
            avg_orders_shipped=avg_orders_shipped,
            avg_lines_picked=avg_lines_picked,
            avg_lines_per_hour=avg_lines_per_hour,
            avg_pick_accuracy=avg_pick_accuracy,
        )

        get_wms_metrics_summary_response_200_data_average_metrics_picking.additional_properties = d
        return get_wms_metrics_summary_response_200_data_average_metrics_picking

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
