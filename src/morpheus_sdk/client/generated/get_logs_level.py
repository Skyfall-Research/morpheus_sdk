from enum import Enum


class GetLogsLevel(str, Enum):
    DEBUG = "debug"
    ERROR = "error"
    FATAL = "fatal"
    INFO = "info"
    TRACE = "trace"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
