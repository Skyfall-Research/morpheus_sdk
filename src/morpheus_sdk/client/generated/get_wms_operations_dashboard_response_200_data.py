from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_operations_dashboard_response_200_data_fulfillment import (
        GetWMSOperationsDashboardResponse200DataFulfillment,
    )
    from ..models.get_wms_operations_dashboard_response_200_data_inventory import (
        GetWMSOperationsDashboardResponse200DataInventory,
    )
    from ..models.get_wms_operations_dashboard_response_200_data_receiving import (
        GetWMSOperationsDashboardResponse200DataReceiving,
    )
    from ..models.get_wms_operations_dashboard_response_200_data_tasks import (
        GetWMSOperationsDashboardResponse200DataTasks,
    )


T = TypeVar("T", bound="GetWMSOperationsDashboardResponse200Data")


@_attrs_define
class GetWMSOperationsDashboardResponse200Data:
    """
    Attributes:
        inventory (Union[Unset, GetWMSOperationsDashboardResponse200DataInventory]):
        receiving (Union[Unset, GetWMSOperationsDashboardResponse200DataReceiving]):
        fulfillment (Union[Unset, GetWMSOperationsDashboardResponse200DataFulfillment]):
        tasks (Union[Unset, GetWMSOperationsDashboardResponse200DataTasks]):
    """

    inventory: Union[Unset, "GetWMSOperationsDashboardResponse200DataInventory"] = UNSET
    receiving: Union[Unset, "GetWMSOperationsDashboardResponse200DataReceiving"] = UNSET
    fulfillment: Union[Unset, "GetWMSOperationsDashboardResponse200DataFulfillment"] = UNSET
    tasks: Union[Unset, "GetWMSOperationsDashboardResponse200DataTasks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = self.inventory.to_dict()

        receiving: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.receiving, Unset):
            receiving = self.receiving.to_dict()

        fulfillment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fulfillment, Unset):
            fulfillment = self.fulfillment.to_dict()

        tasks: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = self.tasks.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if receiving is not UNSET:
            field_dict["receiving"] = receiving
        if fulfillment is not UNSET:
            field_dict["fulfillment"] = fulfillment
        if tasks is not UNSET:
            field_dict["tasks"] = tasks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_operations_dashboard_response_200_data_fulfillment import (
            GetWMSOperationsDashboardResponse200DataFulfillment,
        )
        from ..models.get_wms_operations_dashboard_response_200_data_inventory import (
            GetWMSOperationsDashboardResponse200DataInventory,
        )
        from ..models.get_wms_operations_dashboard_response_200_data_receiving import (
            GetWMSOperationsDashboardResponse200DataReceiving,
        )
        from ..models.get_wms_operations_dashboard_response_200_data_tasks import (
            GetWMSOperationsDashboardResponse200DataTasks,
        )

        d = dict(src_dict)
        _inventory = d.pop("inventory", UNSET)
        inventory: Union[Unset, GetWMSOperationsDashboardResponse200DataInventory]
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = GetWMSOperationsDashboardResponse200DataInventory.from_dict(_inventory)

        _receiving = d.pop("receiving", UNSET)
        receiving: Union[Unset, GetWMSOperationsDashboardResponse200DataReceiving]
        if isinstance(_receiving, Unset):
            receiving = UNSET
        else:
            receiving = GetWMSOperationsDashboardResponse200DataReceiving.from_dict(_receiving)

        _fulfillment = d.pop("fulfillment", UNSET)
        fulfillment: Union[Unset, GetWMSOperationsDashboardResponse200DataFulfillment]
        if isinstance(_fulfillment, Unset):
            fulfillment = UNSET
        else:
            fulfillment = GetWMSOperationsDashboardResponse200DataFulfillment.from_dict(_fulfillment)

        _tasks = d.pop("tasks", UNSET)
        tasks: Union[Unset, GetWMSOperationsDashboardResponse200DataTasks]
        if isinstance(_tasks, Unset):
            tasks = UNSET
        else:
            tasks = GetWMSOperationsDashboardResponse200DataTasks.from_dict(_tasks)

        get_wms_operations_dashboard_response_200_data = cls(
            inventory=inventory,
            receiving=receiving,
            fulfillment=fulfillment,
            tasks=tasks,
        )

        get_wms_operations_dashboard_response_200_data.additional_properties = d
        return get_wms_operations_dashboard_response_200_data

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
