from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxDetail")


@_attrs_define
class TaxDetail:
    """Tax detail information for orders, invoices, and line items

    Attributes:
        tax_type (Union[Unset, str]): Type of tax (e.g., VAT, SALES, STATE, LOCAL) Example: VAT.
        jurisdiction (Union[Unset, str]): Tax jurisdiction Example: US-CA.
        tax_rate (Union[Unset, float]): Tax rate as a decimal Example: 0.08.
        tax_amount (Union[Unset, float]): Calculated tax amount Example: 24.
        taxable_base (Union[Unset, float]): Base amount on which tax is calculated Example: 300.
        tax_id (Union[Unset, str]): Tax identifier Example: TAX_001.
    """

    tax_type: Union[Unset, str] = UNSET
    jurisdiction: Union[Unset, str] = UNSET
    tax_rate: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    taxable_base: Union[Unset, float] = UNSET
    tax_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tax_type = self.tax_type

        jurisdiction = self.jurisdiction

        tax_rate = self.tax_rate

        tax_amount = self.tax_amount

        taxable_base = self.taxable_base

        tax_id = self.tax_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tax_type is not UNSET:
            field_dict["taxType"] = tax_type
        if jurisdiction is not UNSET:
            field_dict["jurisdiction"] = jurisdiction
        if tax_rate is not UNSET:
            field_dict["taxRate"] = tax_rate
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if taxable_base is not UNSET:
            field_dict["taxableBase"] = taxable_base
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tax_type = d.pop("taxType", UNSET)

        jurisdiction = d.pop("jurisdiction", UNSET)

        tax_rate = d.pop("taxRate", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        taxable_base = d.pop("taxableBase", UNSET)

        tax_id = d.pop("taxId", UNSET)

        tax_detail = cls(
            tax_type=tax_type,
            jurisdiction=jurisdiction,
            tax_rate=tax_rate,
            tax_amount=tax_amount,
            taxable_base=taxable_base,
            tax_id=tax_id,
        )

        tax_detail.additional_properties = d
        return tax_detail

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
