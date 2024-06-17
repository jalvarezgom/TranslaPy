class ActionBase:
    msg = None
    description = None

    @classmethod
    def execute(cls, **kwargs):
        raise NotImplementedError("Method not implemented")

    @classmethod
    def to_dict(self):
        return {"msg": self.msg, "description": self.description, "action": self.execute, "class": self}
