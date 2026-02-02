from enum import Enum


class GetLogsServiceType(str, Enum):
    CAPABILITY = "capability"
    EDI = "edi"
    ERP = "erp"
    FINANCE = "finance"
    KNOWLEDGE_GRAPH = "knowledge-graph"
    MANUFACTURING = "manufacturing"
    OD = "od"
    PERSONA = "persona"
    TICKETS = "tickets"
    TMS = "tms"
    WMS = "wms"
    WORLD = "world"

    def __str__(self) -> str:
        return str(self.value)
