from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSReplenishmentQuantity")


@_attrs_define
class WMSReplenishmentQuantity:
    """Multi-level quantity tracking throughout replenishment lifecycle

    Attributes:
        suggested (float): Initially suggested quantity for replenishment Example: 150.
        uom (str): Unit of measure for all quantities Example: EA.
        approved (Union[None, Unset, float]): Management-approved quantity (may differ from suggested) Example: 120.
        actual (Union[None, Unset, float]): Actual quantity moved during execution Example: 118.
    """

    suggested: float
    uom: str
    approved: Union[None, Unset, float] = UNSET
    actual: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggested = self.suggested

        uom = self.uom

        approved: Union[None, Unset, float]
        if isinstance(self.approved, Unset):
            approved = UNSET
        else:
            approved = self.approved

        actual: Union[None, Unset, float]
        if isinstance(self.actual, Unset):
            actual = UNSET
        else:
            actual = self.actual

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suggested": suggested,
                "uom": uom,
            }
        )
        if approved is not UNSET:
            field_dict["approved"] = approved
        if actual is not UNSET:
            field_dict["actual"] = actual

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        suggested = d.pop("suggested")

        uom = d.pop("uom")

        def _parse_approved(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        approved = _parse_approved(d.pop("approved", UNSET))

        def _parse_actual(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        actual = _parse_actual(d.pop("actual", UNSET))

        wms_replenishment_quantity = cls(
            suggested=suggested,
            uom=uom,
            approved=approved,
            actual=actual,
        )

        wms_replenishment_quantity.additional_properties = d
        return wms_replenishment_quantity

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
