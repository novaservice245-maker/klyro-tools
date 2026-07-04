#!/usr/bin/env python3
"""Klyor - Modern Terminal Multitool.

Main entry point for the Klyor application.

Usage:
    python main.py
"""

import sys
from pathlib import Path

# Add klyor package to path
sys.path.insert(0, str(Path(__file__).parent))

from klyor.core.app import KlyorApp


def main() -> int:
    """Main entry point.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    app = KlyorApp()
    try:
        return app.run()
    except KeyboardInterrupt:
        print("\n[cyan]Goodbye![/cyan]")
        return 0
    finally:
        app.shutdown()


if __name__ == "__main__":
    sys.exit(main())
