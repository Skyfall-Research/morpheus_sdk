from enum import Enum


class GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItemDoorType(str, Enum):
    CROSS_DOCK = "CROSS_DOCK"
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"

    def __str__(self) -> str:
        return str(self.value)
