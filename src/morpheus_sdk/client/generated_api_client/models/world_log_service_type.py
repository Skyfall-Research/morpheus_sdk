from enum import Enum


class WorldLogServiceType(str, Enum):
    AS2 = "as2"
    EDI = "edi"
    ERP = "erp"
    GATEWAY = "gateway"
    INFRA = "infra"
    OTHER = "other"
    TRANSLATOR = "translator"
    VALIDATOR = "validator"

    def __str__(self) -> str:
        return str(self.value)
