from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_upsert_erp_companies_body_companies_item import BulkUpsertERPCompaniesBodyCompaniesItem


T = TypeVar("T", bound="BulkUpsertERPCompaniesBody")


@_attrs_define
class BulkUpsertERPCompaniesBody:
    """
    Attributes:
        companies (list['BulkUpsertERPCompaniesBodyCompaniesItem']): Array of company objects to upsert Example:
            [{'companyId': 'COMP_ACME001', 'name': 'Acme Corporation', 'status': 'ACTIVE', 'companyType': 'CUSTOMER'},
            {'companyId': 'COMP_BETA002', 'name': 'Beta Industries', 'status': 'ACTIVE', 'companyType': 'SUPPLIER'}].
    """

    companies: list["BulkUpsertERPCompaniesBodyCompaniesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companies": companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_upsert_erp_companies_body_companies_item import BulkUpsertERPCompaniesBodyCompaniesItem

        d = dict(src_dict)
        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = BulkUpsertERPCompaniesBodyCompaniesItem.from_dict(companies_item_data)

            companies.append(companies_item)

        bulk_upsert_erp_companies_body = cls(
            companies=companies,
        )

        bulk_upsert_erp_companies_body.additional_properties = d
        return bulk_upsert_erp_companies_body

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
