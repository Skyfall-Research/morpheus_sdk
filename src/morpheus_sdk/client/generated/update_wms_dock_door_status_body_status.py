from enum import Enum


class UpdateWMSDockDoorStatusBodyStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    CLOSED = "CLOSED"
    MAINTENANCE = "MAINTENANCE"
    OCCUPIED = "OCCUPIED"

    def __str__(self) -> str:
        return str(self.value)
