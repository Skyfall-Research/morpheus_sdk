from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEdiDollarAmountStatisticsResponse200DataType0EdiDollarAmountExposureByPartnersItem")


@_attrs_define
class GetEdiDollarAmountStatisticsResponse200DataType0EdiDollarAmountExposureByPartnersItem:
    """
    Attributes:
        partner_id (Union[Unset, str]): Trading partner identifier Example: PARTNER_WALMART_001.
        total_dollar_amount (Union[Unset, float]): Total dollar value of EDI transactions for this partner Example:
            125000.5.
        transaction_count (Union[Unset, int]): Number of transactions for this partner Example: 45.
    """

    partner_id: Union[Unset, str] = UNSET
    total_dollar_amount: Union[Unset, float] = UNSET
    transaction_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partner_id = self.partner_id

        total_dollar_amount = self.total_dollar_amount

        transaction_count = self.transaction_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if total_dollar_amount is not UNSET:
            field_dict["totalDollarAmount"] = total_dollar_amount
        if transaction_count is not UNSET:
            field_dict["transactionCount"] = transaction_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        partner_id = d.pop("partnerId", UNSET)

        total_dollar_amount = d.pop("totalDollarAmount", UNSET)

        transaction_count = d.pop("transactionCount", UNSET)

        get_edi_dollar_amount_statistics_response_200_data_type_0_edi_dollar_amount_exposure_by_partners_item = cls(
            partner_id=partner_id,
            total_dollar_amount=total_dollar_amount,
            transaction_count=transaction_count,
        )

        get_edi_dollar_amount_statistics_response_200_data_type_0_edi_dollar_amount_exposure_by_partners_item.additional_properties = d
        return get_edi_dollar_amount_statistics_response_200_data_type_0_edi_dollar_amount_exposure_by_partners_item

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
