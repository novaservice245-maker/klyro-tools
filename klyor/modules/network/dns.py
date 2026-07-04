"""DNS Tools - Domain Name System Utilities.

Provides DNS lookup and resolution utilities.
"""

import socket
from typing import Dict, List, Optional

try:
    import dns.resolver
    DNSPYTHON_AVAILABLE = True
except ImportError:
    DNSPYTHON_AVAILABLE = False


class DNS:
    """DNS utilities for domain resolution and lookup.

    Provides methods for DNS queries and domain name resolution.
    """

    @staticmethod
    def resolve(domain: str) -> Dict[str, List[str]]:
        """Resolve domain to IP address(es).

        Args:
            domain: Domain name to resolve.

        Returns:
            Dictionary with resolved IP addresses.
        """
        try:
            ips = socket.gethostbyname_ex(domain)[2]
            return {
                "domain": domain,
                "ips": ips,
            }
        except socket.gaierror as e:
            return {
                "domain": domain,
                "error": f"Could not resolve: {e}",
            }

    @staticmethod
    def reverse_lookup(ip: str) -> Dict[str, str]:
        """Perform reverse DNS lookup on an IP address.

        Args:
            ip: IP address to reverse lookup.

        Returns:
            Dictionary with domain name if found.
        """
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return {
                "ip": ip,
                "hostname": hostname,
            }
        except socket.herror:
            return {
                "ip": ip,
                "hostname": "Not found",
            }
