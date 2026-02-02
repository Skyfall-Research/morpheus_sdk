from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_wms_inventory_status_body_inventory_status import UpdateWMSInventoryStatusBodyInventoryStatus

T = TypeVar("T", bound="UpdateWMSInventoryStatusBody")


@_attrs_define
class UpdateWMSInventoryStatusBody:
    """
    Attributes:
        inventory_status (UpdateWMSInventoryStatusBodyInventoryStatus): New status for the inventory item Example: HOLD.
    """

    inventory_status: UpdateWMSInventoryStatusBodyInventoryStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory_status = self.inventory_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inventoryStatus": inventory_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inventory_status = UpdateWMSInventoryStatusBodyInventoryStatus(d.pop("inventoryStatus"))

        update_wms_inventory_status_body = cls(
            inventory_status=inventory_status,
        )

        update_wms_inventory_status_body.additional_properties = d
        return update_wms_inventory_status_body

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
