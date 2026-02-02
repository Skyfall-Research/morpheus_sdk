from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFinanceStatsResponse200DataSummary")


@_attrs_define
class GetFinanceStatsResponse200DataSummary:
    """Overall financial summary

    Attributes:
        total_incoming (Union[Unset, float]):  Example: 75000.
        total_outgoing (Union[Unset, float]):  Example: 32000.
        net_balance (Union[Unset, float]):  Example: 43000.
        transaction_count (Union[Unset, float]):  Example: 68.
        avg_transaction_amount (Union[Unset, float]):  Example: 1573.53.
    """

    total_incoming: Union[Unset, float] = UNSET
    total_outgoing: Union[Unset, float] = UNSET
    net_balance: Union[Unset, float] = UNSET
    transaction_count: Union[Unset, float] = UNSET
    avg_transaction_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_incoming = self.total_incoming

        total_outgoing = self.total_outgoing

        net_balance = self.net_balance

        transaction_count = self.transaction_count

        avg_transaction_amount = self.avg_transaction_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_incoming is not UNSET:
            field_dict["totalIncoming"] = total_incoming
        if total_outgoing is not UNSET:
            field_dict["totalOutgoing"] = total_outgoing
        if net_balance is not UNSET:
            field_dict["netBalance"] = net_balance
        if transaction_count is not UNSET:
            field_dict["transactionCount"] = transaction_count
        if avg_transaction_amount is not UNSET:
            field_dict["avgTransactionAmount"] = avg_transaction_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_incoming = d.pop("totalIncoming", UNSET)

        total_outgoing = d.pop("totalOutgoing", UNSET)

        net_balance = d.pop("netBalance", UNSET)

        transaction_count = d.pop("transactionCount", UNSET)

        avg_transaction_amount = d.pop("avgTransactionAmount", UNSET)

        get_finance_stats_response_200_data_summary = cls(
            total_incoming=total_incoming,
            total_outgoing=total_outgoing,
            net_balance=net_balance,
            transaction_count=transaction_count,
            avg_transaction_amount=avg_transaction_amount,
        )

        get_finance_stats_response_200_data_summary.additional_properties = d
        return get_finance_stats_response_200_data_summary

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
