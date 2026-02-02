import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tms_inbound_trailer_status import TMSInboundTrailerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_inbound_trailer_appointment_info import TMSInboundTrailerAppointmentInfo
    from ..models.tms_inbound_trailer_cargo import TMSInboundTrailerCargo
    from ..models.tms_inbound_trailer_carrier_info import TMSInboundTrailerCarrierInfo
    from ..models.tms_inbound_trailer_custom_fields import TMSInboundTrailerCustomFields
    from ..models.tms_inbound_trailer_delays_item import TMSInboundTrailerDelaysItem
    from ..models.tms_inbound_trailer_facility_info import TMSInboundTrailerFacilityInfo
    from ..models.tms_inbound_trailer_world_ref import TMSInboundTrailerWorldRef


T = TypeVar("T", bound="TMSInboundTrailer")


@_attrs_define
class TMSInboundTrailer:
    """Complete TMS inbound trailer record for dock scheduling and operations

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        trailer_id (str): Unique trailer identifier Example: TRAILER_001.
        trailer_number (str): Physical trailer number/license plate Example: TR-12345.
        status (TMSInboundTrailerStatus): Current operational status of the trailer Example: CHECKED_IN.
        appointment_info (TMSInboundTrailerAppointmentInfo): Appointment scheduling and timing details
        facility_info (TMSInboundTrailerFacilityInfo): Distribution center and facility details
        world_ref (TMSInboundTrailerWorldRef): World reference information
        created_at (datetime.datetime): Timestamp when the trailer record was created Example: 2024-01-19T10:30:00.000Z.
        updated_at (datetime.datetime): Timestamp when the trailer record was last updated Example:
            2024-01-20T08:15:00.000Z.
        id (Union[Unset, str]): Formatted document identifier for API responses Example: 507f1f77bcf86cd799439011.
        carrier_info (Union[Unset, TMSInboundTrailerCarrierInfo]): Carrier and driver information
        shipment_ids (Union[Unset, list[str]]): Associated shipment identifiers Example: ['SHIPMENT_001',
            'SHIPMENT_002'].
        cargo (Union[Unset, TMSInboundTrailerCargo]): Cargo and freight information
        delays (Union[Unset, list['TMSInboundTrailerDelaysItem']]): Delay events and disruptions
        custom_fields (Union[Unset, TMSInboundTrailerCustomFields]): Additional custom fields for extensibility Example:
            {'specialInstructions': 'Fragile items - handle with care', 'priority': 'HIGH'}.
    """

    field_id: str
    trailer_id: str
    trailer_number: str
    status: TMSInboundTrailerStatus
    appointment_info: "TMSInboundTrailerAppointmentInfo"
    facility_info: "TMSInboundTrailerFacilityInfo"
    world_ref: "TMSInboundTrailerWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, str] = UNSET
    carrier_info: Union[Unset, "TMSInboundTrailerCarrierInfo"] = UNSET
    shipment_ids: Union[Unset, list[str]] = UNSET
    cargo: Union[Unset, "TMSInboundTrailerCargo"] = UNSET
    delays: Union[Unset, list["TMSInboundTrailerDelaysItem"]] = UNSET
    custom_fields: Union[Unset, "TMSInboundTrailerCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        trailer_id = self.trailer_id

        trailer_number = self.trailer_number

        status = self.status.value

        appointment_info = self.appointment_info.to_dict()

        facility_info = self.facility_info.to_dict()

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id

        carrier_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.carrier_info, Unset):
            carrier_info = self.carrier_info.to_dict()

        shipment_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shipment_ids, Unset):
            shipment_ids = self.shipment_ids

        cargo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cargo, Unset):
            cargo = self.cargo.to_dict()

        delays: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.delays, Unset):
            delays = []
            for delays_item_data in self.delays:
                delays_item = delays_item_data.to_dict()
                delays.append(delays_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "trailerId": trailer_id,
                "trailerNumber": trailer_number,
                "status": status,
                "appointmentInfo": appointment_info,
                "facilityInfo": facility_info,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if carrier_info is not UNSET:
            field_dict["carrierInfo"] = carrier_info
        if shipment_ids is not UNSET:
            field_dict["shipmentIds"] = shipment_ids
        if cargo is not UNSET:
            field_dict["cargo"] = cargo
        if delays is not UNSET:
            field_dict["delays"] = delays
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_inbound_trailer_appointment_info import TMSInboundTrailerAppointmentInfo
        from ..models.tms_inbound_trailer_cargo import TMSInboundTrailerCargo
        from ..models.tms_inbound_trailer_carrier_info import TMSInboundTrailerCarrierInfo
        from ..models.tms_inbound_trailer_custom_fields import TMSInboundTrailerCustomFields
        from ..models.tms_inbound_trailer_delays_item import TMSInboundTrailerDelaysItem
        from ..models.tms_inbound_trailer_facility_info import TMSInboundTrailerFacilityInfo
        from ..models.tms_inbound_trailer_world_ref import TMSInboundTrailerWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        trailer_id = d.pop("trailerId")

        trailer_number = d.pop("trailerNumber")

        status = TMSInboundTrailerStatus(d.pop("status"))

        appointment_info = TMSInboundTrailerAppointmentInfo.from_dict(d.pop("appointmentInfo"))

        facility_info = TMSInboundTrailerFacilityInfo.from_dict(d.pop("facilityInfo"))

        world_ref = TMSInboundTrailerWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        id = d.pop("id", UNSET)

        _carrier_info = d.pop("carrierInfo", UNSET)
        carrier_info: Union[Unset, TMSInboundTrailerCarrierInfo]
        if isinstance(_carrier_info, Unset):
            carrier_info = UNSET
        else:
            carrier_info = TMSInboundTrailerCarrierInfo.from_dict(_carrier_info)

        shipment_ids = cast(list[str], d.pop("shipmentIds", UNSET))

        _cargo = d.pop("cargo", UNSET)
        cargo: Union[Unset, TMSInboundTrailerCargo]
        if isinstance(_cargo, Unset):
            cargo = UNSET
        else:
            cargo = TMSInboundTrailerCargo.from_dict(_cargo)

        delays = []
        _delays = d.pop("delays", UNSET)
        for delays_item_data in _delays or []:
            delays_item = TMSInboundTrailerDelaysItem.from_dict(delays_item_data)

            delays.append(delays_item)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, TMSInboundTrailerCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = TMSInboundTrailerCustomFields.from_dict(_custom_fields)

        tms_inbound_trailer = cls(
            field_id=field_id,
            trailer_id=trailer_id,
            trailer_number=trailer_number,
            status=status,
            appointment_info=appointment_info,
            facility_info=facility_info,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            carrier_info=carrier_info,
            shipment_ids=shipment_ids,
            cargo=cargo,
            delays=delays,
            custom_fields=custom_fields,
        )

        tms_inbound_trailer.additional_properties = d
        return tms_inbound_trailer

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
