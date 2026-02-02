from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInboundOrderReceivingMetricsResponse200DataOrdersByStatusItem")


@_attrs_define
class GetWMSInboundOrderReceivingMetricsResponse200DataOrdersByStatusItem:
    """
    Attributes:
        status (Union[Unset, str]): Order status Example: RECEIVED.
        count (Union[Unset, float]): Number of orders with this status Example: 142.
    """

    status: Union[Unset, str] = UNSET
    count: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        count = d.pop("count", UNSET)

        get_wms_inbound_order_receiving_metrics_response_200_data_orders_by_status_item = cls(
            status=status,
            count=count,
        )

        get_wms_inbound_order_receiving_metrics_response_200_data_orders_by_status_item.additional_properties = d
        return get_wms_inbound_order_receiving_metrics_response_200_data_orders_by_status_item

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
