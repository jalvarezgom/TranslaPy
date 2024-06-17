import deepl
from deepl import Translator as TransDeepl

from cfg import DEEPL_SECRET_KEY
from src.classes.translator import Translator


class TranslatorDeepl(Translator):
    __SECRET_KEY = ""

    def __init__(self):
        if not DEEPL_SECRET_KEY:
            raise ValueError("DEEPL_SECRET_KEY is not set. Please set it in cfg.py")
        self._translator: TransDeepl = deepl.Translator(DEEPL_SECRET_KEY)

    def translate(self, text, target_lang, xtra_actions={}, **xtra_args):
        translation = self._translator.translate_text(text, target_lang=target_lang, **xtra_args)
        if xtra_actions.get("rich_progress") and xtra_actions.get("rich_task") is not None:
            xtra_actions["rich_progress"].update(xtra_actions["rich_task"], advance=1)
        return translation

    def get_languages(self, country_code=None, country_name=None):
        languages = self._translator.get_source_languages()
        languages = sorted(languages, key=lambda x: x.name)
        return languages

    def get_usage(self):
        return self._translator.get_usage()
