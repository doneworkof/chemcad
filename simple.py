from chemobj import ChemObj
from ion import Ion


class Simple(ChemObj):
    '''Простое вещество'''
    def __init__(self, element):
        index = 2 if element.is_paired_simple else 1
        self.element = element(count=index, free=False)
        self.label = self.element.to_str()

    def dessolve(self):
        return [Ion(self)]

__all__ = [
    'Simple'
]