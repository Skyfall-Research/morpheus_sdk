from enum import Enum


class UpdateERPShipmentBodyStatus(str, Enum):
    CREATED = "CREATED"
    DELIVERED = "DELIVERED"
    EXCEPTION = "EXCEPTION"
    IN_TRANSIT = "IN_TRANSIT"

    def __str__(self) -> str:
        return str(self.value)
