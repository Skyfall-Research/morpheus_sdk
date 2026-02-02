from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wms_outbound_shipment_carrier_mode import WMSOutboundShipmentCarrierMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundShipmentCarrier")


@_attrs_define
class WMSOutboundShipmentCarrier:
    """Carrier information for transportation

    Attributes:
        name (Union[Unset, str]): Carrier company name (used in repository queries as carrier.name) Example: UPS.
        scac (Union[Unset, str]): Standard Carrier Alpha Code Example: UPSN.
        mode (Union[Unset, WMSOutboundShipmentCarrierMode]): Transportation mode Example: PARCEL.
    """

    name: Union[Unset, str] = UNSET
    scac: Union[Unset, str] = UNSET
    mode: Union[Unset, WMSOutboundShipmentCarrierMode] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scac = self.scac

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if scac is not UNSET:
            field_dict["scac"] = scac
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        scac = d.pop("scac", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, WMSOutboundShipmentCarrierMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = WMSOutboundShipmentCarrierMode(_mode)

        wms_outbound_shipment_carrier = cls(
            name=name,
            scac=scac,
            mode=mode,
        )

        wms_outbound_shipment_carrier.additional_properties = d
        return wms_outbound_shipment_carrier

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
