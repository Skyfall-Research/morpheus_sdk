import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_daily_metrics_body_custom_fields import CreateWMSDailyMetricsBodyCustomFields
    from ..models.create_wms_daily_metrics_body_inbound import CreateWMSDailyMetricsBodyInbound
    from ..models.create_wms_daily_metrics_body_inventory import CreateWMSDailyMetricsBodyInventory
    from ..models.create_wms_daily_metrics_body_labor import CreateWMSDailyMetricsBodyLabor
    from ..models.create_wms_daily_metrics_body_packing import CreateWMSDailyMetricsBodyPacking
    from ..models.create_wms_daily_metrics_body_picking import CreateWMSDailyMetricsBodyPicking
    from ..models.create_wms_daily_metrics_body_putaway import CreateWMSDailyMetricsBodyPutaway
    from ..models.create_wms_daily_metrics_body_quality import CreateWMSDailyMetricsBodyQuality
    from ..models.create_wms_daily_metrics_body_shipping import CreateWMSDailyMetricsBodyShipping


T = TypeVar("T", bound="CreateWMSDailyMetricsBody")


@_attrs_define
class CreateWMSDailyMetricsBody:
    """
    Attributes:
        warehouse_id (str): Warehouse identifier for metrics recording Example: WH_ATL_001.
        date (datetime.date): Date for metrics recording Example: 2024-11-27.
        shift (Union[Unset, str]): Optional shift identifier for shift-based metrics Example: DAY_SHIFT_1.
        zone_id (Union[Unset, str]): Optional zone identifier for zone-based metrics Example: ZONE_PICK_A.
        inbound (Union[Unset, CreateWMSDailyMetricsBodyInbound]): Inbound receiving metrics
        putaway (Union[Unset, CreateWMSDailyMetricsBodyPutaway]): Putaway operation metrics
        picking (Union[Unset, CreateWMSDailyMetricsBodyPicking]): Picking operation metrics
        packing (Union[Unset, CreateWMSDailyMetricsBodyPacking]): Packing operation metrics
        shipping (Union[Unset, CreateWMSDailyMetricsBodyShipping]): Shipping operation metrics
        labor (Union[Unset, CreateWMSDailyMetricsBodyLabor]): Labor and workforce metrics
        inventory (Union[Unset, CreateWMSDailyMetricsBodyInventory]): Inventory management metrics
        quality (Union[Unset, CreateWMSDailyMetricsBodyQuality]): Quality and error tracking metrics
        custom_fields (Union[Unset, CreateWMSDailyMetricsBodyCustomFields]): Additional warehouse-specific metrics
            Example: {'temperatureControlledZones': 4, 'hazMatHandling': True, 'specialEquipmentUsage': 12.5}.
    """

    warehouse_id: str
    date: datetime.date
    shift: Union[Unset, str] = UNSET
    zone_id: Union[Unset, str] = UNSET
    inbound: Union[Unset, "CreateWMSDailyMetricsBodyInbound"] = UNSET
    putaway: Union[Unset, "CreateWMSDailyMetricsBodyPutaway"] = UNSET
    picking: Union[Unset, "CreateWMSDailyMetricsBodyPicking"] = UNSET
    packing: Union[Unset, "CreateWMSDailyMetricsBodyPacking"] = UNSET
    shipping: Union[Unset, "CreateWMSDailyMetricsBodyShipping"] = UNSET
    labor: Union[Unset, "CreateWMSDailyMetricsBodyLabor"] = UNSET
    inventory: Union[Unset, "CreateWMSDailyMetricsBodyInventory"] = UNSET
    quality: Union[Unset, "CreateWMSDailyMetricsBodyQuality"] = UNSET
    custom_fields: Union[Unset, "CreateWMSDailyMetricsBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        date = self.date.isoformat()

        shift = self.shift

        zone_id = self.zone_id

        inbound: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inbound, Unset):
            inbound = self.inbound.to_dict()

        putaway: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.putaway, Unset):
            putaway = self.putaway.to_dict()

        picking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.picking, Unset):
            picking = self.picking.to_dict()

        packing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.packing, Unset):
            packing = self.packing.to_dict()

        shipping: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict()

        labor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.labor, Unset):
            labor = self.labor.to_dict()

        inventory: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = self.inventory.to_dict()

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseId": warehouse_id,
                "date": date,
            }
        )
        if shift is not UNSET:
            field_dict["shift"] = shift
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if inbound is not UNSET:
            field_dict["inbound"] = inbound
        if putaway is not UNSET:
            field_dict["putaway"] = putaway
        if picking is not UNSET:
            field_dict["picking"] = picking
        if packing is not UNSET:
            field_dict["packing"] = packing
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if labor is not UNSET:
            field_dict["labor"] = labor
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if quality is not UNSET:
            field_dict["quality"] = quality
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_daily_metrics_body_custom_fields import CreateWMSDailyMetricsBodyCustomFields
        from ..models.create_wms_daily_metrics_body_inbound import CreateWMSDailyMetricsBodyInbound
        from ..models.create_wms_daily_metrics_body_inventory import CreateWMSDailyMetricsBodyInventory
        from ..models.create_wms_daily_metrics_body_labor import CreateWMSDailyMetricsBodyLabor
        from ..models.create_wms_daily_metrics_body_packing import CreateWMSDailyMetricsBodyPacking
        from ..models.create_wms_daily_metrics_body_picking import CreateWMSDailyMetricsBodyPicking
        from ..models.create_wms_daily_metrics_body_putaway import CreateWMSDailyMetricsBodyPutaway
        from ..models.create_wms_daily_metrics_body_quality import CreateWMSDailyMetricsBodyQuality
        from ..models.create_wms_daily_metrics_body_shipping import CreateWMSDailyMetricsBodyShipping

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        date = isoparse(d.pop("date")).date()

        shift = d.pop("shift", UNSET)

        zone_id = d.pop("zoneId", UNSET)

        _inbound = d.pop("inbound", UNSET)
        inbound: Union[Unset, CreateWMSDailyMetricsBodyInbound]
        if isinstance(_inbound, Unset):
            inbound = UNSET
        else:
            inbound = CreateWMSDailyMetricsBodyInbound.from_dict(_inbound)

        _putaway = d.pop("putaway", UNSET)
        putaway: Union[Unset, CreateWMSDailyMetricsBodyPutaway]
        if isinstance(_putaway, Unset):
            putaway = UNSET
        else:
            putaway = CreateWMSDailyMetricsBodyPutaway.from_dict(_putaway)

        _picking = d.pop("picking", UNSET)
        picking: Union[Unset, CreateWMSDailyMetricsBodyPicking]
        if isinstance(_picking, Unset):
            picking = UNSET
        else:
            picking = CreateWMSDailyMetricsBodyPicking.from_dict(_picking)

        _packing = d.pop("packing", UNSET)
        packing: Union[Unset, CreateWMSDailyMetricsBodyPacking]
        if isinstance(_packing, Unset):
            packing = UNSET
        else:
            packing = CreateWMSDailyMetricsBodyPacking.from_dict(_packing)

        _shipping = d.pop("shipping", UNSET)
        shipping: Union[Unset, CreateWMSDailyMetricsBodyShipping]
        if isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = CreateWMSDailyMetricsBodyShipping.from_dict(_shipping)

        _labor = d.pop("labor", UNSET)
        labor: Union[Unset, CreateWMSDailyMetricsBodyLabor]
        if isinstance(_labor, Unset):
            labor = UNSET
        else:
            labor = CreateWMSDailyMetricsBodyLabor.from_dict(_labor)

        _inventory = d.pop("inventory", UNSET)
        inventory: Union[Unset, CreateWMSDailyMetricsBodyInventory]
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = CreateWMSDailyMetricsBodyInventory.from_dict(_inventory)

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, CreateWMSDailyMetricsBodyQuality]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = CreateWMSDailyMetricsBodyQuality.from_dict(_quality)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateWMSDailyMetricsBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateWMSDailyMetricsBodyCustomFields.from_dict(_custom_fields)

        create_wms_daily_metrics_body = cls(
            warehouse_id=warehouse_id,
            date=date,
            shift=shift,
            zone_id=zone_id,
            inbound=inbound,
            putaway=putaway,
            picking=picking,
            packing=packing,
            shipping=shipping,
            labor=labor,
            inventory=inventory,
            quality=quality,
            custom_fields=custom_fields,
        )

        create_wms_daily_metrics_body.additional_properties = d
        return create_wms_daily_metrics_body

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
