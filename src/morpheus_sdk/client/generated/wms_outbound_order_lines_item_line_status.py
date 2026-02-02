from enum import Enum


class WMSOutboundOrderLinesItemLineStatus(str, Enum):
    ALLOCATED = "ALLOCATED"
    PENDING = "PENDING"
    PICKED = "PICKED"
    PICKING = "PICKING"
    SHIPPED = "SHIPPED"

    def __str__(self) -> str:
        return str(self.value)
