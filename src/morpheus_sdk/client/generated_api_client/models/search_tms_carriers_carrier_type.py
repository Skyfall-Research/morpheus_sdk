from enum import Enum


class SearchTMSCarriersCarrierType(str, Enum):
    AIR = "AIR"
    COURIER = "COURIER"
    FTL = "FTL"
    INTERMODAL = "INTERMODAL"
    LTL = "LTL"
    OCEAN = "OCEAN"
    PARCEL = "PARCEL"
    RAIL = "RAIL"

    def __str__(self) -> str:
        return str(self.value)
