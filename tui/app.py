"""Terminal User Interface (TUI)."""

import os

from textual.app import App, ComposeResult
from textual.widgets import (
    Footer,
    Header,
    Label,
    Markdown,
    TabbedContent,
    TabPane,
    Tabs,
)

from tui.domain.controllers.organization import ORGANIZATION_MARKDOWN

TABS = ["Organization", "Project", "Folder"]


class TUIApp(App):

    CSS = """
    Tabs {
        dock: top;
    }
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:

        with TabbedContent():
            for tab in TABS:
                with TabPane(tab):
                    yield Markdown(ORGANIZATION_MARKDOWN)

        markdown = Markdown(ORGANIZATION_MARKDOWN)
        markdown.code_indent_guides = False

        yield Footer()
        yield Header()

    def on_mount(self) -> None:
        self.title = "google"
        self.sub_title = "Google Cloud Platform"


if __name__ == "__main__":
    app = TUIApp()
    app.run()
