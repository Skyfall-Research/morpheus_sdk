from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_erp_company_body_company_type import CreateERPCompanyBodyCompanyType
from ..models.create_erp_company_body_status import CreateERPCompanyBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.create_erp_company_body_custom_fields import CreateERPCompanyBodyCustomFields
    from ..models.create_erp_company_body_primary_contact import CreateERPCompanyBodyPrimaryContact
    from ..models.create_erp_company_body_tax_registration_numbers_item import (
        CreateERPCompanyBodyTaxRegistrationNumbersItem,
    )


T = TypeVar("T", bound="CreateERPCompanyBody")


@_attrs_define
class CreateERPCompanyBody:
    """
    Attributes:
        name (str): Company name (required) Example: Acme Corporation.
        is_mpc_company (Union[Unset, bool]): Main Player Company designation (exclusive within world) Default: False.
        company_id (Union[Unset, str]): Optional custom company identifier (auto-generated if not provided) Example:
            COMP_ACME001.
        external_reference (Union[Unset, str]): External system reference identifier Example: EXT_REF_12345.
        legal_name (Union[Unset, str]): Legal business name Example: Acme Corporation LLC.
        duns (Union[Unset, str]): DUNS (Data Universal Numbering System) number Example: 123456789.
        tax_id (Union[Unset, str]): Tax identification number Example: TAX123456789.
        tax_registration_numbers (Union[Unset, list['CreateERPCompanyBodyTaxRegistrationNumbersItem']]): Country-
            specific tax registration numbers
        currency (Union[Unset, str]): Primary operating currency Default: 'USD'. Example: USD.
        payment_terms (Union[Unset, str]): Payment terms and conditions Example: NET30.
        credit_limit (Union[Unset, float]): Credit limit amount Example: 100000.
        credit_hold (Union[Unset, bool]): Credit hold status Default: False.
        billing_address (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        shipping_address (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        remit_to (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        primary_contact (Union[Unset, CreateERPCompanyBodyPrimaryContact]): Primary contact information
        sales_org (Union[Unset, str]): Sales organization code Example: US_EAST.
        price_list (Union[Unset, str]): Price list identifier Example: STANDARD_RETAIL.
        gl_account (Union[Unset, str]): General ledger account Example: 1200-AR-TRADE.
        customer_class (Union[Unset, str]): Customer classification Example: PREMIUM.
        status (Union[Unset, CreateERPCompanyBodyStatus]): Company operational status Default:
            CreateERPCompanyBodyStatus.ACTIVE. Example: ACTIVE.
        company_type (Union[Unset, CreateERPCompanyBodyCompanyType]): Company relationship type Default:
            CreateERPCompanyBodyCompanyType.CUSTOMER. Example: CUSTOMER.
        custom_fields (Union[Unset, CreateERPCompanyBodyCustomFields]): Additional custom fields Example: {'erpSource':
            'SAP', 'regionCode': 'US'}.
    """

    name: str
    is_mpc_company: Union[Unset, bool] = False
    company_id: Union[Unset, str] = UNSET
    external_reference: Union[Unset, str] = UNSET
    legal_name: Union[Unset, str] = UNSET
    duns: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    tax_registration_numbers: Union[Unset, list["CreateERPCompanyBodyTaxRegistrationNumbersItem"]] = UNSET
    currency: Union[Unset, str] = "USD"
    payment_terms: Union[Unset, str] = UNSET
    credit_limit: Union[Unset, float] = UNSET
    credit_hold: Union[Unset, bool] = False
    billing_address: Union[Unset, "Address"] = UNSET
    shipping_address: Union[Unset, "Address"] = UNSET
    remit_to: Union[Unset, "Address"] = UNSET
    primary_contact: Union[Unset, "CreateERPCompanyBodyPrimaryContact"] = UNSET
    sales_org: Union[Unset, str] = UNSET
    price_list: Union[Unset, str] = UNSET
    gl_account: Union[Unset, str] = UNSET
    customer_class: Union[Unset, str] = UNSET
    status: Union[Unset, CreateERPCompanyBodyStatus] = CreateERPCompanyBodyStatus.ACTIVE
    company_type: Union[Unset, CreateERPCompanyBodyCompanyType] = CreateERPCompanyBodyCompanyType.CUSTOMER
    custom_fields: Union[Unset, "CreateERPCompanyBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_mpc_company = self.is_mpc_company

        company_id = self.company_id

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

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        company_type: Union[Unset, str] = UNSET
        if not isinstance(self.company_type, Unset):
            company_type = self.company_type.value

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if is_mpc_company is not UNSET:
            field_dict["isMpcCompany"] = is_mpc_company
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
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
        if status is not UNSET:
            field_dict["status"] = status
        if company_type is not UNSET:
            field_dict["companyType"] = company_type
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.create_erp_company_body_custom_fields import CreateERPCompanyBodyCustomFields
        from ..models.create_erp_company_body_primary_contact import CreateERPCompanyBodyPrimaryContact
        from ..models.create_erp_company_body_tax_registration_numbers_item import (
            CreateERPCompanyBodyTaxRegistrationNumbersItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        is_mpc_company = d.pop("isMpcCompany", UNSET)

        company_id = d.pop("companyId", UNSET)

        external_reference = d.pop("externalReference", UNSET)

        legal_name = d.pop("legalName", UNSET)

        duns = d.pop("duns", UNSET)

        tax_id = d.pop("taxId", UNSET)

        tax_registration_numbers = []
        _tax_registration_numbers = d.pop("taxRegistrationNumbers", UNSET)
        for tax_registration_numbers_item_data in _tax_registration_numbers or []:
            tax_registration_numbers_item = CreateERPCompanyBodyTaxRegistrationNumbersItem.from_dict(
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
        primary_contact: Union[Unset, CreateERPCompanyBodyPrimaryContact]
        if isinstance(_primary_contact, Unset):
            primary_contact = UNSET
        else:
            primary_contact = CreateERPCompanyBodyPrimaryContact.from_dict(_primary_contact)

        sales_org = d.pop("salesOrg", UNSET)

        price_list = d.pop("priceList", UNSET)

        gl_account = d.pop("glAccount", UNSET)

        customer_class = d.pop("customerClass", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateERPCompanyBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateERPCompanyBodyStatus(_status)

        _company_type = d.pop("companyType", UNSET)
        company_type: Union[Unset, CreateERPCompanyBodyCompanyType]
        if isinstance(_company_type, Unset):
            company_type = UNSET
        else:
            company_type = CreateERPCompanyBodyCompanyType(_company_type)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateERPCompanyBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateERPCompanyBodyCustomFields.from_dict(_custom_fields)

        create_erp_company_body = cls(
            name=name,
            is_mpc_company=is_mpc_company,
            company_id=company_id,
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
            status=status,
            company_type=company_type,
            custom_fields=custom_fields,
        )

        create_erp_company_body.additional_properties = d
        return create_erp_company_body

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
