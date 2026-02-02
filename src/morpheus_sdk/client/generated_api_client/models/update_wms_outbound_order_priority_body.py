from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_wms_outbound_order_priority_body_priority import UpdateWMSOutboundOrderPriorityBodyPriority

T = TypeVar("T", bound="UpdateWMSOutboundOrderPriorityBody")


@_attrs_define
class UpdateWMSOutboundOrderPriorityBody:
    """
    Attributes:
        priority (UpdateWMSOutboundOrderPriorityBodyPriority): New priority level for the order Example: RUSH.
    """

    priority: UpdateWMSOutboundOrderPriorityBodyPriority
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority = self.priority.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "priority": priority,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        priority = UpdateWMSOutboundOrderPriorityBodyPriority(d.pop("priority"))

        update_wms_outbound_order_priority_body = cls(
            priority=priority,
        )

        update_wms_outbound_order_priority_body.additional_properties = d
        return update_wms_outbound_order_priority_body

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
