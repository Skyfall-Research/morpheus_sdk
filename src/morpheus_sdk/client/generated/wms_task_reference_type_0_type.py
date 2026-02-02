from enum import Enum


class WMSTaskReferenceType0Type(str, Enum):
    INBOUND = "INBOUND"
    ORDER = "ORDER"
    PO = "PO"
    REPLENISHMENT = "REPLENISHMENT"
    WAVE = "WAVE"

    def __str__(self) -> str:
        return str(self.value)
