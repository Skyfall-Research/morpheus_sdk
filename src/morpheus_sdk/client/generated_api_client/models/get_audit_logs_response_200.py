from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_log import AuditLog
    from ..models.get_audit_logs_response_200_meta import GetAuditLogsResponse200Meta


T = TypeVar("T", bound="GetAuditLogsResponse200")


@_attrs_define
class GetAuditLogsResponse200:
    """
    Attributes:
        success (bool): Indicates if the request was successful Example: True.
        status (int): HTTP status code Example: 200.
        data (list['AuditLog']): Array of audit log entries matching the filter criteria
        meta (GetAuditLogsResponse200Meta):
    """

    success: bool
    status: int
    data: list["AuditLog"]
    meta: "GetAuditLogsResponse200Meta"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "status": status,
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_log import AuditLog
        from ..models.get_audit_logs_response_200_meta import GetAuditLogsResponse200Meta

        d = dict(src_dict)
        success = d.pop("success")

        status = d.pop("status")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = AuditLog.from_dict(data_item_data)

            data.append(data_item)

        meta = GetAuditLogsResponse200Meta.from_dict(d.pop("meta"))

        get_audit_logs_response_200 = cls(
            success=success,
            status=status,
            data=data,
            meta=meta,
        )

        get_audit_logs_response_200.additional_properties = d
        return get_audit_logs_response_200

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
