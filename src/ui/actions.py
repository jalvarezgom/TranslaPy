from rich.prompt import Confirm, Prompt

from src.ui.theme import UIColors, UITheme


class UIActions:
    @classmethod
    def print(cls, content, **xtra_styles):
        cls.console.print(f"{content}", style=UIColors.TRANSLAPY)

    @classmethod
    def print_bold(cls, content, **xtra_styles):
        cls.console.print(f"{content}", style=UIColors.TRANSLAPY_BOLD)

    @classmethod
    def print_title(cls, title):
        cls.console.print(f"{title}", style=UITheme.TITLE)

    @classmethod
    def print_subtitle(cls, title):
        cls.console.print(f"{title}", style=UITheme.SUBTITLE)

    @classmethod
    def print_description(cls, description, **xtra_styles):
        pass

    @classmethod
    def print_error(cls, content):
        cls.console.print(f"{content}", style=UITheme.ERROR)

    @classmethod
    def print_success(cls, content):
        cls.console.print(f"{content}", style=UIColors.SUCCESS.value)

    @classmethod
    def input(cls, content, default=None, choices: list = None):
        return Prompt.ask(f"{content}", default=default, choices=choices)

    @classmethod
    def confirm(cls, content):
        return Confirm.ask(f"{content}")

    @classmethod
    def menu_select(cls, title, options):
        cls.print(f"{title}")
        for cont, option in enumerate(options):
            cls.print(f"[{cont+1}] {option}")
        return int(cls.input("Select an option", choices=[str(i) for i in range(1, len(options) + 1)])) - 1
