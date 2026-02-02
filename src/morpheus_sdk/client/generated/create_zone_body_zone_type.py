from enum import Enum


class CreateZoneBodyZoneType(str, Enum):
    PACKING = "PACKING"
    PICKING = "PICKING"
    QC = "QC"
    RECEIVING = "RECEIVING"
    RETURNS = "RETURNS"
    SHIPPING = "SHIPPING"
    STAGING = "STAGING"
    STORAGE = "STORAGE"

    def __str__(self) -> str:
        return str(self.value)
