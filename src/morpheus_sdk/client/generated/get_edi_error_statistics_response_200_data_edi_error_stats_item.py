from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEdiErrorStatisticsResponse200DataEdiErrorStatsItem")


@_attrs_define
class GetEdiErrorStatisticsResponse200DataEdiErrorStatsItem:
    """
    Attributes:
        doc_type (Union[Unset, str]):
        partner_id (Union[Unset, str]):
        count (Union[Unset, int]):
    """

    doc_type: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        doc_type = self.doc_type

        partner_id = self.partner_id

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_type is not UNSET:
            field_dict["docType"] = doc_type
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        doc_type = d.pop("docType", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        count = d.pop("count", UNSET)

        get_edi_error_statistics_response_200_data_edi_error_stats_item = cls(
            doc_type=doc_type,
            partner_id=partner_id,
            count=count,
        )

        get_edi_error_statistics_response_200_data_edi_error_stats_item.additional_properties = d
        return get_edi_error_statistics_response_200_data_edi_error_stats_item

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
