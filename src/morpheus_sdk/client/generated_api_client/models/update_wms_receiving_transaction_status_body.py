from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_wms_receiving_transaction_status_body_status import UpdateWMSReceivingTransactionStatusBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWMSReceivingTransactionStatusBody")


@_attrs_define
class UpdateWMSReceivingTransactionStatusBody:
    """
    Attributes:
        status (UpdateWMSReceivingTransactionStatusBodyStatus): New status for the receiving transaction Example:
            PUTAWAY_PENDING.
        notes (Union[Unset, str]): Optional notes explaining the status change Example: Quality inspection completed
            successfully, ready for putaway.
    """

    status: UpdateWMSReceivingTransactionStatusBodyStatus
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = UpdateWMSReceivingTransactionStatusBodyStatus(d.pop("status"))

        notes = d.pop("notes", UNSET)

        update_wms_receiving_transaction_status_body = cls(
            status=status,
            notes=notes,
        )

        update_wms_receiving_transaction_status_body.additional_properties = d
        return update_wms_receiving_transaction_status_body

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
