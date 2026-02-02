from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddAisleToZoneBody")


@_attrs_define
class AddAisleToZoneBody:
    """
    Attributes:
        aisle_id (str): Aisle identifier Example: AISLE_A1_001.
        aisle_code (str): Aisle code Example: A1.
        aisle_type (str): Aisle type Example: STANDARD.
    """

    aisle_id: str
    aisle_code: str
    aisle_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aisle_id = self.aisle_id

        aisle_code = self.aisle_code

        aisle_type = self.aisle_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aisleId": aisle_id,
                "aisleCode": aisle_code,
                "aisleType": aisle_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aisle_id = d.pop("aisleId")

        aisle_code = d.pop("aisleCode")

        aisle_type = d.pop("aisleType")

        add_aisle_to_zone_body = cls(
            aisle_id=aisle_id,
            aisle_code=aisle_code,
            aisle_type=aisle_type,
        )

        add_aisle_to_zone_body.additional_properties = d
        return add_aisle_to_zone_body

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
