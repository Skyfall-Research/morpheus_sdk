from enum import Enum


class TMSInboundTrailerCargoTrailerType(str, Enum):
    DRY_VAN = "DRY_VAN"
    FLATBED = "FLATBED"
    INTERMODAL = "INTERMODAL"
    REEFER = "REEFER"
    TANKER = "TANKER"

    def __str__(self) -> str:
        return str(self.value)
