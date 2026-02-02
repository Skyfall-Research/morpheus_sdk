import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chaos_policy import ChaosPolicy
    from ..models.persona_config import PersonaConfig
    from ..models.sampling_strategy_type_0 import SamplingStrategyType0
    from ..models.sampling_strategy_type_1 import SamplingStrategyType1
    from ..models.sampling_strategy_type_2 import SamplingStrategyType2
    from ..models.sampling_strategy_type_3 import SamplingStrategyType3


T = TypeVar("T", bound="World")


@_attrs_define
class World:
    """A world environment representing an isolated business context with its own data and configurations

    Attributes:
        field_id (str): Unique identifier for the world Example: 507f1f77bcf86cd799439011.
        name (str): Human-readable name for the world environment Example: Production Environment.
        url (str): URL slug derived from the world name Example: production-environment.
        is_default (bool): Whether this world is the default environment Default: False. Example: True.
        created_at (datetime.datetime): Timestamp when the world was created Example: 2024-01-15T09:00:00.000Z.
        updated_at (datetime.datetime): Timestamp when the world was last modified Example: 2024-01-15T10:30:00.000Z.
        api_key (Union[Unset, str]): API key for authenticating with this world's services Example: prod_api_key_123456.
        api_secret (Union[Unset, str]): API secret for secure authentication Example: prod_secret_789012.
        description (Union[Unset, str]): Detailed description of the world's purpose and usage Example: Main production
            environment for live customer operations and critical business processes.
        layout (Union[Unset, str]): ID of the layout template used to seed this world Example: perishables-food-
            manufacturer.
        mpc_company (Union[Unset, str]): Identifier of the main MPC company associated with this world Example:
            company_skyfall_main_123.
        real_hours_per_sim_day (Union[Unset, float]): Number of real-world hours that equal one simulation day Default:
            2.0. Example: 2.
        sampling_strategy (Union['SamplingStrategyType0', 'SamplingStrategyType1', 'SamplingStrategyType2',
            'SamplingStrategyType3', Unset]): Strategy for sampling capabilities to assign to a world Example: {'type':
            'random', 'count': 10, 'seed': 42}.
        capability_ids (Union[Unset, list[str]]): Array of capability IDs assigned to this world Example:
            ['cap_order_processing', 'cap_inventory_check'].
        personas (Union[Unset, PersonaConfig]): Configuration for personas allowed to access this world
        chaos (Union[Unset, ChaosPolicy]): Chaos engineering policy for injecting failures and anomalies
        ticket_creation_enabled (Union[Unset, bool]): Whether ITSM ticket creation is enabled for this world Default:
            True. Example: True.
    """

    field_id: str
    name: str
    url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_default: bool = False
    api_key: Union[Unset, str] = UNSET
    api_secret: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    layout: Union[Unset, str] = UNSET
    mpc_company: Union[Unset, str] = UNSET
    real_hours_per_sim_day: Union[Unset, float] = 2.0
    sampling_strategy: Union[
        "SamplingStrategyType0", "SamplingStrategyType1", "SamplingStrategyType2", "SamplingStrategyType3", Unset
    ] = UNSET
    capability_ids: Union[Unset, list[str]] = UNSET
    personas: Union[Unset, "PersonaConfig"] = UNSET
    chaos: Union[Unset, "ChaosPolicy"] = UNSET
    ticket_creation_enabled: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sampling_strategy_type_0 import SamplingStrategyType0
        from ..models.sampling_strategy_type_1 import SamplingStrategyType1
        from ..models.sampling_strategy_type_2 import SamplingStrategyType2

        field_id = self.field_id

        name = self.name

        url = self.url

        is_default = self.is_default

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        api_key = self.api_key

        api_secret = self.api_secret

        description = self.description

        layout = self.layout

        mpc_company = self.mpc_company

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
        field_dict.update(
            {
                "_id": field_id,
                "name": name,
                "url": url,
                "is_default": is_default,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if api_secret is not UNSET:
            field_dict["apiSecret"] = api_secret
        if description is not UNSET:
            field_dict["description"] = description
        if layout is not UNSET:
            field_dict["layout"] = layout
        if mpc_company is not UNSET:
            field_dict["mpcCompany"] = mpc_company
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
        field_id = d.pop("_id")

        name = d.pop("name")

        url = d.pop("url")

        is_default = d.pop("is_default")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        api_key = d.pop("apiKey", UNSET)

        api_secret = d.pop("apiSecret", UNSET)

        description = d.pop("description", UNSET)

        layout = d.pop("layout", UNSET)

        mpc_company = d.pop("mpcCompany", UNSET)

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

        world = cls(
            field_id=field_id,
            name=name,
            url=url,
            is_default=is_default,
            created_at=created_at,
            updated_at=updated_at,
            api_key=api_key,
            api_secret=api_secret,
            description=description,
            layout=layout,
            mpc_company=mpc_company,
            real_hours_per_sim_day=real_hours_per_sim_day,
            sampling_strategy=sampling_strategy,
            capability_ids=capability_ids,
            personas=personas,
            chaos=chaos,
            ticket_creation_enabled=ticket_creation_enabled,
        )

        world.additional_properties = d
        return world

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
