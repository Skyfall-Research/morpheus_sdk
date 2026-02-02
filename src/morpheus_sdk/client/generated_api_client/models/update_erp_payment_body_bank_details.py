from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateERPPaymentBodyBankDetails")


@_attrs_define
class UpdateERPPaymentBodyBankDetails:
    """Updated banking information

    Attributes:
        bank_name (Union[Unset, str]):  Example: Chase Bank.
        account_number (Union[Unset, str]):  Example: ****5678.
        routing_number (Union[Unset, str]):  Example: 021000021.
        swift (Union[Unset, str]):  Example: CHASUS33.
    """

    bank_name: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    swift: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bank_name = self.bank_name

        account_number = self.account_number

        routing_number = self.routing_number

        swift = self.swift

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if swift is not UNSET:
            field_dict["swift"] = swift

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bank_name = d.pop("bankName", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        swift = d.pop("swift", UNSET)

        update_erp_payment_body_bank_details = cls(
            bank_name=bank_name,
            account_number=account_number,
            routing_number=routing_number,
            swift=swift,
        )

        update_erp_payment_body_bank_details.additional_properties = d
        return update_erp_payment_body_bank_details

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
