import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_log_after_type_0 import AuditLogAfterType0
    from ..models.audit_log_before_type_0 import AuditLogBeforeType0


T = TypeVar("T", bound="AuditLog")


@_attrs_define
class AuditLog:
    """A single audit log entry tracking data changes within a world environment

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        model (str): The type of data model that was changed Example: EdiTransaction.
        document_id (str): Unique identifier of the document that was changed Example: edi_txn_123456789.
        created_at (datetime.datetime): When this audit log entry was created Example: 2024-01-15T10:25:30.123Z.
        updated_at (datetime.datetime): When this audit log entry was last updated Example: 2024-01-15T10:25:30.123Z.
        changed_by (Union[None, Unset, str]): User ID or system identifier that made the change Example: user_john_doe.
        before (Union['AuditLogBeforeType0', None, Unset]): Complete state of the document before the change (null for
            new documents) Example: {'status': 'PENDING', 'lastUpdated': '2024-01-15T09:00:00.000Z'}.
        after (Union['AuditLogAfterType0', None, Unset]): Complete state of the document after the change (null for
            deleted documents) Example: {'status': 'PROCESSED', 'lastUpdated': '2024-01-15T10:25:30.123Z', 'processedBy':
            'edi-processor-v2'}.
        reason (Union[None, Unset, str]): Optional reason or context for the change Example: Automated EDI processing
            completed.
    """

    field_id: str
    model: str
    document_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    changed_by: Union[None, Unset, str] = UNSET
    before: Union["AuditLogBeforeType0", None, Unset] = UNSET
    after: Union["AuditLogAfterType0", None, Unset] = UNSET
    reason: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_log_after_type_0 import AuditLogAfterType0
        from ..models.audit_log_before_type_0 import AuditLogBeforeType0

        field_id = self.field_id

        model = self.model

        document_id = self.document_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        changed_by: Union[None, Unset, str]
        if isinstance(self.changed_by, Unset):
            changed_by = UNSET
        else:
            changed_by = self.changed_by

        before: Union[None, Unset, dict[str, Any]]
        if isinstance(self.before, Unset):
            before = UNSET
        elif isinstance(self.before, AuditLogBeforeType0):
            before = self.before.to_dict()
        else:
            before = self.before

        after: Union[None, Unset, dict[str, Any]]
        if isinstance(self.after, Unset):
            after = UNSET
        elif isinstance(self.after, AuditLogAfterType0):
            after = self.after.to_dict()
        else:
            after = self.after

        reason: Union[None, Unset, str]
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "model": model,
                "documentId": document_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_log_after_type_0 import AuditLogAfterType0
        from ..models.audit_log_before_type_0 import AuditLogBeforeType0

        d = dict(src_dict)
        field_id = d.pop("_id")

        model = d.pop("model")

        document_id = d.pop("documentId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_changed_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        changed_by = _parse_changed_by(d.pop("changedBy", UNSET))

        def _parse_before(data: object) -> Union["AuditLogBeforeType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                before_type_0 = AuditLogBeforeType0.from_dict(data)

                return before_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AuditLogBeforeType0", None, Unset], data)

        before = _parse_before(d.pop("before", UNSET))

        def _parse_after(data: object) -> Union["AuditLogAfterType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                after_type_0 = AuditLogAfterType0.from_dict(data)

                return after_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AuditLogAfterType0", None, Unset], data)

        after = _parse_after(d.pop("after", UNSET))

        def _parse_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reason = _parse_reason(d.pop("reason", UNSET))

        audit_log = cls(
            field_id=field_id,
            model=model,
            document_id=document_id,
            created_at=created_at,
            updated_at=updated_at,
            changed_by=changed_by,
            before=before,
            after=after,
            reason=reason,
        )

        audit_log.additional_properties = d
        return audit_log

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
