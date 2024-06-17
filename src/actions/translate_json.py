import json
import os

from rich.progress import Progress

from src.actions.base import ActionBase
from src.classes.translator_deepl import TranslatorDeepl
from src.ui.ui import UI


class TranslateJSONAction(ActionBase):
    msg = "TranslateJSON"
    description = "Translate a JSON file to another language."

    @classmethod
    def execute(cls, **kwargs):
        UI.print("Write the path of the JSON file:")
        json_file = input()
        if os.path.exists(json_file):
            UI.print("Write the source language code: (leave empty to auto detect):")
            source_lang = input()
            UI.print("Write the target language code: (If you want multiple languages, separate them with a comma):")
            target_langs = input()
            if not target_langs:
                UI.print_error("Target language is required.")
                return False
            else:
                target_langs = [lang.strip() for lang in target_langs.split(",")]
            UI.print("Write or paste the path of the output file (default: Current directory):")
            output_json_path = input()
            UI.print(f"Write or paste the name of the output file (default: {target_langs[0]}):")
            output_json_file_format = input()
            if not output_json_file_format:
                output_json_file_format = "{target_lang}.json"
            elif len(target_langs) > 1:
                output_json_file_format = output_json_file_format + "_{target_lang}.json"
            else:
                output_json_file_format = output_json_file_format + ".json"

            input_json_data = json.load(open(json_file, encoding="utf-8"))
            counter_values = cls.__counter_json_values(input_json_data)
            for target_lang in target_langs:
                if not target_lang:
                    continue
                if len(target_lang) > 1:
                    output_json_file = output_json_file_format.format(target_lang=target_lang)
                else:
                    output_json_file = output_json_file_format
                output_json_filepath = os.path.join(output_json_path, output_json_file)

                with Progress() as progress:
                    task = progress.add_task("[red]Translating...", total=counter_values)

                    translated_json_data = TranslatorDeepl().translate_json(
                        input_json_data, target_lang, source_lang=source_lang, xtra_actions={"rich_progress": progress, "rich_task": task}
                    )
                json.dump(translated_json_data, open(output_json_filepath, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
                UI.print(f"Translation saved to {output_json_filepath}")
            return True
        else:
            UI.print_error(f"File not found: {json_file}")
            return False

    @classmethod
    def __counter_json_values(cls, json_data: dict, **xtra_args):
        counter = 0
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                counter += cls.__counter_json_values(value, **xtra_args)
        elif isinstance(json_data, list):
            counter += sum([cls.__counter_json_values(item, **xtra_args) for item in json_data])
        elif isinstance(json_data, str):
            return 1
        return counter
