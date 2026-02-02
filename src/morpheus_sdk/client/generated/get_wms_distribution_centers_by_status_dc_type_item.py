from enum import Enum


class GetWMSDistributionCentersByStatusDcTypeItem(str, Enum):
    COLD_STORAGE = "COLD_STORAGE"
    CROSS_DOCK = "CROSS_DOCK"
    FULFILLMENT = "FULFILLMENT"
    VALUE_3 = "3PL"

    def __str__(self) -> str:
        return str(self.value)
