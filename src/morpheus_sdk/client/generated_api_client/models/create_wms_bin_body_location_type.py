from enum import Enum


class CreateWMSBinBodyLocationType(str, Enum):
    DOCK = "DOCK"
    QC = "QC"
    RETURN = "RETURN"
    STAGING = "STAGING"
    STORAGE = "STORAGE"

    def __str__(self) -> str:
        return str(self.value)
