from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_cycle_count_body_scope_abc_classification import CreateWMSCycleCountBodyScopeAbcClassification
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSCycleCountBodyScope")


@_attrs_define
class CreateWMSCycleCountBodyScope:
    """
    Attributes:
        zone_id (Union[Unset, str]): Specific zone to include in count Example: ZONE_PICK_A.
        bin_ids (Union[Unset, list[str]]): Specific bins to include in count Example: ['BIN_ATL_A01_001',
            'BIN_ATL_A01_002'].
        product_ids (Union[Unset, list[str]]): Specific products to count across warehouse Example: ['PROD_12345',
            'PROD_67890'].
        abc_classification (Union[Unset, CreateWMSCycleCountBodyScopeAbcClassification]): ABC classification for
            targeted counting Example: A.
    """

    zone_id: Union[Unset, str] = UNSET
    bin_ids: Union[Unset, list[str]] = UNSET
    product_ids: Union[Unset, list[str]] = UNSET
    abc_classification: Union[Unset, CreateWMSCycleCountBodyScopeAbcClassification] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_id = self.zone_id

        bin_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.bin_ids, Unset):
            bin_ids = self.bin_ids

        product_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids

        abc_classification: Union[Unset, str] = UNSET
        if not isinstance(self.abc_classification, Unset):
            abc_classification = self.abc_classification.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if bin_ids is not UNSET:
            field_dict["binIds"] = bin_ids
        if product_ids is not UNSET:
            field_dict["productIds"] = product_ids
        if abc_classification is not UNSET:
            field_dict["abcClassification"] = abc_classification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        zone_id = d.pop("zoneId", UNSET)

        bin_ids = cast(list[str], d.pop("binIds", UNSET))

        product_ids = cast(list[str], d.pop("productIds", UNSET))

        _abc_classification = d.pop("abcClassification", UNSET)
        abc_classification: Union[Unset, CreateWMSCycleCountBodyScopeAbcClassification]
        if isinstance(_abc_classification, Unset):
            abc_classification = UNSET
        else:
            abc_classification = CreateWMSCycleCountBodyScopeAbcClassification(_abc_classification)

        create_wms_cycle_count_body_scope = cls(
            zone_id=zone_id,
            bin_ids=bin_ids,
            product_ids=product_ids,
            abc_classification=abc_classification,
        )

        create_wms_cycle_count_body_scope.additional_properties = d
        return create_wms_cycle_count_body_scope

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
