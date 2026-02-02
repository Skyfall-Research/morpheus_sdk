from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chaos_policy import ChaosPolicy
    from ..models.persona_config import PersonaConfig
    from ..models.sampling_strategy_type_0 import SamplingStrategyType0
    from ..models.sampling_strategy_type_1 import SamplingStrategyType1
    from ..models.sampling_strategy_type_2 import SamplingStrategyType2
    from ..models.sampling_strategy_type_3 import SamplingStrategyType3


T = TypeVar("T", bound="UpdateWorldBody")


@_attrs_define
class UpdateWorldBody:
    """
    Attributes:
        name (Union[Unset, str]): Updated name for the world Example: Updated Production Environment.
        description (Union[Unset, str]): Updated description Example: Updated description for the production
            environment.
        is_default (Union[Unset, bool]): Set as default world Example: True.
        layout (Union[Unset, str]): Layout template ID Example: perishables-food-manufacturer.
        real_hours_per_sim_day (Union[Unset, float]): Simulation speed ratio Example: 4.
        sampling_strategy (Union['SamplingStrategyType0', 'SamplingStrategyType1', 'SamplingStrategyType2',
            'SamplingStrategyType3', Unset]): Strategy for sampling capabilities to assign to a world Example: {'type':
            'random', 'count': 10, 'seed': 42}.
        capability_ids (Union[Unset, list[str]]): Direct capability ID assignment Example: ['cap_order_processing',
            'cap_inventory_check'].
        personas (Union[Unset, PersonaConfig]): Configuration for personas allowed to access this world
        chaos (Union[Unset, ChaosPolicy]): Chaos engineering policy for injecting failures and anomalies
        ticket_creation_enabled (Union[Unset, bool]): Enable/disable ITSM ticket creation
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    layout: Union[Unset, str] = UNSET
    real_hours_per_sim_day: Union[Unset, float] = UNSET
    sampling_strategy: Union[
        "SamplingStrategyType0", "SamplingStrategyType1", "SamplingStrategyType2", "SamplingStrategyType3", Unset
    ] = UNSET
    capability_ids: Union[Unset, list[str]] = UNSET
    personas: Union[Unset, "PersonaConfig"] = UNSET
    chaos: Union[Unset, "ChaosPolicy"] = UNSET
    ticket_creation_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sampling_strategy_type_0 import SamplingStrategyType0
        from ..models.sampling_strategy_type_1 import SamplingStrategyType1
        from ..models.sampling_strategy_type_2 import SamplingStrategyType2

        name = self.name

        description = self.description

        is_default = self.is_default

        layout = self.layout

        real_hours_per_sim_day = self.real_hours_per_sim_day

        sampling_strategy: Union[Unset, dict[str, Any]]
        if isinstance(self.sampling_strategy, Unset):
            sampling_strategy = UNSET
        elif isinstance(self.sampling_strategy, SamplingStrategyType0):
            sampling_strategy = self.sampling_strategy.to_dict()
        elif isinstance(self.sampling_strategy, SamplingStrategyType1):
            sampling_strategy = self.sampling_strategy.to_dict()
        elif isinstance(self.sampling_strategy, SamplingStrategyType2):
            sampling_strategy = self.sampling_strategy.to_dict()
        else:
            sampling_strategy = self.sampling_strategy.to_dict()

        capability_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.capability_ids, Unset):
            capability_ids = self.capability_ids

        personas: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.personas, Unset):
            personas = self.personas.to_dict()

        chaos: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chaos, Unset):
            chaos = self.chaos.to_dict()

        ticket_creation_enabled = self.ticket_creation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if layout is not UNSET:
            field_dict["layout"] = layout
        if real_hours_per_sim_day is not UNSET:
            field_dict["realHoursPerSimDay"] = real_hours_per_sim_day
        if sampling_strategy is not UNSET:
            field_dict["samplingStrategy"] = sampling_strategy
        if capability_ids is not UNSET:
            field_dict["capabilityIds"] = capability_ids
        if personas is not UNSET:
            field_dict["personas"] = personas
        if chaos is not UNSET:
            field_dict["chaos"] = chaos
        if ticket_creation_enabled is not UNSET:
            field_dict["ticketCreationEnabled"] = ticket_creation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chaos_policy import ChaosPolicy
        from ..models.persona_config import PersonaConfig
        from ..models.sampling_strategy_type_0 import SamplingStrategyType0
        from ..models.sampling_strategy_type_1 import SamplingStrategyType1
        from ..models.sampling_strategy_type_2 import SamplingStrategyType2
        from ..models.sampling_strategy_type_3 import SamplingStrategyType3

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        is_default = d.pop("is_default", UNSET)

        layout = d.pop("layout", UNSET)

        real_hours_per_sim_day = d.pop("realHoursPerSimDay", UNSET)

        def _parse_sampling_strategy(
            data: object,
        ) -> Union[
            "SamplingStrategyType0", "SamplingStrategyType1", "SamplingStrategyType2", "SamplingStrategyType3", Unset
        ]:
            if isinstance(data, Unset):
                return data
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

        sampling_strategy = _parse_sampling_strategy(d.pop("samplingStrategy", UNSET))

        capability_ids = cast(list[str], d.pop("capabilityIds", UNSET))

        _personas = d.pop("personas", UNSET)
        personas: Union[Unset, PersonaConfig]
        if isinstance(_personas, Unset):
            personas = UNSET
        else:
            personas = PersonaConfig.from_dict(_personas)

        _chaos = d.pop("chaos", UNSET)
        chaos: Union[Unset, ChaosPolicy]
        if isinstance(_chaos, Unset):
            chaos = UNSET
        else:
            chaos = ChaosPolicy.from_dict(_chaos)

        ticket_creation_enabled = d.pop("ticketCreationEnabled", UNSET)

        update_world_body = cls(
            name=name,
            description=description,
            is_default=is_default,
            layout=layout,
            real_hours_per_sim_day=real_hours_per_sim_day,
            sampling_strategy=sampling_strategy,
            capability_ids=capability_ids,
            personas=personas,
            chaos=chaos,
            ticket_creation_enabled=ticket_creation_enabled,
        )

        update_world_body.additional_properties = d
        return update_world_body

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
