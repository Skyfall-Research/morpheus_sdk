from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSInboundTrailerWorldRef")


@_attrs_define
class TMSInboundTrailerWorldRef:
    """World reference information

    Attributes:
        world_id (Union[Unset, str]): World identifier Example: 507f1f77bcf86cd799439011.
        dc_id (Union[Unset, str]): Distribution center context Example: DC_ATL_001.
    """

    world_id: Union[Unset, str] = UNSET
    dc_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        world_id = self.world_id

        dc_id = self.dc_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if world_id is not UNSET:
            field_dict["worldId"] = world_id
        if dc_id is not UNSET:
            field_dict["dcId"] = dc_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        world_id = d.pop("worldId", UNSET)

        dc_id = d.pop("dcId", UNSET)

        tms_inbound_trailer_world_ref = cls(
            world_id=world_id,
            dc_id=dc_id,
        )

        tms_inbound_trailer_world_ref.additional_properties = d
        return tms_inbound_trailer_world_ref

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
