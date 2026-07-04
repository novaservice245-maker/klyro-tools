"""Klyor User Interface Module.

Provides Rich-based terminal UI components including dashboard,
theme system, and interactive components.
"""

from klyor.ui.dashboard import Dashboard
from klyor.ui.theme import ThemeManager
from klyor.ui.colors import ColorPalette

__all__ = ["Dashboard", "ThemeManager", "ColorPalette"]
