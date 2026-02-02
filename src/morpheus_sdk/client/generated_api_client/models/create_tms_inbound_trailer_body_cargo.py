from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_tms_inbound_trailer_body_cargo_trailer_type import CreateTMSInboundTrailerBodyCargoTrailerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTMSInboundTrailerBodyCargo")


@_attrs_define
class CreateTMSInboundTrailerBodyCargo:
    """
    Attributes:
        purchase_orders (Union[Unset, list[str]]): Associated purchase order numbers Example: ['PO-2024-001',
            'PO-2024-002'].
        expected_pallets (Union[Unset, int]): Expected number of pallets Example: 20.
        trailer_type (Union[Unset, CreateTMSInboundTrailerBodyCargoTrailerType]): Type of trailer equipment Example:
            DRY_VAN.
        seal_number (Union[Unset, str]): Trailer seal number for security Example: SEAL-789456.
    """

    purchase_orders: Union[Unset, list[str]] = UNSET
    expected_pallets: Union[Unset, int] = UNSET
    trailer_type: Union[Unset, CreateTMSInboundTrailerBodyCargoTrailerType] = UNSET
    seal_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purchase_orders: Union[Unset, list[str]] = UNSET
        if not isinstance(self.purchase_orders, Unset):
            purchase_orders = self.purchase_orders

        expected_pallets = self.expected_pallets

        trailer_type: Union[Unset, str] = UNSET
        if not isinstance(self.trailer_type, Unset):
            trailer_type = self.trailer_type.value

        seal_number = self.seal_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchase_orders is not UNSET:
            field_dict["purchaseOrders"] = purchase_orders
        if expected_pallets is not UNSET:
            field_dict["expectedPallets"] = expected_pallets
        if trailer_type is not UNSET:
            field_dict["trailerType"] = trailer_type
        if seal_number is not UNSET:
            field_dict["sealNumber"] = seal_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        purchase_orders = cast(list[str], d.pop("purchaseOrders", UNSET))

        expected_pallets = d.pop("expectedPallets", UNSET)

        _trailer_type = d.pop("trailerType", UNSET)
        trailer_type: Union[Unset, CreateTMSInboundTrailerBodyCargoTrailerType]
        if isinstance(_trailer_type, Unset):
            trailer_type = UNSET
        else:
            trailer_type = CreateTMSInboundTrailerBodyCargoTrailerType(_trailer_type)

        seal_number = d.pop("sealNumber", UNSET)

        create_tms_inbound_trailer_body_cargo = cls(
            purchase_orders=purchase_orders,
            expected_pallets=expected_pallets,
            trailer_type=trailer_type,
            seal_number=seal_number,
        )

        create_tms_inbound_trailer_body_cargo.additional_properties = d
        return create_tms_inbound_trailer_body_cargo

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
