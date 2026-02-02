from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_invoice_lines_item_accounting import ERPInvoiceLinesItemAccounting
    from ..models.erp_invoice_lines_item_custom_fields import ERPInvoiceLinesItemCustomFields
    from ..models.erp_invoice_lines_item_discount import ERPInvoiceLinesItemDiscount
    from ..models.tax_detail import TaxDetail


T = TypeVar("T", bound="ERPInvoiceLinesItem")


@_attrs_define
class ERPInvoiceLinesItem:
    """
    Attributes:
        line_number (Union[Unset, float]):  Example: 1.
        sku (Union[Unset, str]):  Example: PROD_WIDGET_001.
        description (Union[Unset, str]):  Example: Premium Widget - Blue.
        quantity (Union[Unset, float]):  Example: 10.
        unit_price (Union[Unset, float]):  Example: 99.99.
        line_amount (Union[Unset, float]):  Example: 999.9.
        discount (Union[Unset, ERPInvoiceLinesItemDiscount]): Line-level discount
        tax_details (Union[Unset, list['TaxDetail']]): Line-level tax details
        accounting (Union[Unset, ERPInvoiceLinesItemAccounting]): Line-level accounting info
        custom_fields (Union[Unset, ERPInvoiceLinesItemCustomFields]): Line-specific custom fields
    """

    line_number: Union[Unset, float] = UNSET
    sku: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    line_amount: Union[Unset, float] = UNSET
    discount: Union[Unset, "ERPInvoiceLinesItemDiscount"] = UNSET
    tax_details: Union[Unset, list["TaxDetail"]] = UNSET
    accounting: Union[Unset, "ERPInvoiceLinesItemAccounting"] = UNSET
    custom_fields: Union[Unset, "ERPInvoiceLinesItemCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        sku = self.sku

        description = self.description

        quantity = self.quantity

        unit_price = self.unit_price

        line_amount = self.line_amount

        discount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        tax_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tax_details, Unset):
            tax_details = []
            for tax_details_item_data in self.tax_details:
                tax_details_item = tax_details_item_data.to_dict()
                tax_details.append(tax_details_item)

        accounting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.accounting, Unset):
            accounting = self.accounting.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_number is not UNSET:
            field_dict["lineNumber"] = line_number
        if sku is not UNSET:
            field_dict["sku"] = sku
        if description is not UNSET:
            field_dict["description"] = description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if line_amount is not UNSET:
            field_dict["lineAmount"] = line_amount
        if discount is not UNSET:
            field_dict["discount"] = discount
        if tax_details is not UNSET:
            field_dict["taxDetails"] = tax_details
        if accounting is not UNSET:
            field_dict["accounting"] = accounting
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_invoice_lines_item_accounting import ERPInvoiceLinesItemAccounting
        from ..models.erp_invoice_lines_item_custom_fields import ERPInvoiceLinesItemCustomFields
        from ..models.erp_invoice_lines_item_discount import ERPInvoiceLinesItemDiscount
        from ..models.tax_detail import TaxDetail

        d = dict(src_dict)
        line_number = d.pop("lineNumber", UNSET)

        sku = d.pop("sku", UNSET)

        description = d.pop("description", UNSET)

        quantity = d.pop("quantity", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        line_amount = d.pop("lineAmount", UNSET)

        _discount = d.pop("discount", UNSET)
        discount: Union[Unset, ERPInvoiceLinesItemDiscount]
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = ERPInvoiceLinesItemDiscount.from_dict(_discount)

        tax_details = []
        _tax_details = d.pop("taxDetails", UNSET)
        for tax_details_item_data in _tax_details or []:
            tax_details_item = TaxDetail.from_dict(tax_details_item_data)

            tax_details.append(tax_details_item)

        _accounting = d.pop("accounting", UNSET)
        accounting: Union[Unset, ERPInvoiceLinesItemAccounting]
        if isinstance(_accounting, Unset):
            accounting = UNSET
        else:
            accounting = ERPInvoiceLinesItemAccounting.from_dict(_accounting)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, ERPInvoiceLinesItemCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ERPInvoiceLinesItemCustomFields.from_dict(_custom_fields)

        erp_invoice_lines_item = cls(
            line_number=line_number,
            sku=sku,
            description=description,
            quantity=quantity,
            unit_price=unit_price,
            line_amount=line_amount,
            discount=discount,
            tax_details=tax_details,
            accounting=accounting,
            custom_fields=custom_fields,
        )

        erp_invoice_lines_item.additional_properties = d
        return erp_invoice_lines_item

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
