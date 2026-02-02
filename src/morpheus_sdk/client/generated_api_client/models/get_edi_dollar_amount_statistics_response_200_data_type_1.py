from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_edi_dollar_amount_statistics_response_200_data_type_1_edi_dollar_amount_exposure_by_document_type_item import (
        GetEdiDollarAmountStatisticsResponse200DataType1EdiDollarAmountExposureByDocumentTypeItem,
    )


T = TypeVar("T", bound="GetEdiDollarAmountStatisticsResponse200DataType1")


@_attrs_define
class GetEdiDollarAmountStatisticsResponse200DataType1:
    """
    Attributes:
        edi_dollar_amount_exposure_by_document_type (Union[Unset,
            list['GetEdiDollarAmountStatisticsResponse200DataType1EdiDollarAmountExposureByDocumentTypeItem']]): Dollar
            exposure aggregated by document type (when aggregationType=by-document-type)
    """

    edi_dollar_amount_exposure_by_document_type: Union[
        Unset, list["GetEdiDollarAmountStatisticsResponse200DataType1EdiDollarAmountExposureByDocumentTypeItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edi_dollar_amount_exposure_by_document_type: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edi_dollar_amount_exposure_by_document_type, Unset):
            edi_dollar_amount_exposure_by_document_type = []
            for (
                edi_dollar_amount_exposure_by_document_type_item_data
            ) in self.edi_dollar_amount_exposure_by_document_type:
                edi_dollar_amount_exposure_by_document_type_item = (
                    edi_dollar_amount_exposure_by_document_type_item_data.to_dict()
                )
                edi_dollar_amount_exposure_by_document_type.append(edi_dollar_amount_exposure_by_document_type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edi_dollar_amount_exposure_by_document_type is not UNSET:
            field_dict["ediDollarAmountExposureByDocumentType"] = edi_dollar_amount_exposure_by_document_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_edi_dollar_amount_statistics_response_200_data_type_1_edi_dollar_amount_exposure_by_document_type_item import (
            GetEdiDollarAmountStatisticsResponse200DataType1EdiDollarAmountExposureByDocumentTypeItem,
        )

        d = dict(src_dict)
        edi_dollar_amount_exposure_by_document_type = []
        _edi_dollar_amount_exposure_by_document_type = d.pop("ediDollarAmountExposureByDocumentType", UNSET)
        for edi_dollar_amount_exposure_by_document_type_item_data in _edi_dollar_amount_exposure_by_document_type or []:
            edi_dollar_amount_exposure_by_document_type_item = (
                GetEdiDollarAmountStatisticsResponse200DataType1EdiDollarAmountExposureByDocumentTypeItem.from_dict(
                    edi_dollar_amount_exposure_by_document_type_item_data
                )
            )

            edi_dollar_amount_exposure_by_document_type.append(edi_dollar_amount_exposure_by_document_type_item)

        get_edi_dollar_amount_statistics_response_200_data_type_1 = cls(
            edi_dollar_amount_exposure_by_document_type=edi_dollar_amount_exposure_by_document_type,
        )

        get_edi_dollar_amount_statistics_response_200_data_type_1.additional_properties = d
        return get_edi_dollar_amount_statistics_response_200_data_type_1

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
