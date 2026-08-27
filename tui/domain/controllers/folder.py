"""Folder View."""

import os

from textual.containers import Container, Horizontal
from textual.widgets import (
    Button,
    Static,
)

from tui.domain.models.errors import EnvironmentVariableError

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")

QUESTION = "Do you want to learn about Textual CSS?"


def get_folder_view() -> str:
    return Container(
        Static(QUESTION, classes="question"),
        Horizontal(
            Button("Yes", variant="success"),
            Button("No", variant="error"),
            classes="buttons",
        ),
        id="dialog",
    )
