import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_tms_edi_214_update_body_raw_edi_data import ProcessTMSEdi214UpdateBodyRawEdiData


T = TypeVar("T", bound="ProcessTMSEdi214UpdateBody")


@_attrs_define
class ProcessTMSEdi214UpdateBody:
    """
    Attributes:
        status (str): Mapped shipment status from EDI Example: IN_TRANSIT.
        raw_edi_data (ProcessTMSEdi214UpdateBodyRawEdiData): Complete raw EDI 214 message data Example: {'ISA': 'ISA*00*
            *00*          *ZZ*CARRIER    *ZZ*SHIPPER    *241126*1430*U*00401*000000001*0*T*>', 'GS':
            'GS*QM*CARRIER*SHIPPER*20241126*1430*1*X*004010', 'ST': 'ST*214*0001', 'B10':
            'B10*SHIP-2024-001234*PRO123456789', 'segments': '...'}.
        location_code (Union[Unset, str]): EDI location code Example: MEM.
        city (Union[Unset, str]): Location city from EDI Example: Memphis.
        state (Union[Unset, str]): Location state from EDI Example: TN.
        timestamp (Union[Unset, datetime.datetime]): EDI message timestamp Example: 2024-11-26T14:30:00.000Z.
        equipment_id (Union[Unset, str]): Truck or container identifier Example: TRK12345.
        estimated_delivery_date (Union[Unset, datetime.datetime]): Updated estimated delivery date Example:
            2024-11-29T17:00:00.000Z.
    """

    status: str
    raw_edi_data: "ProcessTMSEdi214UpdateBodyRawEdiData"
    location_code: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    equipment_id: Union[Unset, str] = UNSET
    estimated_delivery_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        raw_edi_data = self.raw_edi_data.to_dict()

        location_code = self.location_code

        city = self.city

        state = self.state

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        equipment_id = self.equipment_id

        estimated_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_delivery_date, Unset):
            estimated_delivery_date = self.estimated_delivery_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "rawEdiData": raw_edi_data,
            }
        )
        if location_code is not UNSET:
            field_dict["locationCode"] = location_code
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if equipment_id is not UNSET:
            field_dict["equipmentId"] = equipment_id
        if estimated_delivery_date is not UNSET:
            field_dict["estimatedDeliveryDate"] = estimated_delivery_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_tms_edi_214_update_body_raw_edi_data import ProcessTMSEdi214UpdateBodyRawEdiData

        d = dict(src_dict)
        status = d.pop("status")

        raw_edi_data = ProcessTMSEdi214UpdateBodyRawEdiData.from_dict(d.pop("rawEdiData"))

        location_code = d.pop("locationCode", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        equipment_id = d.pop("equipmentId", UNSET)

        _estimated_delivery_date = d.pop("estimatedDeliveryDate", UNSET)
        estimated_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_delivery_date, Unset):
            estimated_delivery_date = UNSET
        else:
            estimated_delivery_date = isoparse(_estimated_delivery_date)

        process_tms_edi_214_update_body = cls(
            status=status,
            raw_edi_data=raw_edi_data,
            location_code=location_code,
            city=city,
            state=state,
            timestamp=timestamp,
            equipment_id=equipment_id,
            estimated_delivery_date=estimated_delivery_date,
        )

        process_tms_edi_214_update_body.additional_properties = d
        return process_tms_edi_214_update_body

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
