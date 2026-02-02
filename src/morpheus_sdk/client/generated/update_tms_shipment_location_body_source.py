from enum import Enum


class UpdateTMSShipmentLocationBodySource(str, Enum):
    CARRIER_PORTAL = "CARRIER_PORTAL"
    EDI = "EDI"
    GPS = "GPS"
    MANUAL = "MANUAL"

    def __str__(self) -> str:
        return str(self.value)
