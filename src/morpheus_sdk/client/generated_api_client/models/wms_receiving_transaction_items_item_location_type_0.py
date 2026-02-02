from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSReceivingTransactionItemsItemLocationType0")


@_attrs_define
class WMSReceivingTransactionItemsItemLocationType0:
    """Storage location assignment for this item

    Attributes:
        bin_id (Union[None, Unset, str]): Specific bin location Example: BIN-A-01-01.
        zone_id (Union[None, Unset, str]): Zone identifier Example: ZONE-A.
    """

    bin_id: Union[None, Unset, str] = UNSET
    zone_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_id: Union[None, Unset, str]
        if isinstance(self.bin_id, Unset):
            bin_id = UNSET
        else:
            bin_id = self.bin_id

        zone_id: Union[None, Unset, str]
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        else:
            zone_id = self.zone_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bin_id is not UNSET:
            field_dict["binId"] = bin_id
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bin_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bin_id = _parse_bin_id(d.pop("binId", UNSET))

        def _parse_zone_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zone_id = _parse_zone_id(d.pop("zoneId", UNSET))

        wms_receiving_transaction_items_item_location_type_0 = cls(
            bin_id=bin_id,
            zone_id=zone_id,
        )

        wms_receiving_transaction_items_item_location_type_0.additional_properties = d
        return wms_receiving_transaction_items_item_location_type_0

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
