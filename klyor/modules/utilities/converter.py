"""Converter Utilities - Data Format Conversion.

Provides tools for converting between various data formats.
"""

import base64
import json
from typing import Dict, Optional


class Converter:
    """Data format converter utilities.

    Provides methods for converting between various data formats.
    """

    @staticmethod
    def base64_encode(data: str) -> str:
        """Encode string to Base64.

        Args:
            data: String to encode.

        Returns:
            Base64 encoded string.
        """
        return base64.b64encode(data.encode()).decode()

    @staticmethod
    def base64_decode(data: str) -> str:
        """Decode Base64 string.

        Args:
            data: Base64 string to decode.

        Returns:
            Decoded string.
        """
        try:
            return base64.b64decode(data.encode()).decode()
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def json_format(data: str) -> str:
        """Format JSON string with indentation.

        Args:
            data: JSON string to format.

        Returns:
            Formatted JSON string.
        """
        try:
            parsed = json.loads(data)
            return json.dumps(parsed, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Error: Invalid JSON - {e}"
