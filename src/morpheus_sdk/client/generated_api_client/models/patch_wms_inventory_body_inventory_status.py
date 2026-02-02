from enum import Enum


class PatchWMSInventoryBodyInventoryStatus(str, Enum):
    ALLOCATED = "ALLOCATED"
    AVAILABLE = "AVAILABLE"
    DAMAGED = "DAMAGED"
    EXPIRED = "EXPIRED"
    HOLD = "HOLD"
    QUARANTINE = "QUARANTINE"

    def __str__(self) -> str:
        return str(self.value)
