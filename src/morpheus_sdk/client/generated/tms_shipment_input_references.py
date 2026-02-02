from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentInputReferences")


@_attrs_define
class TMSShipmentInputReferences:
    """Business reference numbers

    Attributes:
        order_id (Union[Unset, str]):  Example: ORD-2024-5678.
        purchase_order_number (Union[Unset, str]):  Example: PO-2024-9012.
        customer_reference (Union[Unset, str]):  Example: CUST-REF-789.
    """

    order_id: Union[Unset, str] = UNSET
    purchase_order_number: Union[Unset, str] = UNSET
    customer_reference: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        purchase_order_number = self.purchase_order_number

        customer_reference = self.customer_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if purchase_order_number is not UNSET:
            field_dict["purchaseOrderNumber"] = purchase_order_number
        if customer_reference is not UNSET:
            field_dict["customerReference"] = customer_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("orderId", UNSET)

        purchase_order_number = d.pop("purchaseOrderNumber", UNSET)

        customer_reference = d.pop("customerReference", UNSET)

        tms_shipment_input_references = cls(
            order_id=order_id,
            purchase_order_number=purchase_order_number,
            customer_reference=customer_reference,
        )

        tms_shipment_input_references.additional_properties = d
        return tms_shipment_input_references

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
