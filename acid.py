from chemobj import ChemObj
from MendeleevTable import H, O
from toolkit import optimized_int, check_compound
from compound import Compound
from exceptions import BadCompoundException, BadOxideException
from ion import Ion


acid_classification = {
    0: ['HF', 'HNO2', 'H2S', 'H2CO3', 'H2SiO3'],
    1: ['H2SO3', 'H3PO4'],
    2: ['HCl', 'HBr', 'HI', 'H2SO4', 'HNO3']
}


def get_acid_strength(label):
    for strength, arr in acid_classification.items():
        if label in arr:
            return strength
    return 0


class Acid(ChemObj):
    def __init__(self, residue):
        self.count = residue.count
        self.hydrogen = H(1, free=False, count=-residue.oxidstate)
        self.residue = residue(count=1, free=False)
        self.label = self.hydrogen.to_str() + residue.label
        self.strength = get_acid_strength(self.label)

    @staticmethod
    def from_oxide(oxide):
        if oxide.type != "acid":
            raise BadOxideException()
        residue = Compound(
            oxide.unit,
            O(-2) * (oxide.residue.count + 1)
        )
        
        return Acid(residue)

    def dessolve(self):
        if self.strength == 2:
            return [
                Ion(self.hydrogen) * self.count,
                Ion(self.residue) * self.count
            ]
        else:
            return [Ion(self)]

    @staticmethod
    def from_compound(comp):
        check_compound(comp)
        if comp.elements[0].label != 'H':
            raise BadCompoundException()
        elif not (type(comp.elements[1]) == Compound or \
        not comp.elements[1].is_metal):
            raise BadCompoundException()
        return Acid(comp.elements[1])(count=comp.count)
        
__all__ = [
    'Acid'
]