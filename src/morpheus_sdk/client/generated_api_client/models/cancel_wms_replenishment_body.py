from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CancelWMSReplenishmentBody")


@_attrs_define
class CancelWMSReplenishmentBody:
    """
    Attributes:
        reason (str): Reason for cancellation Example: Product discontinued.
        cancelled_by (str): User ID who cancelled the replenishment Example: MGR-002.
    """

    reason: str
    cancelled_by: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        cancelled_by = self.cancelled_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "cancelledBy": cancelled_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        cancelled_by = d.pop("cancelledBy")

        cancel_wms_replenishment_body = cls(
            reason=reason,
            cancelled_by=cancelled_by,
        )

        cancel_wms_replenishment_body.additional_properties = d
        return cancel_wms_replenishment_body

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
