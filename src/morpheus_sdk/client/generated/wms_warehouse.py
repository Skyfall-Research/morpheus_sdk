import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_warehouse_status import WMSWarehouseStatus
from ..models.wms_warehouse_warehouse_type import WMSWarehouseWarehouseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_warehouse_address import WMSWarehouseAddress
    from ..models.wms_warehouse_world_ref import WMSWarehouseWorldRef


T = TypeVar("T", bound="WMSWarehouse")


@_attrs_define
class WMSWarehouse:
    """Warehouse facility configuration and management data

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        world_ref (WMSWarehouseWorldRef): Reference to the world environment
        warehouse_id (str): Unique auto-generated warehouse identifier Example: WH_507f1f77bcf86cd799439012.
        warehouse_code (str): Auto-generated warehouse code from warehouse name (slugified) Example: atlanta-
            distribution-center.
        warehouse_name (str): Human readable warehouse name Example: Atlanta Distribution Center.
        address (WMSWarehouseAddress): Physical warehouse address information
        timezone (str): IANA timezone identifier for warehouse operations Example: America/New_York.
        status (WMSWarehouseStatus): Warehouse operational status Default: WMSWarehouseStatus.ACTIVE. Example: ACTIVE.
        created_at (datetime.datetime): Timestamp when the warehouse record was created Example:
            2024-11-27T09:00:00.000Z.
        updated_at (datetime.datetime): Timestamp when the warehouse record was last updated Example:
            2024-11-27T09:35:00.000Z.
        warehouse_type (Union[Unset, WMSWarehouseWarehouseType]): Warehouse operational type classification Example:
            FULFILLMENT.
    """

    field_id: str
    world_ref: "WMSWarehouseWorldRef"
    warehouse_id: str
    warehouse_code: str
    warehouse_name: str
    address: "WMSWarehouseAddress"
    timezone: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status: WMSWarehouseStatus = WMSWarehouseStatus.ACTIVE
    warehouse_type: Union[Unset, WMSWarehouseWarehouseType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_ref = self.world_ref.to_dict()

        warehouse_id = self.warehouse_id

        warehouse_code = self.warehouse_code

        warehouse_name = self.warehouse_name

        address = self.address.to_dict()

        timezone = self.timezone

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        warehouse_type: Union[Unset, str] = UNSET
        if not isinstance(self.warehouse_type, Unset):
            warehouse_type = self.warehouse_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "worldRef": world_ref,
                "warehouseId": warehouse_id,
                "warehouseCode": warehouse_code,
                "warehouseName": warehouse_name,
                "address": address,
                "timezone": timezone,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if warehouse_type is not UNSET:
            field_dict["warehouseType"] = warehouse_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_warehouse_address import WMSWarehouseAddress
        from ..models.wms_warehouse_world_ref import WMSWarehouseWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_ref = WMSWarehouseWorldRef.from_dict(d.pop("worldRef"))

        warehouse_id = d.pop("warehouseId")

        warehouse_code = d.pop("warehouseCode")

        warehouse_name = d.pop("warehouseName")

        address = WMSWarehouseAddress.from_dict(d.pop("address"))

        timezone = d.pop("timezone")

        status = WMSWarehouseStatus(d.pop("status"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _warehouse_type = d.pop("warehouseType", UNSET)
        warehouse_type: Union[Unset, WMSWarehouseWarehouseType]
        if isinstance(_warehouse_type, Unset):
            warehouse_type = UNSET
        else:
            warehouse_type = WMSWarehouseWarehouseType(_warehouse_type)

        wms_warehouse = cls(
            field_id=field_id,
            world_ref=world_ref,
            warehouse_id=warehouse_id,
            warehouse_code=warehouse_code,
            warehouse_name=warehouse_name,
            address=address,
            timezone=timezone,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            warehouse_type=warehouse_type,
        )

        wms_warehouse.additional_properties = d
        return wms_warehouse

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
