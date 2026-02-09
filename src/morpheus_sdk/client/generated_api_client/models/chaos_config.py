from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChaosConfig")


@_attrs_define
class ChaosConfig:
    """Configuration for per-world chaos engineering settings

    Attributes:
        process_chaos_enabled (bool): Enable chaos for process execution (ODs) Default: False. Example: False.
        infra_chaos_enabled (bool): Enable chaos for infrastructure components (tools/DB) Default: False. Example:
            False.
    """

    process_chaos_enabled: bool = False
    infra_chaos_enabled: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_chaos_enabled = self.process_chaos_enabled

        infra_chaos_enabled = self.infra_chaos_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processChaosEnabled": process_chaos_enabled,
                "infraChaosEnabled": infra_chaos_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        process_chaos_enabled = d.pop("processChaosEnabled", False)

        infra_chaos_enabled = d.pop("infraChaosEnabled", False)

        chaos_config = cls(
            process_chaos_enabled=process_chaos_enabled,
            infra_chaos_enabled=infra_chaos_enabled,
        )

        chaos_config.additional_properties = d
        return chaos_config

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
