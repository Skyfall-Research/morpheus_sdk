from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_knowledge_graph_response_200_data_nodes_item_type import GetKnowledgeGraphResponse200DataNodesItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_knowledge_graph_response_200_data_nodes_item_metadata import (
        GetKnowledgeGraphResponse200DataNodesItemMetadata,
    )


T = TypeVar("T", bound="GetKnowledgeGraphResponse200DataNodesItem")


@_attrs_define
class GetKnowledgeGraphResponse200DataNodesItem:
    """
    Attributes:
        id (str): Unique node identifier Example: od:shipment-tracking.
        type_ (GetKnowledgeGraphResponse200DataNodesItemType): Node type Example: OD.
        label (str): Human-readable label Example: Shipment Tracking.
        metadata (Union[Unset, GetKnowledgeGraphResponse200DataNodesItemMetadata]): Optional metadata
    """

    id: str
    type_: GetKnowledgeGraphResponse200DataNodesItemType
    label: str
    metadata: Union[Unset, "GetKnowledgeGraphResponse200DataNodesItemMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        label = self.label

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "label": label,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_knowledge_graph_response_200_data_nodes_item_metadata import (
            GetKnowledgeGraphResponse200DataNodesItemMetadata,
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = GetKnowledgeGraphResponse200DataNodesItemType(d.pop("type"))

        label = d.pop("label")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GetKnowledgeGraphResponse200DataNodesItemMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GetKnowledgeGraphResponse200DataNodesItemMetadata.from_dict(_metadata)

        get_knowledge_graph_response_200_data_nodes_item = cls(
            id=id,
            type_=type_,
            label=label,
            metadata=metadata,
        )

        get_knowledge_graph_response_200_data_nodes_item.additional_properties = d
        return get_knowledge_graph_response_200_data_nodes_item

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
