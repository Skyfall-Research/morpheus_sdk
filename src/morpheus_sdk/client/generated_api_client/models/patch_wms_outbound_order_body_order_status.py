from enum import Enum


class PatchWMSOutboundOrderBodyOrderStatus(str, Enum):
    ALLOCATED = "ALLOCATED"
    CANCELLED = "CANCELLED"
    CREATED = "CREATED"
    PACKED = "PACKED"
    PACKING = "PACKING"
    PICKED = "PICKED"
    PICKING = "PICKING"
    RELEASED = "RELEASED"
    SHIPPED = "SHIPPED"

    def __str__(self) -> str:
        return str(self.value)
