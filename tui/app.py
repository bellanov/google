"""Terminal User Interface (TUI)."""

from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import (
    Button,
    Footer,
    Header,
    Markdown,
    Static,
    TabbedContent,
    TabPane,
)

from tui.domain.controllers.organization import ORGANIZATION_MARKDOWN
from tui.domain.controllers.project import PROJECTS_MARKDOWN
from tui.domain.views.folder import get_folder_view

GOOGLE_BANNER_TEXT = [
    ("G", "#4285F4"),  # G - Blue
    ("o", "#EA4335"),  # o - Red
    ("o", "#FBBC04"),  # o - Yellow
    ("g", "#4285F4"),  # g - Blue
    ("l", "#34A853"),  # l - Green
    ("e", "#EA4335"),  # e - Red
    (" ", "#FFFFFF"),  # Space
    ("C", "#4285F4"),  # C - Blue
    ("l", "#4285F4"),  # l - Blue
    ("o", "#4285F4"),  # o - Blue
    ("u", "#4285F4"),  # u - Blue
    ("d", "#4285F4"),  # d - Blue
    (" ", "#FFFFFF"),  # Space
    ("P", "#4285F4"),  # P - Blue
    ("l", "#4285F4"),  # l - Blue
    ("a", "#4285F4"),  # a - Blue
    ("t", "#4285F4"),  # t - Blue
    ("f", "#4285F4"),  # f - Blue
    ("o", "#4285F4"),  # o - Blue
    ("r", "#4285F4"),  # r - Blue
    ("m", "#4285F4"),  # m - Blue
]

COMPONENTS = {
    "Tabs": {
        "Organization": Container(Markdown(ORGANIZATION_MARKDOWN), id="organization"),
        "Folders": Container(get_folder_view(), id="folder"),
        "Projects": Container(Markdown(PROJECTS_MARKDOWN), id="projects"),
    },
    "Header": {
        "Google": Container(
            Static(Text.assemble(*GOOGLE_BANNER_TEXT), id="google-header"),
            id="header-container",
        ),
    },
}


class TUIApp(App):

    CSS_PATH = "app.tcss"

    def compose(self) -> ComposeResult:
        yield COMPONENTS["Header"]["Google"]

        with TabbedContent():
            for tab in COMPONENTS["Tabs"]:
                with TabPane(tab):
                    yield COMPONENTS["Tabs"][tab]

        yield Footer()


if __name__ == "__main__":
    app = TUIApp()
    app.run()
