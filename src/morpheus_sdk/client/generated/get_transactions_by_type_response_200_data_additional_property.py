from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTransactionsByTypeResponse200DataAdditionalProperty")


@_attrs_define
class GetTransactionsByTypeResponse200DataAdditionalProperty:
    """
    Attributes:
        count (Union[Unset, float]):  Example: 45.
        total_amount (Union[Unset, float]):  Example: 75000.
        avg_amount (Union[Unset, float]): Average transaction amount for this type Example: 1666.67.
    """

    count: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    avg_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        total_amount = self.total_amount

        avg_amount = self.avg_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        count = d.pop("count", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        avg_amount = d.pop("avgAmount", UNSET)

        get_transactions_by_type_response_200_data_additional_property = cls(
            count=count,
            total_amount=total_amount,
            avg_amount=avg_amount,
        )

        get_transactions_by_type_response_200_data_additional_property.additional_properties = d
        return get_transactions_by_type_response_200_data_additional_property

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
