import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.erp_payment_method import ERPPaymentMethod
from ..models.erp_payment_status import ERPPaymentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_payment_bank_details import ERPPaymentBankDetails
    from ..models.erp_payment_custom_fields import ERPPaymentCustomFields
    from ..models.payment_allocation import PaymentAllocation


T = TypeVar("T", bound="ERPPayment")


@_attrs_define
class ERPPayment:
    """ERP payment with comprehensive financial and allocation management

    Attributes:
        field_id (str): MongoDB unique identifier Example: 507f1f77bcf86cd799439020.
        world_id (str): World environment identifier Example: 507f1f77bcf86cd799439011.
        payment_id (str): Unique payment identifier (auto-generated via generateIdByService) Example:
            PAY_507f1f77bcf86cd799439012.
        customer_id (str): Customer identifier (required for payment processing) Example: CUST_507f1f77bcf86cd799439014.
        payment_date (datetime.date): Date when payment was received (required) Example: 2024-01-15.
        total_amount (float): Total payment amount (required) Example: 1500.
        field_v (Union[Unset, float]): MongoDB version key
        remittance_id (Union[Unset, str]): Remittance advice identifier for payment tracking Example:
            REM_507f1f77bcf86cd799439013.
        partner_id (Union[Unset, str]): Partner identifier for B2B payment relationships Example:
            PARTNER_507f1f77bcf86cd799439015.
        currency (Union[Unset, str]): Payment currency code Default: 'USD'. Example: USD.
        method (Union[Unset, ERPPaymentMethod]): Payment method used Default: ERPPaymentMethod.ACH. Example: ACH.
        bank_details (Union[Unset, ERPPaymentBankDetails]): Banking information for payment processing
        allocations (Union[Unset, list['PaymentAllocation']]): Payment allocations to invoices with comprehensive
            tracking
        status (Union[Unset, ERPPaymentStatus]): Current payment processing status Default: ERPPaymentStatus.RECEIVED.
            Example: RECEIVED.
        edi_transaction_id (Union[Unset, str]): Reference to inbound EDI 820 transaction ID Example:
            507f1f77bcf86cd799439021.
        reference_numbers (Union[Unset, list[str]]): Payment reference numbers for tracking Example: ['REF001',
            'CHECK12345'].
        notes (Union[Unset, str]): Payment notes and additional information Example: Customer payment for invoices
            INV_001 and INV_002.
        flow_id (Union[Unset, str]): Business flow identifier for payment processing Example: FLOW_AR_PROCESSING.
        custom_fields (Union[Unset, ERPPaymentCustomFields]): Additional payment-specific fields Example:
            {'processingFee': 5, 'customerReference': 'CUST_PAY_001'}.
        created_at (Union[Unset, datetime.datetime]): Payment creation timestamp Example: 2024-01-15T08:00:00.000Z.
        updated_at (Union[Unset, datetime.datetime]): Last update timestamp Example: 2024-01-15T16:45:00.000Z.
    """

    field_id: str
    world_id: str
    payment_id: str
    customer_id: str
    payment_date: datetime.date
    total_amount: float
    field_v: Union[Unset, float] = UNSET
    remittance_id: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = "USD"
    method: Union[Unset, ERPPaymentMethod] = ERPPaymentMethod.ACH
    bank_details: Union[Unset, "ERPPaymentBankDetails"] = UNSET
    allocations: Union[Unset, list["PaymentAllocation"]] = UNSET
    status: Union[Unset, ERPPaymentStatus] = ERPPaymentStatus.RECEIVED
    edi_transaction_id: Union[Unset, str] = UNSET
    reference_numbers: Union[Unset, list[str]] = UNSET
    notes: Union[Unset, str] = UNSET
    flow_id: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "ERPPaymentCustomFields"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_id = self.world_id

        payment_id = self.payment_id

        customer_id = self.customer_id

        payment_date = self.payment_date.isoformat()

        total_amount = self.total_amount

        field_v = self.field_v

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

        edi_transaction_id = self.edi_transaction_id

        reference_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reference_numbers, Unset):
            reference_numbers = self.reference_numbers

        notes = self.notes

        flow_id = self.flow_id

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
                "worldId": world_id,
                "paymentId": payment_id,
                "customerId": customer_id,
                "paymentDate": payment_date,
                "totalAmount": total_amount,
            }
        )
        if field_v is not UNSET:
            field_dict["__v"] = field_v
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
        if edi_transaction_id is not UNSET:
            field_dict["ediTransactionId"] = edi_transaction_id
        if reference_numbers is not UNSET:
            field_dict["referenceNumbers"] = reference_numbers
        if notes is not UNSET:
            field_dict["notes"] = notes
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_payment_bank_details import ERPPaymentBankDetails
        from ..models.erp_payment_custom_fields import ERPPaymentCustomFields
        from ..models.payment_allocation import PaymentAllocation

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_id = d.pop("worldId")

        payment_id = d.pop("paymentId")

        customer_id = d.pop("customerId")

        payment_date = isoparse(d.pop("paymentDate")).date()

        total_amount = d.pop("totalAmount")

        field_v = d.pop("__v", UNSET)

        remittance_id = d.pop("remittanceId", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        currency = d.pop("currency", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, ERPPaymentMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = ERPPaymentMethod(_method)

        _bank_details = d.pop("bankDetails", UNSET)
        bank_details: Union[Unset, ERPPaymentBankDetails]
        if isinstance(_bank_details, Unset):
            bank_details = UNSET
        else:
            bank_details = ERPPaymentBankDetails.from_dict(_bank_details)

        allocations = []
        _allocations = d.pop("allocations", UNSET)
        for allocations_item_data in _allocations or []:
            allocations_item = PaymentAllocation.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ERPPaymentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ERPPaymentStatus(_status)

        edi_transaction_id = d.pop("ediTransactionId", UNSET)

        reference_numbers = cast(list[str], d.pop("referenceNumbers", UNSET))

        notes = d.pop("notes", UNSET)

        flow_id = d.pop("flowId", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, ERPPaymentCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ERPPaymentCustomFields.from_dict(_custom_fields)

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

        erp_payment = cls(
            field_id=field_id,
            world_id=world_id,
            payment_id=payment_id,
            customer_id=customer_id,
            payment_date=payment_date,
            total_amount=total_amount,
            field_v=field_v,
            remittance_id=remittance_id,
            partner_id=partner_id,
            currency=currency,
            method=method,
            bank_details=bank_details,
            allocations=allocations,
            status=status,
            edi_transaction_id=edi_transaction_id,
            reference_numbers=reference_numbers,
            notes=notes,
            flow_id=flow_id,
            custom_fields=custom_fields,
            created_at=created_at,
            updated_at=updated_at,
        )

        erp_payment.additional_properties = d
        return erp_payment

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
