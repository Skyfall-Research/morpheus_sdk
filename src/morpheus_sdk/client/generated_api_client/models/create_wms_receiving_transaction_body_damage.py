from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSReceivingTransactionBodyDamage")


@_attrs_define
class CreateWMSReceivingTransactionBodyDamage:
    """Damage assessment information

    Attributes:
        has_damage (Union[Unset, bool]): Whether damage was observed
        description (Union[Unset, str]): Detailed damage description Example: Dented corner on 3 units, functionality
            unaffected.
        quantity (Union[Unset, float]): Number of damaged units Example: 3.
        reported_by (Union[Unset, str]): User who reported the damage Example: user_receiver_002.
    """

    has_damage: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    reported_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_damage = self.has_damage

        description = self.description

        quantity = self.quantity

        reported_by = self.reported_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_damage is not UNSET:
            field_dict["hasDamage"] = has_damage
        if description is not UNSET:
            field_dict["description"] = description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if reported_by is not UNSET:
            field_dict["reportedBy"] = reported_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_damage = d.pop("hasDamage", UNSET)

        description = d.pop("description", UNSET)

        quantity = d.pop("quantity", UNSET)

        reported_by = d.pop("reportedBy", UNSET)

        create_wms_receiving_transaction_body_damage = cls(
            has_damage=has_damage,
            description=description,
            quantity=quantity,
            reported_by=reported_by,
        )

        create_wms_receiving_transaction_body_damage.additional_properties = d
        return create_wms_receiving_transaction_body_damage

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
