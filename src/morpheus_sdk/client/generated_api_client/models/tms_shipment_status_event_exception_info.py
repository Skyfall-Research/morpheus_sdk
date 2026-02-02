from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tms_shipment_status_event_exception_info_severity import TMSShipmentStatusEventExceptionInfoSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentStatusEventExceptionInfo")


@_attrs_define
class TMSShipmentStatusEventExceptionInfo:
    """Exception details for EXCEPTION events

    Attributes:
        exception_type (Union[Unset, str]): Category or type of the exception Example: WEATHER_DELAY.
        severity (Union[Unset, TMSShipmentStatusEventExceptionInfoSeverity]): Severity level of the exception Example:
            MEDIUM.
        description (Union[Unset, str]): Detailed description of the exception Example: Severe weather causing transit
            delays.
        resolution (Union[Unset, str]): Current resolution or mitigation action Example: Monitoring weather for safe
            continuation.
    """

    exception_type: Union[Unset, str] = UNSET
    severity: Union[Unset, TMSShipmentStatusEventExceptionInfoSeverity] = UNSET
    description: Union[Unset, str] = UNSET
    resolution: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exception_type = self.exception_type

        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        description = self.description

        resolution = self.resolution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exception_type is not UNSET:
            field_dict["exceptionType"] = exception_type
        if severity is not UNSET:
            field_dict["severity"] = severity
        if description is not UNSET:
            field_dict["description"] = description
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exception_type = d.pop("exceptionType", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, TMSShipmentStatusEventExceptionInfoSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = TMSShipmentStatusEventExceptionInfoSeverity(_severity)

        description = d.pop("description", UNSET)

        resolution = d.pop("resolution", UNSET)

        tms_shipment_status_event_exception_info = cls(
            exception_type=exception_type,
            severity=severity,
            description=description,
            resolution=resolution,
        )

        tms_shipment_status_event_exception_info.additional_properties = d
        return tms_shipment_status_event_exception_info

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
