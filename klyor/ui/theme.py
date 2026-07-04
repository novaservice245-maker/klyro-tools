"""Theme Management for Klyor UI.

Handles theme selection and application throughout the UI.
"""

from typing import Optional
from klyor.ui.colors import ColorPalette, ColorScheme


class ThemeManager:
    """Manages UI themes and color schemes.

    Provides methods to select and apply themes throughout the application.

    Attributes:
        current_theme (str): Name of the currently active theme.
        palette (ColorScheme): Current color palette.
    """

    def __init__(self, theme_name: str = "dark") -> None:
        """Initialize Theme Manager.

        Args:
            theme_name: Initial theme name.
        """
        self.current_theme = theme_name
        self.palette = ColorPalette.get_theme(theme_name)

    def set_theme(self, name: str) -> bool:
        """Set active theme.

        Args:
            name: Theme name to activate.

        Returns:
            True if theme was set successfully, False if invalid.
        """
        if name in ColorPalette.THEMES:
            self.current_theme = name
            self.palette = ColorPalette.get_theme(name)
            return True
        return False

    def get_available_themes(self) -> list[str]:
        """Get list of available themes.

        Returns:
            List of available theme names.
        """
        return list(ColorPalette.THEMES.keys())

    def get_style(self, element: str) -> str:
        """Get Rich style string for UI element.

        Args:
            element: Element type ('primary', 'secondary', 'text', etc.).

        Returns:
            Rich style string.
        """
        color = getattr(self.palette, element.lower(), self.palette.text)
        return f"color({color})"
