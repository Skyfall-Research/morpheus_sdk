from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundShipmentToAddress")


@_attrs_define
class WMSOutboundShipmentToAddress:
    """Required destination address (validated in repository)

    Attributes:
        street1 (str): Street address Example: 123 Customer Ave.
        city (str): City name Example: Miami.
        state (str): State/province Example: FL.
        postal_code (str): Postal code Example: 33101.
        country (Union[Unset, str]): Country code Example: USA.
    """

    street1: str
    city: str
    state: str
    postal_code: str
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
        field_dict.update(
            {
                "street1": street1,
                "city": city,
                "state": state,
                "postalCode": postal_code,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street1 = d.pop("street1")

        city = d.pop("city")

        state = d.pop("state")

        postal_code = d.pop("postalCode")

        country = d.pop("country", UNSET)

        wms_outbound_shipment_to_address = cls(
            street1=street1,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
        )

        wms_outbound_shipment_to_address.additional_properties = d
        return wms_outbound_shipment_to_address

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
