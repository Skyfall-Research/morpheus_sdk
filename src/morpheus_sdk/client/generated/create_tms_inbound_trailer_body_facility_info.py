from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTMSInboundTrailerBodyFacilityInfo")


@_attrs_define
class CreateTMSInboundTrailerBodyFacilityInfo:
    """
    Attributes:
        dc_id (str): Distribution center identifier Example: DC_ATL_001.
        facility_name (Union[Unset, str]): Facility name Example: Atlanta Distribution Center.
    """

    dc_id: str
    facility_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dc_id = self.dc_id

        facility_name = self.facility_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dcId": dc_id,
            }
        )
        if facility_name is not UNSET:
            field_dict["facilityName"] = facility_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dc_id = d.pop("dcId")

        facility_name = d.pop("facilityName", UNSET)

        create_tms_inbound_trailer_body_facility_info = cls(
            dc_id=dc_id,
            facility_name=facility_name,
        )

        create_tms_inbound_trailer_body_facility_info.additional_properties = d
        return create_tms_inbound_trailer_body_facility_info

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
