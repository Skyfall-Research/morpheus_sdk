from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_zone_body_zone_type import UpdateZoneBodyZoneType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_zone_body_custom_fields import UpdateZoneBodyCustomFields
    from ..models.update_zone_body_temperature_range import UpdateZoneBodyTemperatureRange


T = TypeVar("T", bound="UpdateZoneBody")


@_attrs_define
class UpdateZoneBody:
    """
    Attributes:
        zone_name (Union[Unset, str]): Updated zone name Example: Enhanced Picking Zone A.
        zone_type (Union[Unset, UpdateZoneBodyZoneType]): Updated zone type Example: STORAGE.
        temperature_controlled (Union[Unset, bool]): Updated temperature control flag Example: True.
        temperature_range (Union[Unset, UpdateZoneBodyTemperatureRange]): Updated temperature configuration
        capacity_cubic_feet (Union[Unset, float]): Updated zone capacity Example: 75000.
        custom_fields (Union[Unset, UpdateZoneBodyCustomFields]): Updated custom data
    """

    zone_name: Union[Unset, str] = UNSET
    zone_type: Union[Unset, UpdateZoneBodyZoneType] = UNSET
    temperature_controlled: Union[Unset, bool] = UNSET
    temperature_range: Union[Unset, "UpdateZoneBodyTemperatureRange"] = UNSET
    capacity_cubic_feet: Union[Unset, float] = UNSET
    custom_fields: Union[Unset, "UpdateZoneBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_name = self.zone_name

        zone_type: Union[Unset, str] = UNSET
        if not isinstance(self.zone_type, Unset):
            zone_type = self.zone_type.value

        temperature_controlled = self.temperature_controlled

        temperature_range: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temperature_range, Unset):
            temperature_range = self.temperature_range.to_dict()

        capacity_cubic_feet = self.capacity_cubic_feet

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zone_name is not UNSET:
            field_dict["zoneName"] = zone_name
        if zone_type is not UNSET:
            field_dict["zoneType"] = zone_type
        if temperature_controlled is not UNSET:
            field_dict["temperatureControlled"] = temperature_controlled
        if temperature_range is not UNSET:
            field_dict["temperatureRange"] = temperature_range
        if capacity_cubic_feet is not UNSET:
            field_dict["capacityCubicFeet"] = capacity_cubic_feet
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_zone_body_custom_fields import UpdateZoneBodyCustomFields
        from ..models.update_zone_body_temperature_range import UpdateZoneBodyTemperatureRange

        d = dict(src_dict)
        zone_name = d.pop("zoneName", UNSET)

        _zone_type = d.pop("zoneType", UNSET)
        zone_type: Union[Unset, UpdateZoneBodyZoneType]
        if isinstance(_zone_type, Unset):
            zone_type = UNSET
        else:
            zone_type = UpdateZoneBodyZoneType(_zone_type)

        temperature_controlled = d.pop("temperatureControlled", UNSET)

        _temperature_range = d.pop("temperatureRange", UNSET)
        temperature_range: Union[Unset, UpdateZoneBodyTemperatureRange]
        if isinstance(_temperature_range, Unset):
            temperature_range = UNSET
        else:
            temperature_range = UpdateZoneBodyTemperatureRange.from_dict(_temperature_range)

        capacity_cubic_feet = d.pop("capacityCubicFeet", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, UpdateZoneBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = UpdateZoneBodyCustomFields.from_dict(_custom_fields)

        update_zone_body = cls(
            zone_name=zone_name,
            zone_type=zone_type,
            temperature_controlled=temperature_controlled,
            temperature_range=temperature_range,
            capacity_cubic_feet=capacity_cubic_feet,
            custom_fields=custom_fields,
        )

        update_zone_body.additional_properties = d
        return update_zone_body

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
