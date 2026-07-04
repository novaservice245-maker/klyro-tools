"""UI Components for Klyor Dashboard.

Provides reusable Rich-based components for building the dashboard.
"""

from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.console import Console
from typing import List, Optional


class KlyorPanel:
    """Custom panel component for Klyor UI.

    Attributes:
        title (str): Panel title.
        content (str): Panel content.
        style (str): Rich style string.
    """

    def __init__(
        self,
        title: str,
        content: str,
        style: str = "bold cyan",
        expand: bool = False,
    ) -> None:
        """Initialize Klyor Panel.

        Args:
            title: Panel title.
            content: Panel content.
            style: Rich style for the panel.
            expand: Whether panel should expand to fill available space.
        """
        self.title = title
        self.content = content
        self.style = style
        self.expand = expand

    def render(self) -> Panel:
        """Render panel as Rich Panel object.

        Returns:
            Rich Panel instance.
        """
        return Panel(
            self.content,
            title=self.title,
            style=self.style,
            expand=self.expand,
        )


class KlyorTable:
    """Custom table component for Klyor UI.

    Attributes:
        title (str): Table title.
        columns (List[str]): Column headers.
        rows (List[List[str]]): Table rows.
    """

    def __init__(
        self,
        title: str,
        columns: List[str],
        rows: Optional[List[List[str]]] = None,
    ) -> None:
        """Initialize Klyor Table.

        Args:
            title: Table title.
            columns: Column header names.
            rows: Optional initial rows.
        """
        self.title = title
        self.columns = columns
        self.rows = rows or []

    def add_row(self, *values: str) -> None:
        """Add a row to the table.

        Args:
            values: Values for each column.
        """
        self.rows.append(list(values))

    def render(self) -> Table:
        """Render table as Rich Table object.

        Returns:
            Rich Table instance.
        """
        table = Table(title=self.title, style="cyan")

        # Add columns
        for column in self.columns:
            table.add_column(column, style="magenta")

        # Add rows
        for row in self.rows:
            table.add_row(*row)

        return table
