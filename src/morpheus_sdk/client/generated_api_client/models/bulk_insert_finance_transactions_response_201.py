from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_insert_finance_transactions_response_201_data import BulkInsertFinanceTransactionsResponse201Data


T = TypeVar("T", bound="BulkInsertFinanceTransactionsResponse201")


@_attrs_define
class BulkInsertFinanceTransactionsResponse201:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        status (Union[Unset, int]):  Example: 201.
        message (Union[Unset, str]):  Example: Bulk insert completed successfully.
        data (Union[Unset, BulkInsertFinanceTransactionsResponse201Data]):
    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    data: Union[Unset, "BulkInsertFinanceTransactionsResponse201Data"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        message = self.message

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_insert_finance_transactions_response_201_data import (
            BulkInsertFinanceTransactionsResponse201Data,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, BulkInsertFinanceTransactionsResponse201Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = BulkInsertFinanceTransactionsResponse201Data.from_dict(_data)

        bulk_insert_finance_transactions_response_201 = cls(
            success=success,
            status=status,
            message=message,
            data=data,
        )

        bulk_insert_finance_transactions_response_201.additional_properties = d
        return bulk_insert_finance_transactions_response_201

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
