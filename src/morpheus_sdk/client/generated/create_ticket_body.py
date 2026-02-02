from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_ticket_body_priority import CreateTicketBodyPriority
from ..models.create_ticket_body_type import CreateTicketBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTicketBody")


@_attrs_define
class CreateTicketBody:
    """
    Attributes:
        title (str): Brief title describing the issue or request Example: Database connection timeout.
        description (str): Detailed description of the issue Example: Users experiencing timeouts when accessing the
            customer portal.
        requester (str): User ID of the person creating the ticket Example: 507f1f77bcf86cd799439020.
        type_ (Union[Unset, CreateTicketBodyType]):  Default: CreateTicketBodyType.INCIDENT. Example: incident.
        priority (Union[Unset, CreateTicketBodyPriority]):  Default: CreateTicketBodyPriority.MEDIUM. Example: high.
        category (Union[Unset, str]):  Example: Database.
    """

    title: str
    description: str
    requester: str
    type_: Union[Unset, CreateTicketBodyType] = CreateTicketBodyType.INCIDENT
    priority: Union[Unset, CreateTicketBodyPriority] = CreateTicketBodyPriority.MEDIUM
    category: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        requester = self.requester

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "description": description,
                "requester": requester,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if priority is not UNSET:
            field_dict["priority"] = priority
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        description = d.pop("description")

        requester = d.pop("requester")

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CreateTicketBodyType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateTicketBodyType(_type_)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, CreateTicketBodyPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateTicketBodyPriority(_priority)

        category = d.pop("category", UNSET)

        create_ticket_body = cls(
            title=title,
            description=description,
            requester=requester,
            type_=type_,
            priority=priority,
            category=category,
        )

        create_ticket_body.additional_properties = d
        return create_ticket_body

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
