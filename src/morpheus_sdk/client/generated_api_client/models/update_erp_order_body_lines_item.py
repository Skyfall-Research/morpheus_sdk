from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateERPOrderBodyLinesItem")


@_attrs_define
class UpdateERPOrderBodyLinesItem:
    """
    Attributes:
        line_number (Union[Unset, float]):  Example: 1.
        quantity_ordered (Union[Unset, float]):  Example: 15.
        unit_price (Union[Unset, float]):  Example: 89.99.
        line_total (Union[Unset, float]):  Example: 1349.85.
    """

    line_number: Union[Unset, float] = UNSET
    quantity_ordered: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    line_total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        quantity_ordered = self.quantity_ordered

        unit_price = self.unit_price

        line_total = self.line_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_number is not UNSET:
            field_dict["lineNumber"] = line_number
        if quantity_ordered is not UNSET:
            field_dict["quantityOrdered"] = quantity_ordered
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if line_total is not UNSET:
            field_dict["lineTotal"] = line_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_number = d.pop("lineNumber", UNSET)

        quantity_ordered = d.pop("quantityOrdered", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        line_total = d.pop("lineTotal", UNSET)

        update_erp_order_body_lines_item = cls(
            line_number=line_number,
            quantity_ordered=quantity_ordered,
            unit_price=unit_price,
            line_total=line_total,
        )

        update_erp_order_body_lines_item.additional_properties = d
        return update_erp_order_body_lines_item

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
