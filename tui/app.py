"""Terminal User Interface (TUI)."""

import os

from textual.app import App, ComposeResult
from textual.widgets import Markdown

from tui.domain.models.errors import EnvironmentVariableError
from tui.services.organization import get_organization

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")


ORGANIZATION = get_organization(GCP_ORGANIZATION)
print(f"Organization: {ORGANIZATION}")

ORGANIZATION_MARKDOWN = f"""\
## {ORGANIZATION.display_name}

## Organization

|             |                         |
| --------------- | ---------------------------- |
| name   | {ORGANIZATION.name}   |
| display_name   | {ORGANIZATION.display_name}   |
"""


class TUIApp(App):

    def compose(self) -> ComposeResult:
        markdown = Markdown(ORGANIZATION_MARKDOWN)
        markdown.code_indent_guides = False
        yield markdown


if __name__ == "__main__":
    app = TUIApp()
    app.run()
