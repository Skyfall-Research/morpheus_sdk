from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSOrderFulfillmentMetricsResponse200DataTopCustomersItem")


@_attrs_define
class GetWMSOrderFulfillmentMetricsResponse200DataTopCustomersItem:
    """
    Attributes:
        customer_id (Union[Unset, str]):  Example: CUST-ABC-123.
        customer_name (Union[Unset, str]):  Example: ABC Corporation.
        order_count (Union[Unset, float]):  Example: 45.
        total_lines (Union[Unset, float]):  Example: 128.
    """

    customer_id: Union[Unset, str] = UNSET
    customer_name: Union[Unset, str] = UNSET
    order_count: Union[Unset, float] = UNSET
    total_lines: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        customer_name = self.customer_name

        order_count = self.order_count

        total_lines = self.total_lines

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if order_count is not UNSET:
            field_dict["orderCount"] = order_count
        if total_lines is not UNSET:
            field_dict["totalLines"] = total_lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_id = d.pop("customerId", UNSET)

        customer_name = d.pop("customerName", UNSET)

        order_count = d.pop("orderCount", UNSET)

        total_lines = d.pop("totalLines", UNSET)

        get_wms_order_fulfillment_metrics_response_200_data_top_customers_item = cls(
            customer_id=customer_id,
            customer_name=customer_name,
            order_count=order_count,
            total_lines=total_lines,
        )

        get_wms_order_fulfillment_metrics_response_200_data_top_customers_item.additional_properties = d
        return get_wms_order_fulfillment_metrics_response_200_data_top_customers_item

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
