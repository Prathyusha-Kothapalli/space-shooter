"""
Logger module providing structured output, severity levels, and log persistence.
"""

import sys
import time
from enum import IntEnum
from typing import Optional


class LogLevel(IntEnum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4


class Logger:
    """Singleton Logger class."""
    _instance: Optional['Logger'] = None

    def __init__(self, min_level: LogLevel = LogLevel.INFO, log_to_file: bool = False, file_path: str = "game.log"):
        self.min_level = min_level
        self.log_to_file = log_to_file
        self.file_path = file_path
        self._file_handle = None

        if self.log_to_file:
            try:
                self._file_handle = open(self.file_path, 'a', encoding='utf-8')
            except Exception as e:
                print(f"[Logger] Failed to open log file {file_path}: {e}")

    @classmethod
    def get_instance(cls) -> 'Logger':
        if cls._instance is None:
            cls._instance = Logger()
        return cls._instance

    def log(self, level: LogLevel, tag: str, message: str) -> None:
        """Output formatted log entry."""
        if level < self.min_level:
            return

        timestamp = time.strftime("%H:%M:%S", time.localtime())
        level_str = level.name
        formatted = f"[{timestamp}] [{level_str}] [{tag}] {message}"

        # Write to stdout
        if level >= LogLevel.ERROR:
            print(formatted, file=sys.stderr)
        else:
            print(formatted)

        # Write to file if enabled
        if self._file_handle:
            try:
                self._file_handle.write(formatted + "\n")
                self._file_handle.flush()
            except Exception:
                pass

    def debug(self, tag: str, msg: str) -> None:
        self.log(LogLevel.DEBUG, tag, msg)

    def info(self, tag: str, msg: str) -> None:
        self.log(LogLevel.INFO, tag, msg)

    def warning(self, tag: str, msg: str) -> None:
        self.log(LogLevel.WARNING, tag, msg)

    def error(self, tag: str, msg: str) -> None:
        self.log(LogLevel.ERROR, tag, msg)

    def critical(self, tag: str, msg: str) -> None:
        self.log(LogLevel.CRITICAL, tag, msg)


# Helper functions
def log_info(tag: str, msg: str) -> None:
    Logger.get_instance().info(tag, msg)

def log_error(tag: str, msg: str) -> None:
    Logger.get_instance().error(tag, msg)

def log_warning(tag: str, msg: str) -> None:
    Logger.get_instance().warning(tag, msg)
