from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.persona_config_persona_overrides import PersonaConfigPersonaOverrides


T = TypeVar("T", bound="PersonaConfig")


@_attrs_define
class PersonaConfig:
    """Configuration for personas allowed to access this world

    Attributes:
        allowed_personas (Union[Unset, list[str]]): List of persona IDs that can access this world. If not specified,
            all personas have access. Example: ['warehouse-manager', 'procurement-officer', 'sales-rep'].
        persona_overrides (Union[Unset, PersonaConfigPersonaOverrides]): Custom persona-to-capability mappings that
            override defaults Example: {'warehouse-manager': {'capabilityIds': ['cap_inventory_check',
            'cap_stock_transfer']}}.
    """

    allowed_personas: Union[Unset, list[str]] = UNSET
    persona_overrides: Union[Unset, "PersonaConfigPersonaOverrides"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_personas: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_personas, Unset):
            allowed_personas = self.allowed_personas

        persona_overrides: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.persona_overrides, Unset):
            persona_overrides = self.persona_overrides.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_personas is not UNSET:
            field_dict["allowedPersonas"] = allowed_personas
        if persona_overrides is not UNSET:
            field_dict["personaOverrides"] = persona_overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persona_config_persona_overrides import PersonaConfigPersonaOverrides

        d = dict(src_dict)
        allowed_personas = cast(list[str], d.pop("allowedPersonas", UNSET))

        _persona_overrides = d.pop("personaOverrides", UNSET)
        persona_overrides: Union[Unset, PersonaConfigPersonaOverrides]
        if isinstance(_persona_overrides, Unset):
            persona_overrides = UNSET
        else:
            persona_overrides = PersonaConfigPersonaOverrides.from_dict(_persona_overrides)

        persona_config = cls(
            allowed_personas=allowed_personas,
            persona_overrides=persona_overrides,
        )

        persona_config.additional_properties = d
        return persona_config

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
