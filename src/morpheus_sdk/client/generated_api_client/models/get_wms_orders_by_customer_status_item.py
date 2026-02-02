from enum import Enum


class GetWMSOrdersByCustomerStatusItem(str, Enum):
    ALLOCATED = "ALLOCATED"
    CANCELLED = "CANCELLED"
    PACKED = "PACKED"
    PENDING = "PENDING"
    PICKED = "PICKED"
    PICKING = "PICKING"
    RELEASED = "RELEASED"
    SHIPPED = "SHIPPED"

    def __str__(self) -> str:
        return str(self.value)
