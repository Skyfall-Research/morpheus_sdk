from enum import Enum


class GetEdiDollarAmountStatisticsAggregationType(str, Enum):
    BY_DOCUMENT_TYPE = "by-document-type"
    BY_PARTNERS = "by-partners"

    def __str__(self) -> str:
        return str(self.value)
