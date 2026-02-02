from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompanyLedgersSummaryResponse200Data")


@_attrs_define
class GetCompanyLedgersSummaryResponse200Data:
    """
    Attributes:
        total_cash (Union[Unset, float]): Total cash across all ledgers Example: 125000.
        total_receivables (Union[Unset, float]): Total receivables across all ledgers Example: 285000.
        total_payables (Union[Unset, float]): Total payables across all ledgers Example: 165000.
        total_net_position (Union[Unset, float]): Total net position across all ledgers Example: 245000.
        ledger_count (Union[Unset, float]): Total number of ledgers Example: 1.
        positive_ledgers (Union[Unset, float]): Number of ledgers with positive net position Example: 1.
        negative_ledgers (Union[Unset, float]): Number of ledgers with negative net position
    """

    total_cash: Union[Unset, float] = UNSET
    total_receivables: Union[Unset, float] = UNSET
    total_payables: Union[Unset, float] = UNSET
    total_net_position: Union[Unset, float] = UNSET
    ledger_count: Union[Unset, float] = UNSET
    positive_ledgers: Union[Unset, float] = UNSET
    negative_ledgers: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_cash = self.total_cash

        total_receivables = self.total_receivables

        total_payables = self.total_payables

        total_net_position = self.total_net_position

        ledger_count = self.ledger_count

        positive_ledgers = self.positive_ledgers

        negative_ledgers = self.negative_ledgers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_cash is not UNSET:
            field_dict["totalCash"] = total_cash
        if total_receivables is not UNSET:
            field_dict["totalReceivables"] = total_receivables
        if total_payables is not UNSET:
            field_dict["totalPayables"] = total_payables
        if total_net_position is not UNSET:
            field_dict["totalNetPosition"] = total_net_position
        if ledger_count is not UNSET:
            field_dict["ledgerCount"] = ledger_count
        if positive_ledgers is not UNSET:
            field_dict["positiveLedgers"] = positive_ledgers
        if negative_ledgers is not UNSET:
            field_dict["negativeLedgers"] = negative_ledgers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_cash = d.pop("totalCash", UNSET)

        total_receivables = d.pop("totalReceivables", UNSET)

        total_payables = d.pop("totalPayables", UNSET)

        total_net_position = d.pop("totalNetPosition", UNSET)

        ledger_count = d.pop("ledgerCount", UNSET)

        positive_ledgers = d.pop("positiveLedgers", UNSET)

        negative_ledgers = d.pop("negativeLedgers", UNSET)

        get_company_ledgers_summary_response_200_data = cls(
            total_cash=total_cash,
            total_receivables=total_receivables,
            total_payables=total_payables,
            total_net_position=total_net_position,
            ledger_count=ledger_count,
            positive_ledgers=positive_ledgers,
            negative_ledgers=negative_ledgers,
        )

        get_company_ledgers_summary_response_200_data.additional_properties = d
        return get_company_ledgers_summary_response_200_data

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
