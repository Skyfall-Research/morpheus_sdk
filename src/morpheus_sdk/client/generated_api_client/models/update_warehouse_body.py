from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_warehouse_body_warehouse_type import UpdateWarehouseBodyWarehouseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_warehouse_body_address import UpdateWarehouseBodyAddress


T = TypeVar("T", bound="UpdateWarehouseBody")


@_attrs_define
class UpdateWarehouseBody:
    """
    Attributes:
        warehouse_name (Union[Unset, str]): Updated warehouse name Example: Enhanced Atlanta Distribution Center.
        address (Union[Unset, UpdateWarehouseBodyAddress]): Updated warehouse address
        timezone (Union[Unset, str]): Updated IANA timezone identifier Example: America/New_York.
        warehouse_type (Union[Unset, UpdateWarehouseBodyWarehouseType]): Updated warehouse operational type Example:
            3PL.
    """

    warehouse_name: Union[Unset, str] = UNSET
    address: Union[Unset, "UpdateWarehouseBodyAddress"] = UNSET
    timezone: Union[Unset, str] = UNSET
    warehouse_type: Union[Unset, UpdateWarehouseBodyWarehouseType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_name = self.warehouse_name

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        timezone = self.timezone

        warehouse_type: Union[Unset, str] = UNSET
        if not isinstance(self.warehouse_type, Unset):
            warehouse_type = self.warehouse_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warehouse_name is not UNSET:
            field_dict["warehouseName"] = warehouse_name
        if address is not UNSET:
            field_dict["address"] = address
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if warehouse_type is not UNSET:
            field_dict["warehouseType"] = warehouse_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_warehouse_body_address import UpdateWarehouseBodyAddress

        d = dict(src_dict)
        warehouse_name = d.pop("warehouseName", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, UpdateWarehouseBodyAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = UpdateWarehouseBodyAddress.from_dict(_address)

        timezone = d.pop("timezone", UNSET)

        _warehouse_type = d.pop("warehouseType", UNSET)
        warehouse_type: Union[Unset, UpdateWarehouseBodyWarehouseType]
        if isinstance(_warehouse_type, Unset):
            warehouse_type = UNSET
        else:
            warehouse_type = UpdateWarehouseBodyWarehouseType(_warehouse_type)

        update_warehouse_body = cls(
            warehouse_name=warehouse_name,
            address=address,
            timezone=timezone,
            warehouse_type=warehouse_type,
        )

        update_warehouse_body.additional_properties = d
        return update_warehouse_body

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
