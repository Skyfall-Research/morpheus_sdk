from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSMetricsSummaryResponse200DataAverageMetricsInbound")


@_attrs_define
class GetWMSMetricsSummaryResponse200DataAverageMetricsInbound:
    """
    Attributes:
        avg_po_received (Union[Unset, float]):  Example: 42.5.
        avg_units_received (Union[Unset, float]):  Example: 2345.8.
        avg_units_per_hour (Union[Unset, float]):  Example: 74.2.
    """

    avg_po_received: Union[Unset, float] = UNSET
    avg_units_received: Union[Unset, float] = UNSET
    avg_units_per_hour: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_po_received = self.avg_po_received

        avg_units_received = self.avg_units_received

        avg_units_per_hour = self.avg_units_per_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_po_received is not UNSET:
            field_dict["avgPoReceived"] = avg_po_received
        if avg_units_received is not UNSET:
            field_dict["avgUnitsReceived"] = avg_units_received
        if avg_units_per_hour is not UNSET:
            field_dict["avgUnitsPerHour"] = avg_units_per_hour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_po_received = d.pop("avgPoReceived", UNSET)

        avg_units_received = d.pop("avgUnitsReceived", UNSET)

        avg_units_per_hour = d.pop("avgUnitsPerHour", UNSET)

        get_wms_metrics_summary_response_200_data_average_metrics_inbound = cls(
            avg_po_received=avg_po_received,
            avg_units_received=avg_units_received,
            avg_units_per_hour=avg_units_per_hour,
        )

        get_wms_metrics_summary_response_200_data_average_metrics_inbound.additional_properties = d
        return get_wms_metrics_summary_response_200_data_average_metrics_inbound

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
