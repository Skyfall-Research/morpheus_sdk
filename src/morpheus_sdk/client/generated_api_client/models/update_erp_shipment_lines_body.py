from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_erp_shipment_lines_body_lines_item import UpdateERPShipmentLinesBodyLinesItem


T = TypeVar("T", bound="UpdateERPShipmentLinesBody")


@_attrs_define
class UpdateERPShipmentLinesBody:
    """
    Attributes:
        lines (list['UpdateERPShipmentLinesBodyLinesItem']): Complete array of shipment line items (replaces existing)
    """

    lines: list["UpdateERPShipmentLinesBodyLinesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lines": lines,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_erp_shipment_lines_body_lines_item import UpdateERPShipmentLinesBodyLinesItem

        d = dict(src_dict)
        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = UpdateERPShipmentLinesBodyLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        update_erp_shipment_lines_body = cls(
            lines=lines,
        )

        update_erp_shipment_lines_body.additional_properties = d
        return update_erp_shipment_lines_body

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
