from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_insert_finance_transactions_body_transactions_item import (
        BulkInsertFinanceTransactionsBodyTransactionsItem,
    )


T = TypeVar("T", bound="BulkInsertFinanceTransactionsBody")


@_attrs_define
class BulkInsertFinanceTransactionsBody:
    """
    Attributes:
        transactions (list['BulkInsertFinanceTransactionsBodyTransactionsItem']): Array of finance transactions to
            insert
    """

    transactions: list["BulkInsertFinanceTransactionsBodyTransactionsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()
            transactions.append(transactions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactions": transactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_insert_finance_transactions_body_transactions_item import (
            BulkInsertFinanceTransactionsBodyTransactionsItem,
        )

        d = dict(src_dict)
        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = BulkInsertFinanceTransactionsBodyTransactionsItem.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        bulk_insert_finance_transactions_body = cls(
            transactions=transactions,
        )

        bulk_insert_finance_transactions_body.additional_properties = d
        return bulk_insert_finance_transactions_body

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
