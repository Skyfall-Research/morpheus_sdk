from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateWMSPickingProgressBody")


@_attrs_define
class UpdateWMSPickingProgressBody:
    """
    Attributes:
        line_number (float): Target line identifier Example: 1.
        picked_quantity (float): Actual picked amount Example: 18.
    """

    line_number: float
    picked_quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        picked_quantity = self.picked_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineNumber": line_number,
                "pickedQuantity": picked_quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_number = d.pop("lineNumber")

        picked_quantity = d.pop("pickedQuantity")

        update_wms_picking_progress_body = cls(
            line_number=line_number,
            picked_quantity=picked_quantity,
        )

        update_wms_picking_progress_body.additional_properties = d
        return update_wms_picking_progress_body

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
