from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSOutboundOrderBodyLinesItem")


@_attrs_define
class CreateWMSOutboundOrderBodyLinesItem:
    """
    Attributes:
        line_number (float): Sequential line identifier within order Example: 1.
        item_id (str): SKU/product code Example: SKU-WIDGET-001.
        item_description (str): Product display name Example: Premium Widget Assembly.
        ordered_quantity (float): Customer requested amount Example: 25.
        unit_of_measure (str): UOM code (EA, CS, LB, KG, etc.) Example: EA.
        unit_price (Union[Unset, float]): Price per unit (optional) Example: 49.99.
        special_instructions (Union[Unset, str]): Line-specific handling notes Example: Handle with care - fragile.
    """

    line_number: float
    item_id: str
    item_description: str
    ordered_quantity: float
    unit_of_measure: str
    unit_price: Union[Unset, float] = UNSET
    special_instructions: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        item_id = self.item_id

        item_description = self.item_description

        ordered_quantity = self.ordered_quantity

        unit_of_measure = self.unit_of_measure

        unit_price = self.unit_price

        special_instructions = self.special_instructions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineNumber": line_number,
                "itemId": item_id,
                "itemDescription": item_description,
                "orderedQuantity": ordered_quantity,
                "unitOfMeasure": unit_of_measure,
            }
        )
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if special_instructions is not UNSET:
            field_dict["specialInstructions"] = special_instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_number = d.pop("lineNumber")

        item_id = d.pop("itemId")

        item_description = d.pop("itemDescription")

        ordered_quantity = d.pop("orderedQuantity")

        unit_of_measure = d.pop("unitOfMeasure")

        unit_price = d.pop("unitPrice", UNSET)

        special_instructions = d.pop("specialInstructions", UNSET)

        create_wms_outbound_order_body_lines_item = cls(
            line_number=line_number,
            item_id=item_id,
            item_description=item_description,
            ordered_quantity=ordered_quantity,
            unit_of_measure=unit_of_measure,
            unit_price=unit_price,
            special_instructions=special_instructions,
        )

        create_wms_outbound_order_body_lines_item.additional_properties = d
        return create_wms_outbound_order_body_lines_item

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
