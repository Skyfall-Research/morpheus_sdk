from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_edi_dollar_amount_statistics_response_200_data_type_0_edi_dollar_amount_exposure_by_partners_item import (
        GetEdiDollarAmountStatisticsResponse200DataType0EdiDollarAmountExposureByPartnersItem,
    )


T = TypeVar("T", bound="GetEdiDollarAmountStatisticsResponse200DataType0")


@_attrs_define
class GetEdiDollarAmountStatisticsResponse200DataType0:
    """
    Attributes:
        edi_dollar_amount_exposure_by_partners (Union[Unset,
            list['GetEdiDollarAmountStatisticsResponse200DataType0EdiDollarAmountExposureByPartnersItem']]): Dollar exposure
            aggregated by trading partner (when aggregationType=by-partners)
    """

    edi_dollar_amount_exposure_by_partners: Union[
        Unset, list["GetEdiDollarAmountStatisticsResponse200DataType0EdiDollarAmountExposureByPartnersItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edi_dollar_amount_exposure_by_partners: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edi_dollar_amount_exposure_by_partners, Unset):
            edi_dollar_amount_exposure_by_partners = []
            for edi_dollar_amount_exposure_by_partners_item_data in self.edi_dollar_amount_exposure_by_partners:
                edi_dollar_amount_exposure_by_partners_item = edi_dollar_amount_exposure_by_partners_item_data.to_dict()
                edi_dollar_amount_exposure_by_partners.append(edi_dollar_amount_exposure_by_partners_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edi_dollar_amount_exposure_by_partners is not UNSET:
            field_dict["ediDollarAmountExposureByPartners"] = edi_dollar_amount_exposure_by_partners

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_edi_dollar_amount_statistics_response_200_data_type_0_edi_dollar_amount_exposure_by_partners_item import (
            GetEdiDollarAmountStatisticsResponse200DataType0EdiDollarAmountExposureByPartnersItem,
        )

        d = dict(src_dict)
        edi_dollar_amount_exposure_by_partners = []
        _edi_dollar_amount_exposure_by_partners = d.pop("ediDollarAmountExposureByPartners", UNSET)
        for edi_dollar_amount_exposure_by_partners_item_data in _edi_dollar_amount_exposure_by_partners or []:
            edi_dollar_amount_exposure_by_partners_item = (
                GetEdiDollarAmountStatisticsResponse200DataType0EdiDollarAmountExposureByPartnersItem.from_dict(
                    edi_dollar_amount_exposure_by_partners_item_data
                )
            )

            edi_dollar_amount_exposure_by_partners.append(edi_dollar_amount_exposure_by_partners_item)

        get_edi_dollar_amount_statistics_response_200_data_type_0 = cls(
            edi_dollar_amount_exposure_by_partners=edi_dollar_amount_exposure_by_partners,
        )

        get_edi_dollar_amount_statistics_response_200_data_type_0.additional_properties = d
        return get_edi_dollar_amount_statistics_response_200_data_type_0

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
