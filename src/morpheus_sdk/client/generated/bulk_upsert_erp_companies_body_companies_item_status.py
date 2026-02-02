from enum import Enum


class BulkUpsertERPCompaniesBodyCompaniesItemStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    INACTIVE = "INACTIVE"
    PROSPECT = "PROSPECT"

    def __str__(self) -> str:
        return str(self.value)
