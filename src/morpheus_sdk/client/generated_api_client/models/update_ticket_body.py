from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_ticket_body_priority import UpdateTicketBodyPriority
from ..models.update_ticket_body_status import UpdateTicketBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTicketBody")


@_attrs_define
class UpdateTicketBody:
    """
    Attributes:
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        status (Union[Unset, UpdateTicketBodyStatus]):
        priority (Union[Unset, UpdateTicketBodyPriority]):
        assigned_to (Union[Unset, str]):
        resolution_notes (Union[Unset, str]):
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, UpdateTicketBodyStatus] = UNSET
    priority: Union[Unset, UpdateTicketBodyPriority] = UNSET
    assigned_to: Union[Unset, str] = UNSET
    resolution_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        assigned_to = self.assigned_to

        resolution_notes = self.resolution_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if priority is not UNSET:
            field_dict["priority"] = priority
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if resolution_notes is not UNSET:
            field_dict["resolutionNotes"] = resolution_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateTicketBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateTicketBodyStatus(_status)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, UpdateTicketBodyPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = UpdateTicketBodyPriority(_priority)

        assigned_to = d.pop("assignedTo", UNSET)

        resolution_notes = d.pop("resolutionNotes", UNSET)

        update_ticket_body = cls(
            title=title,
            description=description,
            status=status,
            priority=priority,
            assigned_to=assigned_to,
            resolution_notes=resolution_notes,
        )

        update_ticket_body.additional_properties = d
        return update_ticket_body

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
