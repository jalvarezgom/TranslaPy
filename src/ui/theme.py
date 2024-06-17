from enum import auto, StrEnum

from rich.theme import Theme


class UITheme(StrEnum):
    TITLE = auto()
    SUBTITLE = auto()
    TRANSLAPY = auto()
    SUCCESS = auto()
    ERROR = auto()

    @staticmethod
    def get_theme():
        dict = {}
        for theme in UITheme:
            dict[theme.value] = UIColors[theme.name].value
        return Theme(dict)


class UIColors(StrEnum):
    TITLE = "bold #ff6f1e"
    SUBTITLE = "bold #fec504"
    TRANSLAPY = "#fec504"
    TRANSLAPY_BOLD = "bold #fec504"
    TRANSLAPY_DARK = "#ff6f1e"
    SUCCESS = "green"
    ERROR = "bold red"
