from hydroxide import Hydroxide
from acid import Acid
from simple import Simple
from salt import Salt
from compound import Compound
from structures import *
from MendeleevTable import *
from toolkit import *
from oxide import Oxide
from copy import copy


def Reaction(type1, type2):
    rf = reacfunc(type1, type2)
    return rf.past_init


def reaction_token(type1, type2):
    name1 = type1.__name__
    name2 = type2.__name__
    name1s, name2s = sorted([name1, name2])
    inverted = (name1s, name2s) != (name1, name2)
    return f'/{name1s}&{name2s}/', inverted


class ReactionResult:
    def __init__(self, source, result, coef):
        self.source = [
            s * c for s, c in zip(source, coef)]
        self.result = result

    def make_ion_result(self):
        return IonReactionResult(
            self.source, self.result
        )
    
    def __repr__(self):
        halfs = [
            ' + '.join([str(obj) for obj in arr])
            for arr in [self.source, self.result]
        ]
        return ' -> '.join(halfs)


class IonReactionResult:
    def __init__(self, source, result):
        self.full1 = dessolve_objects(source)
        self.full2 = dessolve_objects(result)
        self.short1 = copy(self.full1)
        self.short2 = copy(self.full2)
        idx = 0
        
        while idx < len(self.short1):
            for idx2, ion in enumerate(self.short2):
                if str(ion) == str(self.short1[idx]):
                    self.short1.pop(idx)
                    self.short2.pop(idx2)
                    break
            else:
                idx += 1
        
        divider = gcd(*[
            el.count for el in (self.short1 + self.short2)
        ])
        
        for el in (self.short1 + self.short2):
            el.count //= divider
            
    def to_str(self, short=False):
        if short:
            arr1 = self.short1
            arr2 = self.short2
        else:
            arr1 = self.full1
            arr2 = self.full2
        return ' -> '.join([
            ' + '.join([str(el) for el in arr])
            for arr in [arr1, arr2]
        ])
        
    def __repr__(self):
        return self.to_str(False)

        
class reacfunc:
    def __init__(self, type1, type2):
        self.type1 = type1
        self.type2 = type2
        self.inverted = False

    def get_types(self):
        return self.type1, self.type2

    def set_invertance(self, state):
        self.inverted = state
    
    def past_init(self, f):
        self.func = f
        return self

    def __call__(self, a, b, args_invertance):
        invert = self.inverted != args_invertance
        args = (b, a) if invert else (a, b)
        result = self.func(*args)
        if result is None:
            return None
        r, c = result
        return r, c[::-1] if invert else c


class ReactionCore:
    def __init__(self):
        self.table = {}
        
        for objname in dir(self):
            obj = getattr(self, objname)
            if type(obj) != reacfunc:
                continue
            token, is_inverted = reaction_token(*obj.get_types())
            obj.set_invertance(is_inverted)
            self.table[token] = obj
    
    def __call__(self, a, b):
        a = a(count=1)
        b = b(count=1)
        types = type(a), type(b)
        token, are_inverted = reaction_token(*types)
        if token not in self.table:
            return None
        func = self.table[token]
        return func(a, b, are_inverted)
        
    def construct(self, a, b, ion=False):
        result = self(a, b)
        if result is None:
            return None
        result = ReactionResult((a, b), *result)
        if ion:
            ion_result = result.make_ion_result()
            return result, ion_result
        return result

    @Reaction(Salt, Salt)
    def salt_salt(salt1, salt2):
        if not (salt1.is_soulable and salt2.is_soulable):
            return None
        
        c1, c2 = create_coef(
            salt1.metal,
            salt2.metal
        )
        new_salt1 = Salt(
            salt1.metal, salt2.residue
        )
        new_salt2 = Salt(
            salt2.metal, salt1.residue
        )
        
        if new_salt1.is_soulable and new_salt2.is_soulable:
            return None
        
        return (new_salt1, new_salt2), (c1, c2)

    @Reaction(Salt, Simple)
    def salt_simple(salt, simple):
        if not simple.element.is_metal:
            return None
        elif not simple.element.is_more_active_than(salt.metal):
            return None
        c1, c2 = create_coef(
            salt.metal,
            simple.element
        )
        new_salt = Salt(simple.element, salt.residue)
        new_element = c1 * salt.metal.count * Simple(salt.metal)

        return (new_salt, new_element), (c1, c2)
        
    @Reaction(Hydroxide, Oxide)
    def hydroxide_oxide(hydroxide, oxide):
        if oxide.type != 'acid':
            return None
        elif not hydroxide.is_soulable:
            return None
        
        new_residue = Compound(
            oxide.unit, oxide.residue(
                count=oxide.residue.count + 1
            )
        )

        new_salt = Salt(hydroxide.metal, new_residue)

        k = lcm(oxide.unit.count, new_salt.residue.count)
        c2 = k // oxide.unit.count
        c3 = k // new_salt.residue.count
        c1 = c3 * new_salt.metal.count
        
        c4 = c2 * oxide.residue.count + c1 * hydroxide.residue.count \
         - c3 * new_salt.residue.count * new_salt.residue[1].count
    

        return (new_salt * c3, H2O * c4), (c1, c2)
        
    @Reaction(Salt, Acid)
    def salt_acid(salt, acid):
        fch1 = salt.metal.get_full_charge()
        fch2 = acid.hydrogen.get_full_charge()
        k = lcm(fch1, fch2)
        c1 = k // fch1
        c2 = k // fch2
        metal_idx = c1 * salt.metal.count
        residue_idx = c2
        b = gcd(metal_idx, residue_idx)
        new_salt = Salt(
            salt.metal(count=metal_idx // b),
            acid.residue(count=residue_idx // b)
        ) * b
        hydrogen_idx = acid.hydrogen.count * c2
        residue_idx = salt.residue.count * c1
        f = gcd(hydrogen_idx, residue_idx)
        new_acid = Acid(
            salt.residue(count=residue_idx // f)
        ) * f

        if not (new_acid.strength < acid.strength or \
         not new_salt.is_soulable):
            return None
        
        return (new_salt, new_acid), (c1, c2)

    @Reaction(Acid, Hydroxide)
    def acid_hydroxide(acid, hydroxide):
        c1, c2 = create_coef(
            hydroxide.metal,
            acid.hydrogen
        )
        water = H2O * hydroxide.residue.count
        salt = Salt(hydroxide.metal, acid.residue)
        return (salt, water), (c1, c2)

    @Reaction(Hydroxide, Salt)
    def hydroxide_salt(hydroxide, salt):
        if not hydroxide.is_soulable:
            return None
        elif not salt.is_soulable:
            return None
        
        c1, c2 = create_coef(
            hydroxide.metal,
            salt.metal
        )
        new_hydroxide = Hydroxide.from_compound(
            Compound(
                salt.metal * c2,
                hydroxide.residue * c1
            )
        )
        new_salt = Salt.from_compound(
            Compound(
                hydroxide.metal * c1,
                salt.residue * c2
            )
        )

        if new_salt.is_soulable and new_hydroxide.is_soulable:
            return None
        
        return (new_hydroxide, new_salt), (c1, c2)

    @Reaction(Acid, Simple)
    def acid_simple(acid, simple):
        if not simple.element.is_metal:
            return None
        elif not simple.element.is_more_active_than(H):
            return None
        
        c1, c2 = create_coef(
            acid.hydrogen,
            simple.element * simple.element.count
        )
        hydr_count = c1 * acid.hydrogen.count
        if hydr_count % 2 != 0:
            c1 *= 2
            c2 *= 2
        
        hydrogen = Simple(H(1)) * (c1 * acid.hydrogen.count // 2)
        
        salt = Salt.from_compound(
            Compound(
                simple.element * c2,
                acid.residue * c1
            )
        )
        
        return (salt, hydrogen), (c1, c2)

    @Reaction(Acid, Oxide)
    def acid_oxide(acid, oxide):
        if oxide.type not in ['amphoteric', 'basic']:
            return None
        
        c1, c2 = create_coef(
            acid.hydrogen,
            oxide.unit
        )
        salt = Salt.from_compound(
            Compound(
                oxide.unit * c2,
                acid.residue * c1
            )
        )
        water = H2O * oxide.residue.count * c2
        return (salt, water), (c1, c2)

    @Reaction(Simple, Simple)
    def simple_simple(a, b):
        i1, i2 = index_balance(a.element.oxidstate, b.element.oxidstate)
        
        if a.element.is_metal and b.element.is_metal:
            return a, b
        elif a.element.is_metal:
            return (
                    (
                        Compound(
                            a.element * i1, 
                            b.element * i2
                        ),
                    ),
                    (
                        1,
                    )
            )
        elif b.element.is_metal:
            return (
                    (
                        Compound(
                            b.element * i2, 
                            a.element * i1
                        ),
                    ),
                    (
                        1,
                    )
            )
        else:
            if a.element.electroneg < b.element.electroneg:
                return (
                    (
                        Compound(
                            a.element * i1, 
                            b.element * i2
                        ),
                    ),
                    (
                        1,
                    )
                )
                    
            else:
                return (
                    (
                        Compound(
                            b.element * i2, 
                            a.element * i1
                        ),
                    ),
                    (
                        1,
                    )
                )


reactcore = ReactionCore()


def r(x, y, ion=False):
    return reactcore.construct(x, y, ion=ion)


__all__ = [
    'reactcore'
]