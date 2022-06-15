from chemobj import ChemObj
from math import gcd
from ion import Ion

class Compound(ChemObj): 
    def __init__(self, *elements):
        self.elements = []
        self.oxidstate = 0
        coef = gcd(*[
            el.count for el in elements
        ])
        self.count = coef
        self.label = ''
        for element in elements:
            non_free_el = element(
                count=element.count // coef,
                free=False
            )
            self.label += str(non_free_el)
            self.elements.append(non_free_el)
            self.oxidstate += non_free_el.oxidstate * non_free_el.count

    def __getitem__(self, val):
        return self.elements[val]
    
    def dessolve(self):
        return [Ion(self)]



__all__ = [
    'Compound'
]