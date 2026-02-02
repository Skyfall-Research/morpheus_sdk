from enum import Enum


class WMSInboundOrderOrderType(str, Enum):
    PO = "PO"
    RETURN = "RETURN"
    SAMPLE = "SAMPLE"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
