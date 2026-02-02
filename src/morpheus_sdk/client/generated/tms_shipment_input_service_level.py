from enum import Enum


class TMSShipmentInputServiceLevel(str, Enum):
    ECONOMY = "ECONOMY"
    EXPEDITED = "EXPEDITED"
    NEXT_DAY = "NEXT_DAY"
    STANDARD = "STANDARD"
    TWO_DAY = "TWO_DAY"

    def __str__(self) -> str:
        return str(self.value)
