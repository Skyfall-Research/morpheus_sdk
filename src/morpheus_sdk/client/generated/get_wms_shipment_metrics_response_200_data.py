from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_shipment_metrics_response_200_data_shipments_by_carrier_item import (
        GetWMSShipmentMetricsResponse200DataShipmentsByCarrierItem,
    )
    from ..models.get_wms_shipment_metrics_response_200_data_shipments_by_day_item import (
        GetWMSShipmentMetricsResponse200DataShipmentsByDayItem,
    )


T = TypeVar("T", bound="GetWMSShipmentMetricsResponse200Data")


@_attrs_define
class GetWMSShipmentMetricsResponse200Data:
    """
    Attributes:
        total_shipments (Union[Unset, float]): Total shipments in period Example: 850.
        shipped_shipments (Union[Unset, float]): Shipments in transit or delivered Example: 820.
        delivered_shipments (Union[Unset, float]): Successfully delivered shipments Example: 795.
        exception_shipments (Union[Unset, float]): Shipments with exceptions Example: 12.
        average_transit_time (Union[Unset, float]): Average days from ship to delivery Example: 2.3.
        on_time_delivery_rate (Union[Unset, float]): On-time delivery percentage Example: 94.2.
        shipments_by_carrier (Union[Unset, list['GetWMSShipmentMetricsResponse200DataShipmentsByCarrierItem']]): Carrier
            performance breakdown
        shipments_by_day (Union[Unset, list['GetWMSShipmentMetricsResponse200DataShipmentsByDayItem']]): Daily volume
            trends
    """

    total_shipments: Union[Unset, float] = UNSET
    shipped_shipments: Union[Unset, float] = UNSET
    delivered_shipments: Union[Unset, float] = UNSET
    exception_shipments: Union[Unset, float] = UNSET
    average_transit_time: Union[Unset, float] = UNSET
    on_time_delivery_rate: Union[Unset, float] = UNSET
    shipments_by_carrier: Union[Unset, list["GetWMSShipmentMetricsResponse200DataShipmentsByCarrierItem"]] = UNSET
    shipments_by_day: Union[Unset, list["GetWMSShipmentMetricsResponse200DataShipmentsByDayItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_shipments = self.total_shipments

        shipped_shipments = self.shipped_shipments

        delivered_shipments = self.delivered_shipments

        exception_shipments = self.exception_shipments

        average_transit_time = self.average_transit_time

        on_time_delivery_rate = self.on_time_delivery_rate

        shipments_by_carrier: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipments_by_carrier, Unset):
            shipments_by_carrier = []
            for shipments_by_carrier_item_data in self.shipments_by_carrier:
                shipments_by_carrier_item = shipments_by_carrier_item_data.to_dict()
                shipments_by_carrier.append(shipments_by_carrier_item)

        shipments_by_day: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipments_by_day, Unset):
            shipments_by_day = []
            for shipments_by_day_item_data in self.shipments_by_day:
                shipments_by_day_item = shipments_by_day_item_data.to_dict()
                shipments_by_day.append(shipments_by_day_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_shipments is not UNSET:
            field_dict["totalShipments"] = total_shipments
        if shipped_shipments is not UNSET:
            field_dict["shippedShipments"] = shipped_shipments
        if delivered_shipments is not UNSET:
            field_dict["deliveredShipments"] = delivered_shipments
        if exception_shipments is not UNSET:
            field_dict["exceptionShipments"] = exception_shipments
        if average_transit_time is not UNSET:
            field_dict["averageTransitTime"] = average_transit_time
        if on_time_delivery_rate is not UNSET:
            field_dict["onTimeDeliveryRate"] = on_time_delivery_rate
        if shipments_by_carrier is not UNSET:
            field_dict["shipmentsByCarrier"] = shipments_by_carrier
        if shipments_by_day is not UNSET:
            field_dict["shipmentsByDay"] = shipments_by_day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_shipment_metrics_response_200_data_shipments_by_carrier_item import (
            GetWMSShipmentMetricsResponse200DataShipmentsByCarrierItem,
        )
        from ..models.get_wms_shipment_metrics_response_200_data_shipments_by_day_item import (
            GetWMSShipmentMetricsResponse200DataShipmentsByDayItem,
        )

        d = dict(src_dict)
        total_shipments = d.pop("totalShipments", UNSET)

        shipped_shipments = d.pop("shippedShipments", UNSET)

        delivered_shipments = d.pop("deliveredShipments", UNSET)

        exception_shipments = d.pop("exceptionShipments", UNSET)

        average_transit_time = d.pop("averageTransitTime", UNSET)

        on_time_delivery_rate = d.pop("onTimeDeliveryRate", UNSET)

        shipments_by_carrier = []
        _shipments_by_carrier = d.pop("shipmentsByCarrier", UNSET)
        for shipments_by_carrier_item_data in _shipments_by_carrier or []:
            shipments_by_carrier_item = GetWMSShipmentMetricsResponse200DataShipmentsByCarrierItem.from_dict(
                shipments_by_carrier_item_data
            )

            shipments_by_carrier.append(shipments_by_carrier_item)

        shipments_by_day = []
        _shipments_by_day = d.pop("shipmentsByDay", UNSET)
        for shipments_by_day_item_data in _shipments_by_day or []:
            shipments_by_day_item = GetWMSShipmentMetricsResponse200DataShipmentsByDayItem.from_dict(
                shipments_by_day_item_data
            )

            shipments_by_day.append(shipments_by_day_item)

        get_wms_shipment_metrics_response_200_data = cls(
            total_shipments=total_shipments,
            shipped_shipments=shipped_shipments,
            delivered_shipments=delivered_shipments,
            exception_shipments=exception_shipments,
            average_transit_time=average_transit_time,
            on_time_delivery_rate=on_time_delivery_rate,
            shipments_by_carrier=shipments_by_carrier,
            shipments_by_day=shipments_by_day,
        )

        get_wms_shipment_metrics_response_200_data.additional_properties = d
        return get_wms_shipment_metrics_response_200_data

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
