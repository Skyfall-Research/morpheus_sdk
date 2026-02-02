from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSCycleCountVarianceReportResponse200DataTrendsMonthlyAccuracyItem")


@_attrs_define
class GetWMSCycleCountVarianceReportResponse200DataTrendsMonthlyAccuracyItem:
    """
    Attributes:
        month (Union[Unset, str]):  Example: 2024-01.
        accuracy_percent (Union[Unset, float]):  Example: 94.8.
        total_variance_value (Union[Unset, float]):  Example: 445.67.
    """

    month: Union[Unset, str] = UNSET
    accuracy_percent: Union[Unset, float] = UNSET
    total_variance_value: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        accuracy_percent = self.accuracy_percent

        total_variance_value = self.total_variance_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if month is not UNSET:
            field_dict["month"] = month
        if accuracy_percent is not UNSET:
            field_dict["accuracyPercent"] = accuracy_percent
        if total_variance_value is not UNSET:
            field_dict["totalVarianceValue"] = total_variance_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month", UNSET)

        accuracy_percent = d.pop("accuracyPercent", UNSET)

        total_variance_value = d.pop("totalVarianceValue", UNSET)

        get_wms_cycle_count_variance_report_response_200_data_trends_monthly_accuracy_item = cls(
            month=month,
            accuracy_percent=accuracy_percent,
            total_variance_value=total_variance_value,
        )

        get_wms_cycle_count_variance_report_response_200_data_trends_monthly_accuracy_item.additional_properties = d
        return get_wms_cycle_count_variance_report_response_200_data_trends_monthly_accuracy_item

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
