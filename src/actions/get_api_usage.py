from src.actions.base import ActionBase
from src.classes.translator_deepl import TranslatorDeepl
from src.ui.ui import UI


class GetAPIUsage(ActionBase):
    msg = "API usage info"
    description = "Information about the usage of the Deepl API"

    @classmethod
    def execute(cls, **kwargs):
        UI.print_bold("DEEP API USAGE:")
        usage_info = TranslatorDeepl().get_usage()
        UI.print(f"Character count: {usage_info.character.count} / {usage_info.character.limit}")
        UI.print(f"Is limit reached?: {usage_info.any_limit_reached}")
        UI.print(f"Is limit exceeded?: {usage_info.any_limit_exceeded}")
        return True
