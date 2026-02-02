from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSZoneAislesItem")


@_attrs_define
class WMSZoneAislesItem:
    """
    Attributes:
        aisle_id (Union[Unset, str]): Aisle identifier Example: AISLE_A1_001.
        aisle_code (Union[Unset, str]): Human-readable aisle code Example: A1.
        aisle_type (Union[Unset, str]): Aisle type classification Example: STANDARD.
    """

    aisle_id: Union[Unset, str] = UNSET
    aisle_code: Union[Unset, str] = UNSET
    aisle_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aisle_id = self.aisle_id

        aisle_code = self.aisle_code

        aisle_type = self.aisle_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aisle_id is not UNSET:
            field_dict["aisleId"] = aisle_id
        if aisle_code is not UNSET:
            field_dict["aisleCode"] = aisle_code
        if aisle_type is not UNSET:
            field_dict["aisleType"] = aisle_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aisle_id = d.pop("aisleId", UNSET)

        aisle_code = d.pop("aisleCode", UNSET)

        aisle_type = d.pop("aisleType", UNSET)

        wms_zone_aisles_item = cls(
            aisle_id=aisle_id,
            aisle_code=aisle_code,
            aisle_type=aisle_type,
        )

        wms_zone_aisles_item.additional_properties = d
        return wms_zone_aisles_item

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
