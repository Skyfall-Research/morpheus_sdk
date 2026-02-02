from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_performance_trends_response_200_data_item_metrics import (
        GetWMSPerformanceTrendsResponse200DataItemMetrics,
    )


T = TypeVar("T", bound="GetWMSPerformanceTrendsResponse200DataItem")


@_attrs_define
class GetWMSPerformanceTrendsResponse200DataItem:
    """
    Attributes:
        date (Union[Unset, str]): Date for metrics Example: 2024-11-27.
        metrics (Union[Unset, GetWMSPerformanceTrendsResponse200DataItemMetrics]): Complete metrics object for the
            specified category Example: {'ordersShipped': 125, 'linesPicked': 890, 'unitsPicked': 2240, 'pickingHours':
            45.5, 'linesPerHour': 19.6, 'unitsPerHour': 49.2, 'pickAccuracy': 99.2}.
    """

    date: Union[Unset, str] = UNSET
    metrics: Union[Unset, "GetWMSPerformanceTrendsResponse200DataItemMetrics"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        metrics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_performance_trends_response_200_data_item_metrics import (
            GetWMSPerformanceTrendsResponse200DataItemMetrics,
        )

        d = dict(src_dict)
        date = d.pop("date", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: Union[Unset, GetWMSPerformanceTrendsResponse200DataItemMetrics]
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = GetWMSPerformanceTrendsResponse200DataItemMetrics.from_dict(_metrics)

        get_wms_performance_trends_response_200_data_item = cls(
            date=date,
            metrics=metrics,
        )

        get_wms_performance_trends_response_200_data_item.additional_properties = d
        return get_wms_performance_trends_response_200_data_item

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
