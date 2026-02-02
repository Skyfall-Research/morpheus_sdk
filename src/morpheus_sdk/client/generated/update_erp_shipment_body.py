import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_erp_shipment_body_status import UpdateERPShipmentBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_erp_shipment_body_carrier import UpdateERPShipmentBodyCarrier
    from ..models.update_erp_shipment_body_custom_fields import UpdateERPShipmentBodyCustomFields
    from ..models.update_erp_shipment_body_packaging import UpdateERPShipmentBodyPackaging


T = TypeVar("T", bound="UpdateERPShipmentBody")


@_attrs_define
class UpdateERPShipmentBody:
    """
    Attributes:
        tracking_number (Union[Unset, str]): Updated tracking number Example: 1Z999AA9876543210.
        estimated_arrival (Union[Unset, datetime.date]): Updated estimated arrival date Example: 2024-01-20.
        actual_arrival (Union[Unset, datetime.date]): Actual arrival date Example: 2024-01-19.
        status (Union[Unset, UpdateERPShipmentBodyStatus]): Updated shipment status Example: IN_TRANSIT.
        carrier (Union[Unset, UpdateERPShipmentBodyCarrier]): Updated carrier information
        packaging (Union[Unset, UpdateERPShipmentBodyPackaging]): Updated packaging information
        custom_fields (Union[Unset, UpdateERPShipmentBodyCustomFields]): Updated custom fields
    """

    tracking_number: Union[Unset, str] = UNSET
    estimated_arrival: Union[Unset, datetime.date] = UNSET
    actual_arrival: Union[Unset, datetime.date] = UNSET
    status: Union[Unset, UpdateERPShipmentBodyStatus] = UNSET
    carrier: Union[Unset, "UpdateERPShipmentBodyCarrier"] = UNSET
    packaging: Union[Unset, "UpdateERPShipmentBodyPackaging"] = UNSET
    custom_fields: Union[Unset, "UpdateERPShipmentBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracking_number = self.tracking_number

        estimated_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_arrival, Unset):
            estimated_arrival = self.estimated_arrival.isoformat()

        actual_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.actual_arrival, Unset):
            actual_arrival = self.actual_arrival.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        carrier: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.carrier, Unset):
            carrier = self.carrier.to_dict()

        packaging: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.packaging, Unset):
            packaging = self.packaging.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if estimated_arrival is not UNSET:
            field_dict["estimatedArrival"] = estimated_arrival
        if actual_arrival is not UNSET:
            field_dict["actualArrival"] = actual_arrival
        if status is not UNSET:
            field_dict["status"] = status
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if packaging is not UNSET:
            field_dict["packaging"] = packaging
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_erp_shipment_body_carrier import UpdateERPShipmentBodyCarrier
        from ..models.update_erp_shipment_body_custom_fields import UpdateERPShipmentBodyCustomFields
        from ..models.update_erp_shipment_body_packaging import UpdateERPShipmentBodyPackaging

        d = dict(src_dict)
        tracking_number = d.pop("trackingNumber", UNSET)

        _estimated_arrival = d.pop("estimatedArrival", UNSET)
        estimated_arrival: Union[Unset, datetime.date]
        if isinstance(_estimated_arrival, Unset):
            estimated_arrival = UNSET
        else:
            estimated_arrival = isoparse(_estimated_arrival).date()

        _actual_arrival = d.pop("actualArrival", UNSET)
        actual_arrival: Union[Unset, datetime.date]
        if isinstance(_actual_arrival, Unset):
            actual_arrival = UNSET
        else:
            actual_arrival = isoparse(_actual_arrival).date()

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateERPShipmentBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateERPShipmentBodyStatus(_status)

        _carrier = d.pop("carrier", UNSET)
        carrier: Union[Unset, UpdateERPShipmentBodyCarrier]
        if isinstance(_carrier, Unset):
            carrier = UNSET
        else:
            carrier = UpdateERPShipmentBodyCarrier.from_dict(_carrier)

        _packaging = d.pop("packaging", UNSET)
        packaging: Union[Unset, UpdateERPShipmentBodyPackaging]
        if isinstance(_packaging, Unset):
            packaging = UNSET
        else:
            packaging = UpdateERPShipmentBodyPackaging.from_dict(_packaging)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, UpdateERPShipmentBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = UpdateERPShipmentBodyCustomFields.from_dict(_custom_fields)

        update_erp_shipment_body = cls(
            tracking_number=tracking_number,
            estimated_arrival=estimated_arrival,
            actual_arrival=actual_arrival,
            status=status,
            carrier=carrier,
            packaging=packaging,
            custom_fields=custom_fields,
        )

        update_erp_shipment_body.additional_properties = d
        return update_erp_shipment_body

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
