from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_cycle_count_variance_report_response_200_data_trends_monthly_accuracy_item import (
        GetWMSCycleCountVarianceReportResponse200DataTrendsMonthlyAccuracyItem,
    )


T = TypeVar("T", bound="GetWMSCycleCountVarianceReportResponse200DataTrends")


@_attrs_define
class GetWMSCycleCountVarianceReportResponse200DataTrends:
    """
    Attributes:
        monthly_accuracy (Union[Unset, list['GetWMSCycleCountVarianceReportResponse200DataTrendsMonthlyAccuracyItem']]):
    """

    monthly_accuracy: Union[Unset, list["GetWMSCycleCountVarianceReportResponse200DataTrendsMonthlyAccuracyItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_accuracy: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.monthly_accuracy, Unset):
            monthly_accuracy = []
            for monthly_accuracy_item_data in self.monthly_accuracy:
                monthly_accuracy_item = monthly_accuracy_item_data.to_dict()
                monthly_accuracy.append(monthly_accuracy_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monthly_accuracy is not UNSET:
            field_dict["monthlyAccuracy"] = monthly_accuracy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_cycle_count_variance_report_response_200_data_trends_monthly_accuracy_item import (
            GetWMSCycleCountVarianceReportResponse200DataTrendsMonthlyAccuracyItem,
        )

        d = dict(src_dict)
        monthly_accuracy = []
        _monthly_accuracy = d.pop("monthlyAccuracy", UNSET)
        for monthly_accuracy_item_data in _monthly_accuracy or []:
            monthly_accuracy_item = GetWMSCycleCountVarianceReportResponse200DataTrendsMonthlyAccuracyItem.from_dict(
                monthly_accuracy_item_data
            )

            monthly_accuracy.append(monthly_accuracy_item)

        get_wms_cycle_count_variance_report_response_200_data_trends = cls(
            monthly_accuracy=monthly_accuracy,
        )

        get_wms_cycle_count_variance_report_response_200_data_trends.additional_properties = d
        return get_wms_cycle_count_variance_report_response_200_data_trends

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
