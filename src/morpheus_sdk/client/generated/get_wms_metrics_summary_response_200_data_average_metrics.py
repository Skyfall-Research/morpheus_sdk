from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_metrics_summary_response_200_data_average_metrics_inbound import (
        GetWMSMetricsSummaryResponse200DataAverageMetricsInbound,
    )
    from ..models.get_wms_metrics_summary_response_200_data_average_metrics_inventory import (
        GetWMSMetricsSummaryResponse200DataAverageMetricsInventory,
    )
    from ..models.get_wms_metrics_summary_response_200_data_average_metrics_packing import (
        GetWMSMetricsSummaryResponse200DataAverageMetricsPacking,
    )
    from ..models.get_wms_metrics_summary_response_200_data_average_metrics_picking import (
        GetWMSMetricsSummaryResponse200DataAverageMetricsPicking,
    )


T = TypeVar("T", bound="GetWMSMetricsSummaryResponse200DataAverageMetrics")


@_attrs_define
class GetWMSMetricsSummaryResponse200DataAverageMetrics:
    """Average metrics across all categories

    Attributes:
        inbound (Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetricsInbound]):
        picking (Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetricsPicking]):
        packing (Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetricsPacking]):
        inventory (Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetricsInventory]):
    """

    inbound: Union[Unset, "GetWMSMetricsSummaryResponse200DataAverageMetricsInbound"] = UNSET
    picking: Union[Unset, "GetWMSMetricsSummaryResponse200DataAverageMetricsPicking"] = UNSET
    packing: Union[Unset, "GetWMSMetricsSummaryResponse200DataAverageMetricsPacking"] = UNSET
    inventory: Union[Unset, "GetWMSMetricsSummaryResponse200DataAverageMetricsInventory"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inbound, Unset):
            inbound = self.inbound.to_dict()

        picking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.picking, Unset):
            picking = self.picking.to_dict()

        packing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.packing, Unset):
            packing = self.packing.to_dict()

        inventory: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = self.inventory.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound is not UNSET:
            field_dict["inbound"] = inbound
        if picking is not UNSET:
            field_dict["picking"] = picking
        if packing is not UNSET:
            field_dict["packing"] = packing
        if inventory is not UNSET:
            field_dict["inventory"] = inventory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_metrics_summary_response_200_data_average_metrics_inbound import (
            GetWMSMetricsSummaryResponse200DataAverageMetricsInbound,
        )
        from ..models.get_wms_metrics_summary_response_200_data_average_metrics_inventory import (
            GetWMSMetricsSummaryResponse200DataAverageMetricsInventory,
        )
        from ..models.get_wms_metrics_summary_response_200_data_average_metrics_packing import (
            GetWMSMetricsSummaryResponse200DataAverageMetricsPacking,
        )
        from ..models.get_wms_metrics_summary_response_200_data_average_metrics_picking import (
            GetWMSMetricsSummaryResponse200DataAverageMetricsPicking,
        )

        d = dict(src_dict)
        _inbound = d.pop("inbound", UNSET)
        inbound: Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetricsInbound]
        if isinstance(_inbound, Unset):
            inbound = UNSET
        else:
            inbound = GetWMSMetricsSummaryResponse200DataAverageMetricsInbound.from_dict(_inbound)

        _picking = d.pop("picking", UNSET)
        picking: Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetricsPicking]
        if isinstance(_picking, Unset):
            picking = UNSET
        else:
            picking = GetWMSMetricsSummaryResponse200DataAverageMetricsPicking.from_dict(_picking)

        _packing = d.pop("packing", UNSET)
        packing: Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetricsPacking]
        if isinstance(_packing, Unset):
            packing = UNSET
        else:
            packing = GetWMSMetricsSummaryResponse200DataAverageMetricsPacking.from_dict(_packing)

        _inventory = d.pop("inventory", UNSET)
        inventory: Union[Unset, GetWMSMetricsSummaryResponse200DataAverageMetricsInventory]
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = GetWMSMetricsSummaryResponse200DataAverageMetricsInventory.from_dict(_inventory)

        get_wms_metrics_summary_response_200_data_average_metrics = cls(
            inbound=inbound,
            picking=picking,
            packing=packing,
            inventory=inventory,
        )

        get_wms_metrics_summary_response_200_data_average_metrics.additional_properties = d
        return get_wms_metrics_summary_response_200_data_average_metrics

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
