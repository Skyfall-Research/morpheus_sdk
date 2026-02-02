from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_upsert_erp_shipments_body_shipments_item import BulkUpsertERPShipmentsBodyShipmentsItem


T = TypeVar("T", bound="BulkUpsertERPShipmentsBody")


@_attrs_define
class BulkUpsertERPShipmentsBody:
    """
    Attributes:
        shipments (list['BulkUpsertERPShipmentsBodyShipmentsItem']): Array of shipments to process
    """

    shipments: list["BulkUpsertERPShipmentsBodyShipmentsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipments = []
        for shipments_item_data in self.shipments:
            shipments_item = shipments_item_data.to_dict()
            shipments.append(shipments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipments": shipments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_upsert_erp_shipments_body_shipments_item import BulkUpsertERPShipmentsBodyShipmentsItem

        d = dict(src_dict)
        shipments = []
        _shipments = d.pop("shipments")
        for shipments_item_data in _shipments:
            shipments_item = BulkUpsertERPShipmentsBodyShipmentsItem.from_dict(shipments_item_data)

            shipments.append(shipments_item)

        bulk_upsert_erp_shipments_body = cls(
            shipments=shipments,
        )

        bulk_upsert_erp_shipments_body.additional_properties = d
        return bulk_upsert_erp_shipments_body

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
