from enum import Enum


class GetWMSReplenishmentsByBinType(str, Enum):
    DESTINATION = "destination"
    SOURCE = "source"

    def __str__(self) -> str:
        return str(self.value)
