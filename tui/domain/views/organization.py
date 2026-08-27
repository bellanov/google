"""Organization View."""

from textual.containers import Container
from textual.widgets import (
    Markdown,
)

from tui.domain.controllers.organization import get_organization_markdown


def get_organization_view() -> Container:
    """Builds the organization view."""
    return Container(Markdown(get_organization_markdown()), id="organization")
