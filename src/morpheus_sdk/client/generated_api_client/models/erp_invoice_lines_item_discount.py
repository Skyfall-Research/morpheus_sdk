from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ERPInvoiceLinesItemDiscount")


@_attrs_define
class ERPInvoiceLinesItemDiscount:
    """Line-level discount

    Attributes:
        amount (Union[Unset, float]):  Example: 10.
        percent (Union[Unset, float]):  Example: 5.
    """

    amount: Union[Unset, float] = UNSET
    percent: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        percent = self.percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if percent is not UNSET:
            field_dict["percent"] = percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        percent = d.pop("percent", UNSET)

        erp_invoice_lines_item_discount = cls(
            amount=amount,
            percent=percent,
        )

        erp_invoice_lines_item_discount.additional_properties = d
        return erp_invoice_lines_item_discount

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
