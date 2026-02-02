from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSTaskBodyQuantity")


@_attrs_define
class CreateWMSTaskBodyQuantity:
    """Quantity requirements

    Attributes:
        requested (Union[Unset, float]):  Example: 24.
        uom (Union[Unset, str]):  Example: EA.
    """

    requested: Union[Unset, float] = UNSET
    uom: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested = self.requested

        uom = self.uom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requested is not UNSET:
            field_dict["requested"] = requested
        if uom is not UNSET:
            field_dict["uom"] = uom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requested = d.pop("requested", UNSET)

        uom = d.pop("uom", UNSET)

        create_wms_task_body_quantity = cls(
            requested=requested,
            uom=uom,
        )

        create_wms_task_body_quantity.additional_properties = d
        return create_wms_task_body_quantity

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
