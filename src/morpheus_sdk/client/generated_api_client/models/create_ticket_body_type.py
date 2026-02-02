from enum import Enum


class CreateTicketBodyType(str, Enum):
    CHANGE = "change"
    INCIDENT = "incident"
    PROBLEM = "problem"
    SERVICE_REQUEST = "service_request"

    def __str__(self) -> str:
        return str(self.value)
