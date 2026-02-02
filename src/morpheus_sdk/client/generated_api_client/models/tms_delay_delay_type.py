from enum import Enum


class TMSDelayDelayType(str, Enum):
    CARRIER = "CARRIER"
    CUSTOMS = "CUSTOMS"
    MECHANICAL = "MECHANICAL"
    OTHER = "OTHER"
    TRAFFIC = "TRAFFIC"
    WEATHER = "WEATHER"

    def __str__(self) -> str:
        return str(self.value)
