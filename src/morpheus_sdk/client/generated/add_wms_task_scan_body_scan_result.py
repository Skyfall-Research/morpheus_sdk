from enum import Enum


class AddWMSTaskScanBodyScanResult(str, Enum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"
    OVERRIDE = "OVERRIDE"

    def __str__(self) -> str:
        return str(self.value)
