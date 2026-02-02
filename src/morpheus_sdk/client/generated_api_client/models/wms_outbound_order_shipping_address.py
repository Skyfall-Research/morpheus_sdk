from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundOrderShippingAddress")


@_attrs_define
class WMSOutboundOrderShippingAddress:
    """Required delivery destination

    Attributes:
        street1 (str): Primary address line Example: 123 Main Street.
        city (str): City name Example: Anytown.
        state (str): State/province code Example: CA.
        zip_code (str): Postal code Example: 90210.
        country (str): Country code Example: USA.
        street2 (Union[Unset, str]): Secondary address line (optional) Example: Suite 456.
    """

    street1: str
    city: str
    state: str
    zip_code: str
    country: str
    street2: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street1 = self.street1

        city = self.city

        state = self.state

        zip_code = self.zip_code

        country = self.country

        street2 = self.street2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "street1": street1,
                "city": city,
                "state": state,
                "zipCode": zip_code,
                "country": country,
            }
        )
        if street2 is not UNSET:
            field_dict["street2"] = street2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street1 = d.pop("street1")

        city = d.pop("city")

        state = d.pop("state")

        zip_code = d.pop("zipCode")

        country = d.pop("country")

        street2 = d.pop("street2", UNSET)

        wms_outbound_order_shipping_address = cls(
            street1=street1,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            street2=street2,
        )

        wms_outbound_order_shipping_address.additional_properties = d
        return wms_outbound_order_shipping_address

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
