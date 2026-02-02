from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.verify_entity_body_entity_type import VerifyEntityBodyEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyEntityBody")


@_attrs_define
class VerifyEntityBody:
    """
    Attributes:
        od_id (str): The Operational Descriptor (OD) ID representing the process/workflow type. Example: outbound-
            category-flow.
        entity_id (str): The unique ID of the primary entity (e.g., Order ID, Shipment ID) to verify. Example:
            wms:outbound-order:697c660f2c864f4be38f0a1e.
        entity_type (Union[Unset, VerifyEntityBodyEntityType]): The type of the entity being verified. Defaults to
            'ORDER'. Default: VerifyEntityBodyEntityType.ORDER. Example: ORDER.
    """

    od_id: str
    entity_id: str
    entity_type: Union[Unset, VerifyEntityBodyEntityType] = VerifyEntityBodyEntityType.ORDER
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        od_id = self.od_id

        entity_id = self.entity_id

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "odId": od_id,
                "entityId": entity_id,
            }
        )
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        od_id = d.pop("odId")

        entity_id = d.pop("entityId")

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, VerifyEntityBodyEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = VerifyEntityBodyEntityType(_entity_type)

        verify_entity_body = cls(
            od_id=od_id,
            entity_id=entity_id,
            entity_type=entity_type,
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
