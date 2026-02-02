from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.verify_entity_body_entity_type import VerifyEntityBodyEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verify_entity_body_metadata import VerifyEntityBodyMetadata


T = TypeVar("T", bound="VerifyEntityBody")


@_attrs_define
class VerifyEntityBody:
    """
    Attributes:
        od_id (str): The Operational Descriptor (OD) ID representing the process/workflow type. Example: outbound-
            category-flow.
        entity_id (Union[Unset, str]): The unique ID of the primary entity (e.g., Order ID, Shipment ID) to verify.
            Optional for some ODs. Example: wms:outbound-order:697c660f2c864f4be38f0a1e.
        entity_type (Union[Unset, VerifyEntityBodyEntityType]): The type of the entity being verified. Defaults to
            'ORDER'. Default: VerifyEntityBodyEntityType.ORDER. Example: ORDER.
        metadata (Union[Unset, VerifyEntityBodyMetadata]): Additional context or metadata to pass to the verifier.
            Example: {'snapshotId': 'snap-12345', 'triggerReason': 'manual-check'}.
    """

    od_id: str
    entity_id: Union[Unset, str] = UNSET
    entity_type: Union[Unset, VerifyEntityBodyEntityType] = VerifyEntityBodyEntityType.ORDER
    metadata: Union[Unset, "VerifyEntityBodyMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        od_id = self.od_id

        entity_id = self.entity_id

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "odId": od_id,
            }
        )
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.verify_entity_body_metadata import VerifyEntityBodyMetadata

        d = dict(src_dict)
        od_id = d.pop("odId")

        entity_id = d.pop("entityId", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, VerifyEntityBodyEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = VerifyEntityBodyEntityType(_entity_type)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, VerifyEntityBodyMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = VerifyEntityBodyMetadata.from_dict(_metadata)

        verify_entity_body = cls(
            od_id=od_id,
            entity_id=entity_id,
            entity_type=entity_type,
            metadata=metadata,
        )

        verify_entity_body.additional_properties = d
        return verify_entity_body

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
