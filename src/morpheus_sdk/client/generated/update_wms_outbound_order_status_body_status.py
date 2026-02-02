from enum import Enum


class UpdateWMSOutboundOrderStatusBodyStatus(str, Enum):
    ALLOCATED = "ALLOCATED"
    PACKED = "PACKED"
    PICKED = "PICKED"
    PICKING = "PICKING"
    RELEASED = "RELEASED"
    SHIPPED = "SHIPPED"

    def __str__(self) -> str:
        return str(self.value)
