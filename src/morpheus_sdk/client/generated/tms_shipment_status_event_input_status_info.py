from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentStatusEventInputStatusInfo")


@_attrs_define
class TMSShipmentStatusEventInputStatusInfo:
    """Status change information (for STATUS_CHANGE events)

    Attributes:
        previous_status (Union[Unset, str]): Previous shipment status before the change Example: ACCEPTED.
        new_status (Union[Unset, str]): New shipment status after the change Example: PICKED_UP.
    """

    previous_status: Union[Unset, str] = UNSET
    new_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        previous_status = self.previous_status

        new_status = self.new_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if previous_status is not UNSET:
            field_dict["previousStatus"] = previous_status
        if new_status is not UNSET:
            field_dict["newStatus"] = new_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        previous_status = d.pop("previousStatus", UNSET)

        new_status = d.pop("newStatus", UNSET)

        tms_shipment_status_event_input_status_info = cls(
            previous_status=previous_status,
            new_status=new_status,
        )

        tms_shipment_status_event_input_status_info.additional_properties = d
        return tms_shipment_status_event_input_status_info

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
