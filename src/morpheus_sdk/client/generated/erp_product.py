import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.erp_product_status import ERPProductStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_product_cost import ERPProductCost
    from ..models.erp_product_custom_fields import ERPProductCustomFields
    from ..models.erp_product_dimensions import ERPProductDimensions
    from ..models.erp_product_price import ERPProductPrice
    from ..models.erp_product_weight import ERPProductWeight
    from ..models.erp_product_world_ref import ERPProductWorldRef


T = TypeVar("T", bound="ERPProduct")


@_attrs_define
class ERPProduct:
    """Complete ERP product entity with comprehensive product information and operational configuration

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        world_ref (ERPProductWorldRef): Reference to the world this product belongs to
        product_id (str): Unique product identifier within the world (auto-generated if not provided) Example:
            PROD_507f1f77bcf86cd799439012.
        name (str): Product name Example: Premium Widget.
        status (ERPProductStatus): Product lifecycle status Default: ERPProductStatus.ACTIVE. Example: ACTIVE.
        upc (Union[Unset, str]): Universal Product Code for retail identification Example: 123456789012.
        ean (Union[Unset, str]): European Article Number for international identification Example: 1234567890123.
        description (Union[Unset, str]): Detailed product description Example: High-quality premium widget with enhanced
            features for professional use.
        commodity_code (Union[Unset, str]): Commodity classification code for trade and customs Example: 8421.21.0000.
        tax_classification (Union[Unset, str]): Tax classification for accounting and compliance Example: TAXABLE_GOODS.
        unit_of_measure (Union[Unset, str]): Unit of measure for product quantification Default: 'EA'. Example: EA.
        weight (Union[Unset, ERPProductWeight]): Product weight specification
        dimensions (Union[Unset, ERPProductDimensions]): Product dimensions for shipping and storage calculations
        inventory_tracking (Union[Unset, bool]): Enable inventory tracking for this product Default: True. Example:
            True.
        price (Union[Unset, ERPProductPrice]): Product selling price for sales operations
        cost (Union[Unset, ERPProductCost]): Product cost basis for margin calculations and financial reporting
        lead_time_days (Union[Unset, float]): Lead time in days for procurement or manufacturing Example: 14.
        custom_fields (Union[Unset, ERPProductCustomFields]): Additional custom fields for product-specific data and
            metadata Example: {'brand': 'Premium Brand', 'category': 'Electronics', 'manufacturer': 'ACME Corp', 'warranty':
            '2 years'}.
        created_at (Union[Unset, datetime.datetime]): Product record creation timestamp Example:
            2024-01-15T10:25:30.123Z.
        updated_at (Union[Unset, datetime.datetime]): Product record last update timestamp Example:
            2024-01-15T14:30:45.678Z.
    """

    field_id: str
    world_ref: "ERPProductWorldRef"
    product_id: str
    name: str
    status: ERPProductStatus = ERPProductStatus.ACTIVE
    upc: Union[Unset, str] = UNSET
    ean: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    commodity_code: Union[Unset, str] = UNSET
    tax_classification: Union[Unset, str] = UNSET
    unit_of_measure: Union[Unset, str] = "EA"
    weight: Union[Unset, "ERPProductWeight"] = UNSET
    dimensions: Union[Unset, "ERPProductDimensions"] = UNSET
    inventory_tracking: Union[Unset, bool] = True
    price: Union[Unset, "ERPProductPrice"] = UNSET
    cost: Union[Unset, "ERPProductCost"] = UNSET
    lead_time_days: Union[Unset, float] = UNSET
    custom_fields: Union[Unset, "ERPProductCustomFields"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_ref = self.world_ref.to_dict()

        product_id = self.product_id

        name = self.name

        status = self.status.value

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

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "worldRef": world_ref,
                "productId": product_id,
                "name": name,
                "status": status,
            }
        )
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
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_product_cost import ERPProductCost
        from ..models.erp_product_custom_fields import ERPProductCustomFields
        from ..models.erp_product_dimensions import ERPProductDimensions
        from ..models.erp_product_price import ERPProductPrice
        from ..models.erp_product_weight import ERPProductWeight
        from ..models.erp_product_world_ref import ERPProductWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_ref = ERPProductWorldRef.from_dict(d.pop("worldRef"))

        product_id = d.pop("productId")

        name = d.pop("name")

        status = ERPProductStatus(d.pop("status"))

        upc = d.pop("upc", UNSET)

        ean = d.pop("ean", UNSET)

        description = d.pop("description", UNSET)

        commodity_code = d.pop("commodityCode", UNSET)

        tax_classification = d.pop("taxClassification", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        _weight = d.pop("weight", UNSET)
        weight: Union[Unset, ERPProductWeight]
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = ERPProductWeight.from_dict(_weight)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: Union[Unset, ERPProductDimensions]
        if isinstance(_dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = ERPProductDimensions.from_dict(_dimensions)

        inventory_tracking = d.pop("inventoryTracking", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, ERPProductPrice]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = ERPProductPrice.from_dict(_price)

        _cost = d.pop("cost", UNSET)
        cost: Union[Unset, ERPProductCost]
        if isinstance(_cost, Unset):
            cost = UNSET
        else:
            cost = ERPProductCost.from_dict(_cost)

        lead_time_days = d.pop("leadTimeDays", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, ERPProductCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ERPProductCustomFields.from_dict(_custom_fields)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        erp_product = cls(
            field_id=field_id,
            world_ref=world_ref,
            product_id=product_id,
            name=name,
            status=status,
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
            custom_fields=custom_fields,
            created_at=created_at,
            updated_at=updated_at,
        )

        erp_product.additional_properties = d
        return erp_product

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
