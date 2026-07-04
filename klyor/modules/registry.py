"""Module Registry for Klyor.

Manages registration and loading of all available modules and tools.
"""

from typing import Dict, List, Callable
from pathlib import Path


class ModuleRegistry:
    """Registry for Klyor modules and tools.

    Manages registration, loading, and access to all available modules.

    Attributes:
        modules (Dict): Registered modules.
    """

    def __init__(self) -> None:
        """Initialize Module Registry."""
        self.modules: Dict[str, Dict] = {}
        self._register_builtin_modules()

    def _register_builtin_modules(self) -> None:
        """Register built-in modules."""
        self.register_module(
            "osint",
            {
                "name": "OSINT Tools",
                "description": "Open Source Intelligence utilities",
                "tools": [],
            },
        )
        self.register_module(
            "network",
            {
                "name": "Network Tools",
                "description": "Network analysis and utilities",
                "tools": [],
            },
        )
        self.register_module(
            "utilities",
            {
                "name": "General Utilities",
                "description": "Miscellaneous tools and helpers",
                "tools": [],
            },
        )

    def register_module(
        self,
        module_id: str,
        metadata: Dict,
    ) -> None:
        """Register a module.

        Args:
            module_id: Unique module identifier.
            metadata: Module metadata (name, description, tools).
        """
        self.modules[module_id] = metadata

    def get_module(self, module_id: str) -> Dict:
        """Get module by ID.

        Args:
            module_id: Module identifier.

        Returns:
            Module metadata or empty dict if not found.
        """
        return self.modules.get(module_id, {})

    def list_modules(self) -> List[str]:
        """List all registered module IDs.

        Returns:
            List of module IDs.
        """
        return list(self.modules.keys())

    def load_all(self) -> None:
        """Load all available modules."""
        pass

    def __len__(self) -> int:
        """Get number of registered modules.

        Returns:
            Number of modules.
        """
        return len(self.modules)
