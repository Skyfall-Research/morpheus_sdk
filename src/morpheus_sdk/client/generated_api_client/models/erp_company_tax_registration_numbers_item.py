from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ERPCompanyTaxRegistrationNumbersItem")


@_attrs_define
class ERPCompanyTaxRegistrationNumbersItem:
    """
    Attributes:
        country (str): Country code Example: USA.
        number (str): Tax registration number Example: REG123456789.
    """

    country: str
    number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country": country,
                "number": number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country = d.pop("country")

        number = d.pop("number")

        erp_company_tax_registration_numbers_item = cls(
            country=country,
            number=number,
        )

        erp_company_tax_registration_numbers_item.additional_properties = d
        return erp_company_tax_registration_numbers_item

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
