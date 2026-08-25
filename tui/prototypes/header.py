from textual.app import App, ComposeResult
from textual.widgets import Static
from rich.text import Text

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

class GoogleHeaderApp(App):
    CSS = """
    #custom-header {
        content-align: center middle;
        height: 8;
        text-style: bold;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(Text.assemble(*GOOGLE_BANNER_TEXT), id="custom-header")

if __name__ == "__main__":
    GoogleHeaderApp().run()