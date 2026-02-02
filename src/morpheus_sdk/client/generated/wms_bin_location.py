from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSBinLocation")


@_attrs_define
class WMSBinLocation:
    """Precise physical location within warehouse

    Attributes:
        aisle (Union[Unset, str]): Aisle designation Example: A01.
        bay (Union[Unset, str]): Bay designation within aisle Example: B05.
        level (Union[Unset, int]): Level/tier number Example: 2.
        position (Union[Unset, str]): Position within bay Example: P03.
    """

    aisle: Union[Unset, str] = UNSET
    bay: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    position: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aisle = self.aisle

        bay = self.bay

        level = self.level

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aisle is not UNSET:
            field_dict["aisle"] = aisle
        if bay is not UNSET:
            field_dict["bay"] = bay
        if level is not UNSET:
            field_dict["level"] = level
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aisle = d.pop("aisle", UNSET)

        bay = d.pop("bay", UNSET)

        level = d.pop("level", UNSET)

        position = d.pop("position", UNSET)

        wms_bin_location = cls(
            aisle=aisle,
            bay=bay,
            level=level,
            position=position,
        )

        wms_bin_location.additional_properties = d
        return wms_bin_location

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
