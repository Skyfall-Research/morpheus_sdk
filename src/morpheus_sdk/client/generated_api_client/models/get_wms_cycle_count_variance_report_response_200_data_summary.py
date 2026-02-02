from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSCycleCountVarianceReportResponse200DataSummary")


@_attrs_define
class GetWMSCycleCountVarianceReportResponse200DataSummary:
    """
    Attributes:
        total_counts (Union[Unset, int]):  Example: 45.
        total_variances (Union[Unset, int]):  Example: 128.
        accuracy_percent (Union[Unset, float]):  Example: 94.2.
        total_variance_value (Union[Unset, float]):  Example: 1247.85.
        avg_variance_percent (Union[Unset, float]):  Example: 2.3.
    """

    total_counts: Union[Unset, int] = UNSET
    total_variances: Union[Unset, int] = UNSET
    accuracy_percent: Union[Unset, float] = UNSET
    total_variance_value: Union[Unset, float] = UNSET
    avg_variance_percent: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_counts = self.total_counts

        total_variances = self.total_variances

        accuracy_percent = self.accuracy_percent

        total_variance_value = self.total_variance_value

        avg_variance_percent = self.avg_variance_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_counts is not UNSET:
            field_dict["totalCounts"] = total_counts
        if total_variances is not UNSET:
            field_dict["totalVariances"] = total_variances
        if accuracy_percent is not UNSET:
            field_dict["accuracyPercent"] = accuracy_percent
        if total_variance_value is not UNSET:
            field_dict["totalVarianceValue"] = total_variance_value
        if avg_variance_percent is not UNSET:
            field_dict["avgVariancePercent"] = avg_variance_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_counts = d.pop("totalCounts", UNSET)

        total_variances = d.pop("totalVariances", UNSET)

        accuracy_percent = d.pop("accuracyPercent", UNSET)

        total_variance_value = d.pop("totalVarianceValue", UNSET)

        avg_variance_percent = d.pop("avgVariancePercent", UNSET)

        get_wms_cycle_count_variance_report_response_200_data_summary = cls(
            total_counts=total_counts,
            total_variances=total_variances,
            accuracy_percent=accuracy_percent,
            total_variance_value=total_variance_value,
            avg_variance_percent=avg_variance_percent,
        )

        get_wms_cycle_count_variance_report_response_200_data_summary.additional_properties = d
        return get_wms_cycle_count_variance_report_response_200_data_summary

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
