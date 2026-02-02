from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_erp_product_body_status import CreateERPProductBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_erp_product_body_cost import CreateERPProductBodyCost
    from ..models.create_erp_product_body_custom_fields import CreateERPProductBodyCustomFields
    from ..models.create_erp_product_body_dimensions import CreateERPProductBodyDimensions
    from ..models.create_erp_product_body_price import CreateERPProductBodyPrice
    from ..models.create_erp_product_body_weight import CreateERPProductBodyWeight


T = TypeVar("T", bound="CreateERPProductBody")


@_attrs_define
class CreateERPProductBody:
    """
    Attributes:
        name (str): Product name (required) Example: Premium Widget.
        product_id (Union[Unset, str]): Optional custom product identifier (auto-generated if not provided) Example:
            PROD_WIDGET_001.
        upc (Union[Unset, str]): Universal Product Code for retail identification Example: 123456789012.
        ean (Union[Unset, str]): European Article Number for international identification Example: 1234567890123.
        description (Union[Unset, str]): Detailed product description Example: High-quality premium widget with enhanced
            features.
        commodity_code (Union[Unset, str]): Commodity classification code for trade and customs Example: 8421.21.0000.
        tax_classification (Union[Unset, str]): Tax classification for accounting and compliance Example: TAXABLE_GOODS.
        unit_of_measure (Union[Unset, str]): Unit of measure for product quantification Default: 'EA'. Example: EA.
        weight (Union[Unset, CreateERPProductBodyWeight]): Product weight specification
        dimensions (Union[Unset, CreateERPProductBodyDimensions]): Product dimensions for shipping and storage
        inventory_tracking (Union[Unset, bool]): Enable inventory tracking for this product Default: True. Example:
            True.
        price (Union[Unset, CreateERPProductBodyPrice]): Product selling price
        cost (Union[Unset, CreateERPProductBodyCost]): Product cost basis for margin calculations
        lead_time_days (Union[Unset, float]): Lead time in days for procurement or manufacturing Example: 14.
        status (Union[Unset, CreateERPProductBodyStatus]): Product lifecycle status Default:
            CreateERPProductBodyStatus.ACTIVE. Example: ACTIVE.
        custom_fields (Union[Unset, CreateERPProductBodyCustomFields]): Additional custom fields for product-specific
            data Example: {'brand': 'Premium Brand', 'category': 'Electronics'}.
    """

    name: str
    product_id: Union[Unset, str] = UNSET
    upc: Union[Unset, str] = UNSET
    ean: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    commodity_code: Union[Unset, str] = UNSET
    tax_classification: Union[Unset, str] = UNSET
    unit_of_measure: Union[Unset, str] = "EA"
    weight: Union[Unset, "CreateERPProductBodyWeight"] = UNSET
    dimensions: Union[Unset, "CreateERPProductBodyDimensions"] = UNSET
    inventory_tracking: Union[Unset, bool] = True
    price: Union[Unset, "CreateERPProductBodyPrice"] = UNSET
    cost: Union[Unset, "CreateERPProductBodyCost"] = UNSET
    lead_time_days: Union[Unset, float] = UNSET
    status: Union[Unset, CreateERPProductBodyStatus] = CreateERPProductBodyStatus.ACTIVE
    custom_fields: Union[Unset, "CreateERPProductBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        product_id = self.product_id

        upc = self.upc

        ean = self.ean

        description = self.description

        commodity_code = self.commodity_code

        tax_classification = self.tax_classification

        unit_of_measure = self.unit_of_measure

        weight: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        dimensions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()

        inventory_tracking = self.inventory_tracking

        price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        cost: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cost, Unset):
            cost = self.cost.to_dict()

        lead_time_days = self.lead_time_days

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if upc is not UNSET:
            field_dict["upc"] = upc
        if ean is not UNSET:
            field_dict["ean"] = ean
        if description is not UNSET:
            field_dict["description"] = description
        if commodity_code is not UNSET:
            field_dict["commodityCode"] = commodity_code
        if tax_classification is not UNSET:
            field_dict["taxClassification"] = tax_classification
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if weight is not UNSET:
            field_dict["weight"] = weight
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if inventory_tracking is not UNSET:
            field_dict["inventoryTracking"] = inventory_tracking
        if price is not UNSET:
            field_dict["price"] = price
        if cost is not UNSET:
            field_dict["cost"] = cost
        if lead_time_days is not UNSET:
            field_dict["leadTimeDays"] = lead_time_days
        if status is not UNSET:
            field_dict["status"] = status
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_erp_product_body_cost import CreateERPProductBodyCost
        from ..models.create_erp_product_body_custom_fields import CreateERPProductBodyCustomFields
        from ..models.create_erp_product_body_dimensions import CreateERPProductBodyDimensions
        from ..models.create_erp_product_body_price import CreateERPProductBodyPrice
        from ..models.create_erp_product_body_weight import CreateERPProductBodyWeight

        d = dict(src_dict)
        name = d.pop("name")

        product_id = d.pop("productId", UNSET)

        upc = d.pop("upc", UNSET)

        ean = d.pop("ean", UNSET)

        description = d.pop("description", UNSET)

        commodity_code = d.pop("commodityCode", UNSET)

        tax_classification = d.pop("taxClassification", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        _weight = d.pop("weight", UNSET)
        weight: Union[Unset, CreateERPProductBodyWeight]
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = CreateERPProductBodyWeight.from_dict(_weight)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: Union[Unset, CreateERPProductBodyDimensions]
        if isinstance(_dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = CreateERPProductBodyDimensions.from_dict(_dimensions)

        inventory_tracking = d.pop("inventoryTracking", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, CreateERPProductBodyPrice]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = CreateERPProductBodyPrice.from_dict(_price)

        _cost = d.pop("cost", UNSET)
        cost: Union[Unset, CreateERPProductBodyCost]
        if isinstance(_cost, Unset):
            cost = UNSET
        else:
            cost = CreateERPProductBodyCost.from_dict(_cost)

        lead_time_days = d.pop("leadTimeDays", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateERPProductBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateERPProductBodyStatus(_status)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateERPProductBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateERPProductBodyCustomFields.from_dict(_custom_fields)

        create_erp_product_body = cls(
            name=name,
            product_id=product_id,
            upc=upc,
            ean=ean,
            description=description,
            commodity_code=commodity_code,
            tax_classification=tax_classification,
            unit_of_measure=unit_of_measure,
            weight=weight,
            dimensions=dimensions,
            inventory_tracking=inventory_tracking,
            price=price,
            cost=cost,
            lead_time_days=lead_time_days,
            status=status,
            custom_fields=custom_fields,
        )

        create_erp_product_body.additional_properties = d
        return create_erp_product_body

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
