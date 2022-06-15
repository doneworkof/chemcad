from exceptions import ElementNotFoundException
from toolkit import *
from copy import copy


class ChemObj:
    '''Суперкласс для всех химических объектов'''

    label = 'ELEMENT' # Обозначение в формулах
    oxidstate = 0     # Степень окисления
    count = 1         # Количество элемента
    free = True       # Свободен ли элемент;
                      # Да, если у него нет родителя.

    def __call__(self, count=None, free=None):
        c = copy(self)
        if count is not None:
            c.count = count
        if free is not None:
            c.free = free
        return c
        
    def to_str(self, full=False):
        oxidstate_lbl = f'({int_to_oxidstate(self.oxidstate)})'
        count_lbl = optimized_int(self.count)
        
        if not self.free:
            el_count = count_uppercase(self.label)
            main_lbl = f'({self.label})' if el_count > 1 and count_lbl else self.label
            label = main_lbl + count_lbl
        else:
            label = count_lbl + self.label

        if full:
            label += oxidstate_lbl

        return label

    def dessolve(self):
        raise NotImplementedError()

    def __repr__(self):
        return self.to_str()

    def __mul__(self, coef: int):
        c = copy(self)
        c.count *= coef
        return c

    def __rmul__(self, coef: int):
        return self * coef

    def __imul__(self, coef: int):
        self.count *= coef
        return self

    def get_full_charge(self):
        return self.count * self.oxidstate


__all__ = [
    'ChemObj',
    'activity_row'
]