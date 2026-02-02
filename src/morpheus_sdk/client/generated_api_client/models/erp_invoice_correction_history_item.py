import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_invoice_correction_history_item_previous import ERPInvoiceCorrectionHistoryItemPrevious


T = TypeVar("T", bound="ERPInvoiceCorrectionHistoryItem")


@_attrs_define
class ERPInvoiceCorrectionHistoryItem:
    """
    Attributes:
        previous (Union[Unset, ERPInvoiceCorrectionHistoryItemPrevious]): Previous invoice state
        corrected_at (Union[Unset, datetime.datetime]):  Example: 2024-01-18T14:00:00.000Z.
        corrected_by (Union[Unset, str]):  Example: user@example.com.
    """

    previous: Union[Unset, "ERPInvoiceCorrectionHistoryItemPrevious"] = UNSET
    corrected_at: Union[Unset, datetime.datetime] = UNSET
    corrected_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        previous: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        corrected_at: Union[Unset, str] = UNSET
        if not isinstance(self.corrected_at, Unset):
            corrected_at = self.corrected_at.isoformat()

        corrected_by = self.corrected_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if previous is not UNSET:
            field_dict["previous"] = previous
        if corrected_at is not UNSET:
            field_dict["correctedAt"] = corrected_at
        if corrected_by is not UNSET:
            field_dict["correctedBy"] = corrected_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_invoice_correction_history_item_previous import ERPInvoiceCorrectionHistoryItemPrevious

        d = dict(src_dict)
        _previous = d.pop("previous", UNSET)
        previous: Union[Unset, ERPInvoiceCorrectionHistoryItemPrevious]
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = ERPInvoiceCorrectionHistoryItemPrevious.from_dict(_previous)

        _corrected_at = d.pop("correctedAt", UNSET)
        corrected_at: Union[Unset, datetime.datetime]
        if isinstance(_corrected_at, Unset):
            corrected_at = UNSET
        else:
            corrected_at = isoparse(_corrected_at)

        corrected_by = d.pop("correctedBy", UNSET)

        erp_invoice_correction_history_item = cls(
            previous=previous,
            corrected_at=corrected_at,
            corrected_by=corrected_by,
        )

        erp_invoice_correction_history_item.additional_properties = d
        return erp_invoice_correction_history_item

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
