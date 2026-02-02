from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_world_capabilities_response_200_data_capabilities_item import (
        GetWorldCapabilitiesResponse200DataCapabilitiesItem,
    )
    from ..models.sampling_strategy_type_0 import SamplingStrategyType0
    from ..models.sampling_strategy_type_1 import SamplingStrategyType1
    from ..models.sampling_strategy_type_2 import SamplingStrategyType2
    from ..models.sampling_strategy_type_3 import SamplingStrategyType3


T = TypeVar("T", bound="GetWorldCapabilitiesResponse200Data")


@_attrs_define
class GetWorldCapabilitiesResponse200Data:
    """
    Attributes:
        world_id (str): World unique identifier Example: 507f1f77bcf86cd799439011.
        world_name (str): World display name Example: Production Environment.
        sampling_strategy (Union['SamplingStrategyType0', 'SamplingStrategyType1', 'SamplingStrategyType2',
            'SamplingStrategyType3']): Strategy for sampling capabilities to assign to a world Example: {'type': 'random',
            'count': 10, 'seed': 42}.
        count (int): Number of assigned capabilities Example: 15.
        capability_ids (list[str]): Array of capability IDs Example: ['cap_order_processing', 'cap_inventory_check',
            'cap_shipment_tracking'].
        capabilities (list['GetWorldCapabilitiesResponse200DataCapabilitiesItem']): Full capability objects
    """

    world_id: str
    world_name: str
    sampling_strategy: Union[
        "SamplingStrategyType0", "SamplingStrategyType1", "SamplingStrategyType2", "SamplingStrategyType3"
    ]
    count: int
    capability_ids: list[str]
    capabilities: list["GetWorldCapabilitiesResponse200DataCapabilitiesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sampling_strategy_type_0 import SamplingStrategyType0
        from ..models.sampling_strategy_type_1 import SamplingStrategyType1
        from ..models.sampling_strategy_type_2 import SamplingStrategyType2

        world_id = self.world_id

        world_name = self.world_name

        sampling_strategy: dict[str, Any]
        if isinstance(self.sampling_strategy, SamplingStrategyType0):
            sampling_strategy = self.sampling_strategy.to_dict()
        elif isinstance(self.sampling_strategy, SamplingStrategyType1):
            sampling_strategy = self.sampling_strategy.to_dict()
        elif isinstance(self.sampling_strategy, SamplingStrategyType2):
            sampling_strategy = self.sampling_strategy.to_dict()
        else:
            sampling_strategy = self.sampling_strategy.to_dict()

        count = self.count

        capability_ids = self.capability_ids

        capabilities = []
        for capabilities_item_data in self.capabilities:
            capabilities_item = capabilities_item_data.to_dict()
            capabilities.append(capabilities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "worldId": world_id,
                "worldName": world_name,
                "samplingStrategy": sampling_strategy,
                "count": count,
                "capabilityIds": capability_ids,
                "capabilities": capabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_world_capabilities_response_200_data_capabilities_item import (
            GetWorldCapabilitiesResponse200DataCapabilitiesItem,
        )
        from ..models.sampling_strategy_type_0 import SamplingStrategyType0
        from ..models.sampling_strategy_type_1 import SamplingStrategyType1
        from ..models.sampling_strategy_type_2 import SamplingStrategyType2
        from ..models.sampling_strategy_type_3 import SamplingStrategyType3

        d = dict(src_dict)
        world_id = d.pop("worldId")

        world_name = d.pop("worldName")

        def _parse_sampling_strategy(
            data: object,
        ) -> Union["SamplingStrategyType0", "SamplingStrategyType1", "SamplingStrategyType2", "SamplingStrategyType3"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sampling_strategy_type_0 = SamplingStrategyType0.from_dict(data)

                return componentsschemas_sampling_strategy_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sampling_strategy_type_1 = SamplingStrategyType1.from_dict(data)

                return componentsschemas_sampling_strategy_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sampling_strategy_type_2 = SamplingStrategyType2.from_dict(data)

                return componentsschemas_sampling_strategy_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_sampling_strategy_type_3 = SamplingStrategyType3.from_dict(data)

            return componentsschemas_sampling_strategy_type_3

        sampling_strategy = _parse_sampling_strategy(d.pop("samplingStrategy"))

        count = d.pop("count")

        capability_ids = cast(list[str], d.pop("capabilityIds"))

        capabilities = []
        _capabilities = d.pop("capabilities")
        for capabilities_item_data in _capabilities:
            capabilities_item = GetWorldCapabilitiesResponse200DataCapabilitiesItem.from_dict(capabilities_item_data)

            capabilities.append(capabilities_item)

        get_world_capabilities_response_200_data = cls(
            world_id=world_id,
            world_name=world_name,
            sampling_strategy=sampling_strategy,
            count=count,
            capability_ids=capability_ids,
            capabilities=capabilities,
        )

        get_world_capabilities_response_200_data.additional_properties = d
        return get_world_capabilities_response_200_data

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
