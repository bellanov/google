"""Terminal User Interface (TUI)."""

from textual.containers import Container, Horizontal
from textual.widgets import (
    Markdown,
)

from tui.domain.controllers.organization import get_organization_markdown


def get_organization_view() -> Container:
    return Container(Markdown(get_organization_markdown()), id="organization")
