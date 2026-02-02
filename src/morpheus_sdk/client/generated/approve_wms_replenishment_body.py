from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApproveWMSReplenishmentBody")


@_attrs_define
class ApproveWMSReplenishmentBody:
    """
    Attributes:
        approved_by (str): User ID of the approving manager Example: MGR-001.
        approved_quantity (Union[Unset, float]): Approved quantity (if different from suggested) Example: 120.
    """

    approved_by: str
    approved_quantity: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approved_by = self.approved_by

        approved_quantity = self.approved_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approvedBy": approved_by,
            }
        )
        if approved_quantity is not UNSET:
            field_dict["approvedQuantity"] = approved_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approved_by = d.pop("approvedBy")

        approved_quantity = d.pop("approvedQuantity", UNSET)

        approve_wms_replenishment_body = cls(
            approved_by=approved_by,
            approved_quantity=approved_quantity,
        )

        approve_wms_replenishment_body.additional_properties = d
        return approve_wms_replenishment_body

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
