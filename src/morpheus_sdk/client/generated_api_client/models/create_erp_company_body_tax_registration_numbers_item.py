from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateERPCompanyBodyTaxRegistrationNumbersItem")


@_attrs_define
class CreateERPCompanyBodyTaxRegistrationNumbersItem:
    """
    Attributes:
        country (Union[Unset, str]):  Example: USA.
        number (Union[Unset, str]):  Example: REG123456789.
    """

    country: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country = d.pop("country", UNSET)

        number = d.pop("number", UNSET)

        create_erp_company_body_tax_registration_numbers_item = cls(
            country=country,
            number=number,
        )

        create_erp_company_body_tax_registration_numbers_item.additional_properties = d
        return create_erp_company_body_tax_registration_numbers_item

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
