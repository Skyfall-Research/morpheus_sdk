from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chaos_scenario import ChaosScenario


T = TypeVar("T", bound="ChaosPolicy")


@_attrs_define
class ChaosPolicy:
    """Chaos engineering policy for injecting failures and anomalies

    Attributes:
        enabled (bool): Whether chaos injection is enabled Example: True.
        probability (float): Overall probability (0.0 to 1.0) that chaos will occur Example: 0.1.
        scenarios (list['ChaosScenario']): List of chaos scenarios that can be triggered
        seed (Union[Unset, str]): Optional seed for reproducible chaos Example: test-seed-123.
        persist_corrupted_data (Union[Unset, bool]): When true, persist corrupted data instead of throwing errors
            Default: False.
    """

    enabled: bool
    probability: float
    scenarios: list["ChaosScenario"]
    seed: Union[Unset, str] = UNSET
    persist_corrupted_data: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        probability = self.probability

        scenarios = []
        for scenarios_item_data in self.scenarios:
            scenarios_item = scenarios_item_data.to_dict()
            scenarios.append(scenarios_item)

        seed = self.seed

        persist_corrupted_data = self.persist_corrupted_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "probability": probability,
                "scenarios": scenarios,
            }
        )
        if seed is not UNSET:
            field_dict["seed"] = seed
        if persist_corrupted_data is not UNSET:
            field_dict["persistCorruptedData"] = persist_corrupted_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chaos_scenario import ChaosScenario

        d = dict(src_dict)
        enabled = d.pop("enabled")

        probability = d.pop("probability")

        scenarios = []
        _scenarios = d.pop("scenarios")
        for scenarios_item_data in _scenarios:
            scenarios_item = ChaosScenario.from_dict(scenarios_item_data)

            scenarios.append(scenarios_item)

        seed = d.pop("seed", UNSET)

        persist_corrupted_data = d.pop("persistCorruptedData", UNSET)

        chaos_policy = cls(
            enabled=enabled,
            probability=probability,
            scenarios=scenarios,
            seed=seed,
            persist_corrupted_data=persist_corrupted_data,
        )

        chaos_policy.additional_properties = d
        return chaos_policy

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
