from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_wms_daily_metrics_body_custom_fields import UpdateWMSDailyMetricsBodyCustomFields
    from ..models.update_wms_daily_metrics_body_inbound import UpdateWMSDailyMetricsBodyInbound
    from ..models.update_wms_daily_metrics_body_picking import UpdateWMSDailyMetricsBodyPicking
    from ..models.update_wms_daily_metrics_body_quality import UpdateWMSDailyMetricsBodyQuality


T = TypeVar("T", bound="UpdateWMSDailyMetricsBody")


@_attrs_define
class UpdateWMSDailyMetricsBody:
    """Partial metrics data for updating specific fields

    Attributes:
        inbound (Union[Unset, UpdateWMSDailyMetricsBodyInbound]): Updated inbound receiving metrics
        picking (Union[Unset, UpdateWMSDailyMetricsBodyPicking]): Updated picking operation metrics
        quality (Union[Unset, UpdateWMSDailyMetricsBodyQuality]): Updated quality metrics
        custom_fields (Union[Unset, UpdateWMSDailyMetricsBodyCustomFields]): Updated custom warehouse-specific metrics
            Example: {'temperatureControlledZones': 5, 'specialEquipmentUsage': 15.2}.
    """

    inbound: Union[Unset, "UpdateWMSDailyMetricsBodyInbound"] = UNSET
    picking: Union[Unset, "UpdateWMSDailyMetricsBodyPicking"] = UNSET
    quality: Union[Unset, "UpdateWMSDailyMetricsBodyQuality"] = UNSET
    custom_fields: Union[Unset, "UpdateWMSDailyMetricsBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inbound, Unset):
            inbound = self.inbound.to_dict()

        picking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.picking, Unset):
            picking = self.picking.to_dict()

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound is not UNSET:
            field_dict["inbound"] = inbound
        if picking is not UNSET:
            field_dict["picking"] = picking
        if quality is not UNSET:
            field_dict["quality"] = quality
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_wms_daily_metrics_body_custom_fields import UpdateWMSDailyMetricsBodyCustomFields
        from ..models.update_wms_daily_metrics_body_inbound import UpdateWMSDailyMetricsBodyInbound
        from ..models.update_wms_daily_metrics_body_picking import UpdateWMSDailyMetricsBodyPicking
        from ..models.update_wms_daily_metrics_body_quality import UpdateWMSDailyMetricsBodyQuality

        d = dict(src_dict)
        _inbound = d.pop("inbound", UNSET)
        inbound: Union[Unset, UpdateWMSDailyMetricsBodyInbound]
        if isinstance(_inbound, Unset):
            inbound = UNSET
        else:
            inbound = UpdateWMSDailyMetricsBodyInbound.from_dict(_inbound)

        _picking = d.pop("picking", UNSET)
        picking: Union[Unset, UpdateWMSDailyMetricsBodyPicking]
        if isinstance(_picking, Unset):
            picking = UNSET
        else:
            picking = UpdateWMSDailyMetricsBodyPicking.from_dict(_picking)

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, UpdateWMSDailyMetricsBodyQuality]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = UpdateWMSDailyMetricsBodyQuality.from_dict(_quality)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, UpdateWMSDailyMetricsBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = UpdateWMSDailyMetricsBodyCustomFields.from_dict(_custom_fields)

        update_wms_daily_metrics_body = cls(
            inbound=inbound,
            picking=picking,
            quality=quality,
            custom_fields=custom_fields,
        )

        update_wms_daily_metrics_body.additional_properties = d
        return update_wms_daily_metrics_body

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
