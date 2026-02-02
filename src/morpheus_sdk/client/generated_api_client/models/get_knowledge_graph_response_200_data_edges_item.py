from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_knowledge_graph_response_200_data_edges_item_type import GetKnowledgeGraphResponse200DataEdgesItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_knowledge_graph_response_200_data_edges_item_metadata import (
        GetKnowledgeGraphResponse200DataEdgesItemMetadata,
    )


T = TypeVar("T", bound="GetKnowledgeGraphResponse200DataEdgesItem")


@_attrs_define
class GetKnowledgeGraphResponse200DataEdgesItem:
    """
    Attributes:
        from_ (str): Source node ID Example: od:shipment-tracking.
        to (str): Target node ID Example: tool:getShipmentStatus.
        type_ (GetKnowledgeGraphResponse200DataEdgesItemType): Edge relationship type Example: uses.
        metadata (Union[Unset, GetKnowledgeGraphResponse200DataEdgesItemMetadata]): Optional metadata
    """

    from_: str
    to: str
    type_: GetKnowledgeGraphResponse200DataEdgesItemType
    metadata: Union[Unset, "GetKnowledgeGraphResponse200DataEdgesItemMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        type_ = self.type_.value

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "type": type_,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_knowledge_graph_response_200_data_edges_item_metadata import (
            GetKnowledgeGraphResponse200DataEdgesItemMetadata,
        )

        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        type_ = GetKnowledgeGraphResponse200DataEdgesItemType(d.pop("type"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GetKnowledgeGraphResponse200DataEdgesItemMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GetKnowledgeGraphResponse200DataEdgesItemMetadata.from_dict(_metadata)

        get_knowledge_graph_response_200_data_edges_item = cls(
            from_=from_,
            to=to,
            type_=type_,
            metadata=metadata,
        )

        get_knowledge_graph_response_200_data_edges_item.additional_properties = d
        return get_knowledge_graph_response_200_data_edges_item

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
