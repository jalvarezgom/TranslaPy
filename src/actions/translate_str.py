from src.actions.base import ActionBase
from src.classes.translator_deepl import TranslatorDeepl
from src.ui.ui import UI


class TranslateStrAction(ActionBase):
    msg = "TranslateStr"
    description = "Translate a string"

    @classmethod
    def execute(cls, **kwargs):
        UI.print("Write or paste the string to translate:")
        text = input()
        UI.print("Write the source language code: (leave empty to auto detect):")
        source_lang = input()
        UI.print("Write the target language code:")
        target_lang = input()
        if not target_lang:
            UI.print_error("Target language is required.")
            return False
        translation = TranslatorDeepl().translate(text, target_lang, source_lang=source_lang)
        UI.print(f"Source language detected: {translation.detected_source_lang}")
        UI.print_bold(f"Translation: \n{translation.text}")
        return True
