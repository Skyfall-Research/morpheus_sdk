from enum import Enum


class UpdateTMSTrailerStatusBodyStatus(str, Enum):
    AT_DOCK = "AT_DOCK"
    CANCELLED = "CANCELLED"
    CHECKED_IN = "CHECKED_IN"
    DELAYED = "DELAYED"
    DEPARTED = "DEPARTED"
    EN_ROUTE = "EN_ROUTE"
    SCHEDULED = "SCHEDULED"
    UNLOADED = "UNLOADED"
    UNLOADING = "UNLOADING"

    def __str__(self) -> str:
        return str(self.value)
