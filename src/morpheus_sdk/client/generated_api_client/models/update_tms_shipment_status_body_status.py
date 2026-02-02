from enum import Enum


class UpdateTMSShipmentStatusBodyStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"
    DELAYED = "DELAYED"
    DELIVERED = "DELIVERED"
    EXCEPTION = "EXCEPTION"
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    PICKED_UP = "PICKED_UP"
    PLANNED = "PLANNED"
    TENDERED = "TENDERED"

    def __str__(self) -> str:
        return str(self.value)
