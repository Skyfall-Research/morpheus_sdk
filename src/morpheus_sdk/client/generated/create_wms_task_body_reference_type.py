from enum import Enum


class CreateWMSTaskBodyReferenceType(str, Enum):
    INBOUND = "INBOUND"
    ORDER = "ORDER"
    PO = "PO"
    REPLENISHMENT = "REPLENISHMENT"
    WAVE = "WAVE"

    def __str__(self) -> str:
        return str(self.value)
