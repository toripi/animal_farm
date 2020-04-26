"""An animal base class."""


class Animal():
    """Animal"""

    def __init__(self, kind):
        self.kind = kind

    def get_kind(self):
        """get_kind"""
        return self.kind
