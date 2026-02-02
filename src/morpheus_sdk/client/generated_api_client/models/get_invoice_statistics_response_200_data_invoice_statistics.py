from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInvoiceStatisticsResponse200DataInvoiceStatistics")


@_attrs_define
class GetInvoiceStatisticsResponse200DataInvoiceStatistics:
    """
    Attributes:
        total (Union[Unset, int]):
        errored (Union[Unset, int]):
        rejection_rate (Union[Unset, float]):
        total_exposure_dollar (Union[Unset, float]):
        first_pass_acceptance_rate (Union[Unset, float]):
    """

    total: Union[Unset, int] = UNSET
    errored: Union[Unset, int] = UNSET
    rejection_rate: Union[Unset, float] = UNSET
    total_exposure_dollar: Union[Unset, float] = UNSET
    first_pass_acceptance_rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        errored = self.errored

        rejection_rate = self.rejection_rate

        total_exposure_dollar = self.total_exposure_dollar

        first_pass_acceptance_rate = self.first_pass_acceptance_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if errored is not UNSET:
            field_dict["errored"] = errored
        if rejection_rate is not UNSET:
            field_dict["rejectionRate"] = rejection_rate
        if total_exposure_dollar is not UNSET:
            field_dict["totalExposureDollar"] = total_exposure_dollar
        if first_pass_acceptance_rate is not UNSET:
            field_dict["firstPassAcceptanceRate"] = first_pass_acceptance_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        errored = d.pop("errored", UNSET)

        rejection_rate = d.pop("rejectionRate", UNSET)

        total_exposure_dollar = d.pop("totalExposureDollar", UNSET)

        first_pass_acceptance_rate = d.pop("firstPassAcceptanceRate", UNSET)

        get_invoice_statistics_response_200_data_invoice_statistics = cls(
            total=total,
            errored=errored,
            rejection_rate=rejection_rate,
            total_exposure_dollar=total_exposure_dollar,
            first_pass_acceptance_rate=first_pass_acceptance_rate,
        )

        get_invoice_statistics_response_200_data_invoice_statistics.additional_properties = d
        return get_invoice_statistics_response_200_data_invoice_statistics

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
