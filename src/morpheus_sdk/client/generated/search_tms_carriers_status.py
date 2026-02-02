from enum import Enum


class SearchTMSCarriersStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    SUSPENDED = "SUSPENDED"

    def __str__(self) -> str:
        return str(self.value)
