from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInventoryMovementReportResponse200DataTransactionsByTypeItem")


@_attrs_define
class GetWMSInventoryMovementReportResponse200DataTransactionsByTypeItem:
    """
    Attributes:
        transaction_type (Union[Unset, str]): Type of inventory transaction Example: PUTAWAY.
        count (Union[Unset, int]): Number of transactions of this type Example: 425.
        total_quantity (Union[Unset, float]): Total quantity moved in this transaction type Example: 12750.
    """

    transaction_type: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    total_quantity: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_type = self.transaction_type

        count = self.count

        total_quantity = self.total_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type
        if count is not UNSET:
            field_dict["count"] = count
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transaction_type = d.pop("transactionType", UNSET)

        count = d.pop("count", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        get_wms_inventory_movement_report_response_200_data_transactions_by_type_item = cls(
            transaction_type=transaction_type,
            count=count,
            total_quantity=total_quantity,
        )

        get_wms_inventory_movement_report_response_200_data_transactions_by_type_item.additional_properties = d
        return get_wms_inventory_movement_report_response_200_data_transactions_by_type_item

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
