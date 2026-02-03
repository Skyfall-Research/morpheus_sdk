from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundShipmentFromAddress")


@_attrs_define
class WMSOutboundShipmentFromAddress:
    """Origin address (typically warehouse)

    Attributes:
        street1 (Union[Unset, str]): Street address Example: 100 Warehouse Blvd.
        city (Union[Unset, str]): City name Example: Atlanta.
        state (Union[Unset, str]): State/province Example: GA.
        postal_code (Union[Unset, str]): Postal code Example: 30309.
        country (Union[Unset, str]): Country code Example: USA.
    """

    street1: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street1 = self.street1

        city = self.city

        state = self.state

        postal_code = self.postal_code

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street1 = d.pop("street1", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        country = d.pop("country", UNSET)

        wms_outbound_shipment_from_address = cls(
            street1=street1,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
        )

        wms_outbound_shipment_from_address.additional_properties = d
        return wms_outbound_shipment_from_address

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
