from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_erp_company_body_status import UpdateERPCompanyBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.update_erp_company_body_custom_fields import UpdateERPCompanyBodyCustomFields
    from ..models.update_erp_company_body_primary_contact import UpdateERPCompanyBodyPrimaryContact


T = TypeVar("T", bound="UpdateERPCompanyBody")


@_attrs_define
class UpdateERPCompanyBody:
    """
    Attributes:
        name (Union[Unset, str]): Updated company name Example: Acme Corporation Enhanced.
        status (Union[Unset, UpdateERPCompanyBodyStatus]): Updated company status Example: INACTIVE.
        credit_limit (Union[Unset, float]): Updated credit limit Example: 150000.
        credit_hold (Union[Unset, bool]): Updated credit hold status Example: True.
        primary_contact (Union[Unset, UpdateERPCompanyBodyPrimaryContact]): Updated primary contact information
        billing_address (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        custom_fields (Union[Unset, UpdateERPCompanyBodyCustomFields]): Updated custom fields
    """

    name: Union[Unset, str] = UNSET
    status: Union[Unset, UpdateERPCompanyBodyStatus] = UNSET
    credit_limit: Union[Unset, float] = UNSET
    credit_hold: Union[Unset, bool] = UNSET
    primary_contact: Union[Unset, "UpdateERPCompanyBodyPrimaryContact"] = UNSET
    billing_address: Union[Unset, "Address"] = UNSET
    custom_fields: Union[Unset, "UpdateERPCompanyBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        credit_limit = self.credit_limit

        credit_hold = self.credit_hold

        primary_contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_contact, Unset):
            primary_contact = self.primary_contact.to_dict()

        billing_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if credit_limit is not UNSET:
            field_dict["creditLimit"] = credit_limit
        if credit_hold is not UNSET:
            field_dict["creditHold"] = credit_hold
        if primary_contact is not UNSET:
            field_dict["primaryContact"] = primary_contact
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.update_erp_company_body_custom_fields import UpdateERPCompanyBodyCustomFields
        from ..models.update_erp_company_body_primary_contact import UpdateERPCompanyBodyPrimaryContact

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateERPCompanyBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateERPCompanyBodyStatus(_status)

        credit_limit = d.pop("creditLimit", UNSET)

        credit_hold = d.pop("creditHold", UNSET)

        _primary_contact = d.pop("primaryContact", UNSET)
        primary_contact: Union[Unset, UpdateERPCompanyBodyPrimaryContact]
        if isinstance(_primary_contact, Unset):
            primary_contact = UNSET
        else:
            primary_contact = UpdateERPCompanyBodyPrimaryContact.from_dict(_primary_contact)

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, Address]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = Address.from_dict(_billing_address)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, UpdateERPCompanyBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = UpdateERPCompanyBodyCustomFields.from_dict(_custom_fields)

        update_erp_company_body = cls(
            name=name,
            status=status,
            credit_limit=credit_limit,
            credit_hold=credit_hold,
            primary_contact=primary_contact,
            billing_address=billing_address,
            custom_fields=custom_fields,
        )

        update_erp_company_body.additional_properties = d
        return update_erp_company_body

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
