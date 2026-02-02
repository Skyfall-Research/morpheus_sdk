from enum import Enum


class WMSTaskScansItemScanType(str, Enum):
    BIN = "BIN"
    DESTINATION = "DESTINATION"
    LPN = "LPN"
    PRODUCT = "PRODUCT"

    def __str__(self) -> str:
        return str(self.value)
