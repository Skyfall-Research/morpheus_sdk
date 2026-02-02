from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_inbound_trailer_facility_info_address import TMSInboundTrailerFacilityInfoAddress


T = TypeVar("T", bound="TMSInboundTrailerFacilityInfo")


@_attrs_define
class TMSInboundTrailerFacilityInfo:
    """Distribution center and facility details

    Attributes:
        dc_id (Union[Unset, str]): Distribution center identifier Example: DC_ATL_001.
        facility_name (Union[Unset, str]): Facility name Example: Atlanta Distribution Center.
        address (Union[Unset, TMSInboundTrailerFacilityInfoAddress]): Facility address information
    """

    dc_id: Union[Unset, str] = UNSET
    facility_name: Union[Unset, str] = UNSET
    address: Union[Unset, "TMSInboundTrailerFacilityInfoAddress"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dc_id = self.dc_id

        facility_name = self.facility_name

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dc_id is not UNSET:
            field_dict["dcId"] = dc_id
        if facility_name is not UNSET:
            field_dict["facilityName"] = facility_name
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_inbound_trailer_facility_info_address import TMSInboundTrailerFacilityInfoAddress

        d = dict(src_dict)
        dc_id = d.pop("dcId", UNSET)

        facility_name = d.pop("facilityName", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, TMSInboundTrailerFacilityInfoAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = TMSInboundTrailerFacilityInfoAddress.from_dict(_address)

        tms_inbound_trailer_facility_info = cls(
            dc_id=dc_id,
            facility_name=facility_name,
            address=address,
        )

        tms_inbound_trailer_facility_info.additional_properties = d
        return tms_inbound_trailer_facility_info

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
