import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tms_shipment_status_event_input_event_type import TMSShipmentStatusEventInputEventType
from ..models.tms_shipment_status_event_input_source import TMSShipmentStatusEventInputSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_shipment_status_event_input_eta_info import TMSShipmentStatusEventInputEtaInfo
    from ..models.tms_shipment_status_event_input_exception_info import TMSShipmentStatusEventInputExceptionInfo
    from ..models.tms_shipment_status_event_input_location_info import TMSShipmentStatusEventInputLocationInfo
    from ..models.tms_shipment_status_event_input_raw_data import TMSShipmentStatusEventInputRawData
    from ..models.tms_shipment_status_event_input_status_info import TMSShipmentStatusEventInputStatusInfo


T = TypeVar("T", bound="TMSShipmentStatusEventInput")


@_attrs_define
class TMSShipmentStatusEventInput:
    """Input data for creating a shipment status event

    Attributes:
        event_type (TMSShipmentStatusEventInputEventType): Type of event being recorded Example: STATUS_CHANGE.
        event_time (datetime.datetime): When the event occurred Example: 2024-11-26T14:30:00.000Z.
        status_info (Union[Unset, TMSShipmentStatusEventInputStatusInfo]): Status change information (for STATUS_CHANGE
            events)
        location_info (Union[Unset, TMSShipmentStatusEventInputLocationInfo]): Location information (for LOCATION_UPDATE
            events)
        eta_info (Union[Unset, TMSShipmentStatusEventInputEtaInfo]): ETA information (for ETA_UPDATE events)
        exception_info (Union[Unset, TMSShipmentStatusEventInputExceptionInfo]): Exception information (for EXCEPTION
            events)
        source (Union[Unset, TMSShipmentStatusEventInputSource]): Source of the event data Example: API.
        raw_data (Union[Unset, TMSShipmentStatusEventInputRawData]): Raw event data for audit purposes
    """

    event_type: TMSShipmentStatusEventInputEventType
    event_time: datetime.datetime
    status_info: Union[Unset, "TMSShipmentStatusEventInputStatusInfo"] = UNSET
    location_info: Union[Unset, "TMSShipmentStatusEventInputLocationInfo"] = UNSET
    eta_info: Union[Unset, "TMSShipmentStatusEventInputEtaInfo"] = UNSET
    exception_info: Union[Unset, "TMSShipmentStatusEventInputExceptionInfo"] = UNSET
    source: Union[Unset, TMSShipmentStatusEventInputSource] = UNSET
    raw_data: Union[Unset, "TMSShipmentStatusEventInputRawData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        raw_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.raw_data, Unset):
            raw_data = self.raw_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if raw_data is not UNSET:
            field_dict["rawData"] = raw_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_shipment_status_event_input_eta_info import TMSShipmentStatusEventInputEtaInfo
        from ..models.tms_shipment_status_event_input_exception_info import TMSShipmentStatusEventInputExceptionInfo
        from ..models.tms_shipment_status_event_input_location_info import TMSShipmentStatusEventInputLocationInfo
        from ..models.tms_shipment_status_event_input_raw_data import TMSShipmentStatusEventInputRawData
        from ..models.tms_shipment_status_event_input_status_info import TMSShipmentStatusEventInputStatusInfo

        d = dict(src_dict)
        event_type = TMSShipmentStatusEventInputEventType(d.pop("eventType"))

        event_time = isoparse(d.pop("eventTime"))

        _status_info = d.pop("statusInfo", UNSET)
        status_info: Union[Unset, TMSShipmentStatusEventInputStatusInfo]
        if isinstance(_status_info, Unset):
            status_info = UNSET
        else:
            status_info = TMSShipmentStatusEventInputStatusInfo.from_dict(_status_info)

        _location_info = d.pop("locationInfo", UNSET)
        location_info: Union[Unset, TMSShipmentStatusEventInputLocationInfo]
        if isinstance(_location_info, Unset):
            location_info = UNSET
        else:
            location_info = TMSShipmentStatusEventInputLocationInfo.from_dict(_location_info)

        _eta_info = d.pop("etaInfo", UNSET)
        eta_info: Union[Unset, TMSShipmentStatusEventInputEtaInfo]
        if isinstance(_eta_info, Unset):
            eta_info = UNSET
        else:
            eta_info = TMSShipmentStatusEventInputEtaInfo.from_dict(_eta_info)

        _exception_info = d.pop("exceptionInfo", UNSET)
        exception_info: Union[Unset, TMSShipmentStatusEventInputExceptionInfo]
        if isinstance(_exception_info, Unset):
            exception_info = UNSET
        else:
            exception_info = TMSShipmentStatusEventInputExceptionInfo.from_dict(_exception_info)

        _source = d.pop("source", UNSET)
        source: Union[Unset, TMSShipmentStatusEventInputSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = TMSShipmentStatusEventInputSource(_source)

        _raw_data = d.pop("rawData", UNSET)
        raw_data: Union[Unset, TMSShipmentStatusEventInputRawData]
        if isinstance(_raw_data, Unset):
            raw_data = UNSET
        else:
            raw_data = TMSShipmentStatusEventInputRawData.from_dict(_raw_data)

        tms_shipment_status_event_input = cls(
            event_type=event_type,
            event_time=event_time,
            status_info=status_info,
            location_info=location_info,
            eta_info=eta_info,
            exception_info=exception_info,
            source=source,
            raw_data=raw_data,
        )

        tms_shipment_status_event_input.additional_properties = d
        return tms_shipment_status_event_input

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
