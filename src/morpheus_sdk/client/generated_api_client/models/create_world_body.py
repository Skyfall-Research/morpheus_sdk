from collections.abc import Mapping
from typing import Any, TYPE_CHECKING, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorldBody")


if TYPE_CHECKING:
    from ..models.chaos_config import ChaosConfig
@_attrs_define
class CreateWorldBody:
    """
    Attributes:
        name (str): Unique name for the world environment Example: Production Environment.
        layout (str): ID of the layout template to seed the world with Example: perishables-food-manufacturer.
        url (Union[Unset, str]): URL slug for the world (auto-generated from name if not provided) Example: production-
            environment.
        description (Union[Unset, str]): Detailed description of the world's purpose Example: Main production
            environment for live customer operations.
        is_default (Union[Unset, bool]): Whether this should be the default world Default: False. Example: True.
        api_key (Union[Unset, str]): API key for world authentication (optional) Example: prod_api_key_123456.
        api_secret (Union[Unset, str]): API secret for world authentication (optional) Example: prod_secret_789012.
        mpc_company (Union[Unset, str]): MPC company identifier (optional) Example: company_skyfall_main.
        real_hours_per_sim_day (Union[Unset, float]): Number of real-world hours that equal one simulation day Default:
            2.0. Example: 2.
    """

    name: str
    layout: str
    url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = False
    api_key: Union[Unset, str] = UNSET
    api_secret: Union[Unset, str] = UNSET
    mpc_company: Union[Unset, str] = UNSET
    real_hours_per_sim_day: Union[Unset, float] = 2.0
    chaos: Union[Unset, "ChaosConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        layout = self.layout

        url = self.url

        description = self.description

        is_default = self.is_default

        api_key = self.api_key

        api_secret = self.api_secret

        mpc_company = self.mpc_company

        real_hours_per_sim_day = self.real_hours_per_sim_day

        chaos: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chaos, Unset):
            chaos = self.chaos.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "layout": layout,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if api_secret is not UNSET:
            field_dict["apiSecret"] = api_secret
        if mpc_company is not UNSET:
            field_dict["mpcCompany"] = mpc_company
        if real_hours_per_sim_day is not UNSET:
            field_dict["realHoursPerSimDay"] = real_hours_per_sim_day
        if chaos is not UNSET:
            field_dict["chaos"] = chaos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chaos_config import ChaosConfig

        d = dict(src_dict)
        name = d.pop("name")

        layout = d.pop("layout")

        url = d.pop("url", UNSET)

        description = d.pop("description", UNSET)

        is_default = d.pop("is_default", UNSET)

        api_key = d.pop("apiKey", UNSET)

        api_secret = d.pop("apiSecret", UNSET)

        mpc_company = d.pop("mpcCompany", UNSET)

        real_hours_per_sim_day = d.pop("realHoursPerSimDay", UNSET)

        _chaos = d.pop("chaos", UNSET)
        chaos: Union[Unset, ChaosConfig]
        if isinstance(_chaos, Unset):
            chaos = UNSET
        else:
            chaos = ChaosConfig.from_dict(_chaos)

        create_world_body = cls(
            name=name,
            layout=layout,
            url=url,
            description=description,
            is_default=is_default,
            api_key=api_key,
            api_secret=api_secret,
            mpc_company=mpc_company,
            real_hours_per_sim_day=real_hours_per_sim_day,
            chaos=chaos,
        )

        create_world_body.additional_properties = d
        return create_world_body

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
