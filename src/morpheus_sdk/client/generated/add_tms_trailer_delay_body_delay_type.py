from enum import Enum


class AddTMSTrailerDelayBodyDelayType(str, Enum):
    CARRIER = "CARRIER"
    DOCK_AVAILABILITY = "DOCK_AVAILABILITY"
    MECHANICAL = "MECHANICAL"
    OTHER = "OTHER"
    REGULATORY = "REGULATORY"
    TRAFFIC = "TRAFFIC"
    WEATHER = "WEATHER"

    def __str__(self) -> str:
        return str(self.value)
