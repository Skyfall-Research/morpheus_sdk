from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_tms_shipment_response_201_meta import CreateTMSShipmentResponse201Meta
    from ..models.tms_shipment import TMSShipment


T = TypeVar("T", bound="CreateTMSShipmentResponse201")


@_attrs_define
class CreateTMSShipmentResponse201:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        status (Union[Unset, int]):  Example: 201.
        data (Union[Unset, TMSShipment]): Complete TMS shipment record with all tracking and logistics information
        meta (Union[Unset, CreateTMSShipmentResponse201Meta]):
    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    data: Union[Unset, "TMSShipment"] = UNSET
    meta: Union[Unset, "CreateTMSShipmentResponse201Meta"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_tms_shipment_response_201_meta import CreateTMSShipmentResponse201Meta
        from ..models.tms_shipment import TMSShipment

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, TMSShipment]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TMSShipment.from_dict(_data)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, CreateTMSShipmentResponse201Meta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = CreateTMSShipmentResponse201Meta.from_dict(_meta)

        create_tms_shipment_response_201 = cls(
            success=success,
            status=status,
            data=data,
            meta=meta,
        )

        create_tms_shipment_response_201.additional_properties = d
        return create_tms_shipment_response_201

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
