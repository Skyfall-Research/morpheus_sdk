from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chaos_policy import ChaosPolicy


T = TypeVar("T", bound="GetWorldChaosResponse200Data")


@_attrs_define
class GetWorldChaosResponse200Data:
    """
    Attributes:
        world_id (str): World unique identifier Example: 507f1f77bcf86cd799439011.
        world_name (str): World display name Example: Production Environment.
        chaos (ChaosPolicy): Chaos engineering policy for injecting failures and anomalies
    """

    world_id: str
    world_name: str
    chaos: "ChaosPolicy"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        world_id = self.world_id

        world_name = self.world_name

        chaos = self.chaos.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "worldId": world_id,
                "worldName": world_name,
                "chaos": chaos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chaos_policy import ChaosPolicy

        d = dict(src_dict)
        world_id = d.pop("worldId")

        world_name = d.pop("worldName")

        chaos = ChaosPolicy.from_dict(d.pop("chaos"))

        get_world_chaos_response_200_data = cls(
            world_id=world_id,
            world_name=world_name,
            chaos=chaos,
        )

        get_world_chaos_response_200_data.additional_properties = d
        return get_world_chaos_response_200_data

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
