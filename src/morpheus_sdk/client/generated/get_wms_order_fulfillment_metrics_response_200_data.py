from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_order_fulfillment_metrics_response_200_data_orders_by_status_item import (
        GetWMSOrderFulfillmentMetricsResponse200DataOrdersByStatusItem,
    )
    from ..models.get_wms_order_fulfillment_metrics_response_200_data_top_customers_item import (
        GetWMSOrderFulfillmentMetricsResponse200DataTopCustomersItem,
    )


T = TypeVar("T", bound="GetWMSOrderFulfillmentMetricsResponse200Data")


@_attrs_define
class GetWMSOrderFulfillmentMetricsResponse200Data:
    """
    Attributes:
        total_orders (Union[Unset, float]): Total orders in period Example: 1250.
        completed_orders (Union[Unset, float]): Orders with SHIPPED status Example: 1180.
        average_fulfillment_time (Union[Unset, float]): Average hours from order to ship Example: 18.5.
        on_time_shipments (Union[Unset, float]): Orders shipped by requested date Example: 1050.
        fulfillment_rate (Union[Unset, float]): Completion percentage Example: 94.4.
        orders_by_status (Union[Unset, list['GetWMSOrderFulfillmentMetricsResponse200DataOrdersByStatusItem']]): Status
            distribution
        top_customers (Union[Unset, list['GetWMSOrderFulfillmentMetricsResponse200DataTopCustomersItem']]): Customer
            ranking by volume (top 10)
    """

    total_orders: Union[Unset, float] = UNSET
    completed_orders: Union[Unset, float] = UNSET
    average_fulfillment_time: Union[Unset, float] = UNSET
    on_time_shipments: Union[Unset, float] = UNSET
    fulfillment_rate: Union[Unset, float] = UNSET
    orders_by_status: Union[Unset, list["GetWMSOrderFulfillmentMetricsResponse200DataOrdersByStatusItem"]] = UNSET
    top_customers: Union[Unset, list["GetWMSOrderFulfillmentMetricsResponse200DataTopCustomersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_orders = self.total_orders

        completed_orders = self.completed_orders

        average_fulfillment_time = self.average_fulfillment_time

        on_time_shipments = self.on_time_shipments

        fulfillment_rate = self.fulfillment_rate

        orders_by_status: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.orders_by_status, Unset):
            orders_by_status = []
            for orders_by_status_item_data in self.orders_by_status:
                orders_by_status_item = orders_by_status_item_data.to_dict()
                orders_by_status.append(orders_by_status_item)

        top_customers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.top_customers, Unset):
            top_customers = []
            for top_customers_item_data in self.top_customers:
                top_customers_item = top_customers_item_data.to_dict()
                top_customers.append(top_customers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_orders is not UNSET:
            field_dict["totalOrders"] = total_orders
        if completed_orders is not UNSET:
            field_dict["completedOrders"] = completed_orders
        if average_fulfillment_time is not UNSET:
            field_dict["averageFulfillmentTime"] = average_fulfillment_time
        if on_time_shipments is not UNSET:
            field_dict["onTimeShipments"] = on_time_shipments
        if fulfillment_rate is not UNSET:
            field_dict["fulfillmentRate"] = fulfillment_rate
        if orders_by_status is not UNSET:
            field_dict["ordersByStatus"] = orders_by_status
        if top_customers is not UNSET:
            field_dict["topCustomers"] = top_customers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_order_fulfillment_metrics_response_200_data_orders_by_status_item import (
            GetWMSOrderFulfillmentMetricsResponse200DataOrdersByStatusItem,
        )
        from ..models.get_wms_order_fulfillment_metrics_response_200_data_top_customers_item import (
            GetWMSOrderFulfillmentMetricsResponse200DataTopCustomersItem,
        )

        d = dict(src_dict)
        total_orders = d.pop("totalOrders", UNSET)

        completed_orders = d.pop("completedOrders", UNSET)

        average_fulfillment_time = d.pop("averageFulfillmentTime", UNSET)

        on_time_shipments = d.pop("onTimeShipments", UNSET)

        fulfillment_rate = d.pop("fulfillmentRate", UNSET)

        orders_by_status = []
        _orders_by_status = d.pop("ordersByStatus", UNSET)
        for orders_by_status_item_data in _orders_by_status or []:
            orders_by_status_item = GetWMSOrderFulfillmentMetricsResponse200DataOrdersByStatusItem.from_dict(
                orders_by_status_item_data
            )

            orders_by_status.append(orders_by_status_item)

        top_customers = []
        _top_customers = d.pop("topCustomers", UNSET)
        for top_customers_item_data in _top_customers or []:
            top_customers_item = GetWMSOrderFulfillmentMetricsResponse200DataTopCustomersItem.from_dict(
                top_customers_item_data
            )

            top_customers.append(top_customers_item)

        get_wms_order_fulfillment_metrics_response_200_data = cls(
            total_orders=total_orders,
            completed_orders=completed_orders,
            average_fulfillment_time=average_fulfillment_time,
            on_time_shipments=on_time_shipments,
            fulfillment_rate=fulfillment_rate,
            orders_by_status=orders_by_status,
            top_customers=top_customers,
        )

        get_wms_order_fulfillment_metrics_response_200_data.additional_properties = d
        return get_wms_order_fulfillment_metrics_response_200_data

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
