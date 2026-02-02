from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDockDoorCapabilities")


@_attrs_define
class WMSDockDoorCapabilities:
    """Physical capabilities and specifications for trailer compatibility

    Attributes:
        max_trailer_length (Union[None, Unset, float]): Maximum supported trailer length in feet Example: 53.
        max_trailer_height (Union[None, Unset, float]): Maximum supported trailer height in feet Example: 13.5.
        leveling_dock (Union[Unset, bool]): Whether dock has leveling capability for trailer height adjustment Example:
            True.
        hydraulic_leveler (Union[Unset, bool]): Hydraulic leveling system availability for automated adjustments
            Example: True.
        restraint_system (Union[Unset, bool]): Trailer restraint system for safety during operations Example: True.
        weather_seal (Union[Unset, bool]): Weather sealing capability for environmental protection Example: True.
    """

    max_trailer_length: Union[None, Unset, float] = UNSET
    max_trailer_height: Union[None, Unset, float] = UNSET
    leveling_dock: Union[Unset, bool] = UNSET
    hydraulic_leveler: Union[Unset, bool] = UNSET
    restraint_system: Union[Unset, bool] = UNSET
    weather_seal: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_trailer_length: Union[None, Unset, float]
        if isinstance(self.max_trailer_length, Unset):
            max_trailer_length = UNSET
        else:
            max_trailer_length = self.max_trailer_length

        max_trailer_height: Union[None, Unset, float]
        if isinstance(self.max_trailer_height, Unset):
            max_trailer_height = UNSET
        else:
            max_trailer_height = self.max_trailer_height

        leveling_dock = self.leveling_dock

        hydraulic_leveler = self.hydraulic_leveler

        restraint_system = self.restraint_system

        weather_seal = self.weather_seal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_trailer_length is not UNSET:
            field_dict["maxTrailerLength"] = max_trailer_length
        if max_trailer_height is not UNSET:
            field_dict["maxTrailerHeight"] = max_trailer_height
        if leveling_dock is not UNSET:
            field_dict["levelingDock"] = leveling_dock
        if hydraulic_leveler is not UNSET:
            field_dict["hydraulicLeveler"] = hydraulic_leveler
        if restraint_system is not UNSET:
            field_dict["restraintSystem"] = restraint_system
        if weather_seal is not UNSET:
            field_dict["weatherSeal"] = weather_seal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_max_trailer_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_trailer_length = _parse_max_trailer_length(d.pop("maxTrailerLength", UNSET))

        def _parse_max_trailer_height(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_trailer_height = _parse_max_trailer_height(d.pop("maxTrailerHeight", UNSET))

        leveling_dock = d.pop("levelingDock", UNSET)

        hydraulic_leveler = d.pop("hydraulicLeveler", UNSET)

        restraint_system = d.pop("restraintSystem", UNSET)

        weather_seal = d.pop("weatherSeal", UNSET)

        wms_dock_door_capabilities = cls(
            max_trailer_length=max_trailer_length,
            max_trailer_height=max_trailer_height,
            leveling_dock=leveling_dock,
            hydraulic_leveler=hydraulic_leveler,
            restraint_system=restraint_system,
            weather_seal=weather_seal,
        )

        wms_dock_door_capabilities.additional_properties = d
        return wms_dock_door_capabilities

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
