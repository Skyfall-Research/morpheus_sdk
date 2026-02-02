from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_replenishment_metrics_response_200_data_replenishments_by_type_item import (
        GetWMSReplenishmentMetricsResponse200DataReplenishmentsByTypeItem,
    )
    from ..models.get_wms_replenishment_metrics_response_200_data_top_replenished_products_item import (
        GetWMSReplenishmentMetricsResponse200DataTopReplenishedProductsItem,
    )


T = TypeVar("T", bound="GetWMSReplenishmentMetricsResponse200Data")


@_attrs_define
class GetWMSReplenishmentMetricsResponse200Data:
    """
    Attributes:
        total_replenishments (Union[Unset, float]):  Example: 1250.
        pending_replenishments (Union[Unset, float]):  Example: 45.
        completed_replenishments (Union[Unset, float]):  Example: 1180.
        average_completion_time (Union[Unset, float]): Hours Example: 2.5.
        replenishments_by_type (Union[Unset,
            list['GetWMSReplenishmentMetricsResponse200DataReplenishmentsByTypeItem']]):
        top_replenished_products (Union[Unset,
            list['GetWMSReplenishmentMetricsResponse200DataTopReplenishedProductsItem']]):
    """

    total_replenishments: Union[Unset, float] = UNSET
    pending_replenishments: Union[Unset, float] = UNSET
    completed_replenishments: Union[Unset, float] = UNSET
    average_completion_time: Union[Unset, float] = UNSET
    replenishments_by_type: Union[Unset, list["GetWMSReplenishmentMetricsResponse200DataReplenishmentsByTypeItem"]] = (
        UNSET
    )
    top_replenished_products: Union[
        Unset, list["GetWMSReplenishmentMetricsResponse200DataTopReplenishedProductsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_replenishments = self.total_replenishments

        pending_replenishments = self.pending_replenishments

        completed_replenishments = self.completed_replenishments

        average_completion_time = self.average_completion_time

        replenishments_by_type: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.replenishments_by_type, Unset):
            replenishments_by_type = []
            for replenishments_by_type_item_data in self.replenishments_by_type:
                replenishments_by_type_item = replenishments_by_type_item_data.to_dict()
                replenishments_by_type.append(replenishments_by_type_item)

        top_replenished_products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.top_replenished_products, Unset):
            top_replenished_products = []
            for top_replenished_products_item_data in self.top_replenished_products:
                top_replenished_products_item = top_replenished_products_item_data.to_dict()
                top_replenished_products.append(top_replenished_products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_replenishments is not UNSET:
            field_dict["totalReplenishments"] = total_replenishments
        if pending_replenishments is not UNSET:
            field_dict["pendingReplenishments"] = pending_replenishments
        if completed_replenishments is not UNSET:
            field_dict["completedReplenishments"] = completed_replenishments
        if average_completion_time is not UNSET:
            field_dict["averageCompletionTime"] = average_completion_time
        if replenishments_by_type is not UNSET:
            field_dict["replenishmentsByType"] = replenishments_by_type
        if top_replenished_products is not UNSET:
            field_dict["topReplenishedProducts"] = top_replenished_products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_replenishment_metrics_response_200_data_replenishments_by_type_item import (
            GetWMSReplenishmentMetricsResponse200DataReplenishmentsByTypeItem,
        )
        from ..models.get_wms_replenishment_metrics_response_200_data_top_replenished_products_item import (
            GetWMSReplenishmentMetricsResponse200DataTopReplenishedProductsItem,
        )

        d = dict(src_dict)
        total_replenishments = d.pop("totalReplenishments", UNSET)

        pending_replenishments = d.pop("pendingReplenishments", UNSET)

        completed_replenishments = d.pop("completedReplenishments", UNSET)

        average_completion_time = d.pop("averageCompletionTime", UNSET)

        replenishments_by_type = []
        _replenishments_by_type = d.pop("replenishmentsByType", UNSET)
        for replenishments_by_type_item_data in _replenishments_by_type or []:
            replenishments_by_type_item = GetWMSReplenishmentMetricsResponse200DataReplenishmentsByTypeItem.from_dict(
                replenishments_by_type_item_data
            )

            replenishments_by_type.append(replenishments_by_type_item)

        top_replenished_products = []
        _top_replenished_products = d.pop("topReplenishedProducts", UNSET)
        for top_replenished_products_item_data in _top_replenished_products or []:
            top_replenished_products_item = (
                GetWMSReplenishmentMetricsResponse200DataTopReplenishedProductsItem.from_dict(
                    top_replenished_products_item_data
                )
            )

            top_replenished_products.append(top_replenished_products_item)

        get_wms_replenishment_metrics_response_200_data = cls(
            total_replenishments=total_replenishments,
            pending_replenishments=pending_replenishments,
            completed_replenishments=completed_replenishments,
            average_completion_time=average_completion_time,
            replenishments_by_type=replenishments_by_type,
            top_replenished_products=top_replenished_products,
        )

        get_wms_replenishment_metrics_response_200_data.additional_properties = d
        return get_wms_replenishment_metrics_response_200_data

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
