from ion import Ion
from chemobj import ChemObj
from toolkit import index_balance, is_soulable, check_compound
from compound import Compound
from exceptions import BadCompoundException
from element import Element


class Salt(ChemObj):
    def __init__(self, metal, residue):
        i1, i2 = index_balance(metal.oxidstate, residue.oxidstate)
        self.metal = metal(count=i1, free=False)
        self.residue = residue(count=i2, free=False)
        self.label = self.metal.to_str() + self.residue.to_str()
        self.is_soulable = is_soulable(self.metal, self.residue)

    @staticmethod
    def from_compound(comp):
        check_compound(comp)
        if type(comp.elements[0]) != Element:
            raise BadCompoundException()
        elif not comp.elements[0].is_metal:
            raise BadCompoundException()
        elif not (type(comp.elements[1]) == Compound or not comp.elements[1].is_metal):
            raise BadCompoundException()
        return Salt(comp.elements[0], comp.elements[1])(count=comp.count)

    def dessolve(self):
        if self.is_soulable:
            return [
                Ion(self.metal) * self.count,
                Ion(self.residue) * self.count
            ]
        else:
            return [Ion(self)]

__all__ = [
    'Salt'
]