from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateERPInvoiceBodyLinesItem")


@_attrs_define
class UpdateERPInvoiceBodyLinesItem:
    """
    Attributes:
        line_number (Union[Unset, float]):  Example: 1.
        quantity (Union[Unset, float]):  Example: 12.
        unit_price (Union[Unset, float]):  Example: 89.99.
        line_amount (Union[Unset, float]):  Example: 1079.88.
    """

    line_number: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    line_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        quantity = self.quantity

        unit_price = self.unit_price

        line_amount = self.line_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_number is not UNSET:
            field_dict["lineNumber"] = line_number
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if line_amount is not UNSET:
            field_dict["lineAmount"] = line_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_number = d.pop("lineNumber", UNSET)

        quantity = d.pop("quantity", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        line_amount = d.pop("lineAmount", UNSET)

        update_erp_invoice_body_lines_item = cls(
            line_number=line_number,
            quantity=quantity,
            unit_price=unit_price,
            line_amount=line_amount,
        )

        update_erp_invoice_body_lines_item.additional_properties = d
        return update_erp_invoice_body_lines_item

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
