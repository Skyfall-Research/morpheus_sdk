from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_finance_stats_response_200_data_by_partner_item import GetFinanceStatsResponse200DataByPartnerItem
    from ..models.get_finance_stats_response_200_data_by_type import GetFinanceStatsResponse200DataByType
    from ..models.get_finance_stats_response_200_data_summary import GetFinanceStatsResponse200DataSummary


T = TypeVar("T", bound="GetFinanceStatsResponse200Data")


@_attrs_define
class GetFinanceStatsResponse200Data:
    """
    Attributes:
        by_type (Union[Unset, GetFinanceStatsResponse200DataByType]): Transaction statistics grouped by type Example:
            {'payment_in': {'count': 45, 'totalAmount': 75000, 'avgAmount': 1666.67}, 'payment_out': {'count': 23,
            'totalAmount': 32000, 'avgAmount': 1391.3}}.
        by_partner (Union[Unset, list['GetFinanceStatsResponse200DataByPartnerItem']]): Transaction statistics grouped
            by partner
        summary (Union[Unset, GetFinanceStatsResponse200DataSummary]): Overall financial summary
    """

    by_type: Union[Unset, "GetFinanceStatsResponse200DataByType"] = UNSET
    by_partner: Union[Unset, list["GetFinanceStatsResponse200DataByPartnerItem"]] = UNSET
    summary: Union[Unset, "GetFinanceStatsResponse200DataSummary"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.by_type, Unset):
            by_type = self.by_type.to_dict()

        by_partner: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.by_partner, Unset):
            by_partner = []
            for by_partner_item_data in self.by_partner:
                by_partner_item = by_partner_item_data.to_dict()
                by_partner.append(by_partner_item)

        summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_type is not UNSET:
            field_dict["byType"] = by_type
        if by_partner is not UNSET:
            field_dict["byPartner"] = by_partner
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_finance_stats_response_200_data_by_partner_item import (
            GetFinanceStatsResponse200DataByPartnerItem,
        )
        from ..models.get_finance_stats_response_200_data_by_type import GetFinanceStatsResponse200DataByType
        from ..models.get_finance_stats_response_200_data_summary import GetFinanceStatsResponse200DataSummary

        d = dict(src_dict)
        _by_type = d.pop("byType", UNSET)
        by_type: Union[Unset, GetFinanceStatsResponse200DataByType]
        if isinstance(_by_type, Unset):
            by_type = UNSET
        else:
            by_type = GetFinanceStatsResponse200DataByType.from_dict(_by_type)

        by_partner = []
        _by_partner = d.pop("byPartner", UNSET)
        for by_partner_item_data in _by_partner or []:
            by_partner_item = GetFinanceStatsResponse200DataByPartnerItem.from_dict(by_partner_item_data)

            by_partner.append(by_partner_item)

        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, GetFinanceStatsResponse200DataSummary]
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = GetFinanceStatsResponse200DataSummary.from_dict(_summary)

        get_finance_stats_response_200_data = cls(
            by_type=by_type,
            by_partner=by_partner,
            summary=summary,
        )

        get_finance_stats_response_200_data.additional_properties = d
        return get_finance_stats_response_200_data

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
