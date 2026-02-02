from enum import Enum


class WMSOutboundOrderPriority(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    NORMAL = "NORMAL"
    URGENT = "URGENT"

    def __str__(self) -> str:
        return str(self.value)
