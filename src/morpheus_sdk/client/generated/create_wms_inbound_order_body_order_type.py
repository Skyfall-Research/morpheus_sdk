from enum import Enum


class CreateWMSInboundOrderBodyOrderType(str, Enum):
    PO = "PO"
    RETURN = "RETURN"
    SAMPLE = "SAMPLE"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
