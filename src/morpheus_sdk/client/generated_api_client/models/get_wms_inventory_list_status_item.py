from enum import Enum


class GetWMSInventoryListStatusItem(str, Enum):
    ALLOCATED = "ALLOCATED"
    AVAILABLE = "AVAILABLE"
    DAMAGED = "DAMAGED"
    EXPIRED = "EXPIRED"
    HOLD = "HOLD"
    QUARANTINE = "QUARANTINE"

    def __str__(self) -> str:
        return str(self.value)
