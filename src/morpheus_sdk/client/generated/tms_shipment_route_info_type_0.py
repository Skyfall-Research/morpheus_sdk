from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_shipment_route_info_type_0_planned_route_item import TMSShipmentRouteInfoType0PlannedRouteItem


T = TypeVar("T", bound="TMSShipmentRouteInfoType0")


@_attrs_define
class TMSShipmentRouteInfoType0:
    """Route planning and distance information

    Attributes:
        planned_route (Union[Unset, list['TMSShipmentRouteInfoType0PlannedRouteItem']]): Planned stops along the route
        estimated_distance (Union[None, Unset, float]): Estimated total distance in miles Example: 675.5.
        estimated_duration (Union[None, Unset, float]): Estimated total duration in minutes Example: 720.
    """

    planned_route: Union[Unset, list["TMSShipmentRouteInfoType0PlannedRouteItem"]] = UNSET
    estimated_distance: Union[None, Unset, float] = UNSET
    estimated_duration: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        planned_route: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.planned_route, Unset):
            planned_route = []
            for planned_route_item_data in self.planned_route:
                planned_route_item = planned_route_item_data.to_dict()
                planned_route.append(planned_route_item)

        estimated_distance: Union[None, Unset, float]
        if isinstance(self.estimated_distance, Unset):
            estimated_distance = UNSET
        else:
            estimated_distance = self.estimated_distance

        estimated_duration: Union[None, Unset, float]
        if isinstance(self.estimated_duration, Unset):
            estimated_duration = UNSET
        else:
            estimated_duration = self.estimated_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if planned_route is not UNSET:
            field_dict["plannedRoute"] = planned_route
        if estimated_distance is not UNSET:
            field_dict["estimatedDistance"] = estimated_distance
        if estimated_duration is not UNSET:
            field_dict["estimatedDuration"] = estimated_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_shipment_route_info_type_0_planned_route_item import TMSShipmentRouteInfoType0PlannedRouteItem

        d = dict(src_dict)
        planned_route = []
        _planned_route = d.pop("plannedRoute", UNSET)
        for planned_route_item_data in _planned_route or []:
            planned_route_item = TMSShipmentRouteInfoType0PlannedRouteItem.from_dict(planned_route_item_data)

            planned_route.append(planned_route_item)

        def _parse_estimated_distance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        estimated_distance = _parse_estimated_distance(d.pop("estimatedDistance", UNSET))

        def _parse_estimated_duration(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        estimated_duration = _parse_estimated_duration(d.pop("estimatedDuration", UNSET))

        tms_shipment_route_info_type_0 = cls(
            planned_route=planned_route,
            estimated_distance=estimated_distance,
            estimated_duration=estimated_duration,
        )

        tms_shipment_route_info_type_0.additional_properties = d
        return tms_shipment_route_info_type_0

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
