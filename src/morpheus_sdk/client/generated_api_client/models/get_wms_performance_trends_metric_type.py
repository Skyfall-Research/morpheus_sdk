from enum import Enum


class GetWMSPerformanceTrendsMetricType(str, Enum):
    INBOUND = "inbound"
    INVENTORY = "inventory"
    PACKING = "packing"
    PICKING = "picking"

    def __str__(self) -> str:
        return str(self.value)
