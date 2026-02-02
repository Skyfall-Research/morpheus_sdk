from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSReceivingTransactionDamageType0")


@_attrs_define
class WMSReceivingTransactionDamageType0:
    """Damage assessment and documentation

    Attributes:
        has_damage (Union[Unset, bool]): Flag indicating whether damage was observed
        description (Union[None, Unset, str]): Detailed description of observed damage Example: Dented corner on 3
            units, functionality unaffected.
        quantity (Union[None, Unset, float]): Number of damaged units Example: 3.
        reported_by (Union[None, Unset, str]): User who reported the damage Example: user_receiver_002.
    """

    has_damage: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    reported_by: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_damage = self.has_damage

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        reported_by: Union[None, Unset, str]
        if isinstance(self.reported_by, Unset):
            reported_by = UNSET
        else:
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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_reported_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reported_by = _parse_reported_by(d.pop("reportedBy", UNSET))

        wms_receiving_transaction_damage_type_0 = cls(
            has_damage=has_damage,
            description=description,
            quantity=quantity,
            reported_by=reported_by,
        )

        wms_receiving_transaction_damage_type_0.additional_properties = d
        return wms_receiving_transaction_damage_type_0

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
