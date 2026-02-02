import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tms_shipment_status_event_event_type import TMSShipmentStatusEventEventType
from ..models.tms_shipment_status_event_source import TMSShipmentStatusEventSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_shipment_status_event_eta_info import TMSShipmentStatusEventEtaInfo
    from ..models.tms_shipment_status_event_exception_info import TMSShipmentStatusEventExceptionInfo
    from ..models.tms_shipment_status_event_location_info import TMSShipmentStatusEventLocationInfo
    from ..models.tms_shipment_status_event_status_info import TMSShipmentStatusEventStatusInfo


T = TypeVar("T", bound="TMSShipmentStatusEvent")


@_attrs_define
class TMSShipmentStatusEvent:
    """Status event record for shipment tracking

    Attributes:
        field_id (str):  Example: 507f1f77bcf86cd799439011.
        id (str): Formatted ID for client use (same as _id) Example: 507f1f77bcf86cd799439011.
        event_id (str):  Example: TMS_EVENT_674565c1234567890abcdef.
        shipment_id (str):  Example: SHIP-2024-001234.
        event_type (TMSShipmentStatusEventEventType):  Example: STATUS_CHANGE.
        event_time (datetime.datetime):  Example: 2024-11-26T14:30:00.000Z.
        status_info (Union[Unset, TMSShipmentStatusEventStatusInfo]): Status change details for STATUS_CHANGE events
        location_info (Union[Unset, TMSShipmentStatusEventLocationInfo]): Location details for LOCATION_UPDATE events
        eta_info (Union[Unset, TMSShipmentStatusEventEtaInfo]): ETA update details for ETA_UPDATE events
        exception_info (Union[Unset, TMSShipmentStatusEventExceptionInfo]): Exception details for EXCEPTION events
        source (Union[Unset, TMSShipmentStatusEventSource]):  Example: EDI.
        created_at (Union[Unset, datetime.datetime]):  Example: 2024-11-26T14:30:00.000Z.
    """

    field_id: str
    id: str
    event_id: str
    shipment_id: str
    event_type: TMSShipmentStatusEventEventType
    event_time: datetime.datetime
    status_info: Union[Unset, "TMSShipmentStatusEventStatusInfo"] = UNSET
    location_info: Union[Unset, "TMSShipmentStatusEventLocationInfo"] = UNSET
    eta_info: Union[Unset, "TMSShipmentStatusEventEtaInfo"] = UNSET
    exception_info: Union[Unset, "TMSShipmentStatusEventExceptionInfo"] = UNSET
    source: Union[Unset, TMSShipmentStatusEventSource] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        id = self.id

        event_id = self.event_id

        shipment_id = self.shipment_id

        event_type = self.event_type.value

        event_time = self.event_time.isoformat()

        status_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status_info, Unset):
            status_info = self.status_info.to_dict()

        location_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location_info, Unset):
            location_info = self.location_info.to_dict()

        eta_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.eta_info, Unset):
            eta_info = self.eta_info.to_dict()

        exception_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exception_info, Unset):
            exception_info = self.exception_info.to_dict()

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "id": id,
                "eventId": event_id,
                "shipmentId": shipment_id,
                "eventType": event_type,
                "eventTime": event_time,
            }
        )
        if status_info is not UNSET:
            field_dict["statusInfo"] = status_info
        if location_info is not UNSET:
            field_dict["locationInfo"] = location_info
        if eta_info is not UNSET:
            field_dict["etaInfo"] = eta_info
        if exception_info is not UNSET:
            field_dict["exceptionInfo"] = exception_info
        if source is not UNSET:
            field_dict["source"] = source
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_shipment_status_event_eta_info import TMSShipmentStatusEventEtaInfo
        from ..models.tms_shipment_status_event_exception_info import TMSShipmentStatusEventExceptionInfo
        from ..models.tms_shipment_status_event_location_info import TMSShipmentStatusEventLocationInfo
        from ..models.tms_shipment_status_event_status_info import TMSShipmentStatusEventStatusInfo

        d = dict(src_dict)
        field_id = d.pop("_id")

        id = d.pop("id")

        event_id = d.pop("eventId")

        shipment_id = d.pop("shipmentId")

        event_type = TMSShipmentStatusEventEventType(d.pop("eventType"))

        event_time = isoparse(d.pop("eventTime"))

        _status_info = d.pop("statusInfo", UNSET)
        status_info: Union[Unset, TMSShipmentStatusEventStatusInfo]
        if isinstance(_status_info, Unset):
            status_info = UNSET
        else:
            status_info = TMSShipmentStatusEventStatusInfo.from_dict(_status_info)

        _location_info = d.pop("locationInfo", UNSET)
        location_info: Union[Unset, TMSShipmentStatusEventLocationInfo]
        if isinstance(_location_info, Unset):
            location_info = UNSET
        else:
            location_info = TMSShipmentStatusEventLocationInfo.from_dict(_location_info)

        _eta_info = d.pop("etaInfo", UNSET)
        eta_info: Union[Unset, TMSShipmentStatusEventEtaInfo]
        if isinstance(_eta_info, Unset):
            eta_info = UNSET
        else:
            eta_info = TMSShipmentStatusEventEtaInfo.from_dict(_eta_info)

        _exception_info = d.pop("exceptionInfo", UNSET)
        exception_info: Union[Unset, TMSShipmentStatusEventExceptionInfo]
        if isinstance(_exception_info, Unset):
            exception_info = UNSET
        else:
            exception_info = TMSShipmentStatusEventExceptionInfo.from_dict(_exception_info)

        _source = d.pop("source", UNSET)
        source: Union[Unset, TMSShipmentStatusEventSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = TMSShipmentStatusEventSource(_source)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        tms_shipment_status_event = cls(
            field_id=field_id,
            id=id,
            event_id=event_id,
            shipment_id=shipment_id,
            event_type=event_type,
            event_time=event_time,
            status_info=status_info,
            location_info=location_info,
            eta_info=eta_info,
            exception_info=exception_info,
            source=source,
            created_at=created_at,
        )

        tms_shipment_status_event.additional_properties = d
        return tms_shipment_status_event

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
