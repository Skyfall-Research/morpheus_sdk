import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="WorkNote")


@_attrs_define
class WorkNote:
    """Work note entry for tracking progress and communication

    Attributes:
        author (str): User ID of the note author Example: tech_support_1.
        note (str): Text content of the note Example: Investigating server logs. Found disk space issue on mail server..
        is_public (bool): Whether the note is visible to the requester Default: False.
        created_at (datetime.datetime): When the note was created Example: 2024-01-15T10:25:00.000Z.
        updated_at (datetime.datetime): When the note was last updated Example: 2024-01-15T10:25:00.000Z.
    """

    author: str
    note: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_public: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        note = self.note

        is_public = self.is_public

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "note": note,
                "isPublic": is_public,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author = d.pop("author")

        note = d.pop("note")

        is_public = d.pop("isPublic")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        work_note = cls(
            author=author,
            note=note,
            is_public=is_public,
            created_at=created_at,
            updated_at=updated_at,
        )

        work_note.additional_properties = d
        return work_note

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
