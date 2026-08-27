"""Terminal User Interface (TUI)."""

from textual.containers import Container, Horizontal
from textual.widgets import (
    Markdown,
)

from tui.domain.controllers.project import get_projects_markdown


def get_projects_view() -> Container:
    return Container(Markdown(get_projects_markdown()), id="projects")
