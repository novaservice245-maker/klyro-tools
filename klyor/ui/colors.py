"""Color Palette for Klyor.

Defines the color schemes for the Klyor UI.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class ColorScheme:
    """Color scheme definition.

    Attributes:
        primary: Primary accent color.
        secondary: Secondary accent color.
        background: Background color.
        text: Text color.
        success: Success state color.
        error: Error state color.
        warning: Warning state color.
    """

    primary: str
    secondary: str
    background: str
    text: str
    success: str
    error: str
    warning: str


class ColorPalette:
    """Color palette manager for Klyor.

    Manages multiple color schemes for different themes.
    """

    DARK_THEME = ColorScheme(
        primary="#00FFFF",
        secondary="#FF00FF",
        background="#0a0a0a",
        text="#FFFFFF",
        success="#00FF00",
        error="#FF0000",
        warning="#FFFF00",
    )

    PURPLE_THEME = ColorScheme(
        primary="#9D4EDD",
        secondary="#3A86FF",
        background="#0a0a0a",
        text="#E0AAFF",
        success="#06D6A0",
        error="#EF476F",
        warning="#FFD60A",
    )

    CYAN_THEME = ColorScheme(
        primary="#06D6A0",
        secondary="#118AB2",
        background="#0a0a0a",
        text="#FFFFFF",
        success="#06D6A0",
        error="#D62828",
        warning="#F77F00",
    )

    THEMES: Dict[str, ColorScheme] = {
        "dark": DARK_THEME,
        "purple": PURPLE_THEME,
        "cyan": CYAN_THEME,
    }

    @classmethod
    def get_theme(cls, name: str) -> ColorScheme:
        """Get color scheme by theme name.

        Args:
            name: Theme name.

        Returns:
            ColorScheme for the theme.
        """
        return cls.THEMES.get(name, cls.DARK_THEME)
