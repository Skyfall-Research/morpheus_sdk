from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncrementCompanyLedgerBalancesResponse400")


@_attrs_define
class IncrementCompanyLedgerBalancesResponse400:
    """
    Attributes:
        success (Union[Unset, bool]):
        status (Union[Unset, int]):  Example: 400.
        error (Union[Unset, str]):  Example: At least one delta (cashDelta, receivablesDelta, payablesDelta) is
            required.
    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        error = d.pop("error", UNSET)

        increment_company_ledger_balances_response_400 = cls(
            success=success,
            status=status,
            error=error,
        )

        increment_company_ledger_balances_response_400.additional_properties = d
        return increment_company_ledger_balances_response_400

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
