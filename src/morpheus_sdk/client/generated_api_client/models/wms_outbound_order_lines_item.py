from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wms_outbound_order_lines_item_line_status import WMSOutboundOrderLinesItemLineStatus
from ..models.wms_outbound_order_lines_item_unit_of_measure import WMSOutboundOrderLinesItemUnitOfMeasure
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_outbound_order_lines_item_allocations_item import WMSOutboundOrderLinesItemAllocationsItem


T = TypeVar("T", bound="WMSOutboundOrderLinesItem")


@_attrs_define
class WMSOutboundOrderLinesItem:
    """Individual line item with quantity tracking and allocation details

    Attributes:
        line_number (float): Sequential line identifier within order (used for array updates) Example: 1.
        item_id (str): SKU/product code from inventory system Example: SKU-WIDGET-001.
        item_description (str): Product display name Example: Premium Widget Assembly.
        ordered_quantity (float): Customer requested amount Example: 25.
        unit_of_measure (WMSOutboundOrderLinesItemUnitOfMeasure): Unit of measure code Example: EA.
        line_status (WMSOutboundOrderLinesItemLineStatus): Individual line status (updated automatically during
            allocation and picking) Example: PICKED.
        allocated_quantity (Union[Unset, float]): System allocated quantity (set during allocation process) Example: 25.
        picked_quantity (Union[Unset, float]): Actually picked amount (updated during picking) Example: 23.
        unit_price (Union[Unset, float]): Price per unit (optional) Example: 49.99.
        allocations (Union[Unset, list['WMSOutboundOrderLinesItemAllocationsItem']]): Optional bin-level allocation
            details
        special_instructions (Union[Unset, str]): Line-specific handling notes Example: Handle with care - fragile
            items.
    """

    line_number: float
    item_id: str
    item_description: str
    ordered_quantity: float
    unit_of_measure: WMSOutboundOrderLinesItemUnitOfMeasure
    line_status: WMSOutboundOrderLinesItemLineStatus
    allocated_quantity: Union[Unset, float] = UNSET
    picked_quantity: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    allocations: Union[Unset, list["WMSOutboundOrderLinesItemAllocationsItem"]] = UNSET
    special_instructions: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        item_id = self.item_id

        item_description = self.item_description

        ordered_quantity = self.ordered_quantity

        unit_of_measure = self.unit_of_measure.value

        line_status = self.line_status.value

        allocated_quantity = self.allocated_quantity

        picked_quantity = self.picked_quantity

        unit_price = self.unit_price

        allocations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allocations, Unset):
            allocations = []
            for allocations_item_data in self.allocations:
                allocations_item = allocations_item_data.to_dict()
                allocations.append(allocations_item)

        special_instructions = self.special_instructions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineNumber": line_number,
                "itemId": item_id,
                "itemDescription": item_description,
                "orderedQuantity": ordered_quantity,
                "unitOfMeasure": unit_of_measure,
                "lineStatus": line_status,
            }
        )
        if allocated_quantity is not UNSET:
            field_dict["allocatedQuantity"] = allocated_quantity
        if picked_quantity is not UNSET:
            field_dict["pickedQuantity"] = picked_quantity
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if allocations is not UNSET:
            field_dict["allocations"] = allocations
        if special_instructions is not UNSET:
            field_dict["specialInstructions"] = special_instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_outbound_order_lines_item_allocations_item import WMSOutboundOrderLinesItemAllocationsItem

        d = dict(src_dict)
        line_number = d.pop("lineNumber")

        item_id = d.pop("itemId")

        item_description = d.pop("itemDescription")

        ordered_quantity = d.pop("orderedQuantity")

        unit_of_measure = WMSOutboundOrderLinesItemUnitOfMeasure(d.pop("unitOfMeasure"))

        line_status = WMSOutboundOrderLinesItemLineStatus(d.pop("lineStatus"))

        allocated_quantity = d.pop("allocatedQuantity", UNSET)

        picked_quantity = d.pop("pickedQuantity", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        allocations = []
        _allocations = d.pop("allocations", UNSET)
        for allocations_item_data in _allocations or []:
            allocations_item = WMSOutboundOrderLinesItemAllocationsItem.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        special_instructions = d.pop("specialInstructions", UNSET)

        wms_outbound_order_lines_item = cls(
            line_number=line_number,
            item_id=item_id,
            item_description=item_description,
            ordered_quantity=ordered_quantity,
            unit_of_measure=unit_of_measure,
            line_status=line_status,
            allocated_quantity=allocated_quantity,
            picked_quantity=picked_quantity,
            unit_price=unit_price,
            allocations=allocations,
            special_instructions=special_instructions,
        )

        wms_outbound_order_lines_item.additional_properties = d
        return wms_outbound_order_lines_item

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
