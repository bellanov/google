"""Folder View."""

import os

from textual.containers import Container
from textual.widgets import (
    Markdown,
)

from tui.domain.controllers.folder import get_folders_markdown


def get_folders_view() -> Container:
    """Builds the folders view."""
    return Container(
        Markdown(get_folders_markdown()),
        id="folders",
    )
