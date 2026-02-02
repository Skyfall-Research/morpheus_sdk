from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSCycleCountVarianceReportResponse200DataVariancesByTypeItem")


@_attrs_define
class GetWMSCycleCountVarianceReportResponse200DataVariancesByTypeItem:
    """
    Attributes:
        count_type (Union[Unset, str]):  Example: ABC.
        total_counts (Union[Unset, int]):  Example: 15.
        variance_count (Union[Unset, int]):  Example: 28.
        accuracy_percent (Union[Unset, float]):  Example: 96.5.
        avg_variance_value (Union[Unset, float]):  Example: 25.67.
    """

    count_type: Union[Unset, str] = UNSET
    total_counts: Union[Unset, int] = UNSET
    variance_count: Union[Unset, int] = UNSET
    accuracy_percent: Union[Unset, float] = UNSET
    avg_variance_value: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count_type = self.count_type

        total_counts = self.total_counts

        variance_count = self.variance_count

        accuracy_percent = self.accuracy_percent

        avg_variance_value = self.avg_variance_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count_type is not UNSET:
            field_dict["countType"] = count_type
        if total_counts is not UNSET:
            field_dict["totalCounts"] = total_counts
        if variance_count is not UNSET:
            field_dict["varianceCount"] = variance_count
        if accuracy_percent is not UNSET:
            field_dict["accuracyPercent"] = accuracy_percent
        if avg_variance_value is not UNSET:
            field_dict["avgVarianceValue"] = avg_variance_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count_type = d.pop("countType", UNSET)

        total_counts = d.pop("totalCounts", UNSET)

        variance_count = d.pop("varianceCount", UNSET)

        accuracy_percent = d.pop("accuracyPercent", UNSET)

        avg_variance_value = d.pop("avgVarianceValue", UNSET)

        get_wms_cycle_count_variance_report_response_200_data_variances_by_type_item = cls(
            count_type=count_type,
            total_counts=total_counts,
            variance_count=variance_count,
            accuracy_percent=accuracy_percent,
            avg_variance_value=avg_variance_value,
        )

        get_wms_cycle_count_variance_report_response_200_data_variances_by_type_item.additional_properties = d
        return get_wms_cycle_count_variance_report_response_200_data_variances_by_type_item

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
