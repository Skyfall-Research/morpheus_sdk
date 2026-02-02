from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ERPInvoiceLinesItemAccounting")


@_attrs_define
class ERPInvoiceLinesItemAccounting:
    """Line-level accounting info

    Attributes:
        cost_center (Union[Unset, str]):  Example: CC001.
        gl_account (Union[Unset, str]):  Example: 4100-REVENUE.
    """

    cost_center: Union[Unset, str] = UNSET
    gl_account: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_center = self.cost_center

        gl_account = self.gl_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if gl_account is not UNSET:
            field_dict["glAccount"] = gl_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_center = d.pop("costCenter", UNSET)

        gl_account = d.pop("glAccount", UNSET)

        erp_invoice_lines_item_accounting = cls(
            cost_center=cost_center,
            gl_account=gl_account,
        )

        erp_invoice_lines_item_accounting.additional_properties = d
        return erp_invoice_lines_item_accounting

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
