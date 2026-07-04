"""Ping Tool - Network Latency Testing.

Provides ICMP ping functionality for testing connectivity and latency.
"""

import subprocess
import platform
from typing import Dict, Optional


class Ping:
    """Ping utility for network diagnostics.

    Provides methods for testing connectivity and measuring latency.
    """

    @staticmethod
    def ping(host: str, count: int = 4, timeout: int = 4) -> Dict:
        """Ping a host.

        Args:
            host: Hostname or IP address to ping.
            count: Number of ping attempts.
            timeout: Timeout in seconds.

        Returns:
            Dictionary with ping results.
        """
        try:
            system = platform.system().lower()
            param = "-n" if system == "windows" else "-c"
            timeout_param = "-w" if system == "windows" else "-W"

            cmd = ["ping", param, str(count), timeout_param, str(timeout * 1000), host]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout + 2,
            )

            if result.returncode == 0:
                return {
                    "host": host,
                    "status": "reachable",
                    "output": result.stdout,
                }
            else:
                return {
                    "host": host,
                    "status": "unreachable",
                    "error": result.stderr,
                }
        except Exception as e:
            return {
                "host": host,
                "status": "error",
                "error": str(e),
            }
