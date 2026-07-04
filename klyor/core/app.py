"""Main Klyor Application.

This module implements the main application class that orchestrates
all components and manages the application lifecycle.

Example:
    >>> app = KlyorApp()
    >>> app.run()
"""

import sys
from typing import Optional
from pathlib import Path

from klyor.core.config import ConfigManager
from klyor.core.logger import Logger
from klyor.ui.dashboard import Dashboard
from klyor.modules import ModuleRegistry


class KlyorApp:
    """Main Klyor Application.

    Orchestrates all application components including configuration,
    logging, UI rendering, and module management.

    Attributes:
        config (ConfigManager): Application configuration manager.
        logger (Logger): Centralized logger instance.
        dashboard (Dashboard): Main UI dashboard.
        modules (ModuleRegistry): Registered modules and tools.
    """

    def __init__(self, config_dir: Optional[str] = None) -> None:
        """Initialize Klyor Application.

        Args:
            config_dir: Optional custom configuration directory path.
                       Defaults to ~/.klyor/config if not provided.
        """
        self.config_dir = Path(config_dir) if config_dir else Path.home() / ".klyor"
        self.config = ConfigManager(self.config_dir)
        self.logger = Logger(self.config_dir / "logs")
        self.dashboard = Dashboard(self.config, self.logger)
        self.modules = ModuleRegistry()

        self.logger.info("Klyor Application initialized")

    def initialize_modules(self) -> None:
        """Initialize and register all available modules.

        This method loads all modules from the modules directory
        and registers them with the module registry.
        """
        self.logger.info("Initializing modules...")
        self.modules.load_all()
        self.logger.info(f"Loaded {len(self.modules)} modules")

    def run(self) -> int:
        """Run the main application loop.

        Returns:
            int: Exit code (0 for success, 1 for error).
        """
        try:
            self.logger.info("Starting Klyor")
            self.initialize_modules()
            self.dashboard.render()
            self.logger.info("Klyor closed normally")
            return 0
        except KeyboardInterrupt:
            self.logger.info("Klyor interrupted by user")
            return 0
        except Exception as e:
            self.logger.error(f"Fatal error: {e}", exc_info=True)
            return 1

    def shutdown(self) -> None:
        """Gracefully shutdown the application.

        Cleans up resources and logs shutdown information.
        """
        self.logger.info("Shutting down Klyor")
        self.logger.close()


def main() -> int:
    """Main entry point for Klyor.

    Returns:
        int: Exit code.
    """
    app = KlyorApp()
    try:
        return app.run()
    finally:
        app.shutdown()
