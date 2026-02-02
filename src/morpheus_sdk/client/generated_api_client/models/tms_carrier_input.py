from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tms_carrier_input_carrier_type import TMSCarrierInputCarrierType
from ..models.tms_carrier_input_status import TMSCarrierInputStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_carrier_input_compliance import TMSCarrierInputCompliance
    from ..models.tms_carrier_input_contact import TMSCarrierInputContact
    from ..models.tms_carrier_input_custom_fields import TMSCarrierInputCustomFields
    from ..models.tms_carrier_input_performance import TMSCarrierInputPerformance


T = TypeVar("T", bound="TMSCarrierInput")


@_attrs_define
class TMSCarrierInput:
    """Input data for creating or updating a TMS carrier

    Attributes:
        carrier_code (str): Business carrier code (SCAC or internal) - must be unique Example: ACME.
        carrier_name (str): Official carrier company name Example: ACME Transportation.
        carrier_type (TMSCarrierInputCarrierType): Transportation mode and service type Example: FTL.
        status (Union[Unset, TMSCarrierInputStatus]): Initial carrier status (defaults to ACTIVE) Example: ACTIVE.
        contact (Union[Unset, TMSCarrierInputContact]): Carrier contact information
        compliance (Union[Unset, TMSCarrierInputCompliance]): Carrier compliance and certification information
        performance (Union[Unset, TMSCarrierInputPerformance]): Initial performance metrics (optional)
        service_regions (Union[Unset, list[str]]): List of service regions/states Example: ['GA', 'FL', 'SC', 'NC',
            'TN'].
        custom_fields (Union[Unset, TMSCarrierInputCustomFields]): Additional custom fields for extensibility
    """

    carrier_code: str
    carrier_name: str
    carrier_type: TMSCarrierInputCarrierType
    status: Union[Unset, TMSCarrierInputStatus] = UNSET
    contact: Union[Unset, "TMSCarrierInputContact"] = UNSET
    compliance: Union[Unset, "TMSCarrierInputCompliance"] = UNSET
    performance: Union[Unset, "TMSCarrierInputPerformance"] = UNSET
    service_regions: Union[Unset, list[str]] = UNSET
    custom_fields: Union[Unset, "TMSCarrierInputCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier_code = self.carrier_code

        carrier_name = self.carrier_name

        carrier_type = self.carrier_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        compliance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.compliance, Unset):
            compliance = self.compliance.to_dict()

        performance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.performance, Unset):
            performance = self.performance.to_dict()

        service_regions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.service_regions, Unset):
            service_regions = self.service_regions

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "carrierCode": carrier_code,
                "carrierName": carrier_name,
                "carrierType": carrier_type,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if contact is not UNSET:
            field_dict["contact"] = contact
        if compliance is not UNSET:
            field_dict["compliance"] = compliance
        if performance is not UNSET:
            field_dict["performance"] = performance
        if service_regions is not UNSET:
            field_dict["serviceRegions"] = service_regions
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_carrier_input_compliance import TMSCarrierInputCompliance
        from ..models.tms_carrier_input_contact import TMSCarrierInputContact
        from ..models.tms_carrier_input_custom_fields import TMSCarrierInputCustomFields
        from ..models.tms_carrier_input_performance import TMSCarrierInputPerformance

        d = dict(src_dict)
        carrier_code = d.pop("carrierCode")

        carrier_name = d.pop("carrierName")

        carrier_type = TMSCarrierInputCarrierType(d.pop("carrierType"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, TMSCarrierInputStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TMSCarrierInputStatus(_status)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, TMSCarrierInputContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = TMSCarrierInputContact.from_dict(_contact)

        _compliance = d.pop("compliance", UNSET)
        compliance: Union[Unset, TMSCarrierInputCompliance]
        if isinstance(_compliance, Unset):
            compliance = UNSET
        else:
            compliance = TMSCarrierInputCompliance.from_dict(_compliance)

        _performance = d.pop("performance", UNSET)
        performance: Union[Unset, TMSCarrierInputPerformance]
        if isinstance(_performance, Unset):
            performance = UNSET
        else:
            performance = TMSCarrierInputPerformance.from_dict(_performance)

        service_regions = cast(list[str], d.pop("serviceRegions", UNSET))

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, TMSCarrierInputCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = TMSCarrierInputCustomFields.from_dict(_custom_fields)

        tms_carrier_input = cls(
            carrier_code=carrier_code,
            carrier_name=carrier_name,
            carrier_type=carrier_type,
            status=status,
            contact=contact,
            compliance=compliance,
            performance=performance,
            service_regions=service_regions,
            custom_fields=custom_fields,
        )

        tms_carrier_input.additional_properties = d
        return tms_carrier_input

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
