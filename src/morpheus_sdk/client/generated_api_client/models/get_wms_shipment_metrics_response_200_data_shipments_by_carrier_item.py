from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSShipmentMetricsResponse200DataShipmentsByCarrierItem")


@_attrs_define
class GetWMSShipmentMetricsResponse200DataShipmentsByCarrierItem:
    """
    Attributes:
        carrier (Union[Unset, str]):  Example: UPS.
        count (Union[Unset, float]):  Example: 450.
        on_time_rate (Union[Unset, float]):  Example: 96.1.
        avg_transit_time (Union[Unset, float]):  Example: 2.1.
    """

    carrier: Union[Unset, str] = UNSET
    count: Union[Unset, float] = UNSET
    on_time_rate: Union[Unset, float] = UNSET
    avg_transit_time: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier = self.carrier

        count = self.count

        on_time_rate = self.on_time_rate

        avg_transit_time = self.avg_transit_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if count is not UNSET:
            field_dict["count"] = count
        if on_time_rate is not UNSET:
            field_dict["onTimeRate"] = on_time_rate
        if avg_transit_time is not UNSET:
            field_dict["avgTransitTime"] = avg_transit_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        carrier = d.pop("carrier", UNSET)

        count = d.pop("count", UNSET)

        on_time_rate = d.pop("onTimeRate", UNSET)

        avg_transit_time = d.pop("avgTransitTime", UNSET)

        get_wms_shipment_metrics_response_200_data_shipments_by_carrier_item = cls(
            carrier=carrier,
            count=count,
            on_time_rate=on_time_rate,
            avg_transit_time=avg_transit_time,
        )

        get_wms_shipment_metrics_response_200_data_shipments_by_carrier_item.additional_properties = d
        return get_wms_shipment_metrics_response_200_data_shipments_by_carrier_item

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
