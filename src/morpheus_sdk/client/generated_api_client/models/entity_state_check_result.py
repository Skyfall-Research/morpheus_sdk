from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EntityStateCheckResult")


@_attrs_define
class EntityStateCheckResult:
    """Result of an entity state check

    Attributes:
        entity_type (str): Type of the entity Example: shipment.
        entity_id (str): ID of the entity Example: SHP_12345.
        expected_states (list[str]): List of allowed states Example: ['SHIPPED', 'DELIVERED'].
        actual_state (str): Actual state of the entity Example: PENDING.
        passed (bool): Whether the check passed
    """

    entity_type: str
    entity_id: str
    expected_states: list[str]
    actual_state: str
    passed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type

        entity_id = self.entity_id

        expected_states = self.expected_states

        actual_state = self.actual_state

        passed = self.passed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityType": entity_type,
                "entityId": entity_id,
                "expectedStates": expected_states,
                "actualState": actual_state,
                "passed": passed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_type = d.pop("entityType")

        entity_id = d.pop("entityId")

        expected_states = cast(list[str], d.pop("expectedStates"))

        actual_state = d.pop("actualState")

        passed = d.pop("passed")

        entity_state_check_result = cls(
            entity_type=entity_type,
            entity_id=entity_id,
            expected_states=expected_states,
            actual_state=actual_state,
            passed=passed,
        )

        entity_state_check_result.additional_properties = d
        return entity_state_check_result

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
