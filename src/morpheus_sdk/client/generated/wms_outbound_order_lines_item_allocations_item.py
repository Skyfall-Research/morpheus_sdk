from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundOrderLinesItemAllocationsItem")


@_attrs_define
class WMSOutboundOrderLinesItemAllocationsItem:
    """
    Attributes:
        bin_id (str): Source bin location identifier Example: BIN-A1-001.
        quantity (float): Allocated quantity from this bin Example: 15.
        lot_number (Union[Unset, str]): Optional lot/batch tracking Example: LOT-20241201-A.
    """

    bin_id: str
    quantity: float
    lot_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_id = self.bin_id

        quantity = self.quantity

        lot_number = self.lot_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "binId": bin_id,
                "quantity": quantity,
            }
        )
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bin_id = d.pop("binId")

        quantity = d.pop("quantity")

        lot_number = d.pop("lotNumber", UNSET)

        wms_outbound_order_lines_item_allocations_item = cls(
            bin_id=bin_id,
            quantity=quantity,
            lot_number=lot_number,
        )

        wms_outbound_order_lines_item_allocations_item.additional_properties = d
        return wms_outbound_order_lines_item_allocations_item

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
