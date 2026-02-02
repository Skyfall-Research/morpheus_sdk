from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_world_layout_by_id_response_200_data_docs import GetWorldLayoutByIdResponse200DataDocs


T = TypeVar("T", bound="GetWorldLayoutByIdResponse200Data")


@_attrs_define
class GetWorldLayoutByIdResponse200Data:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        short_description (Union[Unset, str]):
        docs (Union[Unset, GetWorldLayoutByIdResponse200DataDocs]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    short_description: Union[Unset, str] = UNSET
    docs: Union[Unset, "GetWorldLayoutByIdResponse200DataDocs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        short_description = self.short_description

        docs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.docs, Unset):
            docs = self.docs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if short_description is not UNSET:
            field_dict["shortDescription"] = short_description
        if docs is not UNSET:
            field_dict["docs"] = docs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_world_layout_by_id_response_200_data_docs import GetWorldLayoutByIdResponse200DataDocs

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        short_description = d.pop("shortDescription", UNSET)

        _docs = d.pop("docs", UNSET)
        docs: Union[Unset, GetWorldLayoutByIdResponse200DataDocs]
        if isinstance(_docs, Unset):
            docs = UNSET
        else:
            docs = GetWorldLayoutByIdResponse200DataDocs.from_dict(_docs)

        get_world_layout_by_id_response_200_data = cls(
            id=id,
            name=name,
            description=description,
            short_description=short_description,
            docs=docs,
        )

        get_world_layout_by_id_response_200_data.additional_properties = d
        return get_world_layout_by_id_response_200_data

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
