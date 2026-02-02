import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_daily_metrics_custom_fields import WMSDailyMetricsCustomFields
    from ..models.wms_daily_metrics_inbound import WMSDailyMetricsInbound
    from ..models.wms_daily_metrics_inventory import WMSDailyMetricsInventory
    from ..models.wms_daily_metrics_labor import WMSDailyMetricsLabor
    from ..models.wms_daily_metrics_packing import WMSDailyMetricsPacking
    from ..models.wms_daily_metrics_picking import WMSDailyMetricsPicking
    from ..models.wms_daily_metrics_putaway import WMSDailyMetricsPutaway
    from ..models.wms_daily_metrics_quality import WMSDailyMetricsQuality
    from ..models.wms_daily_metrics_shipping import WMSDailyMetricsShipping
    from ..models.wms_daily_metrics_world_ref import WMSDailyMetricsWorldRef


T = TypeVar("T", bound="WMSDailyMetrics")


@_attrs_define
class WMSDailyMetrics:
    """Complete WMS daily metrics record for comprehensive warehouse performance tracking and operational analysis

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        metric_id (str): Unique daily metrics identifier Example: wms_daily-metrics_674565c1234567890abcdef.
        warehouse_id (str): Warehouse identifier for metrics recording Example: WH_ATL_001.
        date (datetime.date): Date for metrics recording Example: 2024-11-27.
        world_ref (WMSDailyMetricsWorldRef): World reference information for multi-tenant context
        created_at (datetime.datetime): Timestamp when the daily metrics record was created Example:
            2024-11-27T18:00:00.000Z.
        updated_at (datetime.datetime): Timestamp when the daily metrics record was last updated Example:
            2024-11-27T20:30:00.000Z.
        id (Union[Unset, str]): Formatted document identifier for API responses Example: 507f1f77bcf86cd799439011.
        shift (Union[Unset, str]): Shift identifier for shift-based metrics (optional) Example: DAY_SHIFT_1.
        zone_id (Union[Unset, str]): Zone identifier for zone-based metrics (optional) Example: ZONE_PICK_A.
        inbound (Union[Unset, WMSDailyMetricsInbound]): Inbound receiving operation metrics
        putaway (Union[Unset, WMSDailyMetricsPutaway]): Putaway operation metrics
        picking (Union[Unset, WMSDailyMetricsPicking]): Picking operation metrics
        packing (Union[Unset, WMSDailyMetricsPacking]): Packing operation metrics
        shipping (Union[Unset, WMSDailyMetricsShipping]): Shipping operation metrics
        labor (Union[Unset, WMSDailyMetricsLabor]): Labor and workforce metrics
        inventory (Union[Unset, WMSDailyMetricsInventory]): Inventory management metrics
        quality (Union[Unset, WMSDailyMetricsQuality]): Quality and error tracking metrics
        custom_fields (Union[Unset, WMSDailyMetricsCustomFields]): Additional warehouse-specific metrics and operational
            data Example: {'temperatureControlledZones': 4, 'hazMatHandling': True, 'specialEquipmentUsage': 12.5,
            'sustainabilityMetrics': {'energyUsageKwh': 2450.5, 'wasteReductionPercent': 15.2}}.
    """

    field_id: str
    metric_id: str
    warehouse_id: str
    date: datetime.date
    world_ref: "WMSDailyMetricsWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, str] = UNSET
    shift: Union[Unset, str] = UNSET
    zone_id: Union[Unset, str] = UNSET
    inbound: Union[Unset, "WMSDailyMetricsInbound"] = UNSET
    putaway: Union[Unset, "WMSDailyMetricsPutaway"] = UNSET
    picking: Union[Unset, "WMSDailyMetricsPicking"] = UNSET
    packing: Union[Unset, "WMSDailyMetricsPacking"] = UNSET
    shipping: Union[Unset, "WMSDailyMetricsShipping"] = UNSET
    labor: Union[Unset, "WMSDailyMetricsLabor"] = UNSET
    inventory: Union[Unset, "WMSDailyMetricsInventory"] = UNSET
    quality: Union[Unset, "WMSDailyMetricsQuality"] = UNSET
    custom_fields: Union[Unset, "WMSDailyMetricsCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        metric_id = self.metric_id

        warehouse_id = self.warehouse_id

        date = self.date.isoformat()

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id

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
                "_id": field_id,
                "metricId": metric_id,
                "warehouseId": warehouse_id,
                "date": date,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
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
        from ..models.wms_daily_metrics_custom_fields import WMSDailyMetricsCustomFields
        from ..models.wms_daily_metrics_inbound import WMSDailyMetricsInbound
        from ..models.wms_daily_metrics_inventory import WMSDailyMetricsInventory
        from ..models.wms_daily_metrics_labor import WMSDailyMetricsLabor
        from ..models.wms_daily_metrics_packing import WMSDailyMetricsPacking
        from ..models.wms_daily_metrics_picking import WMSDailyMetricsPicking
        from ..models.wms_daily_metrics_putaway import WMSDailyMetricsPutaway
        from ..models.wms_daily_metrics_quality import WMSDailyMetricsQuality
        from ..models.wms_daily_metrics_shipping import WMSDailyMetricsShipping
        from ..models.wms_daily_metrics_world_ref import WMSDailyMetricsWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        metric_id = d.pop("metricId")

        warehouse_id = d.pop("warehouseId")

        date = isoparse(d.pop("date")).date()

        world_ref = WMSDailyMetricsWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        id = d.pop("id", UNSET)

        shift = d.pop("shift", UNSET)

        zone_id = d.pop("zoneId", UNSET)

        _inbound = d.pop("inbound", UNSET)
        inbound: Union[Unset, WMSDailyMetricsInbound]
        if isinstance(_inbound, Unset):
            inbound = UNSET
        else:
            inbound = WMSDailyMetricsInbound.from_dict(_inbound)

        _putaway = d.pop("putaway", UNSET)
        putaway: Union[Unset, WMSDailyMetricsPutaway]
        if isinstance(_putaway, Unset):
            putaway = UNSET
        else:
            putaway = WMSDailyMetricsPutaway.from_dict(_putaway)

        _picking = d.pop("picking", UNSET)
        picking: Union[Unset, WMSDailyMetricsPicking]
        if isinstance(_picking, Unset):
            picking = UNSET
        else:
            picking = WMSDailyMetricsPicking.from_dict(_picking)

        _packing = d.pop("packing", UNSET)
        packing: Union[Unset, WMSDailyMetricsPacking]
        if isinstance(_packing, Unset):
            packing = UNSET
        else:
            packing = WMSDailyMetricsPacking.from_dict(_packing)

        _shipping = d.pop("shipping", UNSET)
        shipping: Union[Unset, WMSDailyMetricsShipping]
        if isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = WMSDailyMetricsShipping.from_dict(_shipping)

        _labor = d.pop("labor", UNSET)
        labor: Union[Unset, WMSDailyMetricsLabor]
        if isinstance(_labor, Unset):
            labor = UNSET
        else:
            labor = WMSDailyMetricsLabor.from_dict(_labor)

        _inventory = d.pop("inventory", UNSET)
        inventory: Union[Unset, WMSDailyMetricsInventory]
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = WMSDailyMetricsInventory.from_dict(_inventory)

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, WMSDailyMetricsQuality]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = WMSDailyMetricsQuality.from_dict(_quality)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSDailyMetricsCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSDailyMetricsCustomFields.from_dict(_custom_fields)

        wms_daily_metrics = cls(
            field_id=field_id,
            metric_id=metric_id,
            warehouse_id=warehouse_id,
            date=date,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
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

        wms_daily_metrics.additional_properties = d
        return wms_daily_metrics

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
