from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.apply_erp_payment_allocations_body_allocations_item import (
        ApplyERPPaymentAllocationsBodyAllocationsItem,
    )


T = TypeVar("T", bound="ApplyERPPaymentAllocationsBody")


@_attrs_define
class ApplyERPPaymentAllocationsBody:
    """
    Attributes:
        allocations (list['ApplyERPPaymentAllocationsBodyAllocationsItem']): Array of payment allocations to apply
    """

    allocations: list["ApplyERPPaymentAllocationsBodyAllocationsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocations = []
        for allocations_item_data in self.allocations:
            allocations_item = allocations_item_data.to_dict()
            allocations.append(allocations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allocations": allocations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apply_erp_payment_allocations_body_allocations_item import (
            ApplyERPPaymentAllocationsBodyAllocationsItem,
        )

        d = dict(src_dict)
        allocations = []
        _allocations = d.pop("allocations")
        for allocations_item_data in _allocations:
            allocations_item = ApplyERPPaymentAllocationsBodyAllocationsItem.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        apply_erp_payment_allocations_body = cls(
            allocations=allocations,
        )

        apply_erp_payment_allocations_body.additional_properties = d
        return apply_erp_payment_allocations_body

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
