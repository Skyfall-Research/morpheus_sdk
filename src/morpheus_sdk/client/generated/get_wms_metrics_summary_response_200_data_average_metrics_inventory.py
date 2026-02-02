from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSMetricsSummaryResponse200DataAverageMetricsInventory")


@_attrs_define
class GetWMSMetricsSummaryResponse200DataAverageMetricsInventory:
    """
    Attributes:
        avg_accuracy (Union[Unset, float]):  Example: 99.6.
        avg_turnover (Union[Unset, float]):  Example: 8.2.
    """

    avg_accuracy: Union[Unset, float] = UNSET
    avg_turnover: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_accuracy = self.avg_accuracy

        avg_turnover = self.avg_turnover

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_accuracy is not UNSET:
            field_dict["avgAccuracy"] = avg_accuracy
        if avg_turnover is not UNSET:
            field_dict["avgTurnover"] = avg_turnover

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_accuracy = d.pop("avgAccuracy", UNSET)

        avg_turnover = d.pop("avgTurnover", UNSET)

        get_wms_metrics_summary_response_200_data_average_metrics_inventory = cls(
            avg_accuracy=avg_accuracy,
            avg_turnover=avg_turnover,
        )

        get_wms_metrics_summary_response_200_data_average_metrics_inventory.additional_properties = d
        return get_wms_metrics_summary_response_200_data_average_metrics_inventory

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
