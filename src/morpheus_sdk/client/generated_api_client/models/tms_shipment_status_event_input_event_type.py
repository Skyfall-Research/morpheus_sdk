from enum import Enum


class TMSShipmentStatusEventInputEventType(str, Enum):
    DELAY = "DELAY"
    ETA_UPDATE = "ETA_UPDATE"
    EXCEPTION = "EXCEPTION"
    LOCATION_UPDATE = "LOCATION_UPDATE"
    MILESTONE = "MILESTONE"
    STATUS_CHANGE = "STATUS_CHANGE"

    def __str__(self) -> str:
        return str(self.value)
