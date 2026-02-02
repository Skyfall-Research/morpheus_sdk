from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_world_capabilities_response_200_data_capabilities_item_tags import (
        GetWorldCapabilitiesResponse200DataCapabilitiesItemTags,
    )


T = TypeVar("T", bound="GetWorldCapabilitiesResponse200DataCapabilitiesItem")


@_attrs_define
class GetWorldCapabilitiesResponse200DataCapabilitiesItem:
    """
    Attributes:
        id (Union[Unset, str]): Capability ID
        name (Union[Unset, str]): Capability name
        description (Union[Unset, str]): Capability description
        domain (Union[Unset, str]): Business domain
        od_id (Union[Unset, str]): Associated Operational Descriptor ID
        tags (Union[Unset, GetWorldCapabilitiesResponse200DataCapabilitiesItemTags]): Capability metadata tags
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    od_id: Union[Unset, str] = UNSET
    tags: Union[Unset, "GetWorldCapabilitiesResponse200DataCapabilitiesItemTags"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        domain = self.domain

        od_id = self.od_id

        tags: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if domain is not UNSET:
            field_dict["domain"] = domain
        if od_id is not UNSET:
            field_dict["odId"] = od_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_world_capabilities_response_200_data_capabilities_item_tags import (
            GetWorldCapabilitiesResponse200DataCapabilitiesItemTags,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        domain = d.pop("domain", UNSET)

        od_id = d.pop("odId", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, GetWorldCapabilitiesResponse200DataCapabilitiesItemTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = GetWorldCapabilitiesResponse200DataCapabilitiesItemTags.from_dict(_tags)

        get_world_capabilities_response_200_data_capabilities_item = cls(
            id=id,
            name=name,
            description=description,
            domain=domain,
            od_id=od_id,
            tags=tags,
        )

        get_world_capabilities_response_200_data_capabilities_item.additional_properties = d
        return get_world_capabilities_response_200_data_capabilities_item

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
