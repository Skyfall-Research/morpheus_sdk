import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_erp_payment_body_method import CreateERPPaymentBodyMethod
from ..models.create_erp_payment_body_status import CreateERPPaymentBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_erp_payment_body_allocations_item import CreateERPPaymentBodyAllocationsItem
    from ..models.create_erp_payment_body_bank_details import CreateERPPaymentBodyBankDetails
    from ..models.create_erp_payment_body_custom_fields import CreateERPPaymentBodyCustomFields


T = TypeVar("T", bound="CreateERPPaymentBody")


@_attrs_define
class CreateERPPaymentBody:
    """
    Attributes:
        customer_id (str): Customer identifier (required) Example: CUST_507f1f77bcf86cd799439014.
        payment_date (datetime.date): Payment date (required) Example: 2024-01-15.
        total_amount (float): Total payment amount (required) Example: 1500.
        payment_id (Union[Unset, str]): Optional custom payment identifier (auto-generated if not provided) Example:
            PAY_507f1f77bcf86cd799439012.
        remittance_id (Union[Unset, str]): Remittance advice identifier Example: REM_507f1f77bcf86cd799439013.
        partner_id (Union[Unset, str]): Partner identifier for B2B relationships Example:
            PARTNER_507f1f77bcf86cd799439015.
        currency (Union[Unset, str]): Payment currency Default: 'USD'. Example: USD.
        method (Union[Unset, CreateERPPaymentBodyMethod]): Payment method Default: CreateERPPaymentBodyMethod.ACH.
            Example: ACH.
        bank_details (Union[Unset, CreateERPPaymentBodyBankDetails]): Banking information for payment processing
        allocations (Union[Unset, list['CreateERPPaymentBodyAllocationsItem']]): Payment allocations to invoices
        status (Union[Unset, CreateERPPaymentBodyStatus]): Payment processing status Default:
            CreateERPPaymentBodyStatus.RECEIVED. Example: RECEIVED.
        reference_numbers (Union[Unset, list[str]]): Payment reference numbers Example: ['REF001', 'CHECK12345'].
        notes (Union[Unset, str]): Payment notes and additional information Example: Customer payment for invoices
            INV_001 and INV_002.
        flow_id (Union[Unset, str]): Business flow identifier Example: FLOW_AR_PROCESSING.
        custom_fields (Union[Unset, CreateERPPaymentBodyCustomFields]): Additional payment-specific fields Example:
            {'processingFee': 5, 'customerReference': 'CUST_PAY_001'}.
    """

    customer_id: str
    payment_date: datetime.date
    total_amount: float
    payment_id: Union[Unset, str] = UNSET
    remittance_id: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = "USD"
    method: Union[Unset, CreateERPPaymentBodyMethod] = CreateERPPaymentBodyMethod.ACH
    bank_details: Union[Unset, "CreateERPPaymentBodyBankDetails"] = UNSET
    allocations: Union[Unset, list["CreateERPPaymentBodyAllocationsItem"]] = UNSET
    status: Union[Unset, CreateERPPaymentBodyStatus] = CreateERPPaymentBodyStatus.RECEIVED
    reference_numbers: Union[Unset, list[str]] = UNSET
    notes: Union[Unset, str] = UNSET
    flow_id: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "CreateERPPaymentBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        payment_date = self.payment_date.isoformat()

        total_amount = self.total_amount

        payment_id = self.payment_id

        remittance_id = self.remittance_id

        partner_id = self.partner_id

        currency = self.currency

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        bank_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bank_details, Unset):
            bank_details = self.bank_details.to_dict()

        allocations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allocations, Unset):
            allocations = []
            for allocations_item_data in self.allocations:
                allocations_item = allocations_item_data.to_dict()
                allocations.append(allocations_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        reference_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reference_numbers, Unset):
            reference_numbers = self.reference_numbers

        notes = self.notes

        flow_id = self.flow_id

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
                "paymentDate": payment_date,
                "totalAmount": total_amount,
            }
        )
        if payment_id is not UNSET:
            field_dict["paymentId"] = payment_id
        if remittance_id is not UNSET:
            field_dict["remittanceId"] = remittance_id
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if method is not UNSET:
            field_dict["method"] = method
        if bank_details is not UNSET:
            field_dict["bankDetails"] = bank_details
        if allocations is not UNSET:
            field_dict["allocations"] = allocations
        if status is not UNSET:
            field_dict["status"] = status
        if reference_numbers is not UNSET:
            field_dict["referenceNumbers"] = reference_numbers
        if notes is not UNSET:
            field_dict["notes"] = notes
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_erp_payment_body_allocations_item import CreateERPPaymentBodyAllocationsItem
        from ..models.create_erp_payment_body_bank_details import CreateERPPaymentBodyBankDetails
        from ..models.create_erp_payment_body_custom_fields import CreateERPPaymentBodyCustomFields

        d = dict(src_dict)
        customer_id = d.pop("customerId")

        payment_date = isoparse(d.pop("paymentDate")).date()

        total_amount = d.pop("totalAmount")

        payment_id = d.pop("paymentId", UNSET)

        remittance_id = d.pop("remittanceId", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        currency = d.pop("currency", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, CreateERPPaymentBodyMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = CreateERPPaymentBodyMethod(_method)

        _bank_details = d.pop("bankDetails", UNSET)
        bank_details: Union[Unset, CreateERPPaymentBodyBankDetails]
        if isinstance(_bank_details, Unset):
            bank_details = UNSET
        else:
            bank_details = CreateERPPaymentBodyBankDetails.from_dict(_bank_details)

        allocations = []
        _allocations = d.pop("allocations", UNSET)
        for allocations_item_data in _allocations or []:
            allocations_item = CreateERPPaymentBodyAllocationsItem.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateERPPaymentBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateERPPaymentBodyStatus(_status)

        reference_numbers = cast(list[str], d.pop("referenceNumbers", UNSET))

        notes = d.pop("notes", UNSET)

        flow_id = d.pop("flowId", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateERPPaymentBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateERPPaymentBodyCustomFields.from_dict(_custom_fields)

        create_erp_payment_body = cls(
            customer_id=customer_id,
            payment_date=payment_date,
            total_amount=total_amount,
            payment_id=payment_id,
            remittance_id=remittance_id,
            partner_id=partner_id,
            currency=currency,
            method=method,
            bank_details=bank_details,
            allocations=allocations,
            status=status,
            reference_numbers=reference_numbers,
            notes=notes,
            flow_id=flow_id,
            custom_fields=custom_fields,
        )

        create_erp_payment_body.additional_properties = d
        return create_erp_payment_body

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
