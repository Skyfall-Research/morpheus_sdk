from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSReceivingTransactionBodyPutaway")


@_attrs_define
class CreateWMSReceivingTransactionBodyPutaway:
    """Putaway location assignment

    Attributes:
        assigned_location (Union[Unset, str]): Designated storage location Example: A-01-01.
        assigned_by (Union[Unset, str]): User who assigned the location Example: user_warehouse_manager_001.
        notes (Union[Unset, str]): Putaway instructions Example: Stack carefully - fragile items.
    """

    assigned_location: Union[Unset, str] = UNSET
    assigned_by: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_location = self.assigned_location

        assigned_by = self.assigned_by

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
        assigned_location = d.pop("assignedLocation", UNSET)

        assigned_by = d.pop("assignedBy", UNSET)

        notes = d.pop("notes", UNSET)

        create_wms_receiving_transaction_body_putaway = cls(
            assigned_location=assigned_location,
            assigned_by=assigned_by,
            notes=notes,
        )

        create_wms_receiving_transaction_body_putaway.additional_properties = d
        return create_wms_receiving_transaction_body_putaway

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
