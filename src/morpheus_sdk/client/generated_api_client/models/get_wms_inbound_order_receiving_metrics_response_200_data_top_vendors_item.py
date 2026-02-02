from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInboundOrderReceivingMetricsResponse200DataTopVendorsItem")


@_attrs_define
class GetWMSInboundOrderReceivingMetricsResponse200DataTopVendorsItem:
    """
    Attributes:
        vendor_id (Union[Unset, str]): Vendor identifier Example: VND-SWIFT-001.
        vendor_name (Union[Unset, str]): Vendor company name Example: Swift Manufacturing Co..
        order_count (Union[Unset, float]): Number of orders from this vendor Example: 24.
        total_lines (Union[Unset, float]): Total product lines from this vendor Example: 186.
        on_time_percentage (Union[Unset, float]): On-time delivery percentage for this vendor Example: 95.8.
    """

    vendor_id: Union[Unset, str] = UNSET
    vendor_name: Union[Unset, str] = UNSET
    order_count: Union[Unset, float] = UNSET
    total_lines: Union[Unset, float] = UNSET
    on_time_percentage: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vendor_id = self.vendor_id

        vendor_name = self.vendor_name

        order_count = self.order_count

        total_lines = self.total_lines

        on_time_percentage = self.on_time_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vendor_id is not UNSET:
            field_dict["vendorId"] = vendor_id
        if vendor_name is not UNSET:
            field_dict["vendorName"] = vendor_name
        if order_count is not UNSET:
            field_dict["orderCount"] = order_count
        if total_lines is not UNSET:
            field_dict["totalLines"] = total_lines
        if on_time_percentage is not UNSET:
            field_dict["onTimePercentage"] = on_time_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vendor_id = d.pop("vendorId", UNSET)

        vendor_name = d.pop("vendorName", UNSET)

        order_count = d.pop("orderCount", UNSET)

        total_lines = d.pop("totalLines", UNSET)

        on_time_percentage = d.pop("onTimePercentage", UNSET)

        get_wms_inbound_order_receiving_metrics_response_200_data_top_vendors_item = cls(
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            order_count=order_count,
            total_lines=total_lines,
            on_time_percentage=on_time_percentage,
        )

        get_wms_inbound_order_receiving_metrics_response_200_data_top_vendors_item.additional_properties = d
        return get_wms_inbound_order_receiving_metrics_response_200_data_top_vendors_item

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
