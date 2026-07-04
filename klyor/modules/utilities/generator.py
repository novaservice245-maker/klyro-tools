"""Generator Utilities - Data Generation Tools.

Provides tools for generating various types of test data.
"""

import random
import string
from typing import List


class Generator:
    """Data generation utilities.

    Provides methods for generating various types of data.
    """

    @staticmethod
    def generate_password(length: int = 16) -> str:
        """Generate a random password.

        Args:
            length: Password length.

        Returns:
            Generated password.
        """
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def generate_uuid() -> str:
        """Generate a random UUID.

        Returns:
            Generated UUID.
        """
        import uuid
        return str(uuid.uuid4())

    @staticmethod
    def generate_hex(length: int = 32) -> str:
        """Generate random hexadecimal string.

        Args:
            length: Length of hex string.

        Returns:
            Generated hex string.
        """
        return ''.join(random.choice(string.hexdigits[:16]) for _ in range(length))
