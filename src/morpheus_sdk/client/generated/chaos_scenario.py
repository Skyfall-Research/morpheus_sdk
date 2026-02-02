from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chaos_scenario_type import ChaosScenarioType

if TYPE_CHECKING:
    from ..models.chaos_scenario_config import ChaosScenarioConfig


T = TypeVar("T", bound="ChaosScenario")


@_attrs_define
class ChaosScenario:
    """A specific chaos scenario that can be triggered

    Attributes:
        type_ (ChaosScenarioType): Type of chaos to inject
        weight (float): Relative weight for scenario selection (higher = more likely) Example: 1.
        description (str): Human-readable description of this scenario Example: Simulate missing required fields in API
            response.
        config (ChaosScenarioConfig): Scenario-specific configuration
    """

    type_: ChaosScenarioType
    weight: float
    description: str
    config: "ChaosScenarioConfig"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        weight = self.weight

        description = self.description

        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "weight": weight,
                "description": description,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chaos_scenario_config import ChaosScenarioConfig

        d = dict(src_dict)
        type_ = ChaosScenarioType(d.pop("type"))

        weight = d.pop("weight")

        description = d.pop("description")

        config = ChaosScenarioConfig.from_dict(d.pop("config"))

        chaos_scenario = cls(
            type_=type_,
            weight=weight,
            description=description,
            config=config,
        )

        chaos_scenario.additional_properties = d
        return chaos_scenario

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
