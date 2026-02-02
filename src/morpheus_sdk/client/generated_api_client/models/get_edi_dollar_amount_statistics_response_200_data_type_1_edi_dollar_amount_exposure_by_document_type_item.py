from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEdiDollarAmountStatisticsResponse200DataType1EdiDollarAmountExposureByDocumentTypeItem")


@_attrs_define
class GetEdiDollarAmountStatisticsResponse200DataType1EdiDollarAmountExposureByDocumentTypeItem:
    """
    Attributes:
        doc_type (Union[Unset, str]): EDI document type Example: 810.
        total_dollar_amount (Union[Unset, float]): Total dollar value of EDI transactions for this document type
            Example: 250000.75.
        transaction_count (Union[Unset, int]): Number of transactions for this document type Example: 120.
    """

    doc_type: Union[Unset, str] = UNSET
    total_dollar_amount: Union[Unset, float] = UNSET
    transaction_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        doc_type = self.doc_type

        total_dollar_amount = self.total_dollar_amount

        transaction_count = self.transaction_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_type is not UNSET:
            field_dict["docType"] = doc_type
        if total_dollar_amount is not UNSET:
            field_dict["totalDollarAmount"] = total_dollar_amount
        if transaction_count is not UNSET:
            field_dict["transactionCount"] = transaction_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        doc_type = d.pop("docType", UNSET)

        total_dollar_amount = d.pop("totalDollarAmount", UNSET)

        transaction_count = d.pop("transactionCount", UNSET)

        get_edi_dollar_amount_statistics_response_200_data_type_1_edi_dollar_amount_exposure_by_document_type_item = (
            cls(
                doc_type=doc_type,
                total_dollar_amount=total_dollar_amount,
                transaction_count=transaction_count,
            )
        )

        get_edi_dollar_amount_statistics_response_200_data_type_1_edi_dollar_amount_exposure_by_document_type_item.additional_properties = d
        return (
            get_edi_dollar_amount_statistics_response_200_data_type_1_edi_dollar_amount_exposure_by_document_type_item
        )

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
