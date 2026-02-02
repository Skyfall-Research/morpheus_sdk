from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetChaosStatusResponse200DataStats")


@_attrs_define
class GetChaosStatusResponse200DataStats:
    """Statistics about chaos configuration

    Attributes:
        preset_count (Union[Unset, int]): Number of available presets
        world_policy_count (Union[Unset, int]): Number of world-level policies configured
        capability_override_count (Union[Unset, int]): Number of capability-level overrides configured
        od_override_count (Union[Unset, int]): Number of OD-level overrides configured
    """

    preset_count: Union[Unset, int] = UNSET
    world_policy_count: Union[Unset, int] = UNSET
    capability_override_count: Union[Unset, int] = UNSET
    od_override_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preset_count = self.preset_count

        world_policy_count = self.world_policy_count

        capability_override_count = self.capability_override_count

        od_override_count = self.od_override_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preset_count is not UNSET:
            field_dict["presetCount"] = preset_count
        if world_policy_count is not UNSET:
            field_dict["worldPolicyCount"] = world_policy_count
        if capability_override_count is not UNSET:
            field_dict["capabilityOverrideCount"] = capability_override_count
        if od_override_count is not UNSET:
            field_dict["odOverrideCount"] = od_override_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        preset_count = d.pop("presetCount", UNSET)

        world_policy_count = d.pop("worldPolicyCount", UNSET)

        capability_override_count = d.pop("capabilityOverrideCount", UNSET)

        od_override_count = d.pop("odOverrideCount", UNSET)

        get_chaos_status_response_200_data_stats = cls(
            preset_count=preset_count,
            world_policy_count=world_policy_count,
            capability_override_count=capability_override_count,
            od_override_count=od_override_count,
        )

        get_chaos_status_response_200_data_stats.additional_properties = d
        return get_chaos_status_response_200_data_stats

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
