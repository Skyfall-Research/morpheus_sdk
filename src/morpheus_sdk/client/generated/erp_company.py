import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.erp_company_company_type import ERPCompanyCompanyType
from ..models.erp_company_status import ERPCompanyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.erp_company_custom_fields import ERPCompanyCustomFields
    from ..models.erp_company_primary_contact import ERPCompanyPrimaryContact
    from ..models.erp_company_tax_registration_numbers_item import ERPCompanyTaxRegistrationNumbersItem
    from ..models.erp_company_world_ref import ERPCompanyWorldRef


T = TypeVar("T", bound="ERPCompany")


@_attrs_define
class ERPCompany:
    """Complete ERP company entity with comprehensive business information and operational configuration

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        world_ref (ERPCompanyWorldRef): Reference to the world this company belongs to
        company_id (str): Unique company identifier within the world Example: COMP_507f1f77bcf86cd799439012.
        name (str): Company name Example: Acme Corporation.
        status (ERPCompanyStatus): Company operational status Default: ERPCompanyStatus.ACTIVE. Example: ACTIVE.
        company_type (ERPCompanyCompanyType): Company relationship type Default: ERPCompanyCompanyType.CUSTOMER.
            Example: CUSTOMER.
        is_mpc_company (Union[Unset, bool]): Main Player Company designation (exclusive within world) Default: False.
        external_reference (Union[Unset, str]): External system reference identifier Example: EXT_REF_12345.
        legal_name (Union[Unset, str]): Legal business name Example: Acme Corporation LLC.
        duns (Union[Unset, str]): DUNS (Data Universal Numbering System) number Example: 123456789.
        tax_id (Union[Unset, str]): Tax identification number Example: TAX123456789.
        tax_registration_numbers (Union[Unset, list['ERPCompanyTaxRegistrationNumbersItem']]): Country-specific tax
            registration numbers
        currency (Union[Unset, str]): Primary operating currency Default: 'USD'. Example: USD.
        payment_terms (Union[Unset, str]): Payment terms and conditions Example: NET30.
        credit_limit (Union[Unset, float]): Credit limit amount Example: 100000.
        credit_hold (Union[Unset, bool]): Credit hold status Default: False.
        billing_address (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        shipping_address (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        remit_to (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        primary_contact (Union[Unset, ERPCompanyPrimaryContact]): Primary contact information
        sales_org (Union[Unset, str]): Sales organization code Example: US_EAST.
        price_list (Union[Unset, str]): Price list identifier Example: STANDARD_RETAIL.
        gl_account (Union[Unset, str]): General ledger account Example: 1200-AR-TRADE.
        customer_class (Union[Unset, str]): Customer classification Example: PREMIUM.
        custom_fields (Union[Unset, ERPCompanyCustomFields]): Additional custom fields for company-specific data
            Example: {'erpSource': 'SAP', 'regionCode': 'US', 'salesRep': 'JOHN_DOE'}.
        created_at (Union[Unset, datetime.datetime]): Company record creation timestamp Example:
            2024-01-15T10:25:30.123Z.
        updated_at (Union[Unset, datetime.datetime]): Company record last update timestamp Example:
            2024-01-15T14:30:45.678Z.
    """

    field_id: str
    world_ref: "ERPCompanyWorldRef"
    company_id: str
    name: str
    status: ERPCompanyStatus = ERPCompanyStatus.ACTIVE
    company_type: ERPCompanyCompanyType = ERPCompanyCompanyType.CUSTOMER
    is_mpc_company: Union[Unset, bool] = False
    external_reference: Union[Unset, str] = UNSET
    legal_name: Union[Unset, str] = UNSET
    duns: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    tax_registration_numbers: Union[Unset, list["ERPCompanyTaxRegistrationNumbersItem"]] = UNSET
    currency: Union[Unset, str] = "USD"
    payment_terms: Union[Unset, str] = UNSET
    credit_limit: Union[Unset, float] = UNSET
    credit_hold: Union[Unset, bool] = False
    billing_address: Union[Unset, "Address"] = UNSET
    shipping_address: Union[Unset, "Address"] = UNSET
    remit_to: Union[Unset, "Address"] = UNSET
    primary_contact: Union[Unset, "ERPCompanyPrimaryContact"] = UNSET
    sales_org: Union[Unset, str] = UNSET
    price_list: Union[Unset, str] = UNSET
    gl_account: Union[Unset, str] = UNSET
    customer_class: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "ERPCompanyCustomFields"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_ref = self.world_ref.to_dict()

        company_id = self.company_id

        name = self.name

        status = self.status.value

        company_type = self.company_type.value

        is_mpc_company = self.is_mpc_company

        external_reference = self.external_reference

        legal_name = self.legal_name

        duns = self.duns

        tax_id = self.tax_id

        tax_registration_numbers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tax_registration_numbers, Unset):
            tax_registration_numbers = []
            for tax_registration_numbers_item_data in self.tax_registration_numbers:
                tax_registration_numbers_item = tax_registration_numbers_item_data.to_dict()
                tax_registration_numbers.append(tax_registration_numbers_item)

        currency = self.currency

        payment_terms = self.payment_terms

        credit_limit = self.credit_limit

        credit_hold = self.credit_hold

        billing_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        shipping_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        remit_to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.remit_to, Unset):
            remit_to = self.remit_to.to_dict()

        primary_contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_contact, Unset):
            primary_contact = self.primary_contact.to_dict()

        sales_org = self.sales_org

        price_list = self.price_list

        gl_account = self.gl_account

        customer_class = self.customer_class

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "worldRef": world_ref,
                "companyId": company_id,
                "name": name,
                "status": status,
                "companyType": company_type,
            }
        )
        if is_mpc_company is not UNSET:
            field_dict["isMpcCompany"] = is_mpc_company
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if legal_name is not UNSET:
            field_dict["legalName"] = legal_name
        if duns is not UNSET:
            field_dict["duns"] = duns
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if tax_registration_numbers is not UNSET:
            field_dict["taxRegistrationNumbers"] = tax_registration_numbers
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_terms is not UNSET:
            field_dict["paymentTerms"] = payment_terms
        if credit_limit is not UNSET:
            field_dict["creditLimit"] = credit_limit
        if credit_hold is not UNSET:
            field_dict["creditHold"] = credit_hold
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if remit_to is not UNSET:
            field_dict["remitTo"] = remit_to
        if primary_contact is not UNSET:
            field_dict["primaryContact"] = primary_contact
        if sales_org is not UNSET:
            field_dict["salesOrg"] = sales_org
        if price_list is not UNSET:
            field_dict["priceList"] = price_list
        if gl_account is not UNSET:
            field_dict["glAccount"] = gl_account
        if customer_class is not UNSET:
            field_dict["customerClass"] = customer_class
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.erp_company_custom_fields import ERPCompanyCustomFields
        from ..models.erp_company_primary_contact import ERPCompanyPrimaryContact
        from ..models.erp_company_tax_registration_numbers_item import ERPCompanyTaxRegistrationNumbersItem
        from ..models.erp_company_world_ref import ERPCompanyWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_ref = ERPCompanyWorldRef.from_dict(d.pop("worldRef"))

        company_id = d.pop("companyId")

        name = d.pop("name")

        status = ERPCompanyStatus(d.pop("status"))

        company_type = ERPCompanyCompanyType(d.pop("companyType"))

        is_mpc_company = d.pop("isMpcCompany", UNSET)

        external_reference = d.pop("externalReference", UNSET)

        legal_name = d.pop("legalName", UNSET)

        duns = d.pop("duns", UNSET)

        tax_id = d.pop("taxId", UNSET)

        tax_registration_numbers = []
        _tax_registration_numbers = d.pop("taxRegistrationNumbers", UNSET)
        for tax_registration_numbers_item_data in _tax_registration_numbers or []:
            tax_registration_numbers_item = ERPCompanyTaxRegistrationNumbersItem.from_dict(
                tax_registration_numbers_item_data
            )

            tax_registration_numbers.append(tax_registration_numbers_item)

        currency = d.pop("currency", UNSET)

        payment_terms = d.pop("paymentTerms", UNSET)

        credit_limit = d.pop("creditLimit", UNSET)

        credit_hold = d.pop("creditHold", UNSET)

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, Address]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = Address.from_dict(_billing_address)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, Address]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = Address.from_dict(_shipping_address)

        _remit_to = d.pop("remitTo", UNSET)
        remit_to: Union[Unset, Address]
        if isinstance(_remit_to, Unset):
            remit_to = UNSET
        else:
            remit_to = Address.from_dict(_remit_to)

        _primary_contact = d.pop("primaryContact", UNSET)
        primary_contact: Union[Unset, ERPCompanyPrimaryContact]
        if isinstance(_primary_contact, Unset):
            primary_contact = UNSET
        else:
            primary_contact = ERPCompanyPrimaryContact.from_dict(_primary_contact)

        sales_org = d.pop("salesOrg", UNSET)

        price_list = d.pop("priceList", UNSET)

        gl_account = d.pop("glAccount", UNSET)

        customer_class = d.pop("customerClass", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, ERPCompanyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ERPCompanyCustomFields.from_dict(_custom_fields)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        erp_company = cls(
            field_id=field_id,
            world_ref=world_ref,
            company_id=company_id,
            name=name,
            status=status,
            company_type=company_type,
            is_mpc_company=is_mpc_company,
            external_reference=external_reference,
            legal_name=legal_name,
            duns=duns,
            tax_id=tax_id,
            tax_registration_numbers=tax_registration_numbers,
            currency=currency,
            payment_terms=payment_terms,
            credit_limit=credit_limit,
            credit_hold=credit_hold,
            billing_address=billing_address,
            shipping_address=shipping_address,
            remit_to=remit_to,
            primary_contact=primary_contact,
            sales_org=sales_org,
            price_list=price_list,
            gl_account=gl_account,
            customer_class=customer_class,
            custom_fields=custom_fields,
            created_at=created_at,
            updated_at=updated_at,
        )

        erp_company.additional_properties = d
        return erp_company

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
