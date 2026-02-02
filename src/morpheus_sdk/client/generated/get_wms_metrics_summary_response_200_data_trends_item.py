from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSMetricsSummaryResponse200DataTrendsItem")


@_attrs_define
class GetWMSMetricsSummaryResponse200DataTrendsItem:
    """
    Attributes:
        date (Union[Unset, str]):  Example: 2024-11-27.
        units_received (Union[Unset, float]):  Example: 2450.
        units_shipped (Union[Unset, float]):  Example: 2240.
        pick_accuracy (Union[Unset, float]):  Example: 99.2.
    """

    date: Union[Unset, str] = UNSET
    units_received: Union[Unset, float] = UNSET
    units_shipped: Union[Unset, float] = UNSET
    pick_accuracy: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        units_received = self.units_received

        units_shipped = self.units_shipped

        pick_accuracy = self.pick_accuracy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if units_received is not UNSET:
            field_dict["unitsReceived"] = units_received
        if units_shipped is not UNSET:
            field_dict["unitsShipped"] = units_shipped
        if pick_accuracy is not UNSET:
            field_dict["pickAccuracy"] = pick_accuracy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        units_received = d.pop("unitsReceived", UNSET)

        units_shipped = d.pop("unitsShipped", UNSET)

        pick_accuracy = d.pop("pickAccuracy", UNSET)

        get_wms_metrics_summary_response_200_data_trends_item = cls(
            date=date,
            units_received=units_received,
            units_shipped=units_shipped,
            pick_accuracy=pick_accuracy,
        )

        get_wms_metrics_summary_response_200_data_trends_item.additional_properties = d
        return get_wms_metrics_summary_response_200_data_trends_item

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
