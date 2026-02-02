from enum import Enum


class GetAuditLogsModel(str, Enum):
    CAPABILITY = "Capability"
    CARRIER = "Carrier"
    COMPANY = "Company"
    EDITRANSACTION = "EdiTransaction"
    ERPSHIPMENT = "ERPShipment"
    FINANCETRANSACTION = "FinanceTransaction"
    INBOUNDORDER = "InboundOrder"
    OPERATIONALDESCRIPTOR = "OperationalDescriptor"
    PERSONA = "Persona"
    PRODUCTIONRUN = "ProductionRun"
    TASK = "Task"
    TMSSHIPMENT = "TMSShipment"
    WORLD = "World"
    WORLDITSMTICKET = "WorldItsmTicket"

    def __str__(self) -> str:
        return str(self.value)
