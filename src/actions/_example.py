from src.actions.base import ActionBase


class ExampleAction(ActionBase):
    msg = "Example"
    description = "Example description"

    @classmethod
    def execute(cls, **kwargs):
        pass
