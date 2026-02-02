from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_warehouse_body_status import CreateWarehouseBodyStatus
from ..models.create_warehouse_body_warehouse_type import CreateWarehouseBodyWarehouseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_warehouse_body_address import CreateWarehouseBodyAddress


T = TypeVar("T", bound="CreateWarehouseBody")


@_attrs_define
class CreateWarehouseBody:
    """
    Attributes:
        warehouse_name (str): Human readable warehouse name Example: Atlanta Distribution Center.
        address (CreateWarehouseBodyAddress): Physical warehouse address
        timezone (str): IANA timezone identifier Example: America/New_York.
        warehouse_type (Union[Unset, CreateWarehouseBodyWarehouseType]): Warehouse operational classification Example:
            FULFILLMENT.
        status (Union[Unset, CreateWarehouseBodyStatus]): Warehouse operational status Default:
            CreateWarehouseBodyStatus.ACTIVE. Example: ACTIVE.
    """

    warehouse_name: str
    address: "CreateWarehouseBodyAddress"
    timezone: str
    warehouse_type: Union[Unset, CreateWarehouseBodyWarehouseType] = UNSET
    status: Union[Unset, CreateWarehouseBodyStatus] = CreateWarehouseBodyStatus.ACTIVE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_name = self.warehouse_name

        address = self.address.to_dict()

        timezone = self.timezone

        warehouse_type: Union[Unset, str] = UNSET
        if not isinstance(self.warehouse_type, Unset):
            warehouse_type = self.warehouse_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseName": warehouse_name,
                "address": address,
                "timezone": timezone,
            }
        )
        if warehouse_type is not UNSET:
            field_dict["warehouseType"] = warehouse_type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_warehouse_body_address import CreateWarehouseBodyAddress

        d = dict(src_dict)
        warehouse_name = d.pop("warehouseName")

        address = CreateWarehouseBodyAddress.from_dict(d.pop("address"))

        timezone = d.pop("timezone")

        _warehouse_type = d.pop("warehouseType", UNSET)
        warehouse_type: Union[Unset, CreateWarehouseBodyWarehouseType]
        if isinstance(_warehouse_type, Unset):
            warehouse_type = UNSET
        else:
            warehouse_type = CreateWarehouseBodyWarehouseType(_warehouse_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateWarehouseBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateWarehouseBodyStatus(_status)

        create_warehouse_body = cls(
            warehouse_name=warehouse_name,
            address=address,
            timezone=timezone,
            warehouse_type=warehouse_type,
            status=status,
        )

        create_warehouse_body.additional_properties = d
        return create_warehouse_body

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
