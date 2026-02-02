from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_item_to_wms_receiving_transaction_body_location import (
        AddItemToWMSReceivingTransactionBodyLocation,
    )


T = TypeVar("T", bound="AddItemToWMSReceivingTransactionBody")


@_attrs_define
class AddItemToWMSReceivingTransactionBody:
    """
    Attributes:
        sku (str): Stock keeping unit code for the item Example: ABC-123-XL.
        product_name (str): Human-readable product name Example: Premium Wireless Headphones.
        expected_quantity (float): Expected quantity to be received Example: 50.
        received_quantity (float): Actual quantity received Example: 48.
        unit_of_measure (str): Unit of measure for quantities Example: EA.
        lot_number (Union[Unset, str]): Lot number for batch tracking Example: LOT-2024-Q4-001.
        serial_numbers (Union[Unset, list[str]]): Array of serial numbers for individual item tracking Example:
            ['SN001', 'SN002', 'SN003'].
        condition (Union[Unset, str]): Condition assessment of received items Example: GOOD.
        location (Union[Unset, AddItemToWMSReceivingTransactionBodyLocation]): Storage location assignment for the item
    """

    sku: str
    product_name: str
    expected_quantity: float
    received_quantity: float
    unit_of_measure: str
    lot_number: Union[Unset, str] = UNSET
    serial_numbers: Union[Unset, list[str]] = UNSET
    condition: Union[Unset, str] = UNSET
    location: Union[Unset, "AddItemToWMSReceivingTransactionBodyLocation"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sku = self.sku

        product_name = self.product_name

        expected_quantity = self.expected_quantity

        received_quantity = self.received_quantity

        unit_of_measure = self.unit_of_measure

        lot_number = self.lot_number

        serial_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.serial_numbers, Unset):
            serial_numbers = self.serial_numbers

        condition = self.condition

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sku": sku,
                "productName": product_name,
                "expectedQuantity": expected_quantity,
                "receivedQuantity": received_quantity,
                "unitOfMeasure": unit_of_measure,
            }
        )
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
        from ..models.add_item_to_wms_receiving_transaction_body_location import (
            AddItemToWMSReceivingTransactionBodyLocation,
        )

        d = dict(src_dict)
        sku = d.pop("sku")

        product_name = d.pop("productName")

        expected_quantity = d.pop("expectedQuantity")

        received_quantity = d.pop("receivedQuantity")

        unit_of_measure = d.pop("unitOfMeasure")

        lot_number = d.pop("lotNumber", UNSET)

        serial_numbers = cast(list[str], d.pop("serialNumbers", UNSET))

        condition = d.pop("condition", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, AddItemToWMSReceivingTransactionBodyLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = AddItemToWMSReceivingTransactionBodyLocation.from_dict(_location)

        add_item_to_wms_receiving_transaction_body = cls(
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

        add_item_to_wms_receiving_transaction_body.additional_properties = d
        return add_item_to_wms_receiving_transaction_body

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
