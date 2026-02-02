from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundOrderWorldRef")


@_attrs_define
class WMSOutboundOrderWorldRef:
    """Multi-tenant world reference for data isolation

    Attributes:
        world_id (str): World scope identifier Example: 550e8400-e29b-41d4-a716-446655440000.
        world_name (Union[Unset, str]): Optional world display name Example: Production Environment.
    """

    world_id: str
    world_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        world_id = self.world_id

        world_name = self.world_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "worldId": world_id,
            }
        )
        if world_name is not UNSET:
            field_dict["worldName"] = world_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        world_id = d.pop("worldId")

        world_name = d.pop("worldName", UNSET)

        wms_outbound_order_world_ref = cls(
            world_id=world_id,
            world_name=world_name,
        )

        wms_outbound_order_world_ref.additional_properties = d
        return wms_outbound_order_world_ref

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
