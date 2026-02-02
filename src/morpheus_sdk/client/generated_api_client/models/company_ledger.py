import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_ledger_world_ref import CompanyLedgerWorldRef


T = TypeVar("T", bound="CompanyLedger")


@_attrs_define
class CompanyLedger:
    """Company ledger with comprehensive financial position tracking and automatic net position calculation

    Attributes:
        field_id (str): MongoDB unique identifier Example: 507f1f77bcf86cd799439020.
        world_ref (CompanyLedgerWorldRef): World reference for multi-tenant isolation
        cash (float): Company cash position Default: 0.0. Example: 25000.
        total_receivables (float): Total accounts receivable outstanding Default: 0.0. Example: 45000.
        total_payables (float): Total accounts payable outstanding Default: 0.0. Example: 18000.
        net_position (float): Calculated net financial position (cash + receivables - payables) - Auto-calculated,
            cannot be manually set Example: 52000.
        field_v (Union[Unset, float]): MongoDB version key
        created_at (Union[Unset, datetime.datetime]): Ledger creation timestamp Example: 2024-01-15T08:00:00.000Z.
        updated_at (Union[Unset, datetime.datetime]): Last update timestamp Example: 2024-01-15T16:45:00.000Z.
    """

    field_id: str
    world_ref: "CompanyLedgerWorldRef"
    net_position: float
    cash: float = 0.0
    total_receivables: float = 0.0
    total_payables: float = 0.0
    field_v: Union[Unset, float] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_ref = self.world_ref.to_dict()

        cash = self.cash

        total_receivables = self.total_receivables

        total_payables = self.total_payables

        net_position = self.net_position

        field_v = self.field_v

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
                "cash": cash,
                "totalReceivables": total_receivables,
                "totalPayables": total_payables,
                "netPosition": net_position,
            }
        )
        if field_v is not UNSET:
            field_dict["__v"] = field_v
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_ledger_world_ref import CompanyLedgerWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_ref = CompanyLedgerWorldRef.from_dict(d.pop("worldRef"))

        cash = d.pop("cash")

        total_receivables = d.pop("totalReceivables")

        total_payables = d.pop("totalPayables")

        net_position = d.pop("netPosition")

        field_v = d.pop("__v", UNSET)

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

        company_ledger = cls(
            field_id=field_id,
            world_ref=world_ref,
            cash=cash,
            total_receivables=total_receivables,
            total_payables=total_payables,
            net_position=net_position,
            field_v=field_v,
            created_at=created_at,
            updated_at=updated_at,
        )

        company_ledger.additional_properties = d
        return company_ledger

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
