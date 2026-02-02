from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_erp_product_body_status import UpdateERPProductBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_erp_product_body_cost import UpdateERPProductBodyCost
    from ..models.update_erp_product_body_custom_fields import UpdateERPProductBodyCustomFields
    from ..models.update_erp_product_body_price import UpdateERPProductBodyPrice


T = TypeVar("T", bound="UpdateERPProductBody")


@_attrs_define
class UpdateERPProductBody:
    """
    Attributes:
        name (Union[Unset, str]): Updated product name Example: Premium Widget Enhanced.
        description (Union[Unset, str]): Updated product description Example: Enhanced premium widget with new features.
        status (Union[Unset, UpdateERPProductBodyStatus]): Updated product status Example: DISCONTINUED.
        price (Union[Unset, UpdateERPProductBodyPrice]): Updated product selling price
        cost (Union[Unset, UpdateERPProductBodyCost]): Updated product cost
        inventory_tracking (Union[Unset, bool]): Updated inventory tracking setting
        lead_time_days (Union[Unset, float]): Updated lead time Example: 21.
        custom_fields (Union[Unset, UpdateERPProductBodyCustomFields]): Updated custom fields
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, UpdateERPProductBodyStatus] = UNSET
    price: Union[Unset, "UpdateERPProductBodyPrice"] = UNSET
    cost: Union[Unset, "UpdateERPProductBodyCost"] = UNSET
    inventory_tracking: Union[Unset, bool] = UNSET
    lead_time_days: Union[Unset, float] = UNSET
    custom_fields: Union[Unset, "UpdateERPProductBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        cost: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cost, Unset):
            cost = self.cost.to_dict()

        inventory_tracking = self.inventory_tracking

        lead_time_days = self.lead_time_days

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if price is not UNSET:
            field_dict["price"] = price
        if cost is not UNSET:
            field_dict["cost"] = cost
        if inventory_tracking is not UNSET:
            field_dict["inventoryTracking"] = inventory_tracking
        if lead_time_days is not UNSET:
            field_dict["leadTimeDays"] = lead_time_days
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_erp_product_body_cost import UpdateERPProductBodyCost
        from ..models.update_erp_product_body_custom_fields import UpdateERPProductBodyCustomFields
        from ..models.update_erp_product_body_price import UpdateERPProductBodyPrice

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateERPProductBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateERPProductBodyStatus(_status)

        _price = d.pop("price", UNSET)
        price: Union[Unset, UpdateERPProductBodyPrice]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = UpdateERPProductBodyPrice.from_dict(_price)

        _cost = d.pop("cost", UNSET)
        cost: Union[Unset, UpdateERPProductBodyCost]
        if isinstance(_cost, Unset):
            cost = UNSET
        else:
            cost = UpdateERPProductBodyCost.from_dict(_cost)

        inventory_tracking = d.pop("inventoryTracking", UNSET)

        lead_time_days = d.pop("leadTimeDays", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, UpdateERPProductBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = UpdateERPProductBodyCustomFields.from_dict(_custom_fields)

        update_erp_product_body = cls(
            name=name,
            description=description,
            status=status,
            price=price,
            cost=cost,
            inventory_tracking=inventory_tracking,
            lead_time_days=lead_time_days,
            custom_fields=custom_fields,
        )

        update_erp_product_body.additional_properties = d
        return update_erp_product_body

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
