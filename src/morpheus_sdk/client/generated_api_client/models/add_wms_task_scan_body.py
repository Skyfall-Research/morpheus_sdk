from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_wms_task_scan_body_scan_result import AddWMSTaskScanBodyScanResult
from ..models.add_wms_task_scan_body_scan_type import AddWMSTaskScanBodyScanType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddWMSTaskScanBody")


@_attrs_define
class AddWMSTaskScanBody:
    """
    Attributes:
        scan_type (AddWMSTaskScanBodyScanType): Type of scan being performed Example: PRODUCT.
        scanned_value (Union[Unset, str]): Actual scanned value Example: ABC-XYZ-001.
        expected_value (Union[Unset, str]): Expected value for validation Example: ABC-XYZ-001.
        scan_result (Union[Unset, AddWMSTaskScanBodyScanResult]): Result of scan validation Example: MATCH.
    """

    scan_type: AddWMSTaskScanBodyScanType
    scanned_value: Union[Unset, str] = UNSET
    expected_value: Union[Unset, str] = UNSET
    scan_result: Union[Unset, AddWMSTaskScanBodyScanResult] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scan_type = self.scan_type.value

        scanned_value = self.scanned_value

        expected_value = self.expected_value

        scan_result: Union[Unset, str] = UNSET
        if not isinstance(self.scan_result, Unset):
            scan_result = self.scan_result.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scanType": scan_type,
            }
        )
        if scanned_value is not UNSET:
            field_dict["scannedValue"] = scanned_value
        if expected_value is not UNSET:
            field_dict["expectedValue"] = expected_value
        if scan_result is not UNSET:
            field_dict["scanResult"] = scan_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scan_type = AddWMSTaskScanBodyScanType(d.pop("scanType"))

        scanned_value = d.pop("scannedValue", UNSET)

        expected_value = d.pop("expectedValue", UNSET)

        _scan_result = d.pop("scanResult", UNSET)
        scan_result: Union[Unset, AddWMSTaskScanBodyScanResult]
        if isinstance(_scan_result, Unset):
            scan_result = UNSET
        else:
            scan_result = AddWMSTaskScanBodyScanResult(_scan_result)

        add_wms_task_scan_body = cls(
            scan_type=scan_type,
            scanned_value=scanned_value,
            expected_value=expected_value,
            scan_result=scan_result,
        )

        add_wms_task_scan_body.additional_properties = d
        return add_wms_task_scan_body

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
