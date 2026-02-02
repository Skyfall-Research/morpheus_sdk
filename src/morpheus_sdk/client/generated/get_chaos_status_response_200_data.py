from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_chaos_status_response_200_data_stats import GetChaosStatusResponse200DataStats


T = TypeVar("T", bound="GetChaosStatusResponse200Data")


@_attrs_define
class GetChaosStatusResponse200Data:
    """
    Attributes:
        enabled (Union[Unset, bool]): Whether chaos engineering is currently enabled
        active_preset (Union[None, Unset, str]): The currently active chaos preset (from CHAOS_PRESET env var), or null
            if none
        stats (Union[Unset, GetChaosStatusResponse200DataStats]): Statistics about chaos configuration
    """

    enabled: Union[Unset, bool] = UNSET
    active_preset: Union[None, Unset, str] = UNSET
    stats: Union[Unset, "GetChaosStatusResponse200DataStats"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        active_preset: Union[None, Unset, str]
        if isinstance(self.active_preset, Unset):
            active_preset = UNSET
        else:
            active_preset = self.active_preset

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if active_preset is not UNSET:
            field_dict["activePreset"] = active_preset
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_chaos_status_response_200_data_stats import GetChaosStatusResponse200DataStats

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        def _parse_active_preset(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        active_preset = _parse_active_preset(d.pop("activePreset", UNSET))

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, GetChaosStatusResponse200DataStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = GetChaosStatusResponse200DataStats.from_dict(_stats)

        get_chaos_status_response_200_data = cls(
            enabled=enabled,
            active_preset=active_preset,
            stats=stats,
        )

        get_chaos_status_response_200_data.additional_properties = d
        return get_chaos_status_response_200_data

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
