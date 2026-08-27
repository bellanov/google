"""Terminal User Interface (TUI)."""

from textual.app import App, ComposeResult
from textual.widgets import (
    Footer,
    TabbedContent,
    TabPane,
)

from tui.domain.views.folder import get_folder_view
from tui.domain.views.header import get_google_header_view
from tui.domain.views.organization import get_organization_view
from tui.domain.views.project import get_projects_view

COMPONENTS = {
    "Tabs": {
        "Organization": get_organization_view(),
        "Folders": get_folder_view(),
        "Projects": get_projects_view(),
    },
    "Header": {
        "Google": get_google_header_view(),
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
