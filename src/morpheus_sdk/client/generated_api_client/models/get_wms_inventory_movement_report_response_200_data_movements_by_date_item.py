import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInventoryMovementReportResponse200DataMovementsByDateItem")


@_attrs_define
class GetWMSInventoryMovementReportResponse200DataMovementsByDateItem:
    """
    Attributes:
        date (Union[Unset, datetime.date]): Date of movements Example: 2024-11-15.
        transaction_count (Union[Unset, int]): Number of transactions on this date Example: 127.
        total_quantity (Union[Unset, float]): Total quantity moved on this date Example: 3845.
    """

    date: Union[Unset, datetime.date] = UNSET
    transaction_count: Union[Unset, int] = UNSET
    total_quantity: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        transaction_count = self.transaction_count

        total_quantity = self.total_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if transaction_count is not UNSET:
            field_dict["transactionCount"] = transaction_count
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        transaction_count = d.pop("transactionCount", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        get_wms_inventory_movement_report_response_200_data_movements_by_date_item = cls(
            date=date,
            transaction_count=transaction_count,
            total_quantity=total_quantity,
        )

        get_wms_inventory_movement_report_response_200_data_movements_by_date_item.additional_properties = d
        return get_wms_inventory_movement_report_response_200_data_movements_by_date_item

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
