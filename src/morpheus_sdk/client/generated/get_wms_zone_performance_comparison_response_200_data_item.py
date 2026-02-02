from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_zone_performance_comparison_response_200_data_item_metrics import (
        GetWMSZonePerformanceComparisonResponse200DataItemMetrics,
    )


T = TypeVar("T", bound="GetWMSZonePerformanceComparisonResponse200DataItem")


@_attrs_define
class GetWMSZonePerformanceComparisonResponse200DataItem:
    """
    Attributes:
        zone_id (Union[Unset, str]): Zone identifier Example: ZONE_PICK_A.
        metrics (Union[Unset, GetWMSZonePerformanceComparisonResponse200DataItemMetrics]): Performance metrics for the
            zone
    """

    zone_id: Union[Unset, str] = UNSET
    metrics: Union[Unset, "GetWMSZonePerformanceComparisonResponse200DataItemMetrics"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_id = self.zone_id

        metrics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_zone_performance_comparison_response_200_data_item_metrics import (
            GetWMSZonePerformanceComparisonResponse200DataItemMetrics,
        )

        d = dict(src_dict)
        zone_id = d.pop("zoneId", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: Union[Unset, GetWMSZonePerformanceComparisonResponse200DataItemMetrics]
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = GetWMSZonePerformanceComparisonResponse200DataItemMetrics.from_dict(_metrics)

        get_wms_zone_performance_comparison_response_200_data_item = cls(
            zone_id=zone_id,
            metrics=metrics,
        )

        get_wms_zone_performance_comparison_response_200_data_item.additional_properties = d
        return get_wms_zone_performance_comparison_response_200_data_item

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
