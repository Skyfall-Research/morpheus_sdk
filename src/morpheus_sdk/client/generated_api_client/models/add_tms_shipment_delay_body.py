import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.add_tms_shipment_delay_body_delay_type import AddTMSShipmentDelayBodyDelayType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddTMSShipmentDelayBody")


@_attrs_define
class AddTMSShipmentDelayBody:
    """
    Attributes:
        delay_type (AddTMSShipmentDelayBodyDelayType): Category of delay Example: WEATHER.
        reason (str): Detailed reason for the delay Example: Severe thunderstorms in Memphis area causing safety delays.
        start_time (Union[Unset, datetime.datetime]): When the delay started Example: 2024-11-26T16:00:00.000Z.
        estimated_delay (Union[Unset, float]): Estimated delay in minutes Example: 120.
        end_time (Union[Unset, datetime.datetime]): When the delay ended (optional, for ongoing delays) Example:
            2024-11-26T18:00:00.000Z.
    """

    delay_type: AddTMSShipmentDelayBodyDelayType
    reason: str
    start_time: Union[Unset, datetime.datetime] = UNSET
    estimated_delay: Union[Unset, float] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_type = self.delay_type.value

        reason = self.reason

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        estimated_delay = self.estimated_delay

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delayType": delay_type,
                "reason": reason,
            }
        )
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if estimated_delay is not UNSET:
            field_dict["estimatedDelay"] = estimated_delay
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delay_type = AddTMSShipmentDelayBodyDelayType(d.pop("delayType"))

        reason = d.pop("reason")

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        estimated_delay = d.pop("estimatedDelay", UNSET)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        add_tms_shipment_delay_body = cls(
            delay_type=delay_type,
            reason=reason,
            start_time=start_time,
            estimated_delay=estimated_delay,
            end_time=end_time,
        )

        add_tms_shipment_delay_body.additional_properties = d
        return add_tms_shipment_delay_body

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
