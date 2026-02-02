import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInboundOrderRelationsResponse200DataErpOrder")


@_attrs_define
class GetWMSInboundOrderRelationsResponse200DataErpOrder:
    """Related ERP purchase order

    Attributes:
        order_id (Union[Unset, str]):  Example: PO-2024-001234.
        status (Union[Unset, str]):  Example: APPROVED.
        total_amount (Union[Unset, float]):  Example: 15000.
        customer_id (Union[Unset, str]):  Example: CUST-001.
        partner_id (Union[Unset, str]):  Example: VENDOR-001.
        po_type (Union[Unset, str]):  Example: STANDARD.
        order_date (Union[Unset, datetime.datetime]):  Example: 2024-01-10T00:00:00Z.
    """

    order_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    customer_id: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    po_type: Union[Unset, str] = UNSET
    order_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        status = self.status

        total_amount = self.total_amount

        customer_id = self.customer_id

        partner_id = self.partner_id

        po_type = self.po_type

        order_date: Union[Unset, str] = UNSET
        if not isinstance(self.order_date, Unset):
            order_date = self.order_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if status is not UNSET:
            field_dict["status"] = status
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if po_type is not UNSET:
            field_dict["poType"] = po_type
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("orderId", UNSET)

        status = d.pop("status", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        customer_id = d.pop("customerId", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        po_type = d.pop("poType", UNSET)

        _order_date = d.pop("orderDate", UNSET)
        order_date: Union[Unset, datetime.datetime]
        if isinstance(_order_date, Unset):
            order_date = UNSET
        else:
            order_date = isoparse(_order_date)

        get_wms_inbound_order_relations_response_200_data_erp_order = cls(
            order_id=order_id,
            status=status,
            total_amount=total_amount,
            customer_id=customer_id,
            partner_id=partner_id,
            po_type=po_type,
            order_date=order_date,
        )

        get_wms_inbound_order_relations_response_200_data_erp_order.additional_properties = d
        return get_wms_inbound_order_relations_response_200_data_erp_order

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
