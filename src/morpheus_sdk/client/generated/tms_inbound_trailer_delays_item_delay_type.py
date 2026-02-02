from enum import Enum


class TMSInboundTrailerDelaysItemDelayType(str, Enum):
    CARRIER = "CARRIER"
    DOCK_AVAILABILITY = "DOCK_AVAILABILITY"
    OTHER = "OTHER"
    TRAFFIC = "TRAFFIC"
    WEATHER = "WEATHER"

    def __str__(self) -> str:
        return str(self.value)
