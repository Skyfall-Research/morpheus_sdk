import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSInboundOrderDatesType0")


@_attrs_define
class WMSInboundOrderDatesType0:
    """Important dates for receiving coordination and timeline tracking

    Attributes:
        expected_arrival (Union[Unset, datetime.datetime]): Expected delivery date and time for planning Example:
            2024-11-28T10:00:00Z.
        actual_arrival (Union[None, Unset, datetime.datetime]): Actual delivery date and time for performance tracking
            Example: 2024-11-28T09:45:00Z.
        receiving_started (Union[None, Unset, datetime.datetime]): Timestamp when receiving operations began Example:
            2024-11-28T10:15:00Z.
        receiving_completed (Union[None, Unset, datetime.datetime]): Timestamp when receiving operations completed
            Example: 2024-11-28T14:30:00Z.
    """

    expected_arrival: Union[Unset, datetime.datetime] = UNSET
    actual_arrival: Union[None, Unset, datetime.datetime] = UNSET
    receiving_started: Union[None, Unset, datetime.datetime] = UNSET
    receiving_completed: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.expected_arrival, Unset):
            expected_arrival = self.expected_arrival.isoformat()

        actual_arrival: Union[None, Unset, str]
        if isinstance(self.actual_arrival, Unset):
            actual_arrival = UNSET
        elif isinstance(self.actual_arrival, datetime.datetime):
            actual_arrival = self.actual_arrival.isoformat()
        else:
            actual_arrival = self.actual_arrival

        receiving_started: Union[None, Unset, str]
        if isinstance(self.receiving_started, Unset):
            receiving_started = UNSET
        elif isinstance(self.receiving_started, datetime.datetime):
            receiving_started = self.receiving_started.isoformat()
        else:
            receiving_started = self.receiving_started

        receiving_completed: Union[None, Unset, str]
        if isinstance(self.receiving_completed, Unset):
            receiving_completed = UNSET
        elif isinstance(self.receiving_completed, datetime.datetime):
            receiving_completed = self.receiving_completed.isoformat()
        else:
            receiving_completed = self.receiving_completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expected_arrival is not UNSET:
            field_dict["expectedArrival"] = expected_arrival
        if actual_arrival is not UNSET:
            field_dict["actualArrival"] = actual_arrival
        if receiving_started is not UNSET:
            field_dict["receivingStarted"] = receiving_started
        if receiving_completed is not UNSET:
            field_dict["receivingCompleted"] = receiving_completed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _expected_arrival = d.pop("expectedArrival", UNSET)
        expected_arrival: Union[Unset, datetime.datetime]
        if isinstance(_expected_arrival, Unset):
            expected_arrival = UNSET
        else:
            expected_arrival = isoparse(_expected_arrival)

        def _parse_actual_arrival(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actual_arrival_type_0 = isoparse(data)

                return actual_arrival_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        actual_arrival = _parse_actual_arrival(d.pop("actualArrival", UNSET))

        def _parse_receiving_started(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                receiving_started_type_0 = isoparse(data)

                return receiving_started_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        receiving_started = _parse_receiving_started(d.pop("receivingStarted", UNSET))

        def _parse_receiving_completed(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                receiving_completed_type_0 = isoparse(data)

                return receiving_completed_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        receiving_completed = _parse_receiving_completed(d.pop("receivingCompleted", UNSET))

        wms_inbound_order_dates_type_0 = cls(
            expected_arrival=expected_arrival,
            actual_arrival=actual_arrival,
            receiving_started=receiving_started,
            receiving_completed=receiving_completed,
        )

        wms_inbound_order_dates_type_0.additional_properties = d
        return wms_inbound_order_dates_type_0

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
