from enum import Enum


class CreateWMSDockDoorBodyDoorType(str, Enum):
    CROSS_DOCK = "CROSS_DOCK"
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"

    def __str__(self) -> str:
        return str(self.value)
