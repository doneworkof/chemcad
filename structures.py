from compound import Compound
from MendeleevTable import *
from acid import Acid
#from hydroxide import Hydroxide

SO4 = Compound(S(6), O(-2) * 4)
SO3 = Compound(S(4), O(-2) * 3)
NO3 = Compound(N(5), O(-2) * 3)
CO3 = Compound(C(4), O(-2) * 3)
SiO3 = Compound(Si(4), O(-2) * 3)
PO4 = Compound(P(5), O(-2) * 4)
NO2 = Compound(N(3), O(-2) * 2)
OH = Compound(O(-2), H(1))

residues = [
    SO4,
    SO3,
    NO3,
    CO3,
    SiO3,
    PO4,
    NO2,
    OH,
    O(-2),
    Cl(-1),
    F(-1),
    Br(-1)
]

def get_residue_by_label(label):
    for residue in residues:
        if residue.label == label:
            return residue
    return None

# Вода
H2O = Compound(H(1) * 2, O(-2))

H2SO4 = Acid(SO4)
HCl = Acid(Cl(-1))
HBr = Acid(Br(-1))
HI = Acid(I(-1))
HNO3 = Acid(NO3)
H2SO3 = Acid(SO3)
H3PO4 = Acid(PO4)
HF = Acid(F(-1))
H2CO3 = Acid(CO3)
H2SiO3 = Acid(SiO3)
H2S = Acid(S(-2))
HNO2 = Acid(NO2)

__all__ = [
    'OH',
    'SO4',
    'SO3',
    'NO3',
    'CO3',
    'SiO3',
    'PO4',
    'NO2',
    'H2SO4',
    'HCl',
    'HBr',
    'HI',
    'HNO3',
    'H2SO3',
    'H3PO4',
    'HF',
    'H2CO3',
    'H2SiO3',
    'H2S',
    'HNO2',
    'H2O',
    'get_residue_by_label',
    'residues'
]