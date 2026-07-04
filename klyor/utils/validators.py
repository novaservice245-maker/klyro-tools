"""Input Validators - Data Validation Utilities.

Provides validation functions for common data types.
"""

import re
from typing import Optional


class Validator:
    """Input validation utilities.

    Provides methods for validating various types of input.
    """

    @staticmethod
    def is_email(email: str) -> bool:
        """Validate email address.

        Args:
            email: Email address to validate.

        Returns:
            True if valid email format, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def is_ip(ip: str) -> bool:
        """Validate IP address (IPv4).

        Args:
            ip: IP address to validate.

        Returns:
            True if valid IPv4 format, False otherwise.
        """
        pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return re.match(pattern, ip) is not None

    @staticmethod
    def is_domain(domain: str) -> bool:
        """Validate domain name.

        Args:
            domain: Domain name to validate.

        Returns:
            True if valid domain format, False otherwise.
        """
        pattern = r'^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
        return re.match(pattern, domain) is not None

    @staticmethod
    def is_url(url: str) -> bool:
        """Validate URL.

        Args:
            url: URL to validate.

        Returns:
            True if valid URL format, False otherwise.
        """
        pattern = r'^https?://[^\s/$.?#].[^\s]*$'
        return re.match(pattern, url) is not None
