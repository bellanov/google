"""Terminal User Interface (TUI)."""

import os

from textual.app import App, ComposeResult
from textual.widgets import Markdown

from tui.domain.views.organization import ORGANIZATION_MARKDOWN


class TUIApp(App):

    def compose(self) -> ComposeResult:
        markdown = Markdown(ORGANIZATION_MARKDOWN)
        markdown.code_indent_guides = False
        yield markdown


if __name__ == "__main__":
    app = TUIApp()
    app.run()
