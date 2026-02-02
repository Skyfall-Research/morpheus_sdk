from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tms_shipment_input_service_level import TMSShipmentInputServiceLevel
from ..models.tms_shipment_input_shipment_type import TMSShipmentInputShipmentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_cargo_input import TMSCargoInput
    from ..models.tms_location_input import TMSLocationInput
    from ..models.tms_shipment_input_dates import TMSShipmentInputDates
    from ..models.tms_shipment_input_references import TMSShipmentInputReferences


T = TypeVar("T", bound="TMSShipmentInput")


@_attrs_define
class TMSShipmentInput:
    """Input data for creating a new TMS shipment

    Attributes:
        shipment_number (str): Business shipment number (required) Example: SHIP-2024-001234.
        origin (TMSLocationInput): Input data for TMS location
        destination (TMSLocationInput): Input data for TMS location
        shipment_type (Union[Unset, TMSShipmentInputShipmentType]): Type of shipment movement Example: OUTBOUND.
        service_level (Union[Unset, TMSShipmentInputServiceLevel]): Service level for delivery Example: STANDARD.
        dates (Union[Unset, TMSShipmentInputDates]): Planned shipment dates
        cargo (Union[Unset, TMSCargoInput]): Input data for TMS cargo
        references (Union[Unset, TMSShipmentInputReferences]): Business reference numbers
        lane_id (Union[Unset, str]):  Example: LANE_ATL_MEM_001.
    """

    shipment_number: str
    origin: "TMSLocationInput"
    destination: "TMSLocationInput"
    shipment_type: Union[Unset, TMSShipmentInputShipmentType] = UNSET
    service_level: Union[Unset, TMSShipmentInputServiceLevel] = UNSET
    dates: Union[Unset, "TMSShipmentInputDates"] = UNSET
    cargo: Union[Unset, "TMSCargoInput"] = UNSET
    references: Union[Unset, "TMSShipmentInputReferences"] = UNSET
    lane_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipment_number = self.shipment_number

        origin = self.origin.to_dict()

        destination = self.destination.to_dict()

        shipment_type: Union[Unset, str] = UNSET
        if not isinstance(self.shipment_type, Unset):
            shipment_type = self.shipment_type.value

        service_level: Union[Unset, str] = UNSET
        if not isinstance(self.service_level, Unset):
            service_level = self.service_level.value

        dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates.to_dict()

        cargo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cargo, Unset):
            cargo = self.cargo.to_dict()

        references: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()

        lane_id = self.lane_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipmentNumber": shipment_number,
                "origin": origin,
                "destination": destination,
            }
        )
        if shipment_type is not UNSET:
            field_dict["shipmentType"] = shipment_type
        if service_level is not UNSET:
            field_dict["serviceLevel"] = service_level
        if dates is not UNSET:
            field_dict["dates"] = dates
        if cargo is not UNSET:
            field_dict["cargo"] = cargo
        if references is not UNSET:
            field_dict["references"] = references
        if lane_id is not UNSET:
            field_dict["laneId"] = lane_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_cargo_input import TMSCargoInput
        from ..models.tms_location_input import TMSLocationInput
        from ..models.tms_shipment_input_dates import TMSShipmentInputDates
        from ..models.tms_shipment_input_references import TMSShipmentInputReferences

        d = dict(src_dict)
        shipment_number = d.pop("shipmentNumber")

        origin = TMSLocationInput.from_dict(d.pop("origin"))

        destination = TMSLocationInput.from_dict(d.pop("destination"))

        _shipment_type = d.pop("shipmentType", UNSET)
        shipment_type: Union[Unset, TMSShipmentInputShipmentType]
        if isinstance(_shipment_type, Unset):
            shipment_type = UNSET
        else:
            shipment_type = TMSShipmentInputShipmentType(_shipment_type)

        _service_level = d.pop("serviceLevel", UNSET)
        service_level: Union[Unset, TMSShipmentInputServiceLevel]
        if isinstance(_service_level, Unset):
            service_level = UNSET
        else:
            service_level = TMSShipmentInputServiceLevel(_service_level)

        _dates = d.pop("dates", UNSET)
        dates: Union[Unset, TMSShipmentInputDates]
        if isinstance(_dates, Unset):
            dates = UNSET
        else:
            dates = TMSShipmentInputDates.from_dict(_dates)

        _cargo = d.pop("cargo", UNSET)
        cargo: Union[Unset, TMSCargoInput]
        if isinstance(_cargo, Unset):
            cargo = UNSET
        else:
            cargo = TMSCargoInput.from_dict(_cargo)

        _references = d.pop("references", UNSET)
        references: Union[Unset, TMSShipmentInputReferences]
        if isinstance(_references, Unset):
            references = UNSET
        else:
            references = TMSShipmentInputReferences.from_dict(_references)

        lane_id = d.pop("laneId", UNSET)

        tms_shipment_input = cls(
            shipment_number=shipment_number,
            origin=origin,
            destination=destination,
            shipment_type=shipment_type,
            service_level=service_level,
            dates=dates,
            cargo=cargo,
            references=references,
            lane_id=lane_id,
        )

        tms_shipment_input.additional_properties = d
        return tms_shipment_input

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
