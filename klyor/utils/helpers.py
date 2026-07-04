"""Helper Functions - Common Utility Functions.

Provides commonly used helper functions.
"""

from typing import Any, Dict, List


class Helper:
    """Common helper functions.

    Provides utility functions for common tasks.
    """

    @staticmethod
    def flatten_dict(d: Dict, parent_key: str = '', sep: str = '.') -> Dict:
        """Flatten a nested dictionary.

        Args:
            d: Dictionary to flatten.
            parent_key: Parent key prefix.
            sep: Separator for keys.

        Returns:
            Flattened dictionary.
        """
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(Helper.flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    @staticmethod
    def truncate(text: str, length: int = 50) -> str:
        """Truncate text to specified length.

        Args:
            text: Text to truncate.
            length: Maximum length.

        Returns:
            Truncated text with ellipsis if needed.
        """
        if len(text) <= length:
            return text
        return text[:length - 3] + "..."
