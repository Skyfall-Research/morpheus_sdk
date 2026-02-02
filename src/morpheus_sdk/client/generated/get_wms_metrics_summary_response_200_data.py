from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_metrics_summary_response_200_data_average_metrics import (
        GetWMSMetricsSummaryResponse200DataAverageMetrics,
    )
    from ..models.get_wms_metrics_summary_response_200_data_trends_item import (
        GetWMSMetricsSummaryResponse200DataTrendsItem,
    )


T = TypeVar("T", bound="GetWMSMetricsSummaryResponse200Data")


@_attrs_define
class GetWMSMetricsSummaryResponse200Data:
    """
    Attributes:
        total_days (Union[Unset, float]): Total days included in summary Example: 27.
        average_metrics (Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetrics]): Average metrics across all
            categories
        trends (Union[Unset, list['GetWMSMetricsSummaryResponse200DataTrendsItem']]): Daily trend data with key
            performance indicators
    """

    total_days: Union[Unset, float] = UNSET
    average_metrics: Union[Unset, "GetWMSMetricsSummaryResponse200DataAverageMetrics"] = UNSET
    trends: Union[Unset, list["GetWMSMetricsSummaryResponse200DataTrendsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_days = self.total_days

        average_metrics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.average_metrics, Unset):
            average_metrics = self.average_metrics.to_dict()

        trends: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.trends, Unset):
            trends = []
            for trends_item_data in self.trends:
                trends_item = trends_item_data.to_dict()
                trends.append(trends_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_days is not UNSET:
            field_dict["totalDays"] = total_days
        if average_metrics is not UNSET:
            field_dict["averageMetrics"] = average_metrics
        if trends is not UNSET:
            field_dict["trends"] = trends

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_metrics_summary_response_200_data_average_metrics import (
            GetWMSMetricsSummaryResponse200DataAverageMetrics,
        )
        from ..models.get_wms_metrics_summary_response_200_data_trends_item import (
            GetWMSMetricsSummaryResponse200DataTrendsItem,
        )

        d = dict(src_dict)
        total_days = d.pop("totalDays", UNSET)

        _average_metrics = d.pop("averageMetrics", UNSET)
        average_metrics: Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetrics]
        if isinstance(_average_metrics, Unset):
            average_metrics = UNSET
        else:
            average_metrics = GetWMSMetricsSummaryResponse200DataAverageMetrics.from_dict(_average_metrics)

        trends = []
        _trends = d.pop("trends", UNSET)
        for trends_item_data in _trends or []:
            trends_item = GetWMSMetricsSummaryResponse200DataTrendsItem.from_dict(trends_item_data)

            trends.append(trends_item)

        get_wms_metrics_summary_response_200_data = cls(
            total_days=total_days,
            average_metrics=average_metrics,
            trends=trends,
        )

        get_wms_metrics_summary_response_200_data.additional_properties = d
        return get_wms_metrics_summary_response_200_data

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
