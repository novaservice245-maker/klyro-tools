"""Logging Infrastructure for Klyor.

This module provides centralized logging capabilities with support for
file and console output, with configurable log levels.
"""

import logging
from pathlib import Path
from datetime import datetime
from typing import Optional


class Logger:
    """Centralized Logger for Klyor.

    Provides logging to both console and file with configurable levels.
    Automatically creates log files in the specified directory.

    Attributes:
        log_dir (Path): Directory where log files are stored.
        logger (logging.Logger): Python logger instance.
    """

    def __init__(
        self,
        log_dir: Path,
        level: int = logging.INFO,
        console_output: bool = False,
    ) -> None:
        """Initialize Logger.

        Args:
            log_dir: Directory for log files.
            level: Logging level (default: INFO).
            console_output: Whether to also log to console.
        """
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Create logger
        self.logger = logging.getLogger("klyor")
        self.logger.setLevel(level)

        # Remove existing handlers
        self.logger.handlers.clear()

        # File handler
        log_file = self.log_dir / f"klyor_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(level)

        # Format
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Console handler
        if console_output:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def info(self, message: str) -> None:
        """Log info message.

        Args:
            message: Message to log.
        """
        self.logger.info(message)

    def error(self, message: str, exc_info: bool = False) -> None:
        """Log error message.

        Args:
            message: Message to log.
            exc_info: Include exception info if True.
        """
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Log warning message.

        Args:
            message: Message to log.
        """
        self.logger.warning(message)

    def debug(self, message: str) -> None:
        """Log debug message.

        Args:
            message: Message to log.
        """
        self.logger.debug(message)

    def close(self) -> None:
        """Close all logger handlers."""
        for handler in self.logger.handlers:
            handler.close()
