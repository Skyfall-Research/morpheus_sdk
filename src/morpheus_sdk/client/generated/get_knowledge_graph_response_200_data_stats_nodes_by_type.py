from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetKnowledgeGraphResponse200DataStatsNodesByType")


@_attrs_define
class GetKnowledgeGraphResponse200DataStatsNodesByType:
    """Count of nodes by type

    Attributes:
        persona (Union[Unset, int]):  Example: 3.
        capability (Union[Unset, int]):  Example: 5.
        od (Union[Unset, int]):  Example: 8.
        tool (Union[Unset, int]):  Example: 15.
        service (Union[Unset, int]):  Example: 4.
        entity (Union[Unset, int]):  Example: 7.
    """

    persona: Union[Unset, int] = UNSET
    capability: Union[Unset, int] = UNSET
    od: Union[Unset, int] = UNSET
    tool: Union[Unset, int] = UNSET
    service: Union[Unset, int] = UNSET
    entity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        persona = self.persona

        capability = self.capability

        od = self.od

        tool = self.tool

        service = self.service

        entity = self.entity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if persona is not UNSET:
            field_dict["PERSONA"] = persona
        if capability is not UNSET:
            field_dict["CAPABILITY"] = capability
        if od is not UNSET:
            field_dict["OD"] = od
        if tool is not UNSET:
            field_dict["TOOL"] = tool
        if service is not UNSET:
            field_dict["SERVICE"] = service
        if entity is not UNSET:
            field_dict["ENTITY"] = entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        persona = d.pop("PERSONA", UNSET)

        capability = d.pop("CAPABILITY", UNSET)

        od = d.pop("OD", UNSET)

        tool = d.pop("TOOL", UNSET)

        service = d.pop("SERVICE", UNSET)

        entity = d.pop("ENTITY", UNSET)

        get_knowledge_graph_response_200_data_stats_nodes_by_type = cls(
            persona=persona,
            capability=capability,
            od=od,
            tool=tool,
            service=service,
            entity=entity,
        )

        get_knowledge_graph_response_200_data_stats_nodes_by_type.additional_properties = d
        return get_knowledge_graph_response_200_data_stats_nodes_by_type

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
