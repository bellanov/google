"""Terminal User Interface (TUI)."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import (
    Footer,
    TabbedContent,
    TabPane,
)

from tui.domain.views.folders import get_folders_view
from tui.domain.views.header import get_organization_view
from tui.domain.views.projects import get_projects_view

COMPONENTS = {
    "Tabs": {
        "Folders": get_folders_view(),
        "Projects": get_projects_view(),
    },
    "Header": {
        "Google": get_organization_view(),
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
