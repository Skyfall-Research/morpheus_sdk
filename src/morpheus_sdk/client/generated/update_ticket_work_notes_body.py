from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.work_note import WorkNote


T = TypeVar("T", bound="UpdateTicketWorkNotesBody")


@_attrs_define
class UpdateTicketWorkNotesBody:
    """
    Attributes:
        work_notes (list['WorkNote']):
    """

    work_notes: list["WorkNote"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_notes = []
        for work_notes_item_data in self.work_notes:
            work_notes_item = work_notes_item_data.to_dict()
            work_notes.append(work_notes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workNotes": work_notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_note import WorkNote

        d = dict(src_dict)
        work_notes = []
        _work_notes = d.pop("workNotes")
        for work_notes_item_data in _work_notes:
            work_notes_item = WorkNote.from_dict(work_notes_item_data)

            work_notes.append(work_notes_item)

        update_ticket_work_notes_body = cls(
            work_notes=work_notes,
        )

        update_ticket_work_notes_body.additional_properties = d
        return update_ticket_work_notes_body

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
