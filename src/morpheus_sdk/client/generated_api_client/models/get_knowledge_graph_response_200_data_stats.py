from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_knowledge_graph_response_200_data_stats_nodes_by_type import (
        GetKnowledgeGraphResponse200DataStatsNodesByType,
    )


T = TypeVar("T", bound="GetKnowledgeGraphResponse200DataStats")


@_attrs_define
class GetKnowledgeGraphResponse200DataStats:
    """Graph statistics

    Attributes:
        total_nodes (Union[Unset, int]): Total number of nodes Example: 42.
        total_edges (Union[Unset, int]): Total number of edges Example: 68.
        nodes_by_type (Union[Unset, GetKnowledgeGraphResponse200DataStatsNodesByType]): Count of nodes by type
    """

    total_nodes: Union[Unset, int] = UNSET
    total_edges: Union[Unset, int] = UNSET
    nodes_by_type: Union[Unset, "GetKnowledgeGraphResponse200DataStatsNodesByType"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_nodes = self.total_nodes

        total_edges = self.total_edges

        nodes_by_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nodes_by_type, Unset):
            nodes_by_type = self.nodes_by_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_nodes is not UNSET:
            field_dict["totalNodes"] = total_nodes
        if total_edges is not UNSET:
            field_dict["totalEdges"] = total_edges
        if nodes_by_type is not UNSET:
            field_dict["nodesByType"] = nodes_by_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_knowledge_graph_response_200_data_stats_nodes_by_type import (
            GetKnowledgeGraphResponse200DataStatsNodesByType,
        )

        d = dict(src_dict)
        total_nodes = d.pop("totalNodes", UNSET)

        total_edges = d.pop("totalEdges", UNSET)

        _nodes_by_type = d.pop("nodesByType", UNSET)
        nodes_by_type: Union[Unset, GetKnowledgeGraphResponse200DataStatsNodesByType]
        if isinstance(_nodes_by_type, Unset):
            nodes_by_type = UNSET
        else:
            nodes_by_type = GetKnowledgeGraphResponse200DataStatsNodesByType.from_dict(_nodes_by_type)

        get_knowledge_graph_response_200_data_stats = cls(
            total_nodes=total_nodes,
            total_edges=total_edges,
            nodes_by_type=nodes_by_type,
        )

        get_knowledge_graph_response_200_data_stats.additional_properties = d
        return get_knowledge_graph_response_200_data_stats

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
