from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSTaskQuantityType0")


@_attrs_define
class WMSTaskQuantityType0:
    """Quantity requirements and tracking

    Attributes:
        requested (Union[Unset, float]): Originally requested quantity Example: 24.
        actual (Union[None, Unset, float]): Actual quantity handled upon completion Example: 22.
        uom (Union[Unset, str]): Unit of measure for quantities Example: EA.
    """

    requested: Union[Unset, float] = UNSET
    actual: Union[None, Unset, float] = UNSET
    uom: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested = self.requested

        actual: Union[None, Unset, float]
        if isinstance(self.actual, Unset):
            actual = UNSET
        else:
            actual = self.actual

        uom = self.uom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requested is not UNSET:
            field_dict["requested"] = requested
        if actual is not UNSET:
            field_dict["actual"] = actual
        if uom is not UNSET:
            field_dict["uom"] = uom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requested = d.pop("requested", UNSET)

        def _parse_actual(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        actual = _parse_actual(d.pop("actual", UNSET))

        uom = d.pop("uom", UNSET)

        wms_task_quantity_type_0 = cls(
            requested=requested,
            actual=actual,
            uom=uom,
        )

        wms_task_quantity_type_0.additional_properties = d
        return wms_task_quantity_type_0

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
