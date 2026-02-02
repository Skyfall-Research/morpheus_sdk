from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_location_address import TMSLocationAddress
    from ..models.tms_location_coordinates import TMSLocationCoordinates


T = TypeVar("T", bound="TMSLocation")


@_attrs_define
class TMSLocation:
    """Complete location information for TMS operations

    Attributes:
        location_name (str):  Example: Main Distribution Center.
        address (TMSLocationAddress): Physical address of the location
        location_id (Union[Unset, str]):  Example: DC_001.
        coordinates (Union[Unset, TMSLocationCoordinates]): Geographic coordinates of the location
        contact_name (Union[Unset, str]): Name of the primary contact at this location Example: Shipping Manager.
        contact_phone (Union[Unset, str]): Phone number for the primary contact Example: 555-0123.
    """

    location_name: str
    address: "TMSLocationAddress"
    location_id: Union[Unset, str] = UNSET
    coordinates: Union[Unset, "TMSLocationCoordinates"] = UNSET
    contact_name: Union[Unset, str] = UNSET
    contact_phone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_name = self.location_name

        address = self.address.to_dict()

        location_id = self.location_id

        coordinates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates.to_dict()

        contact_name = self.contact_name

        contact_phone = self.contact_phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locationName": location_name,
                "address": address,
            }
        )
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if contact_phone is not UNSET:
            field_dict["contactPhone"] = contact_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_location_address import TMSLocationAddress
        from ..models.tms_location_coordinates import TMSLocationCoordinates

        d = dict(src_dict)
        location_name = d.pop("locationName")

        address = TMSLocationAddress.from_dict(d.pop("address"))

        location_id = d.pop("locationId", UNSET)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: Union[Unset, TMSLocationCoordinates]
        if isinstance(_coordinates, Unset):
            coordinates = UNSET
        else:
            coordinates = TMSLocationCoordinates.from_dict(_coordinates)

        contact_name = d.pop("contactName", UNSET)

        contact_phone = d.pop("contactPhone", UNSET)

        tms_location = cls(
            location_name=location_name,
            address=address,
            location_id=location_id,
            coordinates=coordinates,
            contact_name=contact_name,
            contact_phone=contact_phone,
        )

        tms_location.additional_properties = d
        return tms_location

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
