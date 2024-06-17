from src.classes.singleton_meta import SingletonMeta


class Translator(metaclass=SingletonMeta):
    _translator = None

    def translate(self, text, target_lang, xtra_actions, **xtra_args):
        raise NotImplementedError("You must implement this method.")

    def get_languages(self, country_code=None, country_name=None):
        raise NotImplementedError("You must implement this method.")

    def translate_json(self, input_data, target_lang, xtra_actions={}, **xtra_args):
        new_json_data = {}
        if isinstance(input_data, dict):
            for key, value in input_data.items():
                new_json_data[key] = self.translate_json(value, target_lang, xtra_actions, **xtra_args)
        elif isinstance(input_data, list):
            new_json_data = [self.translate_json(item, target_lang, xtra_actions, **xtra_args) for item in input_data]
        elif isinstance(input_data, str):
            return self.translate(input_data, target_lang, xtra_actions, **xtra_args).text
        return new_json_data
