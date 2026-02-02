import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.edi_transaction_direction import EdiTransactionDirection
from ..models.edi_transaction_doc_type import EdiTransactionDocType
from ..models.edi_transaction_status import EdiTransactionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edi_transaction_error_details import EdiTransactionErrorDetails
    from ..models.edi_transaction_payload import EdiTransactionPayload


T = TypeVar("T", bound="EdiTransaction")


@_attrs_define
class EdiTransaction:
    """Electronic Data Interchange transaction for B2B document exchange

    Attributes:
        field_id (str): Unique database identifier for the EDI transaction Example: 507f1f77bcf86cd799439015.
        transaction_id (str): System-generated unique transaction identifier Example: edi_edi_2024_001.
        partner_id (str): Trading partner identifier Example: PARTNER_WALMART_001.
        doc_type (EdiTransactionDocType): EDI document type code (850=PO, 810=Invoice, 856=ASN, etc.) Example: 810.
        direction (EdiTransactionDirection): Transaction direction - IN=received, OUT=sending Example: IN.
        timestamp (datetime.datetime): When the EDI transaction was processed Example: 2024-01-15T09:30:00.000Z.
        status (EdiTransactionStatus): Current processing status of the transaction Example: ERRORED.
        created_at (datetime.datetime): When the transaction record was created Example: 2024-01-15T09:30:00.000Z.
        updated_at (datetime.datetime): When the transaction record was last modified Example: 2024-01-15T09:35:00.000Z.
        customer_id (Union[Unset, str]): Customer identifier (optional, used for simulation) Example:
            CUSTOMER_AMAZON_123.
        company_id (Union[Unset, str]): Portal company identifier (optional) Example: COMPANY_SKYFALL_MAIN.
        dollar_value (Union[Unset, float]): Monetary value extracted from the EDI document Example: 1250.
        interchange_control_number (Union[Unset, str]): ISA13 - X12 Interchange Control Number for correlation Example:
            000000001.
        group_control_number (Union[Unset, str]): GS06 - X12 Functional Group Control Number Example: 1.
        transaction_set_control_number (Union[Unset, str]): ST02 - X12 Transaction Set Control Number Example: 0001.
        business_document_number (Union[Unset, str]): Business-level document identifier (PO#, Invoice#, ASN#) Example:
            INV-2024-001.
        error_reason (Union[Unset, str]): Reason for error if status is ERRORED Example: Validation failed: Missing
            required field TXN02.
        error_details (Union[Unset, EdiTransactionErrorDetails]): Detailed error information for troubleshooting
            Example: {'segment': 'TXN', 'position': '02', 'field': 'Total Amount', 'error': 'Required field missing'}.
        file_name (Union[Unset, str]): Original filename if transaction originated from file Example:
            invoice_walmart_20240115.edi.
        flow_id (Union[Unset, str]): Business flow identifier for transaction correlation Example: FLOW_PO_2024_001.
        raw_edi (Union[Unset, str]): Complete raw EDI X12/EDIFACT document text Example: ISA*00*          *00*
            *ZZ*WALMART      *ZZ*SKYFALL      *240115*1030*U*00401*000000001*0*P*>~GS*IN*WALMART*SKYFALL*20240115*1030*1*X*0
            04010~ST*810*0001~BIG*20240115*INV-2024-001*PO-2024-5678~....
        payload (Union[Unset, EdiTransactionPayload]): Structured metadata or parsed EDI business data Example:
            {'invoiceNumber': 'INV-2024-001', 'poNumber': 'PO-2024-5678', 'totalAmount': 1250, 'lineItems': 5, 'department':
            'DEPT001', 'requestedDeliveryDate': '2024-01-20'}.
    """

    field_id: str
    transaction_id: str
    partner_id: str
    doc_type: EdiTransactionDocType
    direction: EdiTransactionDirection
    timestamp: datetime.datetime
    status: EdiTransactionStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    customer_id: Union[Unset, str] = UNSET
    company_id: Union[Unset, str] = UNSET
    dollar_value: Union[Unset, float] = UNSET
    interchange_control_number: Union[Unset, str] = UNSET
    group_control_number: Union[Unset, str] = UNSET
    transaction_set_control_number: Union[Unset, str] = UNSET
    business_document_number: Union[Unset, str] = UNSET
    error_reason: Union[Unset, str] = UNSET
    error_details: Union[Unset, "EdiTransactionErrorDetails"] = UNSET
    file_name: Union[Unset, str] = UNSET
    flow_id: Union[Unset, str] = UNSET
    raw_edi: Union[Unset, str] = UNSET
    payload: Union[Unset, "EdiTransactionPayload"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        transaction_id = self.transaction_id

        partner_id = self.partner_id

        doc_type = self.doc_type.value

        direction = self.direction.value

        timestamp = self.timestamp.isoformat()

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        customer_id = self.customer_id

        company_id = self.company_id

        dollar_value = self.dollar_value

        interchange_control_number = self.interchange_control_number

        group_control_number = self.group_control_number

        transaction_set_control_number = self.transaction_set_control_number

        business_document_number = self.business_document_number

        error_reason = self.error_reason

        error_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error_details, Unset):
            error_details = self.error_details.to_dict()

        file_name = self.file_name

        flow_id = self.flow_id

        raw_edi = self.raw_edi

        payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "transactionId": transaction_id,
                "partnerId": partner_id,
                "docType": doc_type,
                "direction": direction,
                "timestamp": timestamp,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if dollar_value is not UNSET:
            field_dict["dollarValue"] = dollar_value
        if interchange_control_number is not UNSET:
            field_dict["interchangeControlNumber"] = interchange_control_number
        if group_control_number is not UNSET:
            field_dict["groupControlNumber"] = group_control_number
        if transaction_set_control_number is not UNSET:
            field_dict["transactionSetControlNumber"] = transaction_set_control_number
        if business_document_number is not UNSET:
            field_dict["businessDocumentNumber"] = business_document_number
        if error_reason is not UNSET:
            field_dict["errorReason"] = error_reason
        if error_details is not UNSET:
            field_dict["errorDetails"] = error_details
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if raw_edi is not UNSET:
            field_dict["rawEdi"] = raw_edi
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edi_transaction_error_details import EdiTransactionErrorDetails
        from ..models.edi_transaction_payload import EdiTransactionPayload

        d = dict(src_dict)
        field_id = d.pop("_id")

        transaction_id = d.pop("transactionId")

        partner_id = d.pop("partnerId")

        doc_type = EdiTransactionDocType(d.pop("docType"))

        direction = EdiTransactionDirection(d.pop("direction"))

        timestamp = isoparse(d.pop("timestamp"))

        status = EdiTransactionStatus(d.pop("status"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        customer_id = d.pop("customerId", UNSET)

        company_id = d.pop("companyId", UNSET)

        dollar_value = d.pop("dollarValue", UNSET)

        interchange_control_number = d.pop("interchangeControlNumber", UNSET)

        group_control_number = d.pop("groupControlNumber", UNSET)

        transaction_set_control_number = d.pop("transactionSetControlNumber", UNSET)

        business_document_number = d.pop("businessDocumentNumber", UNSET)

        error_reason = d.pop("errorReason", UNSET)

        _error_details = d.pop("errorDetails", UNSET)
        error_details: Union[Unset, EdiTransactionErrorDetails]
        if isinstance(_error_details, Unset):
            error_details = UNSET
        else:
            error_details = EdiTransactionErrorDetails.from_dict(_error_details)

        file_name = d.pop("fileName", UNSET)

        flow_id = d.pop("flowId", UNSET)

        raw_edi = d.pop("rawEdi", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, EdiTransactionPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = EdiTransactionPayload.from_dict(_payload)

        edi_transaction = cls(
            field_id=field_id,
            transaction_id=transaction_id,
            partner_id=partner_id,
            doc_type=doc_type,
            direction=direction,
            timestamp=timestamp,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            customer_id=customer_id,
            company_id=company_id,
            dollar_value=dollar_value,
            interchange_control_number=interchange_control_number,
            group_control_number=group_control_number,
            transaction_set_control_number=transaction_set_control_number,
            business_document_number=business_document_number,
            error_reason=error_reason,
            error_details=error_details,
            file_name=file_name,
            flow_id=flow_id,
            raw_edi=raw_edi,
            payload=payload,
        )

        edi_transaction.additional_properties = d
        return edi_transaction

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
