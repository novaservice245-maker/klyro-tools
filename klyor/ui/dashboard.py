"""Main Dashboard for Klyor.

Provides the primary user interface for the Klyor application.
"""

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from typing import Optional

from klyor.core.config import ConfigManager
from klyor.core.logger import Logger
from klyor.ui.theme import ThemeManager
from klyor.ui.components import KlyorPanel, KlyorTable


class Dashboard:
    """Main Klyor Dashboard.

    Displays the primary user interface with tools, modules, and status.

    Attributes:
        config (ConfigManager): Application configuration.
        logger (Logger): Application logger.
        console (Console): Rich console instance.
        theme (ThemeManager): Theme manager.
    """

    def __init__(
        self,
        config: ConfigManager,
        logger: Logger,
    ) -> None:
        """Initialize Dashboard.

        Args:
            config: Configuration manager instance.
            logger: Logger instance.
        """
        self.config = config
        self.logger = logger
        self.console = Console()
        self.theme = ThemeManager(config.get("theme", "dark"))

    def render_header(self) -> None:
        """Render application header."""
        header_text = Text()
        header_text.append("⚡ KLYOR v1.0", style="bold cyan")
        header_text.append(" | ", style="dim")
        header_text.append(
            f"User: {self.config.get('username')}", style="magenta"
        )
        self.console.print(header_text)
        self.console.print("-" * 80, style="dim")

    def render_welcome(self) -> None:
        """Render welcome screen."""
        self.console.clear()
        self.render_header()

        # Welcome panel
        welcome_text = Text()
        welcome_text.append(
            "Welcome to Klyor - Modern Terminal Multitool\n\n",
            style="bold bright_cyan",
        )
        welcome_text.append(
            "Select a category to begin:\n",
            style="white",
        )

        panel = Panel(
            welcome_text,
            title="[bold magenta]Main Menu[/bold magenta]",
            style="cyan",
            expand=False,
        )
        self.console.print(panel)

        # Categories
        table = Table(title="Available Categories", style="cyan")
        table.add_column("#", style="magenta", width=5)
        table.add_column("Category", style="white")
        table.add_column("Description", style="dim")

        categories = [
            ("1", "OSINT", "Open Source Intelligence Tools"),
            ("2", "Network", "Network & Connectivity Tools"),
            ("3", "Utilities", "General Purpose Utilities"),
            ("4", "Settings", "Application Settings"),
            ("Q", "Quit", "Exit Application"),
        ]

        for num, cat, desc in categories:
            table.add_row(num, cat, desc)

        self.console.print(table)
        self.console.print()

    def render(self) -> None:
        """Render main dashboard."""
        self.render_welcome()

        # Simple input loop for demo
        while True:
            try:
                choice = input("\n> Select option: ").strip().upper()

                if choice == "Q":
                    self.console.print(
                        "[bold cyan]Thank you for using Klyor![/bold cyan]"
                    )
                    break
                elif choice == "1":
                    self.show_osint_menu()
                elif choice == "2":
                    self.show_network_menu()
                elif choice == "3":
                    self.show_utilities_menu()
                elif choice == "4":
                    self.show_settings_menu()
                else:
                    self.console.print(
                        "[bold red]Invalid option[/bold red]"
                    )
            except KeyboardInterrupt:
                self.console.print(
                    "\n[bold cyan]Goodbye![/bold cyan]"
                )
                break

    def show_osint_menu(self) -> None:
        """Show OSINT tools menu."""
        self.console.clear()
        self.render_header()

        panel = Panel(
            "[bold]OSINT Tools[/bold]\n\nOpen Source Intelligence utilities",
            title="[bold magenta]OSINT[/bold magenta]",
            style="cyan",
        )
        self.console.print(panel)
        input("\nPress Enter to go back...")
        self.render()

    def show_network_menu(self) -> None:
        """Show Network tools menu."""
        self.console.clear()
        self.render_header()

        panel = Panel(
            "[bold]Network Tools[/bold]\n\nNetwork analysis and utilities",
            title="[bold magenta]Network[/bold magenta]",
            style="cyan",
        )
        self.console.print(panel)
        input("\nPress Enter to go back...")
        self.render()

    def show_utilities_menu(self) -> None:
        """Show Utilities menu."""
        self.console.clear()
        self.render_header()

        panel = Panel(
            "[bold]General Utilities[/bold]\n\nMiscellaneous tools and helpers",
            title="[bold magenta]Utilities[/bold magenta]",
            style="cyan",
        )
        self.console.print(panel)
        input("\nPress Enter to go back...")
        self.render()

    def show_settings_menu(self) -> None:
        """Show Settings menu."""
        self.console.clear()
        self.render_header()

        panel = Panel(
            "[bold]Application Settings[/bold]\n\nConfigure Klyor",
            title="[bold magenta]Settings[/bold magenta]",
            style="cyan",
        )
        self.console.print(panel)
        input("\nPress Enter to go back...")
        self.render()
