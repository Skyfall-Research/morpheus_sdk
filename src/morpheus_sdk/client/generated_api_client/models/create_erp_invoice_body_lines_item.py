from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateERPInvoiceBodyLinesItem")


@_attrs_define
class CreateERPInvoiceBodyLinesItem:
    """
    Attributes:
        line_number (float): Line item sequence number Example: 1.
        sku (str): Product SKU identifier Example: PROD_WIDGET_001.
        quantity (float): Invoiced quantity Example: 10.
        unit_price (float): Unit price per item Example: 99.99.
        description (Union[Unset, str]): Line item description Example: Premium Widget - Blue.
        line_amount (Union[Unset, float]): Total line amount Example: 999.9.
    """

    line_number: float
    sku: str
    quantity: float
    unit_price: float
    description: Union[Unset, str] = UNSET
    line_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        sku = self.sku

        quantity = self.quantity

        unit_price = self.unit_price

        description = self.description

        line_amount = self.line_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineNumber": line_number,
                "sku": sku,
                "quantity": quantity,
                "unitPrice": unit_price,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if line_amount is not UNSET:
            field_dict["lineAmount"] = line_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_number = d.pop("lineNumber")

        sku = d.pop("sku")

        quantity = d.pop("quantity")

        unit_price = d.pop("unitPrice")

        description = d.pop("description", UNSET)

        line_amount = d.pop("lineAmount", UNSET)

        create_erp_invoice_body_lines_item = cls(
            line_number=line_number,
            sku=sku,
            quantity=quantity,
            unit_price=unit_price,
            description=description,
            line_amount=line_amount,
        )

        create_erp_invoice_body_lines_item.additional_properties = d
        return create_erp_invoice_body_lines_item

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
