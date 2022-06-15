from chemobj import ChemObj
from toolkit import *
from exceptions import ForbiddenOxidstateException, BadCompoundException
from MendeleevTable import O
from compound import Compound
from ion import Ion

'''
Классификация оксидов:
1. Основный (basic)
2. Амфотерный (amphoteric)
3. Кислотный (acid)
4. Несолеобразующий (non-salt-forming)
'''

non_salt_forming = [
    'N(+)', 'N(2+)', 'C(2+)'
]

class Oxide(ChemObj):
    def __init__(self, unit):
        self.count = unit.count
        if unit.is_metal:
            if 1 <= unit.oxidstate <= 2:
                self.type = 'basic'
            elif 3 <= unit.oxidstate <= 4:
                self.type = 'amphoteric'
            else:
                self.type = 'acid'
        else:
            if unit(count=1).to_str(full=True) in non_salt_forming:
                self.type = 'non_salt_forming'
            else:
                self.type = 'acid'
        
        i1, i2 = index_balance(unit.oxidstate, 2)
        self.unit = unit(count=i1, free=False)
        self.residue = O(-2, count=i2, free=False)
        self.label = self.unit.to_str() + self.residue.to_str()

    @staticmethod
    def from_compound(comp):
        check_compound(comp)
        if comp.elements[1].label != 'O':
            raise BadCompoundException()
        return Oxide(comp.elements[0])(count=comp.count)

    def dessolve(self):
        return [Ion(self)]
        
        