from enum import Enum


class GetWMSOrdersReadyForPickingOrderTypeItem(str, Enum):
    BULK = "BULK"
    EXPRESS = "EXPRESS"
    RETURNS = "RETURNS"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
