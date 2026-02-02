from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wms_receiving_transaction_quality_type_0_status import WMSReceivingTransactionQualityType0Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSReceivingTransactionQualityType0")


@_attrs_define
class WMSReceivingTransactionQualityType0:
    """Quality control and inspection information

    Attributes:
        status (Union[Unset, WMSReceivingTransactionQualityType0Status]): Quality inspection result status Example:
            PENDING.
        inspected_by (Union[None, Unset, str]): User identifier of the quality inspector Example: user_qc_inspector_001.
        notes (Union[None, Unset, str]): Quality inspection notes and observations Example: Visual inspection completed,
            minor packaging damage noted but product integrity maintained.
    """

    status: Union[Unset, WMSReceivingTransactionQualityType0Status] = UNSET
    inspected_by: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        inspected_by: Union[None, Unset, str]
        if isinstance(self.inspected_by, Unset):
            inspected_by = UNSET
        else:
            inspected_by = self.inspected_by

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
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
        status: Union[Unset, WMSReceivingTransactionQualityType0Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WMSReceivingTransactionQualityType0Status(_status)

        def _parse_inspected_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inspected_by = _parse_inspected_by(d.pop("inspectedBy", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        wms_receiving_transaction_quality_type_0 = cls(
            status=status,
            inspected_by=inspected_by,
            notes=notes,
        )

        wms_receiving_transaction_quality_type_0.additional_properties = d
        return wms_receiving_transaction_quality_type_0

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
