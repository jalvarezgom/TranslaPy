from src.actions.base import ActionBase
from src.classes.translator_deepl import TranslatorDeepl
from src.ui.ui import UI


class GetLanguagesAction(ActionBase):
    msg = "Get languages for translation"
    description = "Get languages available for translation from Deepl"

    @classmethod
    def execute(cls, **kwargs):
        UI.print("Getting languages...")
        languages = TranslatorDeepl().get_languages()
        for language in languages:
            UI.print(f"{language.name} ({language.code})")
        return True
