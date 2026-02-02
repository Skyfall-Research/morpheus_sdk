from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentCarrierInfo")


@_attrs_define
class TMSShipmentCarrierInfo:
    """Carrier and transportation details

    Attributes:
        carrier_id (Union[Unset, str]):  Example: CARRIER_FEDEX_001.
        carrier_name (Union[Unset, str]):  Example: FedEx Freight.
        carrier_code (Union[Unset, str]):  Example: FDXF.
        scac_code (Union[Unset, str]):  Example: FXFE.
        pro_number (Union[Unset, str]):  Example: PRO123456789.
        tracking_number (Union[Unset, str]):  Example: TRK987654321.
    """

    carrier_id: Union[Unset, str] = UNSET
    carrier_name: Union[Unset, str] = UNSET
    carrier_code: Union[Unset, str] = UNSET
    scac_code: Union[Unset, str] = UNSET
    pro_number: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier_id = self.carrier_id

        carrier_name = self.carrier_name

        carrier_code = self.carrier_code

        scac_code = self.scac_code

        pro_number = self.pro_number

        tracking_number = self.tracking_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier_id is not UNSET:
            field_dict["carrierId"] = carrier_id
        if carrier_name is not UNSET:
            field_dict["carrierName"] = carrier_name
        if carrier_code is not UNSET:
            field_dict["carrierCode"] = carrier_code
        if scac_code is not UNSET:
            field_dict["scacCode"] = scac_code
        if pro_number is not UNSET:
            field_dict["proNumber"] = pro_number
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        carrier_id = d.pop("carrierId", UNSET)

        carrier_name = d.pop("carrierName", UNSET)

        carrier_code = d.pop("carrierCode", UNSET)

        scac_code = d.pop("scacCode", UNSET)

        pro_number = d.pop("proNumber", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        tms_shipment_carrier_info = cls(
            carrier_id=carrier_id,
            carrier_name=carrier_name,
            carrier_code=carrier_code,
            scac_code=scac_code,
            pro_number=pro_number,
            tracking_number=tracking_number,
        )

        tms_shipment_carrier_info.additional_properties = d
        return tms_shipment_carrier_info

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
