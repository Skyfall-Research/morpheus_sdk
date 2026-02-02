from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_cycle_count_variance_report_response_200_data_summary import (
        GetWMSCycleCountVarianceReportResponse200DataSummary,
    )
    from ..models.get_wms_cycle_count_variance_report_response_200_data_trends import (
        GetWMSCycleCountVarianceReportResponse200DataTrends,
    )
    from ..models.get_wms_cycle_count_variance_report_response_200_data_variances_by_type_item import (
        GetWMSCycleCountVarianceReportResponse200DataVariancesByTypeItem,
    )
    from ..models.get_wms_cycle_count_variance_report_response_200_data_variances_by_warehouse_item import (
        GetWMSCycleCountVarianceReportResponse200DataVariancesByWarehouseItem,
    )


T = TypeVar("T", bound="GetWMSCycleCountVarianceReportResponse200Data")


@_attrs_define
class GetWMSCycleCountVarianceReportResponse200Data:
    """
    Attributes:
        summary (Union[Unset, GetWMSCycleCountVarianceReportResponse200DataSummary]):
        variances_by_type (Union[Unset, list['GetWMSCycleCountVarianceReportResponse200DataVariancesByTypeItem']]):
        variances_by_warehouse (Union[Unset,
            list['GetWMSCycleCountVarianceReportResponse200DataVariancesByWarehouseItem']]):
        trends (Union[Unset, GetWMSCycleCountVarianceReportResponse200DataTrends]):
    """

    summary: Union[Unset, "GetWMSCycleCountVarianceReportResponse200DataSummary"] = UNSET
    variances_by_type: Union[Unset, list["GetWMSCycleCountVarianceReportResponse200DataVariancesByTypeItem"]] = UNSET
    variances_by_warehouse: Union[
        Unset, list["GetWMSCycleCountVarianceReportResponse200DataVariancesByWarehouseItem"]
    ] = UNSET
    trends: Union[Unset, "GetWMSCycleCountVarianceReportResponse200DataTrends"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        variances_by_type: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.variances_by_type, Unset):
            variances_by_type = []
            for variances_by_type_item_data in self.variances_by_type:
                variances_by_type_item = variances_by_type_item_data.to_dict()
                variances_by_type.append(variances_by_type_item)

        variances_by_warehouse: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.variances_by_warehouse, Unset):
            variances_by_warehouse = []
            for variances_by_warehouse_item_data in self.variances_by_warehouse:
                variances_by_warehouse_item = variances_by_warehouse_item_data.to_dict()
                variances_by_warehouse.append(variances_by_warehouse_item)

        trends: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trends, Unset):
            trends = self.trends.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if variances_by_type is not UNSET:
            field_dict["variancesByType"] = variances_by_type
        if variances_by_warehouse is not UNSET:
            field_dict["variancesByWarehouse"] = variances_by_warehouse
        if trends is not UNSET:
            field_dict["trends"] = trends

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_cycle_count_variance_report_response_200_data_summary import (
            GetWMSCycleCountVarianceReportResponse200DataSummary,
        )
        from ..models.get_wms_cycle_count_variance_report_response_200_data_trends import (
            GetWMSCycleCountVarianceReportResponse200DataTrends,
        )
        from ..models.get_wms_cycle_count_variance_report_response_200_data_variances_by_type_item import (
            GetWMSCycleCountVarianceReportResponse200DataVariancesByTypeItem,
        )
        from ..models.get_wms_cycle_count_variance_report_response_200_data_variances_by_warehouse_item import (
            GetWMSCycleCountVarianceReportResponse200DataVariancesByWarehouseItem,
        )

        d = dict(src_dict)
        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, GetWMSCycleCountVarianceReportResponse200DataSummary]
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = GetWMSCycleCountVarianceReportResponse200DataSummary.from_dict(_summary)

        variances_by_type = []
        _variances_by_type = d.pop("variancesByType", UNSET)
        for variances_by_type_item_data in _variances_by_type or []:
            variances_by_type_item = GetWMSCycleCountVarianceReportResponse200DataVariancesByTypeItem.from_dict(
                variances_by_type_item_data
            )

            variances_by_type.append(variances_by_type_item)

        variances_by_warehouse = []
        _variances_by_warehouse = d.pop("variancesByWarehouse", UNSET)
        for variances_by_warehouse_item_data in _variances_by_warehouse or []:
            variances_by_warehouse_item = (
                GetWMSCycleCountVarianceReportResponse200DataVariancesByWarehouseItem.from_dict(
                    variances_by_warehouse_item_data
                )
            )

            variances_by_warehouse.append(variances_by_warehouse_item)

        _trends = d.pop("trends", UNSET)
        trends: Union[Unset, GetWMSCycleCountVarianceReportResponse200DataTrends]
        if isinstance(_trends, Unset):
            trends = UNSET
        else:
            trends = GetWMSCycleCountVarianceReportResponse200DataTrends.from_dict(_trends)

        get_wms_cycle_count_variance_report_response_200_data = cls(
            summary=summary,
            variances_by_type=variances_by_type,
            variances_by_warehouse=variances_by_warehouse,
            trends=trends,
        )

        get_wms_cycle_count_variance_report_response_200_data.additional_properties = d
        return get_wms_cycle_count_variance_report_response_200_data

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
