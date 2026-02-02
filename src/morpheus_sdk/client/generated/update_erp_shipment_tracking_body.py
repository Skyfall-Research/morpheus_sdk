from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_erp_shipment_tracking_body_carrier import UpdateERPShipmentTrackingBodyCarrier


T = TypeVar("T", bound="UpdateERPShipmentTrackingBody")


@_attrs_define
class UpdateERPShipmentTrackingBody:
    """
    Attributes:
        carrier (UpdateERPShipmentTrackingBodyCarrier): Carrier information (required)
        tracking_number (Union[Unset, str]): Carrier tracking number Example: 1Z999AA1234567890.
    """

    carrier: "UpdateERPShipmentTrackingBodyCarrier"
    tracking_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier = self.carrier.to_dict()

        tracking_number = self.tracking_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "carrier": carrier,
            }
        )
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_erp_shipment_tracking_body_carrier import UpdateERPShipmentTrackingBodyCarrier

        d = dict(src_dict)
        carrier = UpdateERPShipmentTrackingBodyCarrier.from_dict(d.pop("carrier"))

        tracking_number = d.pop("trackingNumber", UNSET)

        update_erp_shipment_tracking_body = cls(
            carrier=carrier,
            tracking_number=tracking_number,
        )

        update_erp_shipment_tracking_body.additional_properties = d
        return update_erp_shipment_tracking_body

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
