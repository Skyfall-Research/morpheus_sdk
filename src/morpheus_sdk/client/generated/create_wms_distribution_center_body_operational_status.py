from enum import Enum


class CreateWMSDistributionCenterBodyOperationalStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    MAINTENANCE = "MAINTENANCE"

    def __str__(self) -> str:
        return str(self.value)
