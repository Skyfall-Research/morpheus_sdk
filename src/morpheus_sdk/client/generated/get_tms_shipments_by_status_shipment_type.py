from enum import Enum


class GetTMSShipmentsByStatusShipmentType(str, Enum):
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"
    RETURN = "RETURN"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
