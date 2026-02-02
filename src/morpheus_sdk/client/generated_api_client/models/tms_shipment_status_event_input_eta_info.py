import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentStatusEventInputEtaInfo")


@_attrs_define
class TMSShipmentStatusEventInputEtaInfo:
    """ETA information (for ETA_UPDATE events)

    Attributes:
        previous_eta (Union[Unset, datetime.datetime]): Previous estimated time of arrival
        new_eta (Union[Unset, datetime.datetime]): Updated estimated time of arrival
        delay_minutes (Union[Unset, float]): Delay in minutes (negative values indicate earlier arrival)
    """

    previous_eta: Union[Unset, datetime.datetime] = UNSET
    new_eta: Union[Unset, datetime.datetime] = UNSET
    delay_minutes: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        previous_eta: Union[Unset, str] = UNSET
        if not isinstance(self.previous_eta, Unset):
            previous_eta = self.previous_eta.isoformat()

        new_eta: Union[Unset, str] = UNSET
        if not isinstance(self.new_eta, Unset):
            new_eta = self.new_eta.isoformat()

        delay_minutes = self.delay_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if previous_eta is not UNSET:
            field_dict["previousETA"] = previous_eta
        if new_eta is not UNSET:
            field_dict["newETA"] = new_eta
        if delay_minutes is not UNSET:
            field_dict["delayMinutes"] = delay_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _previous_eta = d.pop("previousETA", UNSET)
        previous_eta: Union[Unset, datetime.datetime]
        if isinstance(_previous_eta, Unset):
            previous_eta = UNSET
        else:
            previous_eta = isoparse(_previous_eta)

        _new_eta = d.pop("newETA", UNSET)
        new_eta: Union[Unset, datetime.datetime]
        if isinstance(_new_eta, Unset):
            new_eta = UNSET
        else:
            new_eta = isoparse(_new_eta)

        delay_minutes = d.pop("delayMinutes", UNSET)

        tms_shipment_status_event_input_eta_info = cls(
            previous_eta=previous_eta,
            new_eta=new_eta,
            delay_minutes=delay_minutes,
        )

        tms_shipment_status_event_input_eta_info.additional_properties = d
        return tms_shipment_status_event_input_eta_info

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
