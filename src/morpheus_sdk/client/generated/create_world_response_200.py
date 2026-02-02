from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_world_response_200_capabilities import CreateWorldResponse200Capabilities
    from ..models.create_world_response_200_seed_result_type_0 import CreateWorldResponse200SeedResultType0
    from ..models.erp_company import ERPCompany
    from ..models.erp_product import ERPProduct
    from ..models.world import World


T = TypeVar("T", bound="CreateWorldResponse200")


@_attrs_define
class CreateWorldResponse200:
    """
    Attributes:
        world (Union[Unset, World]): A world environment representing an isolated business context with its own data and
            configurations
        main_company (Union[Unset, ERPCompany]): Complete ERP company entity with comprehensive business information and
            operational configuration
        npc_companies (Union[Unset, list['ERPCompany']]): Array of NPC companies created
        products_for_mpc (Union[Unset, list['ERPProduct']]): Array of products created for MPC
        seed_result (Union['CreateWorldResponse200SeedResultType0', None, Unset]): Result of the world seeding process
            (if layout seeder was run)
        capabilities (Union[Unset, CreateWorldResponse200Capabilities]): Capability sampling results (only present when
            samplingStrategy is provided)
    """

    world: Union[Unset, "World"] = UNSET
    main_company: Union[Unset, "ERPCompany"] = UNSET
    npc_companies: Union[Unset, list["ERPCompany"]] = UNSET
    products_for_mpc: Union[Unset, list["ERPProduct"]] = UNSET
    seed_result: Union["CreateWorldResponse200SeedResultType0", None, Unset] = UNSET
    capabilities: Union[Unset, "CreateWorldResponse200Capabilities"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_world_response_200_seed_result_type_0 import CreateWorldResponse200SeedResultType0

        world: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.world, Unset):
            world = self.world.to_dict()

        main_company: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.main_company, Unset):
            main_company = self.main_company.to_dict()

        npc_companies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.npc_companies, Unset):
            npc_companies = []
            for npc_companies_item_data in self.npc_companies:
                npc_companies_item = npc_companies_item_data.to_dict()
                npc_companies.append(npc_companies_item)

        products_for_mpc: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products_for_mpc, Unset):
            products_for_mpc = []
            for products_for_mpc_item_data in self.products_for_mpc:
                products_for_mpc_item = products_for_mpc_item_data.to_dict()
                products_for_mpc.append(products_for_mpc_item)

        seed_result: Union[None, Unset, dict[str, Any]]
        if isinstance(self.seed_result, Unset):
            seed_result = UNSET
        elif isinstance(self.seed_result, CreateWorldResponse200SeedResultType0):
            seed_result = self.seed_result.to_dict()
        else:
            seed_result = self.seed_result

        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if world is not UNSET:
            field_dict["world"] = world
        if main_company is not UNSET:
            field_dict["mainCompany"] = main_company
        if npc_companies is not UNSET:
            field_dict["npcCompanies"] = npc_companies
        if products_for_mpc is not UNSET:
            field_dict["productsForMpc"] = products_for_mpc
        if seed_result is not UNSET:
            field_dict["seedResult"] = seed_result
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_world_response_200_capabilities import CreateWorldResponse200Capabilities
        from ..models.create_world_response_200_seed_result_type_0 import CreateWorldResponse200SeedResultType0
        from ..models.erp_company import ERPCompany
        from ..models.erp_product import ERPProduct
        from ..models.world import World

        d = dict(src_dict)
        _world = d.pop("world", UNSET)
        world: Union[Unset, World]
        if isinstance(_world, Unset):
            world = UNSET
        else:
            world = World.from_dict(_world)

        _main_company = d.pop("mainCompany", UNSET)
        main_company: Union[Unset, ERPCompany]
        if isinstance(_main_company, Unset):
            main_company = UNSET
        else:
            main_company = ERPCompany.from_dict(_main_company)

        npc_companies = []
        _npc_companies = d.pop("npcCompanies", UNSET)
        for npc_companies_item_data in _npc_companies or []:
            npc_companies_item = ERPCompany.from_dict(npc_companies_item_data)

            npc_companies.append(npc_companies_item)

        products_for_mpc = []
        _products_for_mpc = d.pop("productsForMpc", UNSET)
        for products_for_mpc_item_data in _products_for_mpc or []:
            products_for_mpc_item = ERPProduct.from_dict(products_for_mpc_item_data)

            products_for_mpc.append(products_for_mpc_item)

        def _parse_seed_result(data: object) -> Union["CreateWorldResponse200SeedResultType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                seed_result_type_0 = CreateWorldResponse200SeedResultType0.from_dict(data)

                return seed_result_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CreateWorldResponse200SeedResultType0", None, Unset], data)

        seed_result = _parse_seed_result(d.pop("seedResult", UNSET))

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, CreateWorldResponse200Capabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = CreateWorldResponse200Capabilities.from_dict(_capabilities)

        create_world_response_200 = cls(
            world=world,
            main_company=main_company,
            npc_companies=npc_companies,
            products_for_mpc=products_for_mpc,
            seed_result=seed_result,
            capabilities=capabilities,
        )

        create_world_response_200.additional_properties = d
        return create_world_response_200

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
