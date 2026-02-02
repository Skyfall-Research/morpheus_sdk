from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTransactionsByPartnerResponse200DataItem")


@_attrs_define
class GetTransactionsByPartnerResponse200DataItem:
    """
    Attributes:
        partner_id (Union[Unset, str]): Business partner identifier Example: PARTNER_001.
        count (Union[Unset, float]): Number of transactions with this partner Example: 12.
        total_amount (Union[Unset, float]): Total transaction amount with this partner Example: 18500.
        avg_amount (Union[Unset, float]): Average transaction amount with this partner Example: 1541.67.
    """

    partner_id: Union[Unset, str] = UNSET
    count: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    avg_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partner_id = self.partner_id

        count = self.count

        total_amount = self.total_amount

        avg_amount = self.avg_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if count is not UNSET:
            field_dict["count"] = count
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if avg_amount is not UNSET:
            field_dict["avgAmount"] = avg_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        partner_id = d.pop("partnerId", UNSET)

        count = d.pop("count", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        avg_amount = d.pop("avgAmount", UNSET)

        get_transactions_by_partner_response_200_data_item = cls(
            partner_id=partner_id,
            count=count,
            total_amount=total_amount,
            avg_amount=avg_amount,
        )

        get_transactions_by_partner_response_200_data_item.additional_properties = d
        return get_transactions_by_partner_response_200_data_item

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
