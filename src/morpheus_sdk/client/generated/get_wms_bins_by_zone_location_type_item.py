from enum import Enum


class GetWMSBinsByZoneLocationTypeItem(str, Enum):
    DOCK = "DOCK"
    QC = "QC"
    RETURN = "RETURN"
    STAGING = "STAGING"
    STORAGE = "STORAGE"

    def __str__(self) -> str:
        return str(self.value)
