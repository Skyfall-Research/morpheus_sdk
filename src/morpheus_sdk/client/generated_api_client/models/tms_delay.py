import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tms_delay_delay_type import TMSDelayDelayType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSDelay")


@_attrs_define
class TMSDelay:
    """Delay information for shipments

    Attributes:
        delay_type (TMSDelayDelayType):  Example: WEATHER.
        reason (str):  Example: Severe thunderstorms causing safety delays.
        start_time (datetime.datetime):  Example: 2024-11-26T16:00:00.000Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2024-11-26T18:00:00.000Z.
        estimated_delay (Union[Unset, float]):  Example: 120.
    """

    delay_type: TMSDelayDelayType
    reason: str
    start_time: datetime.datetime
    end_time: Union[Unset, datetime.datetime] = UNSET
    estimated_delay: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_type = self.delay_type.value

        reason = self.reason

        start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        estimated_delay = self.estimated_delay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delayType": delay_type,
                "reason": reason,
                "startTime": start_time,
            }
        )
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if estimated_delay is not UNSET:
            field_dict["estimatedDelay"] = estimated_delay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delay_type = TMSDelayDelayType(d.pop("delayType"))

        reason = d.pop("reason")

        start_time = isoparse(d.pop("startTime"))

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        estimated_delay = d.pop("estimatedDelay", UNSET)

        tms_delay = cls(
            delay_type=delay_type,
            reason=reason,
            start_time=start_time,
            end_time=end_time,
            estimated_delay=estimated_delay,
        )

        tms_delay.additional_properties = d
        return tms_delay

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
