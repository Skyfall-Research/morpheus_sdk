from enum import Enum


class WMSOutboundOrderLinesItemUnitOfMeasure(str, Enum):
    CS = "CS"
    EA = "EA"
    FT = "FT"
    GAL = "GAL"
    KG = "KG"
    L = "L"
    LB = "LB"
    M = "M"

    def __str__(self) -> str:
        return str(self.value)
