import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.finance_transaction_source_type import FinanceTransactionSourceType
from ..models.finance_transaction_type import FinanceTransactionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finance_transaction_metadata import FinanceTransactionMetadata
    from ..models.finance_transaction_world_ref import FinanceTransactionWorldRef


T = TypeVar("T", bound="FinanceTransaction")


@_attrs_define
class FinanceTransaction:
    """Finance transaction with comprehensive financial tracking and business intelligence

    Attributes:
        field_id (str): MongoDB unique identifier Example: 507f1f77bcf86cd799439020.
        world_ref (FinanceTransactionWorldRef): World reference for multi-tenant isolation
        transaction_id (str): Unique transaction identifier (auto-generated via generateIdByService) Example:
            TRANS_507f1f77bcf86cd799439012.
        type_ (FinanceTransactionType): Transaction direction - incoming or outgoing payment (required) Example:
            payment_in.
        amount (float): Transaction amount - must be greater than 0 (required) Example: 1500.
        source_type (FinanceTransactionSourceType): Source document type for transaction linkage (required) Example:
            invoice.
        source_id (str): Source document identifier for audit trail (required) Example: INV_507f1f77bcf86cd799439014.
        field_v (Union[Unset, float]): MongoDB version key
        partner_id (Union[Unset, str]): Business partner identifier for relationship tracking Example:
            PARTNER_507f1f77bcf86cd799439013.
        metadata (Union[Unset, FinanceTransactionMetadata]): Additional transaction-specific data for flexible
            extensions Example: {'paymentMethod': 'ACH', 'bankReference': 'REF123456', 'customerReference': 'CUST_PAY_001',
            'exchangeRate': 1, 'originalCurrency': 'USD'}.
        created_at (Union[Unset, datetime.datetime]): Transaction creation timestamp Example: 2024-01-15T08:00:00.000Z.
        updated_at (Union[Unset, datetime.datetime]): Last update timestamp Example: 2024-01-15T16:45:00.000Z.
    """

    field_id: str
    world_ref: "FinanceTransactionWorldRef"
    transaction_id: str
    type_: FinanceTransactionType
    amount: float
    source_type: FinanceTransactionSourceType
    source_id: str
    field_v: Union[Unset, float] = UNSET
    partner_id: Union[Unset, str] = UNSET
    metadata: Union[Unset, "FinanceTransactionMetadata"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_ref = self.world_ref.to_dict()

        transaction_id = self.transaction_id

        type_ = self.type_.value

        amount = self.amount

        source_type = self.source_type.value

        source_id = self.source_id

        field_v = self.field_v

        partner_id = self.partner_id

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

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
                "transactionId": transaction_id,
                "type": type_,
                "amount": amount,
                "sourceType": source_type,
                "sourceId": source_id,
            }
        )
        if field_v is not UNSET:
            field_dict["__v"] = field_v
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finance_transaction_metadata import FinanceTransactionMetadata
        from ..models.finance_transaction_world_ref import FinanceTransactionWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_ref = FinanceTransactionWorldRef.from_dict(d.pop("worldRef"))

        transaction_id = d.pop("transactionId")

        type_ = FinanceTransactionType(d.pop("type"))

        amount = d.pop("amount")

        source_type = FinanceTransactionSourceType(d.pop("sourceType"))

        source_id = d.pop("sourceId")

        field_v = d.pop("__v", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, FinanceTransactionMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = FinanceTransactionMetadata.from_dict(_metadata)

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

        finance_transaction = cls(
            field_id=field_id,
            world_ref=world_ref,
            transaction_id=transaction_id,
            type_=type_,
            amount=amount,
            source_type=source_type,
            source_id=source_id,
            field_v=field_v,
            partner_id=partner_id,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
        )

        finance_transaction.additional_properties = d
        return finance_transaction

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
