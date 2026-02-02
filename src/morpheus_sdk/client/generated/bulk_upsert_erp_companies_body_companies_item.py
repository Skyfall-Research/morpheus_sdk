from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_upsert_erp_companies_body_companies_item_status import BulkUpsertERPCompaniesBodyCompaniesItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkUpsertERPCompaniesBodyCompaniesItem")


@_attrs_define
class BulkUpsertERPCompaniesBodyCompaniesItem:
    """Company data (same as create company schema)

    Attributes:
        company_id (Union[Unset, str]): Company identifier for upsert matching Example: COMP_ACME001.
        name (Union[Unset, str]): Company name Example: Acme Corporation.
        status (Union[Unset, BulkUpsertERPCompaniesBodyCompaniesItemStatus]):  Example: ACTIVE.
    """

    company_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, BulkUpsertERPCompaniesBodyCompaniesItemStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BulkUpsertERPCompaniesBodyCompaniesItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BulkUpsertERPCompaniesBodyCompaniesItemStatus(_status)

        bulk_upsert_erp_companies_body_companies_item = cls(
            company_id=company_id,
            name=name,
            status=status,
        )

        bulk_upsert_erp_companies_body_companies_item.additional_properties = d
        return bulk_upsert_erp_companies_body_companies_item

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
