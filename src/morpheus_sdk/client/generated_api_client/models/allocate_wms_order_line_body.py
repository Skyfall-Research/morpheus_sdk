from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allocate_wms_order_line_body_allocation_details_item import (
        AllocateWMSOrderLineBodyAllocationDetailsItem,
    )


T = TypeVar("T", bound="AllocateWMSOrderLineBody")


@_attrs_define
class AllocateWMSOrderLineBody:
    """
    Attributes:
        allocated_quantity (float): Total allocated amount Example: 20.
        allocation_details (Union[Unset, list['AllocateWMSOrderLineBodyAllocationDetailsItem']]): Optional bin-level
            allocations
    """

    allocated_quantity: float
    allocation_details: Union[Unset, list["AllocateWMSOrderLineBodyAllocationDetailsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocated_quantity = self.allocated_quantity

        allocation_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allocation_details, Unset):
            allocation_details = []
            for allocation_details_item_data in self.allocation_details:
                allocation_details_item = allocation_details_item_data.to_dict()
                allocation_details.append(allocation_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allocatedQuantity": allocated_quantity,
            }
        )
        if allocation_details is not UNSET:
            field_dict["allocationDetails"] = allocation_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocate_wms_order_line_body_allocation_details_item import (
            AllocateWMSOrderLineBodyAllocationDetailsItem,
        )

        d = dict(src_dict)
        allocated_quantity = d.pop("allocatedQuantity")

        allocation_details = []
        _allocation_details = d.pop("allocationDetails", UNSET)
        for allocation_details_item_data in _allocation_details or []:
            allocation_details_item = AllocateWMSOrderLineBodyAllocationDetailsItem.from_dict(
                allocation_details_item_data
            )

            allocation_details.append(allocation_details_item)

        allocate_wms_order_line_body = cls(
            allocated_quantity=allocated_quantity,
            allocation_details=allocation_details,
        )

        allocate_wms_order_line_body.additional_properties = d
        return allocate_wms_order_line_body

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
