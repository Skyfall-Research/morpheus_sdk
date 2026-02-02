from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_receiving_transaction_body_quality_status import CreateWMSReceivingTransactionBodyQualityStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSReceivingTransactionBodyQuality")


@_attrs_define
class CreateWMSReceivingTransactionBodyQuality:
    """Quality control information

    Attributes:
        status (Union[Unset, CreateWMSReceivingTransactionBodyQualityStatus]): Quality inspection result Example:
            PENDING.
        inspected_by (Union[Unset, str]): User who performed quality inspection Example: user_qc_inspector_001.
        notes (Union[Unset, str]): Quality inspection notes Example: Visual inspection completed, minor packaging damage
            noted.
    """

    status: Union[Unset, CreateWMSReceivingTransactionBodyQualityStatus] = UNSET
    inspected_by: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        inspected_by = self.inspected_by

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if inspected_by is not UNSET:
            field_dict["inspectedBy"] = inspected_by
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateWMSReceivingTransactionBodyQualityStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateWMSReceivingTransactionBodyQualityStatus(_status)

        inspected_by = d.pop("inspectedBy", UNSET)

        notes = d.pop("notes", UNSET)

        create_wms_receiving_transaction_body_quality = cls(
            status=status,
            inspected_by=inspected_by,
            notes=notes,
        )

        create_wms_receiving_transaction_body_quality.additional_properties = d
        return create_wms_receiving_transaction_body_quality

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
