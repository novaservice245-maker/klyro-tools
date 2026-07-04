"""Configuration Management for Klyor.

This module handles loading, parsing, and managing application configuration.
Supports JSON configuration files with defaults and validation.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional
from dataclasses import dataclass, asdict


@dataclass
class Settings:
    """Application settings dataclass.

    Attributes:
        language: User interface language ('en' or 'fr').
        theme: Active color theme name.
        username: Username for the application.
        skip_boot_animation: Whether to skip boot animation on startup.
        auto_update: Enable automatic updates.
    """

    language: str = "en"
    theme: str = "dark"
    username: str = "Operator"
    skip_boot_animation: bool = False
    auto_update: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert settings to dictionary.

        Returns:
            Dictionary representation of settings.
        """
        return asdict(self)


class ConfigManager:
    """Manages application configuration.

    Handles loading, saving, and accessing application settings.
    Automatically creates configuration files if they don't exist.

    Attributes:
        config_dir (Path): Configuration directory path.
        settings_file (Path): Path to settings.json file.
        settings (Settings): Current settings instance.
    """

    DEFAULT_SETTINGS = Settings()

    def __init__(self, config_dir: Path) -> None:
        """Initialize Configuration Manager.

        Args:
            config_dir: Path to configuration directory.
        """
        self.config_dir = Path(config_dir)
        self.settings_file = self.config_dir / "settings.json"
        self.settings = self.DEFAULT_SETTINGS

        # Create config directory if it doesn't exist
        self.config_dir.mkdir(parents=True, exist_ok=True)

        # Load settings
        self.load()

    def load(self) -> None:
        """Load settings from configuration file.

        If the file doesn't exist, creates it with default settings.
        """
        if self.settings_file.exists():
            try:
                with open(self.settings_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.settings = Settings(**data)
            except (json.JSONDecodeError, TypeError):
                self.settings = self.DEFAULT_SETTINGS
                self.save()
        else:
            self.save()

    def save(self) -> None:
        """Save current settings to configuration file."""
        with open(self.settings_file, "w", encoding="utf-8") as f:
            json.dump(self.settings.to_dict(), f, indent=2, ensure_ascii=False)

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value.

        Args:
            key: Configuration key name.
            default: Default value if key not found.

        Returns:
            Configuration value or default.
        """
        return getattr(self.settings, key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value.

        Args:
            key: Configuration key name.
            value: New value to set.
        """
        if hasattr(self.settings, key):
            setattr(self.settings, key, value)
            self.save()
