import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ERPInvoiceDisputesItem")


@_attrs_define
class ERPInvoiceDisputesItem:
    """
    Attributes:
        ticket_id (Union[Unset, str]):  Example: TICKET_001.
        reason (Union[Unset, str]):  Example: Price discrepancy.
        created_at (Union[Unset, datetime.datetime]):  Example: 2024-01-20T10:00:00.000Z.
    """

    ticket_id: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticket_id = self.ticket_id

        reason = self.reason

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ticket_id is not UNSET:
            field_dict["ticketId"] = ticket_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticket_id = d.pop("ticketId", UNSET)

        reason = d.pop("reason", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        erp_invoice_disputes_item = cls(
            ticket_id=ticket_id,
            reason=reason,
            created_at=created_at,
        )

        erp_invoice_disputes_item.additional_properties = d
        return erp_invoice_disputes_item

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
