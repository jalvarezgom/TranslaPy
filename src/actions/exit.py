from src.actions.base import ActionBase


class ExitAction(ActionBase):
    msg = "Exit"
    description = None

    @classmethod
    def execute(cls, **kwargs):
        exit()
