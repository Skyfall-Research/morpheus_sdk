import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ERPInvoiceAccounting")


@_attrs_define
class ERPInvoiceAccounting:
    """Accounting configuration

    Attributes:
        ar_account (Union[Unset, str]):  Example: 1200-AR-TRADE.
        period (Union[Unset, str]):  Example: 2024-01.
        posting_date (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
    """

    ar_account: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    posting_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ar_account = self.ar_account

        period = self.period

        posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.posting_date, Unset):
            posting_date = self.posting_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ar_account is not UNSET:
            field_dict["arAccount"] = ar_account
        if period is not UNSET:
            field_dict["period"] = period
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ar_account = d.pop("arAccount", UNSET)

        period = d.pop("period", UNSET)

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.datetime]
        if isinstance(_posting_date, Unset):
            posting_date = UNSET
        else:
            posting_date = isoparse(_posting_date)

        erp_invoice_accounting = cls(
            ar_account=ar_account,
            period=period,
            posting_date=posting_date,
        )

        erp_invoice_accounting.additional_properties = d
        return erp_invoice_accounting

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
