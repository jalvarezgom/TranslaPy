from rich.console import Console

from src.ui.actions import UIActions
from src.ui.theme import UITheme, UIColors
from src.ui_constants import APP_TITLE


class UI(UIActions):
    console = None

    @classmethod
    def prepare(cls):
        # install(show_locals=True)
        cls.custom_theme = UITheme.get_theme()
        cls.console = Console(
            width=100,
            theme=cls.custom_theme,
        )

    @classmethod
    def show_title(cls):
        cls.print_title(APP_TITLE)

    @classmethod
    def show_menu(cls, menu):
        cls.print_subtitle(
            """ __  __              
|  \/  |___ _ _ _  _ 
| |\/| / -_) ' \ || |
|_|  |_\___|_||_\_,_|              
"""
        )
        cont = 1
        for key, value in menu.items():
            description = "" if value["description"] is None else f"({value['description']})"
            cls.print(f"[{cont}] {value['msg']} {description}")
            cont += 1
        option = cls.input(content="Choose an option: ", choices=[str(x) for x in range(1, len(menu) + 1)])
        if option is None or not option.isdigit():
            cls.console.print("Invalid option", style=UIColors.ERROR.value)
            return None, None
        option = int(option)
        if option < 1 or option > len(menu):
            cls.console.print("Invalid option", style=UIColors.ERROR.value)
            return None, None
        key_option = list(menu.keys())[option - 1]
        action = menu[key_option]["action"]
        return key_option, action
