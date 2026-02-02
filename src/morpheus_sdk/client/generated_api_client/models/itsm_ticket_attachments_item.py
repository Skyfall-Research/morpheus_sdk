import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItsmTicketAttachmentsItem")


@_attrs_define
class ItsmTicketAttachmentsItem:
    """
    Attributes:
        url (Union[Unset, str]): URL to the attached file Example:
            https://storage.example.com/attachments/error_logs.txt.
        filename (Union[Unset, str]): Original filename of the attachment Example: error_logs.txt.
        uploaded_at (Union[Unset, datetime.datetime]): When the file was uploaded Example: 2024-01-15T10:30:00.000Z.
    """

    url: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    uploaded_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        filename = self.filename

        uploaded_at: Union[Unset, str] = UNSET
        if not isinstance(self.uploaded_at, Unset):
            uploaded_at = self.uploaded_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if filename is not UNSET:
            field_dict["filename"] = filename
        if uploaded_at is not UNSET:
            field_dict["uploadedAt"] = uploaded_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        filename = d.pop("filename", UNSET)

        _uploaded_at = d.pop("uploadedAt", UNSET)
        uploaded_at: Union[Unset, datetime.datetime]
        if isinstance(_uploaded_at, Unset):
            uploaded_at = UNSET
        else:
            uploaded_at = isoparse(_uploaded_at)

        itsm_ticket_attachments_item = cls(
            url=url,
            filename=filename,
            uploaded_at=uploaded_at,
        )

        itsm_ticket_attachments_item.additional_properties = d
        return itsm_ticket_attachments_item

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
