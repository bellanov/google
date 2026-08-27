"""Terminal User Interface (TUI)."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import (
    Footer,
    TabbedContent,
    TabPane,
)

from tui.domain.views.folders import get_folders_view
from tui.domain.views.header import get_google_header_view
from tui.domain.views.organization import get_organization_view
from tui.domain.views.projects import get_projects_view

COMPONENTS = {
    "Tabs": {
        "Organization": get_organization_view(),
        "Folders": get_folders_view(),
        "Projects": get_projects_view(),
    },
    "Header": {
        "Google": get_google_header_view(),
    },
}


class TUIApp(App):

    CSS_PATH = "app.tcss"

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding(key="delete", action="delete", description="Delete the thing"),
        Binding(key="j", action="down", description="Scroll down", show=False),
    ]

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
