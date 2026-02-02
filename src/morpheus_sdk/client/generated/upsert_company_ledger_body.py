from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpsertCompanyLedgerBody")


@_attrs_define
class UpsertCompanyLedgerBody:
    """
    Attributes:
        cash (Union[Unset, float]): Company cash position Default: 0.0. Example: 25000.
        total_receivables (Union[Unset, float]): Total accounts receivable Default: 0.0. Example: 45000.
        total_payables (Union[Unset, float]): Total accounts payable Default: 0.0. Example: 18000.
    """

    cash: Union[Unset, float] = 0.0
    total_receivables: Union[Unset, float] = 0.0
    total_payables: Union[Unset, float] = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cash = self.cash

        total_receivables = self.total_receivables

        total_payables = self.total_payables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cash is not UNSET:
            field_dict["cash"] = cash
        if total_receivables is not UNSET:
            field_dict["totalReceivables"] = total_receivables
        if total_payables is not UNSET:
            field_dict["totalPayables"] = total_payables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cash = d.pop("cash", UNSET)

        total_receivables = d.pop("totalReceivables", UNSET)

        total_payables = d.pop("totalPayables", UNSET)

        upsert_company_ledger_body = cls(
            cash=cash,
            total_receivables=total_receivables,
            total_payables=total_payables,
        )

        upsert_company_ledger_body.additional_properties = d
        return upsert_company_ledger_body

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
