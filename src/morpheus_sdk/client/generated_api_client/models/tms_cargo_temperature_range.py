from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tms_cargo_temperature_range_uom import TMSCargoTemperatureRangeUom
from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSCargoTemperatureRange")


@_attrs_define
class TMSCargoTemperatureRange:
    """
    Attributes:
        min_ (Union[Unset, float]):  Example: 32.
        max_ (Union[Unset, float]):  Example: 45.
        uom (Union[Unset, TMSCargoTemperatureRangeUom]):  Example: F.
    """

    min_: Union[Unset, float] = UNSET
    max_: Union[Unset, float] = UNSET
    uom: Union[Unset, TMSCargoTemperatureRangeUom] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_ = self.min_

        max_ = self.max_

        uom: Union[Unset, str] = UNSET
        if not isinstance(self.uom, Unset):
            uom = self.uom.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if uom is not UNSET:
            field_dict["uom"] = uom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        _uom = d.pop("uom", UNSET)
        uom: Union[Unset, TMSCargoTemperatureRangeUom]
        if isinstance(_uom, Unset):
            uom = UNSET
        else:
            uom = TMSCargoTemperatureRangeUom(_uom)

        tms_cargo_temperature_range = cls(
            min_=min_,
            max_=max_,
            uom=uom,
        )

        tms_cargo_temperature_range.additional_properties = d
        return tms_cargo_temperature_range

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
