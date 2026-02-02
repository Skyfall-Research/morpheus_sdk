import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tms_inbound_trailer_delays_item_delay_type import TMSInboundTrailerDelaysItemDelayType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSInboundTrailerDelaysItem")


@_attrs_define
class TMSInboundTrailerDelaysItem:
    """
    Attributes:
        delay_type (Union[Unset, TMSInboundTrailerDelaysItemDelayType]): Type of delay encountered Example: TRAFFIC.
        reason (Union[Unset, str]): Detailed reason for the delay Example: Heavy traffic on I-75 due to construction.
        reported_at (Union[Unset, datetime.datetime]): When the delay was first reported Example:
            2024-01-20T07:15:00.000Z.
        estimated_delay (Union[Unset, int]): Estimated delay duration in minutes Example: 45.
    """

    delay_type: Union[Unset, TMSInboundTrailerDelaysItemDelayType] = UNSET
    reason: Union[Unset, str] = UNSET
    reported_at: Union[Unset, datetime.datetime] = UNSET
    estimated_delay: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_type: Union[Unset, str] = UNSET
        if not isinstance(self.delay_type, Unset):
            delay_type = self.delay_type.value

        reason = self.reason

        reported_at: Union[Unset, str] = UNSET
        if not isinstance(self.reported_at, Unset):
            reported_at = self.reported_at.isoformat()

        estimated_delay = self.estimated_delay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delay_type is not UNSET:
            field_dict["delayType"] = delay_type
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reported_at is not UNSET:
            field_dict["reportedAt"] = reported_at
        if estimated_delay is not UNSET:
            field_dict["estimatedDelay"] = estimated_delay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _delay_type = d.pop("delayType", UNSET)
        delay_type: Union[Unset, TMSInboundTrailerDelaysItemDelayType]
        if isinstance(_delay_type, Unset):
            delay_type = UNSET
        else:
            delay_type = TMSInboundTrailerDelaysItemDelayType(_delay_type)

        reason = d.pop("reason", UNSET)

        _reported_at = d.pop("reportedAt", UNSET)
        reported_at: Union[Unset, datetime.datetime]
        if isinstance(_reported_at, Unset):
            reported_at = UNSET
        else:
            reported_at = isoparse(_reported_at)

        estimated_delay = d.pop("estimatedDelay", UNSET)

        tms_inbound_trailer_delays_item = cls(
            delay_type=delay_type,
            reason=reason,
            reported_at=reported_at,
            estimated_delay=estimated_delay,
        )

        tms_inbound_trailer_delays_item.additional_properties = d
        return tms_inbound_trailer_delays_item

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
