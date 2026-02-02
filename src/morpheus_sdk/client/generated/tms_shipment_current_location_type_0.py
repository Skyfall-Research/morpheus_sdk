import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_shipment_current_location_type_0_last_known_position import (
        TMSShipmentCurrentLocationType0LastKnownPosition,
    )


T = TypeVar("T", bound="TMSShipmentCurrentLocationType0")


@_attrs_define
class TMSShipmentCurrentLocationType0:
    """Current shipment location (null until tracking begins)

    Attributes:
        last_known_position (Union[Unset, TMSShipmentCurrentLocationType0LastKnownPosition]):
        last_update_time (Union[Unset, datetime.datetime]):  Example: 2024-11-26T14:30:00.000Z.
        current_city (Union[Unset, str]):  Example: Memphis.
        current_state (Union[Unset, str]):  Example: TN.
    """

    last_known_position: Union[Unset, "TMSShipmentCurrentLocationType0LastKnownPosition"] = UNSET
    last_update_time: Union[Unset, datetime.datetime] = UNSET
    current_city: Union[Unset, str] = UNSET
    current_state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_known_position: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_known_position, Unset):
            last_known_position = self.last_known_position.to_dict()

        last_update_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_time, Unset):
            last_update_time = self.last_update_time.isoformat()

        current_city = self.current_city

        current_state = self.current_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_known_position is not UNSET:
            field_dict["lastKnownPosition"] = last_known_position
        if last_update_time is not UNSET:
            field_dict["lastUpdateTime"] = last_update_time
        if current_city is not UNSET:
            field_dict["currentCity"] = current_city
        if current_state is not UNSET:
            field_dict["currentState"] = current_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_shipment_current_location_type_0_last_known_position import (
            TMSShipmentCurrentLocationType0LastKnownPosition,
        )

        d = dict(src_dict)
        _last_known_position = d.pop("lastKnownPosition", UNSET)
        last_known_position: Union[Unset, TMSShipmentCurrentLocationType0LastKnownPosition]
        if isinstance(_last_known_position, Unset):
            last_known_position = UNSET
        else:
            last_known_position = TMSShipmentCurrentLocationType0LastKnownPosition.from_dict(_last_known_position)

        _last_update_time = d.pop("lastUpdateTime", UNSET)
        last_update_time: Union[Unset, datetime.datetime]
        if isinstance(_last_update_time, Unset):
            last_update_time = UNSET
        else:
            last_update_time = isoparse(_last_update_time)

        current_city = d.pop("currentCity", UNSET)

        current_state = d.pop("currentState", UNSET)

        tms_shipment_current_location_type_0 = cls(
            last_known_position=last_known_position,
            last_update_time=last_update_time,
            current_city=current_city,
            current_state=current_state,
        )

        tms_shipment_current_location_type_0.additional_properties = d
        return tms_shipment_current_location_type_0

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
