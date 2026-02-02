import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.itsm_ticket_impact import ItsmTicketImpact
from ..models.itsm_ticket_priority import ItsmTicketPriority
from ..models.itsm_ticket_status import ItsmTicketStatus
from ..models.itsm_ticket_type import ItsmTicketType
from ..models.itsm_ticket_urgency import ItsmTicketUrgency
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.itsm_ticket_attachments_item import ItsmTicketAttachmentsItem
    from ..models.itsm_ticket_metadata import ItsmTicketMetadata
    from ..models.itsm_ticket_world_ref import ItsmTicketWorldRef
    from ..models.work_note import WorkNote


T = TypeVar("T", bound="ItsmTicket")


@_attrs_define
class ItsmTicket:
    """ITSM ticket for managing incidents, service requests, problems, and changes

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        world_ref (ItsmTicketWorldRef):
        title (str): Brief descriptive title of the ticket Example: Email server not responding.
        description (str): Detailed description of the issue or request Example: Users unable to access email. Server
            appears to be down since 9:00 AM..
        requester (str): User ID who created the ticket Example: 507f1f77bcf86cd799439020.
        status (ItsmTicketStatus): Current status of the ticket Example: in_progress.
        priority (ItsmTicketPriority): Priority level of the ticket Example: high.
        impact (ItsmTicketImpact): Business impact level Example: high.
        urgency (ItsmTicketUrgency): Time sensitivity level Example: medium.
        type_ (ItsmTicketType): Type of ITSM ticket Example: incident.
        created_at (datetime.datetime): When the ticket was created Example: 2024-01-15T09:15:00.000Z.
        updated_at (datetime.datetime): When the ticket was last updated Example: 2024-01-15T11:45:00.000Z.
        assigned_to (Union[None, Unset, str]): User ID assigned to handle the ticket Example: 507f1f77bcf86cd799439021.
        category (Union[None, Unset, str]): Department or category classification Example: Infrastructure.
        attachments (Union[Unset, list['ItsmTicketAttachmentsItem']]): File attachments related to the ticket
        resolution_notes (Union[None, Unset, str]): Notes describing how the ticket was resolved Example: Cleared disk
            space on mail server. Service restored at 11:45 AM..
        work_notes (Union[Unset, list['WorkNote']]): Array of work notes documenting progress and actions
        metadata (Union[Unset, ItsmTicketMetadata]): Additional context and system metadata
    """

    field_id: str
    world_ref: "ItsmTicketWorldRef"
    title: str
    description: str
    requester: str
    status: ItsmTicketStatus
    priority: ItsmTicketPriority
    impact: ItsmTicketImpact
    urgency: ItsmTicketUrgency
    type_: ItsmTicketType
    created_at: datetime.datetime
    updated_at: datetime.datetime
    assigned_to: Union[None, Unset, str] = UNSET
    category: Union[None, Unset, str] = UNSET
    attachments: Union[Unset, list["ItsmTicketAttachmentsItem"]] = UNSET
    resolution_notes: Union[None, Unset, str] = UNSET
    work_notes: Union[Unset, list["WorkNote"]] = UNSET
    metadata: Union[Unset, "ItsmTicketMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_ref = self.world_ref.to_dict()

        title = self.title

        description = self.description

        requester = self.requester

        status = self.status.value

        priority = self.priority.value

        impact = self.impact.value

        urgency = self.urgency.value

        type_ = self.type_.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        assigned_to: Union[None, Unset, str]
        if isinstance(self.assigned_to, Unset):
            assigned_to = UNSET
        else:
            assigned_to = self.assigned_to

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        attachments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        resolution_notes: Union[None, Unset, str]
        if isinstance(self.resolution_notes, Unset):
            resolution_notes = UNSET
        else:
            resolution_notes = self.resolution_notes

        work_notes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.work_notes, Unset):
            work_notes = []
            for work_notes_item_data in self.work_notes:
                work_notes_item = work_notes_item_data.to_dict()
                work_notes.append(work_notes_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "worldRef": world_ref,
                "title": title,
                "description": description,
                "requester": requester,
                "status": status,
                "priority": priority,
                "impact": impact,
                "urgency": urgency,
                "type": type_,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if category is not UNSET:
            field_dict["category"] = category
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if resolution_notes is not UNSET:
            field_dict["resolutionNotes"] = resolution_notes
        if work_notes is not UNSET:
            field_dict["workNotes"] = work_notes
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.itsm_ticket_attachments_item import ItsmTicketAttachmentsItem
        from ..models.itsm_ticket_metadata import ItsmTicketMetadata
        from ..models.itsm_ticket_world_ref import ItsmTicketWorldRef
        from ..models.work_note import WorkNote

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_ref = ItsmTicketWorldRef.from_dict(d.pop("worldRef"))

        title = d.pop("title")

        description = d.pop("description")

        requester = d.pop("requester")

        status = ItsmTicketStatus(d.pop("status"))

        priority = ItsmTicketPriority(d.pop("priority"))

        impact = ItsmTicketImpact(d.pop("impact"))

        urgency = ItsmTicketUrgency(d.pop("urgency"))

        type_ = ItsmTicketType(d.pop("type"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_assigned_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assigned_to = _parse_assigned_to(d.pop("assignedTo", UNSET))

        def _parse_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category = _parse_category(d.pop("category", UNSET))

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = ItsmTicketAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        def _parse_resolution_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resolution_notes = _parse_resolution_notes(d.pop("resolutionNotes", UNSET))

        work_notes = []
        _work_notes = d.pop("workNotes", UNSET)
        for work_notes_item_data in _work_notes or []:
            work_notes_item = WorkNote.from_dict(work_notes_item_data)

            work_notes.append(work_notes_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ItsmTicketMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ItsmTicketMetadata.from_dict(_metadata)

        itsm_ticket = cls(
            field_id=field_id,
            world_ref=world_ref,
            title=title,
            description=description,
            requester=requester,
            status=status,
            priority=priority,
            impact=impact,
            urgency=urgency,
            type_=type_,
            created_at=created_at,
            updated_at=updated_at,
            assigned_to=assigned_to,
            category=category,
            attachments=attachments,
            resolution_notes=resolution_notes,
            work_notes=work_notes,
            metadata=metadata,
        )

        itsm_ticket.additional_properties = d
        return itsm_ticket

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
