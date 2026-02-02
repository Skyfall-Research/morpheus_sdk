from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProcessTMSEdi214UpdateBodyRawEdiData")


@_attrs_define
class ProcessTMSEdi214UpdateBodyRawEdiData:
    """Complete raw EDI 214 message data

    Example:
        {'ISA': 'ISA*00*          *00*          *ZZ*CARRIER    *ZZ*SHIPPER    *241126*1430*U*00401*000000001*0*T*>',
            'GS': 'GS*QM*CARRIER*SHIPPER*20241126*1430*1*X*004010', 'ST': 'ST*214*0001', 'B10':
            'B10*SHIP-2024-001234*PRO123456789', 'segments': '...'}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        process_tms_edi_214_update_body_raw_edi_data = cls()

        process_tms_edi_214_update_body_raw_edi_data.additional_properties = d
        return process_tms_edi_214_update_body_raw_edi_data

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
