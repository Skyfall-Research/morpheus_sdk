from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_receiving_transaction_items_item_location_type_0 import (
        WMSReceivingTransactionItemsItemLocationType0,
    )


T = TypeVar("T", bound="WMSReceivingTransactionItemsItem")


@_attrs_define
class WMSReceivingTransactionItemsItem:
    """Individual item details within the receiving transaction

    Attributes:
        sku (Union[Unset, str]): Stock keeping unit for this item Example: ABC-123-XL.
        product_name (Union[Unset, str]): Product name for this item Example: Premium Wireless Headphones.
        expected_quantity (Union[Unset, float]): Expected quantity to receive Example: 50.
        received_quantity (Union[Unset, float]): Actual quantity received Example: 48.
        unit_of_measure (Union[Unset, str]): Unit of measure for this item Example: EA.
        lot_number (Union[None, Unset, str]): Lot number for batch tracking Example: LOT-2024-Q4-001.
        serial_numbers (Union[Unset, list[str]]): Serial numbers for individual item tracking Example: ['SN001',
            'SN002', 'SN003'].
        condition (Union[None, Unset, str]): Condition assessment of the item Example: GOOD.
        location (Union['WMSReceivingTransactionItemsItemLocationType0', None, Unset]): Storage location assignment for
            this item
    """

    sku: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    expected_quantity: Union[Unset, float] = UNSET
    received_quantity: Union[Unset, float] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    lot_number: Union[None, Unset, str] = UNSET
    serial_numbers: Union[Unset, list[str]] = UNSET
    condition: Union[None, Unset, str] = UNSET
    location: Union["WMSReceivingTransactionItemsItemLocationType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wms_receiving_transaction_items_item_location_type_0 import (
            WMSReceivingTransactionItemsItemLocationType0,
        )

        sku = self.sku

        product_name = self.product_name

        expected_quantity = self.expected_quantity

        received_quantity = self.received_quantity

        unit_of_measure = self.unit_of_measure

        lot_number: Union[None, Unset, str]
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        serial_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.serial_numbers, Unset):
            serial_numbers = self.serial_numbers

        condition: Union[None, Unset, str]
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, WMSReceivingTransactionItemsItemLocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku is not UNSET:
            field_dict["sku"] = sku
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if expected_quantity is not UNSET:
            field_dict["expectedQuantity"] = expected_quantity
        if received_quantity is not UNSET:
            field_dict["receivedQuantity"] = received_quantity
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if serial_numbers is not UNSET:
            field_dict["serialNumbers"] = serial_numbers
        if condition is not UNSET:
            field_dict["condition"] = condition
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_receiving_transaction_items_item_location_type_0 import (
            WMSReceivingTransactionItemsItemLocationType0,
        )

        d = dict(src_dict)
        sku = d.pop("sku", UNSET)

        product_name = d.pop("productName", UNSET)

        expected_quantity = d.pop("expectedQuantity", UNSET)

        received_quantity = d.pop("receivedQuantity", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        def _parse_lot_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))

        serial_numbers = cast(list[str], d.pop("serialNumbers", UNSET))

        def _parse_condition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        condition = _parse_condition(d.pop("condition", UNSET))

        def _parse_location(data: object) -> Union["WMSReceivingTransactionItemsItemLocationType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = WMSReceivingTransactionItemsItemLocationType0.from_dict(data)

                return location_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSReceivingTransactionItemsItemLocationType0", None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))

        wms_receiving_transaction_items_item = cls(
            sku=sku,
            product_name=product_name,
            expected_quantity=expected_quantity,
            received_quantity=received_quantity,
            unit_of_measure=unit_of_measure,
            lot_number=lot_number,
            serial_numbers=serial_numbers,
            condition=condition,
            location=location,
        )

        wms_receiving_transaction_items_item.additional_properties = d
        return wms_receiving_transaction_items_item

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
