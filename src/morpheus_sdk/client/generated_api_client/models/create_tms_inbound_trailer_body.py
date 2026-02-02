from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_tms_inbound_trailer_body_appointment_info import CreateTMSInboundTrailerBodyAppointmentInfo
    from ..models.create_tms_inbound_trailer_body_cargo import CreateTMSInboundTrailerBodyCargo
    from ..models.create_tms_inbound_trailer_body_carrier_info import CreateTMSInboundTrailerBodyCarrierInfo
    from ..models.create_tms_inbound_trailer_body_facility_info import CreateTMSInboundTrailerBodyFacilityInfo


T = TypeVar("T", bound="CreateTMSInboundTrailerBody")


@_attrs_define
class CreateTMSInboundTrailerBody:
    """
    Attributes:
        trailer_number (str): Physical trailer number/license plate Example: TR-12345.
        appointment_info (CreateTMSInboundTrailerBodyAppointmentInfo):
        facility_info (CreateTMSInboundTrailerBodyFacilityInfo):
        trailer_id (Union[Unset, str]): Unique trailer identifier (auto-generated if not provided) Example: TRAILER_001.
        carrier_info (Union[Unset, CreateTMSInboundTrailerBodyCarrierInfo]):
        cargo (Union[Unset, CreateTMSInboundTrailerBodyCargo]):
    """

    trailer_number: str
    appointment_info: "CreateTMSInboundTrailerBodyAppointmentInfo"
    facility_info: "CreateTMSInboundTrailerBodyFacilityInfo"
    trailer_id: Union[Unset, str] = UNSET
    carrier_info: Union[Unset, "CreateTMSInboundTrailerBodyCarrierInfo"] = UNSET
    cargo: Union[Unset, "CreateTMSInboundTrailerBodyCargo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trailer_number = self.trailer_number

        appointment_info = self.appointment_info.to_dict()

        facility_info = self.facility_info.to_dict()

        trailer_id = self.trailer_id

        carrier_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.carrier_info, Unset):
            carrier_info = self.carrier_info.to_dict()

        cargo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cargo, Unset):
            cargo = self.cargo.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trailerNumber": trailer_number,
                "appointmentInfo": appointment_info,
                "facilityInfo": facility_info,
            }
        )
        if trailer_id is not UNSET:
            field_dict["trailerId"] = trailer_id
        if carrier_info is not UNSET:
            field_dict["carrierInfo"] = carrier_info
        if cargo is not UNSET:
            field_dict["cargo"] = cargo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_tms_inbound_trailer_body_appointment_info import CreateTMSInboundTrailerBodyAppointmentInfo
        from ..models.create_tms_inbound_trailer_body_cargo import CreateTMSInboundTrailerBodyCargo
        from ..models.create_tms_inbound_trailer_body_carrier_info import CreateTMSInboundTrailerBodyCarrierInfo
        from ..models.create_tms_inbound_trailer_body_facility_info import CreateTMSInboundTrailerBodyFacilityInfo

        d = dict(src_dict)
        trailer_number = d.pop("trailerNumber")

        appointment_info = CreateTMSInboundTrailerBodyAppointmentInfo.from_dict(d.pop("appointmentInfo"))

        facility_info = CreateTMSInboundTrailerBodyFacilityInfo.from_dict(d.pop("facilityInfo"))

        trailer_id = d.pop("trailerId", UNSET)

        _carrier_info = d.pop("carrierInfo", UNSET)
        carrier_info: Union[Unset, CreateTMSInboundTrailerBodyCarrierInfo]
        if isinstance(_carrier_info, Unset):
            carrier_info = UNSET
        else:
            carrier_info = CreateTMSInboundTrailerBodyCarrierInfo.from_dict(_carrier_info)

        _cargo = d.pop("cargo", UNSET)
        cargo: Union[Unset, CreateTMSInboundTrailerBodyCargo]
        if isinstance(_cargo, Unset):
            cargo = UNSET
        else:
            cargo = CreateTMSInboundTrailerBodyCargo.from_dict(_cargo)

        create_tms_inbound_trailer_body = cls(
            trailer_number=trailer_number,
            appointment_info=appointment_info,
            facility_info=facility_info,
            trailer_id=trailer_id,
            carrier_info=carrier_info,
            cargo=cargo,
        )

        create_tms_inbound_trailer_body.additional_properties = d
        return create_tms_inbound_trailer_body

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
