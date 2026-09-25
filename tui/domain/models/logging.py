"""Logging Models."""

import logging
from enum import StrEnum

LOG_FORMAT_DEBUG = "%(levelname)s:%(message)s:%(pathname)s:%(funcName)s:%(lineno)d"


class LogLevels(StrEnum):
    """Define Log Levels."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


def configure_logging(log_level: str = LogLevels.INFO):
    """Configure logging settings.

    Args:
        log_level: The desired log level (DEBUG, INFO, WARNING, ERROR).
    """
    log_level = str(log_level).upper()

    if log_level not in LogLevels.__members__:
        logging.basicConfig(level=LogLevels.ERROR)
        return

    if log_level == LogLevels.DEBUG:
        logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT_DEBUG)
        return

    logging.basicConfig(level=log_level)
