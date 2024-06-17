from cfg import RAISE_ERRORS
from src.actions import Actions
from src.ui.theme import UIColors
from src.ui.ui import UI


def main():
    UI.prepare()
    UI.console.clear()
    UI.show_title()
    user_actions = Actions.get_user_actions()
    while True:
        key_option, user_action = UI.show_menu(user_actions)
        UI.print("")
        if user_action:
            try:
                status = user_action()
                if not status:
                    UI.print_error(f"Action failed: {key_option}")
            except Exception as e:
                if RAISE_ERRORS:
                    raise e
                UI.print_error(f"Error executing action: {key_option}")
                UI.print_error(f"Error: {str(e)}")
            UI.print("Press any key to continue...")
            input()
        else:
            UI.print_error("No action found")
        UI.console.rule(style=UIColors.TRANSLAPY_DARK)


if __name__ == "__main__":
    main()
