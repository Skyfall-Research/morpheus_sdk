from enum import Enum


class UpdateWMSInventoryStatusBodyInventoryStatus(str, Enum):
    ALLOCATED = "ALLOCATED"
    AVAILABLE = "AVAILABLE"
    EXPIRED = "EXPIRED"
    HOLD = "HOLD"
    QUARANTINE = "QUARANTINE"

    def __str__(self) -> str:
        return str(self.value)
