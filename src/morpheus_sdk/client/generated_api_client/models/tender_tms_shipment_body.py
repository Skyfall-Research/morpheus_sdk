from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TenderTMSShipmentBody")


@_attrs_define
class TenderTMSShipmentBody:
    """
    Attributes:
        carrier_id (str): Unique carrier identifier Example: CARRIER_FEDEX_001.
        carrier_name (str): Carrier display name Example: FedEx Freight.
        carrier_code (str): Standard carrier code Example: FDXF.
        scac_code (str): Standard Carrier Alpha Code Example: FXFE.
    """

    carrier_id: str
    carrier_name: str
    carrier_code: str
    scac_code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier_id = self.carrier_id

        carrier_name = self.carrier_name

        carrier_code = self.carrier_code

        scac_code = self.scac_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "carrierId": carrier_id,
                "carrierName": carrier_name,
                "carrierCode": carrier_code,
                "scacCode": scac_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        carrier_id = d.pop("carrierId")

        carrier_name = d.pop("carrierName")

        carrier_code = d.pop("carrierCode")

        scac_code = d.pop("scacCode")

        tender_tms_shipment_body = cls(
            carrier_id=carrier_id,
            carrier_name=carrier_name,
            carrier_code=carrier_code,
            scac_code=scac_code,
        )

        tender_tms_shipment_body.additional_properties = d
        return tender_tms_shipment_body

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
