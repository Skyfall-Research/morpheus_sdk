from enum import Enum


class WMSOutboundShipmentCarrierMode(str, Enum):
    LTL = "LTL"
    PARCEL = "PARCEL"
    TL = "TL"

    def __str__(self) -> str:
        return str(self.value)
