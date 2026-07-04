"""Plugin Loader - Dynamic Plugin Loading System.

Handles loading and managing third-party plugins.
"""

from pathlib import Path
from typing import Dict, List, Optional
import importlib.util
import sys


class PluginLoader:
    """Loader for Klyor plugins.

    Dynamically loads plugins from the plugins directory.

    Attributes:
        plugins_dir (Path): Directory containing plugins.
        loaded_plugins (Dict): Loaded plugin instances.
    """

    def __init__(self, plugins_dir: Path) -> None:
        """Initialize Plugin Loader.

        Args:
            plugins_dir: Path to plugins directory.
        """
        self.plugins_dir = Path(plugins_dir)
        self.loaded_plugins: Dict[str, any] = {}

    def load_plugin(self, plugin_name: str) -> bool:
        """Load a single plugin.

        Args:
            plugin_name: Name of plugin to load.

        Returns:
            True if plugin loaded successfully, False otherwise.
        """
        plugin_path = self.plugins_dir / f"{plugin_name}.py"

        if not plugin_path.exists():
            return False

        try:
            spec = importlib.util.spec_from_file_location(
                plugin_name,
                plugin_path,
            )
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                sys.modules[plugin_name] = module
                spec.loader.exec_module(module)
                self.loaded_plugins[plugin_name] = module
                return True
        except Exception:
            pass

        return False

    def load_all(self) -> List[str]:
        """Load all plugins from plugins directory.

        Returns:
            List of successfully loaded plugin names.
        """
        loaded = []
        if self.plugins_dir.exists():
            for plugin_file in self.plugins_dir.glob("*.py"):
                if plugin_file.name != "__init__.py":
                    plugin_name = plugin_file.stem
                    if self.load_plugin(plugin_name):
                        loaded.append(plugin_name)
        return loaded

    def get_plugin(self, plugin_name: str) -> Optional[any]:
        """Get loaded plugin module.

        Args:
            plugin_name: Name of plugin.

        Returns:
            Plugin module or None if not loaded.
        """
        return self.loaded_plugins.get(plugin_name)
