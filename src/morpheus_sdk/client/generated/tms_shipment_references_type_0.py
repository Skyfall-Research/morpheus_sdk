from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentReferencesType0")


@_attrs_define
class TMSShipmentReferencesType0:
    """Business reference numbers (optional)

    Attributes:
        order_id (Union[None, Unset, str]): Associated order ID Example: ORD-2024-5678.
        purchase_order_number (Union[None, Unset, str]): Purchase order number Example: PO-2024-9012.
        invoice_number (Union[None, Unset, str]): Invoice number Example: INV-2024-3456.
        customer_reference (Union[None, Unset, str]): Customer reference number Example: CUST-REF-789.
        load_number (Union[None, Unset, str]): Load number Example: LOAD-2024-012.
    """

    order_id: Union[None, Unset, str] = UNSET
    purchase_order_number: Union[None, Unset, str] = UNSET
    invoice_number: Union[None, Unset, str] = UNSET
    customer_reference: Union[None, Unset, str] = UNSET
    load_number: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id: Union[None, Unset, str]
        if isinstance(self.order_id, Unset):
            order_id = UNSET
        else:
            order_id = self.order_id

        purchase_order_number: Union[None, Unset, str]
        if isinstance(self.purchase_order_number, Unset):
            purchase_order_number = UNSET
        else:
            purchase_order_number = self.purchase_order_number

        invoice_number: Union[None, Unset, str]
        if isinstance(self.invoice_number, Unset):
            invoice_number = UNSET
        else:
            invoice_number = self.invoice_number

        customer_reference: Union[None, Unset, str]
        if isinstance(self.customer_reference, Unset):
            customer_reference = UNSET
        else:
            customer_reference = self.customer_reference

        load_number: Union[None, Unset, str]
        if isinstance(self.load_number, Unset):
            load_number = UNSET
        else:
            load_number = self.load_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if purchase_order_number is not UNSET:
            field_dict["purchaseOrderNumber"] = purchase_order_number
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if customer_reference is not UNSET:
            field_dict["customerReference"] = customer_reference
        if load_number is not UNSET:
            field_dict["loadNumber"] = load_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order_id = _parse_order_id(d.pop("orderId", UNSET))

        def _parse_purchase_order_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        purchase_order_number = _parse_purchase_order_number(d.pop("purchaseOrderNumber", UNSET))

        def _parse_invoice_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        invoice_number = _parse_invoice_number(d.pop("invoiceNumber", UNSET))

        def _parse_customer_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer_reference = _parse_customer_reference(d.pop("customerReference", UNSET))

        def _parse_load_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        load_number = _parse_load_number(d.pop("loadNumber", UNSET))

        tms_shipment_references_type_0 = cls(
            order_id=order_id,
            purchase_order_number=purchase_order_number,
            invoice_number=invoice_number,
            customer_reference=customer_reference,
            load_number=load_number,
        )

        tms_shipment_references_type_0.additional_properties = d
        return tms_shipment_references_type_0

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
