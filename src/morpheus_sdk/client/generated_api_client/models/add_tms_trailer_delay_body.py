import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.add_tms_trailer_delay_body_delay_type import AddTMSTrailerDelayBodyDelayType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddTMSTrailerDelayBody")


@_attrs_define
class AddTMSTrailerDelayBody:
    """
    Attributes:
        delay_type (AddTMSTrailerDelayBodyDelayType): Type of delay encountered Example: TRAFFIC.
        reason (str): Detailed reason for the delay Example: Heavy traffic on I-75 due to construction.
        reported_at (datetime.datetime): When the delay was first reported Example: 2024-01-20T07:15:00.000Z.
        estimated_delay (Union[Unset, int]): Estimated delay duration in minutes Example: 45.
    """

    delay_type: AddTMSTrailerDelayBodyDelayType
    reason: str
    reported_at: datetime.datetime
    estimated_delay: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_type = self.delay_type.value

        reason = self.reason

        reported_at = self.reported_at.isoformat()

        estimated_delay = self.estimated_delay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delayType": delay_type,
                "reason": reason,
                "reportedAt": reported_at,
            }
        )
        if estimated_delay is not UNSET:
            field_dict["estimatedDelay"] = estimated_delay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delay_type = AddTMSTrailerDelayBodyDelayType(d.pop("delayType"))

        reason = d.pop("reason")

        reported_at = isoparse(d.pop("reportedAt"))

        estimated_delay = d.pop("estimatedDelay", UNSET)

        add_tms_trailer_delay_body = cls(
            delay_type=delay_type,
            reason=reason,
            reported_at=reported_at,
            estimated_delay=estimated_delay,
        )

        add_tms_trailer_delay_body.additional_properties = d
        return add_tms_trailer_delay_body

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
