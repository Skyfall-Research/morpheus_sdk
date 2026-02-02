from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSReceivingTransactionPutawayType0")


@_attrs_define
class WMSReceivingTransactionPutawayType0:
    """Putaway location assignment and management

    Attributes:
        assigned_location (Union[None, Unset, str]): Designated storage location for received goods Example: A-01-01.
        assigned_by (Union[None, Unset, str]): User who assigned the putaway location Example:
            user_warehouse_manager_001.
        notes (Union[None, Unset, str]): Special putaway instructions and notes Example: Stack carefully - fragile
            items.
    """

    assigned_location: Union[None, Unset, str] = UNSET
    assigned_by: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_location: Union[None, Unset, str]
        if isinstance(self.assigned_location, Unset):
            assigned_location = UNSET
        else:
            assigned_location = self.assigned_location

        assigned_by: Union[None, Unset, str]
        if isinstance(self.assigned_by, Unset):
            assigned_by = UNSET
        else:
            assigned_by = self.assigned_by

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_location is not UNSET:
            field_dict["assignedLocation"] = assigned_location
        if assigned_by is not UNSET:
            field_dict["assignedBy"] = assigned_by
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_assigned_location(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assigned_location = _parse_assigned_location(d.pop("assignedLocation", UNSET))

        def _parse_assigned_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assigned_by = _parse_assigned_by(d.pop("assignedBy", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        wms_receiving_transaction_putaway_type_0 = cls(
            assigned_location=assigned_location,
            assigned_by=assigned_by,
            notes=notes,
        )

        wms_receiving_transaction_putaway_type_0.additional_properties = d
        return wms_receiving_transaction_putaway_type_0

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
