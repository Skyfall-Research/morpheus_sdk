import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tms_shipment_service_level import TMSShipmentServiceLevel
from ..models.tms_shipment_shipment_type import TMSShipmentShipmentType
from ..models.tms_shipment_status import TMSShipmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_cargo import TMSCargo
    from ..models.tms_delay import TMSDelay
    from ..models.tms_location import TMSLocation
    from ..models.tms_shipment_carrier_info import TMSShipmentCarrierInfo
    from ..models.tms_shipment_costs_type_0 import TMSShipmentCostsType0
    from ..models.tms_shipment_current_location_type_0 import TMSShipmentCurrentLocationType0
    from ..models.tms_shipment_dates import TMSShipmentDates
    from ..models.tms_shipment_external_events_item import TMSShipmentExternalEventsItem
    from ..models.tms_shipment_references_type_0 import TMSShipmentReferencesType0
    from ..models.tms_shipment_route_info_type_0 import TMSShipmentRouteInfoType0


T = TypeVar("T", bound="TMSShipment")


@_attrs_define
class TMSShipment:
    """Complete TMS shipment record with all tracking and logistics information

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        id (str): Formatted ID for client use (same as _id) Example: 507f1f77bcf86cd799439011.
        shipment_id (str): Unique shipment identifier Example: TMS_SHIP_674565c1234567890abcdef.
        shipment_number (str): Business shipment number Example: SHIP-2024-001234.
        status (TMSShipmentStatus): Current shipment status Example: IN_TRANSIT.
        origin (TMSLocation): Complete location information for TMS operations
        destination (TMSLocation): Complete location information for TMS operations
        shipment_type (Union[Unset, TMSShipmentShipmentType]): Type of shipment movement Example: OUTBOUND.
        service_level (Union[Unset, TMSShipmentServiceLevel]): Service level for delivery Example: STANDARD.
        carrier_info (Union[Unset, TMSShipmentCarrierInfo]): Carrier and transportation details
        dates (Union[Unset, TMSShipmentDates]): Important shipment dates
        cargo (Union[Unset, TMSCargo]): Cargo and freight information
        costs (Union['TMSShipmentCostsType0', None, Unset]): Shipment cost breakdown (optional, may be null if costs not
            yet calculated)
        current_location (Union['TMSShipmentCurrentLocationType0', None, Unset]): Current shipment location (null until
            tracking begins)
        delays (Union[Unset, list['TMSDelay']]): Recorded delays for this shipment
        route_info (Union['TMSShipmentRouteInfoType0', None, Unset]): Route planning and distance information
        external_events (Union[Unset, list['TMSShipmentExternalEventsItem']]): External events related to this shipment
            from external systems
        references (Union['TMSShipmentReferencesType0', None, Unset]): Business reference numbers (optional)
        created_at (Union[Unset, datetime.datetime]):  Example: 2024-11-26T08:00:00.000Z.
        updated_at (Union[Unset, datetime.datetime]):  Example: 2024-11-26T14:30:00.000Z.
    """

    field_id: str
    id: str
    shipment_id: str
    shipment_number: str
    status: TMSShipmentStatus
    origin: "TMSLocation"
    destination: "TMSLocation"
    shipment_type: Union[Unset, TMSShipmentShipmentType] = UNSET
    service_level: Union[Unset, TMSShipmentServiceLevel] = UNSET
    carrier_info: Union[Unset, "TMSShipmentCarrierInfo"] = UNSET
    dates: Union[Unset, "TMSShipmentDates"] = UNSET
    cargo: Union[Unset, "TMSCargo"] = UNSET
    costs: Union["TMSShipmentCostsType0", None, Unset] = UNSET
    current_location: Union["TMSShipmentCurrentLocationType0", None, Unset] = UNSET
    delays: Union[Unset, list["TMSDelay"]] = UNSET
    route_info: Union["TMSShipmentRouteInfoType0", None, Unset] = UNSET
    external_events: Union[Unset, list["TMSShipmentExternalEventsItem"]] = UNSET
    references: Union["TMSShipmentReferencesType0", None, Unset] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tms_shipment_costs_type_0 import TMSShipmentCostsType0
        from ..models.tms_shipment_current_location_type_0 import TMSShipmentCurrentLocationType0
        from ..models.tms_shipment_references_type_0 import TMSShipmentReferencesType0
        from ..models.tms_shipment_route_info_type_0 import TMSShipmentRouteInfoType0

        field_id = self.field_id

        id = self.id

        shipment_id = self.shipment_id

        shipment_number = self.shipment_number

        status = self.status.value

        origin = self.origin.to_dict()

        destination = self.destination.to_dict()

        shipment_type: Union[Unset, str] = UNSET
        if not isinstance(self.shipment_type, Unset):
            shipment_type = self.shipment_type.value

        service_level: Union[Unset, str] = UNSET
        if not isinstance(self.service_level, Unset):
            service_level = self.service_level.value

        carrier_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.carrier_info, Unset):
            carrier_info = self.carrier_info.to_dict()

        dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates.to_dict()

        cargo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cargo, Unset):
            cargo = self.cargo.to_dict()

        costs: Union[None, Unset, dict[str, Any]]
        if isinstance(self.costs, Unset):
            costs = UNSET
        elif isinstance(self.costs, TMSShipmentCostsType0):
            costs = self.costs.to_dict()
        else:
            costs = self.costs

        current_location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.current_location, Unset):
            current_location = UNSET
        elif isinstance(self.current_location, TMSShipmentCurrentLocationType0):
            current_location = self.current_location.to_dict()
        else:
            current_location = self.current_location

        delays: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.delays, Unset):
            delays = []
            for delays_item_data in self.delays:
                delays_item = delays_item_data.to_dict()
                delays.append(delays_item)

        route_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.route_info, Unset):
            route_info = UNSET
        elif isinstance(self.route_info, TMSShipmentRouteInfoType0):
            route_info = self.route_info.to_dict()
        else:
            route_info = self.route_info

        external_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_events, Unset):
            external_events = []
            for external_events_item_data in self.external_events:
                external_events_item = external_events_item_data.to_dict()
                external_events.append(external_events_item)

        references: Union[None, Unset, dict[str, Any]]
        if isinstance(self.references, Unset):
            references = UNSET
        elif isinstance(self.references, TMSShipmentReferencesType0):
            references = self.references.to_dict()
        else:
            references = self.references

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "id": id,
                "shipmentId": shipment_id,
                "shipmentNumber": shipment_number,
                "status": status,
                "origin": origin,
                "destination": destination,
            }
        )
        if shipment_type is not UNSET:
            field_dict["shipmentType"] = shipment_type
        if service_level is not UNSET:
            field_dict["serviceLevel"] = service_level
        if carrier_info is not UNSET:
            field_dict["carrierInfo"] = carrier_info
        if dates is not UNSET:
            field_dict["dates"] = dates
        if cargo is not UNSET:
            field_dict["cargo"] = cargo
        if costs is not UNSET:
            field_dict["costs"] = costs
        if current_location is not UNSET:
            field_dict["currentLocation"] = current_location
        if delays is not UNSET:
            field_dict["delays"] = delays
        if route_info is not UNSET:
            field_dict["routeInfo"] = route_info
        if external_events is not UNSET:
            field_dict["externalEvents"] = external_events
        if references is not UNSET:
            field_dict["references"] = references
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_cargo import TMSCargo
        from ..models.tms_delay import TMSDelay
        from ..models.tms_location import TMSLocation
        from ..models.tms_shipment_carrier_info import TMSShipmentCarrierInfo
        from ..models.tms_shipment_costs_type_0 import TMSShipmentCostsType0
        from ..models.tms_shipment_current_location_type_0 import TMSShipmentCurrentLocationType0
        from ..models.tms_shipment_dates import TMSShipmentDates
        from ..models.tms_shipment_external_events_item import TMSShipmentExternalEventsItem
        from ..models.tms_shipment_references_type_0 import TMSShipmentReferencesType0
        from ..models.tms_shipment_route_info_type_0 import TMSShipmentRouteInfoType0

        d = dict(src_dict)
        field_id = d.pop("_id")

        id = d.pop("id")

        shipment_id = d.pop("shipmentId")

        shipment_number = d.pop("shipmentNumber")

        status = TMSShipmentStatus(d.pop("status"))

        origin = TMSLocation.from_dict(d.pop("origin"))

        destination = TMSLocation.from_dict(d.pop("destination"))

        _shipment_type = d.pop("shipmentType", UNSET)
        shipment_type: Union[Unset, TMSShipmentShipmentType]
        if isinstance(_shipment_type, Unset):
            shipment_type = UNSET
        else:
            shipment_type = TMSShipmentShipmentType(_shipment_type)

        _service_level = d.pop("serviceLevel", UNSET)
        service_level: Union[Unset, TMSShipmentServiceLevel]
        if isinstance(_service_level, Unset):
            service_level = UNSET
        else:
            service_level = TMSShipmentServiceLevel(_service_level)

        _carrier_info = d.pop("carrierInfo", UNSET)
        carrier_info: Union[Unset, TMSShipmentCarrierInfo]
        if isinstance(_carrier_info, Unset):
            carrier_info = UNSET
        else:
            carrier_info = TMSShipmentCarrierInfo.from_dict(_carrier_info)

        _dates = d.pop("dates", UNSET)
        dates: Union[Unset, TMSShipmentDates]
        if isinstance(_dates, Unset):
            dates = UNSET
        else:
            dates = TMSShipmentDates.from_dict(_dates)

        _cargo = d.pop("cargo", UNSET)
        cargo: Union[Unset, TMSCargo]
        if isinstance(_cargo, Unset):
            cargo = UNSET
        else:
            cargo = TMSCargo.from_dict(_cargo)

        def _parse_costs(data: object) -> Union["TMSShipmentCostsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                costs_type_0 = TMSShipmentCostsType0.from_dict(data)

                return costs_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TMSShipmentCostsType0", None, Unset], data)

        costs = _parse_costs(d.pop("costs", UNSET))

        def _parse_current_location(data: object) -> Union["TMSShipmentCurrentLocationType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_location_type_0 = TMSShipmentCurrentLocationType0.from_dict(data)

                return current_location_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TMSShipmentCurrentLocationType0", None, Unset], data)

        current_location = _parse_current_location(d.pop("currentLocation", UNSET))

        delays = []
        _delays = d.pop("delays", UNSET)
        for delays_item_data in _delays or []:
            delays_item = TMSDelay.from_dict(delays_item_data)

            delays.append(delays_item)

        def _parse_route_info(data: object) -> Union["TMSShipmentRouteInfoType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                route_info_type_0 = TMSShipmentRouteInfoType0.from_dict(data)

                return route_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TMSShipmentRouteInfoType0", None, Unset], data)

        route_info = _parse_route_info(d.pop("routeInfo", UNSET))

        external_events = []
        _external_events = d.pop("externalEvents", UNSET)
        for external_events_item_data in _external_events or []:
            external_events_item = TMSShipmentExternalEventsItem.from_dict(external_events_item_data)

            external_events.append(external_events_item)

        def _parse_references(data: object) -> Union["TMSShipmentReferencesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                references_type_0 = TMSShipmentReferencesType0.from_dict(data)

                return references_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TMSShipmentReferencesType0", None, Unset], data)

        references = _parse_references(d.pop("references", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        tms_shipment = cls(
            field_id=field_id,
            id=id,
            shipment_id=shipment_id,
            shipment_number=shipment_number,
            status=status,
            origin=origin,
            destination=destination,
            shipment_type=shipment_type,
            service_level=service_level,
            carrier_info=carrier_info,
            dates=dates,
            cargo=cargo,
            costs=costs,
            current_location=current_location,
            delays=delays,
            route_info=route_info,
            external_events=external_events,
            references=references,
            created_at=created_at,
            updated_at=updated_at,
        )

        tms_shipment.additional_properties = d
        return tms_shipment

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
