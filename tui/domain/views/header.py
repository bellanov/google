"""Terminal User Interface (TUI)."""

from rich.text import Text
from textual.containers import Container
from textual.widgets import (
    Static,
)

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


def get_google_header_view() -> Container:
    return Container(
        Static(Text.assemble(*GOOGLE_BANNER_TEXT), id="google-header"),
        id="header-container",
    )
