from enum import Enum


class UpdateWMSDistributionCenterStatusBodyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    MAINTENANCE = "MAINTENANCE"

    def __str__(self) -> str:
        return str(self.value)
