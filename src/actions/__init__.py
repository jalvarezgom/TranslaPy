from enum import StrEnum, auto

from src.actions.exit import ExitAction
from src.actions.get_api_usage import GetAPIUsage
from src.actions.get_languages import GetLanguagesAction
from src.actions.translate_json import TranslateJSONAction
from src.actions.translate_str import TranslateStrAction


class Actions(StrEnum):
    TRANSLATE_STR = auto()
    TRANSLATE_JSON = auto()
    GET_LANGUAGES = auto()
    GET_API_USAGE = auto()
    EXIT = auto()

    @staticmethod
    def get_user_actions():
        user_actions = dict()
        user_actions[Actions.TRANSLATE_STR] = TranslateStrAction.to_dict()
        user_actions[Actions.TRANSLATE_JSON] = TranslateJSONAction.to_dict()
        user_actions[Actions.GET_LANGUAGES] = GetLanguagesAction.to_dict()
        user_actions[Actions.GET_API_USAGE] = GetAPIUsage.to_dict()
        user_actions[Actions.EXIT] = ExitAction.to_dict()
        return user_actions
