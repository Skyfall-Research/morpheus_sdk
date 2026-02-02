from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.capability_filter_complexity import CapabilityFilterComplexity
from ..types import UNSET, Unset

T = TypeVar("T", bound="CapabilityFilter")


@_attrs_define
class CapabilityFilter:
    """Filter criteria for capability sampling

    Attributes:
        domain (Union[Unset, list[str]]): Filter by domain names Example: ['order-management', 'inventory'].
        complexity (Union[Unset, CapabilityFilterComplexity]): Filter by complexity level
        services (Union[Unset, list[str]]): Filter by required services Example: ['erp', 'wms'].
        personas (Union[Unset, list[str]]): Filter by associated personas Example: ['warehouse-manager', 'procurement-
            officer'].
        patterns (Union[Unset, list[str]]): Filter by capability patterns Example: ['crud', 'workflow'].
    """

    domain: Union[Unset, list[str]] = UNSET
    complexity: Union[Unset, CapabilityFilterComplexity] = UNSET
    services: Union[Unset, list[str]] = UNSET
    personas: Union[Unset, list[str]] = UNSET
    patterns: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain: Union[Unset, list[str]] = UNSET
        if not isinstance(self.domain, Unset):
            domain = self.domain

        complexity: Union[Unset, str] = UNSET
        if not isinstance(self.complexity, Unset):
            complexity = self.complexity.value

        services: Union[Unset, list[str]] = UNSET
        if not isinstance(self.services, Unset):
            services = self.services

        personas: Union[Unset, list[str]] = UNSET
        if not isinstance(self.personas, Unset):
            personas = self.personas

        patterns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.patterns, Unset):
            patterns = self.patterns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if complexity is not UNSET:
            field_dict["complexity"] = complexity
        if services is not UNSET:
            field_dict["services"] = services
        if personas is not UNSET:
            field_dict["personas"] = personas
        if patterns is not UNSET:
            field_dict["patterns"] = patterns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = cast(list[str], d.pop("domain", UNSET))

        _complexity = d.pop("complexity", UNSET)
        complexity: Union[Unset, CapabilityFilterComplexity]
        if isinstance(_complexity, Unset):
            complexity = UNSET
        else:
            complexity = CapabilityFilterComplexity(_complexity)

        services = cast(list[str], d.pop("services", UNSET))

        personas = cast(list[str], d.pop("personas", UNSET))

        patterns = cast(list[str], d.pop("patterns", UNSET))

        capability_filter = cls(
            domain=domain,
            complexity=complexity,
            services=services,
            personas=personas,
            patterns=patterns,
        )

        capability_filter.additional_properties = d
        return capability_filter

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
