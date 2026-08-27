"""Folder View."""

import os

from textual.containers import Container
from textual.widgets import (
    Markdown,
)

from tui.domain.controllers.folders import get_folders_markdown
from tui.domain.models.errors import EnvironmentVariableError

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")


def get_folders_view() -> str:
    return Container(
        Markdown(get_folders_markdown()),
        id="folders",
    )
