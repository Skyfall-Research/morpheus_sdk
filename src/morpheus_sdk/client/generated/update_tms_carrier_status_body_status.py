from enum import Enum


class UpdateTMSCarrierStatusBodyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    SUSPENDED = "SUSPENDED"

    def __str__(self) -> str:
        return str(self.value)
