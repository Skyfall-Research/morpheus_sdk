from enum import Enum


class GetWMSShipmentsByStatusStatusItem(str, Enum):
    CREATED = "CREATED"
    DELIVERED = "DELIVERED"
    EXCEPTION = "EXCEPTION"
    IN_TRANSIT = "IN_TRANSIT"
    LOADED = "LOADED"
    LOADING = "LOADING"
    MANIFESTED = "MANIFESTED"
    SHIPPED = "SHIPPED"

    def __str__(self) -> str:
        return str(self.value)
