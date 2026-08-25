"""Terminal User Interface (TUI)."""

from rich.text import Text

from textual.app import App, ComposeResult
from textual.widgets import (
    Footer,
    Header,
    Markdown,
    Static,
    TabbedContent,
    TabPane,
)

from tui.domain.controllers.organization import ORGANIZATION_MARKDOWN

TABS = {
    "Organization": ORGANIZATION_MARKDOWN,
    "Projects": ORGANIZATION_MARKDOWN,
    "Folders": ORGANIZATION_MARKDOWN,
}

GOOGLE_BANNER_TEXT = [
    ("G", "#4285F4"),  # G - Blue
    ("o", "#EA4335"),  # o - Red
    ("o", "#FBBC04"),  # o - Yellow
    ("g", "#4285F4"),  # g - Blue
    ("l", "#34A853"),  # l - Green
    ("e", "#EA4335"),  # e - Red
    (" ", "#FFFFFF"),  # Space
    ("C", "#4285F4"),  # C - Dark Gray
    ("l", "#4285F4"),  # l - Dark Gray
    ("o", "#4285F4"),  # o - Dark Gray
    ("u", "#4285F4"),  # u - Dark Gray
    ("d", "#4285F4"),  # d - Dark Gray
]

class TUIApp(App):

    CSS = """
    #google-header {
        content-align: center middle;
        height: 8;
        text-style: bold;
    }
    Tabs {
        dock: top;
    }
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(Text.assemble(*GOOGLE_BANNER_TEXT), id="google-header")

        with TabbedContent():
            for tab in TABS:
                with TabPane(tab):
                    yield Markdown(TABS[tab])

        yield Footer()
        yield Header()

    def on_mount(self) -> None:
        self.title = "GCP"
        self.sub_title = "Google Cloud Platform"


if __name__ == "__main__":
    app = TUIApp()
    app.run()
