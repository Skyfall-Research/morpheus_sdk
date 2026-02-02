from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_shipment import TMSShipment
    from ..models.tms_shipment_status_event import TMSShipmentStatusEvent


T = TypeVar("T", bound="GetTMSShipmentByIdResponse200Data")


@_attrs_define
class GetTMSShipmentByIdResponse200Data:
    """
    Attributes:
        shipment (Union[Unset, TMSShipment]): Complete TMS shipment record with all tracking and logistics information
        events (Union[Unset, list['TMSShipmentStatusEvent']]): Status events ordered by timestamp (most recent first)
    """

    shipment: Union[Unset, "TMSShipment"] = UNSET
    events: Union[Unset, list["TMSShipmentStatusEvent"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipment, Unset):
            shipment = self.shipment.to_dict()

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment is not UNSET:
            field_dict["shipment"] = shipment
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_shipment import TMSShipment
        from ..models.tms_shipment_status_event import TMSShipmentStatusEvent

        d = dict(src_dict)
        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, TMSShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = TMSShipment.from_dict(_shipment)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = TMSShipmentStatusEvent.from_dict(events_item_data)

            events.append(events_item)

        get_tms_shipment_by_id_response_200_data = cls(
            shipment=shipment,
            events=events,
        )

        get_tms_shipment_by_id_response_200_data.additional_properties = d
        return get_tms_shipment_by_id_response_200_data

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
