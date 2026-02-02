from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ERPProductWorldRef")


@_attrs_define
class ERPProductWorldRef:
    """Reference to the world this product belongs to

    Attributes:
        world_id (UUID): Unique identifier of the world Example: 550e8400-e29b-41d4-a716-446655440000.
    """

    world_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        world_id = str(self.world_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "worldId": world_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        world_id = UUID(d.pop("worldId"))

        erp_product_world_ref = cls(
            world_id=world_id,
        )

        erp_product_world_ref.additional_properties = d
        return erp_product_world_ref

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
