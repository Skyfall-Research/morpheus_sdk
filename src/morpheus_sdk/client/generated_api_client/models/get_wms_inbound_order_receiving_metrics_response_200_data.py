from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_inbound_order_receiving_metrics_response_200_data_orders_by_status_item import (
        GetWMSInboundOrderReceivingMetricsResponse200DataOrdersByStatusItem,
    )
    from ..models.get_wms_inbound_order_receiving_metrics_response_200_data_top_vendors_item import (
        GetWMSInboundOrderReceivingMetricsResponse200DataTopVendorsItem,
    )


T = TypeVar("T", bound="GetWMSInboundOrderReceivingMetricsResponse200Data")


@_attrs_define
class GetWMSInboundOrderReceivingMetricsResponse200Data:
    """
    Attributes:
        total_orders (Union[Unset, float]): Total number of inbound orders in analysis period Example: 156.
        completed_orders (Union[Unset, float]): Number of fully received orders Example: 142.
        average_receiving_time (Union[Unset, float]): Average receiving time in hours Example: 4.2.
        on_time_receipts (Union[Unset, float]): Number of orders received on time Example: 134.
        late_receipts (Union[Unset, float]): Number of orders received late Example: 8.
        receiving_accuracy (Union[Unset, float]): Receiving accuracy percentage Example: 98.7.
        orders_by_status (Union[Unset, list['GetWMSInboundOrderReceivingMetricsResponse200DataOrdersByStatusItem']]):
            Distribution of orders by current status
        top_vendors (Union[Unset, list['GetWMSInboundOrderReceivingMetricsResponse200DataTopVendorsItem']]): Top
            performing vendors by order volume and performance
    """

    total_orders: Union[Unset, float] = UNSET
    completed_orders: Union[Unset, float] = UNSET
    average_receiving_time: Union[Unset, float] = UNSET
    on_time_receipts: Union[Unset, float] = UNSET
    late_receipts: Union[Unset, float] = UNSET
    receiving_accuracy: Union[Unset, float] = UNSET
    orders_by_status: Union[Unset, list["GetWMSInboundOrderReceivingMetricsResponse200DataOrdersByStatusItem"]] = UNSET
    top_vendors: Union[Unset, list["GetWMSInboundOrderReceivingMetricsResponse200DataTopVendorsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_orders = self.total_orders

        completed_orders = self.completed_orders

        average_receiving_time = self.average_receiving_time

        on_time_receipts = self.on_time_receipts

        late_receipts = self.late_receipts

        receiving_accuracy = self.receiving_accuracy

        orders_by_status: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.orders_by_status, Unset):
            orders_by_status = []
            for orders_by_status_item_data in self.orders_by_status:
                orders_by_status_item = orders_by_status_item_data.to_dict()
                orders_by_status.append(orders_by_status_item)

        top_vendors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.top_vendors, Unset):
            top_vendors = []
            for top_vendors_item_data in self.top_vendors:
                top_vendors_item = top_vendors_item_data.to_dict()
                top_vendors.append(top_vendors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_orders is not UNSET:
            field_dict["totalOrders"] = total_orders
        if completed_orders is not UNSET:
            field_dict["completedOrders"] = completed_orders
        if average_receiving_time is not UNSET:
            field_dict["averageReceivingTime"] = average_receiving_time
        if on_time_receipts is not UNSET:
            field_dict["onTimeReceipts"] = on_time_receipts
        if late_receipts is not UNSET:
            field_dict["lateReceipts"] = late_receipts
        if receiving_accuracy is not UNSET:
            field_dict["receivingAccuracy"] = receiving_accuracy
        if orders_by_status is not UNSET:
            field_dict["ordersByStatus"] = orders_by_status
        if top_vendors is not UNSET:
            field_dict["topVendors"] = top_vendors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_inbound_order_receiving_metrics_response_200_data_orders_by_status_item import (
            GetWMSInboundOrderReceivingMetricsResponse200DataOrdersByStatusItem,
        )
        from ..models.get_wms_inbound_order_receiving_metrics_response_200_data_top_vendors_item import (
            GetWMSInboundOrderReceivingMetricsResponse200DataTopVendorsItem,
        )

        d = dict(src_dict)
        total_orders = d.pop("totalOrders", UNSET)

        completed_orders = d.pop("completedOrders", UNSET)

        average_receiving_time = d.pop("averageReceivingTime", UNSET)

        on_time_receipts = d.pop("onTimeReceipts", UNSET)

        late_receipts = d.pop("lateReceipts", UNSET)

        receiving_accuracy = d.pop("receivingAccuracy", UNSET)

        orders_by_status = []
        _orders_by_status = d.pop("ordersByStatus", UNSET)
        for orders_by_status_item_data in _orders_by_status or []:
            orders_by_status_item = GetWMSInboundOrderReceivingMetricsResponse200DataOrdersByStatusItem.from_dict(
                orders_by_status_item_data
            )

            orders_by_status.append(orders_by_status_item)

        top_vendors = []
        _top_vendors = d.pop("topVendors", UNSET)
        for top_vendors_item_data in _top_vendors or []:
            top_vendors_item = GetWMSInboundOrderReceivingMetricsResponse200DataTopVendorsItem.from_dict(
                top_vendors_item_data
            )

            top_vendors.append(top_vendors_item)

        get_wms_inbound_order_receiving_metrics_response_200_data = cls(
            total_orders=total_orders,
            completed_orders=completed_orders,
            average_receiving_time=average_receiving_time,
            on_time_receipts=on_time_receipts,
            late_receipts=late_receipts,
            receiving_accuracy=receiving_accuracy,
            orders_by_status=orders_by_status,
            top_vendors=top_vendors,
        )

        get_wms_inbound_order_receiving_metrics_response_200_data.additional_properties = d
        return get_wms_inbound_order_receiving_metrics_response_200_data

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
