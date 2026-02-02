from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSTaskBodyTo")


@_attrs_define
class CreateWMSTaskBodyTo:
    """Destination location details

    Attributes:
        bin_id (Union[Unset, str]):  Example: BIN-SHIP-001.
        bin_code (Union[Unset, str]):  Example: SHIP-001.
        zone_id (Union[Unset, str]):  Example: ZONE-SHIPPING.
    """

    bin_id: Union[Unset, str] = UNSET
    bin_code: Union[Unset, str] = UNSET
    zone_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_id = self.bin_id

        bin_code = self.bin_code

        zone_id = self.zone_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bin_id is not UNSET:
            field_dict["binId"] = bin_id
        if bin_code is not UNSET:
            field_dict["binCode"] = bin_code
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bin_id = d.pop("binId", UNSET)

        bin_code = d.pop("binCode", UNSET)

        zone_id = d.pop("zoneId", UNSET)

        create_wms_task_body_to = cls(
            bin_id=bin_id,
            bin_code=bin_code,
            zone_id=zone_id,
        )

        create_wms_task_body_to.additional_properties = d
        return create_wms_task_body_to

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
