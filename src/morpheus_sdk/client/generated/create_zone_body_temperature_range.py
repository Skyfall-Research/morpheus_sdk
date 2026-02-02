from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateZoneBodyTemperatureRange")


@_attrs_define
class CreateZoneBodyTemperatureRange:
    """Temperature configuration for controlled zones

    Attributes:
        min_ (Union[Unset, float]):  Example: 32.
        max_ (Union[Unset, float]):  Example: 40.
        unit (Union[Unset, str]):  Example: Fahrenheit.
    """

    min_: Union[Unset, float] = UNSET
    max_: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_ = self.min_

        max_ = self.max_

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        unit = d.pop("unit", UNSET)

        create_zone_body_temperature_range = cls(
            min_=min_,
            max_=max_,
            unit=unit,
        )

        create_zone_body_temperature_range.additional_properties = d
        return create_zone_body_temperature_range

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
