from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_knowledge_graph_response_200_data_edges_item import GetKnowledgeGraphResponse200DataEdgesItem
    from ..models.get_knowledge_graph_response_200_data_nodes_item import GetKnowledgeGraphResponse200DataNodesItem
    from ..models.get_knowledge_graph_response_200_data_stats import GetKnowledgeGraphResponse200DataStats


T = TypeVar("T", bound="GetKnowledgeGraphResponse200Data")


@_attrs_define
class GetKnowledgeGraphResponse200Data:
    """
    Attributes:
        nodes (list['GetKnowledgeGraphResponse200DataNodesItem']): Array of graph nodes
        edges (list['GetKnowledgeGraphResponse200DataEdgesItem']): Array of graph edges
        stats (GetKnowledgeGraphResponse200DataStats): Graph statistics
        filtered (bool): Whether the graph was filtered by capabilities Example: True.
        seed_o_ds (Union[Unset, list[str]]): OD IDs used as seeds for filtering (only present when filtered) Example:
            ['shipment-tracking', 'inventory-check'].
        message (Union[Unset, str]): Info message (only present when not filtered) Example: No capabilities assigned to
            this world. Showing full graph..
    """

    nodes: list["GetKnowledgeGraphResponse200DataNodesItem"]
    edges: list["GetKnowledgeGraphResponse200DataEdgesItem"]
    stats: "GetKnowledgeGraphResponse200DataStats"
    filtered: bool
    seed_o_ds: Union[Unset, list[str]] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()
            edges.append(edges_item)

        stats = self.stats.to_dict()

        filtered = self.filtered

        seed_o_ds: Union[Unset, list[str]] = UNSET
        if not isinstance(self.seed_o_ds, Unset):
            seed_o_ds = self.seed_o_ds

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodes": nodes,
                "edges": edges,
                "stats": stats,
                "filtered": filtered,
            }
        )
        if seed_o_ds is not UNSET:
            field_dict["seedODs"] = seed_o_ds
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_knowledge_graph_response_200_data_edges_item import GetKnowledgeGraphResponse200DataEdgesItem
        from ..models.get_knowledge_graph_response_200_data_nodes_item import GetKnowledgeGraphResponse200DataNodesItem
        from ..models.get_knowledge_graph_response_200_data_stats import GetKnowledgeGraphResponse200DataStats

        d = dict(src_dict)
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = GetKnowledgeGraphResponse200DataNodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        edges = []
        _edges = d.pop("edges")
        for edges_item_data in _edges:
            edges_item = GetKnowledgeGraphResponse200DataEdgesItem.from_dict(edges_item_data)

            edges.append(edges_item)

        stats = GetKnowledgeGraphResponse200DataStats.from_dict(d.pop("stats"))

        filtered = d.pop("filtered")

        seed_o_ds = cast(list[str], d.pop("seedODs", UNSET))

        message = d.pop("message", UNSET)

        get_knowledge_graph_response_200_data = cls(
            nodes=nodes,
            edges=edges,
            stats=stats,
            filtered=filtered,
            seed_o_ds=seed_o_ds,
            message=message,
        )

        get_knowledge_graph_response_200_data.additional_properties = d
        return get_knowledge_graph_response_200_data

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
