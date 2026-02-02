from enum import Enum


class GetWMSBinsByZoneStatusItem(str, Enum):
    AVAILABLE = "AVAILABLE"
    BLOCKED = "BLOCKED"
    DAMAGED = "DAMAGED"
    OCCUPIED = "OCCUPIED"
    RESERVED = "RESERVED"

    def __str__(self) -> str:
        return str(self.value)
