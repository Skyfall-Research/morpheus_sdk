import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tms_carrier_input_compliance_safety_rating import TMSCarrierInputComplianceSafetyRating
from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSCarrierInputCompliance")


@_attrs_define
class TMSCarrierInputCompliance:
    """Carrier compliance and certification information

    Attributes:
        dot_number (Union[Unset, str]): US DOT number Example: 12345678.
        mc_number (Union[Unset, str]): Motor carrier number Example: MC-987654.
        scac_code (Union[Unset, str]): Standard Carrier Alpha Code Example: ACME.
        smart_way_certified (Union[Unset, bool]): EPA SmartWay certification status Example: True.
        insurance_expiry (Union[Unset, datetime.datetime]): Insurance policy expiration date Example:
            2025-12-31T23:59:59.999Z.
        safety_rating (Union[Unset, TMSCarrierInputComplianceSafetyRating]): FMCSA safety rating Example: SATISFACTORY.
    """

    dot_number: Union[Unset, str] = UNSET
    mc_number: Union[Unset, str] = UNSET
    scac_code: Union[Unset, str] = UNSET
    smart_way_certified: Union[Unset, bool] = UNSET
    insurance_expiry: Union[Unset, datetime.datetime] = UNSET
    safety_rating: Union[Unset, TMSCarrierInputComplianceSafetyRating] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dot_number = self.dot_number

        mc_number = self.mc_number

        scac_code = self.scac_code

        smart_way_certified = self.smart_way_certified

        insurance_expiry: Union[Unset, str] = UNSET
        if not isinstance(self.insurance_expiry, Unset):
            insurance_expiry = self.insurance_expiry.isoformat()

        safety_rating: Union[Unset, str] = UNSET
        if not isinstance(self.safety_rating, Unset):
            safety_rating = self.safety_rating.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dot_number is not UNSET:
            field_dict["dotNumber"] = dot_number
        if mc_number is not UNSET:
            field_dict["mcNumber"] = mc_number
        if scac_code is not UNSET:
            field_dict["scacCode"] = scac_code
        if smart_way_certified is not UNSET:
            field_dict["smartWayCertified"] = smart_way_certified
        if insurance_expiry is not UNSET:
            field_dict["insuranceExpiry"] = insurance_expiry
        if safety_rating is not UNSET:
            field_dict["safetyRating"] = safety_rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dot_number = d.pop("dotNumber", UNSET)

        mc_number = d.pop("mcNumber", UNSET)

        scac_code = d.pop("scacCode", UNSET)

        smart_way_certified = d.pop("smartWayCertified", UNSET)

        _insurance_expiry = d.pop("insuranceExpiry", UNSET)
        insurance_expiry: Union[Unset, datetime.datetime]
        if isinstance(_insurance_expiry, Unset):
            insurance_expiry = UNSET
        else:
            insurance_expiry = isoparse(_insurance_expiry)

        _safety_rating = d.pop("safetyRating", UNSET)
        safety_rating: Union[Unset, TMSCarrierInputComplianceSafetyRating]
        if isinstance(_safety_rating, Unset):
            safety_rating = UNSET
        else:
            safety_rating = TMSCarrierInputComplianceSafetyRating(_safety_rating)

        tms_carrier_input_compliance = cls(
            dot_number=dot_number,
            mc_number=mc_number,
            scac_code=scac_code,
            smart_way_certified=smart_way_certified,
            insurance_expiry=insurance_expiry,
            safety_rating=safety_rating,
        )

        tms_carrier_input_compliance.additional_properties = d
        return tms_carrier_input_compliance

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
