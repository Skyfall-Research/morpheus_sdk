import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.world_log_level import WorldLogLevel
from ..models.world_log_service_type import WorldLogServiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.world_log_metadata import WorldLogMetadata
    from ..models.world_log_world_ref import WorldLogWorldRef


T = TypeVar("T", bound="WorldLog")


@_attrs_define
class WorldLog:
    """A single operational log entry within a world environment

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        world_ref (WorldLogWorldRef): Reference to the world this log belongs to
        log_id (str): Unique identifier for this log entry Example: log_123456789.
        timestamp (datetime.datetime): When this log entry was created Example: 2024-01-15T10:25:30.123Z.
        service_type (WorldLogServiceType): Type of service that generated this log Example: edi.
        level (WorldLogLevel): Severity level of the log entry Example: info.
        msg (str): Human-readable log message Example: EDI 850 Purchase Order processed successfully.
        metadata (Union[Unset, WorldLogMetadata]): Additional structured data related to this log entry Example:
            {'transactionId': 'txn_789abc', 'partnerId': 'partner_456', 'docType': '850', 'direction': 'IN',
            'processingTime': 1250}.
    """

    field_id: str
    world_ref: "WorldLogWorldRef"
    log_id: str
    timestamp: datetime.datetime
    service_type: WorldLogServiceType
    level: WorldLogLevel
    msg: str
    metadata: Union[Unset, "WorldLogMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_ref = self.world_ref.to_dict()

        log_id = self.log_id

        timestamp = self.timestamp.isoformat()

        service_type = self.service_type.value

        level = self.level.value

        msg = self.msg

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "worldRef": world_ref,
                "logId": log_id,
                "timestamp": timestamp,
                "serviceType": service_type,
                "level": level,
                "msg": msg,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.world_log_metadata import WorldLogMetadata
        from ..models.world_log_world_ref import WorldLogWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_ref = WorldLogWorldRef.from_dict(d.pop("worldRef"))

        log_id = d.pop("logId")

        timestamp = isoparse(d.pop("timestamp"))

        service_type = WorldLogServiceType(d.pop("serviceType"))

        level = WorldLogLevel(d.pop("level"))

        msg = d.pop("msg")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, WorldLogMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = WorldLogMetadata.from_dict(_metadata)

        world_log = cls(
            field_id=field_id,
            world_ref=world_ref,
            log_id=log_id,
            timestamp=timestamp,
            service_type=service_type,
            level=level,
            msg=msg,
            metadata=metadata,
        )

        world_log.additional_properties = d
        return world_log

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
