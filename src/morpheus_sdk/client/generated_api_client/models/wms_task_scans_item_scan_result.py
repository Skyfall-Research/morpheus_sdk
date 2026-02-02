from enum import Enum


class WMSTaskScansItemScanResult(str, Enum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"
    OVERRIDE = "OVERRIDE"

    def __str__(self) -> str:
        return str(self.value)
