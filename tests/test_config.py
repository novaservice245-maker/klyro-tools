"""Tests for Configuration Management.

Tests the ConfigManager class and Settings dataclass.
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from klyor.core.config import ConfigManager, Settings


def test_config_manager_initialization():
    """Test ConfigManager initialization."""
    with TemporaryDirectory() as tmpdir:
        config = ConfigManager(Path(tmpdir))
        assert config.config_dir == Path(tmpdir)
        assert isinstance(config.settings, Settings)


def test_config_manager_save_load():
    """Test saving and loading configuration."""
    with TemporaryDirectory() as tmpdir:
        config = ConfigManager(Path(tmpdir))
        config.settings.username = "TestUser"
        config.save()

        config2 = ConfigManager(Path(tmpdir))
        assert config2.settings.username == "TestUser"


def test_settings_to_dict():
    """Test Settings to_dict method."""
    settings = Settings(username="Test", language="fr")
    d = settings.to_dict()
    assert d["username"] == "Test"
    assert d["language"] == "fr"
