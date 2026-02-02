import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_task_scans_item_scan_result import WMSTaskScansItemScanResult
from ..models.wms_task_scans_item_scan_type import WMSTaskScansItemScanType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSTaskScansItem")


@_attrs_define
class WMSTaskScansItem:
    """
    Attributes:
        scan_type (Union[Unset, WMSTaskScansItemScanType]): Type of scan performed Example: PRODUCT.
        scanned_value (Union[Unset, str]): Actual scanned value Example: ABC-XYZ-001.
        expected_value (Union[Unset, str]): Expected value for validation Example: ABC-XYZ-001.
        scan_result (Union[Unset, WMSTaskScansItemScanResult]): Result of scan validation Example: MATCH.
        scanned_at (Union[Unset, datetime.datetime]): Timestamp of the scan Example: 2024-11-27T09:25:00Z.
    """

    scan_type: Union[Unset, WMSTaskScansItemScanType] = UNSET
    scanned_value: Union[Unset, str] = UNSET
    expected_value: Union[Unset, str] = UNSET
    scan_result: Union[Unset, WMSTaskScansItemScanResult] = UNSET
    scanned_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scan_type: Union[Unset, str] = UNSET
        if not isinstance(self.scan_type, Unset):
            scan_type = self.scan_type.value

        scanned_value = self.scanned_value

        expected_value = self.expected_value

        scan_result: Union[Unset, str] = UNSET
        if not isinstance(self.scan_result, Unset):
            scan_result = self.scan_result.value

        scanned_at: Union[Unset, str] = UNSET
        if not isinstance(self.scanned_at, Unset):
            scanned_at = self.scanned_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scan_type is not UNSET:
            field_dict["scanType"] = scan_type
        if scanned_value is not UNSET:
            field_dict["scannedValue"] = scanned_value
        if expected_value is not UNSET:
            field_dict["expectedValue"] = expected_value
        if scan_result is not UNSET:
            field_dict["scanResult"] = scan_result
        if scanned_at is not UNSET:
            field_dict["scannedAt"] = scanned_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _scan_type = d.pop("scanType", UNSET)
        scan_type: Union[Unset, WMSTaskScansItemScanType]
        if isinstance(_scan_type, Unset):
            scan_type = UNSET
        else:
            scan_type = WMSTaskScansItemScanType(_scan_type)

        scanned_value = d.pop("scannedValue", UNSET)

        expected_value = d.pop("expectedValue", UNSET)

        _scan_result = d.pop("scanResult", UNSET)
        scan_result: Union[Unset, WMSTaskScansItemScanResult]
        if isinstance(_scan_result, Unset):
            scan_result = UNSET
        else:
            scan_result = WMSTaskScansItemScanResult(_scan_result)

        _scanned_at = d.pop("scannedAt", UNSET)
        scanned_at: Union[Unset, datetime.datetime]
        if isinstance(_scanned_at, Unset):
            scanned_at = UNSET
        else:
            scanned_at = isoparse(_scanned_at)

        wms_task_scans_item = cls(
            scan_type=scan_type,
            scanned_value=scanned_value,
            expected_value=expected_value,
            scan_result=scan_result,
            scanned_at=scanned_at,
        )

        wms_task_scans_item.additional_properties = d
        return wms_task_scans_item

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
