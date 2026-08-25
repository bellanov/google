"""Terminal User Interface (TUI)."""

from textual.app import App, ComposeResult
from textual.widgets import (
    Footer,
    Header,
    Markdown,
    TabbedContent,
    TabPane,
)

from tui.domain.controllers.organization import ORGANIZATION_MARKDOWN

TABS = {
    "Organization": ORGANIZATION_MARKDOWN,
    "Project": ORGANIZATION_MARKDOWN,
    "Folder": ORGANIZATION_MARKDOWN,
}


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
                    yield Markdown(TABS[tab])

        yield Footer()
        yield Header()

    def on_mount(self) -> None:
        self.title = "google"
        self.sub_title = "Google Cloud Platform"


if __name__ == "__main__":
    app = TUIApp()
    app.run()

pass