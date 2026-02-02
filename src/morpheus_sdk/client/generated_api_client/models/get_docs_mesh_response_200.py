from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_docs_mesh_response_200_endpoints_item import GetDocsMeshResponse200EndpointsItem
    from ..models.get_docs_mesh_response_200_filters import GetDocsMeshResponse200Filters


T = TypeVar("T", bound="GetDocsMeshResponse200")


@_attrs_define
class GetDocsMeshResponse200:
    """
    Attributes:
        service (Union[Unset, str]):  Example: wms.
        filters (Union[Unset, GetDocsMeshResponse200Filters]):
        count (Union[Unset, float]):  Example: 1.
        endpoints (Union[Unset, list['GetDocsMeshResponse200EndpointsItem']]):
    """

    service: Union[Unset, str] = UNSET
    filters: Union[Unset, "GetDocsMeshResponse200Filters"] = UNSET
    count: Union[Unset, float] = UNSET
    endpoints: Union[Unset, list["GetDocsMeshResponse200EndpointsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service = self.service

        filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        count = self.count

        endpoints: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = []
            for endpoints_item_data in self.endpoints:
                endpoints_item = endpoints_item_data.to_dict()
                endpoints.append(endpoints_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if filters is not UNSET:
            field_dict["filters"] = filters
        if count is not UNSET:
            field_dict["count"] = count
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_docs_mesh_response_200_endpoints_item import GetDocsMeshResponse200EndpointsItem
        from ..models.get_docs_mesh_response_200_filters import GetDocsMeshResponse200Filters

        d = dict(src_dict)
        service = d.pop("service", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, GetDocsMeshResponse200Filters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = GetDocsMeshResponse200Filters.from_dict(_filters)

        count = d.pop("count", UNSET)

        endpoints = []
        _endpoints = d.pop("endpoints", UNSET)
        for endpoints_item_data in _endpoints or []:
            endpoints_item = GetDocsMeshResponse200EndpointsItem.from_dict(endpoints_item_data)

            endpoints.append(endpoints_item)

        get_docs_mesh_response_200 = cls(
            service=service,
            filters=filters,
            count=count,
            endpoints=endpoints,
        )

        get_docs_mesh_response_200.additional_properties = d
        return get_docs_mesh_response_200

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
