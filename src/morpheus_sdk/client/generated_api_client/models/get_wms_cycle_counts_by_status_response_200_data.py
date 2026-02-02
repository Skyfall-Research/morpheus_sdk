from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_cycle_counts_by_status_response_200_data_pagination import (
        GetWMSCycleCountsByStatusResponse200DataPagination,
    )
    from ..models.wms_cycle_count import WMSCycleCount


T = TypeVar("T", bound="GetWMSCycleCountsByStatusResponse200Data")


@_attrs_define
class GetWMSCycleCountsByStatusResponse200Data:
    """
    Attributes:
        counts (Union[Unset, list['WMSCycleCount']]):
        pagination (Union[Unset, GetWMSCycleCountsByStatusResponse200DataPagination]):
    """

    counts: Union[Unset, list["WMSCycleCount"]] = UNSET
    pagination: Union[Unset, "GetWMSCycleCountsByStatusResponse200DataPagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = []
            for counts_item_data in self.counts:
                counts_item = counts_item_data.to_dict()
                counts.append(counts_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counts is not UNSET:
            field_dict["counts"] = counts
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_cycle_counts_by_status_response_200_data_pagination import (
            GetWMSCycleCountsByStatusResponse200DataPagination,
        )
        from ..models.wms_cycle_count import WMSCycleCount

        d = dict(src_dict)
        counts = []
        _counts = d.pop("counts", UNSET)
        for counts_item_data in _counts or []:
            counts_item = WMSCycleCount.from_dict(counts_item_data)

            counts.append(counts_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, GetWMSCycleCountsByStatusResponse200DataPagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = GetWMSCycleCountsByStatusResponse200DataPagination.from_dict(_pagination)

        get_wms_cycle_counts_by_status_response_200_data = cls(
            counts=counts,
            pagination=pagination,
        )

        get_wms_cycle_counts_by_status_response_200_data.additional_properties = d
        return get_wms_cycle_counts_by_status_response_200_data

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
