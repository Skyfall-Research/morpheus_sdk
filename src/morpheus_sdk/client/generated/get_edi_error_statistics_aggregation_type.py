from enum import Enum


class GetEdiErrorStatisticsAggregationType(str, Enum):
    BY_DOCTYPE = "by-doctype"
    BY_PARTNERS = "by-partners"

    def __str__(self) -> str:
        return str(self.value)
