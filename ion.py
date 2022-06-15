from chemobj import ChemObj
from exceptions import ForbiddenChargeException
from copy import copy

class Ion(ChemObj):
    def __init__(self, obj):
        self.count = obj.count
        self.obj = obj(free=False, count=1)
        self.label = self.obj.to_str(full=True)

    def __call__(self):
        raise NotImplementedError()


__all__ = [
    'Ion'
]