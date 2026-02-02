from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wms_task_reference_type_0_type import WMSTaskReferenceType0Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSTaskReferenceType0")


@_attrs_define
class WMSTaskReferenceType0:
    """Reference to originating business document

    Attributes:
        type_ (Union[Unset, WMSTaskReferenceType0Type]): Type of originating document Example: ORDER.
        id (Union[Unset, str]): Identifier of originating document Example: ORD-12345.
    """

    type_: Union[Unset, WMSTaskReferenceType0Type] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, WMSTaskReferenceType0Type]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WMSTaskReferenceType0Type(_type_)

        id = d.pop("id", UNSET)

        wms_task_reference_type_0 = cls(
            type_=type_,
            id=id,
        )

        wms_task_reference_type_0.additional_properties = d
        return wms_task_reference_type_0

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
