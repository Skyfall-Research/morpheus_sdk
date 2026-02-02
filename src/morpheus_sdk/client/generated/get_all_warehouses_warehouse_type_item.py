from enum import Enum


class GetAllWarehousesWarehouseTypeItem(str, Enum):
    FULFILLMENT = "FULFILLMENT"
    RETURNS = "RETURNS"
    STAGING = "STAGING"
    VALUE_3 = "3PL"
    VIRTUAL = "VIRTUAL"

    def __str__(self) -> str:
        return str(self.value)
