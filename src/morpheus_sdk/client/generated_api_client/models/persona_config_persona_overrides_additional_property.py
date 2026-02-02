from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonaConfigPersonaOverridesAdditionalProperty")


@_attrs_define
class PersonaConfigPersonaOverridesAdditionalProperty:
    """
    Attributes:
        capability_ids (Union[Unset, list[str]]): Capability IDs assigned to this persona
    """

    capability_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capability_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.capability_ids, Unset):
            capability_ids = self.capability_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capability_ids is not UNSET:
            field_dict["capabilityIds"] = capability_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        capability_ids = cast(list[str], d.pop("capabilityIds", UNSET))

        persona_config_persona_overrides_additional_property = cls(
            capability_ids=capability_ids,
        )

        persona_config_persona_overrides_additional_property.additional_properties = d
        return persona_config_persona_overrides_additional_property

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
