from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_edi_dollar_amount_statistics_response_200_data_type_0 import (
        GetEdiDollarAmountStatisticsResponse200DataType0,
    )
    from ..models.get_edi_dollar_amount_statistics_response_200_data_type_1 import (
        GetEdiDollarAmountStatisticsResponse200DataType1,
    )
    from ..models.get_edi_dollar_amount_statistics_response_200_meta import GetEdiDollarAmountStatisticsResponse200Meta


T = TypeVar("T", bound="GetEdiDollarAmountStatisticsResponse200")


@_attrs_define
class GetEdiDollarAmountStatisticsResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        status (Union[Unset, int]):  Example: 200.
        data (Union['GetEdiDollarAmountStatisticsResponse200DataType0',
            'GetEdiDollarAmountStatisticsResponse200DataType1', Unset]): Response varies based on aggregationType parameter
        meta (Union[Unset, GetEdiDollarAmountStatisticsResponse200Meta]):
    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    data: Union[
        "GetEdiDollarAmountStatisticsResponse200DataType0", "GetEdiDollarAmountStatisticsResponse200DataType1", Unset
    ] = UNSET
    meta: Union[Unset, "GetEdiDollarAmountStatisticsResponse200Meta"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_edi_dollar_amount_statistics_response_200_data_type_0 import (
            GetEdiDollarAmountStatisticsResponse200DataType0,
        )

        success = self.success

        status = self.status

        data: Union[Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, GetEdiDollarAmountStatisticsResponse200DataType0):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_edi_dollar_amount_statistics_response_200_data_type_0 import (
            GetEdiDollarAmountStatisticsResponse200DataType0,
        )
        from ..models.get_edi_dollar_amount_statistics_response_200_data_type_1 import (
            GetEdiDollarAmountStatisticsResponse200DataType1,
        )
        from ..models.get_edi_dollar_amount_statistics_response_200_meta import (
            GetEdiDollarAmountStatisticsResponse200Meta,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        def _parse_data(
            data: object,
        ) -> Union[
            "GetEdiDollarAmountStatisticsResponse200DataType0",
            "GetEdiDollarAmountStatisticsResponse200DataType1",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = GetEdiDollarAmountStatisticsResponse200DataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = GetEdiDollarAmountStatisticsResponse200DataType1.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data", UNSET))

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, GetEdiDollarAmountStatisticsResponse200Meta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetEdiDollarAmountStatisticsResponse200Meta.from_dict(_meta)

        get_edi_dollar_amount_statistics_response_200 = cls(
            success=success,
            status=status,
            data=data,
            meta=meta,
        )

        get_edi_dollar_amount_statistics_response_200.additional_properties = d
        return get_edi_dollar_amount_statistics_response_200

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
