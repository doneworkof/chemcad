from chemobj import ChemObj
from exceptions import ForbiddenOxidstateException, ElementNotFoundException
import copy


activity_row = [
    'Li', 
    'K', 
    'Ba', 
    'Ca', 
    'Na', 
    'Mg', 
    'Al', 
    'Be', 
    'Mn', 
    'Cr', 
    'Zn',
    'Fe', 
    'Cd', 
    'Co',
    'Ni',
    'Sn',
    'Pb',
    'H',
    'Sb',
    'Cu',
    'Hg',
    'Ag',
    'Pt',
    'Au'
]


class Element(ChemObj):
    '''Класс химического элемента'''
    def __init__(self, number: int, position: tuple, label: str, is_metal: int, atomic_mass: float, molar_volume: float, possible_oxidstates: tuple, oxidstate: int=0, is_paired_simple=False, electroneg: int=-1):
        self.number = number
        self.position = position
        self.label = label
        self.possible_oxidstates = possible_oxidstates
        self.molar_volume = molar_volume
        self.is_metal = is_metal
        self.atomic_mass = atomic_mass
        self.oxidstate = oxidstate
        self.is_paired_simple = is_paired_simple
        self.electroneg = electroneg

    def is_more_active_than(self, other):
        if self.to_str() not in activity_row:
            ElementNotFoundException('element do not exist in activity row')
        return activity_row.index(self.label) < activity_row.index(other.label)
    
    def __call__(self, oxidstate=None, count=None, free=None):
        c = copy.copy(self)
        if oxidstate is not None:
            if oxidstate not in self.possible_oxidstates:
                raise ForbiddenOxidstateException('Forbidden oxidstate for ' + self.label)
            c.oxidstate = oxidstate
        if count is not None:
            c.count = count
        if free is not None:
            c.free = free
        return c

    def describe(self):
        print(f'Элемент', self.label)
        print('Тип:', 'Металл' if self.is_metal else 'Неметалл')
        print('Порядковый номер:', self.number)
        print(f'Расположение(период, группа, подгруппа):', self.position)
        print('Молярный объём:', self.molar_volume)
        print('Возможные степени окисления:', ', '.join([
            str(round(po, 2)) for po in self.possible_oxidstates
        ]))
        print('Атомная масса:', self.atomic_mass)
        print('Электроотрицательность:', self.electroneg)
        print('Простое вещество имеет индекс 2:', 'Да' if self.is_paired_simple else 'Нет')

__all__ = [
    'Element'
]