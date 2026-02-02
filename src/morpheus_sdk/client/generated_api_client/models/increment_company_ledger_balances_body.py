from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncrementCompanyLedgerBalancesBody")


@_attrs_define
class IncrementCompanyLedgerBalancesBody:
    """
    Attributes:
        cash_delta (Union[Unset, float]): Amount to add/subtract from cash (positive = increase, negative = decrease)
            Example: 5000.
        receivables_delta (Union[Unset, float]): Amount to add/subtract from receivables (positive = increase, negative
            = decrease) Example: -2000.
        payables_delta (Union[Unset, float]): Amount to add/subtract from payables (positive = increase, negative =
            decrease) Example: 1500.
    """

    cash_delta: Union[Unset, float] = UNSET
    receivables_delta: Union[Unset, float] = UNSET
    payables_delta: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cash_delta = self.cash_delta

        receivables_delta = self.receivables_delta

        payables_delta = self.payables_delta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cash_delta is not UNSET:
            field_dict["cashDelta"] = cash_delta
        if receivables_delta is not UNSET:
            field_dict["receivablesDelta"] = receivables_delta
        if payables_delta is not UNSET:
            field_dict["payablesDelta"] = payables_delta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cash_delta = d.pop("cashDelta", UNSET)

        receivables_delta = d.pop("receivablesDelta", UNSET)

        payables_delta = d.pop("payablesDelta", UNSET)

        increment_company_ledger_balances_body = cls(
            cash_delta=cash_delta,
            receivables_delta=receivables_delta,
            payables_delta=payables_delta,
        )

        increment_company_ledger_balances_body.additional_properties = d
        return increment_company_ledger_balances_body

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
