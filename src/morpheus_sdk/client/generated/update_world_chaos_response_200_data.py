from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chaos_policy import ChaosPolicy


T = TypeVar("T", bound="UpdateWorldChaosResponse200Data")


@_attrs_define
class UpdateWorldChaosResponse200Data:
    """
    Attributes:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        chaos (ChaosPolicy): Chaos engineering policy for injecting failures and anomalies
        message (str):  Example: World chaos configuration updated successfully.
    """

    world_id: str
    chaos: "ChaosPolicy"
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        world_id = self.world_id

        chaos = self.chaos.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "worldId": world_id,
                "chaos": chaos,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chaos_policy import ChaosPolicy

        d = dict(src_dict)
        world_id = d.pop("worldId")

        chaos = ChaosPolicy.from_dict(d.pop("chaos"))

        message = d.pop("message")

        update_world_chaos_response_200_data = cls(
            world_id=world_id,
            chaos=chaos,
            message=message,
        )

        update_world_chaos_response_200_data.additional_properties = d
        return update_world_chaos_response_200_data

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
