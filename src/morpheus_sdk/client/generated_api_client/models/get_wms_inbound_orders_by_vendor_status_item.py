from enum import Enum


class GetWMSInboundOrdersByVendorStatusItem(str, Enum):
    CANCELLED = "CANCELLED"
    CLOSED = "CLOSED"
    EXPECTED = "EXPECTED"
    IN_TRANSIT = "IN_TRANSIT"
    RECEIVED = "RECEIVED"
    RECEIVING = "RECEIVING"

    def __str__(self) -> str:
        return str(self.value)
