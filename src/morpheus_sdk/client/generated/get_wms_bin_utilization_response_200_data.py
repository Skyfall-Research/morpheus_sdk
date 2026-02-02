from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_bin_utilization_response_200_data_by_zone_item import (
        GetWMSBinUtilizationResponse200DataByZoneItem,
    )
    from ..models.get_wms_bin_utilization_response_200_data_capacity import GetWMSBinUtilizationResponse200DataCapacity
    from ..models.get_wms_bin_utilization_response_200_data_overall import GetWMSBinUtilizationResponse200DataOverall


T = TypeVar("T", bound="GetWMSBinUtilizationResponse200Data")


@_attrs_define
class GetWMSBinUtilizationResponse200Data:
    """
    Attributes:
        overall (Union[Unset, GetWMSBinUtilizationResponse200DataOverall]):
        by_zone (Union[Unset, list['GetWMSBinUtilizationResponse200DataByZoneItem']]):
        capacity (Union[Unset, GetWMSBinUtilizationResponse200DataCapacity]):
    """

    overall: Union[Unset, "GetWMSBinUtilizationResponse200DataOverall"] = UNSET
    by_zone: Union[Unset, list["GetWMSBinUtilizationResponse200DataByZoneItem"]] = UNSET
    capacity: Union[Unset, "GetWMSBinUtilizationResponse200DataCapacity"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overall: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.overall, Unset):
            overall = self.overall.to_dict()

        by_zone: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.by_zone, Unset):
            by_zone = []
            for by_zone_item_data in self.by_zone:
                by_zone_item = by_zone_item_data.to_dict()
                by_zone.append(by_zone_item)

        capacity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capacity, Unset):
            capacity = self.capacity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overall is not UNSET:
            field_dict["overall"] = overall
        if by_zone is not UNSET:
            field_dict["byZone"] = by_zone
        if capacity is not UNSET:
            field_dict["capacity"] = capacity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_bin_utilization_response_200_data_by_zone_item import (
            GetWMSBinUtilizationResponse200DataByZoneItem,
        )
        from ..models.get_wms_bin_utilization_response_200_data_capacity import (
            GetWMSBinUtilizationResponse200DataCapacity,
        )
        from ..models.get_wms_bin_utilization_response_200_data_overall import (
            GetWMSBinUtilizationResponse200DataOverall,
        )

        d = dict(src_dict)
        _overall = d.pop("overall", UNSET)
        overall: Union[Unset, GetWMSBinUtilizationResponse200DataOverall]
        if isinstance(_overall, Unset):
            overall = UNSET
        else:
            overall = GetWMSBinUtilizationResponse200DataOverall.from_dict(_overall)

        by_zone = []
        _by_zone = d.pop("byZone", UNSET)
        for by_zone_item_data in _by_zone or []:
            by_zone_item = GetWMSBinUtilizationResponse200DataByZoneItem.from_dict(by_zone_item_data)

            by_zone.append(by_zone_item)

        _capacity = d.pop("capacity", UNSET)
        capacity: Union[Unset, GetWMSBinUtilizationResponse200DataCapacity]
        if isinstance(_capacity, Unset):
            capacity = UNSET
        else:
            capacity = GetWMSBinUtilizationResponse200DataCapacity.from_dict(_capacity)

        get_wms_bin_utilization_response_200_data = cls(
            overall=overall,
            by_zone=by_zone,
            capacity=capacity,
        )

        get_wms_bin_utilization_response_200_data.additional_properties = d
        return get_wms_bin_utilization_response_200_data

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
