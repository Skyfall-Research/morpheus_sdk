from enum import Enum


class TMSShipmentStatusEventSource(str, Enum):
    API = "API"
    CARRIER_PORTAL = "CARRIER_PORTAL"
    EDI = "EDI"
    GPS = "GPS"
    MANUAL = "MANUAL"

    def __str__(self) -> str:
        return str(self.value)
