import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentRouteInfoType0PlannedRouteItem")


@_attrs_define
class TMSShipmentRouteInfoType0PlannedRouteItem:
    """
    Attributes:
        stop_number (Union[Unset, int]): Sequential stop number Example: 1.
        location_name (Union[Unset, str]): Name of the stop location Example: Memphis Hub.
        arrival_time (Union[None, Unset, datetime.datetime]): Planned arrival time at the stop Example:
            2024-11-27T14:00:00.000Z.
        departure_time (Union[None, Unset, datetime.datetime]): Planned departure time from the stop Example:
            2024-11-27T16:00:00.000Z.
    """

    stop_number: Union[Unset, int] = UNSET
    location_name: Union[Unset, str] = UNSET
    arrival_time: Union[None, Unset, datetime.datetime] = UNSET
    departure_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stop_number = self.stop_number

        location_name = self.location_name

        arrival_time: Union[None, Unset, str]
        if isinstance(self.arrival_time, Unset):
            arrival_time = UNSET
        elif isinstance(self.arrival_time, datetime.datetime):
            arrival_time = self.arrival_time.isoformat()
        else:
            arrival_time = self.arrival_time

        departure_time: Union[None, Unset, str]
        if isinstance(self.departure_time, Unset):
            departure_time = UNSET
        elif isinstance(self.departure_time, datetime.datetime):
            departure_time = self.departure_time.isoformat()
        else:
            departure_time = self.departure_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stop_number is not UNSET:
            field_dict["stopNumber"] = stop_number
        if location_name is not UNSET:
            field_dict["locationName"] = location_name
        if arrival_time is not UNSET:
            field_dict["arrivalTime"] = arrival_time
        if departure_time is not UNSET:
            field_dict["departureTime"] = departure_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stop_number = d.pop("stopNumber", UNSET)

        location_name = d.pop("locationName", UNSET)

        def _parse_arrival_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                arrival_time_type_0 = isoparse(data)

                return arrival_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        arrival_time = _parse_arrival_time(d.pop("arrivalTime", UNSET))

        def _parse_departure_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                departure_time_type_0 = isoparse(data)

                return departure_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        departure_time = _parse_departure_time(d.pop("departureTime", UNSET))

        tms_shipment_route_info_type_0_planned_route_item = cls(
            stop_number=stop_number,
            location_name=location_name,
            arrival_time=arrival_time,
            departure_time=departure_time,
        )

        tms_shipment_route_info_type_0_planned_route_item.additional_properties = d
        return tms_shipment_route_info_type_0_planned_route_item

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
