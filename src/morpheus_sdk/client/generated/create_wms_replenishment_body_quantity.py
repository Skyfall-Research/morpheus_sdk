from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateWMSReplenishmentBodyQuantity")


@_attrs_define
class CreateWMSReplenishmentBodyQuantity:
    """Quantity information for replenishment

    Attributes:
        suggested (float):  Example: 150.
        uom (str):  Example: EA.
    """

    suggested: float
    uom: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggested = self.suggested

        uom = self.uom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suggested": suggested,
                "uom": uom,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        suggested = d.pop("suggested")

        uom = d.pop("uom")

        create_wms_replenishment_body_quantity = cls(
            suggested=suggested,
            uom=uom,
        )

        create_wms_replenishment_body_quantity.additional_properties = d
        return create_wms_replenishment_body_quantity

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
