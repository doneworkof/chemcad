from chemobj import ChemObj
from toolkit import group_to_str, is_soulable, check_compound
from exceptions import ForbiddenOxidstateException, BadCompoundException, BadOxideException
from structures import OH
from ion import Ion


class Hydroxide(ChemObj):
    '''Гидроксид (основание)'''    
    def __init__(self, metal):
        self.count = metal.count
        self.metal = metal(count=1, free=False)
        self.residue = OH(free=False, count=metal.oxidstate)
        self.label = metal.label + self.residue.to_str()
        self.is_soulable = is_soulable(metal, self.residue)

    def dessolve(self):
        if self.is_soulable:
            return [
                Ion(self.metal) * self.count,
                Ion(self.residue) * self.count
            ]
        return [Ion(self)]

    @staticmethod
    def from_compound(comp):
        check_compound(comp)
        if not comp.elements[0].is_metal:
            raise BadCompoundException()
        elif comp.elements[1].label != 'OH':
            raise BadCompoundException()
        return Hydroxide(comp.elements[0])(count=comp.count)

    @staticmethod
    def from_oxide(oxide):
        if oxide.type != "basic" and oxide.type != "amphoteric":
            raise BadOxideException()
            
        residue = Hydroxide(
            oxide.unit(count=1)
        )
        
        return residue


__all__ = [
    'Hydroxide'
]